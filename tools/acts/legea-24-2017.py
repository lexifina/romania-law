"""Legea nr. 24/2017 privind emitenții de instrumente financiare și operațiuni de piață (Lexifina, 2026-11-02).

Act page 187788, also its base text (DetaliiDocumentAfis/187788). 10 forms listed by DetaliiDocumentAfis/305316
(28.08.2020 .. 16.01.2026), all held from Common Crawl (forms.d/legea-24-2017.json); the republication of 10.08.2021
from its DetaliiDocumentAfis page. It took over part of Legea nr. 297/2004 (part 99l-legea-297-2004).
"""
SLUG = 'legea-24-2017'
TITLE = 'Legea nr. 24/2017 privind emitenții de instrumente financiare și operațiuni de piață'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-24-2017', 'short': 'Legea nr. 24/2017', 'pad': 3, 'cc_forms': True,
        # art. 154 rewrites articles of Legea nr. 297/2004 and quotes them (S_ART inside S_ART)
        'quoted_articles': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/187788',
        'in_force': '2017-04-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 213 of 29 March 2017; it sets no general day of '
                     'its own, so in force 3 days after publication (Constituția art. 78): 1 April 2017.',
        'form_note': {'245244': 'The law as republished in Monitorul Oficial nr. 772 of 10 August 2021 under art. III '
                                'of Legea nr. 158/2020, with renumbered articles.'},
        'republished': {'245244': 'legea-158-2020'},
        'decisions': [
            'Legea nr. 24/2017: the first version is the law as published in Monitorul Oficial nr. 213 of 29 March '
            '2017 (DetaliiDocumentAfis/187788), dated 1 April 2017: it sets no general in-force day of its own, so 3 '
            'days after publication (Constituția art. 78). Art. 150 alin. (2) (from 3 January 2018) and art. 154 pct. '
            '4 (from the day set by art. 69 alin. (2) of Regulamentul (UE) nr. 909/2014, its art. 156) are shown '
            'from 1 April 2017 with the rest of the law. The portal\'s first form is of 28 August 2020, so the '
            'changes made up to then arrive together that day.',
            'Legea nr. 24/2017: the republication of 10 August 2021 (art. III of Legea nr. 158/2020), with '
            'renumbered articles, is read from its own page (DetaliiDocumentAfis/245244); changes on that day that no '
            'note explains are credited to the act that ordered the republication, as the republication note says; '
            'files follow each text\'s own numbering.',
            'Legea nr. 24/2017: Legea nr. 158/2020 (read as published, DetaliiDocumentAfis/228486; Monitorul Oficial '
            'nr. 673 of 29 July 2020) is in force 30 days after publication, on 28 August 2020, save its art. I pct. '
            '46 as to arts. 91^3-91^5 and the provisions of pct. 53 sanctioning them, in force on 3 September 2020 '
            '(its art. XXVIII). The portal prints arts. 91^3, 91^4 and 91^5 from its form of 28 August 2020. Under '
            'the rule for text printed before its law, the three articles are absent until 3 September 2020, when a '
            'version adds them, credited to Legea nr. 158/2020. Pct. 53 rewrites art. 126 alin. (1) lit. a) pct. '
            '1-5 as a whole, its pct. 3 naming arts. 91^3-91^5 among many others; that wording stands from 28 August '
            '2020, the references to the three articles taking effect with them.',
            'Legea nr. 24/2017: the portal\'s notes give arts. 91^2 and 92^1, inserted by Legea nr. 158/2020 (art. I '
            'pct. 46 and 48) in the form of 28 August 2020, no note of their own; they are committed as the '
            'publisher\'s with the rest of that day\'s changes.',
            'Legea nr. 24/2017: the dates of the forms of 25 June, 5 July and 21 December 2024 follow OUG nr. 71/2024 '
            '(read as published, DetaliiDocumentAfis/284542; Monitorul Oficial nr. 591 of 25 June 2024), in force on '
            'publication save art. IV pct. 8-11, 13 and 14 (10 days after publication) and art. IV pct. 6, 7 and 12 '
            '(21 December 2024) (its art. XIV). The form of 16 January 2026 (Legea nr. 238/2025, in force 30 days '
            'after publication in Monitorul Oficial nr. 1171 of 17 December 2025) prints the changes its art. XIII '
            'puts in force 90 days after publication (art. IV pct. 11-15 and pct. 16 as to art. 108 alin. (13), from '
            '17 March 2026) only as the portal\'s notes, which are not text; no form of 17 March 2026 is held, so '
            'those changes are not in this record.',
        ],
        # Legea nr. 158/2020 art. XXVIII: in force 30 days after publication (28.08.2020), save art. I pct. 46 as to
        # arts. 91^3-91^5 (and the sanctions for them in pct. 53), from 3 September 2020; the form of 28.08.2020
        # prints them
        'later_provisions': (
            {'day': '2020-09-03', 'law': 'legea-158-2020', 'lines': (),
             'units': ('art-091-3', 'art-091-4', 'art-091-5'),
             'note': 'Arts. 91^3, 91^4 and 91^5, inserted by Legea nr. 158/2020 (art. I pct. 46), take effect on this '
                     'day (its art. XXVIII); the portal prints them from its form of 28.08.2020.'},
        ),
        'repeal_acts': {},
        'root_word': 'act page',
    }
    # as the portal's note links name it (the same entry part 99l-legea-297-2004 carries); dates read from the act as
    # published (DetaliiDocumentAfis/187788: "București, 21 martie 2017. Nr. 24.", MO nr. 213 din 29 martie 2017)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 24/2017', 'kind': 'law',
        'title': 'Legea nr. 24 din 21 martie 2017, publicată în Monitorul Oficial al României, Partea I, nr. 213 din 29 '
                 'martie 2017',
        'enacted': '2017-03-21', 'published': '2017-03-29', 'url': P.PORTAL + 'DetaliiDocument/187788',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
