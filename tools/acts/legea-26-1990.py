"""Legea nr. 26/1990 privind registrul comerțului (Lexifina, 2026-11-02).

Act page 785, also the 1998 republication (its text as printed: DetaliiDocumentAfis/785); base text
DetaliiDocumentAfis/783; 23 consolidated forms 14.06.2002 .. 26.09.2020, all held from Common Crawl
(forms.d/legea-26-1990.json, listed from DetaliiDocumentAfis/785's capture). Parsed as the Phase 6 acts. Repealed in
full by Legea nr. 265/2022 (acts/legea-265-2022.py) from 26 November 2022 (act_repeal).
"""
SLUG = 'legea-26-1990'

# acts read as published (Common Crawl captures of their DetaliiDocumentAfis pages)
CC = {
    'legea-348-2001': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/29502',
                       'timestamp': '20251112122814', 'crawl': 'CC-MAIN-2025-47',
                       'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439343239.12/warc/'
                                   'CC-MAIN-20251112100515-20251112130515-00902.warc.gz',
                       'offset': '288886158', 'length': '12402', 'digest': 'HVOPL4Q7UVHZ3HZQA4I5HTWX7V4TCN5W'},
    'oug-129-2002': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/38865',
                     'timestamp': '20251215025743', 'crawl': 'CC-MAIN-2025-51',
                     'filename': 'crawl-data/CC-MAIN-2025-51/segments/1764871645602.73/warc/'
                                 'CC-MAIN-20251215005813-20251215035813-00704.warc.gz',
                     'offset': '280808812', 'length': '18048', 'digest': 'YNRQ7GTFGBWMIQSDVL4MYTFPPVWUTIZD'},
    'legea-161-2003': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/43323',
                       'timestamp': '20251118020051', 'crawl': 'CC-MAIN-2025-47',
                       'filename': 'crawl-data/CC-MAIN-2025-47/segments/1762439649042.63/warc/'
                                   'CC-MAIN-20251118000149-20251118030149-00339.warc.gz',
                       'offset': '298059980', 'length': '221320', 'digest': 'HS4TZI7LBHVYDL77EDF3G2TBTT4SP63Y'},
    'legea-265-2022': {'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/257835',
                       'timestamp': '20260218001254', 'crawl': 'CC-MAIN-2026-08',
                       'filename': 'crawl-data/CC-MAIN-2026-08/segments/1770395863965.96/warc/'
                                   'CC-MAIN-20260217225554-20260218015554-00696.warc.gz',
                       'offset': '277016138', 'length': '106683', 'digest': 'C2DONCZ6DQ4CQ43QY5452IVYI4N54DQM'},
}
# Legea nr. 12/1998, read as published: DetaliiDocumentAfis/14026, Common Crawl CC-MAIN-2026-04 20260116061723


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-26-1990', 'short': 'Legea nr. 26/1990', 'pad': 3, 'cc_forms': True,
        # quoted terms printed as "<<...>>" or " lt; lt;... gt; gt;"; older notes spell "ORDONANTA" without diacritics
        'angle_quotes': True, 'plain_ordonanta': True,
        'title': 'Legea nr. 26/1990 privind registrul comerțului',
        'url': P.PORTAL + 'DetaliiDocument/785',
        'in_force': '1990-12-07', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 121 of 7 November 1990, in force 30 days after '
                     'publication (its art. 51): 7 December 1990.',
        'form_note': {'785': 'The law as republished in Monitorul Oficial nr. 49 of 4 February 1998 under art. IV of '
                             'Legea nr. 12/1998, with renumbered articles; dated 18 February 1998, the day Legea nr. '
                             '12/1998 took effect (its art. 3: 30 days after publication in Monitorul Oficial nr. 15 of '
                             '19 January 1998).'},
        'republished': {'785': 'legea-12-1998'},
        # the republication of 04.02.1998 prints the changes of Legea nr. 12/1998, in force 30 days after its
        # publication of 19.01.1998 (its art. 3)
        'form_day': {'785': '1998-02-18'},
        'repeal_acts': {
            'legea-348-2001': {
                'label': 'Legea nr. 348/2001', 'page': '29502', 'capture': CC['legea-348-2001']['timestamp'],
                'cc': CC['legea-348-2001'], 'in_force': '2001-07-12',
                'why': 'no in-force clause of its own: in force on publication in Monitorul Oficial nr. 381 of 12 July '
                       '2001 (Constituția of 1991, art. 78)',
                'read': 'art. I pct. 2: "Articolul 52 se abroga."'},
            'oug-129-2002': {
                'label': 'OUG nr. 129/2002', 'page': '38865', 'capture': CC['oug-129-2002']['timestamp'],
                'cc': CC['oug-129-2002'], 'in_force': '2002-10-11',
                'why': 'no in-force clause of its own: in force on publication in Monitorul Oficial nr. 746 of 11 '
                       'October 2002',
                'read': 'art. I pct. 8: "Articolul 49 se abroga."'},
            'legea-161-2003': {
                'label': 'Legea nr. 161/2003', 'page': '43323', 'capture': CC['legea-161-2003']['timestamp'],
                'cc': CC['legea-161-2003'], 'in_force': '2003-04-21',
                'why': 'book II, title II (art. VIII) has no in-force clause of its own (only book I titles II and '
                       'V do, arts. 33 and 238): in force on publication in Monitorul Oficial nr. 279 of 21 April 2003 '
                       '(Constituția of 1991, art. 78)',
                'read': 'book II, title II, art. VIII pct. 25: "Articolul 27 se abroga."'},
        },
        # the whole law repealed after its newest form (26.09.2020), read from the repealing act
        'act_repeal': {
            'law': 'legea-265-2022', 'day': '2022-11-26', 'page': '257835',
            'capture': CC['legea-265-2022']['timestamp'], 'cc': CC['legea-265-2022'],
            'note': 'Legea nr. 26/1990 repealed in full by art. 140 alin. (1) lit. a) of Legea nr. 265/2022 privind '
                    'registrul comerțului (Monitorul Oficial nr. 750 of 26 July 2022), on the day that law took '
                    'effect, 4 months after its publication (its art. 141 alin. (1)): 26 November 2022.'},
        'decisions': [
            'Legea nr. 26/1990: the first version is the law as published in Monitorul Oficial nr. 121 of 7 November '
            '1990 (enacted 5 November 1990; DetaliiDocumentAfis/783), in force 30 days after publication (its art. '
            '51): 7 December 1990.',
            'Legea nr. 26/1990: the next version is the text republished in Monitorul Oficial nr. 49 of 4 February '
            '1998 under art. IV of Legea nr. 12/1998, with renumbered articles, read from its own page '
            '(DetaliiDocumentAfis/785). Legea nr. 12/1998 (enacted 8 January 1998, published in Monitorul Oficial nr. '
            '15 of 19 January 1998; read as published, DetaliiDocumentAfis/14026) takes effect 30 days after '
            'publication (its art. 3), and the republished text prints its changes (the republication\'s own note '
            'lists the amended provisions as in force from that day), so the republished text is dated 18 February '
            '1998: the act as published wins over the day of the republication. Changes on that day are credited to '
            'Legea nr. 12/1998, which ordered the republication; files follow each text\'s own numbering.',
            'Legea nr. 26/1990: the portal holds no consolidated form between the republication of 1998 and the form '
            'of 14 June 2002, so the changes made in those years arrive with that form (save the repeal of art. 52, '
            'dated by its act).',
            'Legea nr. 26/1990: the acts that repealed arts. 52 (Legea nr. 348/2001), 49 (OUG nr. 129/2002) and 27 '
            '(Legea nr. 161/2003, book II, title II) were read as published (DetaliiDocumentAfis/29502, 38865, 43323). '
            'None sets an in-force day for those provisions, and before the revision of 2003 the Constitution '
            '(art. 78 of the 1991 text) put a law in force on its publication, so each repeal is dated by the day '
            'of publication, the day the portal\'s own notes give.',
            'Legea nr. 26/1990: the form of 21 April 2003 prints, after art. 53, art. III of OUG nr. 129/2002 (the '
            'transfer of the trade registry staff), introduced by a portal note ("Conform art. III ..."); it is not '
            'this law\'s text and is left out.',
            'Legea nr. 26/1990: the forms of 2003-2017 print the quotation marks of quoted terms in arts. 31 and 39 as '
            '"<<asociație familială>>" (which an HTML reader takes for a tag, losing the words) or as "lt; '
            'lt;asociație familială gt; gt;"; both are read as quoted terms („asociație familială”), so that no words '
            'are lost. Older notes spell "ORDONANTA" without diacritics; they are read as naming the ordinance.',
            'Legea nr. 26/1990: repealed in full by art. 140 alin. (1) lit. a) of Legea nr. 265/2022 privind '
            'registrul comerțului (enacted 22 July 2022, published in Monitorul Oficial nr. 750 of 26 July 2022), '
            'read as published (DetaliiDocumentAfis/257835), from the day that law took effect, 4 months after its '
            'publication (its art. 141 alin. (1)): 26 November 2022. The record ends with a version that removes '
            'every article, credited to Legea nr. 265/2022 (legea-265-2022/). The portal lists no form of Legea nr. '
            '26/1990 after that of 26 September 2020, so any amendment between that day and the repeal is missing.',
        ],
    }
    # the form of 21.04.2003 prints, after art. 53, art. III of OUG nr. 129/2002 (staff transfer), which a portal note
    # introduces ("Conform art. III ..."): not this law's text
    P.EDITORIAL_LINES[SLUG] = {
        'art-053': ('"Art. III', 'Personalul actual al Oficiului Național al Registrului Comerțului de pe lângă Camera'),
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/783, Common Crawl 20251208064615)
        'label': 'Legea nr. 26/1990', 'kind': 'law',
        'title': 'Legea nr. 26/1990 privind registrul comerțului, publicată în Monitorul Oficial al României, Partea I, '
                 'nr. 121 din 7 noiembrie 1990',
        'enacted': '1990-11-05', 'published': '1990-11-07', 'url': P.PORTAL + 'DetaliiDocumentAfis/783',
    }
    P.BASE_LAWS['legea-12-1998'] = {  # read from the act as published (DetaliiDocumentAfis/14026)
        'label': 'Legea nr. 12/1998', 'kind': 'law',
        'title': 'Legea nr. 12 din 8 ianuarie 1998, publicată în Monitorul Oficial al României, Partea I, nr. 15 din 19 '
                 'ianuarie 1998',
        'enacted': '1998-01-08', 'published': '1998-01-19', 'url': P.PORTAL + 'DetaliiDocument/14026',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
