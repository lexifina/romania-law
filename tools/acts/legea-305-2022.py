"""Legea nr. 305/2022 privind Consiliul Superior al Magistraturii (Lexifina, 2026-11-02).

Act page 261415, also its base text (DetaliiDocumentAfis/261415); one consolidated form, 31.10.2023 (forms.d/legea-305-2022.json;
the form is read from the act page, which shows it). Parsed as the Phase 6 acts. It replaced Legea nr. 317/2004.
"""
SLUG = 'legea-305-2022'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-305-2022', 'short': 'Legea nr. 305/2022', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 305/2022 privind Consiliul Superior al Magistraturii',
        'url': P.PORTAL + 'DetaliiDocument/261415',
        'in_force': '2022-12-16', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 1105 of 16 November 2022, in force 30 days after '
                     'publication (its art. 96 alin. (1)): 16 December 2022.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 305/2022: the first version is the law as published in Monitorul Oficial nr. 1105 of 16 '
            'November 2022 (DetaliiDocumentAfis/261415), in force 30 days after publication (its art. 96 alin. '
            '(1)): 16 December 2022. The portal\'s only form is of 31 October 2023, so the changes made up to then '
            'arrive together that day.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/261415)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 305/2022',
        'title': 'Legea nr. 305 din 15 noiembrie 2022, publicată în Monitorul Oficial al României, Partea I, nr. 1105 '
                 'din 16 noiembrie 2022',
        'kind': 'law', 'enacted': '2022-11-15', 'published': '2022-11-16', 'url': P.PORTAL + 'DetaliiDocument/261415',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
