"""OUG nr. 99/2006 privind instituțiile de credit și adecvarea capitalului (credit institutions and capital adequacy):
Lexifina, 2026-11-02.

Act page 78313, also its base text (DetaliiDocumentAfis/78313); no republication; 26 consolidated forms 21.07.2007 ..
05.03.2026 (forms.d/oug-99-2006.json): 25 from Common Crawl, the newest from the act page's archive.org capture made
while it was the newest form. Parsed as the Phase 6 acts.
"""
SLUG = 'oug-99-2006'
TITLE = 'Ordonanța de urgență a Guvernului nr. 99/2006 privind instituțiile de credit și adecvarea capitalului'

# acts read as published (their DetaliiDocumentAfis pages, Common Crawl)
CC = {
    'oug-25-2009': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/103693', 'timestamp': '20251017150600',
                    'crawl': 'CC-MAIN-2025-43',
                    'filename': 'crawl-data/CC-MAIN-2025-43/segments/1759648665304.94/warc/'
                                'CC-MAIN-20251017125300-20251017155300-00038.warc.gz',
                    'offset': '323489246', 'length': '24291', 'digest': '6BV7P7WF6S7EWECC6EIMXMMYZ5XNHH3K'},
    'oug-26-2010': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/117587', 'timestamp': '20260114000213',
                    'crawl': 'CC-MAIN-2026-04',
                    'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469026.40/warc/'
                                'CC-MAIN-20260113234451-20260114024451-00735.warc.gz',
                    'offset': '283340944', 'length': '47238', 'digest': 'NQSZN5G2CHKB37N5VSK5I7QTXUGFGFJY'},
    'oug-113-2013': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/154066',
                     'timestamp': '20251010063555', 'crawl': 'CC-MAIN-2025-43',
                     'filename': 'crawl-data/CC-MAIN-2025-43/segments/1759648358512.22/warc/'
                                 'CC-MAIN-20251010045559-20251010075559-00578.warc.gz',
                     'offset': '336603226', 'length': '98145', 'digest': 'NJO6TVIEVHJLUYMAJEJ7LTJU5Z6U4YEP'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-99-2006', 'short': 'OUG nr. 99/2006', 'pad': 3, 'cc_forms': True, 'sign_tail': True,
        'ell_digit': True,  # "Articolul l58" (lowercase l for 1) in the forms of 2007-2022
        # the form of 01.02.2014 prints arts. 240^33-240^37 inside art. 240^32
        'nested_own': True, 'return_rule': True, 'staged_dating': True, 'reprint_notes': True,
        'root_word': 'act page',
        # the forms of 01.04.2010 and 13.12.2010 quote, after a C.T.C.E. note "... urmează să fie modificat ...
        # începând cu data de 30 aprilie 2011 (31 octombrie 2010) ... având următorul conținut:", the wording OUG nr.
        # 26/2010 gives from that day: not the text in force on the form's day
        'future_text': {'117642': {'arts': ('Articolul 36', 'Articolul 181')}, '125394': {'arts': ('Articolul 36',)}},
        # Legea nr. 319/2021 (MO nr. 1247 of 30.12.2021): its art. II puts art. 126^3, 126^4 alin. (2), 126^6 and
        # 126^8 alin. (2) in force on 01.01.2022; the rest 3 days after publication, 02.01.2022. The portal's form of
        # 01.01.2022 prints all of it: arts. 126^5 and 126^7 (its notes date them 02.01.2022) are left out of that form,
        # and alin. (1) of arts. 126^4 and 126^8 takes effect on 02.01.2022
        'early_text': {'249521': {'absent': ('art-126-5', 'art-126-7'), 'placeholder': ()}},
        'later_provisions': (
            {'day': '2022-01-02', 'law': 'legea-319-2021',
             'lines': ('(1) Instituțiile de credit care îndeplinesc cerința amortizorului combinat',
                       '(1) Fac obiectul restricțiilor prevăzute de'),
             'note': 'Art. 126^4 alin. (1) and art. 126^8 alin. (1), inserted by Legea nr. 319/2021, take effect on this '
                     'day, 3 days after its publication (its art. II gives 1 January 2022 only for alin. (2) of both); '
                     'the portal prints them from its form of 01.01.2022.'},
        ),
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/78313',
        'in_force': '2007-01-01', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 1.027 of 27 December 2006, in '
                     'force on 1 January 2007 (its art. 419 alin. (1)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 99/2006: the first version is the emergency ordinance as published in Monitorul Oficial nr. 1.027 '
            'of 27 December 2006 (DetaliiDocumentAfis/78313), dated 1 January 2007, when it takes effect (its art. '
            '419 alin. (1)). The signature block printed after the last article ("PRIM-MINISTRU ...") is not part of '
            'the article.',
            'OUG nr. 99/2006: approved with amendments by Legea nr. 227/2007 (Monitorul Oficial nr. 480 of 18 July '
            '2007); the portal\'s first consolidated form (21 July 2007) carries its changes, each credited to it from '
            'the portal\'s notes.',
        ],
        'repeal_acts': {
            'oug-25-2009': {
                'label': 'OUG nr. 25/2009', 'page': '103693', 'capture': CC['oug-25-2009']['timestamp'],
                'cc': CC['oug-25-2009'], 'in_force': '2009-03-23',
                'why': 'an emergency ordinance with no in-force clause of its own: in force on publication in '
                       'Monitorul Oficial nr. 179 of 23 March 2009',
                'read': 'art. I pct. 5: "Articolul 9 se abrogă."; pct. 15: "Articolul 30 se abrogă."; pct. 23: '
                        '"Articolul 118 se abrogă."; pct. 38: "Articolul 413 se abrogă."'},
            'oug-26-2010': {
                'label': 'OUG nr. 26/2010', 'page': '117587', 'capture': CC['oug-26-2010']['timestamp'],
                'cc': CC['oug-26-2010'], 'in_force': '2010-04-01',
                'in_force_keys': {'art-047': '2011-04-30', 'art-058': '2011-04-30'},
                'why': 'its art. VII: in force on publication in Monitorul Oficial nr. 208 of 1 April 2010, except art. '
                       'I pct. 4, 16-18, 20-23 and 25-28 (31 October 2010) and pct. 1-3, 5, 6, 10, 12, 15 and 38 (30 '
                       'April 2011)',
                'read': 'art. I pct. 37 repeals arts. 241-254 (in force on publication); pct. 12 repeals arts. 47 and '
                        '58 (art. VII lit. b): 30 April 2011).'},
            # art. 383: left out by the forms of 01.01.2014 and 01.02.2014, printed again on 15.03.2015 in the
            # wording of OUG nr. 113/2013 art. VIII pct. 190
            'oug-113-2013': {
                'label': 'OUG nr. 113/2013', 'page': '154066', 'capture': CC['oug-113-2013']['timestamp'],
                'cc': CC['oug-113-2013'], 'in_force': '2014-01-01', 'returns': {'152137': ('art-383',)},
                'why': 'its art. XI: arts. VIII-X in force on 1 January 2014 (pct. 190 is not among the exceptions)',
                'read': 'art. VIII pct. 190: "Articolul 383 se modifică și va avea următorul cuprins: Art. 383. - Prin '
                        'excepție de la dispozițiile Legii societăților nr. 31/1990 ..."; its art. XI puts arts. '
                        'VIII-X in force on 1 January 2014, save points it lists (190 not among them).'},
        },
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/78313, Common Crawl 20260124123228)
        'label': 'OUG nr. 99/2006', 'kind': 'decree',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 1.027 din 27 decembrie 2006',
        'enacted': '2006-12-06', 'published': '2006-12-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/78313',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
