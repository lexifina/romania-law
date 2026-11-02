"""Legea nr. 46/2008 - Codul silvic (Lexifina, 2026-11-02).

Act page 170527 (the republication of 12 August 2015, which also lists the forms); 22 forms 08.12.2008 .. 13.04.2024,
all held from Common Crawl (forms.d/legea-46-2008.json); the republication is read from its DetaliiDocumentAfis page
('afis_cc'). The text as first published is not held, so the record starts at the oldest form (no_base). Parsed as the
Phase 6 acts. The Codul silvic of Legea nr. 331/2024 replaces it; no repeal version is made up.
"""
SLUG = 'legea-46-2008'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-46-2008', 'short': 'Legea nr. 46/2008', 'pad': 3, 'cc_forms': True,
        'no_base': True, 'first_law': None, 'revert_credit': True, 'earlier_laws': [SLUG],
        'title': 'Legea nr. 46/2008 - Codul silvic',
        'url': P.PORTAL + 'DetaliiDocument/280837',
        'in_force': '2008-12-08',
        'base_note': 'Oldest version available: the portal\'s consolidated form of 8 December 2008. The law was enacted '
                     'on 19 March 2008 and first published in Monitorul Oficial nr. 238 of 27 March 2008; it sets no '
                     'day of its own, so it took effect 3 days after publication (Constituția art. 78); that text is '
                     'not held.',
        'form_note': {'170527': 'The law as republished in Monitorul Oficial nr. 611 of 12 August 2015 under art. IV '
                                'of Legea nr. 133/2015, with renumbered articles.'},
        'republished': {'170527': 'legea-133-2015'},
        'decisions': DECISIONS,
    }
    P.BASE_LAWS.update({
        SLUG: {  # dates read from the form of 8 December 2008 (100191), which prints the act's heading
            'label': 'Legea nr. 46/2008', 'kind': 'law',
            'title': 'Legea nr. 46/2008 - Codul silvic, publicată în Monitorul Oficial al României, Partea I, nr. 238 '
                     'din 27 martie 2008',
            'enacted': '2008-03-19', 'published': '2008-03-27', 'url': None,
        },
        'legea-133-2015': {  # read from the act as published (DetaliiDocumentAfis/168721)
            'label': 'Legea nr. 133/2015', 'kind': 'law',
            'title': 'Legea nr. 133/2015 pentru modificarea și completarea Legii nr. 46/2008 - Codul silvic, '
                     'publicată în Monitorul Oficial al României, Partea I, nr. 411 din 10 iunie 2015',
            'enacted': '2015-06-08', 'published': '2015-06-10', 'url': P.PORTAL + 'DetaliiDocumentAfis/168721',
        },
    })
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)


DECISIONS = [
    'Legea nr. 46/2008: the base text is missing. The law as first published (Monitorul Oficial nr. 238 of 27 March '
    '2008) is not held: the portal\'s page for it (DetaliiDocumentAfis/90766) has no readable capture. The record '
    'starts at the oldest form held, the portal\'s consolidated form of 8 December 2008 (updated to OUG nr. 193/2008), '
    'credited to the publisher as the oldest version available; any change made before that day is already in it. No '
    'enacted version is made up; the law\'s enactment (19 March 2008) and first publication (27 March 2008) are kept '
    'in its metadata. The law sets no day of its own, so it took effect 3 days after publication (Constituția art. '
    '78).',
    'Legea nr. 46/2008: the text republished in Monitorul Oficial nr. 611 of 12 August 2015 under art. IV of Legea '
    'nr. 133/2015 (enacted 8 June 2015, published in Monitorul Oficial nr. 411 of 10 June 2015), with renumbered '
    'articles, is read from its own page (DetaliiDocumentAfis/170527). Changes on that day that no note explains are '
    'credited to Legea nr. 133/2015, as the republication note says; files follow each text\'s own numbering, so many '
    'change that day. The act page 170527 stands, in the portal\'s list of forms, for that republication; the newest '
    'form (13 April 2024) has its own page, 280837.',
    'Legea nr. 46/2008: the portal lists no form between 8 December 2008 and 4 June 2009, and none between 4 June '
    '2009 and 5 March 2010 (nor between other days far apart), so the changes made in those periods arrive with the '
    'next form held. Legea nr. 331/2024 (the new Codul silvic) replaces this law; no repeal version is made up.',
]
