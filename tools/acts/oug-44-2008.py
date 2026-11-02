"""OUG nr. 44/2008 (PFA, sole proprietorships, family businesses): Lexifina, 2026-11-02.

Act page 91808 is also its base text (DetaliiDocumentAfis/91808); 6 forms 24.04.2009 .. 26.11.2022, all held from
Common Crawl (forms.d/oug-44-2008.json)."""

SLUG = 'oug-44-2008'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-44-2008', 'short': 'OUG nr. 44/2008', 'pad': 3, 'cc_forms': True, 'trailing_notes': True, 'sign_tail': True,
        'title': 'Ordonanța de urgență a Guvernului nr. 44/2008 privind desfășurarea activităților economice de către '
                 'persoanele fizice autorizate, întreprinderile individuale și întreprinderile familiale',
        'url': P.PORTAL + 'DetaliiDocument/91808',
        'in_force': '2008-04-25', 'first_law': 'oug-44-2008',
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 328 of 25 April 2008; it sets no '
                     'day of its own, so in force on publication.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 44/2008: the first version is the emergency ordinance as published in Monitorul Oficial nr. 328 of '
            '25 April 2008 (DetaliiDocumentAfis/91808), dated 25 April 2008: it sets no in-force day of its own, so in '
            'force on publication. Its annex (Anexa 1, the documents supporting an application for registration) is '
            'not an article and is not read; the portal\'s consolidated forms do not print it.',
            'OUG nr. 44/2008: approved with amendments by Legea nr. 182/2016 (Monitorul Oficial nr. 828 of 19 October '
            '2016); the portal\'s notes date its changes 17 January 2017, the date of the form that carries them, and '
            'each change is credited to it from those notes.',
            'OUG nr. 44/2008: the portal prints the repeal notes of arts. 34 and 42 just after the article ("Articolul '
            '34 ... a fost abrogat de Punctul 27, Articolul I din LEGEA nr. 182 ..."); they are read as that article\'s '
            'notes. The signature block printed after art. 44 ("PRIM-MINISTRU ...") is not part of the article.',
        ],
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'OUG nr. 44/2008', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 44/2008 privind desfășurarea activităților economice de către '
                 'persoanele fizice autorizate, întreprinderile individuale și întreprinderile familiale, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 328 din 25 aprilie 2008',
        'enacted': '2008-04-16', 'published': '2008-04-25', 'url': P.PORTAL + 'DetaliiDocumentAfis/91808',
    }
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
