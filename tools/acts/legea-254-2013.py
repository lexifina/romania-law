"""Legea nr. 254/2013 privind executarea pedepselor și a măsurilor privative de libertate dispuse de organele judiciare
în cursul procesului penal (Lexifina, 2026-11-02).

Act page 150699, also its base text (DetaliiDocumentAfis/150699); 16 consolidated forms 07.02.2014 .. 10.05.2024, all
held (forms.d/legea-254-2013.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-254-2013'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-254-2013', 'short': 'Legea nr. 254/2013', 'pad': 3, 'cc_forms': True,
        'trailing_notes': True,
        'title': 'Legea nr. 254/2013 privind executarea pedepselor și a măsurilor privative de libertate dispuse de '
                 'organele judiciare în cursul procesului penal',
        'url': P.PORTAL + 'DetaliiDocument/150699',
        'in_force': '2014-02-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 514 of 14 August 2013, in force with the Criminal '
                     'Code and the Code of Criminal Procedure on 1 February 2014 (its art. 187 alin. (1)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 254/2013: the first version is the law as published in Monitorul Oficial nr. 514 of 14 August '
            '2013 (DetaliiDocumentAfis/150699), dated 1 February 2014, the day its art. 187 alin. (1) puts it in force '
            'with Legea nr. 286/2009 (Codul penal) and Legea nr. 135/2010 (Codul de procedură penală). Art. 187 alin. '
            '(2) alone took effect earlier, 5 days after publication; the record has no version before 1 February '
            '2014, so that provision is shown from that day with the rest of the text. The portal\'s first form is of '
            '7 February 2014, so the changes made up to then arrive together that day.',
            'Legea nr. 254/2013: the portal\'s act page as captured on 9 August 2025 '
            'shows the form of 10 May 2024 as the newest, and the Afis page captured on 21 January 2026 lists no '
            'later form; the record ends there and no repeal is made up.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS.setdefault(SLUG, {  # read from the act as published (DetaliiDocumentAfis/150699)
        'label': 'Legea nr. 254/2013', 'kind': 'law',
        'title': 'Legea nr. 254 din 19 iulie 2013, publicată în Monitorul Oficial al României, Partea I, nr. 514 din '
                 '14 august 2013',
        'enacted': '2013-07-19', 'published': '2013-08-14', 'url': P.PORTAL + 'DetaliiDocumentAfis/150699',
    })
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
