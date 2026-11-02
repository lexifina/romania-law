"""Legea nr. 126/2018 privind piețele de instrumente financiare (Lexifina, 2026-11-02).

Act page 201860, also its base text (DetaliiDocumentAfis/201860). 10 forms listed by DetaliiDocument/305317
(02.08.2018 .. 16.01.2026), all held from Common Crawl (forms.d/legea-126-2018.json); no republication. It took over
part of Legea nr. 297/2004 (part 99l-legea-297-2004).
"""
SLUG = 'legea-126-2018'
TITLE = 'Legea nr. 126/2018 privind piețele de instrumente financiare'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-126-2018', 'short': 'Legea nr. 126/2018', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/201860',
        'in_force': '2018-07-06', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 521 of 26 June 2018, in force 10 days after '
                     'publication (its art. 284): 6 July 2018.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 126/2018: the first version is the law as published in Monitorul Oficial nr. 521 of 26 June '
            '2018 (DetaliiDocumentAfis/201860), in force 10 days after publication (its art. 284): 6 July 2018. '
            'Art. 169 alin. (5)-(7), which apply from 3 September 2019 (the same article), are shown from 6 July 2018 '
            'with the rest of the law.',
            'Legea nr. 126/2018: Legea nr. 158/2020 (read as published, DetaliiDocumentAfis/228486; Monitorul Oficial '
            'nr. 673 of 29 July 2020) is in force 30 days after publication, on 28 August 2020, save its art. VIII '
            'pct. 16, in force on 3 September 2020 (its art. XXVIII). Art. VIII pct. 16 rewrites art. 177 alin. (3) '
            'and (5); the portal prints the new wording from its form of 28 August 2020. Under the rule for text '
            'printed before its law, the earlier wording of both alineate, as the previous forms print it, stands '
            'until 3 September 2020, when the new wording takes effect, credited to Legea nr. 158/2020.',
            'Legea nr. 126/2018: Legea nr. 188/2022 (read as published, DetaliiDocumentAfis/256681; Monitorul Oficial '
            'nr. 617 of 23 June 2022) is in force 10 days after publication, 3 July 2022, the form\'s date; its art. '
            'V defers art. I pct. 53 (art. 261 alin. (4) partea introductivă and lit. d)) to 1 January 2023 only as '
            'to the environmental objectives of art. 9 lit. c)-f) of Regulamentul (UE) 2020/852, a limit on what '
            'the provision covers, not on its wording; the new wording is shown from 3 July 2022, as the portal '
            'dates it.',
            'Legea nr. 126/2018: the dates of the forms of 25 June and 5 July 2024 follow OUG nr. 71/2024 (read as '
            'published, DetaliiDocumentAfis/284542; Monitorul Oficial nr. 591 of 25 June 2024), in force on '
            'publication save art. V pct. 12-22, 10 days after publication (its art. XIV).',
        ],
        # Legea nr. 158/2020 art. XXVIII: art. VIII pct. 16 (art. 177 alin. (3) and (5)) from 3 September 2020; the
        # form of 28.08.2020 prints the new wording
        'later_provisions': (
            {'day': '2020-09-03', 'law': 'legea-158-2020',
             'lines': ('(3) Depozitarul central furnizează emitenților pentru care efectuează și operațiunile de '
                       'înregistrare prin înscriere în cont și serviciile legate de registrele de acționari',
                       '(5) În situația utilizării sistemului de conturi globale, în vederea determinării structurii '
                       'deținătorilor de instrumente financiare emise de un emitent, la o anumită dată, participanții '
                       'vor raporta depozitarului central, în cazul în care depozitarul central efectuează și '
                       'operațiuni de înscriere în cont și servicii legate de registrele de acționari'),
             'old': {'(3) Depozitarul central furnizează emitenților pentru care efectuează și operațiunile de '
                     'înregistrare prin înscriere în cont și serviciile legate de registrele de acționari':
                     '(3) Depozitarul central furnizează emitenților pentru care efectuează și operațiunile de '
                     'înregistrare prin înscriere în cont informațiile necesare pentru exercitarea drepturilor '
                     'aferente instrumentelor financiare depozitate, altele decât cele derivate, putând presta servicii '
                     'pentru îndeplinirea obligațiilor emitentului față de deținătorii de instrumente financiare, '
                     'altele decât cele derivate.',
                     '(5) În situația utilizării sistemului de conturi globale, în vederea determinării structurii '
                     'deținătorilor de instrumente financiare emise de un emitent, la o anumită dată, participanții '
                     'vor raporta depozitarului central, în cazul în care depozitarul central efectuează și '
                     'operațiuni de înscriere în cont și servicii legate de registrele de acționari':
                     '(5) În situația utilizării sistemului de conturi globale, în vederea determinării structurii '
                     'deținătorilor de instrumente financiare emise de un emitent, la o anumită dată, participanții '
                     'vor raporta depozitarului central, în cazul în care depozitarul central efectuează și '
                     'operațiuni de înscriere în cont, informații privind titularii subconturilor din evidențele '
                     'proprii și deținerile acestora.'},
             'note': 'Art. 177 alin. (3) and (5) in the wording of Legea nr. 158/2020 (art. VIII pct. 16) take effect '
                     'on this day (its art. XXVIII); the portal prints the new wording from its form of 28.08.2020.'},
        ),
        'repeal_acts': {},
        'root_word': 'act page',
    }
    # as the portal's note links name it (the same entry part 99l-legea-297-2004 carries); dates read from the act as
    # published (DetaliiDocumentAfis/201860: "București, 11 iunie 2018. Nr. 126.", MO nr. 521 din 26 iunie 2018)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 126/2018', 'kind': 'law',
        'title': 'Legea nr. 126 din 11 iunie 2018, publicată în Monitorul Oficial al României, Partea I, nr. 521 din 26 '
                 'iunie 2018',
        'enacted': '2018-06-11', 'published': '2018-06-26', 'url': P.PORTAL + 'DetaliiDocument/201860',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
