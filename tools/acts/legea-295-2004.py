"""Legea nr. 295/2004 privind regimul armelor și al munițiilor (Lexifina, 2026-11-02).

Act page 53150, also the text as published (DetaliiDocumentAfis/53150). 23 forms 30.12.2004 .. 02.11.2025 are listed
(forms.d/legea-295-2004.json) and all are held. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-295-2004'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-295-2004', 'short': 'Legea nr. 295/2004', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'typeset_notes': True,
        'root_word': 'act page',
        'title': 'Legea nr. 295/2004 privind regimul armelor și al munițiilor',
        'url': P.PORTAL + 'DetaliiDocument/53150',
        'in_force': '2004-12-30', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 583 of 30 June 2004, in force 6 months after '
                     'publication (its art. 145): 30 December 2004.',
        'form_note': {
            '132994': 'The law as republished on 17 November 2011 under art. VII of Legea nr. 117/2011.',
            '158882': 'The law as republished on 10 June 2014 under art. 248 of Legea nr. 187/2012.'},
        'republished': {'132994': 'legea-117-2011', '158882': 'legea-187-2012'},
        'decisions': [
            'Legea nr. 295/2004: the first version is the law as published in Monitorul Oficial nr. 583 of 30 June '
            '2004 (DetaliiDocumentAfis/53150), dated 30 December 2004: its art. 145 puts it in force 6 months after '
            'publication.',
            'Legea nr. 295/2004: the republication of 17 November 2011 (132994) is credited, for the changes no note '
            'explains, to Legea nr. 117/2011, under whose art. VII it was republished, as its own note says.',
            'Legea nr. 295/2004: the republication of 10 June 2014 (158882) is credited, for the changes no note '
            'explains, to Legea nr. 187/2012, under whose art. 248 it was republished, as its own note says.',
            'Legea nr. 295/2004: arts. 4, 19, 58^3, 92, 93, 98, 99, 100, 102, 123, 127, 128, 139 and 140 are left out '
            'of the form of 27 July 2011. Legea nr. 117/2011 (Monitorul Oficial nr. 446 of 27 June 2011, read as '
            'published, DetaliiDocumentAfis/129609) repeals them in art. I pct. 13, 25, 60, 90, 95, 117, 122 and 128 '
            'and takes effect 30 days after publication (its art. III), on 27 July 2011, the day of the form; the '
            'repeal is dated by the act.',
            'Legea nr. 295/2004: the form of 4 November 2019 (219212) prints, in a note, that under art. I pct. 56 of '
            'Legea nr. 196/2019 (Monitorul Oficial nr. 880 of 1 November 2019) the phrase "arme și muniții" is '
            'replaced throughout the law by "arme, componente esențiale și muniții" and that the replacement was made '
            'directly in the text of the form. The 30 articles that this changes and that carry no note of their own '
            'are credited to Legea nr. 196/2019.',
            'Legea nr. 295/2004: the form of 30 December 2004 (the first form, in force the day the law takes '
            'effect) prints the text with the diacritics partly missing and a few typing errors ("Oblibațiile" for '
            '"Obligațiile" in arts. 77, 110, 111 and 112), so its version differs from the text as published only in '
            'typesetting and is credited to no law; so is the space the form of 17 November 2008 prints in "243/2002 ," '
            'in art. 15.',
            'Legea nr. 295/2004: the form of 17 November 2011 (the republication) prints arts. 21 and 138 without '
            'their marginal titles, which the form of 19 December 2011 prints again; the change is the publisher\'s '
            'and credited to no law.',
            'Legea nr. 295/2004: the headings of subsections ("2. Regimul dreptului de deținere a armelor letale", '
            '"2. Procurarea, deținerea și folosirea armelor și munițiilor de către ..." and the like), which some '
            'forms print as the last line of the article before them, and the sentence that closes the law in its '
            '2004 text and some forms ("Prezenta lege transpune Directiva nr. 91/477/CEE ..."), are left out of the '
            'articles; the form of 17 November 2008 also prints, under art. 61, the quoted art. IV of the ordinance '
            'that changed it, which is left out.',
        ],
        'form_credits': {'219212': {f'art-{n:03d}': 'legea-196-2019' for n in (
            7, 8, 26, 28, 44, 47, 48, 51, 53, 68, 70, 73, 75, 76, 77, 78, 79, 80, 83, 86, 87, 88, 92, 93, 112, 113,
            114, 126, 127, 133)}},
        'repeal_acts': {
            'legea-117-2011': {
                'label': 'Legea nr. 117/2011', 'page': '129609', 'capture': '20260120025647',
                'cc': {'crawl': 'CC-MAIN-2026-04', 'timestamp': '20260120025647',
                       'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469512.27/warc/'
                                   'CC-MAIN-20260120014810-20260120044810-00553.warc.gz',
                       'offset': '259897088', 'length': '74383',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/129609'},
                'in_force': '2011-07-27',
                'why': 'its art. III: in force 30 days after publication in Monitorul Oficial nr. 446 of 27 June '
                       '2011',
                'read': 'art. I pct. 13 (art. 4), 25 (art. 19), 60 (art. 58^3), 90 (arts. 92 and 93), 95 (arts. 98, '
                        '99, 100 and 102), 117 (art. 123), 122 (arts. 127 and 128) and 128 (arts. 139 and 140): '
                        '"Articolul ... se abrogă."',
                'repeals': {'129867': ('art-004', 'art-019', 'art-058-3', 'art-092', 'art-093', 'art-098',
                                       'art-099', 'art-100', 'art-102', 'art-123', 'art-127', 'art-128', 'art-139',
                                       'art-140')},
                'cite': 'Abrogat de LEGEA nr. 117 din 15 iunie 2011, publicată în MONITORUL OFICIAL nr. 446 din 27 '
                        'iunie 2011'},
        },
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {  # from the text as published (DetaliiDocumentAfis/53150)
        'label': 'Legea nr. 295/2004', 'kind': 'law',
        'title': 'Legea nr. 295/2004 privind regimul armelor și al munițiilor, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 583 din 30 iunie 2004',
        'enacted': '2004-06-28', 'published': '2004-06-30', 'url': P.PORTAL + 'DetaliiDocumentAfis/53150',
    })
    # the headings of subsections (printed as the last line of the article before them in some forms, apart in
    # others) and the mention of the directive the law transposes (art. 145 of the 2004 numbering)
    headings = ('2. Regimul dreptului de', '3. Regimul dreptului de', '4. Regimul procur', '5. Suspendarea, revocarea',
                '6. Regimul c', '7. Furtul, pierderea', '2. Procurarea,', '3. Procurarea,', '4. Procurarea,',
                '5. Regimul func')
    P.EDITORIAL_LINES[SLUG] = {k: headings for k in (
        'art-027', 'art-032', 'art-043', 'art-045', 'art-047', 'art-047-1', 'art-050', 'art-078', 'art-079', 'art-081',
        'art-082', 'art-083', 'art-084', 'art-085')}
    P.EDITORIAL_LINES[SLUG]['art-145'] = ('Prezenta lege transpune Directiva',)
    # the form of 17 November 2008 prints the quoted art. IV of the ordinance that amended art. 61 under it
    P.EDITORIAL_TAILS[SLUG] = {'art-061': '"Art. IV'}
