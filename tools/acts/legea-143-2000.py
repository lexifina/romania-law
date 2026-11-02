"""Legea nr. 143/2000 privind prevenirea și combaterea traficului și consumului ilicit de droguri (Lexifina, 2026-11-02).

Act page 23629, also its base text (DetaliiDocumentAfis/23629); 21 consolidated forms 01.03.2003 .. 29.03.2025, all
held (forms.d/legea-143-2000.json); the republication of 06.03.2014 (156116) read from its text as printed
(DetaliiDocumentAfis/156116). Parsed as the Phase 6 acts. Legea nr. 187/2012 (the law putting the 2009 Penal Code into
force, 01.02.2014) is credited under its existing law key, legea-187-2012, from the portal's notes.
"""
SLUG = 'legea-143-2000'
TITLE = 'Legea nr. 143/2000 privind prevenirea și combaterea traficului și consumului ilicit de droguri'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'oug-121-2006': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/78033',
                     'timestamp': '20260122140106', 'crawl': 'CC-MAIN-2026-04',
                     'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220470194.15/warc/'
                                 'CC-MAIN-20260122122206-20260122152206-00005.warc.gz',
                     'offset': '284991316', 'length': '24077', 'digest': '6G4WUYYHDJ7KDZUGBN2JD2RPUQY7V2ZH'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-143-2000', 'short': 'Legea nr. 143/2000', 'pad': 3,
        'cc_forms': True, 'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/23629',
        'in_force': '2000-08-03', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 362 of 3 August 2000; it sets no day of its own, '
                     'so in force on publication (Constituția of 1991, art. 78): 3 August 2000.',
        'form_note': {'156116': 'The law as republished in Monitorul Oficial nr. 163 of 6 March 2014 under art. 107 '
                                'alin. (3) of Legea nr. 255/2013, with renumbered articles.'},
        'republished': {'156116': 'legea-255-2013'},
        'decisions': [
            'Legea nr. 143/2000: the first version is the law as published in Monitorul Oficial nr. 362 of 3 August '
            '2000 (DetaliiDocumentAfis/23629), dated 3 August 2000: it sets no in-force day of its own, so it took '
            'effect on publication (Constituția of 1991, art. 78). The portal\'s first form is of 1 March 2003, so the '
            'changes made up to then arrive together that day.',
            'Legea nr. 143/2000: the text republished in Monitorul Oficial nr. 163 of 6 March 2014 under art. 107 '
            'alin. (3) of Legea nr. 255/2013 has no DetaliiDocument capture; it is read from its text as printed '
            '(DetaliiDocumentAfis/156116), credited to Legea nr. 255/2013 as the republication note says. It renumbers '
            'the articles, so numbers it leaves out are not repeals.',
        ],
        'repeal_acts': {
            'oug-121-2006': {
                'label': 'OUG nr. 121/2006', 'page': '78033', 'capture': CC['oug-121-2006']['timestamp'],
                'cc': CC['oug-121-2006'], 'in_force': '2007-01-01',
                'why': 'its art. 31: "Prezenta ordonanță de urgență intră în vigoare la data de 1 ianuarie 2007"',
                'read': 'art. 32 lit. b): on its in-force day "se abrogă ... art. 9 din Legea nr. 143/2000"'},
        },
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/23629, Common Crawl 20260118172107)
        'label': 'Legea nr. 143/2000', 'kind': 'law',
        'title': 'Legea nr. 143/2000 privind combaterea traficului și consumului ilicit de droguri, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 362 din 3 august 2000',
        'enacted': '2000-07-26', 'published': '2000-08-03', 'url': P.PORTAL + 'DetaliiDocumentAfis/23629',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
