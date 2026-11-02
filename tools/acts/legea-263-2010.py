"""Legea nr. 263/2010 privind sistemul unitar de pensii publice (Lexifina, 2026-11-02).

Act page 124530, also its base text (DetaliiDocumentAfis/124530); 73 consolidated forms 2010-12-30 .. 31.08.2023, all
held (forms.d/legea-263-2010.json, listed from the act page's capture showing 31.08.2023). Parsed as the Phase 6 acts.
Repealed in full by Legea nr. 360/2023 (acts/legea-360-2023.py) from 1 September 2024 (act_repeal).
"""
SLUG = 'legea-263-2010'

# Legea nr. 360/2023, read as published (DetaliiDocumentAfis/276927)
CC360 = {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/276927',
         'timestamp': '20260121170559', 'crawl': 'CC-MAIN-2026-04',
         'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469725.43/warc/'
                     'CC-MAIN-20260121144900-20260121174900-00879.warc.gz',
         'offset': '258497335', 'length': '155584'}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-263-2010', 'short': 'Legea nr. 263/2010', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 263/2010 privind sistemul unitar de pensii publice',
        'url': P.PORTAL + 'DetaliiDocument/124530',
        'in_force': '2011-01-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 852 of 20 December 2010, in force on 1 January '
                     '2011 (its art. 193 alin. (1)), save art. 70 alin. (1), art. 132, 135 and 194, which took effect '
                     'on 23 December 2010.',
        'form_note': {}, 'republished': {},
        # the portal's form of 30.12.2010 prints OUG nr. 117/2010 (published that day) before the law took effect
        # (1 January 2011): read as of 1 January 2011, after the text as published. The portal lists form 138601
        # under 01.10.2008, before the law existed; its text is the law updated to 24 June 2012 (between the forms
        # of 09.05.2012 and 09.08.2012)
        'read_on': {'125116': '2011-01-01', '138601': '2012-06-24'},
        # the repeal note of an article printed as "Abrogat" follows the article's closing tag
        'trailing_notes': True,
        # the portal prints "la 12-07-2021" on the note of art. 149 alin. (2) (forms 2019-07-20 .. 2021); its sibling
        # note on alin. (1) and its editorial note give 12 July 2019, the day art. 183 alin. (1) of Legea nr. 127/2019
        # took effect
        'note_date_fix': [('2021-07-12', '2019-07-12', 'Articolul 183 din LEGEA nr. 127 din 8 iulie 2019')],
        # the whole law repealed after its newest form (31.08.2023), read from the repealing act as published
        'act_repeal': {
            'law': 'legea-360-2023', 'day': '2024-09-01', 'page': '276927',
            'capture': CC360['timestamp'], 'cc': CC360,
            'note': 'Legea nr. 263/2010 repealed in full by art. 168 alin. (1) lit. a) of Legea nr. 360/2023 privind '
                    'sistemul public de pensii (Monitorul Oficial nr. 1089 of 4 December 2023), on the day that law '
                    'took effect (its art. 167): 1 September 2024.'},
        'decisions': [
            'Legea nr. 263/2010: the first version is the law as published in Monitorul Oficial nr. 852 of 20 '
            'December 2010 (DetaliiDocumentAfis/124530), in force on 1 January 2011 (its art. 193 alin. (1)). Art. 70 '
            'alin. (1), art. 132, 135 and 194 took effect 3 days after publication (23 December 2010); they are '
            'shown from 1 January 2011 with the rest of the law.',
            'Legea nr. 263/2010: the portal\'s form of 30 December 2010 is the law with the changes of OUG nr. 117/2010 '
            '(Monitorul Oficial nr. 891 of 30 December 2010), published before the law took effect. It is read as of '
            '1 January 2011, the same day as the text as published and after it, so the amended text is the one in '
            'force from that day; its changes are credited to OUG nr. 117/2010, as the portal\'s notes say. The form '
            'of 1 January 2011 adds only the portal\'s note quoting art. 17 of Legea nr. 287/2010 and changes no '
            'article.',
            'Legea nr. 263/2010: the portal lists one form (138601) under 1 October 2008, before the law existed. '
            'Its text is the law "updated to 24 June 2012" (the day the provisions of Decizia Curții Constituționale '
            'nr. 297/2012 ceased to have effect), and it sits between the forms of 9 May and 9 August 2012 in the '
            'portal\'s order of ids; it is read as of 24 June 2012. It changes no article.',
            'Legea nr. 263/2010: the forms of 20 July 2019 to 2021 print, on art. 149 alin. (2), the note "la '
            '12-07-2021 ... abrogat de alin. (1) al art. 183 din LEGEA nr. 127 din 8 iulie 2019". The note on alin. '
            '(1) of the same article is dated 12-07-2019 and the portal\'s own note under both says that art. 183 '
            'alin. (1) took effect 3 days after publication (Monitorul Oficial nr. 563 of 9 July 2019), "respectiv '
            '12 iulie 2019"; the printed year is a misprint and the note is read as 12 July 2019.',
            'Legea nr. 263/2010: the portal\'s notes on Decizia Curții Constituționale nr. 297/2012 (art. 196 lit. '
            'j), unconstitutional as it applies to the Court of Accounts\' councillors) and nr. 680/2012 (art. 73 '
            'alin. (1), the phrase "în raport cu vârsta, conform tabelului nr. 3") say those provisions were '
            'suspended and then ceased (or would cease) to have effect on 24 June and 24 September 2012. No form '
            'removes their words on those days (art. 73 is rewritten by Legea nr. 37/2013 from 1 April 2013, and '
            'art. 196 lit. j) stays), so the text is kept as printed.',
            'Legea nr. 263/2010: the forms of 2011-2015 print, as paragraphs of arts. 27, 102, 125 and 170, the '
            'portal\'s quotations of Legea nr. 287/2010 art. 17 (contribution rates of 2011), OUG nr. 1/2013 art. II '
            'and Legea nr. 340/2013 art. II (the point value of 2013 and 2014), Legea nr. 6/2013 and Legea nr. '
            '340/2013 art. 17 (death grant amounts) and the correction index of 2013; they are not the law\'s text '
            'and are left out.',
            'Legea nr. 263/2010: repealed in full by art. 168 alin. (1) lit. a) of Legea nr. 360/2023 privind '
            'sistemul public de pensii (enacted 29 November 2023, published in Monitorul Oficial nr. 1089 of 4 '
            'December 2023), read as published (DetaliiDocumentAfis/276927), from the day that law took effect: 1 '
            'September 2024 (its art. 167; art. 168 alin. (1) is not among the provisions that took effect on 1 '
            'January 2024). The record ends with a version that removes every article, credited to Legea nr. '
            '360/2023 (legea-360-2023/). The portal lists no form of Legea nr. 263/2010 after that of 31 August '
            '2023, so any amendment between that day and the repeal is missing.',
        ],
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 263/2010', 'kind': 'law',
        'title': 'Legea nr. 263 din 16 decembrie 2010, publicată în Monitorul Oficial al României, Partea I, nr. 852 '
                 'din 20 decembrie 2010',
        'enacted': '2010-12-16', 'published': '2010-12-20', 'url': P.PORTAL + 'DetaliiDocument/124530',
    }
    # the portal's editorial quotations of other acts, printed as paragraphs of the articles they concern: Legea nr.
    # 287/2010 art. 17 in art. 27 (2011-2014 forms), OUG nr. 1/2013 art. II and Legea nr. 340/2013 art. II (the point
    # value of 2013 and 2014) in art. 102, Legea nr. 6/2013 and Legea nr. 340/2013 art. 17 (death grant amounts) in art.
    # 125, OUG nr. 1/2013 (correction index 2013) in art. 170
    P.EDITORIAL_LINES[SLUG] = {
        'art-027': ('"Art. 17', '(1) Pentru anul 2011 cotele de contribuție de asigurări sociale se stabilesc',
                    'a) 31,3% pentru condiții normale de muncă, datorată de angajator',
                    'b) 36,3% pentru condiții deosebite de muncă, datorată de angajator',
                    'c) 41,3% pentru condiții speciale de muncă, datorată de angajator',
                    '(2) În cota de contribuție individuală de asigurări sociale prevăzută la alin. (1) este inclusă',
                    '(3) Cotele prevăzute la alin. (1) și (2) se aplică începând cu veniturile aferente lunii ianuarie '
                    '2011."'),
        'art-102': ('1. Conform art. II din ORDONANȚA DE URGENȚĂ nr. 1 din 22 ianuarie 2013',
                    '2. Conform art. II din LEGEA nr. 340 din 10 decembrie 2013'),
        'art-125': ('1. A se vedea și art. 17 din LEGEA nr. 6', '2. A se vedea și art. 17 din LEGEA nr. 340',
                    'a) asiguratului sau pensionarului, la 2.223 lei', 'a) asiguratului sau pensionarului, la 2.298 lei',
                    'b) unui membru de familie al asiguratului sau al pensionarului, la 1.112 lei',
                    'b) unui membru de familie al asiguratului sau al pensionarului, la 1.149 lei'),
        'art-170': ('"(1) În anul 2013, indicele de corecție care se aplică punctajului mediu anual',
                    '(2) Indicele de corecție prevăzut la alin. (1) se aplică și punctajelor medii anuale calculate',
                    '(3) În situația persoanelor prevăzute la alin. (2), indicele de corecție se aplică asupra'),
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
