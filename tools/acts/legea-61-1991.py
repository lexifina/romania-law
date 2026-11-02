"""Legea nr. 61/1991 pentru sancționarea faptelor de încălcare a unor norme de conviețuire socială, a ordinii și liniștii
publice (Lexifina, 2026-11-02).

Act page 1534, also the text as published (DetaliiDocumentAfis/1534). 24 forms 24.01.1997 .. 13.06.2026 are listed
(forms.d/legea-61-1991.json); the form of 27.03.2026 (307796) is held by no archive, the others are held. Parsed as the
Phase 6 acts.
"""
SLUG = 'legea-61-1991'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-61-1991', 'short': 'Legea nr. 61/1991', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'root_word': 'act page',
        'title': 'Legea nr. 61/1991 pentru sancționarea faptelor de încălcare a unor norme de conviețuire socială, '
                 'a ordinii și liniștii publice',
        'url': P.PORTAL + 'DetaliiDocument/1534',
        'in_force': '1991-09-27', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 196 of 27 September 1991; it sets no day of its '
                     'own, so in force on publication (Constituția of 1991, art. 78, which applied until 29 October '
                     '2003).',
        'form_note': {
            '1535': 'The law as republished on 24 January 1997 under art. II of Legea nr. 132/1996.',
            '23832': 'The law as republished on 18 August 2000 under art. II of Legea nr. 2/2000.',
            '125693': 'The law as republished on 31 January 2011 under art. II of Legea nr. 153/2010.',
            '155343': 'The law as republished on 7 February 2014 under art. 248 of Legea nr. 187/2012.',
            '223135': 'The law as republished on 18 February 2020 under art. V of Legea nr. 192/2019.'},
        'republished': {'1535': 'legea-132-1996', '23832': 'legea-2-2000', '125693': 'legea-153-2010',
                        '155343': 'legea-187-2012', '223135': 'legea-192-2019'},
        'decisions': [
            'Legea nr. 61/1991: the first version is the law as published in Monitorul Oficial nr. 196 of 27 '
            'September 1991 (DetaliiDocumentAfis/1534), dated 27 September 1991: it sets no day of its own, so in '
            'force on publication (Constituția of 1991, art. 78, which applied until 29 October 2003). The portal '
            'holds no consolidated form before 24 January 1997, so the changes made up to then arrive together that '
            'day.',
            'Legea nr. 61/1991: the republication of 24 January 1997 (1535) is credited, for the changes no note '
            'explains, to Legea nr. 132/1996, under whose art. II it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 18 August 2000 (23832) is credited, for the changes no note '
            'explains, to Legea nr. 2/2000, under whose art. II it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 31 January 2011 (125693) is credited, for the changes no note '
            'explains, to Legea nr. 153/2010, under whose art. II it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 7 February 2014 (155343) is credited, for the changes no note '
            'explains, to Legea nr. 187/2012, under whose art. 248 it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 18 February 2020 (223135) is credited, for the changes no note '
            'explains, to Legea nr. 192/2019, under whose art. V it was republished, as its own note says.',
            'Legea nr. 61/1991: the portal lists a form of 27 March 2026 (307796) that no archive holds; the act page '
            'captured in July 2026 shows the form of 13 June 2026. The record ends with that form, and the changes '
            'made on 27 March 2026 arrive together with those of 13 June 2026.',
            'Legea nr. 61/1991: arts. 11-16 are left out of the form of 29 September 2002 with no note. OG nr. 55/2002 '
            '(Monitorul Oficial nr. 642 of 30 August 2002, read as published, DetaliiDocumentAfis/38212) repeals them '
            'in its art. 28 and takes effect 30 days after publication (art. 27), on 29 September 2002, the day of '
            'the form; the repeal is dated by the act.',
            'Legea nr. 61/1991: arts. 4, 5 and 10 are left out of the form of 22 July 2010 with no note. Legea nr. '
            '153/2010 (Monitorul Oficial nr. 496 of 19 July 2010, read as published, DetaliiDocumentAfis/120675) '
            'repeals them in art. I pct. 2 and 4; it sets no day of its own, so it took effect 3 days after '
            'publication (Constituția art. 78), on 22 July 2010, the day of the form; the repeal is dated by the act.',
        ],
        'repeal_acts': {
            'og-55-2002': {
                'label': 'OG nr. 55/2002', 'page': '38212', 'capture': '20251114111329',
                'cc': {'crawl': 'CC-MAIN-2025-47', 'timestamp': '20251114111329',
                       'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439343932.66/warc/'
                                   'CC-MAIN-20251114104301-20251114134301-00780.warc.gz',
                       'offset': '302316931', 'length': '23362',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/38212'},
                'in_force': '2002-09-29',
                'why': 'its art. 27: in force 30 days after publication in Monitorul Oficial nr. 642 of 30 August '
                       '2002',
                'read': 'art. 28: "Pe data intrării în vigoare a prezentei ordonanțe se abroga ... alin. 3 și 4 ale '
                        'art. 10 și art. 11-16 din Legea nr. 61/1991 ..."; the form of 29.09.2002 leaves arts. 11-16 '
                        'out with no note.',
                'repeals': {'41204': ('art-011', 'art-012', 'art-013', 'art-014', 'art-015', 'art-016')},
                'cite': 'Art. 11-16 au fost abrogate de art. 28 din ORDONANTA nr. 55 din 16 august 2002, publicată în '
                        'MONITORUL OFICIAL nr. 642 din 30 august 2002'},
            'legea-153-2010': {
                'label': 'Legea nr. 153/2010', 'page': '120675', 'capture': '20240422123828',
                'cc': {'crawl': 'CC-MAIN-2024-18', 'timestamp': '20240422123828',
                       'filename': 'crawl-data/CC-MAIN-2024-18/segments/1712296818293.64/warc/'
                                   'CC-MAIN-20240422113340-20240422143340-00847.warc.gz',
                       'offset': '313855364', 'length': '11715',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/120675'},
                'in_force': '2010-07-22',
                'why': 'it sets no in-force day of its own: 3 days after publication in Monitorul Oficial nr. 496 of '
                       '19 July 2010 (Constituția art. 78)',
                'read': 'art. I pct. 2: "Articolele 4 și 5 se abrogă."; pct. 4: "Articolul 10 se abrogă."; the form of '
                        '22.07.2010 leaves them out with no note.',
                'repeals': {'120796': ('art-004', 'art-005', 'art-010')},
                'cite': 'Art. 4, 5 și 10 au fost abrogate de art. I pct. 2 și 4 din LEGEA nr. 153 din 12 iulie 2010, '
                        'publicată în MONITORUL OFICIAL nr. 496 din 19 iulie 2010'},
        },
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    # the laws that ordered the republications and the acts that repealed articles, from the notes of the forms
    # (republication notes) and from the acts read as published
    P.BASE_LAWS.setdefault('legea-132-1996', {
        'label': 'Legea nr. 132/1996', 'kind': 'law',
        'title': 'Legea nr. 132/1996, publicată în Monitorul Oficial al României, Partea I, nr. 271 din 31 octombrie '
                 '1996',
        'enacted': '1996-10-28', 'published': '1996-10-31', 'url': None,
    })
    P.BASE_LAWS.setdefault('legea-2-2000', {
        'label': 'Legea nr. 2/2000', 'kind': 'law',
        'title': 'Legea nr. 2/2000, publicată în Monitorul Oficial al României, Partea I, nr. 16 din 18 ianuarie 2000',
        'enacted': '2000-01-17', 'published': '2000-01-18', 'url': None,
    })
    P.BASE_LAWS.setdefault('legea-153-2010', {  # read as published (DetaliiDocumentAfis/120675)
        'label': 'Legea nr. 153/2010', 'kind': 'law',
        'title': 'Legea nr. 153/2010 privind modificarea Legii nr. 61/1991 pentru sancționarea faptelor de încălcare '
                 'a unor norme de conviețuire socială, a ordinii și liniștii publice, publicată în Monitorul Oficial '
                 'al României, Partea I, nr. 496 din 19 iulie 2010',
        'enacted': '2010-07-12', 'published': '2010-07-19', 'url': P.PORTAL + 'DetaliiDocumentAfis/120675',
    })
    P.BASE_LAWS.setdefault('legea-192-2019', {
        'label': 'Legea nr. 192/2019', 'kind': 'law',
        'title': 'Legea nr. 192/2019 pentru modificarea și completarea unor acte normative din domeniul ordinii și '
                 'siguranței publice, publicată în Monitorul Oficial al României, Partea I, nr. 868 din 28 octombrie '
                 '2019',
        'enacted': None, 'published': '2019-10-28', 'url': None,  # the cached pages give no date of adoption
    })
    P.BASE_LAWS.setdefault('og-55-2002', {  # read as published (DetaliiDocumentAfis/38212)
        'label': 'OG nr. 55/2002', 'kind': 'decree',
        'title': 'Ordonanța Guvernului nr. 55/2002 privind regimul juridic al sancțiunilor prestării unei activități '
                 'în folosul comunității și închisorii contravenționale, publicată în Monitorul Oficial al României, '
                 'Partea I, nr. 642 din 30 august 2002',
        'enacted': '2002-08-16', 'published': '2002-08-30', 'url': P.PORTAL + 'DetaliiDocumentAfis/38212',
    })
    P.BASE_LAWS.setdefault(SLUG, {  # from the text as published (DetaliiDocumentAfis/1534)
        'label': 'Legea nr. 61/1991', 'kind': 'law',
        'title': 'Legea nr. 61/1991, publicată în Monitorul Oficial al României, Partea I, nr. 196 din 27 septembrie '
                 '1991',
        'enacted': '1991-09-27', 'published': '1991-09-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/1534',
    })
