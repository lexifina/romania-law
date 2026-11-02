"""Legea nr. 255/2013 pentru punerea în aplicare a Legii nr. 135/2010 privind Codul de procedură penală (Lexifina,
2026-11-02).

Act page 150697 is also its base text (DetaliiDocumentAfis/150697); no republication; 2 forms 01.02.2014 and 28.06.2014,
both held from Common Crawl (forms listed by the act page's capture 20260608043958). forms.d/legea-255-2013.json.
Its articles that amend other acts quote the text they insert or rewrite; that text stays inside the amending article
('quoted_articles', 'quoted_lines', 'quoted_siblings'). The law key 'legea-255-2013' is the one other parts already
credit from the portal's notes; this module adds the same entry to BASE_LAWS (same fields, same order), so they parse
byte-identical.
"""
SLUG = 'legea-255-2013'
TITLE = ('Legea nr. 255/2013 pentru punerea în aplicare a Legii nr. 135/2010 privind Codul de procedură penală și pentru '
         'modificarea și completarea unor acte normative care cuprind dispoziții procesual penale')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-255-2013', 'short': 'Legea nr. 255/2013', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'quoted_lines': True, 'quoted_siblings': True, 'trailing_notes': True,
        'reprint_law': True, 'rect_after': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/150697',
        'in_force': '2014-02-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 515 of 14 August 2013, in force with the Code of '
                     'Criminal Procedure on 1 February 2014 (its art. 104).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 255/2013: the first version is the law as published in Monitorul Oficial nr. 515 of 14 August '
            '2013 (DetaliiDocumentAfis/150697), dated 1 February 2014, the day its art. 104 puts it in force with the '
            'Code of Criminal Procedure; the same day the portal\'s form of 01.02.2014 gives the text in force, '
            'with the changes of OUG nr. 116/2013 (arts. 23 and 104).',
            'Legea nr. 255/2013: OUG nr. 116/2013 (Monitorul Oficial nr. 837 of 24 December 2013) rewrote art. 104 so '
            'that art. 104 itself and art. 23 alin. (5) and (6), in its own new wording, took effect on 30 December '
            '2013. The law as published gives a single day, 1 February 2014, and the record starts then: the two '
            'provisions are not shown from 30 December 2013, since their wording of that day is the ordinance\'s, '
            'not the law\'s as enacted.',
            'Legea nr. 255/2013: most of its articles amend other acts and quote the text they insert or rewrite. The '
            'quoted text is kept inside the amending article, as printed, and is not filed as articles of this law. '
            'The law as published prints the quoted articles as articles inside the amending article; the forms '
            'print them as paragraphs ("Art. 252^2"); these layout changes have no note and are the publisher\'s, '
            'labelled unexplained.',
            'Legea nr. 255/2013: the note after art. 109 on the EU directives the law transposes ("* Prezenta lege '
            'transpune ...") is not an article\'s text and is left out.',
        ],
        'repeal_acts': {},
    }
    # the entry the portal's note links give (other parts carry it), read from Legea nr. 255/2013's heading
    P.BASE_LAWS.setdefault(SLUG, {
        'label': 'Legea nr. 255/2013',
        'title': 'Legea nr. 255 din 19 iulie 2013, publicată în Monitorul Oficial al României, Partea I, nr. 515 din '
                 '14 august 2013',
        'kind': 'law', 'enacted': '2013-07-19', 'published': '2013-08-14',
        'url': P.PORTAL + 'DetaliiDocument/150697',
    })
    # the transposition note printed after the last article
    P.EDITORIAL_LINES[SLUG] = {'art-109': (
        '*', 'Prezenta lege transpune dispoziții cuprinse în directive ale Uniunii Europene',
        '1. art. 1, art. 2 alin. (1)-(5), art. 3 alin. (1), (2), (5), (7) și (9) și art. 4 din Directiva 2010/64/UE',
        '2. art. 3, 4, 6, 7 și art. 8 alin. (2) din Directiva 2012/13/UE')}
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
