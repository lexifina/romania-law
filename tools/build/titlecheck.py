"""titlecheck.py: the standard pre-check for a candidate act, run before writing its ACTS entry or parsing it.
usage: python -X utf8 titlecheck.py <slug>   (reads the cache only: forms.json must hold the act; no requests)

Reads every held form's article titles (S_ART_TTL) in parse.py's load() order: the root's Afis republication is read
only for republication entries, never for the newest form. For each article a form leaves out (outside a
republication, which renumbers), it reports whether that form prints a repeal note for it and in which later form the
article comes back. Every "GAP" line must be settled by the drop rule (see PROGRESS.md) before the act is built.
(Phase 7's fixed copy of the Phase 5 script; made the standard pre-check in Phase 8.)"""
import sys, json, re, html
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import parse as P
slug = sys.argv[1]
m = json.loads((P.HERE / 'forms.json').read_text(encoding='utf-8'))[slug]
newest = max(f['date'] for f in m['forms'])
miss = set(m.get('missing', []))
forms = sorted((f for f in m['forms'] if f['id'] not in miss
                and (f['id'] != m['root'] or f['date'] == newest or (f['kind'] == 'republicare' and f['id'] in m.get('afis_ia', {})))),
               key=lambda f: (f['date'], int(f['id'])))  # as parse.py's load()
sts = []
for f in forms:
    if f['kind'] == 'republicare' and f['id'] in m.get('afis_ia', {}):
        key = P.archive_url(f['id'], m['afis_ia'][f['id']], True)
    else:
        try:
            _, key, _ = P.page_for(slug, f, m)
        except SystemExit as e:
            print('  skip', f, e); continue
    raw = P.cached(key).decode('utf-8', 'replace')
    t = [P.norm(html.unescape(re.sub(r'<[^>]+>', '', x))) for x in re.findall(r'<span class="S_ART_TTL"[^>]*>(.*?)</span>', raw, re.S)]
    arts = {re.sub(r'\s+', '', x[len('Articolul'):]).rstrip('.') for x in t if x.startswith('Articolul')}
    sts.append((f, arts, P.plain_text(raw.encode('utf-8'))))
print(slug, len(forms), 'forms held,', len(sts), 'read:', ' '.join(f"{f['date']}{'R' if f['kind']=='republicare' else ''}:{len(a)}" for f, a, _ in sts))
bad = 0
for i, ((pf, pa, _), (f, a, plain)) in enumerate(zip(sts, sts[1:]), 1):
    if f['kind'] == 'republicare':
        print(f"  {f['date']} {f['id']} republication: {len(pa - a)} numbers gone, {len(a - pa)} new")
        continue
    for n in sorted(pa - a):
        note = re.search(rf'(?:Art\.|Articolul) {re.escape(n)}\b[^.]{{0,60}}?(?:a fost|au fost) (?:abrogat|eliminat)', plain)
        back = next((g for g, b, _ in sts[i + 1:] if n in b), None)
        bad += not note
        print(f"  {f['date']} {f['id']} drops art. {n}: note in form: {bool(note)}; back in: {back['date'] + ' ' + back['id'] if back else '-'}{'' if note else '  <-- GAP'}")
print(slug, 'articles dropped with no note in the form:', bad)
