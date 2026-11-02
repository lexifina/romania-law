"""Legea nr. 144/2007 privind înființarea, organizarea și funcționarea Agenției Naționale de Integritate (Lexifina,
2026-11-02).

Act page 263394 (forms 30.05.2007 .. 06.01.2023, all held in forms.d/legea-144-2007.json); base text
DetaliiDocumentAfis/82317; the republication of 3 August 2009 is read from DetaliiDocumentAfis/110133. Parsed as the
Phase 6 acts.
"""
SLUG = 'legea-144-2007'

# acts read as published (their DetaliiDocumentAfis pages)
CC = {
    'dcc-415-2010': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/118456',
                     'timestamp': '20251011034605', 'crawl': 'CC-MAIN-2025-43',
                     'filename': 'crawl-data/CC-MAIN-2025-43/segments/1759648358621.26/warc/'
                                 'CC-MAIN-20251011025302-20251011055302-00471.warc.gz',
                     'offset': '343722636', 'length': '30603', 'digest': 'WEKEGSVD7ETY7MKJ5VRJJDDJTMP5PA7A'},
    'legea-176-2010': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/121924',
                       'timestamp': '20260118114044', 'crawl': 'CC-MAIN-2026-04',
                       'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469408.36/warc/'
                                   'CC-MAIN-20260118094130-20260118124130-00165.warc.gz',
                       'offset': '306686264', 'length': '50993', 'digest': 'TQ7JSO6BJQKLIOILKPWU7SS3OJXSRAFI'},
}
TITLE = 'Legea nr. 144/2007 privind înființarea, organizarea și funcționarea Agenției Naționale de Integritate'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-144-2007', 'short': 'Legea nr. 144/2007', 'pad': 3, 'cc_forms': True,
        # art. 64 rewrites articles of Legea nr. 115/1996 and the 2013 forms quote them (S_ART inside S_ART)
        'quoted_articles': True,
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
        # a Constitutional Court decision's effect (arts. 45-50 of the 2009 text) comes before the law that later
        # repealed the same articles formally (Legea nr. 176/2010 art. 33): the repeal entry names the form it applies to
        'repeals_first': True,
        'repeal_acts': {
            'dcc-415-2010': {
                'label': 'Decizia CCR nr. 415/2010', 'page': '118456', 'capture': CC['dcc-415-2010']['timestamp'],
                'cc': CC['dcc-415-2010'], 'in_force': '2010-06-19',
                'why': 'a Constitutional Court decision: the provisions it finds unconstitutional cease to have effect '
                       '45 days after its publication in Monitorul Oficial nr. 294 of 5 May 2010 (Constituția art. 147 '
                       'alin. (1)), none having been brought into line in that time',
                'read': 'point 1 of its operative part allows the exception as to art. 14 lit. c)-f) and chapter VI '
                        '"Verificarea averilor, a conflictelor de interese și a incompatibilităților" (arts. 45-50) of '
                        'Legea nr. 144/2007 (the republished numbering) and finds them unconstitutional; they ceased to '
                        'have effect 45 days after publication on 5 May 2010: 19 June 2010. The form of 20.06.2010 '
                        'leaves arts. 45-50 out with no note; the form of 05.05.2010 prints them as declared '
                        'unconstitutional and suspended.',
                'repeals': {'122231': ('art-045', 'art-046', 'art-047', 'art-048', 'art-049', 'art-050')},
                'cite': 'Art. 45-50 și-au încetat efectele juridice conform DECIZIEI CURȚII CONSTITUȚIONALE nr. 415 din '
                        '14 aprilie 2010, publicată în MONITORUL OFICIAL nr. 294 din 5 mai 2010'},
            'legea-176-2010': {
                'label': 'Legea nr. 176/2010', 'page': '121924', 'capture': CC['legea-176-2010']['timestamp'],
                'cc': CC['legea-176-2010'], 'in_force': '2010-09-05',
                'why': 'it sets no day of its own: in force 3 days after publication in Monitorul Oficial nr. 621 of 2 '
                       'September 2010 (Constituția art. 78)',
                'read': 'art. 33 (title II) rewrites Legea nr. 144/2007 point by point; its pct. 1 ("Articolele 1-12 se '
                        'abrogă"), pct. 3 ("Articolul 14 se abrogă"), pct. 6 ("Articolul 17 se abrogă") and pct. 16 '
                        '("Articolele 41-57 se abrogă") repeal the articles the form of 05.09.2010 leaves out.'},
        },
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
