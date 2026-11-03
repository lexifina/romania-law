"""Split a FreeWebService document text (the act as published, plain text) into articles, in the corpus unit format.

    from ws_units import units_of
    units = units_of(text)   # {'art-001': {'label': 'Art. 1', 'text': '# Articolul 1\\n...'}, ...}

The service prints each structural item after a "\\xa0+\\xa0" marker line, and articles as "Articolul N" (also
"Articolul N^M", "Articolul unic"). Headings (Titlul, Capitolul, Secțiunea) are not text, as in parse.py. Text is
normalised the way parse.py does it (comma-below ș/ț, no-break spaces, collapsed spaces). One line per paragraph.

"""
import re
import sys

ART = re.compile(r'^\s*Art(?:icol(?:ul)?|\.)\s+(unic|\d+)(?:\s*\^\s*(\d+))?\s*\.?\s*(?:-\s*)?(.*)$', re.I)
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


def units_of(text: str, pad: int = 3) -> dict:
    blocks = re.split(r'\n\s*\xa0?\+\xa0?\s*\n', text.replace('\r', ''))
    units: dict = {}
    pending = None  # a short sub-heading block ("a) Prin naștere"): the next article's marginal title, as in parse.py
    for b in blocks[1:]:  # block 0 is the act's header (title, issuer, publication, preamble)
        lines = [norm(x) for x in b.split('\n') if norm(x)]
        if not lines:
            continue
        m = ART.match(lines[0])
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

