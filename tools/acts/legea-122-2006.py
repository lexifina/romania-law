"""Legea nr. 122/2006 privind azilul în România (Lexifina, 2026-11-02).

Act page 71808, also its base text (DetaliiDocumentAfis/71808); 22 forms 29.01.2007 .. 26.05.2025
(forms.d/legea-122-2006.json), all read from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-122-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-122-2006', 'short': 'Legea nr. 122/2006', 'pad': 3, 'cc_forms': True,
        'root_word': 'act page',
        'title': 'Legea nr. 122/2006 privind azilul în România',
        'url': P.PORTAL + 'DetaliiDocument/71808',
        'in_force': '2006-08-16', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 428 of 18 May 2006, in force 90 days after '
                     'publication (its art. 152 alin. (1)): 16 August 2006.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 122/2006: the first version is the law as published in Monitorul Oficial nr. 428 of 18 May '
            '2006 (DetaliiDocumentAfis/71808), in force 90 days after publication (its art. 152 alin. (1)): 16 '
            'August 2006. The portal\'s first form is of 29 January 2007, so the changes made up to then arrive '
            'together that day.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/71808)
        'label': 'Legea nr. 122/2006', 'kind': 'law',
        'title': 'Legea nr. 122 din 4 mai 2006 privind azilul în România, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 428 din 18 mai 2006',
        'enacted': '2006-05-04', 'published': '2006-05-18', 'url': P.PORTAL + 'DetaliiDocumentAfis/71808',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
