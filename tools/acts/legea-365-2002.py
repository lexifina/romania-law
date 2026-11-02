"""Legea nr. 365/2002 privind comerțul electronic (Lexifina, 2026-11-02).

Act page 37075, also its base text (DetaliiDocumentAfis/37075); 5 consolidated forms 21.04.2003 .. 08.10.2024
(forms.d/legea-365-2002.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-365-2002'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-365-2002', 'short': 'Legea nr. 365/2002', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 365/2002 privind comerțul electronic',
        'url': P.PORTAL + 'DetaliiDocument/37075',
        'in_force': '2002-07-05', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 483 of 5 July 2002, in force on publication '
                     '(its art. 33 alin. (2)): 5 July 2002.',
        'form_note': {'77218': 'The law as republished in Monitorul Oficial nr. 959 of 29 November 2006 under art. II '
                               'of Legea nr. 121/2006, with renumbered articles.'},
        'republished': {'77218': 'legea-121-2006'},
        'decisions': [
            'Legea nr. 365/2002: the first version is the law as published in Monitorul Oficial nr. 483 of 5 July '
            '2002 (DetaliiDocumentAfis/37075), in force on publication (its art. 33 alin. (2)): 5 July 2002. The same '
            'paragraph puts the law into application 3 months after that day; the version is dated by the in-force '
            'day.',
            'Legea nr. 365/2002: the portal\'s first consolidated form is of 21 April 2003, so the changes made up to '
            'then arrive together that day.',
            'Legea nr. 365/2002: the republication of 29 November 2006 (Monitorul Oficial nr. 959, under art. II of '
            'Legea nr. 121/2006), with renumbered articles, has no DetaliiDocument capture of its own and is read from '
            'its DetaliiDocumentAfis page (77218); changes on that day that no note explains are credited to the act '
            'that ordered the republication, as the republication note says; files follow each text\'s own numbering.',
            'Legea nr. 365/2002: the republication of 2006 and the forms up to 2014 print the law\'s mention of the '
            'directive it transposes (Directiva 2000/31/CE, with a "*" line) as the last lines of art. 32; the later '
            'forms print it after the articles. It is a note and is left out of the article.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/37075)
        'label': 'Legea nr. 365/2002', 'kind': 'law',
        'title': 'Legea nr. 365/2002 privind comerțul electronic, publicată în Monitorul Oficial al României, '
                 'Partea I, nr. 483 din 5 iulie 2002',
        'enacted': '2002-06-07', 'published': '2002-07-05', 'url': P.PORTAL + 'DetaliiDocumentAfis/37075',
    }
    # the republication of 29.11.2006 and the forms to 2014 print the law's EU-transposition mention (a "*" line and
    # "Prezenta lege transpune Directiva 2000/31/CE ...") as the last lines of art. 32; the later forms print it after
    # the articles. It is a note, not the article's text.
    P.EDITORIAL_LINES[SLUG] = {'art-032': ('*', 'Prezenta lege transpune Directiva 2000/31/CE')}
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
