"""Legea nr. 188/2000 privind executorii judecătorești (Lexifina, 2026-11-02).

Act page 24928, also its base text (DetaliiDocumentAfis/24928). 12 forms 25.07.2002 .. 17.07.2022, all held from Common
Crawl (forms.d/legea-188-2000.json): own pages, and the republication of 20.10.2011 from its DetaliiDocumentAfis page.
Parsed as the Phase 6 acts.
"""
SLUG = 'legea-188-2000'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'oug-190-2005': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/67324',
                     'timestamp': '20260121190535', 'crawl': 'CC-MAIN-2026-04',
                     'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469726.25/warc/'
                                 'CC-MAIN-20260121175607-20260121205607-00546.warc.gz',
                     'offset': '308803492', 'length': '18397', 'digest': '4VYSHA2ZSFHVCFDG6WIDXAWNDA5BGGRB'},
    'og-7-2001': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/29951',
                  'timestamp': '20251214100049', 'crawl': 'CC-MAIN-2025-51',
                  'filename': 'crawl-data/CC-MAIN-2025-51/segments/1764871307934.76/warc/'
                              'CC-MAIN-20251214093639-20251214123639-00900.warc.gz',
                  'offset': '281541621', 'length': '59520', 'digest': 'X5QRYZGCBLMHA3ODLZGI6ZTBG7FUFBQU'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-188-2000', 'short': 'Legea nr. 188/2000', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 188/2000 privind executorii judecătorești',
        'url': P.PORTAL + 'DetaliiDocument/24928',
        'in_force': '2000-11-10', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 559 of 10 November 2000, in force on '
                     'publication (its art. 66 alin. (1)): 10 November 2000.',
        'form_note': {'132311': 'The law as republished in Monitorul Oficial nr. 738 of 20 October 2011 under art. II '
                                'of Legea nr. 151/2011, with renumbered articles.'},
        'republished': {'132311': 'legea-151-2011'},
        'repeal_acts': {
            'og-7-2001': {
                'label': 'OG nr. 7/2001', 'page': '29951', 'capture': CC['og-7-2001']['timestamp'],
                'cc': CC['og-7-2001'], 'in_force': '2002-01-01',
                'why': 'its own clause: in force on 1 January 2002 (published in Monitorul Oficial nr. 435 of 3 '
                       'August 2001)',
                'read': 'art. 85: on the day it takes effect "se abrogă ... prevederile art. 64 din Legea privind '
                        'executorii judecătorești nr. 188/2000"; the form of 25.07.2002 leaves art. 64 out with no '
                        'note.',
                'repeals': {'43794': ('art-064',)},
                'cite': 'Art. 64 a fost abrogat de art. 85 din ORDONANȚA nr. 7 din 19 iulie 2001, publicată în '
                        'MONITORUL OFICIAL nr. 435 din 3 august 2001'},
            'oug-190-2005': {
                'label': 'OUG nr. 190/2005', 'page': '67324', 'capture': CC['oug-190-2005']['timestamp'],
                'cc': CC['oug-190-2005'], 'in_force': '2005-12-28',
                'why': 'an emergency ordinance with no day of its own, in force on publication in Monitorul Oficial '
                       'nr. 1.179 of 28 December 2005',
                'read': 'art. II pct. 8: "Articolul 36 se abrogă."; the form of 28.12.2005 leaves art. 36 out with '
                        'no note.',
                'repeals': {'67801': ('art-036',)},
                'cite': 'Art. 36 a fost abrogat de pct. 8 al art. II din ORDONANȚA DE URGENȚĂ nr. 190 din 21 '
                        'noiembrie 2005, publicată în MONITORUL OFICIAL nr. 1179 din 28 decembrie 2005'},
        },
        'decisions': [
            'Legea nr. 188/2000: the first version is the law as published in Monitorul Oficial nr. 559 of 10 '
            'November 2000 (DetaliiDocumentAfis/24928), in force on publication (its art. 66 alin. (1), which puts '
            'it into application 90 days after that day; no article is given a later day). The portal\'s first '
            'form is of 25 July 2002, so the changes made up to then arrive together that day.',
            'Legea nr. 188/2000: the text republished in Monitorul Oficial nr. 738 of 20 October 2011 under art. II '
            'of Legea nr. 151/2011, with renumbered articles, is read from its own page '
            '(DetaliiDocumentAfis/132311); changes on that day that no note explains are credited to Legea nr. '
            '151/2011, as the republication note says; files follow each text\'s own numbering.',
        ],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/24928)
        'label': 'Legea nr. 188/2000', 'kind': 'law',
        'title': 'Legea nr. 188 din 1 octombrie 2000 privind executorii judecătorești, publicată în Monitorul Oficial '
                 'al României, Partea I, nr. 559 din 10 noiembrie 2000',
        'enacted': '2000-10-01', 'published': '2000-11-10', 'url': P.PORTAL + 'DetaliiDocumentAfis/24928',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
