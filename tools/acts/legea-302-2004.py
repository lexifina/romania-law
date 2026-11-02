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
        'typeset_notes': True,
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
            'Legea nr. 302/2004: the portal's list of forms ends with a form of 19 December 2025 (listed on the pages '
            'of the act captured in January 2026) that its pages as captured do not hold; the act page captured on 14 '
            'December 2025 shows the form of 19 October 2025 as the newest. The record ends with the form of 19 '
            'October 2025 and no repeal is made up.',
            'Legea nr. 302/2004: its art. 189 alin. (1) puts the provisions on the European arrest warrant (title III) '
            'in force on the day Romania joins the European Union, 1 January 2007; Legea nr. 224/2006 (Monitorul '
            'Oficial nr. 534 of 21 June 2006, read as published, DetaliiDocumentAfis/72813) restates that clause for '
            'title III and for the provisions it inserts, ch. III^1 of title II (arts. 76^1-76^6), ch. II^1 of title '
            'IV (art. 114^1) and ch. II of title VII (arts. 187^4-187^18). The portal prints all of them, title III '
            'as published in 2004 and then as changed by Legea nr. 224/2006, from the form of 24 June 2006 on. Under '
            'the rule for text printed before its day, none of these provisions is in the record before 1 January '
            '2007: the first version leaves title III out, the version of 24 June 2006 gives only the rest of the '
            'changes of Legea nr. 224/2006, and on 1 January 2007 a version adds them as the form of 24 June 2006 '
            'prints them, credited to Legea nr. 224/2006.',
            'Legea nr. 302/2004: art. 107, in title III, was repealed by Legea nr. 224/2006 (art. I pct. 66) before '
            'title III took effect, so it never appears in the record. Art. 187^9 (inserted by Legea nr. 224/2006, in '
            'ch. II of title VII) was repealed by art. 27 of OUG nr. 103/2006 (Monitorul Oficial nr. 1.019 of 21 '
            'December 2006, read as published, DetaliiDocumentAfis/77941) on the same day, 1 January 2007, the day '
            'Romania joined the European Union; it took effect and was repealed that day, so it never appears. The '
            'form of 13 November 2008 prints it as "Abrogat." with the portal's note.',
            'Legea nr. 302/2004: Legea nr. 224/2006 repealed arts. 8, 9, 11, 19, 107, 126 and 131 (art. I pct. 5, 6, '
            '8, 15, 66, 87 and 89). It sets no in-force day of its own, so it took effect 3 days after publication, on '
            '24 June 2006 (Constituția art. 78), the day of the portal's first form, which leaves them out with no '
            'note; the change is credited to Legea nr. 224/2006. The form of 13 November 2008 prints them again as '
            '"Abrogat.", which is the publisher's typesetting, not a change.',
            'Legea nr. 302/2004: the forms of 24 June 2006 and 13 November 2008 print the text without diacritics, '
            'and the form of 13 November 2008 reprints the earlier notes in new wording; a change that differs from '
            'the text before it only in diacritics or spacing is the publisher's typesetting and is credited to no '
            'law, whatever notes the form reprints. The same goes for the typing errors the forms of 27 December '
            '2015 and 17 December 2017 correct.',
            'Legea nr. 302/2004: the republications of 31 May 2011 (art. III of Legea nr. 222/2008) and 27 May 2019 '
            '(art. II of Legea nr. 236/2017), each with renumbered articles, are read from their own pages '
            '(DetaliiDocumentAfis/128922, 214172); changes on those days that no note explains are credited to the '
            'act that ordered the republication, as each republication note says; files follow each text's own '
            'numbering.',
            'Legea nr. 302/2004: the forms of 26 December 2013 to 27 December 2015 print the headings "PARAGRAFUL 2" '
            'and "PARAGRAFUL 3" and their titles as the last lines of arts. 223, 224, 234^1, 238, 252 and 257, and the '
            'forms of 31 May 2011 to 27 December 2015 print, after the last article, the "*" and the law's mention '
            'that it transposes framework decisions (from 2019 to 2024-05-10 the mention is printed without the "*"). '
            'Neither is an article's text, and both are left out.',
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
    P.EDITORIAL_LINES[SLUG] = {
        'art-223': ('PARAGRAFUL 2', 'Procedura de emitere și transmitere a ordinelor de indisponibilizare'),
        'art-224': ('PARAGRAFUL 3', 'Procedura de executare de către autoritățile române a ordinelor de '
                                    'indisponibilizare'),
        'art-234-1': ('PARAGRAFUL 2', 'Procedura de transmitere a hotărârii'),
        'art-238': ('PARAGRAFUL 3', 'Procedura de executare a hotărârii'),
        'art-252': ('PARAGRAFUL 2', 'Procedura de transmitere de către autoritățile române a ordinelor de confiscare '
                                    'și a certificatului'),
        'art-257': ('PARAGRAFUL 3', 'Procedura de executare de către autoritățile române a ordinelor de confiscare'),
    }
    # the "*" and the transposition mention printed at the end of the last article (art. 270 of the 2011 text, art. 271
    # from 2013; art. 355 of the 2019 text, without the "*")
    P.EDITORIAL_TAILS[SLUG] = {
        'art-270': '*', 'art-271': '*',
        'art-355': 'Prezenta lege transpune în legislația națională dispozițiile deciziilor-cadru ale Uniunii '
                   'Europene din domeniul cooperării judiciare în materie penală, după cum urmează:'}
