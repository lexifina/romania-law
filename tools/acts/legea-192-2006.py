"""Legea nr. 192/2006 privind medierea și organizarea profesiei de mediator (Lexifina, 2026-11-02).

Act page 71928, also its base text (DetaliiDocumentAfis/71928); 15 forms 06.12.2009 .. 29.07.2019, all held from Common
Crawl (forms.d/legea-192-2006.json; the newest is read from the act page, which shows it). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-192-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-192-2006', 'short': 'Legea nr. 192/2006', 'pad': 3, 'cc_forms': True, 'cte_notes': True, 'hold': True,
        'title': 'Legea nr. 192/2006 privind medierea și organizarea profesiei de mediator',
        'url': P.PORTAL + 'DetaliiDocument/71928',
        'in_force': '2006-05-25', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 441 of 22 May 2006, with no day of its own, so in '
                     'force 3 days after publication (Constituția, art. 78): 25 May 2006.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 192/2006: the first version is the law as published in Monitorul Oficial nr. 441 of 22 May '
            '2006 (DetaliiDocumentAfis/71928). It sets no in-force day of its own, so it took effect 3 days after '
            'publication (Constituția of 1991 as republished, art. 78): 25 May 2006. Its art. 74 alin. (2) makes the '
            'opinion of art. 9 applicable from the publication of the training standards; no article is given a '
            'later day. The portal\'s first form is of 6 December 2009, so the changes made up to then arrive '
            'together that day.',
        ],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/71928)
        'label': 'Legea nr. 192/2006', 'kind': 'law',
        'title': 'Legea nr. 192 din 16 mai 2006 privind medierea și organizarea profesiei de mediator, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 441 din 22 mai 2006',
        'enacted': '2006-05-16', 'published': '2006-05-22', 'url': P.PORTAL + 'DetaliiDocumentAfis/71928',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
