"""Legea nr. 76/2012 pentru punerea în aplicare a Legii nr. 134/2010 privind Codul de procedură civilă (Lexifina,
2026-11-02).

Act page 138484 is also its base text (DetaliiDocumentAfis/138484); no republication; 4 forms 14.02.2013 .. 19.10.2014,
all held from Common Crawl (forms listed by the act page's capture 20251213014308). forms.d/legea-76-2012.json.
Its articles that amend other acts quote the text they insert or rewrite; that text stays inside the amending article
('quoted_articles', 'quoted_lines', 'quoted_siblings'). The law key 'legea-76-2012' is the one the Code of Civil
Procedure part already credits (BASE_LAWS, unchanged).
"""
SLUG = 'legea-76-2012'
# art. 38 pct. 1 and 2 (arts. 12 and 13 of Legea nr. 193/2000, as rewritten), put off to 1 October 2013
ART38 = ('1. Articolul 12 va avea următorul cuprins:', '"Art. 12', '(1) În cazul în care constată utilizarea unor',
         '(2) La cererea de chemare în judecată va fi anexat', '(3) Asociațiile pentru protecția consumatorului',
         '(4) Dispozițiile alin. (1)-(3) nu aduc atingere', '2. Articolul 13 va avea următorul cuprins:', '"Art. 13',
         '(1) Instanța, în cazul în care constată existența', '(2) În cazul prevăzut la alin. (1), instanța va aplica',
         '(3) Dacă instanța constată că nu sunt clauze abuzive', '(4) Hotărârea este supusă numai apelului')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-76-2012', 'short': 'Legea nr. 76/2012', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'quoted_lines': True, 'quoted_siblings': True, 'trailing_notes': True,
        'reprint_law': True,
        'title': 'Legea nr. 76/2012 pentru punerea în aplicare a Legii nr. 134/2010 privind Codul de procedură civilă',
        'url': P.PORTAL + 'DetaliiDocument/138484',
        'in_force': '2013-02-15', 'first_law': SLUG,
        # art. 82: art. 80 in force 3 days after publication (Monitorul Oficial nr. 365 of 30 May 2012)
        'early_units': {
            'day': '2012-06-02', 'arts': {'art-080': None},
            'note': 'The provision in force 3 days after the law was published in Monitorul Oficial nr. 365 of 30 May '
                    '2012, as its art. 82 provides: art. 80. The rest of the law takes effect with the Code of Civil '
                    'Procedure, on 15 February 2013.',
        },
        'later_provisions': (
            {'day': '2013-10-01', 'law': SLUG, 'lines': ART38, 'keys': ('art-038',),
             'note': 'Art. 38 pct. 1 and 2 take effect on this day: art. 82 of the law, as OUG nr. 4/2013 amended it '
                     'and Legea nr. 214/2013 amended that ordinance, puts them in force on 1 October 2013.'},
        ),
        'base_note': 'The rest of the law as published in Monitorul Oficial nr. 365 of 30 May 2012, in force with the '
                     'Code of Civil Procedure on 15 February 2013 (its arts. 81 alin. (1) and 82, as amended).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 76/2012: the law as published in Monitorul Oficial nr. 365 of 30 May 2012 '
            '(DetaliiDocumentAfis/138484). Its art. 82 puts it in force on the day its art. 81 alin. (1) gives the '
            'Code of Civil Procedure, except art. 80, in force 3 days after publication. That day was 1 September '
            '2012 as published; OUG nr. 44/2012 moved it to 1 February 2013 and OUG nr. 4/2013 to 15 February 2013, '
            'each before the earlier day came. So the first version, of 2 June 2012, holds only art. 80; on 15 '
            'February 2013 the rest of the law as published is added, credited to Legea nr. 76/2012, and the same '
            'day the portal\'s form of 15.02.2013 gives the text in force (OUG nr. 44/2012, OUG nr. 4/2013, and Legea '
            'nr. 2/2013, which repealed arts. 39 and 60 from that day).',
            'Legea nr. 76/2012: the portal\'s form of 14 February 2013 comes before the day the law took effect '
            '(save art. 80, which it does not change) and is not used; its changes (OUG nr. 44/2012, to art. 81) '
            'arrive with the form of 15 February 2013.',
            'Legea nr. 76/2012: art. 82 as amended by OUG nr. 4/2013 put art. 38 pct. 1 and 2 (the new arts. 12 and 13 '
            'of Legea nr. 193/2000) in force on 1 July 2013, and Legea nr. 214/2013 moved that to 1 October 2013. '
            'Under the rule for text printed before its day, those two points are absent until 1 October 2013 and '
            'are added that day, credited to Legea nr. 76/2012.',
            'Legea nr. 76/2012: most of its articles amend other acts and quote the text they insert or rewrite. The '
            'quoted text is kept inside the amending article, as printed. The law as published prints art. 13\'s '
            'quoted arts. 964^1 and 964^2 of the Code of Civil Procedure as paragraphs ("Art. 964^1"), and the '
            'forms print them as articles placed after art. 13, the rest of art. 13 inside the second; both are read '
            'as text of art. 13, in the printed order.',
            'Legea nr. 76/2012: the forms print in art. 13 the portal\'s line "Legea nr. 134/2010 privind Codul de '
            'procedură civilă a fost republicată în MONITORUL OFICIAL nr. 545 din 3 august 2012."; it is editorial '
            'matter, not the law\'s text, and is left out.',
        ],
        'repeal_acts': {},
    }
    P.EDITORIAL_LINES[SLUG] = {
        'art-013': ('Legea nr. 134/2010 privind Codul de procedură civilă a fost republicată în MONITORUL OFICIAL nr. '
                    '545 din 3 august 2012.',)}
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
