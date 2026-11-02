"""Legea nr. 350/2001 on spatial planning and urbanism (Lexifina, 2026-11-02).

Act page 29453, also its base text (DetaliiDocumentAfis/29453); 35 consolidated forms listed (27.08.2004 ..
25.02.2026; forms.d/legea-350-2001.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-350-2001'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-350-2001', 'short': 'Legea nr. 350/2001', 'pad': 3, 'cc_forms': True,
        # the forms of 2017 print "a revenit la forma anterioară ... ca urmare a respingerii ... prin LEGEA nr. 86/2017"
        # (rejecting OUG nr. 100/2016); the forms of 2008-2013 print "*) NOTA C.T.C.E." notes inside articles
        'revert_credit': True, 'cte_notes': True,
        # the form of 27.08.2004 names OG nr. 69/2004 as "ORDONANTA nr. 69" (art. 38 alin. (2^1))
        'plain_ordonanta': True,
        'title': 'Legea nr. 350/2001 privind amenajarea teritoriului și urbanismul',
        'url': P.PORTAL + 'DetaliiDocument/29453',
        'in_force': '2001-07-10', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 373 of 10 July 2001; it sets no day of its own, so '
                     'in force on publication (Constituția art. 78 as it then stood).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 350/2001: the first version is the law as published in Monitorul Oficial nr. 373 of 10 July '
            '2001 (DetaliiDocumentAfis/29453); it sets no day of its own, so it took effect on publication '
            '(Constituția art. 78 as it then stood). Its annexes are not articles and are left out, as for the '
            'other acts.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/29453: "LEGE nr. 350 din 6 iulie 2001", MO nr. 373 din
    # 10 iulie 2001)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 350/2001', 'kind': 'law',
        'title': 'Legea nr. 350 din 6 iulie 2001, publicată în Monitorul Oficial al României, Partea I, nr. 373 din 10 '
                 'iulie 2001',
        'enacted': '2001-07-06', 'published': '2001-07-10', 'url': P.PORTAL + 'DetaliiDocument/29453',
    }
    # the forms of 17.07.2011 .. 13.07.2013 print, after art. 36^1, a "* NOTA C.T.C.E." quoting art. V of OUG nr.
    # 7/2011 ("Menținerea în funcție a arhitecților-șefi ..."); the quotation is another act's text, not this article's
    P.EDITORIAL_LINES[SLUG] = {'art-036-1': ('"Menținerea în funcție a arhitecților-șefi care nu îndeplinesc',)}
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
