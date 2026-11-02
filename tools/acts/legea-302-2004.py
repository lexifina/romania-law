"""Legea nr. 302/2004 privind cooperarea judiciară internațională în materie penală (Lexifina, 2026-11-02).

Act page 53158, also its base text (DetaliiDocumentAfis/53158); 17 forms 24.06.2006 .. 19.12.2025 listed
(forms.d/legea-302-2004.json), the newest (19.12.2025) held by no archive; the republications of 2011 and 2019 are read
from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-302-2004'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-302-2004', 'short': 'Legea nr. 302/2004', 'pad': 3, 'cc_forms': True,
        'trailing_notes': True,
        'title': 'Legea nr. 302/2004 privind cooperarea judiciară internațională în materie penală',
        'url': P.PORTAL + 'DetaliiDocument/53158',
        'in_force': '2004-08-30', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 594 of 1 July 2004, in force 60 days after '
                     'publication (its art. 189 alin. (1)): 30 August 2004.',
        'form_note': {'128922': 'The law as republished in Monitorul Oficial nr. 377 of 31 May 2011 under art. III of '
                                'Legea nr. 222/2008, with renumbered articles.',
                      '214172': 'The law as republished in Monitorul Oficial nr. 411 of 27 May 2019 under art. II of '
                                'Legea nr. 236/2017, with renumbered articles.'},
        'republished': {'128922': 'legea-222-2008', '214172': 'legea-236-2017'},
        'decisions': [
            'Legea nr. 302/2004: the first version is the law as published in Monitorul Oficial nr. 594 of 1 July '
            '2004 (DetaliiDocumentAfis/53158), in force 60 days after publication (its art. 189 alin. (1)): 30 August '
            '2004. The portal\'s first form is of 24 June 2006, so the changes made up to then arrive together that '
            'day.',
        ],
        'repeal_acts': {},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {  # read from the act as published (DetaliiDocumentAfis/53158)
        'label': 'Legea nr. 302/2004', 'kind': 'law',
        'title': 'Legea nr. 302 din 28 iunie 2004, publicată în Monitorul Oficial al României, Partea I, nr. 594 din '
                 '1 iulie 2004',
        'enacted': '2004-06-28', 'published': '2004-07-01', 'url': P.PORTAL + 'DetaliiDocumentAfis/53158',
    })
