"""Legea nr. 295/2004 privind regimul armelor și al munițiilor (Lexifina, 2026-11-02).

Act page 53150, also the text as published (DetaliiDocumentAfis/53150). 23 forms 30.12.2004 .. 02.11.2025 are listed
(forms.d/legea-295-2004.json) and all are held. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-295-2004'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-295-2004', 'short': 'Legea nr. 295/2004', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'root_word': 'act page',
        'title': 'Legea nr. 295/2004 privind regimul armelor și al munițiilor',
        'url': P.PORTAL + 'DetaliiDocument/53150',
        'in_force': '2004-12-30', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 583 of 30 June 2004, in force 6 months after '
                     'publication (its art. 145): 30 December 2004.',
        'form_note': {
            '132994': 'The law as republished on 17 November 2011 under art. VII of Legea nr. 117/2011.',
            '158882': 'The law as republished on 10 June 2014 under art. 248 of Legea nr. 187/2012.'},
        'republished': {'132994': 'legea-117-2011', '158882': 'legea-187-2012'},
        'decisions': [
            'Legea nr. 295/2004: the first version is the law as published in Monitorul Oficial nr. 583 of 30 June '
            '2004 (DetaliiDocumentAfis/53150), dated 30 December 2004: its art. 145 puts it in force 6 months after '
            'publication.',
            'Legea nr. 295/2004: the republication of 17 November 2011 (132994) is credited, for the changes no note '
            'explains, to Legea nr. 117/2011, under whose art. VII it was republished, as its own note says.',
            'Legea nr. 295/2004: the republication of 10 June 2014 (158882) is credited, for the changes no note '
            'explains, to Legea nr. 187/2012, under whose art. 248 it was republished, as its own note says.',
        ],
        'repeal_acts': {},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {  # from the text as published (DetaliiDocumentAfis/53150)
        'label': 'Legea nr. 295/2004', 'kind': 'law',
        'title': 'Legea nr. 295/2004 privind regimul armelor și al munițiilor, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 583 din 30 iunie 2004',
        'enacted': '2004-06-28', 'published': '2004-06-30', 'url': P.PORTAL + 'DetaliiDocumentAfis/53150',
    })
