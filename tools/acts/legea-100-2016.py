"""Legea nr. 100/2016 privind concesiunile de lucrări și concesiunile de servicii (Lexifina, 2026-11-02).

Act page 178689 is also its base text (DetaliiDocumentAfis/178689); no republication; 12 forms, all held from Common
Crawl. forms.d/legea-100-2016.json.
"""
SLUG = 'legea-100-2016'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-100-2016', 'short': 'Legea nr. 100/2016', 'pad': 3, 'titles': False,
        'trailing_notes': True, 'cc_forms': True,
        # the value threshold (art. 11 alin. (1)): the portal rewrote it in its then-newest form from 1 January of the
        # year its editorial note gives (EU delegated regulations), so it is dated that day
        'editorial_days': {
            '222869': {'art-011': '2020-01-01'},  # Regulamentul delegat (UE) 2019/1827
            '245518': {'art-011': '2022-01-01'},  # Regulamentele delegate 2021/1950-1953
            '259945': {'art-011': '2024-01-01'},  # 2023/2495-2497, 2023/2510
        },
        'title': 'Legea nr. 100/2016 privind concesiunile de lucrări și concesiunile de servicii',
        'url': P.PORTAL + 'DetaliiDocument/178689',
        'in_force': '2016-05-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 392 of 23 May 2016; it sets no day of its own, so '
                     'in force 3 days after publication (Constituția art. 78): 26 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 100/2016: the first version is the law as published in Monitorul Oficial nr. 392 of 23 May 2016 '
            '(DetaliiDocumentAfis/178689), dated 26 May 2016: it sets no in-force day of its own, so 3 days after '
            'publication (Constituția art. 78). The portal holds no consolidated form before 7 December 2016, so the '
            'changes made up to then arrive together that day.',
            'Legea nr. 100/2016: the value threshold of art. 11 alin. (1) is not amended by a Romanian act: the portal '
            'rewrites the amount when EU delegated regulations change it, with an editorial note giving the new amount '
            'and the day it applies from (1 January 2020, 2022 and 2024). Those changes are dated by the editorial '
            'note, the earlier amount standing until then: 1 January 2020 (form of 12.02.2020), 1 January 2022 (form '
            'of 30.08.2021) and 1 January 2024 (form of 06.10.2022). No note names a law for them, so they are the '
            'publisher\'s. The form of 17.11.2024 carries a note for a further change from 1 January 2026 but prints '
            'the unchanged amount, so no change is made for it.',
            'Legea nr. 100/2016: the form of 12 February 2020 loses the space in art. 10 ("și nr. 1.107/70" printed '
            'as "șinr."); no note explains it. This change is the publisher\'s, labelled unexplained.',
            'Legea nr. 100/2016: the portal prints some repeal notes just after the article they concern; they are read '
            'as that article\'s notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178689)
        'label': 'Legea nr. 100/2016', 'kind': 'law',
        'title': 'Legea nr. 100/2016 privind concesiunile de lucrări și concesiunile de servicii, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 392 din 23 mai 2016',
        'enacted': '2016-05-19', 'published': '2016-05-23', 'url': P.PORTAL + 'DetaliiDocumentAfis/178689',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
