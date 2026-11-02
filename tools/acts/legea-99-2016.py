"""Legea nr. 99/2016 privind achizițiile sectoriale (Lexifina, 2026-11-02).

Act page 178661 is also its base text (DetaliiDocumentAfis/178661); no republication; 19 forms, all held from Common
Crawl or the Internet Archive. forms.d/legea-99-2016.json.
"""
SLUG = 'legea-99-2016'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-99-2016', 'short': 'Legea nr. 99/2016', 'pad': 3, 'titles': False,
        'trailing_notes': True, 'cc_forms': True,
        # art. 257 alin. (2): art. 208 alin. (2) in force on 18 October 2018; the forms print it from the start
        'later_provisions': (
            {'day': '2018-10-18', 'law': SLUG,
             'lines': ('(2) Entitățile contractante utilizează e-Certis',),
             'note': 'Art. 208 alin. (2) takes effect on this day (art. 257 alin. (2) of the law); the portal prints it '
                     'from the law as published.'},
        ),
        'title': 'Legea nr. 99/2016 privind achizițiile sectoriale',
        'url': P.PORTAL + 'DetaliiDocument/178661',
        'in_force': '2016-05-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 391 of 23 May 2016, in force 3 days after '
                     'publication (its art. 257 alin. (1)): 26 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 99/2016: the first version is the law as published in Monitorul Oficial nr. 391 of 23 May 2016 '
            '(DetaliiDocumentAfis/178661), dated 26 May 2016: its art. 257 alin. (1) puts it in force 3 days after '
            'publication. Its art. 257 alin. (2) puts art. 208 alin. (2) in force on 18 October 2018; under the rule for '
            'text printed before its day, that provision is absent until then and is added that day, credited to '
            'Legea nr. 99/2016.',
            'Legea nr. 99/2016: the portal prints some repeal notes just after the article they concern; they are read '
            'as that article\'s notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178661)
        'label': 'Legea nr. 99/2016', 'kind': 'law',
        'title': 'Legea nr. 99/2016 privind achizițiile sectoriale, publicată în Monitorul Oficial al României, '
                 'Partea I, nr. 391 din 23 mai 2016',
        'enacted': '2016-05-19', 'published': '2016-05-23', 'url': P.PORTAL + 'DetaliiDocumentAfis/178661',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
