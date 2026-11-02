"""Legea nr. 100/2016 privind concesiunile de lucrări și concesiunile de servicii (Lexifina, 2026-11-02).

Act page 178689 is also its base text (DetaliiDocumentAfis/178689); no republication; 12 forms, all held from Common
Crawl. forms.d/legea-100-2016.json.
"""
SLUG = 'legea-100-2016'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-100-2016', 'short': 'Legea nr. 100/2016', 'pad': 3, 'titles': False,
        'trailing_notes': True, 'cc_forms': True,
        'title': 'Legea nr. 100/2016 privind concesiunile de lucrări și concesiunile de servicii',
        'url': P.PORTAL + 'DetaliiDocument/178689',
        'in_force': '2016-05-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 392 of 23 May 2016; it sets no day of its own, so '
                     'in force 3 days after publication (Constituția art. 78): 26 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 100/2016: the first version is the law as published in Monitorul Oficial nr. 392 of 23 May 2016 '
            '(DetaliiDocumentAfis/178689), dated 26 May 2016: it sets no in-force day of its own, so 3 days after '
            'publication (Constituția art. 78). The portal holds no consolidated form before 7 December 2016, so the '
            'changes made up to then arrive together that day.',
            'Legea nr. 100/2016: the portal prints some repeal notes just after the article they concern; they are read '
            'as that article\'s notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178689)
        'label': 'Legea nr. 100/2016', 'kind': 'law',
        'title': 'Legea nr. 100/2016 privind concesiunile de lucrări și concesiunile de servicii, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 392 din 23 mai 2016',
        'enacted': '2016-05-19', 'published': '2016-05-23', 'url': P.PORTAL + 'DetaliiDocumentAfis/178689',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
