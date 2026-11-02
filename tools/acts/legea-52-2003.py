"""Legea nr. 52/2003 privind transparența decizională în administrația publică (Lexifina, 2026-11-02).

Act page 41571, also its base text (DetaliiDocumentAfis/41571); 3 consolidated forms 13.12.2010 .. 02.03.2022, all held
(forms.d/legea-52-2003.json, listed from the act page): the 2013 republication from its DetaliiDocumentAfis page, the
rest from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-52-2003'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-52-2003', 'short': 'Legea nr. 52/2003', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 52/2003 privind transparența decizională în administrația publică',
        'url': P.PORTAL + 'DetaliiDocument/41571',
        'in_force': '2003-04-04', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 70 of 3 February 2003, in force 60 days after '
                     'publication (its art. 16 alin. (1)): 4 April 2003.',
        'form_note': {'153210': 'The law as republished in Monitorul Oficial nr. 749 of 3 December 2013 under art. II '
                                'of Legea nr. 281/2013, with renumbered articles.'},
        'republished': {'153210': 'legea-281-2013'},
        'repeal_acts': {},
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/41571, Common Crawl 20260210191054)
        'label': 'Legea nr. 52/2003', 'kind': 'law',
        'title': 'Legea nr. 52/2003 privind transparența decizională în administrația publică, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 70 din 3 februarie 2003',
        'enacted': '2003-01-21', 'published': '2003-02-03', 'url': P.PORTAL + 'DetaliiDocumentAfis/41571',
    }
    P.BASE_LAWS.setdefault('legea-281-2013', {  # read as published (DetaliiDocumentAfis/152367, Common Crawl 20250914081246)
        'label': 'Legea nr. 281/2013', 'kind': 'law',
        'title': 'Legea nr. 281/2013 pentru modificarea și completarea Legii nr. 52/2003 privind transparența '
                 'decizională în administrația publică, publicată în Monitorul Oficial al României, Partea I, nr. 679 '
                 'din 5 noiembrie 2013',
        'enacted': '2013-10-31', 'published': '2013-11-05', 'url': P.PORTAL + 'DetaliiDocumentAfis/152367',
    })
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
