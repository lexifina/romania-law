"""OUG nr. 194/2002 privind regimul străinilor în România (Lexifina, 2026-11-02).

Base text DetaliiDocumentAfis/41005; the portal's act page is 93712 (the republication of 2008). 34 forms listed
27.01.2004 .. 27.04.2026 (forms.d/oug-194-2002.json): the republications of 2004 (50236) and 2008 (93712) are read
from their DetaliiDocumentAfis pages, the other forms from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'oug-194-2002'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'legea-56-2007': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/80555',
                      'timestamp': '20251217004545', 'crawl': 'CC-MAIN-2025-51',
                      'filename': 'crawl-data/CC-MAIN-2025-51/segments/1764871657426.86/warc/'
                                  'CC-MAIN-20251216230723-20251217020723-00067.warc.gz',
                      'offset': '273905048', 'length': '64002', 'digest': 'UIN7BSELXXXRFVG3PJBKCSL5RJNLHX54'},
    'oug-55-2007': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/83150',
                    'timestamp': '20251213104603', 'crawl': 'CC-MAIN-2025-51',
                    'filename': 'crawl-data/CC-MAIN-2025-51/segments/1764871307743.66/warc/'
                                'CC-MAIN-20251213090347-20251213120347-00591.warc.gz',
                    'offset': '270292872', 'length': '28917', 'digest': 'WQQ2LXANMLP7ENZ6APLGWANFKUJXBNOG'},
    'legea-157-2011': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/130383',
                       'timestamp': '20260218220549', 'crawl': 'CC-MAIN-2026-08',
                       'filename': 'crawl-data/CC-MAIN-2026-08/segments/1770395866066.88/warc/'
                                   'CC-MAIN-20260218201643-20260218231643-00314.warc.gz',
                       'offset': '258680016', 'length': '73313', 'digest': 'GJVOU5J2WFK77WFXW2PZJPU6AKEKZLFP'},
    'og-25-2014': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/160962',
                   'timestamp': '20251112000045', 'crawl': 'CC-MAIN-2025-47',
                   'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439343049.28/warc/'
                               'CC-MAIN-20251111215956-20251112005956-00580.warc.gz',
                   'offset': '281328317', 'length': '106889', 'digest': 'BAVSOFPJW5YDYTVXUGS5BQ7EB3YR3JJA'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-194-2002', 'short': 'OUG nr. 194/2002', 'pad': 3, 'cc_forms': True,
        'root_word': 'act page',
        'title': 'Ordonanța de urgență a Guvernului nr. 194/2002 privind regimul străinilor în România',
        'url': P.PORTAL + 'DetaliiDocument/93712',
        'in_force': '2003-01-26', 'first_law': SLUG, 'cte_notes': True,
        # the consolidator's note in art. 31 quotes the wording Legea nr. 157/2011 art. III gives arts. 29-31 and 36
        # from Romania's Schengen accession; the form of 24.12.2015 quotes art. 11's future wording the same way: each
        # quoted article follows the article in force under the same title
        'future_text': {
            '130491': {'arts': ('Articolul 29', 'Articolul 30', 'Articolul 31', 'Articolul 36')},
            '144566': {'arts': ('Articolul 29', 'Articolul 30', 'Articolul 31', 'Articolul 36')},
            '148111': {'arts': ('Articolul 29', 'Articolul 30', 'Articolul 31')},
            '174303': {'arts': ('Articolul 11',)},
        },
        # the same note's quotation of Legea nr. 157/2011 art. III, point by point ("8. Articolul 27 se modifică ...:"
        # and the new wording), is printed inside the articles it amends in the forms of 2011-2016
        'quoted_amendment': {'act': 'legea-157-2011', 'start': 'Articolul III', 'end': 'Articolul IV',
                             'forms': ('130491', '144566', '148111', '154329', '161147', '174303', '181399'),
                             'before': '116732', 'after': '198370'},
        # arts. 28^1 and 33^1 are inserted by Legea nr. 157/2011 art. III pct. 10 and 23 only from Romania's full
        # application of the Schengen acquis (the later forms' notes: 31.03.2024); the forms of 2011-2016 print them
        # before that day
        'early_text': {
            '130491': {'absent': ('art-028-1', 'art-033-1'), 'placeholder': ()},
            '144566': {'absent': ('art-028-1', 'art-033-1'), 'placeholder': ()},
            '148111': {'absent': ('art-028-1', 'art-033-1'), 'placeholder': ()},
            '154329': {'absent': ('art-028-1', 'art-033-1'), 'placeholder': ()},
            '174303': {'absent': ('art-033-1',), 'placeholder': ()},
            '181399': {'absent': ('art-033-1',), 'placeholder': ()},
            # art. 135 lit. a) as reworded by Legea nr. 28/2024 art. I pct. 38, in force 30 days after publication
            # (its art. II: 4.4.2024), after the next form's day too (22.03.2024): the earlier text stands here
            '279226': {'absent': (), 'placeholder': (), 'carry': ('art-135',)},
        },
        # OG nr. 25/2014 art. 41 pct. 71 replaces chapter V (arts. 81-106^6) in full from 28.11.2014 (art. 44 alin.
        # (1)); the form of that day gives the chapter no note of its own
        'form_credits': {'161147': {k: 'og-25-2014' for k in (
            [f'art-{n:03d}' for n in range(81, 107)] + [f'art-106-{s}' for s in range(1, 6)])}},
        'repeal_acts': {
            'legea-56-2007': {
                'label': 'Legea nr. 56/2007', 'page': '80555', 'capture': CC['legea-56-2007']['timestamp'],
                'cc': CC['legea-56-2007'], 'in_force': '2007-03-29',
                'why': 'it sets no day of its own: in force 3 days after publication in Monitorul Oficial nr. 201 of 26 '
                       'March 2007 (Constituția art. 78)',
                'read': 'art. I pct. 29, 38, 47, 70 and 74: "Articolul 39 [49, 63, 84, 86^1] se abrogă."; the form of '
                        '29.03.2007 leaves them out, later forms note the repeals.'},
            'oug-55-2007': {
                'label': 'OUG nr. 55/2007', 'page': '83150', 'capture': CC['oug-55-2007']['timestamp'],
                'cc': CC['oug-55-2007'], 'in_force': '2007-06-26',
                'why': 'an emergency ordinance with no day of its own, in force on publication in Monitorul Oficial '
                       'nr. 424 of 26 June 2007',
                'read': 'art. 6 pct. II subpct. 46: "Articolul 120 se abrogă."'},
            'legea-157-2011': {
                'label': 'Legea nr. 157/2011', 'page': '130383', 'capture': CC['legea-157-2011']['timestamp'],
                'cc': CC['legea-157-2011'], 'in_force': '2011-07-31',
                'why': 'it sets no day of its own for art. I: in force 3 days after publication in Monitorul Oficial '
                       'nr. 533 of 28 July 2011 (Constituția art. 78)',
                'read': 'art. I pct. 34: "Articolul 26 se abrogă."'},
            'og-25-2014': {
                'label': 'OG nr. 25/2014', 'page': '160962', 'capture': CC['og-25-2014']['timestamp'],
                'cc': CC['og-25-2014'], 'in_force': '2014-11-28',
                'why': 'in force 90 days after publication in Monitorul Oficial nr. 640 of 30 August 2014 (its art. '
                       '44 alin. (1))',
                'read': 'art. 41 pct. 71 replaces chapter V ("Regimul îndepărtării străinilor de pe teritoriul '
                        'României") in full; the new chapter has no art. 92^1 or 97^1. The form of 28.11.2014 leaves '
                        'both out with no note.',
                'repeals': {'161147': ('art-092-1', 'art-097-1')},
                'cite': 'Art. 92^1 și art. 97^1 au fost abrogate prin înlocuirea Capitolului V de pct. 71 al art. 41, '
                        'Titlul II din ORDONANȚA nr. 25 din 26 august 2014, publicată în MONITORUL OFICIAL nr. 640 din '
                        '30 august 2014'},
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
            'OUG nr. 194/2002: the act page (93712) is both the republication of 5 June 2008 and the page of the newest '
            'form; the republication is read from its DetaliiDocumentAfis text. The newest form the portal lists, of '
            '27 April 2026 (309238), is held by no archive, so the record ends with the form of 10 July 2025.',
            'OUG nr. 194/2002: Legea nr. 157/2011 (Monitorul Oficial nr. 533 of 28 July 2011, read as published, '
            'DetaliiDocumentAfis/130383) amends the ordinance by its art. I from 31 July 2011 and, by its art. III, '
            'again only "de la data aplicării în totalitate de către România a dispozițiilor acquis-ului Schengen", '
            'which the portal\'s notes date 31 March 2024. The forms of 2011-2016 print the consolidator\'s quotation '
            'of art. III in three ways, none of them text then in force: (1) the new wording of arts. 29, 30, 31 and 36 '
            '(and, in the form of 24 December 2015, of art. 11) as a second article under the same title, which is '
            'left out; (2) arts. 28^1 and 33^1, which art. III pct. 10 and 23 insert, as articles, which are left out of '
            'those forms under the rule for text printed before its law (both arrive with their notes on 31 March '
            '2024); (3) art. III\'s points, line by line, inside the articles they amend ("8. Articolul 27 se modifică '
            'și va avea următorul cuprins:" and the new wording). A line of (3) is left out when it is word for word a '
            'line of art. III as published and is not in the article\'s text in the forms of 1 March 2010 and 12 March '
            '2018, which print no quotation (226 lines in the forms of 31.07.2011-03.09.2016); two quoted lines the '
            'portal reworded (art. 39 alin. (1) in the form of 26 December 2013, art. 33 alin. (4^1) in quotation marks, '
            '2015-2016) are left out by name. The form of 26 June 2007 prints the whole ordinance twice; one copy is '
            'kept.',
            'OUG nr. 194/2002: arts. 92^1 and 97^1 (Legea nr. 157/2011), left out by the form of 28 November 2014 with '
            'no note, are taken as repealed on that day by OG nr. 25/2014 (Monitorul Oficial nr. 640 of 30 August '
            '2014, read as published, DetaliiDocumentAfis/160962), whose art. 41 pct. 71 replaces chapter V in full '
            'with a text that has no such articles, in force 90 days after publication (its art. 44 alin. (1)): 28 '
            'November 2014. The new chapter V (arts. 81-106^6), which the form prints with no note of its own, is '
            'credited to OG nr. 25/2014.',
            'OUG nr. 194/2002: the form of 8 March 2024 already prints art. 135 lit. a) as reworded by Legea nr. '
            '28/2024 art. I pct. 38, which its art. II puts in force 30 days after publication (Monitorul Oficial nr. '
            '176 of 5 March 2024): 4 April 2024, after the next form (22 March 2024) too. In that form the earlier text '
            'stands; the change is dated 4 April 2024 from the next form\'s note (DetaliiDocumentAfis/279587).',
            'OUG nr. 194/2002: the forms of 2011-2016 print the sub-section names of chapter III section 3 ("1. '
            'Prelungirea dreptului de ședere temporară pentru ...") as the last line of the article before, and the '
            'forms of 2014-2015 print the EU-transposition notes after art. 152; neither is an article\'s text and both '
            'are left out.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/41005)
        'label': 'OUG nr. 194/2002', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 194 din 12 decembrie 2002 privind regimul străinilor în '
                 'România, publicată în Monitorul Oficial al României, Partea I, nr. 955 din 27 decembrie 2002',
        'enacted': '2002-12-12', 'published': '2002-12-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/41005',
    }
    # printed as text lines: the sub-section names of chapter III section 3 ("1. Prelungirea dreptului de ședere
    # temporară pentru ..."), at the end of the article before; and two lines
    # of the consolidator's Legea nr. 157/2011 art. III quotation that the portal reworded (ministry name, "ori"), so
    # not word for word in the act (art. 39 alin. (1), form of 26.12.2013; art. 33 alin. (4^1) in quotation marks,
    # 2015-2016)
    P.EDITORIAL_LINES[SLUG] = {
        'art-052': ('1. Prelungirea dreptului de ședere temporară pentru',),
        'art-055': ('2. Prelungirea dreptului de ședere temporară pentru',),
        'art-057': ('3. Prelungirea dreptului de ședere temporară pentru',),
        'art-061': ('4. Prelungirea dreptului de ședere temporară pentru',),
        'art-065': ('5. Prelungirea dreptului de ședere temporară pentru',),
        'art-039': ('(1) Forma, conținutul și elementele de siguranță ale formularului invitației prevăzute de prezenta '
                    'secțiune se stabilesc de către Ministerul Afacerilor Interne, cu avizul',),
        'art-033': ('„(4^1) Decizia de anulare',),
    }
    # the forms of 2014-2015 print, after art. 152, the EU-transposition notes of the ordinance and of acts that
    # amended it ("*" / "Prezenta ordonanță de urgență transpune:" / "1. Directiva ..."): not the article's text
    P.EDITORIAL_TAILS[SLUG] = {'art-152': '*'}
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
