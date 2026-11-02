"""Legea nr. 265/2022 privind registrul comerțului (Lexifina, 2026-11-02).

Act page 257835, also its base text (DetaliiDocumentAfis/257835); 2 consolidated forms (23.07.2023, 12.09.2024), both
held from Common Crawl (forms.d/legea-265-2022.json, listed from the act page's capture showing 12.09.2024). Parsed as
the Phase 6 acts. It replaced Legea nr. 26/1990 (acts/legea-26-1990.py) from 26 November 2022.
"""
SLUG = 'legea-265-2022'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-265-2022', 'short': 'Legea nr. 265/2022', 'pad': 3, 'cc_forms': True,
        # art. 129-132 amend other acts and quote the articles they rewrite (S_ART inside S_ART)
        'quoted_articles': True,
        'title': 'Legea nr. 265/2022 privind registrul comerțului și pentru modificarea și completarea altor acte '
                 'normative cu incidență asupra înregistrării în registrul comerțului',
        'url': P.PORTAL + 'DetaliiDocument/257835',
        'in_force': '2022-11-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 750 of 26 July 2022, in force 4 months after '
                     'publication (its art. 141 alin. (1)): 26 November 2022.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 265/2022: the first version is the law as published in Monitorul Oficial nr. 750 of 26 July '
            '2022 (DetaliiDocumentAfis/257835), in force 4 months after publication (its art. 141 alin. (1)): 26 '
            'November 2022. Arts. 133, 134, 137 and 138 took effect 3 days after publication (29 July 2022), and '
            'art. 8 alin. (2) applies from 1 August 2023 (art. 141 alin. (2)); they are shown from 26 November 2022 '
            'with the rest of the law.',
        ],
    }
    # as the portal's note links name it (the same entry part 80-legea-31-1990 carries for Legea nr. 265/2022); dates
    # read from the act as published (DetaliiDocumentAfis/257835: "București, 22 iulie 2022. Nr. 265.", MO nr. 750
    # din 26 iulie 2022)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 265/2022', 'kind': 'law',
        'title': 'Legea nr. 265 din 22 iulie 2022, publicată în Monitorul Oficial al României, Partea I, nr. 750 din 26 '
                 'iulie 2022',
        'enacted': '2022-07-22', 'published': '2022-07-26', 'url': P.PORTAL + 'DetaliiDocument/257835',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
