"""Legea nr. 218/2002 privind organizarea și funcționarea Poliției Române (Lexifina, 2026-11-02).

Act page 35841 is also its base text (DetaliiDocumentAfis/35841, Monitorul Oficial nr. 305 of 9 May 2002); 14
consolidated forms (2003-07-01 .. 2022-08-25) incl. the republications 157719 (2014) and 223421 (2020).
forms.d/legea-218-2002.json.
"""
SLUG = 'legea-218-2002'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-218-2002', 'short': 'Legea nr. 218/2002', 'pad': 3, 'titles': False,
        'cc_forms': True,
        'title': 'Legea nr. 218/2002 privind organizarea și funcționarea Poliției Române',
        'url': P.PORTAL + 'DetaliiDocument/35841',
        'in_force': '2002-05-09', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 305 of 9 May 2002; it sets no day of its own, so '
                     'in force on publication (Constituția art. 78 as it then stood).',
        'form_note': {'157719': 'The law as republished in Monitorul Oficial nr. 307 of 25 April 2014 under art. 107 '
                                'alin. (3) of Legea nr. 255/2013, with renumbered articles.',
                      '223421': 'The law as republished in Monitorul Oficial nr. 170 of 2 March 2020 under art. V of '
                                'Legea nr. 192/2019, with renumbered articles.'},
        'republished': {'157719': 'legea-255-2013', '223421': 'legea-192-2019'},
        'decisions': [
            'Legea nr. 218/2002: the first version is the law as published in Monitorul Oficial nr. 305 of 9 May 2002 '
            '(DetaliiDocumentAfis/35841), dated that day: the law sets no day of its own, so it took effect on '
            'publication.',
            'Legea nr. 218/2002: the portal holds no consolidated form before 1 July 2003, so the changes made '
            'between the law as published and that form arrive together that day.',
            'Legea nr. 218/2002: the republications of 25 April 2014 (art. 107 alin. (3) of Legea nr. 255/2013, '
            'enacted 19 July 2013, published in Monitorul Oficial nr. 515 of 14 August 2013) and 2 March 2020 (art. V '
            'of Legea nr. 192/2019, published in Monitorul Oficial nr. 868 of 28 October 2019), each with renumbered '
            'articles, are read from their own pages (DetaliiDocumentAfis/157719 and 223421); changes on those days '
            'that no note explains are credited to the law that ordered the republication, as each republication '
            'note says.',
            'Legea nr. 218/2002: the forms of 1 July 2003 and 5 March 2018 differ from the form before them in '
            'spelling, diacritics and list layout (for example "îndrumă" / "îndruma", "inlaturare" / "înlăturare") '
            'that no note explains; those changes are the publisher\'s, labelled unexplained.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the law as published (DetaliiDocumentAfis/35841)
        'label': 'Legea nr. 218/2002', 'kind': 'law',
        'title': 'Legea nr. 218/2002 privind organizarea și funcționarea Poliției Române, publicată în Monitorul '
                 'Oficial al României, Partea I, nr. 305 din 9 mai 2002',
        'enacted': '2002-04-23', 'published': '2002-05-09', 'url': P.PORTAL + 'DetaliiDocumentAfis/35841',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
