"""Legea nr. 24/2000 privind normele de tehnică legislativă pentru elaborarea actelor normative (Lexifina, 2026-11-02).

Act page 21698, also its base text (DetaliiDocumentAfis/21698); 10 consolidated forms 31.05.2004 .. 15.12.2022, all held
(forms.d/legea-24-2000.json, listed from the act page): the republications of 2004 and 2010 from their
DetaliiDocumentAfis pages, the rest from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-24-2000'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-24-2000', 'short': 'Legea nr. 24/2000', 'pad': 3, 'cc_forms': True, 'titles': True,
        'title': 'Legea nr. 24/2000 privind normele de tehnică legislativă pentru elaborarea actelor normative',
        'url': P.PORTAL + 'DetaliiDocument/21698',
        'in_force': '2000-03-31', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 139 of 31 March 2000, in force on publication '
                     '(it sets no day of its own).',
        'form_note': {'54722': 'The law as republished in Monitorul Oficial nr. 777 of 25 August 2004 under art. II of '
                               'Legea nr. 189/2004, with renumbered articles.',
                      '118116': 'The law as republished in Monitorul Oficial nr. 260 of 21 April 2010 under art. II of '
                                'Legea nr. 60/2010, with renumbered articles.'},
        'republished': {'54722': 'legea-189-2004', '118116': 'legea-60-2010'},
        'repeal_acts': {},
        'decisions': [
            'Legea nr. 24/2000: the first version is the law as published in Monitorul Oficial nr. 139 of 31 March '
            '2000 (DetaliiDocumentAfis/21698). It sets no in-force day of its own, so it took effect on publication.',
            'Legea nr. 24/2000: the portal\'s first consolidated form is of 31 May 2004, so the changes made up to then '
            '(OUG nr. 6/2003, rejected by Legea nr. 268/2004, and Legea nr. 189/2004, published in Monitorul Oficial '
            'nr. 463 of 24 May 2004) arrive together that day. The form prints no note for the changes to arts. 29 '
            'and 43, which are committed as the publisher\'s.',
            'Legea nr. 24/2000: the republications of 25 August 2004 (Monitorul Oficial nr. 777, under art. II of Legea '
            'nr. 189/2004, enacted 20 May 2004; read from DetaliiDocumentAfis/54722) and 21 April 2010 (Monitorul '
            'Oficial nr. 260, under art. II of Legea nr. 60/2010, enacted 31 March 2010, which approved OUG nr. '
            '61/2009; read from DetaliiDocumentAfis/118116) renumber the articles. Changes on those days that no note '
            'explains are credited to the law that ordered the republication, as each republication note says; files '
            'follow each text\'s own numbering.',
            'Legea nr. 24/2000: the marginal titles are read as the first line of each article. The title of art. 1 '
            '("Activitatea de legiferare") follows the chapter heading in the base text and is read only from the '
            'forms that print it inside the article (25 August 2004 to 7 July 2007).',
            'Legea nr. 24/2000: the forms of 24 March 2007 to 9 April 2010 print many words without their diacritics '
            '("relatiilor", "dispozitii", "ordonantelor") and the republication of 21 April 2010 prints them again; '
            'those changes are the publisher\'s.',
        ],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/21698, Common Crawl 20251015014842)
        'label': 'Legea nr. 24/2000', 'kind': 'law',
        'title': 'Legea nr. 24/2000 privind normele de tehnică legislativă pentru elaborarea actelor normative, '
                 'publicată în Monitorul Oficial al României, Partea I, nr. 139 din 31 martie 2000',
        'enacted': '2000-03-27', 'published': '2000-03-31', 'url': P.PORTAL + 'DetaliiDocumentAfis/21698',
    }
    P.BASE_LAWS.setdefault('legea-189-2004', {  # read as published (DetaliiDocumentAfis/52129, Common Crawl 20250807093557)
        'label': 'Legea nr. 189/2004', 'kind': 'law',
        'title': 'Legea nr. 189/2004 pentru modificarea și completarea Legii nr. 24/2000 privind normele de tehnică '
                 'legislativă pentru elaborarea actelor normative, publicată în Monitorul Oficial al României, Partea '
                 'I, nr. 463 din 24 mai 2004',
        'enacted': '2004-05-20', 'published': '2004-05-24', 'url': P.PORTAL + 'DetaliiDocumentAfis/52129',
    })
    P.BASE_LAWS.setdefault('legea-60-2010', {  # read as published (DetaliiDocumentAfis/117655, Common Crawl 20260206222519)
        'label': 'Legea nr. 60/2010', 'kind': 'law',
        'title': 'Legea nr. 60/2010 privind aprobarea Ordonanței de urgență a Guvernului nr. 61/2009 pentru modificarea '
                 'și completarea Legii nr. 24/2000 privind normele de tehnică legislativă pentru elaborarea actelor '
                 'normative, publicată în Monitorul Oficial al României, Partea I, nr. 215 din 6 aprilie 2010',
        'enacted': '2010-03-31', 'published': '2010-04-06', 'url': P.PORTAL + 'DetaliiDocumentAfis/117655',
    })
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
