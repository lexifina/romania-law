"""Legea nr. 71/2011 pentru punerea în aplicare a Legii nr. 287/2009 privind Codul civil (Lexifina, 2026-11-02).

Act page 129268 is also its base text (DetaliiDocumentAfis/129268); no republication; 12 forms, all held from Common
Crawl (forms listed by the act page's capture 20251017111911). forms.d/legea-71-2011.json.
Its articles that amend other acts quote the text they insert or rewrite: that text stays inside the amending article
('quoted_articles'). The law key 'legea-71-2011' is the one the Civil Code part already credits (BASE_LAWS, unchanged).
"""
SLUG = 'legea-71-2011'
EARLY = ('art-214', 'art-216', 'art-217', 'art-218', 'art-224', 'art-225', 'art-226', 'art-228')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-71-2011', 'short': 'Legea nr. 71/2011', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'trailing_notes': True, 'reprint_law': True,
        'title': 'Legea nr. 71/2011 pentru punerea în aplicare a Legii nr. 287/2009 privind Codul civil',
        'url': P.PORTAL + 'DetaliiDocument/129268',
        'in_force': '2011-10-01', 'first_law': SLUG,
        # art. 221: arts. 214, 216-218, 224, art. 225 alin. (1) and (2), arts. 226 and 228 in force 3 days after
        # publication (Monitorul Oficial nr. 409 of 10 June 2011): 13 June 2011; the rest with the Civil Code
        'early_units': {
            'day': '2011-06-13',
            'arts': {**{k: None for k in EARLY}, 'art-225': (('(1) ', '(3) '),)},
            'note': 'The provisions in force 3 days after the law was published in Monitorul Oficial nr. 409 of 10 '
                    'June 2011, as its art. 221 provides: arts. 214, 216-218, 224, art. 225 alin. (1) and (2), arts. '
                    '226 and 228. The rest of the law takes effect with the Civil Code, on 1 October 2011.',
        },
        'base_note': 'The rest of the law as published in Monitorul Oficial nr. 409 of 10 June 2011, in force with the '
                     'Civil Code on 1 October 2011 (its arts. 220 alin. (1) and 221).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 71/2011: the law as published in Monitorul Oficial nr. 409 of 10 June 2011 '
            '(DetaliiDocumentAfis/129268). Its art. 221 puts it in force with the Civil Code, on 1 October 2011 (art. '
            '220 alin. (1)), except arts. 214, 216-218, 224, art. 225 alin. (1) and (2), arts. 226 and 228, in force 3 '
            'days after publication. So the first version, of 13 June 2011, holds only those provisions; on 1 October '
            '2011 the rest of the law as published is added, credited to Legea nr. 71/2011.',
            'Legea nr. 71/2011: the portal\'s form of 8 July 2011 comes before the day the law took effect save its '
            'early provisions, and changes none of them: it prints the corrections of RECTIFICAREA published in '
            'Monitorul Oficial nr. 489 of 8 July 2011 to arts. 20, 83, 99, 190 and 212. It is not used; those '
            'corrections arrive with the form of 1 October 2011, credited to that rectification from its notes.',
            'Legea nr. 71/2011: most of its articles amend other acts and quote the text they insert or rewrite '
            '("Articolul 1 va avea următorul cuprins: ..."). The quoted text is kept inside the amending article, as '
            'printed, and is not filed as articles of this law. In later forms the portal rewrites some quoted text '
            'as the amended act changed (art. 90, art. 5 of Legea nr. 341/2004, by OUG nr. 95/2014) and adds a note '
            'naming that act; such a change is credited from the note when the note dates it after the form before, '
            'and is otherwise the publisher\'s.',
            'Legea nr. 71/2011: the form of 4 February 2016 reprints the quoted articles in the portal\'s newer layout '
            '("Articolul 1" for "ART. 1", without the quotation marks) and with the later wording of some amended '
            'acts, and several forms of 2013-2014 move line breaks around the names of other acts; no note covers '
            'these changes, so they are the publisher\'s, labelled unexplained.',
            'Legea nr. 71/2011: a note the portal reprints with new spelling ("Denumirea marginala" / "marginală", art. '
            '83, form of 19 October 2014) is not a new note, so the typesetting change printed with it is not '
            'credited to the act it names.',
        ],
        'repeal_acts': {},
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
