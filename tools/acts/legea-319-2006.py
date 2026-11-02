"""Legea nr. 319/2006 a securității și sănătății în muncă (Lexifina, 2026-11-02).

Act page 73772, also its base text (DetaliiDocumentAfis/73772); 6 consolidated forms (24.03.2012 .. 25.07.2021), all
held from Common Crawl (forms.d/legea-319-2006.json, listed from the act page's capture showing 25.07.2021). Parsed as
the Phase 6 acts.
"""
SLUG = 'legea-319-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-319-2006', 'short': 'Legea nr. 319/2006', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 319/2006 a securității și sănătății în muncă',
        'url': P.PORTAL + 'DetaliiDocument/73772',
        'in_force': '2006-10-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 646 of 26 July 2006, in force on 1 October 2006 '
                     '(its art. 53 alin. (1)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 319/2006: the first version is the law as published in Monitorul Oficial nr. 646 of 26 July '
            '2006 (DetaliiDocumentAfis/73772), in force on 1 October 2006 (its art. 53 alin. (1)). The portal holds '
            'no consolidated form before 24 March 2012, so the changes made up to then arrive together that day.',
            'Legea nr. 319/2006: the form of 24.03.2012 prints, as the last lines of art. 53, the portal\'s "*" and the '
            'law\'s mention that it transposes Directiva 89/391/CEE (the law as published prints it after the '
            'articles; later forms leave it out). It is not an article\'s text, and is left out.',
            'Legea nr. 319/2006: the form of 19.07.2017 adds the portal\'s note on Decizia Curții Constituționale nr. '
            '513/2017 (art. 37 alin. (2), the phrase "consecințe deosebite"); the portal leaves the article\'s text as '
            'it was, and so does this record.',
        ],
        'repeal_acts': {},
    }
    # the form of 24.03.2012 prints the portal's "*" and the law's EU-transposition mention as the last lines of art. 53
    P.EDITORIAL_LINES[SLUG] = {'art-053': ('*', 'Prezenta lege transpune Directiva Consiliului nr. 89/391/CEE')}
    # dates read from the act as published (DetaliiDocumentAfis/73772: "LEGE nr. 319 din 14 iulie 2006",
    # "București, 14 iulie 2006. Nr. 319.", MONITORUL OFICIAL nr. 646 din 26 iulie 2006)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 319/2006', 'kind': 'law',
        'title': 'Legea nr. 319 din 14 iulie 2006 a securității și sănătății în muncă, publicată în Monitorul Oficial '
                 'al României, Partea I, nr. 646 din 26 iulie 2006',
        'enacted': '2006-07-14', 'published': '2006-07-26', 'url': P.PORTAL + 'DetaliiDocument/73772',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
