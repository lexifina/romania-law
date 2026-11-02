"""Legea nr. 263/2010 privind sistemul unitar de pensii publice (Lexifina, 2026-11-02).

Act page 124530, also its base text (DetaliiDocumentAfis/124530); 73 consolidated forms 2010-12-30 .. 31.08.2023, all
held (forms.d/legea-263-2010.json, listed from the act page's capture showing 31.08.2023). Parsed as the Phase 6 acts.
Repealed in full by Legea nr. 360/2023 (acts/legea-360-2023.py) from 1 September 2024 (act_repeal).
"""
SLUG = 'legea-263-2010'


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
        'decisions': [],
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
