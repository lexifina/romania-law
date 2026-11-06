"""Where each act lives in the repository: its official identifier, <kind>/<year>/<number>/ (lege/1990/31/).

Act slugs (legea-31-1990, codul-civil, constitutia) stay the act ids, for tags (`<slug>/<day>`), the corpus and the
tools. Only the folder follows the official identifier, as the UK (ukpga/2014/6/) and German corpora do, so the
repository stays browsable at thousands of acts and every act is found by its number.

Library (used by append.py) and a one-off command:

    python -X utf8 layout.py move <repo> --when <epoch seconds>   # append the move commit to main (no push)

The move is one commit, labelled `Kind: layout`, that renames every act folder from its slug to its path and writes
data/paths.json. History before it keeps the old folders (git log --follow, or tools/on.py, which reads both).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

KINDS = {'legea': 'lege', 'oug': 'oug', 'og': 'og', 'hg': 'hg', 'decret': 'decret', 'decret-lege': 'decret-lege',
         # Parliament's decisions: numbered per chamber (and for joint sittings), so the chamber is a folder level
         'hotarare-senat': 'hotarare-parlament/senat', 'hotarare-camera': 'hotarare-parlament/camera',
         'hotarare-parlament': 'hotarare-parlament/parlament',
         # a Permanent Bureau numbers its decisions apart from its chamber's plenary: a folder of its own
         'hotarare-senat-birou': 'hotarare-parlament/senat/birou', 'hotarare-camera-birou': 'hotarare-parlament/camera/birou',
         'hotarare-parlament-birou': 'hotarare-parlament/parlament/birou'}
KIND_NAMES = {'constitutie': 'Constituția', 'lege': 'Laws (legi)', 'oug': 'Emergency ordinances (OUG)',
              'og': 'Ordinances (OG)', 'hg': 'Government decisions (HG)', 'decret': 'Decrees', 'decret-lege': 'Decree-laws',
              'hotarare-parlament': "Parliament's decisions (Senate, Chamber of Deputies, joint sittings)",
              'cod': 'Historical codes', 'alte': 'Other acts'}
# Orders and the numbered instruments of an authority (approved 2026-11-04): an order's number is unique only within one
# issuer's yearly register, so their folders add the issuer, a lineage slug that is frozen once published:
# <kind>/<issuer>/<year>/<number>[-<series>]/, ids <kind>-<issuer>-<number>[-<series>]-<year>
# (ordin/justitie/2012/492-c/, ordin-justitie-492-c-2012).
ORDER_KINDS = {'ordin': 'Ministerial and authority orders (ordine)', 'norma': 'Norms (norme)',
               'regulament': 'Regulations (regulamente)', 'instructiuni': 'Instructions (instrucțiuni)',
               'precizari': 'Clarifications (precizări)', 'metodologie': 'Methodologies (metodologii)',
               'criterii': 'Criteria (criterii)',
               # the normative acts autonomous authorities issue under other names (sources/norms, 2026-11-06): BNR
               # circulars and board decisions, the decisions of ASF, ANCOM, CNA and the other regulators; numbered per
               # issuer and year like an order: circulara/bnr/2026/27/, hotarare/bnr/2010/5/, decizie/ancom/2024/123/
               'circulara': 'Circulars of authorities (circulare)',
               'hotarare': "Decisions of authorities' boards (hotărâri)",
               'decizie': 'Decisions of authorities (decizii)'}
# The kinds added on 2026-11-06 share a first word with the lane roots decizie-bec and hotarare-aep: an id of those
# roots is never read as one of these kinds (act_path below).
NEW_ORDER_KINDS = ('circulara', 'hotarare', 'decizie')
KIND_NAMES = {**{k: v for k, v in KIND_NAMES.items() if k not in ('cod', 'alte')}, **ORDER_KINDS,
              'cod': KIND_NAMES['cod'], 'alte': KIND_NAMES['alte']}
# The publish-first source lanes (approved 2026-11-04; sources/<lane>/ready, built into parts by
# ro-explore/pubfirst/lane_parts.py). Each act carries the folder its lane built it in (`folder`), under one of these
# roots, and its id starts with that root: decizie-bec/<election>/<nr>, hotarare-aep/<year>/<nr>, norma-aep/<year>/<id>,
# curtea-de-conturi/<kind>/<year>/<nr>, avocatul-poporului/<kind>/<year>/<nr>, cncd/hotarare/<year>/<nr>,
# anspdcp/<kind>/<year>/<nr or day>, normativ-tehnic/<code>, proiect/<initiator>/<year>/<id>,
# profesii/<body>/<doc> or profesii/<body>/<organ-kind>/<year>/<nr>.
LANE_KINDS = {'decizie-bec': 'Central Electoral Bureau decisions, regulations and results (BEC)',
              'hotarare-aep': 'Permanent Electoral Authority decisions (AEP)',
              'norma-aep': 'Permanent Electoral Authority norms, instructions and lists (AEP)',
              'curtea-de-conturi': 'Court of Accounts (plenum decisions, regulations)',
              'avocatul-poporului': 'Ombudsman (Avocatul Poporului): recommendations, reports, constitutional referrals',
              'cncd': 'Anti-discrimination council decisions (CNCD)',
              'anspdcp': 'Data protection authority decisions and sanction notices (ANSPDCP)',
              'normativ-tehnic': 'Technical rules for construction (normative tehnice)',
              'proiect': 'Draft acts in consultation and bills in Parliament (proiecte)',
              # EU legislation in force with its authentic Romanian OJ text (sources/eu-law, from CELLAR; 2026-11-05):
              # ue/<regulament|directiva|decizie>/<year>/<number>[-<n>], id ue-<kind>-<number>[-<n>]-<year>. The
              # folder follows the CELEX number (3 + year + R/L/D + number): 32016R0679 -> ue/regulament/2016/679.
              'ue': 'EU law in Romanian: regulations and directives in force (Official Journal text)',
              # Official annexes published apart from their act (sources/citizen; 2026-11-05): the act's own id is a
              # folder level, so an annex never collides with an act: anexa/<act id>/<annex>/, id anexa-<act id>-<annex>
              # (anexa/hg-1217-2023/anexa/, anexa/ordin-justitie-359-c-2013/anexa-2/); <annex> is "anexa" for a single
              # unnumbered annex, else "anexa-<n>".
              'anexa': 'Annexes published apart from their act (court circumscriptions, official forms)',
              # sources/professions: the rules each legal profession's body issues (not the statutes): a named
              # instrument amended over time is profesii/<body>/<doc> (profesii/unbr/statut, profesii/csm/cod-deontologic),
              # a numbered act is profesii/<body>/<organ-kind>/<year>/<nr> (profesii/unbr/hotarare-consiliu/2017/268);
              # bodies: unbr, inppa, unnpr, unej, ocjr, cscjr, unpir, mediere, csm, inm, ceccar, cafr;
              # ids profesii-<folder below the root, "/" -> "-"> (profesii-unbr-statut, profesii-unbr-hotarare-consiliu-2017-268)
              'profesii': "Legal professions' rules: statutes, codes of ethics, regulations and decisions of the "
                          'professional bodies (UNBR, UNNPR, UNEJ, OCJR, UNPIR, Consiliul de Mediere, CSM, INM, CAFR)',
              # Treaty texts (sources/treaties; 2026-11-06): the "Act Internațional" documents published in the
              # Monitorul Oficial with the act that ratifies or approves them. A treaty has no number of its own, so the
              # signing day and type name it: tratat/<year>/<MM-DD>-<type>[-<n>], id tratat-<year>-<MM-DD>-<type>[-<n>]
              # (tratat/2024/05-21-acord); -2, -3 ... in service document order for one day's several of one type.
              'tratat': 'Treaties and international agreements (texts published with their ratifying act)',
              # CNSC decisions (sources/cnsc; 2026-11-06): the public-procurement complaints council's decisions from its
              # portal, numbered per year: cnsc/decizie/<year>/<nr>[-<n>], id cnsc-decizie-<year>-<nr>[-<n>]
              # (cnsc/decizie/2026/3557, id cnsc-decizie-2026-3557); -2, -3 ... only when one year lists a number twice.
              'cnsc': 'Public procurement complaints council decisions (CNSC)'}
KIND_NAMES = {**{k: v for k, v in KIND_NAMES.items() if k not in ('cod', 'alte')}, **LANE_KINDS,
              'cod': KIND_NAMES['cod'], 'alte': KIND_NAMES['alte']}
LANE_ROOTS = tuple(LANE_KINDS)
LANE_FOLDER = re.compile(r'^(?:' + '|'.join(map(re.escape, LANE_ROOTS)) + r')(?:/[a-z0-9][a-z0-9-]*){1,4}$')
LANE_SLUG = re.compile(r'^(' + '|'.join(map(re.escape, LANE_ROOTS)) + r')-([a-z0-9][a-z0-9-]*)$')
# Local acts (approved 2026-11-04): a council numbers its decisions per year, so the council is the folder path:
# local/bucuresti/cgmb/<year>/<n>, local/bucuresti/sector-<k>/<year>/<n>, local/judet/<county>/<year>/<n>,
# local/<county>/<locality>/<year>/<n>; ids hcgmb-<n>-<year>, hcls<k>-<n>-<year>, hcj-<county>-<n>-<year>,
# hcl-<county>--<locality>-<n>-<year> (county and locality slugs may hold hyphens, so "--" parts them).
KIND_NAMES = {**{k: v for k, v in KIND_NAMES.items() if k not in ('cod', 'alte')},
              'local': 'Local acts (decisions of local and county councils)',
              'cod': KIND_NAMES['cod'], 'alte': KIND_NAMES['alte']}
LOCAL_SLUGS = [
    (re.compile(r'^hcgmb-(\d+)-(\d{4})(?:-\d+)?$'), lambda m: f'local/bucuresti/cgmb/{m.group(2)}/{int(m.group(1))}'),
    (re.compile(r'^hcls([1-6])-(\d+)-(\d{4})(?:-\d+)?$'),
     lambda m: f'local/bucuresti/sector-{m.group(1)}/{m.group(3)}/{int(m.group(2))}'),
    (re.compile(r'^hcj-([a-z]+(?:-[a-z]+)*)-(\d+)-(\d{4})(?:-\d+)?$'),
     lambda m: f'local/judet/{m.group(1)}/{m.group(3)}/{int(m.group(2))}'),
    (re.compile(r'^hcl-([a-z]+(?:-[a-z]+)*)--([a-z0-9]+(?:-[a-z0-9]+)*)-(\d+)-(\d{4})(?:-\d+)?$'),
     lambda m: f'local/{m.group(1)}/{m.group(2)}/{m.group(4)}/{int(m.group(3))}'),
]
KIND_ORDER = list(KIND_NAMES)
ORDER_SLUG_RE = re.compile(r'^(' + '|'.join(ORDER_KINDS) + r')-([a-z]+)-(\d+)(?:-([a-z]+))?-(\d{4})(?:-\d+)?$')
# An optional "-2", "-3" ... marks a second act under the same number after an earlier id was withdrawn (ids are never
# reused, so their tags never clash); the folder is still the official identifier.
SLUG_RE = re.compile(r'^(legea|oug|og|hg|decret|decret-lege|hotarare-senat|hotarare-camera|hotarare-parlament|hotarare-senat-birou|hotarare-camera-birou|'
                     r'hotarare-parlament-birou)-(\d+)-'
                     r'(\d{4})(?:-\d+)?$')
# A code's own act, from its title: "Codul civil (Legea nr. 287/2009)", "Codul administrativ (Ordonanța de urgență a
# Guvernului nr. 57/2019)".
TITLE_RE = [(re.compile(r'Ordonan[țţ]a de urgen[țţ][ăa] a Guvernului nr\.\s*(\d+)/(\d{4})'), 'oug'),
            (re.compile(r'Ordonan[țţ]a Guvernului nr\.\s*(\d+)/(\d{4})'), 'og'),
            (re.compile(r'\bLegea nr\.\s*(\d+)/(\d{4})'), 'lege')]
FIXED = {'constitutia': 'constitutie/1991'}
# A historical code with no law number of its own: codul-civil-1864, codul-procedura-civila-1865.
CODE_SLUG = re.compile(r'^codul-([a-z0-9-]+?)-(\d{4})$')
AMENDING = re.compile(r'\b(?:pentru|privind)\s+(?:modificarea|completarea|aprobarea|abrogarea|prorogarea|'
                      r'suspendarea|respingerea)\b|\bde modificare\b', re.I)
# A code is an act that IS a code: "Codul civil (Legea nr. 287/2009)", "Legea nr. 46/2008 - Codul silvic",
# "Legea nr. 86/2006 privind Codul vamal al României" (not an act that amends one: "pentru modificarea ... Codul fiscal").
CODE_NAME = re.compile(r'^(Cod(?:ul)?\b[^(]*?)\s*(?:\(|$)|^(?:Legea|Ordonan\S+(?: de urgen\S+)?(?: a Guvernului)?) nr\.\s*\d+/\d{4}'
                       r'\s*(?:-|–|privind)\s*(Codul [^,;(]+?)\s*$', re.I)


def act_path(slug: str, title: str = '') -> str:
    """The folder for an act: lege/1990/31 from legea-31-1990; a code's own act from its title."""
    if slug in FIXED:
        return FIXED[slug]
    m = SLUG_RE.match(slug)
    if m:
        return f'{KINDS[m.group(1)]}/{m.group(3)}/{int(m.group(2))}'
    m = ORDER_SLUG_RE.match(slug)
    if m and m.group(1) in NEW_ORDER_KINDS and LANE_SLUG.match(slug):
        m = None  # decizie-bec-..., hotarare-aep-...: a lane root's id, not an authority's decision
    if m:  # ordin-justitie-492-c-2012 -> ordin/justitie/2012/492-c
        return f'{m.group(1)}/{m.group(2)}/{m.group(5)}/{int(m.group(3))}' + (f'-{m.group(4)}' if m.group(4) else '')
    for rx, path in LOCAL_SLUGS:  # hcgmb-67-2004 -> local/bucuresti/cgmb/2004/67 (before the title rules: a local
        m = rx.match(slug)        # decision's title often names a law)
        if m:
            return path(m)
    for rx, kind in TITLE_RE:
        t = rx.search(title or '')
        if t:
            return f'{kind}/{t.group(2)}/{int(t.group(1))}'
    m = CODE_SLUG.match(slug)
    if m:  # a code older than numbered laws (Codul civil of 1864): cod/<year>/<name>
        return f'cod/{m.group(2)}/{m.group(1)}'
    m = LANE_SLUG.match(slug)
    if m:  # a source-lane act known only by id (a withdrawn row): under its root
        return f'{m.group(1)}/{m.group(2)}'
    # Never stop a publish for want of an identifier: the act goes under alte/ until FIXED names its folder.
    print(f'layout: no official identifier for act {slug!r} ({title!r}); filed under alte/{slug}', file=sys.stderr)
    return f'alte/{slug}'


def parts_of(path: str) -> tuple[str, str, str]:
    bits = path.split('/')
    if bits[0] == 'anexa' and len(bits) == 3:  # anexa/<act id>/<annex>: the act's year, the annex under its act
        m = re.search(r'-(\d{4})$', bits[1]) or re.search(r'-(\d{4})-\d{1,2}$', bits[1])  # hg-10-2021-2: 2021
        return bits[0], (m.group(1) if m else ''), f'{bits[1]}/{bits[2]}'
    if bits[0] in LANE_ROOTS and len(bits) >= 2:  # <root>/.../<year>/<id>: the year is the last 4-digit level, if any
        year = next((b for b in reversed(bits[1:-1]) if re.fullmatch(r'\d{4}', b)), '')
        if not year and bits[0] == 'decizie-bec' and len(bits) == 3:  # decizie-bec/<election>-<year>/<nr>
            m = re.search(r'(\d{4})$', bits[1])
            year = m.group(1) if m else ''
        return bits[0], year, bits[-1]
    if bits[0] == 'hotarare-parlament' and len(bits) == 4:  # hotarare-parlament/<chamber>/<year>/<number>
        return bits[0], bits[2], bits[3]
    if bits[0] == 'hotarare-parlament' and len(bits) == 5:  # hotarare-parlament/<chamber>/birou/<year>/<number>
        return bits[0], bits[3], bits[4]
    if bits[0] in ORDER_KINDS and len(bits) == 4:  # ordin/<issuer>/<year>/<number>[-<series>]
        return bits[0], bits[2], bits[3]
    if bits[0] == 'local' and len(bits) >= 5:  # local/<council ...>/<year>/<number>
        return bits[0], bits[-2], bits[-1]
    return bits[0], (bits[1] if len(bits) > 1 else ''), (bits[2] if len(bits) > 2 else '')


# The bodies that issue orders, by the issuer slug of their folders (frozen once published): each slug names one
# body and its successors (a lineage).
ISSUER_NAMES: dict[str, str] = {
    'aaas': 'Autoritatea pentru Administrarea Activelor Statului (APAPS 2000-2004, AVAS 2004-2012)',
    'achizitii': 'Public procurement (ANRMAP, ANAP)',
    'adoptii': 'Oficiul Român pentru Adopții',
    'adr': 'Autoritatea pentru Digitalizarea României',
    'aep': 'Autoritatea Electorală Permanentă',
    'agricultura': 'Ministerul Agriculturii (all names)',
    'amepip': 'Agenția pentru Monitorizarea și Evaluarea Performanțelor Întreprinderilor Publice',
    'anaf': 'Agenția Națională de Administrare Fiscală (ANAF)',
    'anci': 'Agenția Națională pentru Comunicații și Informatică',
    'ancom': 'ANCOM (and ANRC, IGCTI before it)',
    'ancpi': 'Agenția Națională de Cadastru și Publicitate Imobiliară',
    'ancs': 'Research authority (ANSTI, Autoritatea Națională pentru Cercetare Științifică)',
    'andpdca': 'Autoritatea Națională pentru Drepturile Persoanelor cu Dizabilități, Copii și Adopții',
    'anfp': 'Agenția Națională a Funcționarilor Publici',
    'anmcs': 'Autoritatea Națională de Management al Calității în Sănătate',
    'anofm': 'Agenția Națională pentru Ocuparea Forței de Muncă',
    'anpc': 'Autoritatea Națională pentru Protecția Consumatorilor',
    'anre': 'Autoritatea Națională de Reglementare în Domeniul Energiei',
    'anrgn': 'Autoritatea Națională de Reglementare în Domeniul Gazelor Naturale (to 2007, now ANRE)',
    'anrm': 'Agenția Națională pentru Resurse Minerale',
    'anrp': 'Autoritatea Națională pentru Restituirea Proprietăților',
    'anrsc': 'ANRSC (community utilities; ANRSPGC before it)',
    'anspdcp': 'Autoritatea Națională de Supraveghere a Prelucrării Datelor cu Caracter Personal',
    'ansvsa': 'ANSVSA (veterinary and food safety)',
    'antidoping': 'Agenția Națională Antidoping',
    'aparare': 'Ministerul Apărării Naționale',
    'ard': 'Agenția Română de Dezvoltare',
    'arhitecti': 'Ordinul Arhitecților din România',
    'arice': 'Agenția Română pentru Investiții și Comerț Exterior',
    'asf': 'Autoritatea de Supraveghere Financiară',
    'asg': 'Agenția pentru Strategii Guvernamentale',
    'asistentimedicali': 'Ordinul Asistenților Medicali Generaliști, Moașelor și Asistenților Medicali din România',
    'aspaas': 'Autoritatea pentru Supravegherea Publică a Activității de Audit Statutar',
    'autoritateacontrol': 'Autoritatea Națională de Control',
    'avocatulpoporului': 'Avocatul Poporului',
    'bnr': 'Banca Națională a României',
    'cafr': 'Camera Auditorilor Financiari din România',
    'camera': 'Camera Deputaților',
    'casaopsnaj': 'Casa Asigurărilor de Sănătate a Apărării, Ordinii Publice, Siguranței Naționale și Autorității Judecătorești',
    'ccir': 'Camera de Comerț și Industrie a României',
    'cear': 'Centrul Euro-Atlantic pentru Reziliență',
    'ceccar': 'Corpul Experților Contabili și Contabililor Autorizați din România',
    'cetatenie': 'Autoritatea Națională pentru Cetățenie',
    'cifga': 'Comitetul Interministerial de Finanțări, Garanții și Asigurări',
    'cinematografie': 'Centrul (Oficiul) Național al Cinematografiei',
    'cmdpd': 'Consiliul de Monitorizare a Implementării Convenției privind Drepturile Persoanelor cu Dizabilități',
    'cnas': 'Casa Națională de Asigurări de Sănătate',
    'cncan': 'Comisia Națională pentru Controlul Activităților Nucleare',
    'cna': 'Consiliul Național al Audiovizualului',
    'cncd': 'Consiliul Național pentru Combaterea Discriminării',
    'cnpp': 'Casa Națională de Pensii Publice',
    'cnvm': 'Comisia Națională a Valorilor Mobiliare (to 2013, now ASF)',
    'comunicatii': 'Ministerul Comunicațiilor / Cercetării, Inovării și Digitalizării',
    'conas': 'Comisia Națională de Acreditare a Spitalelor',
    'concurenta': 'Consiliul Concurenței',
    'copii': 'Child protection (ANPCA, ANPDC, ANPDCA)',
    'cosr': 'Comitetul Olimpic și Sportiv Român',
    'csa': 'Comisia de Supraveghere a Asigurărilor (to 2013, now ASF)',
    'csm': 'Consiliul Superior al Magistraturii',
    'csspp': 'Comisia de Supraveghere a Sistemului de Pensii Private (to 2013, now ASF)',
    'culte': 'Secretariatul de Stat pentru Culte',
    'cultura': 'Ministerul Culturii (all names)',
    'curteadeconturi': 'Curtea de Conturi',
    'dapl': 'Departamentul pentru Administrație Publică Locală',
    'dezvoltare': 'Ministerul Dezvoltării / Lucrărilor Publice (construction rules)',
    'dgep': 'Direcția Generală pentru Evidența Persoanelor',
    'dgia': 'Direcția Generală de Informații a Apărării',
    'disciplinafunctionari': 'Comisia de disciplină pentru înalții funcționari publici',
    'dizabilitati': 'Persons with disabilities (SSPH, ANPH, ANPDPD)',
    'dna': 'Direcția Națională Anticorupție (Parchetul Național Anticorupție before it)',
    'dnsc': 'Directoratul Național de Securitate Cibernetică',
    'dsu': 'Departamentul pentru Situații de Urgență',
    'economie': 'Ministerul Economiei (all names)',
    'educatie': 'Ministerul Educației (all names)',
    'egalitate': 'Agenția Națională pentru Egalitatea de Șanse între Femei și Bărbați',
    'europene': 'European affairs (Ministerul Integrării Europene, Ministerul / Departamentul Afacerilor Europene)',
    'exporturi': 'Agenția Națională de Control al Exporturilor (Strategice ...)',
    'externe': 'Ministerul Afacerilor Externe',
    'familie': 'Ministerul Familiei (all names)',
    'fci': 'Fondul de Compensare a Investitorilor',
    'fga': 'Fondul de Garantare a Asiguraților',
    'fgdb': 'Fondul de Garantare a Depozitelor Bancare',
    'fgdspp': 'Fondul de Garantare a Drepturilor din Sistemul de Pensii Private',
    'finante': 'Ministerul Finanțelor (Publice); Ministerul Economiei și Finanțelor',
    'fonduri': 'Ministerul Fondurilor / Investițiilor și Proiectelor Europene',
    'fps': 'Fondul Proprietății de Stat',
    'functiepublica': 'Ministerul Funcției Publice',
    'geodezi': 'Ordinul Geodezilor din România',
    'guvern': 'Guvernul (prime-minister orders, Secretariatul General al Guvernului)',
    'hipica': 'Autoritatea Hipică Națională',
    'iccj': 'Înalta Curte de Casație și Justiție (Curtea Supremă de Justiție before it)',
    'igsu': 'Inspectoratul General pentru Situații de Urgență',
    'iiccr': 'Institutul de Investigare a Crimelor Comunismului în România',
    'imm': 'Small and medium enterprises (ANIMMC; the ministries and departments for SMEs)',
    'ina': 'Institutul Național de Administrație',
    'inaltifunctionari': 'Comisia de concurs pentru recrutarea înalților funcționari publici',
    'infrastructura': 'Departamentul pentru Proiecte de Infrastructură și Investiții (Străine ...)',
    'ins': 'Institutul Național de Statistică (Comisia Națională pentru Statistică before it)',
    'inspectiajudiciara': 'Inspecția Judiciară',
    'integritate': 'Agenția Națională de Integritate',
    'international': 'International bodies (Council of Europe ...: out of scope)',
    'interne': 'Ministerul Afacerilor Interne (all names)',
    'isc': 'Inspectoratul de Stat în Construcții',
    'iscir': 'ISCIR (boilers, pressure vessels and lifting equipment)',
    'justitie': 'Ministerul Justiției',
    'luptatori': 'Secretariatul de Stat pentru Recunoașterea Meritelor Luptătorilor împotriva Regimului Comunist',
    'macroprudential': 'Comitetul Național pentru Supravegherea Macroprudențială',
    'medici': 'Colegiul Medicilor din România',
    'mediu': 'Ministerul Mediului (all names)',
    'metrologie': 'Biroul Român de Metrologie (Legală)',
    'minoritati': 'Departamentul pentru Protecția Minorităților Naționale',
    'moldova': 'Departamentul pentru Relația cu Republica Moldova',
    'munca': 'Ministerul Muncii (all names)',
    'nucleara': 'Agenția Nucleară',
    'offshore': 'Black Sea offshore operations regulator (ACROPO)',
    'oli': 'Oficiul pentru Licență Industrială',
    'onac': 'Oficiul Național pentru Achiziții Centralizate',
    'onjn': 'Oficiul Național pentru Jocuri de Noroc',
    'onpcsb': 'Oficiul Național de Prevenire și Combatere a Spălării Banilor',
    'onrc': 'Oficiul Național al Registrului Comerțului',
    'orniss': 'Oficiul Registrului Național al Informațiilor Secrete de Stat',
    'osim': 'Oficiul de Stat pentru Invenții și Mărci',
    'parchet': 'Ministerul Public (Parchetul de pe lângă Înalta Curte / Curtea Supremă)',
    'penitenciare': 'Administrația Națională a Penitenciarelor',
    'privatizare': 'Agenția Națională pentru Privatizare (and for SME development); Ministerul Privatizării',
    'prognoza': 'Comisia Națională de (Strategie și) Prognoză',
    'rechizitii': 'Comisia Centrală de Rechiziții',
    'revolutionari': 'Secretariatul de Stat pentru Problemele Revoluționarilor din Decembrie 1989',
    'rezervestat': 'State reserves and special problems (OCSPS, ANRSPS)',
    'romaniipretutindeni': 'Românii de pretutindeni (ministry, department)',
    'romi': 'Agenția Națională pentru Romi',
    'rur': 'Registrul Urbaniștilor din România',
    'sanatate': 'Ministerul Sănătății',
    'senat': 'Senatul',
    'sie': 'Serviciul de Informații Externe',
    'smap': 'Statul Major al Apărării',
    'sport': 'Sport and youth (Ministerul Tineretului și Sportului, Ministerul Sportului, ANS, ANST)',
    'spp': 'Serviciul de Protecție și Pază',
    'sri': 'Serviciul Român de Informații',
    'sts': 'Serviciul de Telecomunicații Speciale',
    'transporturi': 'Ministerul Transporturilor (all names)',
    'turism': 'Tourism (Ministerul Turismului, Autoritatea Națională pentru Turism, Ministerul Antreprenoriatului și Turismului)',
    'ue': 'EU institutions (acts reprinted in the Monitorul Oficial: out of scope)',
    'vama': 'Autoritatea Vamală Română / Autoritatea Națională a Vămilor',
}

def council_of(path: str) -> str:
    """The council of a local act's folder (local/bucuresti/cgmb/2004/67 -> bucuresti/cgmb); '' for every other act."""
    bits = (path or '').split('/')
    return '/'.join(bits[1:-2]) if bits[0] == 'local' and len(bits) >= 5 else ''


def issuer_of(path: str) -> str:
    """The issuer level of an order's folder (ordin/justitie/2012/492-c -> justitie); '' for every other act."""
    bits = (path or '').split('/')
    return bits[1] if bits[0] in ORDER_KINDS and len(bits) == 4 else ''


def paths_at(repo: Path, ref: str = 'main') -> dict[str, str]:
    """{slug: path} recorded on ref (data/paths.json), or {} before the layout move."""
    out = subprocess.run(['git', 'show', f'{ref}:data/paths.json'], cwd=repo, capture_output=True, text=True,
                         encoding='utf-8')
    if out.returncode:
        return {}
    return json.loads(out.stdout).get('paths', {})


def assign(c: dict, known: dict[str, str]) -> None:
    """Give every act its folder: the recorded one, else its official identifier. Two acts may never share one."""
    seen: dict[str, str] = {}
    for a in c['acts']:
        p = known.get(a['slug']) or lane_folder(a) or act_path(a['slug'], a.get('title', ''))
        if p in seen and seen[p] != a['slug']:
            # Two corpus acts claim one identifier (a duplicate entry): keep publishing, the later one under alte/.
            print(f'layout: {a["slug"]} and {seen[p]} both claim {p}; {a["slug"]} filed under alte/', file=sys.stderr)
            p = f'alte/{a["slug"]}'
        seen[p] = a['slug']
        a['path'] = p


def lane_folder(a: dict) -> str | None:
    """The folder a source-lane act names for itself (`folder`), when it lies under its own id's root; else None."""
    f, m = a.get('folder'), LANE_SLUG.match(a['slug'])
    if isinstance(f, str) and m and LANE_FOLDER.match(f) and f.split('/', 1)[0] == m.group(1):
        return f
    return None


def status(a: dict) -> str:
    if a.get('_withdrawn'):
        return 'withdrawn'
    last = a['versions'][-1] if a['versions'] else {}
    if 'units' in last and not last['units']:
        return f'repealed {last["from"]}'
    if a.get('unconsolidated'):  # amended, but the portal publishes no consolidated text: the act as published only
        return 'amended, not consolidated'
    if a.get('amendments_checked') is False:  # published as it appeared; whether it was amended is not checked yet
        return 'as published, amendments not yet checked'
    if a.get('record_status') and (lane_folder(a) or council_of(a.get('path') or '')):
        # a source-lane or local act states its own (metadata only, text withheld, text pending OCR ...)
        return a['record_status']
    if AMENDING.search(a.get('title', '')):
        return 'amending act'
    return 'in force'


def code_name(a: dict) -> str | None:
    if a['slug'] == 'constitutia':
        return 'Constituția României'
    if AMENDING.search(a.get('title', '')):
        return None
    m = CODE_NAME.search(a.get('title', ''))
    if not m:
        return None
    name = (m.group(1) or m.group(2) or '').strip()
    return name if name.lower().startswith('cod') else None


def acts_rows(c: dict) -> list[dict]:
    rows = []
    for a in c['acts']:
        p = a.get('path') or a['slug']
        kind, year, number = parts_of(p if not a.get('_withdrawn') else act_path(a['slug'], a.get('title', '')))
        vs = a['versions']
        rows.append({'slug': a['slug'], 'path': None if a.get('_withdrawn') else p, 'kind': kind, 'year': year,
                     'number': number, 'withdrawn_by': a.get('_withdrawn_by'), 'reason': a.get('_reason'),
                     'title': a.get('title', ''), 'short': a.get('short', ''), 'code': code_name(a), 'status': status(a),
                     'versions': len(vs), 'from': vs[0]['from'] if vs else None, 'latest': vs[-1]['from'] if vs else None,
                     'portal': a.get('url'),
                     # orders: the issuer level, and a joint order's co-issuers with the id each one's number gives it
                     **({'issuer': issuer_of(p), 'joint': a.get('joint') or []} if issuer_of(p) else {}),
                     # a source-lane act's machine flags (text_withheld: personal_data, text_missing, annex_missing ...)
                     **({'flags': a['lane_flags']} if a.get('lane_flags') and lane_folder(a) else {}),
                     # local acts: the council's folder and name, and the act's machine flags (text_pending: ocr ...)
                     **({'council': council_of(p), 'council_name': a.get('council_name') or '',
                         **({'flags': a['lane_flags']} if a.get('lane_flags') else {})} if council_of(p) else {})})
    return sort_rows(rows)


def _num(n: str) -> int:
    m = re.match(r'\d+', n or '')
    return int(m.group(0)) if m else 0


def sort_rows(rows: list[dict]) -> list[dict]:
    """Kind, then year and number; orders by issuer first. Acts of the other kinds keep the earlier order exactly (the
    sort is stable, and their key adds only constants)."""
    order = {k: i for i, k in enumerate(KIND_ORDER)}

    def key(r):
        if r.get('council'):
            return (order.get(r['kind'], 99), r['council'], r['year'], _num(r['number']), r['number'])
        if r.get('issuer'):
            return (order.get(r['kind'], 99), r['issuer'], r['year'], _num(r['number']), r['number'])
        return (order.get(r['kind'], 99), '', r['year'], int(r['number']) if r['number'].isdigit() else 0, '')
    rows.sort(key=key)
    return rows


def acts_json(c: dict) -> str:
    return json.dumps({'country': c['country']['code'], 'acts': acts_rows(c)}, ensure_ascii=False, indent=0) + '\n'


def paths_json(c: dict, since: str) -> str:
    orders = any(issuer_of(a.get('path') or '') for a in c['acts'])
    local = any(council_of(a.get('path') or '') for a in c['acts'] if not a.get('_withdrawn'))
    al = aliases_of(c)
    return json.dumps({'layout': '<kind>/<year>/<number>' + ('; orders: <kind>/<issuer>/<year>/<number>[-<series>]'
                                                             if orders else '') +
                       ('; local acts: local/<council>/<year>/<number>' if local else ''), 'since': since,
                       'note': 'Act folders before the layout move were named by slug; tools/on.py reads both.' + (
                           ' A joint order lives once, under its first issuer; `aliases` maps the id each co-issuer\'s '
                           'number gives it to that folder.' if al else ''),
                       'paths': {a['slug']: a['path'] for a in sorted(c['acts'], key=lambda a: a['slug'])
                                 if a.get('path') and not a.get('_withdrawn')},
                       **({'aliases': al} if al else {})},
                      ensure_ascii=False, indent=0) + '\n'


def aliases_of(c: dict) -> dict[str, str]:
    """A joint order lives once, under the issuer its EMITENT block lists first; every co-issuer's own number gives it
    an alias id (ordin-munca-1883-2016 -> ordin/sanatate/2016/1306). No duplicate folders and no symlinks: tools/on.py
    resolves the alias. An alias that is an act's own id is never written."""
    ids = {a['slug'] for a in c['acts']}
    out = {}
    for a in c['acts']:
        if a.get('path') and not a.get('_withdrawn'):
            for j in a.get('joint') or []:
                if j.get('alias') and j['alias'] != a['slug'] and j['alias'] not in ids:
                    out[j['alias']] = a['path']
    return dict(sorted(out.items()))


def acts_md(c: dict) -> str:
    rows = acts_rows(c)
    esc = lambda s: (s or '').replace('|', '/')  # noqa: E731
    orders = any(r.get('issuer') for r in rows)
    out = ['# Every act in this repository', '',
           f'{len(rows)} acts, {sum(r["versions"] for r in rows):,} versions. Each act lives in a folder named by its '
           'official identifier, `<kind>/<year>/<number>/` (Legea nr. 31/1990 is `lege/1990/31/`)' + (
               '; an order adds its issuer, `ordin/<issuer>/<year>/<number>[-<series>]/` (`ordin/justitie/2012/492-c/`)'
               if orders else '') + '; its README.md lists its articles and the decisions made by hand. Dates are in-force days. Generated on every publish; '
           'the same list is in [data/acts.json](data/acts.json).', '']
    codes = [r for r in rows if r['code']]
    if codes:
        out += ['## Codes and the Constitution, by name', '', '| Code | Act | Folder | Versions | Latest |',
                '| --- | --- | --- | ---: | --- |']
        for r in sorted(codes, key=lambda r: r['code']):
            out.append(f'| {esc(r["code"])} | {esc(r["short"] or r["title"])} | [`{r["path"]}/`]({r["path"]}/) | '
                       f'{r["versions"]} | {r["latest"]} |')
        out.append('')
    gone = [r for r in rows if r['status'] == 'withdrawn']
    rows = [r for r in rows if r['status'] != 'withdrawn']
    for kind in KIND_ORDER + sorted({r['kind'] for r in rows} - set(KIND_ORDER)):
        group = [r for r in rows if r['kind'] == kind]
        if not group:
            continue
        n_amend = sum(1 for r in group if r['status'] == 'amending act')
        out += [f'## {KIND_NAMES.get(kind, kind)} ({len(group)}' + (f', of which {n_amend} amending acts' if n_amend else '')
                + ')', '']
        if kind in ORDER_KINDS:
            out += order_sections(group, esc)
            continue
        if kind == 'local':
            out += local_sections(group, esc)
            continue
        out += ['| Act | Folder | Status | Versions | From | Latest |', '| --- | --- | --- | ---: | --- | --- |']
        for r in group:
            out.append(f'| {esc(r["title"])} | [`{r["path"]}/`]({r["path"]}/) | {r["status"]} | {r["versions"]} | '
                       f'{r["from"]} | {r["latest"]} |')
        out.append('')
    if gone:
        out += [f'## Withdrawn from the record ({len(gone)})', '',
                'Acts published here and later found not to belong (for example, titled as Government decisions but '
                'issued by another body). Their folders were removed by a correction commit; the commits that added '
                'them stay in the history. Their ids are retired: a later act with the same number gets the id with '
                '`-2` appended.', '', '| Act id | Reason | Removed by |', '| --- | --- | --- |']
        for r in sorted(gone, key=lambda r: r['slug']):
            out.append(f'| `{r["slug"]}` | {esc(r.get("reason") or "")} | {r.get("withdrawn_by") or ""} |')
        out.append('')
    return '\n'.join(out)



def order_sections(group: list[dict], esc) -> list[str]:
    """One section per issuer (its slug and name); a joint order is listed under its first issuer and again under each
    co-issuer, there marked "joint with <first issuer>" and named by the co-issuer's own number and alias id."""
    by: dict[str, list] = {}
    for r in group:
        by.setdefault(r.get('issuer', ''), []).append((r, None))
        for j in r.get('joint') or []:
            if j.get('issuer') and j['issuer'] != r.get('issuer'):
                by.setdefault(j['issuer'], []).append((r, j))
    out = []
    for iss in sorted(by):
        items = by[iss]
        name = ISSUER_NAMES.get(iss, '')
        out += [f'### `{iss}`' + (f': {esc(name)}' if name else '') + f' ({len(items)})', '',
                '| Act | Folder | Status | Versions | From | Latest |', '| --- | --- | --- | ---: | --- | --- |']
        for r, j in sorted(items, key=lambda x: (x[0]['year'], _num((x[1] or {}).get('nr') or x[0]['number']),
                                                 x[0]['slug'])):
            title = esc(r['title'])
            if j:
                title = f'{title} (joint with `{r.get("issuer")}`; this issuer\'s number {j.get("nr", "")}' + (
                    f', id `{j["alias"]}`' if j.get('alias') else '') + ')'
            elif r.get('joint'):
                title += ' (joint with ' + ', '.join(f'`{x["issuer"]}`' for x in r['joint'] if x.get('issuer')) + ')'
            out.append(f'| {title} | [`{r["path"]}/`]({r["path"]}/) | {r["status"]} | {r["versions"]} | '
                       f'{r["from"]} | {r["latest"]} |')
        out.append('')
    return out


def local_sections(group: list[dict], esc) -> list[str]:
    """One section per council (its folder and name), its decisions by year and number."""
    by: dict[str, list] = {}
    for r in group:
        by.setdefault(r.get('council', ''), []).append(r)
    out = []
    for c in sorted(by):
        items = by[c]
        name = next((r.get('council_name') for r in items if r.get('council_name')), '')
        out += [f'### `local/{c}/`' + (f': {esc(name)}' if name else '') + f' ({len(items)})', '',
                '| Act | Folder | Status | Versions | From | Latest |', '| --- | --- | --- | ---: | --- | --- |']
        for r in items:
            out.append(f'| {esc(r["title"])} | [`{r["path"]}/`]({r["path"]}/) | {r["status"]} | {r["versions"]} | '
                       f'{r["from"]} | {r["latest"]} |')
        out.append('')
    return out


def move(repo: Path, when: int) -> str:
    """Append the layout commit to main: rename every act folder on main from its slug to its official identifier."""
    git = lambda *a: subprocess.run(['git', *a], cwd=repo, capture_output=True, text=True, encoding='utf-8',  # noqa: E731
                                    check=True).stdout
    if paths_at(repo, 'main'):
        raise SystemExit('main already has data/paths.json: the layout move is done')
    vj = json.loads(git('show', 'main:data/versions.json'))
    top = set(git('ls-tree', '--name-only', 'main').split())
    # Only acts whose folder is on main move; an act whose folder a correction removed (withdrawn) gets no path.
    c = {'country': {'code': vj.get('country', 'RO')}, 'acts': [a for a in vj['acts'] if a['slug'] in top]}
    assign(c, {})
    head = git('rev-parse', 'main').strip()
    ct = max(int(git('log', '-1', '--format=%ct', 'main').strip()), when)
    moves = [(a['slug'], a['path']) for a in c['acts'] if a['slug'] in top]
    since = __import__('datetime').datetime.fromtimestamp(ct, __import__('datetime').timezone.utc).strftime('%Y-%m-%d')
    msg = (f'Layout: every act in a folder named by its official identifier\n\n'
           f'Each act moves from a folder named by its id (legea-31-1990/) to <kind>/<year>/<number>/ (lege/1990/31/).\n'
           f'No text changes. Act ids, tags and history are unchanged; before this commit the folders have their old\n'
           f'names (git log --follow, or tools/on.py, which reads both). data/paths.json maps every id to its folder.\n\n'
           f'Kind: layout\nMoved: {len(moves)} acts\nPaths: data/paths.json\n')
    pj = paths_json(c, since).encode('utf-8')
    m = msg.encode('utf-8')
    who = 'Lexifina <romania-law@lexifina.com>'
    body = (f'commit refs/heads/main\nauthor {who} {ct} +0000\ncommitter {who} {ct} +0000\n'.encode('utf-8')
            + f'data {len(m)}\n'.encode() + m + b'\n' + f'from {head}\n'.encode())
    for old, new in moves:
        body += f'R "{old}" "{new}"\n'.encode('utf-8')
    body += f'M 100644 inline data/paths.json\ndata {len(pj)}\n'.encode() + pj + b'\n' + b'done\n'
    p = subprocess.run(['git', 'fast-import', '--quiet', '--done', '--date-format=raw'], cwd=repo, input=body,
                       capture_output=True)
    if p.returncode:
        raise SystemExit(f'fast-import failed: {p.stderr.decode("utf-8", "replace")[-800:]}')
    subprocess.run(['git', '-c', 'checkout.workers=0', 'checkout', '-q', '-f', 'main'], cwd=repo, check=True)
    return git('rev-parse', 'main').strip()


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'move':
        when = int(sys.argv[sys.argv.index('--when') + 1]) if '--when' in sys.argv else int(__import__('time').time())
        print(move(Path(sys.argv[2]), when))
    else:
        sys.exit(__doc__)
