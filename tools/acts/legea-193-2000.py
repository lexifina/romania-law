"""Legea nr. 193/2000 privind clauzele abuzive din contractele încheiate între profesioniști și consumatori (Lexifina,
2026-11-02).

Act page 24922, also its base text (DetaliiDocumentAfis/24922). 12 forms 15.12.2003 .. 28.05.2022, all held from
Common Crawl (forms.d/legea-193-2000.json, listed from DetaliiDocumentAfis/91502): own pages, and the republications of
2006, 2008 and 2012 from their DetaliiDocumentAfis pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-193-2000'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-193-2000', 'short': 'Legea nr. 193/2000', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 193/2000 privind clauzele abuzive din contractele încheiate între profesioniști și '
                 'consumatori',
        'url': P.PORTAL + 'DetaliiDocument/24922',
        'in_force': '2000-12-10', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 560 of 10 November 2000, in force 30 days after '
                     'publication (its art. 17): 10 December 2000.',
        'form_note': {'77879': 'The law as republished in Monitorul Oficial nr. 1.014 of 20 December 2006 under art. '
                               'III of Legea nr. 65/2002, with renumbered articles.',
                      '91502': 'The law as republished in Monitorul Oficial nr. 305 of 18 April 2008 under art. V lit. '
                               'm) of title III of Legea nr. 363/2007, with renumbered articles.'},
        'republished': {'77879': 'legea-65-2002', '91502': 'legea-363-2007'},
        # the republication of 03.08.2012 prints the law as Legea nr. 76/2012 art. 38 amends it from 15.02.2013 and
        # 01.07.2013; the in-force text of 03.08.2012-30.01.2013 is the form of 22.07.2010 (decision line)
        'skip': {'140214'},
        # the form of 15.12.2003 prints only Legea nr. 65/2002, in force on its publication (MO 52/25.01.2002)
        'form_day': {'48642': '2002-01-25'},
        'form_credits': {
            '48642': {'art-004': 'legea-65-2002'},  # art. 2 of Legea nr. 65/2002 ("contract standard preformulat")
            '149436': {'art-012': 'legea-76-2012', 'art-013': 'legea-76-2012'},  # art. 38 pct. 1, 2 of Legea 76/2012
        },
        'repeal_acts': {},
        'decisions': [
            'Legea nr. 193/2000: the first version is the law as published in Monitorul Oficial nr. 560 of 10 '
            'November 2000 (DetaliiDocumentAfis/24922), in force 30 days after publication (its art. 17): 10 '
            'December 2000.',
            'Legea nr. 193/2000: the portal\'s first form, of 15 December 2003, prints the law with the changes of '
            'Legea nr. 65/2002 alone (its heading and every note name only that law). Legea nr. 65/2002 (Monitorul '
            'Oficial nr. 52 of 25 January 2002; read as published, DetaliiDocumentAfis/33591) has no in-force clause '
            'of its own, so it took effect on publication (Constituția of 1991, art. 78): the form\'s changes are '
            'dated 25 January 2002. Its art. 2 replaces "contract standard" and "clauză standard" with "contract '
            'standard preformulat" and "clauză standard preformulată" throughout the law; the form gives art. 4 no '
            'note of its own, and the change to art. 4 is credited to Legea nr. 65/2002 from that article. The '
            'form\'s other changes (diacritics and spacing) are the publisher\'s.',
            'Legea nr. 193/2000: the republications of 20 December 2006 (art. III of Legea nr. 65/2002) and 18 April '
            '2008 (art. V lit. m) of title III of Legea nr. 363/2007), each with renumbered articles, are read from '
            'their own pages (DetaliiDocumentAfis/77879, 91502); changes on those days that no note explains are '
            'credited to the act that ordered the republication, as each republication note says; files follow each '
            'text\'s own numbering.',
            'Legea nr. 193/2000: the republication of 3 August 2012 (Monitorul Oficial nr. 543, under art. 80 of '
            'Legea nr. 76/2012; DetaliiDocumentAfis/140214) prints the law as art. 38 of Legea nr. 76/2012 amends '
            'it. Those amendments took effect later: art. 38 pct. 3 (the word "profesionist" for "comerciant") on 15 '
            'February 2013 and pct. 1 and 2 (arts. 12 and 13) on 1 July 2013 (art. 82 of Legea nr. 76/2012 as '
            'amended by art. I pct. 2 of OUG nr. 4/2013; both read as published, DetaliiDocumentAfis/138484 and '
            '145075). Apart from them the republished text is the in-force text of the form of 22 July 2010: the '
            'portal\'s form of 31 January 2013 prints that text, with only OUG nr. 4/2013\'s art. 13 alin. (3) '
            'added. Under the rule for text printed before its law, the republication is not read as a version of '
            'its own (it would change nothing in force that day): the earlier text stands, and each amendment '
            'arrives on its own day with the forms of 15 February and 1 July 2013.',
            'Legea nr. 193/2000: the portal lists two forms of 1 July 2013. The first (DetaliiDocument/145121) '
            'prints the text of 15 February 2013 unchanged; the second (DetaliiDocument/149436) prints arts. 12 and '
            '13 in the wording of art. 38 pct. 1 and 2 of Legea nr. 76/2012, in force that day, with no note; those '
            'two changes are credited to Legea nr. 76/2012 (read as published). That form also prints art. 4 alin. '
            '(2) with "comercianți" again (the form of 13 June 2014 has "profesioniști" back) and art. 17 with "La '
            'aceeași dată": no act made these changes, and they are the publisher\'s.',
            'Legea nr. 193/2000: its annex (the list of clauses considered abusive) is not an article and is not '
            'part of this record. Legea nr. 161/2010 (art. II) changed only the annex (lit. j) of pct. 1), so the '
            'form of 22 July 2010 changes no article.',
            'Legea nr. 193/2000: the 2008 and 2012 texts and the forms based on them print the heading of chapter III '
            '("CAP III", "Organele abilitate pentru constatarea contravențiilor și soluționarea litigiilor") as the '
            'last line of art. 7 and the first line of art. 8; from 31 December 2007 the forms print, after the last '
            'article, the law\'s mention that it transposes Directiva 93/13/CEE (with the portal\'s "*" from 2012). '
            'Neither is an article\'s text, and both are left out.',
        ],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/24922, Common Crawl 20251010032224)
        'label': 'Legea nr. 193/2000', 'kind': 'law',
        'title': 'Legea nr. 193/2000 privind clauzele abuzive din contractele încheiate între comercianți și '
                 'consumatori, publicată în Monitorul Oficial al României, Partea I, nr. 560 din 10 noiembrie 2000',
        'enacted': '2000-11-06', 'published': '2000-11-10', 'url': P.PORTAL + 'DetaliiDocumentAfis/24922',
    }
    # the republications of 2008 and 2012 and the forms based on them print the chapter III heading as the last line of
    # art. 7 and the first of art. 8; from 31.12.2007 the forms print, after the last article, the portal's "*" and the
    # law's EU-transposition mention (not an article: no article of the law holds it)
    P.EDITORIAL_LINES[SLUG] = {
        'art-007': ('CAP III',),
        'art-008': ('Organele abilitate pentru constatarea contravențiilor și soluționarea litigiilor',),
        'art-016': ('Prezenta lege transpune prevederile Directivei',),
        'art-017': ('*', 'Prezenta lege transpune prevederile Directivei'),
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
