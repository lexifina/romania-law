"""Legea nr. 99/2016 privind achizițiile sectoriale (Lexifina, 2026-11-02).

Act page 178661 is also its base text (DetaliiDocumentAfis/178661); no republication; 19 forms, all held from Common
Crawl or the Internet Archive. forms.d/legea-99-2016.json.
"""
SLUG = 'legea-99-2016'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-99-2016', 'short': 'Legea nr. 99/2016', 'pad': 3, 'titles': False,
        'trailing_notes': True, 'cc_forms': True,
        # art. 257 alin. (2): art. 208 alin. (2) in force on 18 October 2018; the forms print it from the start
        'later_provisions': (
            {'day': '2018-10-18', 'law': SLUG,
             'lines': ('(2) Entitățile contractante utilizează e-Certis',),
             'note': 'Art. 208 alin. (2) takes effect on this day (art. 257 alin. (2) of the law); the portal prints it '
                     'from the law as published.'},
        ),
        # the value thresholds (art. 12 alin. (1), art. 24 alin. (1) lit. a)): the portal rewrote them in its then-newest
        # form from 1 January of the year its editorial note gives (EU delegated regulations), so they are dated that day
        'editorial_days': {
            '222868': {'art-012': '2020-01-01'},  # Regulamentul delegat (UE) 2019/1829 (art. 12 only in the note)
            '245517': {'art-012': '2022-01-01', 'art-024': '2022-01-01'},  # Regulamentele delegate 2021/1950-1953
            '266840': {'art-012': '2024-01-01', 'art-024': '2024-01-01'},  # 2023/2495-2497, 2023/2510
        },
        'title': 'Legea nr. 99/2016 privind achizițiile sectoriale',
        'url': P.PORTAL + 'DetaliiDocument/178661',
        'in_force': '2016-05-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 391 of 23 May 2016, in force 3 days after '
                     'publication (its art. 257 alin. (1)): 26 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 99/2016: the first version is the law as published in Monitorul Oficial nr. 391 of 23 May 2016 '
            '(DetaliiDocumentAfis/178661), dated 26 May 2016: its art. 257 alin. (1) puts it in force 3 days after '
            'publication. Its art. 257 alin. (2) puts art. 208 alin. (2) in force on 18 October 2018; under the rule for '
            'text printed before its day, that provision is absent until then and is added that day, credited to '
            'Legea nr. 99/2016.',
            'Legea nr. 99/2016: the value thresholds of art. 12 alin. (1) and art. 24 alin. (1) lit. a) are not amended '
            'by a Romanian act: the portal rewrites the amounts when EU delegated regulations change them, with an '
            'editorial note giving the new amounts and the day they apply from (1 January 2020, 2022 and 2024). Those '
            'changes are dated by the editorial note, the earlier amounts standing until then: art. 12 on 1 January '
            '2020 (form of 12.02.2020), arts. 12 and 24 on 1 January 2022 (form of 30.08.2021) and 1 January 2024 '
            '(form of 21.04.2023). No note names a law for them, so they are the publisher\'s. The form of 12.02.2020 '
            'also changes the amounts in art. 24, which that note does not cover; that change keeps the form\'s date.',
            'Legea nr. 99/2016: the law as published and the form of 6 June 2016 print two misprints (art. 149 '
            '"i^n" for "în", art. 179 "l77" for "177"); the form of 9 June 2016 prints them corrected, the form of 11 '
            'January 2017 misprints them again, and the form of 22 December 2017 corrects them for good; the form of '
            '4 June 2018 prints a stub "Abrogat." for art. 246 '
            'with a full stop; the form of 12 February 2020 prints art. 196 alin. (5) as "Abrogat."; the form of 7 July '
            '2020 prints art. 4 alin. (1) lit. d) as "abrogată." and art. 6 alin. (3) as "Abrogat." No note explains '
            'them. These changes are the publisher\'s, labelled unexplained.',
            'Legea nr. 99/2016: the portal prints some repeal notes just after the article they concern; they are read '
            'as that article\'s notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178661)
        'label': 'Legea nr. 99/2016', 'kind': 'law',
        'title': 'Legea nr. 99/2016 privind achizițiile sectoriale, publicată în Monitorul Oficial al României, '
                 'Partea I, nr. 391 din 23 mai 2016',
        'enacted': '2016-05-19', 'published': '2016-05-23', 'url': P.PORTAL + 'DetaliiDocumentAfis/178661',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
