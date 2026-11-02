"""Legea nr. 346/2004 on stimulating the founding and development of small and medium-sized enterprises: Lexifina,
2026-11-02.

Act page 215250 (form 28.06.2019); the base text is DetaliiDocumentAfis/53946. 19 forms 27.08.2004 .. 12.12.2025: 18 held
from Common Crawl, the form of 12.12.2025 from its DetaliiDocumentAfis page (forms.d/legea-346-2004.json)."""

SLUG = 'legea-346-2004'
TITLE = 'Legea nr. 346/2004 privind stimularea înființării și dezvoltării întreprinderilor mici și mijlocii'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-346-2004', 'short': 'Legea nr. 346/2004', 'pad': 3, 'cc_forms': True,
        'trailing_notes': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/215250',
        'in_force': '2004-08-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 681 of 29 July 2004; it sets no day of its own, so '
                     'in force 3 days after publication (Constituția art. 78): 1 August 2004.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 346/2004: the first version is the law as published in Monitorul Oficial nr. 681 of 29 July '
            '2004 (DetaliiDocumentAfis/53946), dated 1 August 2004: it sets no in-force day of its own, so 3 days '
            'after publication (Constituția art. 78). The portal\'s first consolidated form is of 27 August 2004, so '
            'the changes made up to then arrive together that day.',
        ],
        'repeal_acts': {},
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 346/2004', 'kind': 'law',
        'title': 'Legea nr. 346 din 14 iulie 2004 privind stimularea înființării și dezvoltării întreprinderilor mici '
                 'și mijlocii, publicată în Monitorul Oficial al României, Partea I, nr. 681 din 29 iulie 2004',
        'enacted': '2004-07-14', 'published': '2004-07-29', 'url': P.PORTAL + 'DetaliiDocumentAfis/53946',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
