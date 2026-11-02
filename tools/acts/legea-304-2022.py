"""Legea nr. 304/2022 privind organizarea judiciară (Lexifina, 2026-11-02).

Act page 261410, also its base text (DetaliiDocumentAfis/261410); 5 consolidated forms 15.05.2023 .. 31.12.2025, all
held (forms.d/legea-304-2022.json; the newest is read from the act page, which shows it). Parsed as the Phase 6 acts. It replaced Legea nr. 304/2004 (part 99w).
"""
SLUG = 'legea-304-2022'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-304-2022', 'short': 'Legea nr. 304/2022', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 304/2022 privind organizarea judiciară',
        'url': P.PORTAL + 'DetaliiDocument/261410',
        'in_force': '2022-12-16', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 1104 of 16 November 2022, in force 30 days after '
                     'publication (its art. 168 alin. (1)): 16 December 2022.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 304/2022: the first version is the law as published in Monitorul Oficial nr. 1104 of 16 '
            'November 2022 (DetaliiDocumentAfis/261410), in force 30 days after publication (its art. 168 alin. '
            '(1)): 16 December 2022. The portal\'s first form is of 15 May 2023, so the changes made up to then '
            'arrive together that day.',
            'Legea nr. 304/2022: art. 168 alin. (2) puts off to a later day (1 January 2026 as published; 1 January '
            '2027 from 31 December 2025, as OUG nr. 93/2025 amended it) only the rule on counting service without '
            'the time spent as a trainee prosecutor (auditor de justiție); it names no provision of its own, so no '
            'article is given a later day.',
            'Legea nr. 304/2022: the forms of 15 May 2023, 29 December 2023 and 17 July 2025 change no article and '
            'add no version (the first two add only the portal\'s notes on other acts; the third changes Anexa nr. '
            '1, which is not read as an article).',
        ],
    }
    # as the portal's note links name it (the same entry part 99w carries for Legea nr. 304/2022); dates read from
    # the act as published (DetaliiDocumentAfis/261410)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 304/2022',
        'title': 'Legea nr. 304 din 15 noiembrie 2022, publicată în Monitorul Oficial al României, Partea I, nr. 1104 '
                 'din 16 noiembrie 2022',
        'kind': 'law', 'enacted': '2022-11-15', 'published': '2022-11-16', 'url': P.PORTAL + 'DetaliiDocument/261410',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
