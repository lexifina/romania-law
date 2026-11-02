"""Legea nr. 144/2007 privind înființarea, organizarea și funcționarea Agenției Naționale de Integritate (Lexifina,
2026-11-02).

Act page 263394 (forms 30.05.2007 .. 06.01.2023, all held in forms.d/legea-144-2007.json); base text
DetaliiDocumentAfis/82317; the republication of 3 August 2009 is read from DetaliiDocumentAfis/110133. Parsed as the
Phase 6 acts.
"""
SLUG = 'legea-144-2007'
TITLE = 'Legea nr. 144/2007 privind înființarea, organizarea și funcționarea Agenției Naționale de Integritate'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-144-2007', 'short': 'Legea nr. 144/2007', 'pad': 3, 'cc_forms': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/263394',
        'in_force': '2007-05-28', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 359 of 25 May 2007. Under its art. 59 alin. (1) '
                     'chapters III and IV are in force 3 days after publication (28 May 2007) and chapters I, II and '
                     'V-VII 6 months after publication (25 November 2007); the whole text is shown from 28 May 2007.',
        'form_note': {'110133': 'The law as republished in Monitorul Oficial nr. 535 of 3 August 2009 under art. II of '
                                'Ordonanța de urgență a Guvernului nr. 138/2007, with renumbered articles.'},
        'republished': {'110133': 'oug-138-2007'},
        'decisions': [
            'Legea nr. 144/2007: the first version is the law as published in Monitorul Oficial nr. 359 of 25 May '
            '2007 (DetaliiDocumentAfis/82317). Its art. 59 alin. (1) puts chapters III and IV (the Agency and the '
            'National Integrity Council) in force 3 days after publication, 28 May 2007, and chapters I, II and V-VII '
            '6 months after publication, 25 November 2007; the whole text is shown from 28 May 2007, as the law prints '
            'it. The portal\'s first form is of 30 May 2007, so the changes made up to then arrive together that day.',
            'Legea nr. 144/2007: the republication of 3 August 2009 (Monitorul Oficial nr. 535, under art. II of '
            'Ordonanța de urgență a Guvernului nr. 138/2007, with renumbered articles) is read from its own page '
            '(DetaliiDocumentAfis/110133); changes on that day that no note explains are credited to the act that '
            'ordered the republication, as the republication note says; files follow each text\'s own numbering.',
        ],
        'repeal_acts': {},
        'root_word': 'act page',
    }
    # dates read from the act as published (DetaliiDocumentAfis/82317: "București, 21 mai 2007. Nr. 144.", Monitorul
    # Oficial nr. 359 din 25 mai 2007)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 144/2007', 'kind': 'law',
        'title': 'Legea nr. 144 din 21 mai 2007, publicată în Monitorul Oficial al României, Partea I, nr. 359 din '
                 '25 mai 2007',
        'enacted': '2007-05-21', 'published': '2007-05-25', 'url': P.PORTAL + 'DetaliiDocumentAfis/82317',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
