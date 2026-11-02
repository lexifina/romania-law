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
                                'Legea nr. 71/2011, dated 1 October 2011, the day that law\'s art. 84 (arts. 35-37) '
                                'took effect.'},
        'republished': {'129800': 'legea-71-2011'},
        # the republished text prints art. 84 of Legea nr. 71/2011 (arts. 35-37), in force with the Civil Code on
        # 1 October 2011 (its arts. 220 alin. (1) and 221): dated that day, as Legea nr. 26/1990's 1998 republication
        'form_day': {'129800': '2011-10-01'},
        'decisions': [
            'Legea nr. 33/1994: the first version is the law as published in Monitorul Oficial nr. 139 of 2 June 1994 '
            '(DetaliiDocumentAfis/4066); it sets no day of its own, so it took effect on publication (Constituția '
            'art. 78 as it then stood).',
            'Legea nr. 33/1994: the portal holds no form between the law as published and the text republished in '
            'Monitorul Oficial nr. 472 of 5 July 2011 under art. 218 of Legea nr. 71/2011 (read from its own page, '
            'DetaliiDocumentAfis/129800); the republication note names no other amending act. The republished text '
            'prints the new wording of arts. 35-37 given by art. 84 of Legea nr. 71/2011 (read as published, '
            'DetaliiDocumentAfis/129268), which takes effect with the Civil Code on 1 October 2011 (its arts. 220 '
            'alin. (1) and 221), so the republished text is dated 1 October 2011: the act as published wins over the '
            'day of the republication. Changes on that day are credited to Legea nr. 71/2011, which ordered the '
            'republication (the rest are the republication\'s spelling, numbering of paragraphs and updated names of '
            'institutions and acts).',
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
