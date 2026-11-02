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
        # the form of 13.12.2010 prints the note on art. 11 alin. (3) as a paragraph, with a misprint ("a fot introdus")
        'mod_lines': True, 'mod_typos': ((' a fot introdus', ' a fost introdus'),),
        'decisions': [
            'Legea nr. 52/2003: the first version is the law as published in Monitorul Oficial nr. 70 of 3 February '
            '2003 (DetaliiDocumentAfis/41571), in force 60 days after publication (its art. 16 alin. (1)): 4 April '
            '2003. The portal\'s first consolidated form is of 13 December 2010; the only change made before it, '
            'Legea nr. 242/2010 (Monitorul Oficial nr. 828 of 10 December 2010), arrives with it.',
            'Legea nr. 52/2003: the form of 13 December 2010 prints the portal\'s note on art. 11 alin. (3) as a '
            'paragraph of the article, with a misprint ("a fot introdus de pct. 3 al art. unic din LEGEA nr. 242 ..."); '
            'it is not text and is left out, and is read as the article\'s note naming Legea nr. 242/2010, whose art. '
            'unic pct. 3 (read as published: DetaliiDocumentAfis/124325) inserts that paragraph.',
            'Legea nr. 52/2003: the republication of 3 December 2013 (Monitorul Oficial nr. 749, under art. II of '
            'Legea nr. 281/2013, enacted 31 October 2013 and published in Monitorul Oficial nr. 679 of 5 November 2013; '
            'read from DetaliiDocumentAfis/153210) renumbers the articles. The portal holds no form between 13 '
            'December 2010 and that republication, so the changes of Legea nr. 281/2013 arrive together on 3 December '
            '2013 and are credited to it, as the republication note says; files follow each text\'s own numbering.',
        ],
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
