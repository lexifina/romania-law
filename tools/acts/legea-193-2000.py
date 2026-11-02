"""Legea nr. 193/2000 privind clauzele abuzive din contractele încheiate între profesioniști și consumatori (Lexifina,
2026-11-02).

Act page 24922, also its base text (DetaliiDocumentAfis/24922). 12 forms 15.12.2003 .. 28.05.2022, all held from
Common Crawl (forms.d/legea-193-2000.json, listed from DetaliiDocumentAfis/91502): own pages, and the republications of
2006, 2008 and 2012 from their DetaliiDocumentAfis pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-193-2000'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-193-2000', 'short': 'Legea nr. 193/2000', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 193/2000 privind clauzele abuzive din contractele încheiate între profesioniști și '
                 'consumatori',
        'url': P.PORTAL + 'DetaliiDocument/24922',
        'in_force': '2000-12-10', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 560 of 10 November 2000, in force 30 days after '
                     'publication (its art. 17): 10 December 2000.',
        'form_note': {'77879': 'The law as republished in Monitorul Oficial nr. 1.014 of 20 December 2006 under art. '
                               'III of Legea nr. 65/2002, with renumbered articles.',
                      '91502': 'The law as republished in Monitorul Oficial nr. 305 of 18 April 2008 under art. V lit. '
                               'm) of title III of Legea nr. 363/2007, with renumbered articles.'},
        'republished': {'77879': 'legea-65-2002', '91502': 'legea-363-2007'},
        # the republication of 03.08.2012 prints the law as Legea nr. 76/2012 art. 38 amends it from 15.02.2013 and
        # 01.07.2013; the in-force text of 03.08.2012-30.01.2013 is the form of 22.07.2010 (decision line)
        'skip': {'140214'},
        # the form of 15.12.2003 prints only Legea nr. 65/2002, in force on its publication (MO 52/25.01.2002)
        'form_day': {'48642': '2002-01-25'},
        'form_credits': {
            '48642': {'art-004': 'legea-65-2002'},  # art. 2 of Legea nr. 65/2002 ("contract standard preformulat")
            '149436': {'art-012': 'legea-76-2012', 'art-013': 'legea-76-2012'},  # art. 38 pct. 1, 2 of Legea 76/2012
        },
        'repeal_acts': {},
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/24922, Common Crawl 20251010032224)
        'label': 'Legea nr. 193/2000', 'kind': 'law',
        'title': 'Legea nr. 193/2000 privind clauzele abuzive din contractele încheiate între comercianți și '
                 'consumatori, publicată în Monitorul Oficial al României, Partea I, nr. 560 din 10 noiembrie 2000',
        'enacted': '2000-11-06', 'published': '2000-11-10', 'url': P.PORTAL + 'DetaliiDocumentAfis/24922',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
