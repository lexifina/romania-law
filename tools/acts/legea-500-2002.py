"""Legea nr. 500/2002 privind finanțele publice (Lexifina, 2026-11-02).

Act page 37954, also its base text (DetaliiDocumentAfis/37954); 32 consolidated forms 14.07.2003 .. 05.10.2023, all
held from Common Crawl (forms.d/legea-500-2002.json, listed from the act page). Never republished. Parsed as the Phase
6 acts.
"""
SLUG = 'legea-500-2002'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-500-2002', 'short': 'Legea nr. 500/2002', 'pad': 3, 'cc_forms': True,
        'titles': True, 'hg_notes': True, 'reprint_law': True,
        'title': 'Legea nr. 500/2002 privind finanțele publice',
        'url': P.PORTAL + 'DetaliiDocument/37954',
        'in_force': '2003-01-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 597 of 13 August 2002, in force on 1 January 2003 '
                     '(its art. 80 alin. (1)).',
        'form_note': {}, 'republished': {},
        'decisions': DECISIONS,
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/37954, Common Crawl 20260115205737)
        'label': 'Legea nr. 500/2002', 'kind': 'law',
        'title': 'Legea nr. 500/2002 privind finanțele publice, publicată în Monitorul Oficial al României, Partea I, '
                 'nr. 597 din 13 august 2002',
        'enacted': '2002-07-11', 'published': '2002-08-13', 'url': P.PORTAL + 'DetaliiDocumentAfis/37954',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)


DECISIONS = [
    'Legea nr. 500/2002: the first version is the law as published in Monitorul Oficial nr. 597 of 13 August 2002 '
    '(DetaliiDocumentAfis/37954), in force on 1 January 2003 (its art. 80 alin. (1)). The portal\'s first form is of '
    '14 July 2003, so the changes made up to then arrive together that day. The law has not been republished.',
    'Legea nr. 500/2002: the amounts in art. 42 (which body approves an investment project, by value) are updated by '
    'Government decisions (HG nr. 1.865/2006, 406/2009, 335/2011, 207/2020), each named by the portal\'s note on the '
    'article; the changes are credited to them.',
    'Legea nr. 500/2002: the forms print the articles\' marginal titles unevenly: before the article, as the last '
    'paragraph of the article before it, or not at all (for example art. 15 in 2009-2011, arts. 10, 24, 31-33 and 38 '
    'in 2014-2015, art. 46 in 2015-2016), and some forms break a provision\'s line after a linked act\'s name (2016). '
    'A marginal title that appears, moves or disappears with no note, and such line breaks, are the publisher\'s '
    'typesetting, committed as found; so are the diacritic corrections of 14 July 2003, 4 April 2014 and 1 January '
    '2015 and the stub "d) abrogată;" printed in art. 74 from 30 September 2015.',
    'Legea nr. 500/2002: a note the portal prints again in a later form, unchanged but for a rule line or its opening '
    'words, is not read as a new amendment (Legea nr. 314/2003 on art. 15 in the form of 1 February 2014; OUG nr. '
    '47/2012 on art. 2 in the form of 21 October 2013).',
    'Legea nr. 500/2002: the act page as captured on 2 February 2026 (Internet Archive 20260202190648) still shows the '
    'form of 5 October 2023 as the newest.',
]
