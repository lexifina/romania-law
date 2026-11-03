"""Split a FreeWebService document text (the act as published, plain text) into articles, in the corpus unit format.

    from ws_units import units_of
    units = units_of(text)   # {'art-001': {'label': 'Art. 1', 'text': '# Articolul 1\\n...'}, ...}

The service prints each structural item after a "\\xa0+\\xa0" marker line, and articles as "Articolul N" (also
"Articolul N^M", "Articolul unic"). Headings (Titlul, Capitolul, Secțiunea) are not text, as in parse.py. Text is
normalised the way parse.py does it (comma-below ș/ț, no-break spaces, collapsed spaces). One line per paragraph.

"""
import re
import sys

ART = re.compile(r'^\s*Art(?:icol(?:ul)?|\.)\s+(unic|\d+|[IVXLC]+(?![\w]))(?:\s*\^\s*(\d+))?\s*\.?\s*(?:-\s*)?(.*)$', re.I)
ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def roman_value(r: str) -> int:
    v = [ROMAN[c] for c in r.upper()]
    return sum(-x if i + 1 < len(v) and x < v[i + 1] else x for i, x in enumerate(v))
HEAD = re.compile(r'^\s*(Titlul|Capitolul|Sec[țţ]iunea|Cartea|Partea|Paragraful|Anexa|ANEXA|§)\b', re.I)
SUBHEAD = re.compile(r'^[a-z]\)\s+[A-ZĂÂÎȘȚ][^.;:]{0,70}$')  # a lettered sub-heading run onto the end of the article before
TAIL = re.compile(r'^\s*(Aceast[ăa] lege a fost adoptat|PRIM-MINISTRU|PREȘEDINTELE|PRESEDINTELE|Contrasemneaz|NOT[ĂA]\b)', re.I)
# The service prints a paragraph's run on one line, so the signature block often follows the last words of the last
# article on the same line: cut there too (case-sensitive, as the automatic pass's checker: SIGN_SPLIT_RE)
TAIL_MID = re.compile(r'\bPRIM-MINISTRU\b|\bAceast[ăa] lege a fost adoptat[ăa]\b|\bPRE[ȘS]EDINTELE CAMEREI DEPUTA[ȚT]ILOR\b')
# The act's EU-transposition note: cut only from the end of the last article, when short (as the checker's EU_NOTE_RE)
EU_NOTE = re.compile(r'\*?\s*Prezenta (?:lege|ordonanță(?: de urgență)?|ordonanta(?: de urgenta)?|hotărâre|hotarare) '
                     r'(?:transpune|asigură transpunerea|asigura transpunerea)\b')


def norm(s: str) -> str:
    s = s.replace('\xa0', ' ').replace('ş', 'ș').replace('ţ', 'ț').replace('Ş', 'Ș').replace('Ţ', 'Ț')
    s = s.replace('\ufeff', '').replace('“', '”').replace('–', '-').replace('—', '-')
    return re.sub(r'[ \t]+', ' ', s).strip()


def _is_roman(num: str) -> bool:
    return num.lower() != 'unic' and not num.isdigit()


# An amending act's numbered points run on after the sentence before them ("... se abrogă. 14. La articolul 25, ..."):
# each is a paragraph of its own, as the page prints it (Roman-numbered acts only: they are the amending acts)
POINT_SPLIT = re.compile(r'(?<=[.;:"”»])[ \t]+(?=\d{1,3}(?:\^\d+)?\.[ \t]+(?:La|Articolul|Articolele|După|Alineatul|'
                         r'Alineatele|Anexa|Anexele|Punctul|Punctele|Litera|Literele|Titlul|Capitolul|Partea|Secțiunea|'
                         r'Denumirea|Cuprinsul|Sintagma|Textul|În|Nota|Preambulul|Formula)\b)')


def _roman_units(blocks: list, pad: int) -> dict:
    """Units of an act whose own articles are numbered in Roman numerals (an amending act): every block after a Roman
    article, until the next one, is that article's text as the page prints it (the quoted articles "Articolul 4",
    the quoted annexes "Anexa nr. 2 la Hotărârea ..."), not an article or heading of the act's own."""
    units: dict = {}
    cur = None
    last_own = 0  # the act's own series: I, II, III ... in order
    prev_end = ''  # the last line of the block before ("... va avea următorul cuprins:" introduces a quotation)
    for b in blocks[1:]:
        lines = [norm(x) for x in b.split('\n') if norm(x)]
        if not lines:
            continue
        m = ART.match(lines[0])
        own = False
        if m and _is_roman(m.group(1)) and not m.group(2):
            v = roman_value(m.group(1).upper())
            # an own article is the next number of the act's series, unless the block before introduces a quotation
            # ("... va avea următorul cuprins:"; a plain "după cum urmează:" opens the act's own list, legea-71-2024);
            # any other Roman heading is an article the act quotes from another act (legea-17-2022 quotes
            # "Articolul VI"), kept in the text of the article quoting it, as for Arabic quoted articles
            own = v == last_own + 1 and not re.search(r'cuprins\s*:$', prev_end)
        prev_end = lines[-1]
        if own:
            num, rest = m.group(1).upper(), m.group(3)
            last_own = roman_value(num)
            cur = f'art-{last_own:0{pad}d}'
            units[cur] = {'label': f'Articolul {num}', 'lines': []}
            lines = ([rest] if rest else []) + lines[1:]
        elif cur is None:
            continue  # before the first article (headings), after a repeated number, or after the signatures
        for ln in lines:
            # the elision dots of a partial quotation ("........") are a line of their own, as the page prints them
            parts = [p for x in POINT_SPLIT.split(ln) for p in re.split(r'[ \t]*(\.{6,}|…{2,})[ \t]*', x) if p.strip()]
            for part in parts:
                if TAIL.match(part):  # the signatures (or a note) end this article; the next Roman one opens again
                    cur = None
                    break
                mid = TAIL_MID.search(part)
                if mid:
                    if part[:mid.start()].strip():
                        units[cur]['lines'].append(part[:mid.start()].strip())
                    cur = None
                    break
                units[cur]['lines'].append(part)
            if cur is None:
                break
    # the EU-transposition note stays: the pages of these acts print it in their last article
    return {k: {'label': u['label'], 'text': '\n'.join([f'# {u["label"]}'] + u['lines']) + '\n'} for k, u in units.items()}


def units_of(text: str, pad: int = 3) -> dict:
    blocks = re.split(r'\n\s*\xa0?\+\xa0?\s*\n', text.replace('\r', ''))
    first = next((m for b in blocks[1:] for m in [ART.match(norm(b.split('\n')[0]) if b.strip() else '')] if m), None)
    if first and _is_roman(first.group(1)):  # the act numbers its own articles I, II, ...
        return _roman_units(blocks, pad)
    units: dict = {}
    pending = None  # a short sub-heading block ("a) Prin naștere"): the next article's marginal title, as in parse.py
    for b in blocks[1:]:  # block 0 is the act's header (title, issuer, publication, preamble)
        lines = [norm(x) for x in b.split('\n') if norm(x)]
        if not lines:
            continue
        m = ART.match(lines[0])
        if m and _is_roman(m.group(1)):
            m = None  # a Roman number quoted in an Arabic-numbered act: handled as before Roman numbers were read
        if not m:
            joined = ' '.join(lines)
            pending = None if HEAD.match(lines[0]) or len(joined) > 160 else joined
            continue  # structural headings (Titlul/Capitolul/…) are not text
        num, sup, rest = m.group(1), m.group(2), m.group(3)
        key = 'art-unic' if num.lower() == 'unic' else f'art-{int(num):0{pad}d}' + (f'-{int(sup)}' if sup else '')
        label = 'Articolul unic' if num.lower() == 'unic' else f'Articolul {int(num)}' + (f'^{sup}' if sup else '')
        body = ([pending] if pending else []) + ([rest] if rest else []) + lines[1:]
        pending = None
        out = []
        for ln in body:
            if TAIL.match(ln) or HEAD.match(ln):
                break
            mid = TAIL_MID.search(ln)
            if mid:
                if ln[:mid.start()].strip():
                    out.append(ln[:mid.start()].strip())
                break
            out.append(ln)
        if out and SUBHEAD.match(out[-1]):
            pending = out.pop()  # it heads the next article (its marginal title), not this one
        if key in units:
            continue  # the first print of a number wins (quoted copies come later)
        units[key] = {'label': label, 'text': '\n'.join([f'# {label}'] + out) + '\n'}
        last = key
    if units:
        t = units[last]['text']
        body_start = t.index('\n') + 1
        m = EU_NOTE.search(t, body_start)
        if m and m.start() > body_start and len(t[m.start():].split()) <= 120:
            units[last]['text'] = t[:m.start()].rstrip() + '\n'
    return units

