"""Legea nr. 76/2012 pentru punerea în aplicare a Legii nr. 134/2010 privind Codul de procedură civilă (Lexifina,
2026-11-02). Draft, held.
"""
SLUG = 'legea-76-2012'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-76-2012', 'short': 'Legea nr. 76/2012', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'trailing_notes': True, 'reprint_law': True,
        'title': 'Legea nr. 76/2012 pentru punerea în aplicare a Legii nr. 134/2010 privind Codul de procedură civilă',
        'url': P.PORTAL + 'DetaliiDocument/138484',
        'in_force': '2012-06-02', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 365 of 30 May 2012.',
        'form_note': {}, 'republished': {},
        'hold': True,
        'decisions': [],
        'repeal_acts': {},
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
