"""Legea nr. 255/2013 pentru punerea în aplicare a Legii nr. 135/2010 privind Codul de procedură penală și pentru modificarea și completarea unor acte normative care cuprind dispoziții procesual penale (Lexifina, 2026-11-02). Draft, held."""
SLUG = 'legea-255-2013'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-255-2013', 'short': 'Legea nr. 255/2013', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'trailing_notes': True, 'reprint_law': True,
        'title': 'Legea nr. 255/2013 pentru punerea în aplicare a Legii nr. 135/2010 privind Codul de procedură penală și pentru modificarea și completarea unor acte normative care cuprind dispoziții procesual penale',
        'url': P.PORTAL + 'DetaliiDocument/150697',
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
