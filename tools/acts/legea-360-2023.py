"""Legea nr. 360/2023 privind sistemul public de pensii (Lexifina, 2026-11-02).

Act page 276927, also its base text (DetaliiDocumentAfis/276927); 2 consolidated forms (31.12.2024, 28.07.2025), both
held (forms.d/legea-360-2023.json, listed from the act page's capture showing 28.07.2025). Parsed as the Phase 6 acts.
It replaced Legea nr. 263/2010 (acts/legea-263-2010.py) from 1 September 2024.
"""
SLUG = 'legea-360-2023'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-360-2023', 'short': 'Legea nr. 360/2023', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 360/2023 privind sistemul public de pensii',
        'url': P.PORTAL + 'DetaliiDocument/276927',
        'in_force': '2024-09-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 1089 of 4 December 2023, in force on 1 September '
                     '2024 (its art. 167), save the provisions that took effect on 1 January 2024.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 360/2023: the first version is the law as published in Monitorul Oficial nr. 1089 of 4 '
            'December 2023 (DetaliiDocumentAfis/276927), in force on 1 September 2024 (its art. 167), save art. 46 '
            'alin. (2), art. 84 alin. (6), art. 127, art. 168 alin. (2) and art. 169, which took effect on 1 January '
            '2024; they are shown from 1 September 2024 with the rest of the law. The portal\'s first form is of 31 '
            'December 2024, so the changes made up to then would arrive together that day.',
            'Legea nr. 360/2023: the forms of 31 December 2024 and 28 July 2025 print every article as published and '
            'add only the portal\'s notes: OUG nr. 156/2024 art. XVII (the reference point of art. 83 alin. (1) kept at 81 '
            'lei in 2025, art. 84 alin. (3)-(5), (7) and (8) applied from 2026) and Legea nr. 141/2025 art. XXXI '
            '(the same for 2026 and from 2027), Legea nr. 10/2025 art. 22 (death grant amounts), the reference to '
            'HG nr. 48/2025, and the "Decizie de respingere" notes naming Hotărârile Parlamentului nr. 307/2025, '
            '319/2025, 370/2025, 382/2025 and 396/2025. No article text changes, so neither form adds a version; the '
            'annexes are not articles and are not read.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/276927: "București, 29 noiembrie 2023. Nr. 360.",
    # Monitorul Oficial nr. 1089 din 4 decembrie 2023)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 360/2023', 'kind': 'law',
        'title': 'Legea nr. 360 din 29 noiembrie 2023, publicată în Monitorul Oficial al României, Partea I, nr. 1089 '
                 'din 4 decembrie 2023',
        'enacted': '2023-11-29', 'published': '2023-12-04', 'url': P.PORTAL + 'DetaliiDocument/276927',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
