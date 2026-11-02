"""Ordonanța Guvernului nr. 21/1992 privind protecția consumatorilor (Lexifina, 2026-11-02).

Act page 2175, also its base text (DetaliiDocumentAfis/2175). 10 forms 28.03.2007 .. 11.11.2023, all held from Common
Crawl (forms.d/og-21-1992.json, listed from DetaliiDocumentAfis/2175): the 2007 republication from its
DetaliiDocumentAfis page, the rest from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'og-21-1992'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-og-21-1992', 'short': 'OG nr. 21/1992', 'pad': 3, 'cc_forms': True, 'sign_tail': True, 'provision_not_note': True,
        'title': 'Ordonanța Guvernului nr. 21/1992 privind protecția consumatorilor',
        'url': P.PORTAL + 'DetaliiDocument/2175',
        'in_force': '1992-08-28', 'first_law': SLUG,
        'base_note': 'The ordinance as published in Monitorul Oficial nr. 212 of 28 August 1992, in force on '
                     'publication (it sets no day of its own).',
        'form_note': {'80603': 'The ordinance as republished in Monitorul Oficial nr. 208 of 28 March 2007 under art. '
                               'V of Legea nr. 476/2006, with renumbered articles.'},
        'republished': {'80603': 'legea-476-2006'},
        'repeal_acts': {},
        'decisions': [
            'OG nr. 21/1992: the first version is the ordinance as published in Monitorul Oficial nr. 212 of 28 August '
            '1992 (DetaliiDocumentAfis/2175). It sets no in-force day of its own, so it took effect on publication. '
            'The Government\'s signature block printed inside its last article (art. 61) is not text and is left '
            'out.',
            'OG nr. 21/1992: the portal holds no form between the ordinance as published and its republication of 28 '
            'March 2007 (Monitorul Oficial nr. 208, under art. V of Legea nr. 476/2006; read from '
            'DetaliiDocumentAfis/80603). The republication note lists what came between: the republication of 23 '
            'March 1994 (Monitorul Oficial nr. 75), Legea nr. 178/1998, OG nr. 58/2000 (approved by Legea nr. '
            '37/2002), Hotărârea Guvernului nr. 752/2001 (fine amounts), OUG nr. 146/2001 (approved by Legea nr. '
            '322/2002), OUG nr. 84/2002 (approved by Legea nr. 37/2003), Legea nr. 449/2003, Legea nr. 240/2004, '
            'Legea nr. 363/2005 and Legea nr. 476/2006. Their changes arrive together on 28 March 2007, with '
            'renumbered articles, and are credited to Legea nr. 476/2006, which ordered the republication, as the '
            'republication note says; files follow each text\'s own numbering.',
            'OG nr. 21/1992: the older forms print their notes after a rule line, as plain paragraphs; a paragraph '
            'after such a note that opens like a provision ("18^1. data-limită de consum ...", art. 2, forms of 2008 '
            'to 2015) is the ordinance\'s text, even though its wording ("au fost respectate condițiile de ...") '
            'reads like a note.',
            'OG nr. 21/1992: the forms of 13 June 2014 and 7 September 2015 print repealed letters and indents again '
            'as "abrogată" stubs (arts. 7, 37 and 66) and fix diacritics; no act made these changes, and they are the '
            'publisher\'s.',
        ],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/2175, Common Crawl 20250916110121)
        'label': 'OG nr. 21/1992', 'kind': 'decree',
        'title': 'Ordonanța Guvernului nr. 21/1992 privind protecția consumatorilor, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 212 din 28 august 1992',
        'enacted': '1992-08-21', 'published': '1992-08-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/2175',
    }
    P.BASE_LAWS.setdefault('legea-476-2006', {  # read as published (DetaliiDocumentAfis/77917, Common Crawl 20251216172342)
        'label': 'Legea nr. 476/2006', 'kind': 'law',
        'title': 'Legea nr. 476/2006 pentru modificarea și completarea Ordonanței Guvernului nr. 21/1992 privind '
                 'protecția consumatorilor, publicată în Monitorul Oficial al României, Partea I, nr. 1.018 din 21 '
                 'decembrie 2006',
        'enacted': '2006-12-12', 'published': '2006-12-21', 'url': P.PORTAL + 'DetaliiDocumentAfis/77917',
    })
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
