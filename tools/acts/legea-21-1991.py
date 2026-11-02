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
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-21-1991', 'short': 'Legea nr. 21/1991', 'pad': 3, 'cc_forms': True,
        'root_word': 'act page',
        'title': 'Legea cetățeniei române nr. 21/1991',
        'url': P.PORTAL + 'DetaliiDocument/1464',
        'in_force': '1991-04-05', 'first_law': SLUG,
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
