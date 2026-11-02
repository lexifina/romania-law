"""Ordonanța Guvernului nr. 26/2000 cu privire la asociații și fundații (Lexifina, 2026-11-02).

Act page 280838 (the form of 13.04.2024), base text DetaliiDocumentAfis/20740; 17 consolidated forms 03.03.2003 ..
24.07.2025, all held from Common Crawl (forms.d/og-26-2000.json, listed from the page of the newest form). Parsed as the
Phase 6 acts.
"""
SLUG = 'og-26-2000'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-og-26-2000', 'short': 'OG nr. 26/2000', 'pad': 3, 'cc_forms': True,
        'title': 'Ordonanța Guvernului nr. 26/2000 cu privire la asociații și fundații',
        'url': P.PORTAL + 'DetaliiDocument/280838',
        'in_force': '2000-04-30', 'first_law': SLUG,
        'base_note': 'The ordinance as published in Monitorul Oficial nr. 39 of 31 January 2000, in force 3 months '
                     'after publication (its art. 78): 30 April 2000.',
        'form_note': {},
        'republished': {},
        'repeal_acts': {},
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/20740, Common Crawl 20250916100015)
        'label': 'OG nr. 26/2000', 'kind': 'decree',
        'title': 'Ordonanța Guvernului nr. 26/2000 cu privire la asociații și fundații, publicată în Monitorul '
                 'Oficial al României, Partea I, nr. 39 din 31 ianuarie 2000',
        'enacted': '2000-01-30', 'published': '2000-01-31', 'url': P.PORTAL + 'DetaliiDocumentAfis/20740',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
