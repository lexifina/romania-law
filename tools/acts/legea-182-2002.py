"""Legea nr. 182/2002 privind protecția informațiilor clasificate (Lexifina, 2026-11-02).

Base text DetaliiDocumentAfis/35209 (Monitorul Oficial nr. 248 of 12 April 2002); the act page 35209 shows the newest
form. 4 consolidated forms (2005-03-10 .. 2015-06-30). forms.d/legea-182-2002.json.
"""
SLUG = 'legea-182-2002'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-182-2002', 'short': 'Legea nr. 182/2002', 'pad': 3, 'titles': False,
        'cc_forms': True,
        'title': 'Legea nr. 182/2002 privind protecția informațiilor clasificate',
        'url': P.PORTAL + 'DetaliiDocument/35209',
        'in_force': '2002-06-11', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 248 of 12 April 2002, in force 60 days after '
                     'publication (its art. 43): 11 June 2002.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 182/2002: the first version is the law as published in Monitorul Oficial nr. 248 of 12 April '
            '2002 (DetaliiDocumentAfis/35209), dated 11 June 2002: its art. 43 puts it in force 60 days after '
            'publication.',
            'Legea nr. 182/2002: the portal holds no consolidated form before 10 March 2005, so the changes made '
            'between the law as published and that form arrive together that day.',
            'Legea nr. 182/2002: the portal dates its newest form 30 June 2015, the day Legea nr. 167/2015 was '
            'published, but the notes of that form date the law\'s changes (arts. 15 and 17) 3 July 2015, the day the '
            'law took effect; those changes are therefore a version of 3 July 2015, and the rest of that form (only '
            'typesetting) keeps the form\'s date.',
            'Legea nr. 182/2002: the forms of 10 March 2005 and 30 June 2015 differ from the form before them in '
            'spelling and diacritics (for example "alterarii" / "alterării", "sa" / "să") that no note explains; '
            'those changes are the publisher\'s, labelled unexplained.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the law as published (DetaliiDocumentAfis/35209)
        'label': 'Legea nr. 182/2002', 'kind': 'law',
        'title': 'Legea nr. 182/2002 privind protecția informațiilor clasificate, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 248 din 12 aprilie 2002',
        'enacted': '2002-04-12', 'published': '2002-04-12', 'url': P.PORTAL + 'DetaliiDocumentAfis/35209',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
