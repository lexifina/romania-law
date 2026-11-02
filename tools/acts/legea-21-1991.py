"""Legea cetățeniei române nr. 21/1991 (Lexifina, 2026-11-02).

Act page 1464, also its base text (DetaliiDocumentAfis/1464); 22 forms 06.03.2000 .. 15.03.2025
(forms.d/legea-21-1991.json): the republications of 2000 and 2010 are read from their DetaliiDocumentAfis pages, the
other forms from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-21-1991'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'oug-68-2002': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/36706',
                    'timestamp': '20260117163617', 'crawl': 'CC-MAIN-2026-04',
                    'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469354.41/warc/'
                                'CC-MAIN-20260117151209-20260117181209-00976.warc.gz',
                    'offset': '309237875', 'length': '11924', 'digest': 'SMNU7WF44TADLPNVDPH4BKBNI77H4ARQ'},
    'oug-5-2010': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/115987',
                   'timestamp': '20251008110731', 'crawl': 'CC-MAIN-2025-43',
                   'filename': 'crawl-data/CC-MAIN-2025-43/segments/1759648358322.61/warc/'
                               'CC-MAIN-20251008085453-20251008115453-00997.warc.gz',
                   'offset': '359743880', 'length': '23489', 'digest': 'WAV4XQ77SNOAP54NFJHIKO6X5LT2ZY2I'},
    'oug-87-2007': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/85351',
                    'timestamp': '20260118101022', 'crawl': 'CC-MAIN-2026-04',
                    'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469408.36/warc/'
                                'CC-MAIN-20260118094130-20260118124130-00096.warc.gz',
                    'offset': '289463896', 'length': '17581', 'digest': '5CE6INDPTH7PJ764CAH4GJ365EWPMY6I'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-21-1991', 'short': 'Legea nr. 21/1991', 'pad': 3, 'cc_forms': True,
        'root_word': 'act page',
        'title': 'Legea cetățeniei române nr. 21/1991',
        'url': P.PORTAL + 'DetaliiDocument/1464',
        'in_force': '1991-04-05', 'first_law': SLUG, 'hold': True,
        'base_note': 'The law as published in Monitorul Oficial nr. 44 of 6 March 1991, in force 30 days after '
                     'publication (its art. 42): 5 April 1991.',
        'form_note': {
            '21269': 'The law as republished in Monitorul Oficial nr. 98 of 6 March 2000 under art. III of Legea nr. '
                     '192/1999, with renumbered articles.',
            '121439': 'The law as republished in Monitorul Oficial nr. 576 of 13 August 2010 under art. 21 of OUG nr. '
                      '5/2010, with renumbered articles.',
        },
        'republished': {'21269': 'legea-192-1999', '121439': 'oug-5-2010'},
        'repeal_acts': {
            'oug-68-2002': {
                'label': 'OUG nr. 68/2002', 'page': '36706', 'capture': CC['oug-68-2002']['timestamp'],
                'cc': CC['oug-68-2002'], 'in_force': '2002-06-18',
                'why': 'an emergency ordinance with no day of its own, in force on publication in Monitorul Oficial '
                       'nr. 424 of 18 June 2002',
                'read': 'art. I pct. 4: "Articolul 35 se abrogă."; the form of 04.10.2002 leaves art. 35 out with no '
                        'note.',
                'repeals': {'41161': ('art-035',)},
                'cite': 'Art. 35 a fost abrogat de pct. 4 al art. I din ORDONANȚA DE URGENȚĂ nr. 68 din 13 iunie '
                        '2002, publicată în MONITORUL OFICIAL nr. 424 din 18 iunie 2002'},
            'oug-5-2010': {
                'label': 'OUG nr. 5/2010', 'page': '115987', 'capture': CC['oug-5-2010']['timestamp'],
                'cc': CC['oug-5-2010'], 'in_force': '2010-02-10',
                'why': 'an emergency ordinance with no day of its own, in force on publication in Monitorul Oficial '
                       'nr. 93 of 10 February 2010',
                'read': 'art. 14 pct. 1: "Articolul 10^2 se abrogă."; the form of 10.02.2010 leaves art. 10^2 out '
                        'with no note.',
                'repeals': {'119695': ('art-010-2',)},
                'cite': 'Art. 10^2 a fost abrogat de pct. 1 al art. 14 din ORDONANȚA DE URGENȚĂ nr. 5 din 5 februarie '
                        '2010, publicată în MONITORUL OFICIAL nr. 93 din 10 februarie 2010'},
            'oug-87-2007': {
                'label': 'OUG nr. 87/2007', 'page': '85351', 'capture': CC['oug-87-2007']['timestamp'],
                'cc': CC['oug-87-2007'], 'in_force': '2007-09-14',
                'why': 'an emergency ordinance with no day of its own, in force on publication in Monitorul Oficial '
                       'nr. 634 of 14 September 2007',
                'read': 'art. I pct. 5 and 14: "Articolul 15 se abrogă." and "Articolele 32, 33 şi 37^1 se abrogă."; '
                        'the form of 14.09.2007 prints notes for them.',
                'repeals': {'85458': ('art-015', 'art-032', 'art-033', 'art-037-1')},
                'cite': 'Art. 15 a fost abrogat de pct. 5 al art. I din ORDONANŢA DE URGENŢĂ nr. 87 din 5 septembrie '
                        '2007, publicată în MONITORUL OFICIAL nr. 634 din 14 septembrie 2007'},
        },
        'decisions': [
            'Legea nr. 21/1991: the first version is the law as published in Monitorul Oficial nr. 44 of 6 March '
            '1991 (DetaliiDocumentAfis/1464), in force 30 days after publication (its art. 42): 5 April 1991. The '
            'portal\'s first form is the republication of 6 March 2000, so the changes made up to then arrive '
            'together that day.',
            'Legea nr. 21/1991: the texts republished in Monitorul Oficial nr. 98 of 6 March 2000 (under art. III of '
            'Legea nr. 192/1999) and nr. 576 of 13 August 2010 (under art. 21 of OUG nr. 5/2010) renumber the '
            'articles; each is read from its own DetaliiDocumentAfis page (21269, 121439), changes on those days that '
            'no note explains are credited to the republishing act, as each republication note says, and files '
            'follow each text\'s own numbering.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/1464)
        'label': 'Legea nr. 21/1991', 'kind': 'law',
        'title': 'Legea nr. 21 din 1 martie 1991 a cetățeniei române, publicată în Monitorul Oficial al României, '
                 'Partea I, nr. 44 din 6 martie 1991',
        'enacted': '1991-03-01', 'published': '1991-03-06', 'url': P.PORTAL + 'DetaliiDocumentAfis/1464',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
