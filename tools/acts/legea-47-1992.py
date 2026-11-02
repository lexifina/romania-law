"""Legea nr. 47/1992 privind organizarea și funcționarea Curții Constituționale (Lexifina, 2026-11-02).

Act page 124149 (also the 2010 republication); base DetaliiDocumentAfis/2248 (the law as published in 1992); 10 forms
listed, all held from Common Crawl (forms.d/legea-47-1992.json): republications 2250 (1997) and 53577 (2004) read from
their DetaliiDocumentAfis pages ('afis'), the act page's own republication 124149 (2010) from its DetaliiDocumentAfis
page ('afis_cc'). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-47-1992'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-47-1992', 'short': 'Legea nr. 47/1992', 'pad': 3, 'cc_forms': True,
        'revert_credit': True, 'revert_unic': True,
        'title': 'Legea nr. 47/1992 privind organizarea și funcționarea Curții Constituționale',
        'url': P.PORTAL + 'DetaliiDocument/124149',
        'in_force': '1992-05-22', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 101 of 22 May 1992; it sets no day of its own, so '
                     'in force on publication (Constituția art. 78 as it then stood).',
        'form_note': {'2250': 'The law as republished in Monitorul Oficial nr. 187 of 7 August 1997 under art. III of '
                              'Legea nr. 138/1997, with renumbered articles.',
                      '53577': 'The law as republished in Monitorul Oficial nr. 643 of 16 July 2004 under art. III of '
                               'Legea nr. 232/2004, with renumbered articles.',
                      '124149': 'The law as republished in Monitorul Oficial nr. 807 of 3 December 2010 under art. V '
                                'of Legea nr. 177/2010, with renumbered articles.'},
        'republished': {'2250': 'legea-138-1997', '53577': 'legea-232-2004', '124149': 'legea-177-2010'},
        'repeal_acts': {
            'legea-330-2009': {
                'label': 'Legea-cadru nr. 330/2009', 'page': '113154', 'capture': '20260218223533',
                'cc': {'crawl': 'CC-MAIN-2026-08', 'timestamp': '20260218223533',
                       'filename': 'crawl-data/CC-MAIN-2026-08/segments/1770395866066.88/warc/'
                                   'CC-MAIN-20260218201643-20260218231643-00631.warc.gz',
                       'offset': '258029969', 'length': '346615',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/113154'},
                'in_force': '2010-01-01',
                'why': 'its art. 47: in force on 1 January 2010 (save arts. 49-52, which art. 48 is not)',
                'read': 'art. 48 alin. (1): "La data intrării în vigoare a prezentei legi se abrogă: ... 39. Art. 70 din '
                        'Legea nr. 47/1992 privind organizarea și funcționarea Curții Constituționale, republicată în '
                        'Monitorul Oficial al României, Partea I, nr. 643 din 16 iulie 2004."'},
        },
        'decisions': DECISIONS,
    }
    P.BASE_LAWS.update({
        SLUG: {  # read from the act as published (DetaliiDocumentAfis/2248, Common Crawl 20260122081843)
            'label': 'Legea nr. 47/1992', 'kind': 'law',
            'title': 'Legea nr. 47/1992 privind organizarea și funcționarea Curții Constituționale, publicată în '
                     'Monitorul Oficial al României, Partea I, nr. 101 din 22 mai 1992',
            'enacted': '1992-05-18', 'published': '1992-05-22', 'url': P.PORTAL + 'DetaliiDocumentAfis/2248',
        },
        'legea-138-1997': {  # read from the act as published (DetaliiDocumentAfis/11771, Common Crawl 20260207014843)
            'label': 'Legea nr. 138/1997', 'kind': 'law',
            'title': 'Legea nr. 138/1997 pentru modificarea și completarea Legii nr. 47/1992 privind organizarea și '
                     'funcționarea Curții Constituționale, publicată în Monitorul Oficial al României, Partea I, nr. '
                     '170 din 25 iulie 1997',
            'enacted': '1997-07-24', 'published': '1997-07-25', 'url': P.PORTAL + 'DetaliiDocumentAfis/11771',
        },
        'legea-232-2004': {  # read from the act as published (DetaliiDocumentAfis/52439, Common Crawl 20251010182241)
            'label': 'Legea nr. 232/2004', 'kind': 'law',
            'title': 'Legea nr. 232/2004 pentru modificarea și completarea Legii nr. 47/1992 privind organizarea și '
                     'funcționarea Curții Constituționale, publicată în Monitorul Oficial al României, Partea I, nr. '
                     '502 din 3 iunie 2004',
            'enacted': '2004-06-03', 'published': '2004-06-03', 'url': P.PORTAL + 'DetaliiDocumentAfis/52439',
        },
        'legea-177-2010': {  # read from the act as published (DetaliiDocumentAfis/122525, Common Crawl 20251111173537)
            'label': 'Legea nr. 177/2010', 'kind': 'law',
            'title': 'Legea nr. 177/2010 pentru modificarea și completarea Legii nr. 47/1992 privind organizarea și '
                     'funcționarea Curții Constituționale, a Codului de procedură civilă și a Codului de procedură '
                     'penală al României, publicată în Monitorul Oficial al României, Partea I, nr. 672 din 4 '
                     'octombrie 2010',
            'enacted': '2010-09-28', 'published': '2010-10-04', 'url': P.PORTAL + 'DetaliiDocumentAfis/122525',
        },
    })
    # The base text, the 1997 and 2004 republications and the forms of 07.10.2010, 04.07.2012 and 23.06.2013 print
    # the numbered sub-headings of chapter III ("2. Verificarea constituționalității inițiativelor de revizuire a
    # Constituției", ...) as the last line of the article before them; they are headings, not that article's text.
    P.EDITORIAL_LINES[SLUG] = {k: tuple(v) for k, v in HEADINGS.items()}
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)


_H = {
    2: ('2. Verificarea constituționalității inițiativelor de revizuire a Constituției',
        '2. Controlul constituționalității regulamentelor Parlamentului'),
    3: ('3. Soluționarea excepției de neconstituționalitate',
        '3. Controlul constituționalității tratatelor sau a altor acorduri internaționale'),
    4: ('4. Respectarea procedurii pentru alegerea Președintelui României',
        '4. Controlul constituționalității regulamentelor Parlamentului'),
    5: ('5. Judecarea contestațiilor care au ca obiect constituționalitatea unui partid politic',
        '5. Soluționarea excepției de neconstituționalitate ridicate în fața instanțelor judecătore'),
    6: ('6. Emiterea avizului pentru suspendarea din funcție a Președintelui României',
        '6. Soluționarea excepției de neconstituționalitate ridicate de Avocatul Poporului'),
    7: ('7. Constatarea existenței împrejurărilor care justifica interimatul în exercitarea funcției de Pre',
        '7. Soluționarea conflictelor juridice de natură constituțională dintre autoritățile publice'),
    8: ('8. Respectarea procedurii pentru alegerea Președintelui României',),
    9: ('9. Judecarea contestațiilor care au ca obiect constituționalitatea unui partid politic',),
    10: ('10. Emiterea avizului pentru suspendarea din funcție a Președintelui României',),
    11: ('11. Constatarea existenței împrejurărilor care justifică interimatul în exercitarea funcției de Pre',),
    12: ('12. Exercitarea atribuțiilor privitoare la organizarea și desfășurarea referendumului și la confirma',),
    13: ('13. Verificarea îndeplinirii condițiilor pentru exercitarea inițiativei legislative de către cetă',),
}
# article (in each text's own numbering) -> the sub-heading lines printed at its end
HEADINGS = {
    'art-018': _H[2], 'art-020': _H[2], 'art-022': _H[3], 'art-023': _H[3], 'art-025': _H[4], 'art-026': _H[4],
    'art-027': _H[5], 'art-028': _H[5], 'art-030': _H[6], 'art-031': _H[6], 'art-032': _H[7], 'art-033': _H[7],
    'art-036': _H[8], 'art-038': _H[9], 'art-041': _H[10], 'art-043': _H[11], 'art-045': _H[12], 'art-047': _H[13],
}

DECISIONS = [
    'Legea nr. 47/1992: the first version is the law as published in Monitorul Oficial nr. 101 of 22 May 1992 '
    '(DetaliiDocumentAfis/2248), in force that day: it sets no day of its own (Constituția art. 78 as it then stood). '
    'The portal holds no form between the base text and the republication of 7 August 1997, none between that and '
    'the republication of 16 July 2004, and none between that and the form of 1 January 2010, so the changes made in '
    'those years arrive with the next text held.',
    'Legea nr. 47/1992: the republications of 7 August 1997 (art. III of Legea nr. 138/1997, enacted 24 July 1997, '
    'published in Monitorul Oficial nr. 170 of 25 July 1997), 16 July 2004 (art. III of Legea nr. 232/2004, enacted '
    'and published in Monitorul Oficial nr. 502 of 3 June 2004) and 3 December 2010 (art. V of Legea nr. 177/2010, '
    'enacted 28 September 2010, published in Monitorul Oficial nr. 672 of 4 October 2010), each with renumbered '
    'articles, are read from their texts as printed (DetaliiDocumentAfis/2250, 53577, 124149); files follow each '
    'text\'s own numbering. Changes on those days that no note explains are credited to the act that ordered the '
    'republication, as each republication note says; the 2004 note also names Legea nr. 124/2000, whose changes '
    'arrive with that republication. Each ordering act was read as published (DetaliiDocumentAfis/11771, 52439, '
    '122525).',
    'Legea nr. 47/1992: the act page 124149 stands, in the portal\'s list of forms, both for the republication of 3 '
    'December 2010 and for the newest form (08.12.2023, which also has its own page, 269412); the 2010 text is read '
    'from DetaliiDocumentAfis/124149 and the newest form from the act page.',
    'Legea nr. 47/1992: the base text, the republications of 1997 and 2004 and the forms of 7 October 2010, 4 July '
    '2012 and 23 June 2013 print the numbered sub-headings of chapter III ("2. Verificarea constituționalității '
    'inițiativelor de revizuire a Constituției" and the others) as the last line of the article before them; they are '
    'headings, not that article\'s text, and are left out in every form.',
    'Legea nr. 47/1992: art. 27 alin. (1), changed on 4 July 2012 by OUG nr. 38/2012, is printed in its earlier wording '
    'from the form of 23 June 2013 with the portal\'s note that it went back to that wording because art. unic of '
    'Legea nr. 183/2013 (Monitorul Oficial nr. 369 of 20 June 2013, in force 3 days later, on 23 June 2013) rejected '
    'the ordinance; the change is credited to Legea nr. 183/2013.',
    'Legea nr. 47/1992: art. 63 (the judges\' oath) is printed without its quotation marks from the form of 19 March '
    '2018, with no note: the publisher\'s typesetting.',
    'Legea nr. 47/1992: the act page as captured on 9 June 2026 (Internet Archive 20260609105631) still shows the form '
    'of 8 December 2023 as the newest.',
]
