32001R2163
8.11.2001
JURNALUL OFICIAL AL COMUNITĂȚILOR EUROPENE
L 291/13
REGULAMENTUL (CE) NR. 2163/2001 AL COMISIEI
din 7 noiembrie 2001
privind modalitățile tehnice de transmitere a datelor, în vederea stabilirii statisticilor de transport rutier
de mărfuri
(Text cu relevanță pentru SEE)
COMISIA COMUNITĂȚILOR EUROPENE,
având în vedere Tratatul de instituire a Comunității Europene,
având în vedere Regulamentul (CE) nr. 1172/98 al Consiliului din
25 mai 1998 privind raportările statistice cu privire la transpor-
turile rutiere de mărfuri (1), astfel cum a fost modificat prin Regu-
lamentul (CE) nr. 2691/1999 al Comisiei (2), în special articolul 5
alineatul (2) și articolul 9,
întrucât:
(1)
În conformitate cu articolul 5 alineatul (2) din Regulamen-
tul (CE) nr. 1172/98, Comisia adoptă modalitățile de trans-
mitere a datelor de către statele membre.
(2)
Trebuie să se specifice cu suficiente detalii formatul în care
datele trebuie transmise la Eurostat, în scopul garantării
unei procesări rapide a datelor la cel mai bun cost.
(3)
Prezentul regulament nu modifică nimic în statutul
variabilelor considerate facultative din Regulamentul (CE)
nr. 1172/98.
(4)
Măsurile definite prin prezentul regulament sunt conforme
cu avizul Comitetului programului statistic instituit prin
Decizia nr. 89/382/CEE, Euratom a Consiliului (3).
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Formatul tehnic pentru transmiterea datelor către Comisie
(Eurostat) este definit în anexa la prezentul regulament.
Statele membre utilizează acest format pentru datele privind anul
de referință 2002 și următorii ani.
Articolul 2
Statele membre transmit Comisiei (Eurostat) datele și metadatele
solicitate prin prezentul regulament, în format electronic, cu
respectarea unui standard de schimb propus de Comisie
(Eurostat).
Articolul 3
Prezentul regulament intră în vigoare în cea de-a douăzecea zi de
la publicarea în Jurnalul Oficial al Comunităților Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele
membre.
Adoptat la Bruxelles, 7 noiembrie 2001.
Pentru Comisie
Pedro SOLBES MIRA
Membru al Comisiei
(1)
JO L 163, 6.6.1998, p. 1.
(2)
JO L 326, 18.12.1999, p. 39.
(3)
JO L 181, 28.6.1989, p. 47.
124
RO
Jurnalul Oficial al Uniunii Europene
07/vol. 8

ANEXĂ
MODALITĂȚI TEHNICE DE TRANSMITERE A DATELOR
1.
STRUCTURA DATELOR
Datele individuale trimestriale de transmis la Eurostat se repartizează în trei seturi cu legătură între ele și acoperă:
A1 variabilele referitoare la vehicule;
A2 variabilele referitoare la parcursuri;
A3 variabilele referitoare la mărfuri (în cadrul operațiunii elementare de transport).
Fiecare „înregistrare de vehicul” din ansamblul A1 are legătură cu una sau mai multe „înregistrări de parcursuri”
(ansamblul A2), conținând informații asupra parcursurilor efectuate de vehicul pe durata perioadei de anchetă (în
general o săptămână). La rândul său, fiecare înregistrare a unui parcurs echivalează cu zero, una sau mai multe
„înregistrări de mărfuri” (ansamblul A3), cuprinzând date despre operațiunile elementare de transport, care
constituie parcursul total.
Figura 1 ilustrează structura datelor.
Trebuie observat că nu există întotdeauna mai multe înregistrări de mărfuri pentru fiecare înregistrare de parcurs.
În ceea ce privește parcursurile sub sarcină este posibil să nu existe decât o singură înregistrare de mărfuri la o
înregistrare de parcurs.
Aceasta depinde de metoda utilizată pentru înregistrarea parcursurilor și/sau de tipul de parcurs. În cazul
parcursurilor fără sarcină nu există, de obicei, nici o înregistrare de mărfuri (deși este posibil să se lege o operațiune
de transport fără sarcină și un parcurs fără sarcină).
„Apendicele metodologic” din anexa A la Regulamentul (CE) nr. 1172/98 furnizează informații mai detaliate.
2.
LISTA CÂMPURILOR
Pentru fiecare câmp se furnizează informațiile următoare:
— numărul câmpului: identifică poziția câmpului în cadrul înregistrării;
— variabila: fie referința la variabila Regulamentului (CE) nr. 1172/98, fie identificatorul său intern;
07/vol. 8
RO
Jurnalul Oficial al Uniunii Europene
125

— descrierea: scurtă descriere a conținutului câmpului;
— codificarea: variabilele trebuie să fie codificate conform dispozițiilor din anexele A – G la Regulamentul (CE)
nr. 1172/98. Aici se definesc regulile de codificare suplimentare. Eurostat poate furniza recomandări și
explicații suplimentare în materie de codificare, în cadrul manualului de referință privind aplicarea
Regulamentului (CE) nr. 1172/98;
— tipul câmpului: arată dacă în câmp există informații numerice sau textuale;
— cu excepția variabilei A1.9 toate câmpurile numerice vor conține un număr întreg;
— în cazul variabilei A1.9 pentru separarea zecimalelor se utilizează virgula („,”), ca separator zecimal;
— variabila facultativă: indică dacă variabila este facultativă, în temeiul anexei A la Regulamentul (CE)
nr. 1172/98;
— lungimea maximă: lungimea maximă prevăzută pentru datele din acest câmp. Datele care sunt prea lungi nu
pot fi încărcate;
— câmpul-cheie: combinarea valorilor câmpurilor-cheie ale unui set de date trebuie să permită realizarea unei
valori-cheie unice, în cadrul setului de date respectiv. Prezența a două valori-cheie identice blochează
încărcarea setului de date și a seturilor de care sunt legate deoarece legăturile dintre înregistrările vehiculului,
ale parcursurilor și ale mărfurilor nu pot fi stabilite corect.
Setul de date A1: Variabilele vehiculului
Numărul
câmpului
Variabila
Descrierea
Codificarea
Tipul
câmpului
* = Variabila
facultativă
Lungimea
maximă
* = câmpul
cheie
Coduri specifice
ale valorilor lipsă
1
RCount
Țara declarantă
(1)
Text
2
*
2
DSetID
Identificarea setului de date
A1
Text
2
*
3
Year
Anul setului de date
4 cifre
Text
4
*
4
Quarter
Trimestrul setului de date
Q1, Q2, Q3 sau Q4
Text
2
*
5
QuestN
Identificarea chestionarului
Text
9
*
6
A1.1
Posibilitatea de a utiliza
vehiculul pentru efectuarea
de transporturi combinate
De elaborat
Text
*
1
7
A1.3
Vârsta
autovehiculului
rutier (camion sau tractor
rutier)
Anii scurși de la prima
înmatriculare
Numeric
2
99
8
A1.6
Clasa de activitate NACE
(Revizia 1) a operatorului
vehiculului
Nivel NACE patru cifre
Text
*
5
9
A1.8.1
Total kilometri parcurși pe
durata perioadei anchetei –
sub sarcină
km
Numeric
4
(1) Această variabilă se codifică prin intermediul codurilor țărilor definite în anexa G la Regulamentul (CE) nr. 1172/98.
126
RO
Jurnalul Oficial al Uniunii Europene
07/vol. 8

Numărul
câmpului
Variabila
Descrierea
Codificarea
Tipul
câmpului
* = Variabila
facultativă
Lungimea
maximă
* = câmpul
cheie
Coduri specifice
ale valorilor lipsă
10
A1.8.2
Total kilometri parcurși pe
durata
perioadei
de
anchetă
–
fără
sarcină
(inclusiv
parcursul
tractoarelor
rutiere
fără
semiremorcă)
km
Numeric
*
4
11
A1.9
Ponderarea vehiculului, de
utilizat pentru elaborarea
rezultatelor complete pe
baza datelor elementare,
dacă informațiile se colec-
tează prin sondaj
Numeric
8
12
Stratum
Stratul eșantionului căruia
îi aparține vehiculul
Text
7
13
A2 link
Numărul de înregistrări A2
corespunzătoare
Numeric
Numeric
5
Setul de date A2: Variabilele parcursului
Numărul
câmpului
Variabila
Descrierea
Codificarea
Tipul
câmpului
* = variabila
facultativă
Lungimea
maximă
* = câmpul
cheie
Coduri specifice
ale valorilor lipsă
1
RCount
Țara declarantă
(1)
Text
2
*
2
DSetID
Identificarea setului de date
A2
Text
2
*
3
Year
Anul setului de date
patru cifre
Text
4
*
4
Quarter
Trimestrul setului de date
Q1, Q2, Q3 sau Q4
Text
2
*
5
QuestN
Identificarea chestionarului
Text
9
*
6
JournN
Identificarea parcursului
Text
5
*
7
A1.2
Configurația osiilor
Anexa B la Regula-
mentul
(CE)
nr. 1172/98
Text
*
3
8
A1.4
Greutatea maximă permisă
sub sarcină
100 kg
Numeric
4
9
A1.5
Sarcina utilă
100 kg
Numeric
4
(1) Această variabilă se codifică prin intermediul codurilor țărilor definite în anexa G la Regulamentul (CE) nr. 1172/98.
07/vol. 8
RO
Jurnalul Oficial al Uniunii Europene
127

Numărul
câmpului
Variabila
Descrierea
Codificarea
Tipul
câmpului
* = variabila
facultativă
Lungimea
maximă
* = câmpul
cheie
Coduri specifice
ale valorilor lipsă
10
A1.7
Tipul transportului
Anexa A la Regula-
mentul
(CE)
nr. 1172/98
Text
1
9
11
A2.1
Tipul parcursului
Anexa C la Regula-
mentul
(CE)
nr. 1172/98
Text
1
12
A2.2
Greutatea mărfii
Greutatea
brută
la
100 kg
Numeric
4
13
A2.3
Locul de încărcare (a auto-
vehiculului rutier pentru
transportul de mărfuri la
un parcurs sub sarcină)
(1)
Text
5
XX
14
A2.4
Locul
de
descărcare
(al
autovehiculului rutier pen-
tru transportul de mărfuri
la un parcurs sub sarcină)
(1)
Text
5
XX
15
A2.5
Distanța parcursă: distanța
reală, cu excepția distanței
parcurse
în
timp
ce
vehiculul este transportat
de
un
alt
mijloc
de
transport
km
Numeric
4
16
A2.6
Tone-km
realizate
pe
durata parcursului
tone-km
Numeric
8
17
A2.7
Țări traversate în tranzit
(maximum cinci)
(1)
Text
10
18
A2.8
Dacă este cazul, locul de
încărcare a autovehiculului
rutier pe un alt mijloc de
transport
(1)
Text
*
5
XX
19
A2.9
Dacă este cazul, locul de
descărcare a autovehiculu-
lui rutier de pe un alt mij-
loc de transport
(1)
Text
*
5
XX
20
A2.10
Gradul de încărcare a vehi-
culului
(din
punct
de
vedere al volumului maxim
al
spațiului
utilizat
pe
durata parcursului)
Text
*
1
9
21
A3 link
Numărul înregistrărilor A3
corespunzătoare
Numeric
8
(1) Această variabilă se codifică potrivit regulilor din anexa G la Regulamentul (CE) nr. 1172/98.
128
RO
Jurnalul Oficial al Uniunii Europene
07/vol. 8

Setul de date A3: Variabilele mărfii (în cadrul operației elementare de transport)
Numărul
câmpului
Variabila
Descrierea
Codificarea
Tipul
câmpului
* = variabila
facultativă
Lungimea
maximă
* = câmpul
cheie
Coduri specifice
ale valorilor lipsă
1
RCount
Țara declarantă
(1)
Text
2
*
2
DSetID
Identificarea setului de date
A3
Text
2
*
3
Year
Anul setului de date
patru cifre
Text
4
*
4
Quarter
Trimestrul setului de date
Q1, Q2, Q3 sau Q4
Text
2
*
5
QuestN
Identificarea chestionarului
Text
9
*
6
JournN
Identificarea parcursului
Text
4
*
7
GoodsN
Identificarea operațiunii în
funcție de marfă
Text
6
*
8
A3.1
Tipul mărfii transportate
conform
grupelor
de
mărfuri care se referă la o
clasificare adecvată
Anexa D la Regula-
mentul
(CE)
nr. 1172/98 (NST/R)
Text
2
9
A3.2
Greutatea mărfii
Greutatea
brută
la
100 kg
Numeric
4
10
A3.3
Nomenclatorul mărfurilor
periculoase
Anexa E la Regulamen-
tul (CE) nr. 1172/98
(principalele categorii
ale
Directivei
94/55/CE)
Text
3
11
A3.4
Tipul ambalajului
Anexa F la Regulamen-
tul (CE) nr. 1172/98
(nivelul
1
al
recomandării
ONU
nr. 21)
Text
*
1
12
A3.5
Locul de încărcare a mărfii
(2)
Text
5
XX
13
A3.6
Locul de descărcare a măr-
fii
(2)
Text
5
XX
(1) Această variabilă se codifică prin intermediul codurilor țărilor definite în anexa G la Regulamentul (CE) nr. 1172/98.
(2) Această variabilă se codifică potrivit regulilor stabilite în anexa G la Regulamentul (CE) nr. 1172/98.
07/vol. 8
RO
Jurnalul Oficial al Uniunii Europene
129

Numărul
câmpului
Variabila
Descrierea
Codificarea
Tipul
câmpului
* = variabila
facultativă
Lungimea
maximă
* = câmpul
cheie
Coduri specifice
ale valorilor lipsă
14
A3.7
Distanța parcursă: distanța
reală, cu excepția distanței
parcurse în timp ce autove-
hiculul
rutier
pentru
transportul mărfurilor este
transportat de un alt mijloc
de transport
km
Numeric
4
3.
DATELE LIPSĂ
Datele lipsă din situații se codifică automat ca un câmp vid (fără date între doi separatori de câmpuri succesive).
Pentru anumite câmpuri, Eurostat poate recomanda utilizarea unor coduri specifice pentru datele lipsă sau alte
date speciale (vezi coloana „Coduri specifice ale valorilor lipsă”).
Informații complementare se găsesc în manualul de referință pentru aplicarea Regulamentului (CE) nr. 1172/98
privind tabelul statistic al transportului rutier de mărfuri.
4.
SCHIMBAREA CONFIGURAȚIEI SAU A TIPULUI DE TRANSPORT
Conform anexei A la Regulamentul (CE) nr. 1172/98, pe durata perioadei de anchetă poate surveni o schimbare
a configurației vehiculului (adăugarea unei remorci, ceea ce modifică configurația osiilor și sarcina utilă) sau a
tipului de transport, în funcție de parcurs. Se recomandă înregistrarea acestor schimbări (chiar dacă nu există nici
o obligație în acest sens).
Pentru a se permite transmiterea acestor date conform structurilor normale definite în cele de față, datele
referitoare la variabilele A1.2, A1.4, A1.5 și A1.7 se transmit în setul A2 (variabilele parcursului).
5.
VALIDAREA DATELOR DE CĂTRE EUROSTAT
Eurostat supune datele transmise de statele membre unor controale de validare, înainte de a le încărca în baza
de date de producție. Dacă un număr semnificativ de înregistrări nu sunt validate, Eurostat le semnalează statului
membru și precizează motivele neacceptării lor. Statul membru este rugat să rectifice erorile semnalate și să
transmită din nou cele trei seturi complete pe trimestrul respectiv (și nu numai înregistrările eronate). Acest lucru
este necesar dacă se dorește garantarea corectitudinii factorilor de ponderare, precum și coerența datelor
referitoare la vehicule, parcursurile efectuate și mărfurile transportate.
Dacă fișierul nu cuprinde decât un număr foarte mic de erori, care nu pot avea decât o incidență minimă asupra
analizelor, Eurostat încarcă înregistrările valide și nu ia în considerare înregistrările eronate. Într-un astfel de caz,
înregistrările care nu satisfac controalele și motivele neacceptării acestora sunt semnalate statului membru în
cauză, care este invitat să corecteze erorile detectate, dacă dorește acest lucru, și să retransmită cele trei seturi
complete pentru trimestrul respectiv (și nu numai înregistrările eronate). În cazul unei retransmiteri a datelor,
Eurostat încarcă datele corectate. În schimb, dacă statul membru preferă să nu retransmită datele, Eurostat
utilizează datele deja acceptate pentru alcătuirea de tabele agregate.
6.
IDENTIFICAREA SETURILOR DE DATE
Denumirea seturilor de date („CCYYQnROADAxZZZ”, conform exigențelor programului Stadium) cuprinde
elementele următoare:
CC
Țara declarantă
YY
Ultimele două cifre ale anului (exemplu:
„01” pentru anul 2001)
130
RO
Jurnalul Oficial al Uniunii Europene
07/vol. 8

Qn
Trimestrul: n = 1 – 4
ROADAx
Identificarea seturilor de date:
A1: date referitoare la vehicul
A2: date referitoare la parcurs
A3: date referitoare la marfă
.ZZZ
Tipul setului de date:
.dat: fișiere individuale
.zip: fișiere comprimate în format Pkzip sau WinZip
Exemple:
1. Setul de date „ES99Q2ROADA1.zip” este un fișier comprimat cu extensie „.zip”, care cuprinde setul de date
A1 al Spaniei pe al doilea trimestru al anului 1999 („ES99Q2ROADA1.dat”).
2. Setul de date „UK99Q3ROADA2.dat” cuprinde datele A2 ale Regatului Unit pe al treilea trimestru al anului
1999.
Denumirea seturilor de date de mai sus trebuie să figureze în câmpul „Obiect” al mesajului electronic.
7.
SUPORTUL TRANSMITERII
Suportul de referință al transmiterii este Stadium. Adresa acestuia este furnizată de Eurostat. Trebuie avut în vedere
că mesajele electronice nu pot depăși o mărime bine definită. În consecință, nu se pot transmite pe această cale
fișiere mari de date.
8.
PERIOADA DE TRANZIȚIE
Pe durata unei perioade de tranziție, datele pot fi transmise și în seturi de date de tip ASCII, cuprinzând câmpuri
cu lungime variabilă. Pentru separarea câmpurilor se utilizează punctul și virgula („;”).
Trebuie să fie prezente toate câmpurile, chiar dacă sunt vide (două separatoare de câmpuri consecutive).
Se ignoră spațiile suplimentare cuprinse în câmpurile de date, cu excepția cazului când există instrucțiuni specifice
referitoare la un câmp care interzic prezența unor spații suplimentare.
În plus, pe durata acestei perioade de tranziție, Eurostat acceptă și dischetele sau CD-urile înregistrabile (CD-R),
care îi sunt expediate. Nu se acceptă benzile magnetice și suporturile de hârtie.
În timpul perioadei de tranziție, diferitele etape ale transmisiei pe cale electronică la Eurostat a seturilor de date
sunt următoarele:
— datele sunt trimise sub formă de seturi de date anexate;
— este posibilă anexarea doar a unui singur set de date pe mesaj;
— denumirea setului de date este menționată în câmpul „Obiect” al mesajului;
— dacă doriți să adăugați comentarii (note metodologice, observații asupra calității datelor etc.), în legătură cu
un set de date anexat la un mesaj electronic, vă recomandăm să faceți acest lucru sub forma unui text în cadrul
mesajului. Nu este permisă utilizarea unui text formatat;
— dacă doriți să faceți comentarii asupra unui set de date care nu este anexat la un mesaj electronic, indicați
referința „CCYYQnROADAx.rem” din câmpul „Obiect” și adăugați observațiile dumneavoastră sub forma
unui text în cadrul mesajului. Nu este permisă utilizarea unui text formatat;
— dacă doriți să corectați un set de date transmis deja la Eurostat, retrimiteți setul complet având corecțiile de
rigoare, sub aceeași denumire, și introduceți o notă explicativă în cadrul mesajului.
07/vol. 8
RO
Jurnalul Oficial al Uniunii Europene
131
