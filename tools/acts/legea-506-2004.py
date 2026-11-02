"""Legea nr. 506/2004 privind prelucrarea datelor cu caracter personal și protecția vieții private în sectorul
comunicațiilor electronice (Lexifina, 2026-11-02).

Act page 56973, also its base text (DetaliiDocumentAfis/56973); 8 consolidated forms 07.07.2006 .. 08.10.2024
(forms.d/legea-506-2004.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-506-2004'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-506-2004', 'short': 'Legea nr. 506/2004', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 506/2004 privind prelucrarea datelor cu caracter personal și protecția vieții private în '
                 'sectorul comunicațiilor electronice',
        'url': P.PORTAL + 'DetaliiDocument/56973',
        'in_force': '2004-11-28', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 1101 of 25 November 2004; it sets no day of its '
                     'own, so in force 3 days after publication (Constituția art. 78): 28 November 2004.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 506/2004: the first version is the law as published in Monitorul Oficial nr. 1101 of 25 '
            'November 2004 (DetaliiDocumentAfis/56973), dated 28 November 2004: it sets no in-force day of its own, so '
            '3 days after publication (Constituția art. 78).',
            'Legea nr. 506/2004: the portal\'s first consolidated form is of 7 July 2006, so the changes made up to then '
            'arrive together that day.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/56973)
        'label': 'Legea nr. 506/2004', 'kind': 'law',
        'title': 'Legea nr. 506/2004 privind prelucrarea datelor cu caracter personal și protecția vieții private în '
                 'sectorul comunicațiilor electronice, publicată în Monitorul Oficial al României, Partea I, '
                 'nr. 1101 din 25 noiembrie 2004',
        'enacted': '2004-11-17', 'published': '2004-11-25', 'url': P.PORTAL + 'DetaliiDocumentAfis/56973',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
