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
        },
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
