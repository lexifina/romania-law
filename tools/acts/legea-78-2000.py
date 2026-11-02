"""Legea nr. 78/2000 pentru prevenirea, descoperirea și sancționarea faptelor de corupție (Lexifina, 2026-11-02).

Act page 22361, also its base text (DetaliiDocumentAfis/22361); 11 consolidated forms 21.04.2003 .. 23.07.2022, all
held (forms.d/legea-78-2000.json). Parsed as the Phase 6 acts. Legea nr. 187/2012 (the law putting the 2009 Penal
Code into force, 01.02.2014) is credited under its existing law key, legea-187-2012, from the portal's notes.
"""
SLUG = 'legea-78-2000'
TITLE = 'Legea nr. 78/2000 pentru prevenirea, descoperirea și sancționarea faptelor de corupție'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'oug-43-2002': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/35165',
                    'timestamp': '20251114124449', 'crawl': 'CC-MAIN-2025-47',
                    'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439343932.66/warc/'
                                'CC-MAIN-20251114104301-20251114134301-00604.warc.gz',
                    'offset': '301563165', 'length': '24898', 'digest': 'MXKTVR5APU5GKSVZSC4RMDC5DBYXL2VX'},
    'legea-161-2003': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/43323',
                       'timestamp': '20251118020051', 'crawl': 'CC-MAIN-2025-47',
                       'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439649042.63/warc/'
                                   'CC-MAIN-20251118000149-20251118030149-00339.warc.gz',
                       'offset': '298059980', 'length': '221320', 'digest': 'HS4TZI7LBHVYDL77EDF3G2TBTT4SP63Y'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-78-2000', 'short': 'Legea nr. 78/2000', 'pad': 3,
        'cc_forms': True, 'root_word': 'act page',
        # the form of 01.04.2007 reprints the older undated notes without diacritics ("a fost modificata de ...")
        'reprint_law': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/22361',
        'in_force': '2000-05-18', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 219 of 18 May 2000; it sets no day of its own, so '
                     'in force on publication (Constituția of 1991, art. 78): 18 May 2000.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 78/2000: the first version is the law as published in Monitorul Oficial nr. 219 of 18 May 2000 '
            '(DetaliiDocumentAfis/22361), dated 18 May 2000: it sets no in-force day of its own, so it took effect on '
            'publication (Constituția of 1991, art. 78). The portal\'s first form is of 21 April 2003, so the changes '
            'made up to then arrive together that day.',
        ],
        'repeal_acts': {
            'oug-43-2002': {
                'label': 'OUG nr. 43/2002', 'page': '35165', 'capture': CC['oug-43-2002']['timestamp'],
                'cc': CC['oug-43-2002'], 'in_force': '2002-09-01',
                'why': 'its art. 34: "Pe data de 1 septembrie 2002 dispozițiile art. 28 și ale art. 29 alin. (2) din '
                       'Legea nr. 78/2000 ... se abrogă"',
                'read': 'art. 34 (published in Monitorul Oficial nr. 244 of 11 April 2002)'},
            'legea-161-2003': {
                'label': 'Legea nr. 161/2003', 'page': '43323', 'capture': CC['legea-161-2003']['timestamp'],
                'cc': CC['legea-161-2003'], 'in_force': '2003-04-21',
                'why': 'book II, title I has no in-force clause of its own (only book I titles II and V do, arts. 33 '
                       'and 238): in force on publication in Monitorul Oficial nr. 279 of 21 April 2003 (Constituția '
                       'of 1991, art. 78)',
                'read': 'book II, title I, art. I pct. 25: "Articolul 32 se abrogă."'},
        },
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/22361, Common Crawl 20251217035058)
        'label': 'Legea nr. 78/2000', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 219 din 18 mai 2000',
        'enacted': '2000-05-08', 'published': '2000-05-18', 'url': P.PORTAL + 'DetaliiDocumentAfis/22361',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
