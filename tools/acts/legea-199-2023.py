"""Legea nr. 199/2023 a învățământului superior (Lexifina, 2026-11-02).

Act page 271898, also its base text (DetaliiDocumentAfis/271898); 15 consolidated forms 04.09.2023 .. 20.04.2026, 13
held (forms.d/legea-199-2023.json): 27.02.2026 and 20.04.2026 are in no capture. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-199-2023'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-199-2023', 'short': 'Legea nr. 199/2023', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 199/2023 a învățământului superior',
        'url': P.PORTAL + 'DetaliiDocument/271898',
        'in_force': '2023-09-03', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 614 of 5 July 2023, in force 60 days after '
                     'publication (its art. 260 alin. (1)): 3 September 2023.',
        'form_note': {}, 'republished': {},
        'form_date': {'274194': '2023-09-03'},
        'root_word': 'act page',
        'decisions': [
            'Legea nr. 199/2023: three forms are read from Internet Archive captures: those of 19.12.2025 (304546) '
            'and 19.01.2026 (306016) from the act page 271898 as captured on 5 and 20 January 2026, while each was '
            'the newest form, and that of 30.01.2026 (306815) from DetaliiDocumentAfis/306815 as captured on 2 April '
            '2026, which shows it; the other ten consolidated forms come from Common Crawl.',
            'Legea nr. 199/2023: the first version is the law as published in Monitorul Oficial nr. 614 of 5 July '
            '2023 (DetaliiDocumentAfis/271898), in force 60 days after publication (its art. 260 alin. (1)): 3 '
            'September 2023.',
            'Legea nr. 199/2023: the form the portal lists under 4 September 2023 (274194) is read at 3 September '
            '2023, the day the law took effect: its only new notes date the changes made by OUG nr. 72/2023 (arts. '
            '57, 98 and 128) "la 03-09-2023". It is a version of its own on that day, after the law as published.',
            'Legea nr. 199/2023: art. 260 puts off the application of some provisions to later academic years (for '
            'example short-cycle studies and dual higher education from 2024-2025); the text of every article is '
            'shown from its form\'s date as the portal prints it, and no article is given a later day.',
        ],
    }
    # as the portal's note links name it; dates read from the act as published (DetaliiDocumentAfis/271898)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 199/2023',
        'title': 'Legea nr. 199 din 4 iulie 2023, publicată în Monitorul Oficial al României, Partea I, nr. 614 din '
                 '5 iulie 2023',
        'kind': 'law', 'enacted': '2023-07-04', 'published': '2023-07-05', 'url': P.PORTAL + 'DetaliiDocument/271898',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
