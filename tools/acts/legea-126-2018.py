"""Legea nr. 126/2018 privind piețele de instrumente financiare (Lexifina, 2026-11-02).

Act page 201860, also its base text (DetaliiDocumentAfis/201860). 10 forms listed by DetaliiDocument/305317
(02.08.2018 .. 16.01.2026), all held from Common Crawl (forms.d/legea-126-2018.json); no republication. It took over
part of Legea nr. 297/2004 (part 99l-legea-297-2004).
"""
SLUG = 'legea-126-2018'
TITLE = 'Legea nr. 126/2018 privind piețele de instrumente financiare'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-126-2018', 'short': 'Legea nr. 126/2018', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/201860',
        'in_force': '2018-07-06', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 521 of 26 June 2018, in force 10 days after '
                     'publication (its art. 284): 6 July 2018.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 126/2018: the first version is the law as published in Monitorul Oficial nr. 521 of 26 June '
            '2018 (DetaliiDocumentAfis/201860), in force 10 days after publication (its art. 284): 6 July 2018. Art. 169 alin. '
            '(5)-(7), which apply from 3 September 2019 (the same article), are shown from 6 July 2018 with the rest '
            'of the law.',
        ],
        'repeal_acts': {},
        'root_word': 'act page',
    }
    # as the portal's note links name it (the same entry part 99l-legea-297-2004 carries); dates read from the act as
    # published (DetaliiDocumentAfis/201860: "București, 11 iunie 2018. Nr. 126.", MO nr. 521 din 26 iunie 2018)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 126/2018', 'kind': 'law',
        'title': 'Legea nr. 126 din 11 iunie 2018, publicată în Monitorul Oficial al României, Partea I, nr. 521 din 26 '
                 'iunie 2018',
        'enacted': '2018-06-11', 'published': '2018-06-26', 'url': P.PORTAL + 'DetaliiDocument/201860',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
