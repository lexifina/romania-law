"""Legea nr. 61/1991 pentru sancționarea faptelor de încălcare a unor norme de conviețuire socială, a ordinii și liniștii
publice (Lexifina, 2026-11-02).

Act page 1534, also the text as published (DetaliiDocumentAfis/1534). 24 forms 24.01.1997 .. 13.06.2026 are listed
(forms.d/legea-61-1991.json); the form of 27.03.2026 (307796) is held by no archive, the others are held. Parsed as the
Phase 6 acts.
"""
SLUG = 'legea-61-1991'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-61-1991', 'short': 'Legea nr. 61/1991', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'root_word': 'act page',
        'title': 'Legea nr. 61/1991 pentru sancționarea faptelor de încălcare a unor norme de conviețuire socială, '
                 'a ordinii și liniștii publice',
        'url': P.PORTAL + 'DetaliiDocument/1534',
        'in_force': '1991-09-27', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 196 of 27 September 1991; it sets no day of its '
                     'own, so in force on publication (Constituția of 1991, art. 78, which applied until 29 October '
                     '2003).',
        'form_note': {
            '1535': 'The law as republished on 24 January 1997 under art. II of Legea nr. 132/1996.',
            '23832': 'The law as republished on 18 August 2000 under art. II of Legea nr. 2/2000.',
            '125693': 'The law as republished on 31 January 2011 under art. II of Legea nr. 153/2010.',
            '155343': 'The law as republished on 7 February 2014 under art. 248 of Legea nr. 187/2012.',
            '223135': 'The law as republished on 18 February 2020 under art. V of Legea nr. 192/2019.'},
        'republished': {'1535': 'legea-132-1996', '23832': 'legea-2-2000', '125693': 'legea-153-2010',
                        '155343': 'legea-187-2012', '223135': 'legea-192-2019'},
        'decisions': [
            'Legea nr. 61/1991: the first version is the law as published in Monitorul Oficial nr. 196 of 27 '
            'September 1991 (DetaliiDocumentAfis/1534), dated 27 September 1991: it sets no day of its own, so in '
            'force on publication (Constituția of 1991, art. 78, which applied until 29 October 2003). The portal '
            'holds no consolidated form before 24 January 1997, so the changes made up to then arrive together that '
            'day.',
            'Legea nr. 61/1991: the republication of 24 January 1997 (1535) is credited, for the changes no note '
            'explains, to Legea nr. 132/1996, under whose art. II it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 18 August 2000 (23832) is credited, for the changes no note '
            'explains, to Legea nr. 2/2000, under whose art. II it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 31 January 2011 (125693) is credited, for the changes no note '
            'explains, to Legea nr. 153/2010, under whose art. II it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 7 February 2014 (155343) is credited, for the changes no note '
            'explains, to Legea nr. 187/2012, under whose art. 248 it was republished, as its own note says.',
            'Legea nr. 61/1991: the republication of 18 February 2020 (223135) is credited, for the changes no note '
            'explains, to Legea nr. 192/2019, under whose art. V it was republished, as its own note says.',
            'Legea nr. 61/1991: the portal lists a form of 27 March 2026 (307796) that no archive holds; the act page '
            'captured in July 2026 shows the form of 13 June 2026. The record ends with that form, and the changes '
            'made on 27 March 2026 arrive together with those of 13 June 2026.',
        ],
        'repeal_acts': {},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {  # from the text as published (DetaliiDocumentAfis/1534)
        'label': 'Legea nr. 61/1991', 'kind': 'law',
        'title': 'Legea nr. 61/1991, publicată în Monitorul Oficial al României, Partea I, nr. 196 din 27 septembrie '
                 '1991',
        'enacted': '1991-09-27', 'published': '1991-09-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/1534',
    })
