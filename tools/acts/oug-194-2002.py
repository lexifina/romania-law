"""OUG nr. 194/2002 privind regimul străinilor în România (Lexifina, 2026-11-02).

Base text DetaliiDocumentAfis/41005; the portal's act page is 93712 (the republication of 2008). 34 forms listed
27.01.2004 .. 27.04.2026 (forms.d/oug-194-2002.json): the republications of 2004 (50236) and 2008 (93712) are read
from their DetaliiDocumentAfis pages, the other forms from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'oug-194-2002'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-194-2002', 'short': 'OUG nr. 194/2002', 'pad': 3, 'cc_forms': True,
        'root_word': 'act page',
        'title': 'Ordonanța de urgență a Guvernului nr. 194/2002 privind regimul străinilor în România',
        'url': P.PORTAL + 'DetaliiDocument/93712',
        'in_force': '2003-01-26', 'first_law': SLUG, 'hold': True, 'cte_notes': True,
        # the consolidator's note in art. 31 quotes the wording Legea nr. 157/2011 art. III gives arts. 29-31 and 36
        # from Romania's Schengen accession; the form of 24.12.2015 quotes art. 11's future wording the same way: each
        # quoted article follows the article in force under the same title
        'future_text': {
            '130491': {'arts': ('Articolul 29', 'Articolul 30', 'Articolul 31', 'Articolul 36')},
            '144566': {'arts': ('Articolul 29', 'Articolul 30', 'Articolul 31', 'Articolul 36')},
            '148111': {'arts': ('Articolul 29', 'Articolul 30', 'Articolul 31')},
            '174303': {'arts': ('Articolul 11',)},
        },
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 955 of 27 December 2002, in force '
                     '30 days after publication (its art. 137 alin. (1)): 26 January 2003.',
        'form_note': {
            '50236': 'The emergency ordinance as republished in Monitorul Oficial nr. 201 of 8 March 2004 under art. '
                     'III of Legea nr. 357/2003, with renumbered articles.',
            '93712': 'The emergency ordinance as republished in Monitorul Oficial nr. 421 of 5 June 2008 under art. 7 '
                     'of OUG nr. 55/2007, with renumbered articles.',
        },
        'republished': {'50236': 'legea-357-2003', '93712': 'oug-55-2007'},
        'decisions': [
            'OUG nr. 194/2002: the first version is the emergency ordinance as published in Monitorul Oficial nr. 955 '
            'of 27 December 2002 (DetaliiDocumentAfis/41005), in force 30 days after publication (its art. 137 '
            'alin. (1)): 26 January 2003. The portal\'s first form is of 27 January 2004, so the changes made up to '
            'then arrive together that day.',
            'OUG nr. 194/2002: the texts republished in Monitorul Oficial nr. 201 of 8 March 2004 (under art. III of '
            'Legea nr. 357/2003) and nr. 421 of 5 June 2008 (under art. 7 of OUG nr. 55/2007) renumber the articles; '
            'each is read from its own DetaliiDocumentAfis page (50236, 93712), changes on those days that no note '
            'explains are credited to the republishing act, as each republication note says, and files follow each '
            'text\'s own numbering.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/41005)
        'label': 'OUG nr. 194/2002', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 194 din 12 decembrie 2002 privind regimul străinilor în '
                 'România, publicată în Monitorul Oficial al României, Partea I, nr. 955 din 27 decembrie 2002',
        'enacted': '2002-12-12', 'published': '2002-12-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/41005',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
