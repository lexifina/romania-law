"""Legea nr. 140/2022 privind unele măsuri de ocrotire pentru persoanele cu dizabilități intelectuale și psihosociale
(Lexifina, 2026-11-02).

Act page 255575, also its base text (DetaliiDocumentAfis/255575); the portal lists no consolidated form of it
(forms.d/legea-140-2022.json). Its art. 26 alin. (1) puts it in force 90 days after publication, save art. 20 alin. (6)
teza a III-a and art. 23, in force 3 days after publication.
"""
SLUG = 'legea-140-2022'
TITLE = ('Legea nr. 140/2022 privind unele măsuri de ocrotire pentru persoanele cu dizabilități intelectuale și '
         'psihosociale și modificarea și completarea unor acte normative')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-140-2022', 'short': 'Legea nr. 140/2022', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'quoted_heads': True,
        'titles': False, 'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/255575',
        'in_force': '2022-08-18', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 500 of 20 May 2022, in force 90 days after '
                     'publication (its art. 26 alin. (1)): 18 August 2022.',
        'form_note': {}, 'republished': {},
        # art. 26 alin. (1): art. 20 alin. (6) teza a III-a and art. 23 three days after publication (23 May 2022)
        'early_units': {
            'day': '2022-05-23',
            'arts': {'art-020': (('(6) ', None, 'În scopul reexaminării'),), 'art-023': None},
            'note': 'The provisions in force 3 days after the law was published in Monitorul Oficial nr. 500 of 20 '
                    'May 2022, as its art. 26 alin. (1) provides: art. 20 alin. (6) teza a III-a and art. 23. The rest '
                    'of the law takes effect 90 days after publication, on 18 August 2022.',
        },
        'decisions': [
            'Legea nr. 140/2022: the law as published in Monitorul Oficial nr. 500 of 20 May 2022 '
            '(DetaliiDocumentAfis/255575). Its art. 26 alin. (1) puts it in force 90 days after publication, on 18 '
            'August 2022, except art. 20 alin. (6) teza a III-a and art. 23, in force 3 days after publication, on 23 '
            'May 2022. So the first version, of 23 May 2022, holds only those provisions (of art. 20 alin. (6), the '
            'third sentence, under the alineat number); on 18 August 2022 the rest of the law as published is added, '
            'credited to Legea nr. 140/2022. The portal lists no consolidated form of it, so the text as published is '
            'the only text.',
            'Legea nr. 140/2022: art. 26 alin. (2) puts art. 118 alin. (2) and art. 170 alin. (3) of the Civil Code, '
            'as the law regulates or amends them, in force on a day the special law on the personal representative '
            'will set. The law sets no such day itself, so the two provisions stay in the text of the amending article as '
            'published and no version is made for them.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 140/2022', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 500 din 20 mai 2022',
        'enacted': '2022-05-17', 'published': '2022-05-20', 'url': P.PORTAL + 'DetaliiDocumentAfis/255575',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
