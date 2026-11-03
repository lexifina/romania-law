"""law_labels.json: {law key: label} as the verified parts give it, for parse.py to label every new part the same way.

    python -X utf8 tools/law_labels.py [RO folder]

Reads every part in corpus.d that has a .PUBLISH, in file-name order (the order the corpus build merges them), and
keeps the first label each law key has. The build refuses a part that gives a key another label, so once a key's label
is verified, parse.py gives it in every new part too (an amending law may be "Legea-cadru nr. 153/2017" in its own part
and "Legea nr. 153/2017" in another act's notes). Keys with two labels among the verified parts are listed on stderr.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def build(ro: Path) -> tuple[dict, dict]:
    labels: dict[str, str] = {}
    clash: dict[str, set] = {}
    for p in sorted((ro / 'corpus.d').glob('*.json')):
        if not p.with_suffix('.PUBLISH').exists():
            continue
        for k, law in json.loads(p.read_text(encoding='utf-8')).get('laws', {}).items():
            lab = law.get('label')
            if not lab:
                continue
            if k in labels and labels[k] != lab:
                clash.setdefault(k, {labels[k]}).add(lab)
            labels.setdefault(k, lab)
    return dict(sorted(labels.items())), clash


def main(args: list[str]) -> None:
    ro = Path(args[0]) if args else Path(__file__).resolve().parent.parent
    labels, clash = build(ro)
    out = ro / 'law_labels.json'
    text = json.dumps(labels, ensure_ascii=False, indent=0) + '\n'
    if out.exists() and out.read_text(encoding='utf-8') == text:
        print(f'{out.name}: {len(labels)} keys, unchanged')
    else:
        tmp = out.with_suffix('.json.tmp')
        tmp.write_text(text, encoding='utf-8', newline='\n')
        os.replace(tmp, out)
        print(f'{out.name}: {len(labels)} keys written')
    for k, labs in sorted(clash.items()):
        print(f'two labels for {k}: {sorted(labs)} (kept {labels[k]!r})', file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1:])
