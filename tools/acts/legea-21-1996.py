"""Legea concurenței nr. 21/1996 (competition law): Lexifina, 2026-11-02.

Act page 8005, also its base text (DetaliiDocumentAfis/8005). 42 forms listed by DetaliiDocumentAfis/157060 as captured
on 2026-06-06 (Common Crawl), 17.12.2002 .. 13.03.2026; 41 held from Common Crawl (forms.d/legea-21-1996.json): own
pages, three consolidations from their DetaliiDocumentAfis pages (which mark the form shown), the newest held form
(26.06.2025) from the act page, the republications of 2005, 2014 and 2016 from their DetaliiDocumentAfis pages. The
form of 13.03.2026 (307731) is in neither archive.
"""
SLUG = 'legea-21-1996'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'oug-75-2010': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/120247', 'timestamp': '20260712021710',
                    'crawl': 'CC-MAIN-2026-30',
                    'filename': 'crawl-data/CC-MAIN-2026-30/segments/1783663951536.14/warc/'
                                'CC-MAIN-20260712015859-20260712045859-00712.warc.gz',
                    'offset': '306288803', 'length': '50817', 'digest': 'RHKZ6JBVYTZYAWHX67CNA2LDBOHHJDJT'},
    'legea-149-2011': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/129971',
                       'timestamp': '20251216092753', 'crawl': 'CC-MAIN-2025-51',
                       'filename': 'crawl-data/CC-MAIN-2025-51/segments/1764871656797.88/warc/'
                                   'CC-MAIN-20251216074501-20251216104501-00645.warc.gz',
                       'offset': '263499881', 'length': '30173', 'digest': 'I2EQLLAOYL4NIXZXMA3LRRQLQ3CO5GQT'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-21-1996', 'short': 'Legea nr. 21/1996', 'pad': 3, 'cc_forms': True, 'ccr_revert': True, 'mod_lines': True,
        'title': 'Legea concurenței nr. 21/1996',
        'url': P.PORTAL + 'DetaliiDocument/8005',
        'in_force': '1997-01-30', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 88 of 30 April 1996, in force 9 months after '
                     'publication (its art. 73 alin. (1)): 30 January 1997.',
        'form_note': {'64226': 'The law as republished in Monitorul Oficial nr. 742 of 16 August 2005 under art. III '
                               'of Legea nr. 538/2004, with renumbered articles.',
                      '157060': 'The law as republished in Monitorul Oficial nr. 240 of 3 April 2014 under art. 107 '
                                'alin. (3) of Legea nr. 255/2013, with renumbered articles.',
                      '176165': 'The law as republished in Monitorul Oficial nr. 153 of 29 February 2016 under art. '
                                'III of Legea nr. 347/2015, with renumbered articles.'},
        'republished': {'64226': 'legea-538-2004', '157060': 'legea-255-2013', '176165': 'legea-347-2015'},
        'repeal_acts': {
            'oug-75-2010': {
                'label': 'OUG nr. 75/2010', 'page': '120247', 'capture': CC['oug-75-2010']['timestamp'],
                'cc': CC['oug-75-2010'], 'in_force': '2010-08-05',
                'why': 'its art. IV alin. (1): in force 30 days after publication in Monitorul Oficial nr. 459 of 6 '
                       'July 2010',
                'read': 'art. I pct. 5: "Articolul 7 se abrogă."; pct. 11: "Articolul 13 se abrogă."; pct. 31: '
                        '"Articolul 39 se abrogă."; pct. 55: "Articolul 63 se abrogă."; pct. 59: "Articolul 67 se '
                        'abrogă."'},
            'legea-149-2011': {
                'label': 'Legea nr. 149/2011', 'page': '129971', 'capture': CC['legea-149-2011']['timestamp'],
                'cc': CC['legea-149-2011'], 'in_force': '2011-07-14',
                'why': 'a law with no general in-force clause of its own (its art. II defers only art. 17 alin. (1) '
                       'of Legea nr. 21/1996): 3 days after publication in Monitorul Oficial nr. 490 of 11 July 2011 '
                       '(Constituția art. 78)',
                'read': 'art. I pct. 29, approving OUG nr. 75/2010, inserts in its art. I pct. 40^1: "Articolul 48 se '
                        'abrogă."'},
        },
        # Legea nr. 149/2011 art. II: art. 17 alin. (1) as it rewrites it takes effect one year after the law
        # (14.07.2011), so on 14.07.2012; the forms print the new wording from 14.07.2011
        'later_provisions': (
            {'day': '2012-07-14', 'law': 'legea-149-2011',
             'lines': ('(1) Plenul Consiliului Concurenței este un organ colegial și este format din 7 membri, după cum '
                       'urmează: un președinte, 2 vicepreședinți și 4 consilieri de concurență. Numirea membrilor '
                       'Plenului Consiliului Concurenței se realizează de către Președintele României, la propunerea '
                       'Colegiului Consultativ',),
             'old': {'(1) Plenul Consiliului Concurenței este un organ colegial și este format din 7 membri, după cum '
                     'urmează: un președinte, 2 vicepreședinți și 4 consilieri de concurență. Numirea membrilor '
                     'Plenului Consiliului Concurenței se realizează de către Președintele României, la propunerea '
                     'Colegiului Consultativ':
                     '(1) Plenul Consiliului Concurentei este un organ colegial și este format din 7 membri, după cum '
                     'urmeaza: un presedinte, 2 vicepresedinti și 4 consilieri de concurenta. Numirea membrilor '
                     'Plenului Consiliului Concurentei se realizează de către Președintele României, la propunerea '
                     'Guvernului.'},
             'note': 'Art. 17 alin. (1) in the wording of Legea nr. 149/2011 (art. I pct. 8) takes effect on this day, '
                     'one year after that law (its art. II); the portal prints it from its form of 14.07.2011.'},
        ),
        'decisions': [
            'Legea nr. 21/1996: the first version is the law as published in Monitorul Oficial nr. 88 of 30 April '
            '1996 (DetaliiDocumentAfis/8005), in force 9 months after publication (its art. 73 alin. (1)): 30 '
            'January 1997. The provisions setting up and organising the Consiliul Concurenței and the Oficiul '
            'Concurenței took effect on publication (the same article); they are shown from 30 January 1997 with the '
            'rest. The portal\'s first form is of 17 December 2002, so the changes made up to then arrive together '
            'that day.',
            'Legea nr. 21/1996: the republications of 16 August 2005 (art. III of Legea nr. 538/2004), 3 April 2014 '
            '(art. 107 alin. (3) of Legea nr. 255/2013) and 29 February 2016 (art. III of Legea nr. 347/2015), each '
            'with renumbered articles, are read from their own pages (DetaliiDocumentAfis/64226, 157060, 176165); '
            'changes on those days that no note explains are credited to the act that ordered the republication, as '
            'each republication note says; files follow each text\'s own numbering.',
            'Legea nr. 21/1996: the forms of 30 January 2017, 8 July 2017 and 19 April 2019 have no capture of '
            'their own page; each is read from its DetaliiDocumentAfis page, which marks that form as the one shown '
            'in its list of forms. The form of 26 June 2025 is read from the act page (DetaliiDocument/8005) as '
            'captured on 7 February 2026, when it showed that form.',
            'Legea nr. 21/1996: Legea nr. 149/2011 (art. I pct. 8) rewrites art. 17 alin. (1), but its art. II puts '
            'that alineat in force one year after the law itself (in force 14 July 2011): on 14 July 2012. The '
            'portal prints the new wording from its form of 14 July 2011. Under the rule for text printed before its '
            'law, the earlier wording of alin. (1), as the previous forms print it, stands until 14 July 2012, when '
            'the new wording takes effect, credited to Legea nr. 149/2011.',
            'Legea nr. 21/1996: the portal\'s notes on arts. 8 and 15 name orders of the Consiliul Concurenței '
            '(Ordinul nr. 13/2001 and nr. 216/2002) that raised the turnover thresholds the law lets the Council set. '
            'An order is not credited as a law: the threshold in art. 15 that changes with the form of 17 December '
            '2002 is committed as the publisher\'s, and the orders\' text that the forms of 17 December 2002 to 3 '
            'December 2004 quote at the end of art. 8 ("Plafonul privind cifra de afaceri ... se majorează ...") is '
            'not the law\'s text and is left out. The 2005, 2009 and early 2014 texts print a lone "*" as the last '
            'line of art. 67 (the opening of the closing note); it is left out.',
            'Legea nr. 21/1996: the forms from 6 September 2020 print the portal\'s notes that provisions went back to '
            'their earlier wording, were removed or were put back in force because Decizia Curții Constituționale nr. '
            '239/2020 (Monitorul Oficial nr. 649 of 23 July 2020; read as published, DetaliiDocumentAfis/228306) '
            'found OUG nr. 39/2017 unconstitutional as a whole, the ordinance ceasing to have effect 45 days after '
            'publication, on 6 September 2020 (Constituția art. 147 alin. (1)), the form\'s date; the decision is '
            'credited with those changes. The form of 5 September 2009 likewise notes that art. 28 alin. (2) ceased to '
            'have effect under Decizia Curții Constituționale nr. 1.037/2009 (Monitorul Oficial nr. 501 of 21 July '
            '2009); the decision is credited with that change, dated by the form.',
        ],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/8005, Common Crawl 20260122135056)
        'label': 'Legea nr. 21/1996', 'kind': 'law',
        'title': 'Legea concurenței nr. 21/1996, publicată în Monitorul Oficial al României, Partea I, nr. 88 din 30 '
                 'aprilie 1996',
        'enacted': '1996-04-10', 'published': '1996-04-30', 'url': P.PORTAL + 'DetaliiDocumentAfis/8005',
    }
    # the forms of 17.12.2002 to 03.12.2004 print, at the end of art. 8, the Council's orders raising the turnover
    # threshold (quoted); the 2005, 2009 and 2014 texts print a lone "*" (the start of a closing note) in art. 67
    P.EDITORIAL_LINES[SLUG] = {'art-008': ('"Plafonul privind cifra de afaceri',), 'art-067': ('*',)}
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
