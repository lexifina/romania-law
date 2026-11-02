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
        # forms 01.01.2007 .. 15.02.2010 print "*) NOTA C.T.C.E. SA Piatra Neamt: Potrivit art. II din LEGEA nr. 522
        # ..." inside arts. 19^1 and 19^2: the consolidator's note, not text
        'cte_notes': True,
        # the form of 15.02.2010 reprints older undated notes in new wording ("Lit. h) a art. 1 ...")
        'reprint_law': True,
        # Legea nr. 522/2004 art. II: arts. 19^1 and 19^2 take effect with the new Penal Code (1 February 2014); the
        # portal prints them from its form of 07.03.2005
        'later_provisions': (
            {'day': '2014-02-01', 'law': 'legea-522-2004', 'lines': (), 'units': ('art-019-1', 'art-019-2'),
             'note': 'Arts. 19^1 and 19^2, inserted by Legea nr. 522/2004 (art. I pct. 12), take effect on the day the '
                     'new Penal Code takes effect (its art. II): 1 February 2014; the portal prints them from its form '
                     'of 07.03.2005.'},
        ),
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
            'Legea nr. 143/2000: arts. 19^1 and 19^2 were inserted by Legea nr. 522/2004 (art. I pct. 12), whose art. II '
            '(read as published: DetaliiDocumentAfis/57376, Common Crawl 20260212031050) puts the law in force 3 months '
            'after publication "cu excepția art. 19^1 și 19^2 din Legea nr. 143/2000, care intră în vigoare la data '
            'intrării în vigoare a noului Cod penal". The Penal Code of 2004 (Legea nr. 301/2004) never took effect '
            '(repealed by art. 446 alin. (2) of Legea nr. 286/2009); the Penal Code of 2009 took effect on 1 February '
            '2014, the day Legea nr. 187/2012 (art. 81 pct. 11 and 12) reworded both articles. The portal prints them '
            'from its form of 7 March 2005. Under the rule for text printed before its law, both are absent until 1 '
            'February 2014, when they appear in Legea nr. 522/2004\'s wording, credited to it, and the same day in '
            'Legea nr. 187/2012\'s. (Art. 19^2 on 15 February 2010 in the list of uncredited changes below is a '
            'spelling change in the text as printed then, not shown.)',
            'Legea nr. 143/2000: the text republished on 6 March 2014 and the form of 8 May 2014 print the annex\'s '
            'tables of substances (from "TABELUL Nr. I") at the end of art. 27, with no annex markup; every other form '
            'prints them as the annex. Those lines are the annex, not art. 27\'s text, and are left out.',
            'Legea nr. 143/2000: the form of 15 February 2010 reprints older undated notes in new wording; a reworded '
            'note naming a law already noted on that article is the same note, so a typesetting change that day is not '
            'credited to it.',
            'Legea nr. 143/2000: the changes of 1 February 2014, the day the 2009 Penal Code and Code of Criminal '
            'Procedure took effect, are credited as the portal\'s notes name them: Legea nr. 187/2012 (art. 81) and '
            'Legea nr. 255/2013 (art. 43). The other changes no note explains (15 February 2010, 1 February 2014) are '
            'diacritics and spelling only, the publisher\'s.',
            'Legea nr. 143/2000: art. 12 was amended by art. 28 of Legea nr. 39/2003, in force 28 February 2003 (its '
            'art. 33); the change arrives with the portal\'s first form, of 1 March 2003, credited to that law.',
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
    # the republished text (06.03.2014) and the form of 08.05.2014 print the annex's tables of substances at the end of
    # art. 27, with no annex markup; the other forms print them as the annex
    P.EDITORIAL_TAILS[SLUG] = {'art-027': 'TABELUL Nr. I'}
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
