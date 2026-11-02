"""Legea nr. 33/1994 on expropriation for public utility (Lexifina, 2026-11-02).

Act page 4066, also its base text (DetaliiDocumentAfis/4066); 4 forms listed: the republication of 05.07.2011
(129800, read from its DetaliiDocumentAfis page) and the consolidated forms of 15.07.2015, 30.08.2015 and 16.11.2020,
all held (forms.d/legea-33-1994.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-33-1994'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-33-1994', 'short': 'Legea nr. 33/1994', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 33/1994 privind exproprierea pentru cauză de utilitate publică',
        'url': P.PORTAL + 'DetaliiDocument/4066',
        'in_force': '1994-06-02', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 139 of 2 June 1994; it sets no day of its own, so '
                     'in force on publication (Constituția art. 78 as it then stood).',
        'form_note': {'129800': 'The law as republished in Monitorul Oficial nr. 472 of 5 July 2011 under art. 218 of '
                                'Legea nr. 71/2011, with renumbered articles.'},
        'republished': {'129800': 'legea-71-2011'},
        'decisions': [
            'Legea nr. 33/1994: the first version is the law as published in Monitorul Oficial nr. 139 of 2 June 1994 '
            '(DetaliiDocumentAfis/4066); it sets no day of its own, so it took effect on publication (Constituția '
            'art. 78 as it then stood).',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/4066: "LEGE Nr. 33 din 27 mai 1994", MO nr. 139 din 2
    # iunie 1994)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 33/1994', 'kind': 'law',
        'title': 'Legea nr. 33 din 27 mai 1994, publicată în Monitorul Oficial al României, Partea I, nr. 139 din 2 '
                 'iunie 1994',
        'enacted': '1994-05-27', 'published': '1994-06-02', 'url': P.PORTAL + 'DetaliiDocument/4066',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
