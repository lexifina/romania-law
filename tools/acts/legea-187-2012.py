"""Legea nr. 187/2012 pentru punerea în aplicare a Legii nr. 286/2009 privind Codul penal (Lexifina, 2026-11-02).

Act page 142722 is also its base text (DetaliiDocumentAfis/142722); no republication; 6 forms 25.10.2013 .. 09.07.2023,
all held from Common Crawl (forms listed by the act page's capture 20250912203749). forms.d/legea-187-2012.json.
Its articles that amend other acts quote the text they insert or rewrite; that text stays inside the amending article
('quoted_articles', 'quoted_lines', 'quoted_siblings'). The law key 'legea-187-2012' is the one other parts already
credit from the portal's notes; this module adds the same entry to BASE_LAWS (same fields, same order), so they parse
byte-identical.
"""
SLUG = 'legea-187-2012'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-187-2012', 'short': 'Legea nr. 187/2012', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'quoted_lines': True, 'quoted_siblings': True, 'trailing_notes': True,
        'reprint_law': True, 'rect_after': True, 'plain_ordonanta': True,
        'title': 'Legea nr. 187/2012 pentru punerea în aplicare a Legii nr. 286/2009 privind Codul penal',
        'url': P.PORTAL + 'DetaliiDocument/142722',
        'in_force': '2014-02-01', 'first_law': SLUG,
        # art. 247: art. 247 itself, art. 121 pct. 8 and art. 249 in force 3 days after publication (Monitorul
        # Oficial nr. 757 of 12 November 2012)
        'early_units': {
            'day': '2012-11-15',
            'arts': {'art-247': None, 'art-249': None,
                     'art-121': (('Ordonanța de urgență a Guvernului nr. 195/2002', '1. '), ('8. ', '9. '))},
            'note': 'The provisions in force 3 days after the law was published in Monitorul Oficial nr. 757 of 12 '
                    'November 2012, as its art. 247 provides: art. 247 itself, art. 121 pct. 8 (with the opening words '
                    'of art. 121) and art. 249. The rest of the law takes effect with the Penal Code, on 1 February '
                    '2014.',
        },
        'base_note': 'The rest of the law as published in Monitorul Oficial nr. 757 of 12 November 2012, in force with '
                     'the Penal Code on 1 February 2014 (its art. 247).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 187/2012: the law as published in Monitorul Oficial nr. 757 of 12 November 2012 '
            '(DetaliiDocumentAfis/142722). Its art. 247 puts it in force on 1 February 2014, with the Penal Code, '
            'except art. 247 itself, art. 121 pct. 8 and art. 249, in force 3 days after publication. So the first '
            'version, of 15 November 2012, holds only those provisions (art. 121 with its opening words and pct. 8 '
            'alone); on 1 February 2014 the rest of the law as published is added, credited to Legea nr. 187/2012, '
            'and the same day the portal\'s form of 01.02.2014 gives the text in force.',
            'Legea nr. 187/2012: the portal\'s form of 25 October 2013 comes before the day the law took effect save '
            'its early provisions, and is not used; its changes (the rectification of art. 111 and typesetting, one '
            'of them in art. 249) arrive with the form of 1 February 2014. It also prints art. 175 as repealed by '
            'OUG nr. 91/2013; the form of 1 February 2014 prints art. 175 again in full, so no repeal is recorded.',
            'Legea nr. 187/2012: most of its articles amend other acts and quote the text they insert or rewrite. The '
            'quoted text is kept inside the amending article, as printed, and is not filed as articles of this law; '
            'paragraphs the law as published prints as "Art. N" inside an article stay text of that article. In '
            'later forms the portal rewrites some quoted text as the amended act changed and adds a note naming '
            'that act (forms of 12.01.2015 and 30.03.2018); such a change is credited from the note: an undated note '
            'takes the date of the form that first prints it.',
        ],
        'repeal_acts': {},
    }
    # the entry the portal's note links give (other parts carry it), read from Legea nr. 187/2012's heading
    P.BASE_LAWS.setdefault(SLUG, {
        'label': 'Legea nr. 187/2012',
        'title': 'Legea nr. 187 din 24 octombrie 2012, publicată în Monitorul Oficial al României, Partea I, nr. 757 din '
                 '12 noiembrie 2012',
        'kind': 'law', 'enacted': '2012-10-24', 'published': '2012-11-12',
        'url': P.PORTAL + 'DetaliiDocument/142722',
    })
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
