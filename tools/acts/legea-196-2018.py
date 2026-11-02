"""Legea nr. 196/2018 on owners' associations and the administration of condominiums (Lexifina, 2026-11-02).

Act page 203233, also its base text (DetaliiDocumentAfis/203233); 3 consolidated forms (31.08.2019, 24.12.2020,
19.12.2025), all held (forms.d/legea-196-2018.json; the newest from the act page while it showed that form). Parsed as
the Phase 6 acts.
"""
SLUG = 'legea-196-2018'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-196-2018', 'short': 'Legea nr. 196/2018', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 196/2018 privind înființarea, organizarea și funcționarea asociațiilor de proprietari și '
                 'administrarea condominiilor',
        'url': P.PORTAL + 'DetaliiDocument/203233',
        'in_force': '2018-09-28', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 660 of 30 July 2018, in force 60 days after '
                     'publication (its art. 109): 28 September 2018.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 196/2018: the first version is the law as published in Monitorul Oficial nr. 660 of 30 July '
            '2018 (DetaliiDocumentAfis/203233), in force 60 days after publication (its art. 109): 28 September '
            '2018.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/203233: "București, 20 iulie 2018. Nr. 196.", MO nr. 660
    # din 30 iulie 2018)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 196/2018', 'kind': 'law',
        'title': 'Legea nr. 196 din 20 iulie 2018, publicată în Monitorul Oficial al României, Partea I, nr. 660 din 30 '
                 'iulie 2018',
        'enacted': '2018-07-20', 'published': '2018-07-30', 'url': P.PORTAL + 'DetaliiDocument/203233',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
