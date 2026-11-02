"""Legea nr. 51/1995 pentru organizarea și exercitarea profesiei de avocat (Lexifina, 2026-11-02).

Act page 126008 (also the 2011 republication); the portal's base form 282141 is the 2018 republication, so the record
starts at the 2001 republication 27141 (no_base, coordinator ruling). 38 forms, all held from archive.org (forms.json
entry `legea-51-1995`, written in an earlier phase; republications 27141, 126008, 201006 via afis_ia). The acts that
settle the dropped articles were read as published from Common Crawl (repeal_acts entries with 'cc')."""

SLUG = 'legea-51-1995'


def _cc(doc, ts, crawl, filename, offset, length, digest):
    return {'url': f'https://legislatie.just.ro/Public/DetaliiDocumentAfis/{doc}', 'timestamp': ts, 'crawl': crawl,
            'filename': filename, 'offset': offset, 'length': length, 'digest': digest}


CC = {
    'oug-159-2008': _cc('99574', '20250814213020', 'CC-MAIN-2025-33',
                        'crawl-data/CC-MAIN-2025-33/segments/1754151577363.78/warc/'
                        'CC-MAIN-20250814193753-20250814223753-00768.warc.gz', '268231695', '27945',
                        'H2SAXNTTHZRKWHW3GU7PWX6SQ7MTRXFM'),
    'legea-280-2004': _cc('53026', '20251113153346', 'CC-MAIN-2025-47',
                          'crawl-data/CC-MAIN-2025-47/segments/1762439343660.93/warc/'
                          'CC-MAIN-20251113133203-20251113163203-00980.warc.gz', '292211235', '13612',
                          'IDQQTLLXBM6IGMTJR5Q7WA5I25BO6MGV'),
    'legea-270-2010': _cc('124791', '20251205121702', 'CC-MAIN-2025-51',
                          'crawl-data/CC-MAIN-2025-51/segments/1764871306999.25/warc/'
                          'CC-MAIN-20251205103933-20251205133933-00830.warc.gz', '329996319', '29346',
                          'EYEI5GFHBFVL4KI4RCAIOGNOXNBJFAGX'),
    'dcc-109-2010': _cc('117182', '20260117013703', 'CC-MAIN-2026-04',
                        'crawl-data/CC-MAIN-2026-04/segments/1768220469321.37/warc/'
                        'CC-MAIN-20260116234127-20260117024127-00886.warc.gz', '286856055', '13614',
                        'B5XHKHNUHSOIHYRSA4UGLNDSRIE43CG4'),
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-51-1995', 'short': 'Legea nr. 51/1995', 'pad': 3,
        'split_same': True, 'cc_acts': True, 'revert_prin': True, 'reprint_law': True,
        'title': 'Legea nr. 51/1995 pentru organizarea și exercitarea profesiei de avocat',
        'url': P.PORTAL + 'DetaliiDocument/126008',
        'no_base': True, 'in_force': '2001-03-06', 'first_law': None,
        'earlier_laws': ['legea-51-1995', 'legea-231-2000'],
        'base_note': 'Oldest version available: the law as republished in Monitorul Oficial nr. 113 of 6 March 2001 '
                     'under art. V of Legea nr. 231/2000, with renumbered articles. The law was enacted on 7 June 1995 '
                     'and first published in Monitorul Oficial nr. 116 of 9 June 1995; that text is not part of this '
                     'record.',
        'form_note': {'126008': 'The law as republished in Monitorul Oficial nr. 98 of 7 February 2011 under art. VI '
                                'of Legea nr. 270/2010, with renumbered articles.',
                      '201006': 'The law as republished in Monitorul Oficial nr. 440 of 24 May 2018 under art. II of '
                                'Legea nr. 25/2017, with renumbered articles.'},
        'republished': {'126008': 'legea-270-2010', '201006': 'legea-25-2017'},
        # coordinator rulings: the text of art. 44^1 leaves the law on 2 July 2004 (Legea nr. 280/2004); art. 68^14
        # ceases on 3 May 2010 (Decizia CCR nr. 109/2010)
        'eliminated': {'art-044-1': '54084', 'art-068-14': '118647'},
        'repeal_acts': {
            'oug-159-2008': {
                'label': 'OUG nr. 159/2008', 'page': '99574', 'capture': CC['oug-159-2008']['timestamp'],
                'cc': CC['oug-159-2008'], 'in_force': '2008-11-26',
                'why': 'an emergency ordinance with no general in-force clause of its own (its art. III and IV defer '
                       'only the provisions on professional limited-liability companies and art. I pct. 6): in force '
                       'on publication in Monitorul Oficial nr. 792 of 26 November 2008',
                'read': 'art. I pct. 8: "Articolul 16^1 se abrogă."; pct. 30 rewrites chapter V and inserts arts. '
                        '68^1-68^14 (art. 68^14: "U.N.B.R. şi barourile conlucrează cu Ministerul Justiţiei ...").'},
            'legea-270-2010': {
                'label': 'Legea nr. 270/2010', 'page': '124791', 'capture': CC['legea-270-2010']['timestamp'],
                'cc': CC['legea-270-2010'], 'in_force': '2010-12-31',
                'why': 'a law with no in-force clause of its own: 3 days after publication in Monitorul Oficial nr. '
                       '872 of 28 December 2010 (Constituția art. 78)',
                'read': 'art. I pct. 41: "Articolul 77 se abrogă."; pct. 8: "Articolul 16^1 se abrogă."; pct. 38-39 '
                        'insert arts. 68^1-68^13 (no art. 68^14); art. VI orders the republication with renumbered '
                        'articles.'},
            'legea-280-2004': {
                'label': 'Legea nr. 280/2004', 'page': '53026', 'capture': CC['legea-280-2004']['timestamp'],
                'cc': CC['legea-280-2004'], 'in_force': '2004-07-02',
                'why': 'a law with no in-force clause of its own: 3 days after publication in Monitorul Oficial nr. '
                       '574 of 29 June 2004 (Constituția art. 78)',
                'read': 'articol unic pct. 1-2: approving OUG nr. 77/2003, it rewrites the ordinance\'s title and its '
                        'art. I so that the ordinance inserts art. 82^1 into Legea nr. 161/2003 instead of art. 44^1 '
                        'into Legea nr. 51/1995 ("După articolul 82 din Legea nr. 161/2003 ... se introduce un articol '
                        'nou, articolul 82^1"); art. 44^1 of Legea nr. 51/1995 (inserted by OUG nr. 77/2003 art. I, '
                        'Monitorul Oficial nr. 640 of 9 September 2003) leaves the law that day. The form of '
                        '02.07.2004 prints it as a bare "ART. 44^1 *)" paragraph inside art. 44.',
                'repeals': {'54084': ('art-044-1',)},
                'cite': 'Art. 44^1 a fost eliminat prin LEGEA nr. 280 din 23 iunie 2004, publicată în MONITORUL '
                        'OFICIAL nr. 574 din 29 iunie 2004'},
            'dcc-109-2010': {
                'label': 'Decizia CCR nr. 109/2010', 'page': '117182', 'capture': CC['dcc-109-2010']['timestamp'],
                'cc': CC['dcc-109-2010'], 'in_force': '2010-05-03',
                'why': 'a Constitutional Court decision published in Monitorul Oficial nr. 175 of 18 March 2010: the '
                       'provisions it finds unconstitutional are suspended for 45 days from publication (18 March - 2 '
                       'May 2010) and, none having been brought into line, cease to have effect from 3 May 2010 '
                       '(Constituția art. 147 alin. (1))',
                'read': 'it admits the exception and finds the provisions of OUG nr. 159/2008 unconstitutional (art. '
                        '115 alin. (4) of the Constitution); art. I pct. 30 of that ordinance inserted art. 68^14. The '
                        'form of 03.05.2010 still prints it, with the portal\'s note that it ceased to have effect '
                        'from 3 May 2010.',
                'repeals': {'118647': ('art-068-14',)},
                'cite': 'Art. 68^14 și-a încetat efectele juridice conform DECIZIEI CURȚII CONSTITUȚIONALE nr. 109 din '
                        '9 februarie 2010, publicată în MONITORUL OFICIAL nr. 175 din 18 martie 2010'},
        },
        'decisions': [
            'Legea nr. 51/1995: the base text is missing. The portal\'s base form (DetaliiDocumentAfis/282141) shows '
            'the law as republished in 2018, not the 1995 text. The record starts at the oldest form held, the law as '
            'republished in Monitorul Oficial nr. 113 of 6 March 2001 under art. V of Legea nr. 231/2000 (enacted 4 '
            'December 2000, published in Monitorul Oficial nr. 635 of 7 December 2000), credited to the publisher as '
            'the oldest version available; that text already holds the changes made by OUG nr. 85/1997 and Legea nr. '
            '231/2000, as its republication note says. No enacted version is made up; the law\'s enactment (7 June '
            '1995) and first publication (9 June 1995) are kept in its metadata.',
            'Legea nr. 51/1995: the portal holds no consolidated form between the republication of 6 March 2001 and '
            '9 September 2003, so the changes made in between (Legea nr. 489/2002) arrive together that day.',
            'Legea nr. 51/1995: the republications of 7 February 2011 (art. VI of Legea nr. 270/2010, enacted 22 '
            'December 2010, published in Monitorul Oficial nr. 872 of 28 December 2010) and 24 May 2018 (art. II of '
            'Legea nr. 25/2017, enacted 24 March 2017, published in Monitorul Oficial nr. 210 of 28 March 2017), each '
            'with renumbered articles, are read from their own pages (DetaliiDocumentAfis/126008 and 201006); changes '
            'on those days that no note explains are credited to the law that ordered the republication, as each '
            'republication note says; files follow each text\'s own numbering, so many change those days.',
            'Legea nr. 51/1995: art. 44^1, inserted by OUG nr. 77/2003 (in force on publication, 9 September 2003), '
            'leaves the law on 2 July 2004: Legea nr. 280/2004, approving the ordinance, moved its text into Legea nr. '
            '161/2003 as art. 82^1 (read as published). The form of 2 July 2004 prints it as a bare paragraph "ART. '
            '44^1 *)" inside art. 44, which is filed as its own article and then left out; the forms of 3 September '
            '2004 to 25 August 2006 still print its text, and those of 18 March and 13 May 2010 print it as '
            '"Eliminat." with the portal\'s note; these prints are the publisher\'s error and are left out, so the '
            'article stays out from 2 July 2004 (coordinator ruling).',
            'Legea nr. 51/1995: art. 68^14, inserted by OUG nr. 159/2008 (26 November 2008), ceases to have effect on '
            '3 May 2010 under Decizia Curții Constituționale nr. 109/2010 (Monitorul Oficial nr. 175 of 18 March 2010), '
            'which found the whole ordinance unconstitutional: suspended from 18 March to 2 May 2010, ceased from 3 '
            'May 2010 (Constituția art. 147 alin. (1); coordinator ruling). The forms of 3 May 2010 (text) and 13 May '
            '2010 ("Eliminat.") still print it and are left out for it. Legea nr. 81/2010 (Monitorul Oficial nr. 300 '
            'of 10 May 2010, read as published: DetaliiDocumentAfis/118539, Common Crawl CC-MAIN-2025-51), which '
            'rejected OUG nr. 159/2008 and on which the portal\'s "Eliminat." note on art. 68^14 relies, came after '
            'the cessation and is not credited for that article.',
            'Legea nr. 51/1995: the other changes of OUG nr. 159/2008 are shown as the portal\'s forms print them: the '
            'forms of 18 March and 3 May 2010 still print the ordinance\'s wording, with the portal\'s notes that it '
            'was found unconstitutional, suspended and then ceased (those notes, printed as paragraphs, are left '
            'out); the form of 13 May 2010 prints the earlier wording again, or "Eliminat." for the provisions the '
            'ordinance had inserted, and its notes name Legea nr. 81/2010, which is credited with those changes.',
            'Legea nr. 51/1995: art. 16^1 (inserted by Legea nr. 255/2004) is left out by the form of 26 November 2008 '
            'and dated as repealed that day by OUG nr. 159/2008 art. I pct. 8 (the portal\'s note; the ordinance read '
            'as published). The forms of 18 March and 13 May 2010 print it as "Abrogat." with the portal\'s notes '
            'that the repeal was suspended and then ceased, and, in the second, that art. 16^1 had already ceased to '
            'have effect under Decizia Curții Constituționale nr. 513/2006 (Monitorul Oficial nr. 598 of 11 July 2006); '
            'the forms of 2006-2008 print its text, so the record follows them. Arts. 31^1 and 37^1, repealed in 2004 '
            'and 2005 and printed as "Abrogat.", are left out by some forms of 2008-2010 and carried as repealed.',
            'Legea nr. 51/1995: the form of 26 November 2008 prints art. 68^10 run into art. 68^9 ("Art. 68^10. - (1) '
            'Pentru înscrierea ..."); it is filed as its own article. Its note is printed on art. 68^9, so art. 68^10 '
            'is not credited that day and is committed as the publisher\'s (OUG nr. 159/2008 art. I pct. 30 inserted '
            'it).',
            'Legea nr. 51/1995: from the form of 26 November 2008 the portal reprints the older undated notes in new '
            'wording ("Art. 1 a fost modificat de pct. 1 al art. I din LEGEA nr. 255 din 16 iunie 2004, publicată ..." '
            'for "Art. 1 a fost modificat de LEGEA nr. 255 din 16 iunie 2004 publicată ..."); a reworded note naming a '
            'law already noted on that article is the same note, so the typesetting changes printed with it are '
            'committed as the publisher\'s, not credited to that law again.',
        ],
    }
    P.BASE_LAWS.setdefault(SLUG, {  # from the 2001 republication's heading (DetaliiDocumentAfis/27141)
        'label': 'Legea nr. 51/1995', 'kind': 'law',
        'title': 'Legea nr. 51/1995 pentru organizarea și exercitarea profesiei de avocat, publicată în Monitorul '
                 'Oficial al României, Partea I, nr. 116 din 9 iunie 1995',
        'enacted': '1995-06-07', 'published': '1995-06-09', 'url': None,
    })
    P.BASE_LAWS.setdefault('legea-231-2000', {  # read as published (DetaliiDocumentAfis/25399, CC-MAIN-2025-43)
        'label': 'Legea nr. 231/2000', 'kind': 'law',
        'title': 'Legea nr. 231/2000 privind modificarea și completarea Legii nr. 51/1995 pentru organizarea și '
                 'exercitarea profesiei de avocat, publicată în Monitorul Oficial al României, Partea I, nr. 635 din 7 '
                 'decembrie 2000',
        'enacted': '2000-12-04', 'published': '2000-12-07', 'url': P.PORTAL + 'DetaliiDocumentAfis/25399',
    })
    P.BASE_LAWS.setdefault('legea-270-2010', {  # read as published (DetaliiDocumentAfis/124791, CC-MAIN-2025-51)
        'label': 'Legea nr. 270/2010', 'kind': 'law',
        'title': 'Legea nr. 270/2010 privind modificarea și completarea Legii nr. 51/1995 pentru organizarea și '
                 'exercitarea profesiei de avocat, publicată în Monitorul Oficial al României, Partea I, nr. 872 din '
                 '28 decembrie 2010',
        'enacted': '2010-12-22', 'published': '2010-12-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/124791',
    })
    P.BASE_LAWS.setdefault('legea-25-2017', {  # read as published (DetaliiDocumentAfis/187749, CC-MAIN-2026-08)
        'label': 'Legea nr. 25/2017', 'kind': 'law',
        'title': 'Legea nr. 25/2017 privind modificarea și completarea Legii nr. 51/1995 pentru organizarea și '
                 'exercitarea profesiei de avocat, publicată în Monitorul Oficial al României, Partea I, nr. 210 din '
                 '28 martie 2017',
        'enacted': '2017-03-24', 'published': '2017-03-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/187749',
    })
    # the forms of 3 May, 13 May and 31 December 2010 print the portal's pointer to its note at the head of the act as
    # the last paragraph of each article OUG nr. 159/2008 had changed
    P.EDITORIAL_LINES[SLUG] = {k: ('A se vedea Nota * de la începutul actului.',) for k in (
        'art-005', 'art-005-1', 'art-006', 'art-007', 'art-008', 'art-011', 'art-012', 'art-013', 'art-016',
        'art-016-1', 'art-017', 'art-020', 'art-023', 'art-025', 'art-027', 'art-032', 'art-035', 'art-037', 'art-042',
        'art-049', 'art-050', 'art-052', 'art-052-1', 'art-053', 'art-057', 'art-063', 'art-068', 'art-068-1',
        'art-068-10', 'art-068-11', 'art-068-12', 'art-068-13', 'art-068-14', 'art-068-2', 'art-068-3', 'art-068-4',
        'art-068-5', 'art-068-6', 'art-068-7', 'art-068-8', 'art-068-9', 'art-069')}
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
