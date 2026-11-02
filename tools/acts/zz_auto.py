"""Acts added by Lexifina's automatic pass (default rules only), registered from acts/auto/registry.json.

Each registry entry is an ACTS entry without the Phase 6 defaults, which are added here; its forms manifest is
forms.d/auto/<slug>.json (read by parse.py for entries with 'auto'). An act that already has an ACTS entry (a
hand-built act) is never redefined: its registry entry is skipped. This module loads last (file-name order).
"""
import json
from pathlib import Path

REGISTRY = Path(__file__).resolve().parent / 'auto' / 'registry.json'


def register(P):
    if not REGISTRY.exists():
        return
    entries = json.loads(REGISTRY.read_text(encoding='utf-8'))
    added = []
    for slug, entry in sorted(entries.items()):
        if slug in P.ACTS:
            continue
        P.ACTS[slug] = {**P.P6, **entry, 'auto': True}
        added.append(slug)
    P.PHASE6 = P.PHASE6 + tuple(added)
    P.PHASE2 = P.PHASE2 + tuple(added)
