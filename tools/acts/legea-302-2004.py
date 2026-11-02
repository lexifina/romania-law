"""Legea nr. 302/2004 privind cooperarea judiciară internațională în materie penală (Lexifina, 2026-11-02).

Act page 53158, also its base text (DetaliiDocumentAfis/53158); 17 forms 24.06.2006 .. 19.12.2025 listed
(forms.d/legea-302-2004.json), the newest (19.12.2025) held by no archive; the republications of 2011 and 2019 are read
from their own pages. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-302-2004'
UNITS = ([f'art-076-{n}' for n in range(1, 7)] + [f'art-{n:03d}' for n in range(77, 109)] + ['art-114-1'] +
         [f'art-187-{n}' for n in range(4, 19)])


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-302-2004', 'short': 'Legea nr. 302/2004', 'pad': 3, 'cc_forms': True,
        'trailing_notes': True, 'plain_ordonanta': True,
        'reprint_law': True,
        'title': 'Legea nr. 302/2004 privind cooperarea judiciară internațională în materie penală',
        'url': P.PORTAL + 'DetaliiDocument/53158',
        'in_force': '2004-08-30', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 594 of 1 July 2004, in force 60 days after '
                     'publication (its art. 189 alin. (1)): 30 August 2004.',
        'form_note': {'128922': 'The law as republished in Monitorul Oficial nr. 377 of 31 May 2011 under art. III of '
                                'Legea nr. 222/2008, with renumbered articles.',
                      '214172': 'The law as republished in Monitorul Oficial nr. 411 of 27 May 2019 under art. II of '
                                'Legea nr. 236/2017, with renumbered articles.'},
        'republished': {'128922': 'legea-222-2008', '214172': 'legea-236-2017'},
        'decisions': [
            'Legea nr. 302/2004: the first version is the law as published in Monitorul Oficial nr. 594 of 1 July '
            '2004 (DetaliiDocumentAfis/53158), in force 60 days after publication (its art. 189 alin. (1)): 30 August '
            '2004. The portal\'s first form is of 24 June 2006, so the changes made up to then arrive together that '
            'day.',
        ],
        # art. 189 alin. (1) (as Legea nr. 224/2006 restates it): ch. III^1 of title II (arts. 76^1-76^6), title III
        # (arts. 77-108), ch. II^1 of title IV (art. 114^1) and ch. II of title VII (arts. 187^4-187^18) take effect on
        # the day Romania joins the European Union, 1 January 2007; the forms print them from 24 June 2006
        'later_provisions': ({
            'day': '2007-01-01', 'law': 'legea-224-2006', 'lines': (), 'base_units': True,
            'units': tuple(UNITS), 'never': ('art-187-9',),
            'note': 'Ch. III^1 of title II, title III, ch. II^1 of title IV and ch. II of title VII take effect on '
                    'this day, the day Romania joins the European Union (art. 189 alin. (1)); the portal prints them '
                    'from its form of 24.06.2006 (title III as published in 2004).'},),
        'repeal_acts': {
            'legea-224-2006': {
                'label': 'Legea nr. 224/2006', 'page': '72813', 'capture': '20251109164015',
                'cc': {'crawl': 'CC-MAIN-2025-47', 'timestamp': '20251109164015',
                       'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439342726.15/warc/'
                                   'CC-MAIN-20251109151024-20251109181024-00885.warc.gz',
                       'offset': '293201422', 'length': '83298',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/72813'},
                'in_force': '2006-06-24',
                'why': 'it sets no in-force day of its own: 3 days after publication in Monitorul Oficial nr. 534 of '
                       '21 June 2006 (Constituția art. 78)',
                'read': 'art. I pct. 5 (art. 8), 6 (art. 9), 8 (art. 11), 15 (art. 19), 66 (art. 107), 87 (art. 126) '
                        'and 89 (art. 131): "Articolul ... se abrogă."; the form of 24.06.2006 leaves them out with no '
                        'note.',
                'repeals': {'73127': ('art-008', 'art-009', 'art-011', 'art-019', 'art-107', 'art-126', 'art-131')},
                'cite': 'Abrogat de LEGEA nr. 224 din 1 iunie 2006, publicată în MONITORUL OFICIAL nr. 534 din 21 '
                        'iunie 2006'},
            'oug-103-2006': {
                'label': 'OUG nr. 103/2006', 'page': '77941', 'capture': '20251115115521',
                'cc': {'crawl': 'CC-MAIN-2025-47', 'timestamp': '20251115115521',
                       'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439344061.37/warc/'
                                   'CC-MAIN-20251115105906-20251115135906-00892.warc.gz',
                       'offset': '283996679', 'length': '27108',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/77941'},
                'in_force': '2007-01-01',
                'why': 'its art. 27 takes effect on the day Romania joins the European Union, 1 January 2007',
                'read': 'art. 27: "La data aderării României la Uniunea Europeană, art. 187^9 din Legea nr. 302/2004 '
                        '... se abrogă."',
                'cite': 'Abrogat de ORDONANTA DE URGENTA nr. 103 din 13 decembrie 2006, publicata in MONITORUL '
                        'OFICIAL nr. 1.019 din 21 decembrie 2006'},
        },
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {  # read from the act as published (DetaliiDocumentAfis/53158)
        'label': 'Legea nr. 302/2004', 'kind': 'law',
        'title': 'Legea nr. 302 din 28 iunie 2004, publicată în Monitorul Oficial al României, Partea I, nr. 594 din '
                 '1 iulie 2004',
        'enacted': '2004-06-28', 'published': '2004-07-01', 'url': P.PORTAL + 'DetaliiDocumentAfis/53158',
    })
