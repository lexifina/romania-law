"""Legea nr. 17/2014 on the sale of agricultural land outside built-up areas (Lexifina, 2026-11-02).

Act page 156290, also its base text (DetaliiDocumentAfis/156290); 7 consolidated forms (16.05.2014 .. 03.05.2024), all
held (forms.d/legea-17-2014.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-17-2014'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-17-2014', 'short': 'Legea nr. 17/2014', 'pad': 3, 'cc_forms': True,
        # the repeal notes of Legea nr. 129/2017 are printed after each "Abrogat" article (arts. 23-27); art. 22
        # quotes the articles of Legea nr. 268/2001 it rewrites (S_ART inside S_ART from 13.10.2020)
        'trailing_notes': True, 'quoted_articles': True,
        # the stubs of arts. 23-27 are printed "Abrogat" (2017) and "Abrogat." (from 2020): typesetting
        'titled_stubs': True,
        'title': 'Legea nr. 17/2014 privind unele măsuri de reglementare a vânzării-cumpărării terenurilor agricole '
                 'situate în extravilan și de modificare a Legii nr. 268/2001 privind privatizarea societăților '
                 'comerciale ce dețin în administrare terenuri proprietate publică și privată a statului cu destinație '
                 'agricolă și înființarea Agenției Domeniilor Statului',
        'url': P.PORTAL + 'DetaliiDocument/156290',
        'in_force': '2014-04-11', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 178 of 12 March 2014, in force 30 days after '
                     'publication (its art. 21 alin. (2)): 11 April 2014.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 17/2014: the first version is the law as published in Monitorul Oficial nr. 178 of 12 March '
            '2014 (DetaliiDocumentAfis/156290), in force 30 days after publication (its art. 21 alin. (2)): 11 April '
            '2014.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/156290: "București, 7 martie 2014. Nr. 17.", MO nr. 178
    # din 12 martie 2014)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 17/2014', 'kind': 'law',
        'title': 'Legea nr. 17 din 7 martie 2014, publicată în Monitorul Oficial al României, Partea I, nr. 178 din 12 '
                 'martie 2014',
        'enacted': '2014-03-07', 'published': '2014-03-12', 'url': P.PORTAL + 'DetaliiDocument/156290',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
