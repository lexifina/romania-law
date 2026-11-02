"""Legea nr. 367/2022 privind dialogul social (Lexifina, 2026-11-02).

Act page 262989, also its base text (DetaliiDocumentAfis/262989); 3 consolidated forms (25.05.2023, 02.12.2023,
17.11.2024), all held from Common Crawl (forms.d/legea-367-2022.json, listed from the act page's capture showing
17.11.2024). Parsed as the Phase 6 acts. It replaced Legea dialogului social nr. 62/2011 (its art. 189).
"""
SLUG = 'legea-367-2022'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-367-2022', 'short': 'Legea nr. 367/2022', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 367/2022 privind dialogul social',
        'url': P.PORTAL + 'DetaliiDocument/262989',
        'in_force': '2022-12-25', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 1238 of 22 December 2022; it sets no day of its '
                     'own, so in force 3 days after publication (Constituția art. 78): 25 December 2022.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 367/2022: the first version is the law as published in Monitorul Oficial nr. 1238 of 22 '
            'December 2022 (DetaliiDocumentAfis/262989), dated 25 December 2022: it sets no in-force day of its own, '
            'so 3 days after publication (Constituția art. 78).',
        ],
        'repeal_acts': {},
    }
    # dates read from the act as published (DetaliiDocumentAfis/262989: "LEGE nr. 367 din 19 decembrie 2022",
    # "București, 19 decembrie 2022. Nr. 367.", MONITORUL OFICIAL nr. 1238 din 22 decembrie 2022)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 367/2022', 'kind': 'law',
        'title': 'Legea nr. 367 din 19 decembrie 2022 privind dialogul social, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 1238 din 22 decembrie 2022',
        'enacted': '2022-12-19', 'published': '2022-12-22', 'url': P.PORTAL + 'DetaliiDocument/262989',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
