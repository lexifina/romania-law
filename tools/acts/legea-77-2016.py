"""Legea nr. 77/2016 (giving property in payment of credit debts) (Lexifina, 2026-11-02).

Act page 178032 is also its base text (DetaliiDocumentAfis/178032); 4 consolidated forms (18.01.2017 .. 21.09.2021), all held from Common
Crawl (forms.d/legea-77-2016.json)."""

SLUG = 'legea-77-2016'
TITLE = ('Legea nr. 77/2016 privind darea în plată a unor bunuri imobile în vederea stingerii obligațiilor asumate prin credite')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-77-2016', 'short': 'Legea nr. 77/2016', 'pad': 3, 'cc_forms': True, 'trailing_notes': True, 'sign_tail': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/178032',
        'in_force': '2016-05-13', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 330 of 28 April 2016, in force 15 days after publication (its art. 12): 13 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 77/2016: the first version is the law as published in Monitorul Oficial nr. 330 of 28 April 2016 '
            '(DetaliiDocumentAfis/178032), dated 13 May 2016: in force 15 days after publication (its art. 12). The portal\'s consolidated forms start on 18 January 2017, so '
            'the changes made before that day arrive together with that form.',
            'Legea nr. 77/2016: the portal prints repeal and change notes just after the article they concern; they are read as '
            'that article\'s notes. The signature block printed after the last article is not part of the article.',
            'Legea nr. 77/2016: the portal prints, under arts. 3, 4, 5, 8 and 11, notes of Constitutional Court decisions '
            '(Decizia nr. 623/2016, MO nr. 53 of 18 January 2017, on a phrase of art. 11; Decizia nr. '
            '432/2021, MO nr. 905 of 21 September 2021, on the second and third sentences of art. 8 alin. (5)) and of decisions of the High Court '
            '(Decizie de respingere / de admitere, HP nr. ...). Its text of every article stays as published in all '
            'its forms, so no version is made for those decisions and the notes are not part of the article text. '
            'The only amendment is Legea nr. 52/2020 (Monitorul Oficial nr. 386 of 13 May 2020), in the form of 16 May 2020.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178032)
        'label': 'Legea nr. 77/2016', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 330 din 28 aprilie 2016',
        'enacted': '2016-04-28', 'published': '2016-04-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/178032',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
