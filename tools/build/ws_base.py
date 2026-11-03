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


def tidy(line: str, norm=None) -> str:
    # the service escapes markup characters ("&lt;&lt;Autoritatea ...&gt;&gt;"); «…» as parse.py reads "<<…>>"
    line = html.unescape(line).replace('<<', '«').replace('>>', '»')
    # the publisher's footnote run into the text ("... la prezenta hotărâre. *) Anexele nr. 1-6 se publică în Monitorul
    # Oficial ... bis"): not text, as parse.py leaves "*) ..." notes out; then the marker itself ("nr. 1-6 *) la")
    line = re.sub(r'(?<=[.;:])\s*\*{1,4}\)\s.*$', '', line)
    line = re.sub(r'\s*\*{1,4}\)', '', line)
    if norm:  # parse.py's own normalisation (quotes, dashes, spaces), so the text is the one a page would give
        line = norm(line)
    line = re.sub(r'[ \t]{2,}', ' ', line.replace('\xa0', ' '))
    line = re.sub(r' +([.,;:)\]])', r'\1', line)  # the space the service leaves after linked text
    line = re.sub(r'([(\[]) +', r'\1', line)
    return line.strip()


def base_units(text: str, pad: int = 3, norm=None) -> dict:
    """Units of the act as published: the article split of ws_units, each body re-cut into its paragraphs."""
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
        lines = [tidy(x, norm) for x in body.split('\n')]
        out[k] = {'label': label, 'kind': 'art', 'text': '\n'.join([head] + [x for x in lines if x]) + '\n'}
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
