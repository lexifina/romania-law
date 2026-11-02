"""OUG nr. 99/2006 privind instituțiile de credit și adecvarea capitalului (credit institutions and capital adequacy):
Lexifina, 2026-11-02.

Act page 78313, also its base text (DetaliiDocumentAfis/78313); no republication; 26 consolidated forms 21.07.2007 ..
05.03.2026 (forms.d/oug-99-2006.json): 25 from Common Crawl, the newest from the act page's archive.org capture made
while it was the newest form. Parsed as the Phase 6 acts.
"""
SLUG = 'oug-99-2006'
TITLE = 'Ordonanța de urgență a Guvernului nr. 99/2006 privind instituțiile de credit și adecvarea capitalului'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-99-2006', 'short': 'OUG nr. 99/2006', 'pad': 3, 'cc_forms': True, 'sign_tail': True,
        'ell_digit': True,  # "Articolul l58" (lowercase l for 1) in the forms of 2007-2022
        'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/78313',
        'in_force': '2007-01-01', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 1.027 of 27 December 2006, in '
                     'force on 1 January 2007 (its art. 419 alin. (1)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 99/2006: the first version is the emergency ordinance as published in Monitorul Oficial nr. 1.027 '
            'of 27 December 2006 (DetaliiDocumentAfis/78313), dated 1 January 2007, when it takes effect (its art. '
            '419 alin. (1)). The signature block printed after the last article ("PRIM-MINISTRU ...") is not part of '
            'the article.',
            'OUG nr. 99/2006: approved with amendments by Legea nr. 227/2007 (Monitorul Oficial nr. 480 of 18 July '
            '2007); the portal\'s first consolidated form (21 July 2007) carries its changes, each credited to it from '
            'the portal\'s notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/78313, Common Crawl 20260124123228)
        'label': 'OUG nr. 99/2006', 'kind': 'decree',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 1.027 din 27 decembrie 2006',
        'enacted': '2006-12-06', 'published': '2006-12-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/78313',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
