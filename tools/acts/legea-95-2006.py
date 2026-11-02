"""Legea nr. 95/2006 privind reforma în domeniul sănătății (Lexifina, 2026-11-02).

Base: DetaliiDocumentAfis/71139 (the law as published in Monitorul Oficial nr. 372 of 28 April 2006). 205 forms listed
2006-05-05 .. 2026-02-02 (forms.d/legea-95-2006.json), all held: 159 from Common Crawl, 45 from Internet Archive captures
(the portal's pages of the larger forms are cut short in Common Crawl), the republication of 28 August 2015 (170974)
from its DetaliiDocumentAfis page ('afis_cc'). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-95-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-95-2006', 'short': 'Legea nr. 95/2006', 'pad': 3, 'cc_forms': True,
        'revert_credit': True, 'range_bare': True,
        # the forms of 01.01.2008 to 26.11.2008 print, after art. 258 (and, in the first, art. 257), the wording it takes later
        'future_text': {'88591': {'arts': ('Articolul 257', 'Articolul 258')},
                        **{k: {'arts': ('Articolul 258',)} for k in ('95186', '95966', '99744', '99745')}},
        'title': 'Legea nr. 95/2006 privind reforma în domeniul sănătății',
        'url': P.PORTAL + 'DetaliiDocument/306816',
        'in_force': '2006-05-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 372 of 28 April 2006. Its art. 863 brings it into '
                     'force in stages: titles XI to XIV (and art. 704 alin. (2), art. 852) 3 days after publication, '
                     'that is on 1 May 2006, the rest later; this first version carries the whole text from the '
                     'first day.',
        'form_note': {'170974': 'The law as republished in Monitorul Oficial nr. 652 of 28 August 2015 under art. VI of '
                                'Legea nr. 184/2015, with renumbered articles.'},
        'republished': {'170974': 'legea-184-2015'},
        'repeal_acts': {
            SLUG: {  # the law's own art. 862, read as published
                'label': 'Legea nr. 95/2006', 'page': '71139', 'capture': '20260114191857',
                'cc': {'crawl': 'CC-MAIN-2026-04', 'timestamp': '20260114191857',
                       'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220469150.51/warc/'
                                   'CC-MAIN-20260114184901-20260114214901-00435.warc.gz',
                       'offset': '279210058', 'length': '443262',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/71139'},
                'in_force': '2007-01-01',
                'why': 'its art. 862: the provisions it names are repealed on the date of Romania\'s accession to the '
                       'European Union, 1 January 2007',
                'read': 'art. 862: "Următoarele prevederi ale prezentului titlu se abrogă la data aderării României la '
                        'Uniunea Europeană: - art. 700 alin. (2); - art. 730 alin. (3); - art. 733; - art. 735 alin. '
                        '(2); - art. 787 alin. (1)."; the form of 01.01.2007 leaves art. 733 out.',
                'repeals': {'78339': ('art-733',)},
                'cite': 'Art. 733 a fost abrogat de art. 862 din LEGEA nr. 95 din 14 aprilie 2006, publicată în '
                        'MONITORUL OFICIAL nr. 372 din 28 aprilie 2006'},
            'oug-162-2008': {
                'label': 'OUG nr. 162/2008', 'page': '99731', 'capture': '20260122143049',
                'cc': {'crawl': 'CC-MAIN-2026-04', 'timestamp': '20260122143049',
                       'filename': 'crawl-data/CC-MAIN-2026-04/segments/1768220470194.15/warc/'
                                   'CC-MAIN-20260122122206-20260122152206-00563.warc.gz',
                       'offset': '278592809', 'length': '23956',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/99731'},
                'in_force': '2009-01-01',
                'why': 'its art. 25: in force on 1 January 2009',
                'read': 'art. 26: "La data intrării în vigoare a prezentei ordonanțe de urgență se abrogă titlul V din '
                        'Legea nr. 95/2006 ..."; the form of 01.01.2009 leaves arts. 126-140 out.'},
            'legea-329-2009': {
                'label': 'Legea nr. 329/2009', 'page': '113152', 'capture': '20251208080845',
                'cc': {'crawl': 'CC-MAIN-2025-51', 'timestamp': '20251208080845',
                       'filename': 'crawl-data/CC-MAIN-2025-51/segments/1764871307298.13/warc/'
                                   'CC-MAIN-20251208061603-20251208091603-00629.warc.gz',
                       'offset': '282523200', 'length': '127140',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/113152'},
                'in_force': '2009-12-08',
                'why': 'its art. 68: the repeal takes effect when the Government decisions setting up the new bodies '
                       'take effect; for the Școala Națională de Sănătate Publică și Management Sanitar that is '
                       'HOTĂRÂREA nr. 1.421/2009 (DetaliiDocumentAfis/114247, capture 20260122141625), which has no '
                       'in-force clause of its own: in force on publication in Monitorul Oficial nr. 848 of 8 '
                       'December 2009',
                'read': 'art. 68 lit. k): "art. 682 , art. 683 alin. (1), (6)-(8) , art. 684-687 , art. 688 alin. '
                        '(1) teza a 2-a și alin. (3) , art. 689 , 690 și art. 692 alin. (1) din Legea nr. 95/2006"; the '
                        'portal\'s form of 12.11.2009 already leaves them out, with its note that the repeal takes '
                        'effect from the decisions.'},
            'oug-48-2010': {
                'label': 'OUG nr. 48/2010', 'page': '119434', 'capture': '20260207043335',
                'cc': {'crawl': 'CC-MAIN-2026-08', 'timestamp': '20260207043335',
                       'filename': 'crawl-data/CC-MAIN-2026-08/segments/1770395505692.68/warc/'
                                   'CC-MAIN-20260207032847-20260207062847-00198.warc.gz',
                       'offset': '255506516', 'length': '34559',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/119434'},
                'in_force': '2010-06-10',
                'why': 'an emergency ordinance with no in-force clause of its own: in force on publication in '
                       'Monitorul Oficial nr. 384 of 10 June 2010',
                'read': 'art. I pct. 42: "Articolul 202 se abrogă."; the form of 10.06.2010 leaves art. 202 out.'},
            'legea-45-2017': {
                'label': 'Legea nr. 45/2017', 'page': '187930', 'capture': '20260211100355',
                'cc': {'crawl': 'CC-MAIN-2026-08', 'timestamp': '20260211100355',
                       'filename': 'crawl-data/CC-MAIN-2026-08/segments/1770395506147.0/warc/'
                                   'CC-MAIN-20260211082311-20260211112311-00064.warc.gz',
                       'offset': '281579993', 'length': '11449',
                       'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/187930'},
                'in_force': '2017-04-07',
                'why': 'a law with no in-force clause of its own: in force 3 days after publication in Monitorul '
                       'Oficial nr. 229 of 4 April 2017 (Constituția art. 78)',
                'read': 'art. unic: approves OUG nr. 36/2016 "cu următoarea modificare: La articolul unic, punctul 1 se '
                        'abrogă" (the point that added art. 26^1); the form of 07.04.2017 leaves art. 26^1 out, with '
                        'the note that the law eliminated it.',
                'repeals': {'187410': ('art-026-1',)},
                'cite': 'Art. 26^1 a fost eliminat de ARTICOL UNIC din LEGEA nr. 45 din 3 aprilie 2017, publicată în '
                        'MONITORUL OFICIAL nr. 229 din 4 aprilie 2017'},
        },
        'later_repeal': True,
        'decisions': DECISIONS,
    }
    P.BASE_LAWS.update({
        SLUG: {  # read from the act as published (DetaliiDocumentAfis/71139)
            'label': 'Legea nr. 95/2006', 'kind': 'law',
            'title': 'Legea nr. 95/2006 privind reforma în domeniul sănătății, publicată în Monitorul Oficial al '
                     'României, Partea I, nr. 372 din 28 aprilie 2006',
            'enacted': '2006-04-14', 'published': '2006-04-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/71139',
        },
        'legea-184-2015': {  # read from the act as published (DetaliiDocumentAfis/169404)
            'label': 'Legea nr. 184/2015', 'kind': 'law',
            'title': 'Legea nr. 184/2015 pentru aprobarea Ordonanței de urgență a Guvernului nr. 77/2011 privind '
                     'stabilirea unor contribuții pentru finanțarea unor cheltuieli în domeniul sănătății, precum și '
                     'pentru modificarea și completarea Legii nr. 95/2006 privind reforma în domeniul sănătății, '
                     'publicată în Monitorul Oficial al României, Partea I, nr. 490 din 3 iulie 2015',
            'enacted': '2015-07-02', 'published': '2015-07-03', 'url': P.PORTAL + 'DetaliiDocumentAfis/169404',
        },
    })
    # the forms of 04.11.2014 and later print a note quoted from another act as lines after art. 11
    P.EDITORIAL_TAILS[SLUG] = {'art-011': 'NOTA CTCE:'}
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)


DECISIONS = [
    'Legea nr. 95/2006: the first version is the law as published in Monitorul Oficial nr. 372 of 28 April 2006 '
    '(DetaliiDocumentAfis/71139). Its art. 863 brings the titles into force in stages (3, 30 and 90 days after '
    'publication, the date of Romania\'s accession to the European Union, and later days); the first version carries '
    'the whole text from 1 May 2006, the day the first titles took effect.',
    'Legea nr. 95/2006: the text republished in Monitorul Oficial nr. 652 of 28 August 2015 under art. VI of Legea '
    'nr. 184/2015 (enacted 2 July 2015, published in Monitorul Oficial nr. 490 of 3 July 2015), with renumbered '
    'articles, is read from its own page (DetaliiDocumentAfis/170974). Changes on that day that no note explains are '
    'credited to Legea nr. 184/2015, as the republication note says; files follow each text\'s own numbering, so many '
    'change that day.',
]
