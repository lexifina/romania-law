"""Legea nr. 198/2023 a învățământului preuniversitar (Lexifina, 2026-11-02).

Act page 271896, also its base text (DetaliiDocumentAfis/271896); 14 consolidated forms 04.09.2023 .. 20.04.2026, all
held (forms.d/legea-198-2023.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-198-2023'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-198-2023', 'short': 'Legea nr. 198/2023', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 198/2023 a învățământului preuniversitar',
        'url': P.PORTAL + 'DetaliiDocument/271896',
        'in_force': '2023-09-03', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 613 of 5 July 2023, in force 60 days after '
                     'publication (its art. 248 alin. (1)): 3 September 2023.',
        'form_note': {}, 'republished': {},
        'form_date': {'274195': '2023-09-03'},
        'decisions': [
            'Legea nr. 198/2023: the form the portal lists under 4 September 2023 (274195) is read at 3 September '
            '2023, the day the law took effect: its only new notes date the changes made by OUG nr. 72/2023 (art. 85 '
            'alin. (1)) "la 03-09-2023". It is a version of its own on that day, after the law as published.',
            'Legea nr. 198/2023: the first version is the law as published in Monitorul Oficial nr. 613 of 5 July '
            '2023 (DetaliiDocumentAfis/271896), in force 60 days after publication (its art. 248 alin. (1)): 3 '
            'September 2023. The portal\'s first form is of 4 September 2023, so the changes made on that day arrive '
            'together with it.',
            'Legea nr. 198/2023: art. 248 puts off the application of many provisions to later school years or later '
            'periods (for example arts. 69, 83, 86, 108, 139 and 140); the text of every article is shown from its '
            'form\'s date as the portal prints it, and no article is given a later day.',
        ],
    }
    # as the portal's note links name it; dates read from the act as published (DetaliiDocumentAfis/271896)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 198/2023',
        'title': 'Legea nr. 198 din 4 iulie 2023, publicată în Monitorul Oficial al României, Partea I, nr. 613 din '
                 '5 iulie 2023',
        'kind': 'law', 'enacted': '2023-07-04', 'published': '2023-07-05', 'url': P.PORTAL + 'DetaliiDocument/271896',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
