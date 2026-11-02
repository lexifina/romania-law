"""Legea nr. 187/2012 pentru punerea în aplicare a Legii nr. 286/2009 privind Codul penal (Lexifina, 2026-11-02). Draft, held."""
SLUG = 'legea-187-2012'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-187-2012', 'short': 'Legea nr. 187/2012', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'trailing_notes': True, 'reprint_law': True,
        'title': 'Legea nr. 187/2012 pentru punerea în aplicare a Legii nr. 286/2009 privind Codul penal',
        'url': P.PORTAL + 'DetaliiDocument/142722',
        'in_force': '2012-11-15', 'first_law': SLUG,
        'base_note': '',
        'form_note': {}, 'republished': {},
        'hold': True,
        'decisions': [],
        'repeal_acts': {},
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
