"""Legea nr. 98/2016 privind achizițiile publice (Lexifina, 2026-11-02).

Act page 178667 is also its base text (DetaliiDocumentAfis/178667); no republication; 20 forms, all held from
Common Crawl (forms listed by the act page's capture 20260218054809). forms.d/legea-98-2016.json.
"""
SLUG = 'legea-98-2016'


def register(P):
    P.ACTS[SLUG] = {
        # repeal notes printed just after the article (art. 225, 22.12.2017): trailing_notes
        **P.P6, 'part': '9z-legea-98-2016', 'short': 'Legea nr. 98/2016', 'pad': 3, 'titles': False,
        'trailing_notes': True, 'cc_forms': True,
        # art. 240 alin. (2): art. 199 alin. (2) in force on 18 October 2018; the forms print it from the start
        'later_provisions': (
            {'day': '2018-10-18', 'law': SLUG,
             'lines': ('(2) Autoritățile contractante utilizează e-Certis',),
             'note': 'Art. 199 alin. (2) takes effect on this day (art. 240 alin. (2) of the law); the portal prints it '
                     'from the law as published.'},
        ),
        # the value thresholds (art. 7 alin. (1), art. 19 lit. a)): the portal rewrote them in its then-newest form
        # from 1 January of the year its editorial note gives (EU delegated regulations), so they are dated that day
        'editorial_days': {
            '222867': {'art-007': '2020-01-01'},  # Regulamentul delegat (UE) 2019/1828 (art. 7 only in the note)
            '245516': {'art-007': '2022-01-01', 'art-019': '2022-01-01'},  # Regulamentele delegate 2021/1950-1953
            '259943': {'art-007': '2024-01-01', 'art-019': '2024-01-01'},  # 2023/2495-2497, 2023/2510
            '178667': {'art-007': '2026-01-01', 'art-019': '2026-01-01'},  # 2025/2150-2152
        },
        'title': 'Legea nr. 98/2016 privind achizițiile publice',
        'url': P.PORTAL + 'DetaliiDocument/178667',
        'in_force': '2016-05-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 390 of 23 May 2016, in force 3 days after '
                     'publication (its art. 240 alin. (1)): 26 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 98/2016: the first version is the law as published in Monitorul Oficial nr. 390 of 23 May 2016 '
            '(DetaliiDocumentAfis/178667), dated 26 May 2016: its art. 240 alin. (1) puts it in force 3 days after '
            'publication. Its art. 240 alin. (2) puts art. 199 alin. (2) in force on 18 October 2018; under the rule for '
            'text printed before its day, that provision is absent until then and is added that day, credited to '
            'Legea nr. 98/2016.',
            'Legea nr. 98/2016: an Internet Archive capture of the act page of 28 May 2026 (20260528125304) shows the '
            'same newest form (17.11.2024) and lists the same forms.',
            'Legea nr. 98/2016: the value thresholds of art. 7 alin. (1) and art. 19 lit. a) are not amended by a '
            'Romanian act: the portal rewrites the amounts in its newest form when EU delegated regulations change '
            'them, with an editorial note giving the new amounts and the day they apply from (1 January 2020, 2022, '
            '2024 and 2026). Those changes are dated by the editorial note, the earlier amounts standing until then: '
            'art. 7 on 1 January 2020 (form of 12.02.2020), arts. 7 and 19 on 1 January 2022 (form of 30.08.2021), 1 '
            'January 2024 (form of 06.10.2022) and 1 January 2026 (form of 17.11.2024). No note names a law for them, '
            'so they are the publisher\'s. The form of 12.02.2020 also changes the amounts in art. 19 lit. a), which '
            'that note does not cover; that change keeps the form\'s date.',
            'Legea nr. 98/2016: the forms of 6 June to 12 August 2016 leave out art. 167 alin. (1) lit. g), which no act '
            'repealed, and the form of 22 November 2016 prints it again unchanged; every form from 6 June 2016 on '
            'leaves the word "oferta" out of art. 187 alin. (2) ("stabilește cea mai avantajoasă ..."), and no note '
            'explains it. These changes are the publisher\'s, labelled unexplained.',
            'Legea nr. 98/2016: the form of 22 November 2016 alone prints marginal titles ("Praguri", ...), which '
            'neither the law as published nor any other form has; they are read as headings, not text. The same form '
            'prints the law\'s EU-transposition note ("*Prezenta lege transpune ...") as the last lines of art. 240; it '
            'is not an article\'s text and is left out, as in the other forms.',
            'Legea nr. 98/2016: the portal prints some repeal notes just after the article they concern ("Articolul 225 '
            '... a fost abrogat de Punctul 41, Articolul I din ORDONANȚA DE URGENȚĂ nr. 107 ..."); they are read as '
            'that article\'s notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178667, Common Crawl 20251118194653)
        'label': 'Legea nr. 98/2016', 'kind': 'law',
        'title': 'Legea nr. 98/2016 privind achizițiile publice, publicată în Monitorul Oficial al României, Partea I, '
                 'nr. 390 din 23 mai 2016',
        'enacted': '2016-05-19', 'published': '2016-05-23', 'url': P.PORTAL + 'DetaliiDocumentAfis/178667',
    }
    # the form of 22.11.2016 prints the law's EU-transposition note as the last lines of art. 240
    P.EDITORIAL_LINES[SLUG] = {'art-240': ('*', 'Prezenta lege transpune art. 3, art. 5, art. 7-21')}
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
