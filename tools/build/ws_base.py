"""The act as published, from the official web service's text, in the units format parse.py writes (byte for byte
where the two agree): one line per paragraph, "# Articolul N" first, single spaces, no space before punctuation.

    from ws_base import base_units
    units = base_units(text, pad=3)       # {'art-001': {'label': 'Art. 1', 'text': '# Articolul 1\\n...'}}

    python -X utf8 ws_base.py --test       # byte agreement with published automatic parts whose words already agree

The service prints an article's paragraphs on one line, separated by runs of spaces (or "\\xa0...\\xa0"), and a space
on each side of linked text ("anexa nr. 1 ."); both are undone here. Article splitting, headings, tails and the
EU-transposition cut are ws_units.py's.
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ws_units as WU  # noqa: E402

PARA = re.compile(r'(?:\s*\xa0\.\.\.\xa0\s*|\s{3,})(?=\(\d+(?:\^\d+)?\)|[a-z]\)\s|\d+(?:\^\d+)?\.\s|[A-ZĂÂÎȘȚ"„«*-])')
# a paragraph's own label ("(1)", "a)", "3.") at a paragraph start, then the service's run of spaces before its text
LABEL_GAP = re.compile(r'(^|\s{3,}|\xa0\.\.\.\xa0\s*)(\(\d+(?:\^\d+)?\)|[a-z]\)|\d+(?:\^\d+)?\.)\s{2,}', re.M)


def tidy(line: str, norm=None, star_text: bool = False) -> str:
    # the service escapes markup characters ("&lt;&lt;Autoritatea ...&gt;&gt;"); «…» as parse.py reads "<<…>>"
    line = html.unescape(line).replace('<<', '«').replace('>>', '»')
    # the publisher's footnote run into the text ("... la prezenta hotărâre. *) Anexele nr. 1-6 se publică în Monitorul
    # Oficial ... bis"): not text, as parse.py leaves "*) ..." notes out; then the marker itself ("nr. 1-6 *) la")
    # Lexifina ('ws_star_text', per act, off by default; HG nr. 542/2023): the act's "*) ..." text is kept as printed
    # (a note the amending act quotes: 'nota ... va avea următorul cuprins: *) Se confecționează ...')
    if not star_text:
        line = re.sub(r'(?<=[.;:])\s*\*{1,4}\)\s.*$', '', line)
        line = re.sub(r'\s*\*{1,4}\)', '', line)
    if norm:  # parse.py's own normalisation (quotes, dashes, spaces), so the text is the one a page would give
        line = norm(line)
    line = re.sub(r'[ \t]{2,}', ' ', line.replace('\xa0', ' '))
    line = re.sub(r' +([.,;:)\]])', r'\1', line)  # the space the service leaves after linked text
    line = re.sub(r'([(\[]) +', r'\1', line)
    return line.strip()


BLOCK_SEP = re.compile(r'(\n\s*\xa0?\+\xa0?\s*\n)')  # ws_units' block split, separators kept
QUOTE_INTRO = re.compile(r':\s*["„«]?$')  # "... va avea următorul cuprins:" ends the block before a quoted article
QMARK = '\x00Q{}\x00'
QHEAD = re.compile(r'^\s*((?i:art(?:icol(?:ul)?|\.))\s+\d+(?:\s*\^\s*\d+)?[a-z]?)(?=\s|\.|-|$)\.?')


def fold_quoted(raw: str) -> tuple:
    """Lexifina ('ws_quoted', per act, off by default): the service prints each article an amending act quotes after
    a "+" marker of its own, as if it were one of the act's own articles ("ARTICOL UNIC ... art. 4, cu următorul
    cuprins:" + "Articolul 4 ..."). An own article is "Articolul unic" (the first article block) or the next number of
    the act's own series 1, 2, 3 ..., printed after a block that does not end in ":"; every other block after the first
    own article (an article with another number or an "^" number, a heading of the quoted text) up to the signature is
    text of the own article before it, kept in its place as a marker line that base_units expands. A heading block
    is the act's own heading (left out, as ws_units does) when the next article block is an own article. The blocks
    after the signature (the annexes) are left out. Returns the folded text and {marker: quoted lines}."""
    parts = BLOCK_SEP.split(raw)
    heads = []  # per block: (ART match or None, first line, previous block ends ":")
    for j in range(2, len(parts), 2):
        lines = [WU.norm(x) for x in parts[j].split('\n') if WU.norm(x)]
        prev = [WU.norm(x) for x in parts[j - 2].split('\n') if WU.norm(x)]
        heads.append((WU.ART.match(lines[0]) if lines else None, lines,
                      bool(prev and QUOTE_INTRO.search(prev[-1]))))
    out, quoted = [parts[0]], {}
    want, unic, own_seen = 1, False, False

    def is_own(i):
        m, lines, q = heads[i]
        if not m or q or unic:
            return False
        if m.group(1).lower() == 'unic':
            return not own_seen
        return not m.group(2) and int(m.group(1)) == want

    for i, (m, lines, q) in enumerate(heads):
        sep, block = parts[2 * i + 1], parts[2 * i + 2]
        if not lines:
            out += [sep, block]
            continue
        if is_own(i):
            own_seen = True
            if m.group(1).lower() == 'unic':
                unic = True
            else:
                want += 1
            out += [sep, block]
        elif not own_seen:
            out += [sep, block]
        else:
            if not m and not q:  # a heading: the act's own when the next article block is an own article
                nxt = next((n for n in range(i + 1, len(heads)) if heads[n][0]), None)
                if nxt is not None and is_own(nxt) or HEAD_ANNEX.match(lines[0]):
                    out += [sep, block]
                    continue
            body = lines
            if m:  # "Articolul 4  Localitățile ...": the quoted article's heading on a line of its own
                h = QHEAD.match(lines[0])  # with a letter as printed ("Articolul 295^28a")
                head = h.group(1) if h else lines[0][:len(lines[0]) - len(m.group(3))].strip().rstrip('-').strip()
                rest = lines[0][len(h.group(0)):].strip().lstrip('-').strip() if h else m.group(3)
                body = [head] + ([rest] if rest else []) + lines[1:]
            keep, end = [], False
            for ln in body:
                mid = WU.TAIL_MID.search(ln)
                if mid:
                    if ln[:mid.start()].strip():
                        keep.append(ln[:mid.start()].strip())
                    end = True
                    break
                keep.append(ln)
            mark = QMARK.format(len(quoted))
            quoted[mark] = keep
            out[-1] = out[-1].rstrip('\n') + '\n' + mark + '\n'
            if end:  # the signature: what follows (the annexes) is not the act's text
                break
        if WU.TAIL_MID.search(block):
            break
    return ''.join(out), quoted


HEAD_ANNEX = re.compile(r'^\s*(Anex[aăe]|ANEX[AĂE])\b')


def base_units(text: str, pad: int = 3, norm=None, quoted: bool = False, star_text: bool = False) -> dict:
    """Units of the act as published: the article split of ws_units, each body re-cut into its paragraphs.
    `quoted` (an entry's 'ws_quoted'): the articles an amending act quotes stay in the article quoting them
    (fold_quoted). `star_text` (an entry's 'ws_star_text'): "*) ..." runs and markers are kept (tidy)."""
    raw = text.replace('\r', '').replace('\xa0...\xa0', '\n')  # the service's paragraph separator, where it prints one
    # a paragraph label followed by the service's gap ("urmează:  a)    nava") starts a paragraph wherever it stands
    raw = re.sub(r'[ \t]{2,}(\(\d+(?:\^\d+)?\)|[a-z]\)|\d+(?:\^\d+)?\.)[ \t]{3,}', r'\n\1 ', raw)
    raw = LABEL_GAP.sub(lambda m: m.group(1) + m.group(2) + ' ', raw)  # "(1)    Elevii" -> "(1) Elevii"
    # list items the service runs on after ";" or ":" with a single space ("...; 2. elaborează", "...; - acceptarea",
    # "cerințe: (i) să fie"): each item is a line of its own, as the page prints it
    raw = re.sub(r'([;:])[ \t]+(?=(?:-[ \t]|\*[ \t]|\d{1,3}(?:\^\d+)?\.[ \t]|\([ivxlc]{1,6}\)[ \t]|\(\d{1,3}\)[ \t]|'
                 r'[a-z]\)[ \t]))', r'\1\n', raw)
    # an amending act's quoted text: it opens a line after "... cuprins:", and the next numbered point after the closing
    # quote opens another ('cuprins: "29. - ..." 2. La litera B')
    raw = re.sub(r'(cuprins:|următoarele:|astfel:)[ \t]+(?=["„«])', r'\1\n', raw)
    raw = re.sub(r'(["”»])[ \t]+(?=\d{1,3}(?:\^\d+)?\.[ \t][A-ZĂÂÎȘȚ])', r'\1\n', raw)
    # re-cut every article block's run-on line into paragraphs before ws_units splits and tidies the blocks
    raw = '\n'.join(PARA.sub('\n', ln) if not re.match(r'^\s*\xa0?\+\xa0?\s*$', ln) else ln for ln in raw.split('\n'))
    qmap = {}
    if quoted:
        raw, qmap = fold_quoted(raw)
    units = WU.units_of(raw, pad)
    unic = re.search(r'\b(Art(?:icol(?:ul)?)?\.?\s+unic)\b', raw, re.I)
    out = {}
    for k, u in units.items():
        head, _, body = u['text'].partition('\n')
        label = u['label'].replace('Articolul ', 'Art. ')
        if k == 'art-unic':
            # as parse.py: the single article is art-001, its heading and label as printed ("ARTICOL UNIC")
            k = f'art-{1:0{pad}d}'
            printed = re.sub(r'\s+', ' ', unic.group(1)) if unic else 'Articol unic'
            head, label = f'# {printed}', printed
        blines = body.split('\n')
        if qmap:  # each marker line: the quoted text it stands for
            blines = [y for x in blines for y in qmap.get(x.strip(), [x])]
        lines = [tidy(x, norm, star_text) for x in blines]
        out[k] = {'label': label, 'kind': 'art', 'text': '\n'.join([head] + [x for x in lines if x]) + '\n'}
    if qmap and out:  # ws_units' cut of the act's EU-transposition note, now on the last article's whole text
        last = list(out)[-1]
        t = out[last]['text']
        body_start = t.index('\n') + 1
        m = WU.EU_NOTE.search(t, body_start)
        if m and m.start() > body_start and len(t[m.start():].split()) <= 120:
            # with the note's own marker ("*** Prezenta hotărâre transpune ..."), not left as a line of its own
            out[last]['text'] = re.sub(r'\n\*{1,4}$', '', t[:m.start()].rstrip()) + '\n'
    return out


if __name__ == '__main__' and '--test' in sys.argv:
    import glob
    import gzip
    import json
    here = Path(__file__).resolve().parent
    ro = r'~\Documents\lexifina\scripts\romania-law'
    import importlib.util
    _spec = importlib.util.spec_from_file_location('ro_parse_for_test', ro + r'\parse.py')
    _P = importlib.util.module_from_spec(_spec)
    sys.modules['ro_parse_for_test'] = _P
    _spec.loader.exec_module(_P)  # parse.py's norm, as parse.py passes it
    rows = [json.loads(l) for l in open(here / 'audit-ws.jsonl', encoding='utf-8')]
    ident = [r for r in rows if r['both'] and r['same'] == r['both'] and not r['only_part'] and not r['only_ws']]
    byte = tot = acts_all = 0
    diffs = []
    for r in ident:
        mine = json.load(open(glob.glob(ro + rf"\corpus.d\au-{r['slug']}.json")[0], encoding='utf-8'))['acts'][0]['versions'][0]['units']
        ws = base_units(gzip.decompress((here / 'ws-text' / f"{r['ws_id']}.txt.gz").read_bytes()).decode('utf-8'),
                        norm=_P.norm)
        if 'art-unic' in ws and 'art-001' in mine:
            ws['art-001'] = ws.pop('art-unic')
        ok_all = True
        for k in mine:
            tot += 1
            if k in ws and mine[k]['text'] == ws[k]['text']:
                byte += 1
            else:
                ok_all = False
                if len(diffs) < int(sys.argv[sys.argv.index('--test') + 1]) if len(sys.argv) > 2 else 4:
                    diffs.append((r['slug'], k, mine[k]['text'], ws.get(k, {}).get('text', '')))
        acts_all += ok_all
    print(f'byte-identical units {byte}/{tot} ({100 * byte / max(tot, 1):.1f}%); acts with every unit identical '
          f'{acts_all}/{len(ident)}')
    import difflib
    for s, k, a, b in diffs:
        print('==', s, k)
        for d in difflib.ndiff(a.splitlines(), b.splitlines()):
            if d[0] in '+-?':
                print('   ', d[:200])
