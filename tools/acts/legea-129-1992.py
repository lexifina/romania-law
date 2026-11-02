"""Legea nr. 129/1992 privind protecția desenelor și modelelor industriale (Lexifina, 2026-11-02).

Act page 279214. 10 forms 06.01.2003 .. 09.05.2024 listed by DetaliiDocumentAfis/279214 as captured on 2025-08-12, all
held (forms.d/legea-129-1992.json). The portal holds no text as first published, so the record starts at its oldest
form (no_base).
"""
SLUG = 'legea-129-1992'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'legea-280-2007': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/86411',
                       'timestamp': '20230202135318', 'crawl': 'CC-MAIN-2023-06',
                       'filename': 'crawl-data/CC-MAIN-2023-06/segments/1674764500028.12/warc/'
                                   'CC-MAIN-20230202133541-20230202163541-00564.warc.gz',
                       'offset': '374156496', 'length': '25675', 'digest': 'UVMBEDLH3NBDF6WLLSFE6MQBLD64DZ2R'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-129-1992', 'short': 'Legea nr. 129/1992', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 129/1992 privind protecția desenelor și modelelor industriale',
        'url': P.PORTAL + 'DetaliiDocument/282567',
        'no_base': True, 'in_force': '2003-01-06', 'first_law': None, 'revert_credit': True,
        'earlier_laws': [SLUG],
        'base_note': 'Oldest version available: the portal\'s consolidated form of 6 January 2003. The law was enacted '
                     'on 29 December 1992 and first published in Monitorul Oficial nr. 1 of 8 January 1993; that text '
                     'is not held.',
        'form_note': {'42608': 'The law as republished in Monitorul Oficial nr. 193 of 26 March 2003 under art. III of '
                               'Legea nr. 585/2002, with renumbered articles.',
                      '88088': 'The law as republished in Monitorul Oficial nr. 876 of 20 December 2007 under art. IV of '
                               'Legea nr. 280/2007, with renumbered articles.',
                      '157069': 'The law as republished in Monitorul Oficial nr. 242 of 4 April 2014 under art. 248 of '
                                'Legea nr. 187/2012.',
                      '282567': 'The law as republished in Monitorul Oficial nr. 428 of 9 May 2024 under art. VI '
                                'alin. (2) of Legea nr. 30/2024, with renumbered articles.'},
        'republished': {'42608': 'legea-585-2002', '88088': 'legea-280-2007', '157069': 'legea-187-2012',
                        '282567': 'legea-30-2024'},
        'repeal_acts': {
            'legea-280-2007': {
                'label': 'Legea nr. 280/2007', 'page': '86411', 'capture': CC['legea-280-2007']['timestamp'],
                'cc': CC['legea-280-2007'], 'in_force': '2007-11-25',
                'why': 'its art. III alin. (1): in force 30 days after publication in Monitorul Oficial nr. 729 of 26 '
                       'October 2007',
                'read': 'art. I pct. 5: "Articolul 4 se abrogă."; pct. 7: "Articolele 6 și 7 se abrogă."; art. IV '
                        'orders the republication.',
                'repeals': {'86471': ('art-007',)},
                'cite': 'Art. 7 a fost abrogat de pct. 7 al art. I din LEGEA nr. 280 din 17 octombrie 2007, publicată '
                        'în MONITORUL OFICIAL nr. 729 din 26 octombrie 2007'},
        },
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS.setdefault(SLUG, {  # from the heading of the republication of 2003 (DetaliiDocumentAfis/42608)
        'label': 'Legea nr. 129/1992', 'kind': 'law',
        'title': 'Legea nr. 129/1992 privind protecția desenelor și modelelor industriale, publicată în Monitorul '
                 'Oficial al României, Partea I, nr. 1 din 8 ianuarie 1993',
        'enacted': '1992-12-29', 'published': '1993-01-08', 'url': None,
    })
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
