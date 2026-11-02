"""Ordonanța Guvernului nr. 26/2000 cu privire la asociații și fundații (Lexifina, 2026-11-02).

Act page 20740, also its base text (DetaliiDocumentAfis/20740); 17 consolidated forms 03.03.2003 .. 24.07.2025, all
held from Common Crawl (forms.d/og-26-2000.json, listed from the page of the newest form), each from its own page.
Parsed as the Phase 6 acts.
"""
SLUG = 'og-26-2000'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-og-26-2000', 'short': 'OG nr. 26/2000', 'pad': 3, 'cc_forms': True,
        'title': 'Ordonanța Guvernului nr. 26/2000 cu privire la asociații și fundații',
        'url': P.PORTAL + 'DetaliiDocument/20740',
        'in_force': '2000-04-30', 'first_law': SLUG,
        'base_note': 'The ordinance as published in Monitorul Oficial nr. 39 of 31 January 2000, in force 3 months '
                     'after publication (its art. 78): 30 April 2000.',
        'form_note': {},
        'republished': {},
        'repeal_acts': {
            'legea-213-2005': {
                'label': 'Legea nr. 213/2005', 'page': '63026', 'capture': '20251216045517',
                'cc': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/63026',
                       'timestamp': '20251216045517', 'crawl': 'CC-MAIN-2025-51',
                       'filename': 'crawl-data/CC-MAIN-2025-51/segments/1764871656414.82/warc/'
                                   'CC-MAIN-20251216043909-20251216073909-00501.warc.gz',
                       'offset': '275974091', 'length': '11231', 'digest': 'S77UYV3ZBUWKKSYK65B4UUNFGYSCHHKP'},
                'in_force': '2005-07-14',
                'why': 'a law with no in-force clause of its own: 3 days after publication in Monitorul Oficial nr. '
                       '597 of 11 July 2005 (Constituția art. 78)',
                'read': 'its single article: "Se respinge Ordonanța Guvernului nr. 37 din 30 ianuarie 2003 pentru '
                        'modificarea și completarea Ordonanței Guvernului nr. 26/2000"; the articles that ordinance '
                        'inserted (1^1, 38^1, 40^1, 41^1, 41^2) go with it.',
                'repeals': {'63605': ('art-001-1', 'art-038-1', 'art-040-1', 'art-041-1', 'art-041-2')},
                'cite': 'Articolul eliminat prin respingerea ORDONANȚEI nr. 37 din 30 ianuarie 2003, publicate în '
                        'MONITORUL OFICIAL nr. 62 din 1 februarie 2003 de către LEGEA nr. 213 din 5 iulie 2005, '
                        'publicată în MONITORUL OFICIAL nr. 597 din 11 iulie 2005'},
        },
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/20740, Common Crawl 20250916100015)
        'label': 'OG nr. 26/2000', 'kind': 'decree',
        'title': 'Ordonanța Guvernului nr. 26/2000 cu privire la asociații și fundații, publicată în Monitorul '
                 'Oficial al României, Partea I, nr. 39 din 31 ianuarie 2000',
        'enacted': '2000-01-30', 'published': '2000-01-31', 'url': P.PORTAL + 'DetaliiDocumentAfis/20740',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
