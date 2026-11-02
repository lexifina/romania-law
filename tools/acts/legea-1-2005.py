"""Legea nr. 1/2005 on the organisation and functioning of cooperatives: Lexifina, 2026-11-02.

Act page 59553 is also its base text (DetaliiDocumentAfis/59553). 8 forms 22.07.2009 .. 15.07.2018, listed by the capture
of that page; 7 held from Common Crawl, the republication of 20.05.2014 from its DetaliiDocumentAfis page
(forms.d/legea-1-2005.json)."""

SLUG = 'legea-1-2005'
TITLE = 'Legea nr. 1/2005 privind organizarea și funcționarea cooperației'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-1-2005', 'short': 'Legea nr. 1/2005', 'pad': 3, 'cc_forms': True,
        'trailing_notes': True, 'count_afis_ia': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/59553',
        'in_force': '2005-03-03', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 172 of 28 February 2005; it sets no day of its own, '
                     'so in force 3 days after publication (Constituția art. 78): 3 March 2005.',
        'form_note': {'158338': 'The law as republished in Monitorul Oficial nr. 368 of 20 May 2014 under art. 248 of '
                                'Legea nr. 187/2012.'},
        'republished': {'158338': 'legea-187-2012'},
        'decisions': [
            'Legea nr. 1/2005: the first version is the law as published in Monitorul Oficial nr. 172 of 28 February '
            '2005 (DetaliiDocumentAfis/59553), dated 3 March 2005: it sets no in-force day of its own, so 3 days after '
            'publication (Constituția art. 78). The portal\'s first consolidated form is of 22 July 2009, so the '
            'changes made up to then arrive together that day.',
            'Legea nr. 1/2005: the republication of 20 May 2014 (art. 248 of Legea nr. 187/2012), read from its own '
            'page (DetaliiDocumentAfis/158338), is a version of its own; changes on that day that no note explains are '
            'credited to the act that ordered the republication, as its note says.',
        ],
        'repeal_acts': {},
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 1/2005', 'kind': 'law',
        'title': 'Legea nr. 1 din 21 februarie 2005 privind organizarea și funcționarea cooperației, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 172 din 28 februarie 2005',
        'enacted': '2005-02-21', 'published': '2005-02-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/59553',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
