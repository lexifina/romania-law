"""Legea nr. 51/1991 privind securitatea națională a României (Lexifina, 2026-11-02).

Act page 1517 is also its base text (DetaliiDocumentAfis/1517, Monitorul Oficial nr. 163 of 7 August 1991); 9
consolidated forms (2014-02-01 .. 2023-03-18) incl. the 2014 republication 156439. forms.d/legea-51-1991.json.
"""
SLUG = 'legea-51-1991'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-51-1991', 'short': 'Legea nr. 51/1991', 'pad': 3, 'titles': False,
        'cc_forms': True,
        'title': 'Legea nr. 51/1991 privind securitatea națională a României',
        'url': P.PORTAL + 'DetaliiDocument/1517',
        'in_force': '1991-08-07', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 163 of 7 August 1991 (then titled "privind '
                     'siguranța națională a României"); it sets no day of its own, so in force on publication.',
        'form_note': {'156439': 'The law as republished in Monitorul Oficial nr. 190 of 18 March 2014 under art. 107 '
                                'alin. (3) of Legea nr. 255/2013, with renumbered articles.'},
        'republished': {'156439': 'legea-255-2013'},
        'decisions': [
            'Legea nr. 51/1991: the first version is the law as published in Monitorul Oficial nr. 163 of 7 August '
            '1991 (DetaliiDocumentAfis/1517), dated that day: the law sets no day of its own (its art. 29 refers only '
            'to "data intrării în vigoare"), so it took effect on publication.',
            'Legea nr. 51/1991: the portal holds no consolidated form before 1 February 2014, so the changes made '
            'between the law as published and that form arrive together that day.',
            'Legea nr. 51/1991: the law as republished in Monitorul Oficial nr. 190 of 18 March 2014 (art. 107 '
            'alin. (3) of Legea nr. 255/2013; enacted 19 July 2013, published in Monitorul Oficial nr. 515 of 14 '
            'August 2013), with renumbered articles, is read from its own page (DetaliiDocumentAfis/156439); changes on '
            'that day that no note explains are credited to Legea nr. 255/2013, as the republication note says.',
            'Legea nr. 51/1991: the form of 1 February 2014 replaces "siguranța națională" by "securitatea națională" '
            'throughout and carries a note that Legea nr. 255/2013 (art. 29 pct. 1) changed the law\'s title; no note '
            'names the law for the replacement in the articles themselves, so those changes (and the form\'s '
            'spelling changes, for example "forta" / "forță") are the publisher\'s, labelled unexplained.',
            'Legea nr. 51/1991: from the form of 20 April 2018 the portal adds editorial notes to art. 3 lit. f): '
            'Decizia Curții Constituționale nr. 91/2018 (Monitorul Oficial nr. 348 of 20 April 2018) finds the words '
            '"aduc atingere gravă drepturilor și libertăților fundamentale ale cetățenilor români" unconstitutional '
            'and Decizia nr. 802/2018 (Monitorul Oficial nr. 218 of 20 March 2019) the words "ori altor asemenea '
            'interese ale țării"; the notes say the provisions were suspended and ceased to have legal effect on 4 '
            'June 2018 and 4 May 2019 (Constituția art. 147 alin. (1)). The portal keeps printing both phrases in the '
            'text of every later form, with only the notes added, so the text of art. 3 lit. f) is not changed on '
            'either day; no text the portal does not print is made up, and the forms of 20 April 2018, 4 June 2018, '
            '20 March 2019 and 4 May 2019 are unchanged versions. The notes are kept out of the article text, as '
            'for other editorial notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the law as published (DetaliiDocumentAfis/1517)
        'label': 'Legea nr. 51/1991', 'kind': 'law',
        'title': 'Legea nr. 51/1991 privind siguranța națională a României, publicată în Monitorul Oficial al '
                 'României nr. 163 din 7 august 1991',
        'enacted': '1991-07-29', 'published': '1991-08-07', 'url': P.PORTAL + 'DetaliiDocumentAfis/1517',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
