"""Legea nr. 84/1998 privind mărcile și indicațiile geografice (Lexifina, 2026-11-02).

Act page 119052 (also the republication of 2010). 12 forms 28.12.2005 .. 07.03.2024 listed by DetaliiDocumentAfis/119052
as captured on 2026-01-18, all held (forms.d/legea-84-1998.json). The portal holds no text as first published, so the
record starts at its oldest form (no_base).
"""
SLUG = 'legea-84-1998'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'legea-66-2010': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/117786',
                      'timestamp': '20220812183716', 'crawl': 'CC-MAIN-2022-33',
                      'filename': 'crawl-data/CC-MAIN-2022-33/segments/1659882571745.28/warc/'
                                  'CC-MAIN-20220812170436-20220812200436-00256.warc.gz',
                      'offset': '327169889', 'length': '29980', 'digest': 'IMC7I2GUOIHFLWQ5A6H4XTC2AX5UVBMA'},
}


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-84-1998', 'short': 'Legea nr. 84/1998', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 84/1998 privind mărcile și indicațiile geografice',
        'url': P.PORTAL + 'DetaliiDocument/119052',
        'no_base': True, 'in_force': '2005-12-28', 'first_law': None, 'revert_credit': True,
        'earlier_laws': [SLUG],
        'base_note': 'Oldest version available: the portal\'s consolidated form of 28 December 2005. The law was '
                     'enacted on 15 April 1998 and first published in Monitorul Oficial nr. 161 of 23 April 1998; that '
                     'text is not held.',
        'form_note': {'119052': 'The law as republished in Monitorul Oficial nr. 350 of 27 May 2010 under art. V of '
                                'Legea nr. 66/2010, with renumbered articles.',
                      '158000': 'The law as republished in Monitorul Oficial nr. 337 of 8 May 2014 under art. 248 of '
                                'Legea nr. 187/2012, with renumbered articles.',
                      '230312': 'The law as republished in Monitorul Oficial nr. 856 of 18 September 2020 under art. IV '
                                'of Legea nr. 112/2020, with renumbered articles.'},
        'republished': {'119052': 'legea-66-2010', '158000': 'legea-187-2012', '230312': 'legea-112-2020'},
        'repeal_acts': {
            'legea-66-2010': {
                'label': 'Legea nr. 66/2010', 'page': '117786', 'capture': CC['legea-66-2010']['timestamp'],
                'cc': CC['legea-66-2010'], 'in_force': '2010-05-09',
                'why': 'its art. IV alin. (1): in force 30 days after publication in Monitorul Oficial nr. 226 of 9 '
                       'April 2010',
                'read': 'art. I pct. 2: "Articolul 2 se abrogă."; pct. 10: "Articolul 7 se abrogă."; pct. 16: '
                        '"Articolul 18 se abrogă."; pct. 21: "Articolele 23-25 se abrogă."; pct. 37: "Articolele 46 '
                        'și 47 se abrogă."; pct. 61: "Articolele 86-88 se abrogă."; art. V orders the republication.'},
        },
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS.setdefault(SLUG, {  # from the heading of the republication of 2010 (DetaliiDocumentAfis/119052)
        'label': 'Legea nr. 84/1998', 'kind': 'law',
        'title': 'Legea nr. 84/1998 privind mărcile și indicațiile geografice, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 161 din 23 aprilie 1998',
        'enacted': '1998-04-15', 'published': '1998-04-23', 'url': None,
    })
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
