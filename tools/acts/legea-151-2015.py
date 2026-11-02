"""Legea nr. 151/2015 privind procedura insolvenței persoanelor fizice (Lexifina, 2026-11-02).

Act page 169194, also its base text (DetaliiDocumentAfis/169194); no republication; 4 forms 24.12.2015 .. 01.01.2018,
all held from Common Crawl (forms.d/legea-151-2015.json, listed from DetaliiDocumentAfis/169194). Parsed as the Phase 6
acts. The law's in-force day was put off three times before it took effect (decision lines).
"""
SLUG = 'legea-151-2015'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-151-2015', 'short': 'Legea nr. 151/2015', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 151/2015 privind procedura insolvenței persoanelor fizice',
        'url': P.PORTAL + 'DetaliiDocument/169194',
        'in_force': '2018-01-01', 'first_law': SLUG,
        # art. 93: art. 92 in force 3 days after publication (Monitorul Oficial nr. 464 of 26 June 2015)
        'early_units': {
            'day': '2015-06-29',
            'arts': {'art-092': None},
            'note': 'Art. 92 of the law, in force 3 days after the law was published in Monitorul Oficial nr. 464 of '
                    '26 June 2015, as its art. 93 provides. The rest of the law takes effect on 1 January 2018, its '
                    'in-force day as put off by OUG nr. 61/2015, OUG nr. 98/2016 and OG nr. 6/2017.',
        },
        'base_note': 'The rest of the law as published in Monitorul Oficial nr. 464 of 26 June 2015, in force on 1 '
                     'January 2018: its art. 93 set 6 months after publication, a day put off to 31 December 2016 by '
                     'OUG nr. 61/2015, to 1 August 2017 by OUG nr. 98/2016 (art. IX) and to 1 January 2018 by OG nr. '
                     '6/2017.',
        'form_note': {}, 'republished': {},
        'repeal_acts': {},
        'decisions': [
            'Legea nr. 151/2015: the law as published in Monitorul Oficial nr. 464 of 26 June 2015 '
            '(DetaliiDocumentAfis/169194). Its art. 93 puts it in force 6 months after publication, except art. 92 '
            '(setting up the insolvency commissions and the implementing rules), in force 3 days after publication. '
            'So the first version, of 29 June 2015, holds only art. 92; the rest of the law as published is added on '
            'the day it took effect, credited to Legea nr. 151/2015.',
            'Legea nr. 151/2015: that day was put off three times before it came, as the portal\'s notes on the law '
            'say: to 31 December 2016 by the single article of OUG nr. 61/2015 (Monitorul Oficial nr. 962 of 24 '
            'December 2015), to 1 August 2017 by art. IX of OUG nr. 98/2016 (Monitorul Oficial nr. 1.030 of 21 '
            'December 2016) and to 1 January 2018 by the single article of OG nr. 6/2017 (Monitorul Oficial nr. 614 '
            'of 28 July 2017). None of these acts changes the law\'s text; the rest of the law is shown from 1 '
            'January 2018.',
            'Legea nr. 151/2015: the portal\'s forms of 24 December 2015, 21 December 2016 and 31 July 2017 come '
            'before the law took effect and are not used. No act changed the text before then: the forms of 2015 and '
            '2016 differ from the text as published only in one word of art. 22 alin. (1) ("le-ar" where the text '
            'as published and the later forms print "lear"), and the form of 2017 not at all. The form of 1 January 2018, the newest the portal lists, prints the law as published.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/169194, Common Crawl 20251015012956)
        'label': 'Legea nr. 151/2015', 'kind': 'law',
        'title': 'Legea nr. 151/2015 privind procedura insolvenței persoanelor fizice, publicată în Monitorul Oficial '
                 'al României, Partea I, nr. 464 din 26 iunie 2015',
        'enacted': '2015-06-18', 'published': '2015-06-26', 'url': P.PORTAL + 'DetaliiDocumentAfis/169194',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
