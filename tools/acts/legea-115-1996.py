"""Legea nr. 115/1996 privind declararea și controlul averii demnitarilor, magistraților, funcționarilor publici și a
unor persoane cu funcții de conducere (Lexifina, 2026-11-02).

Act page 8602, also its base text (DetaliiDocumentAfis/8602). 8 forms 21.04.2003 .. 05.09.2010, all held
(forms.d/legea-115-1996.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-115-1996'

# acts read as published (their DetaliiDocumentAfis pages)
CC = {
    'legea-161-2003': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/43323',
                       'timestamp': '20251118020051', 'crawl': 'CC-MAIN-2025-47',
                       'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439649042.63/warc/'
                                   'CC-MAIN-20251118000149-20251118030149-00339.warc.gz',
                       'offset': '298059980', 'length': '221320', 'digest': 'HS4TZI7LBHVYDL77EDF3G2TBTT4SP63Y'},
    'legea-144-2007': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/82317',
                       'timestamp': '20260121154619', 'crawl': 'CC-MAIN-2026-04',
                       'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469725.43/warc/'
                                   'CC-MAIN-20260121144900-20260121174900-00605.warc.gz',
                       'offset': '309390040', 'length': '50861', 'digest': 'HKUKXNTWLJFWVBYS5PFQ4RATR3QY6TGR'},
}
TITLE = ('Legea nr. 115/1996 privind declararea și controlul averii demnitarilor, magistraților, funcționarilor '
         'publici și a unor persoane cu funcții de conducere')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-115-1996', 'short': 'Legea nr. 115/1996', 'pad': 3, 'cc_forms': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/8602',
        'in_force': '1996-10-28', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 263 of 28 October 1996; it sets no day of its own, '
                     'so in force on publication (Constituția of 1991, art. 78): 28 October 1996.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 115/1996: the first version is the law as published in Monitorul Oficial nr. 263 of 28 October '
            '1996 (DetaliiDocumentAfis/8602), dated 28 October 1996: it sets no day of its own, and under art. 78 of '
            'the Constitution of 1991, then in force, a law took effect on publication. The portal\'s first form is '
            'of 21 April 2003, so the changes made up to then arrive together that day.',
        ],
        'repeal_acts': {
            'legea-161-2003': {
                'label': 'Legea nr. 161/2003', 'page': '43323', 'capture': CC['legea-161-2003']['timestamp'],
                'cc': CC['legea-161-2003'], 'in_force': '2003-04-21',
                'why': 'its book II, title I has no day of its own and the law was published in Monitorul Oficial nr. '
                       '279 of 21 April 2003, before the revised Constitution took effect: in force on publication '
                       '(Constituția of 1991, art. 78)',
                'read': 'art. III pct. 12: "Articolul 37 se abrogă." (amending Legea nr. 115/1996); the portal\'s first '
                        'form, of 21.04.2003, leaves art. 37 out.'},
            'legea-144-2007': {
                'label': 'Legea nr. 144/2007', 'page': '82317', 'capture': CC['legea-144-2007']['timestamp'],
                'cc': CC['legea-144-2007'], 'in_force': '2007-11-25',
                'why': 'its art. 60 alin. (1) applies "la data intrării în vigoare a prezentei legi, potrivit art. 59 '
                       'alin. (1) lit. b)", that is 6 months after publication in Monitorul Oficial nr. 359 of 25 May '
                       '2007: 25 November 2007',
                'read': 'art. 60 alin. (1) lit. a): "art. 1, 2, art. 3 alin. (2) și (3), art. 4, 5, art. 6 alin. (3) și '
                        '(4), art. 6^1, 8, 9, 11-13, art. 14 alin. (1), art. 16 alin. (2), art. 21, 22, 35 și 36 din '
                        'Legea nr. 115/1996"; the portal\'s form of 25.11.2007 leaves out the whole articles among '
                        'them with a note naming it.'},
        },
        'root_word': 'act page',
    }
    # dates read from the act as published (DetaliiDocumentAfis/8602: "LEGE Nr. 115 din 16 octombrie 1996",
    # Monitorul Oficial nr. 263 din 28 octombrie 1996)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 115/1996', 'kind': 'law',
        'title': 'Legea nr. 115 din 16 octombrie 1996, publicată în Monitorul Oficial al României, Partea I, nr. 263 '
                 'din 28 octombrie 1996',
        'enacted': '1996-10-16', 'published': '1996-10-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/8602',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
