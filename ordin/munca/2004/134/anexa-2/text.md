# Anexa nr. 2
Anexa 2 (Anexa nr. 1.4 la norme) Modalități de transmitere pe cale electronică a Declarațiilor privind evidenta nominală a asiguraților și a obligațiilor de plată către bugetul asigurărilor sociale Condiții generale Declarațiile privind evidența nominală a asiguraților și a obligațiilor de plată către bugetul asigurărilor sociale se vor face numai pe suport electronic. Declarațiile în format electronic se depun odată cu declarațiile nominale pe suport de hârtie (ANEXA 1.1, ANEXA 1.2 listate la calculator, semnate și ștampilate), la Casa Teritorială de Pensii pe raza căreia se află sediul sau domiciliul angajatorului. Condiții tehnice standard pentru formatul electronic Declarațiile în format electronic vor fi transmise numai pe suport tip: dischetă FD 3,5" Microsoft DOS sau CD+ROM, în dublu exemplar. Suporturile vor fi etichetate cu informațiile următoare: - denumire fișier; - Codul unic de înregistrare sau codul fiscal al angajatorului, după caz; - numărul suportului magnetic în cadrul setului de suporturi ex:l/3, 2/3, 3/3, dacă setul are 3 suporturi. Suportul magnetic va conține două fișiere de tip DBF sau TXT, (înregistrări de lungime fixă) pentru fiecare tip de declarație, care va avea în mod obligatoriu următoarele denumiri și conținut: All.DBF sau All.TXT - (ANEXA 1.1) conține datele aferente asiguraților A12.DBF sau A12.TXT - (ANEXA 1.2) conține datele totalizatoare ale fișierului All.DBF sau All.TXT Ordinea câmpurilor din structura fișierelor este obligatorie, indiferent dacă acestea se completează sau nu și sunt de lungime fixă. În descrierea de mai jos "Tip câmp " are următoarea semnificație: N - numeric, aliniat la dreapta C - caracter (alfanumeric), aliniat la stânga, fără:,:,",,..(semne diacritice). În situația transmiterii fișierelor tip DBF se va respecta obligatoriu denumirea câmpurilor date în structurile de fișier. Descrierea organizării înregistrărilor din fișiere: Fișierul All.DBF sau All.TXT (ANEXA 1.1) conține câte o înregistrare pentru fiecare asigurat și are următoarea structură:
Denumire
câmp
Tip
câmp
Lung.
Explicații
Anul
AN
N
4
Se completează cu anul
pentru care se întocmește
declarația
Luna
LN
N
2
Se completează cu luna
anului pentru care se în-
tocmește declarația
Codul unic de în-
registrare (CUI)/
CF pentru angaja-
tori persoane ju-
ridice
CF
N
10
Se completează partea nu-
merică a codului unic de
înregistrare/codului fis-
cal atribuit angajatorilor
- persoane juridice
Cod județ din Nr.
de înmatriculare
în Registrul Co-
merțului
RJ
C
3
Conține primele trei ca-
ractere din numărul de în-
matriculare în registrul
comerțului al angajatoru-
lui
Nr. de înregis-
trare din Regis-
trul Comerțului
RN
N
5
Conține caracterele 4-8
din numărul de înmatricu-
lare în registrul comerțu-
lui al angajatorului (nr.
în RC)
Anul din Nr. de
înmatriculare în
Registrul Comer-
țului
RA
N
4
Conține ultimele patru
caractere din numărul de
înmatriculare în regis-
trul comerțului al anga-
jatorului
Nume și prenume
asigurat
NUME
C
29
Conține numele și prenu-
mele asiguratului
Cod asigurat
CNP
N
13
Conține codul numeric
personal al asiguratului
Contract indivi-
dual de muncă
CM
N
1
Se completează cu:
1 pentru asigurații cu
contract de muncă cu nor-
mă întreagă,
0 în rest
Contract indivi-
dual de muncă cu
timp parțial
CV
N
1
Se completează cu:
1 pentru codificări ante-
rioare
2 pentru asigurații care
lucrează cu contract de
muncă cu timp parțial, 2
ore pe zi;
3 pentru asigurații care
lucrează cu contract de
muncă cu timp parțial, 3
ore pe zi;
4 pentru asigurații care
lucrează cu contract de
muncă cu timp parțial, 4
ore pe zi;
5 pentru asigurații care
lucrează cu contract de
muncă cu timp parțial, 5
ore pe zi;
6 pentru asigurații care
lucrează cu contract de
muncă cu timp parțial, 6
ore pe zi;
7 pentru asigurații care
lucrează cu contract de
muncă cu timp parțial, 7
ore pe zi;
0 în rest
câmpurile TT, NN, DD, SS, PR
Pensionar
PE
N
1
Se completează cu:
1 pentru codificări ante-
rioare
2 pentru pensionarii care
lucrează cu contract de
muncă cu timp parțial, 2
ore pe zi;
3 pentru pensionarii care
lucrează cu contract de
muncă cu timp parțial, 3
ore pe zi;
4 pentru pensionarii care
lucrează cu contract de
muncă cu timp parțial, 4
ore pe zi;
5 pentru pensionarii care
lucrează cu contract de
muncă cu timp parțial, 5
ore pe zi;
6 pentru pensionarii care
lucrează cu contract de
muncă cu timp parțial, 6
ore pe zi;
7 pentru pensionarii care
lucrează cu contract de
muncă cu timp parțial, 7
ore pe zi;
8 pentru pensionarii care
lucrează cu contract de
muncă cu timp parțial, 8
ore pe zi;
0 în rest
Șomer
SOM
N
1
Se completează numai de
ANOFM/AJOFM cu:
1 pentru beneficiarii de
ajutor de șomaj;
2 pentru beneficiarii de
alocație de sprijin;
3 pentru beneficiarii de
plăți compensatorii;
4 pentru alte beneficii
suportate din fondul de
șomaj, potrivit legii;
0 în rest
Total zile
lucrate
TT
N
2
Conține suma zilelor lu-
crate și a zilelor în care
asiguratul a beneficiat de
prestații de asigurări
sociale, inclusiv zilele
nelucrate plătite din fon-
dul de salarii și pentru
care se achită contribuție
de asigurări sociale, care
nu poate fi mai mare decât
numărul de zile lucrătoare
din lună stabilit conform
Legii nr. 53/2003 (Codul
muncii)
Zile lucrate în
condiții normale
NN
N
2
Conține număr zile lu-
crate de asigurat în con-
diții normale de muncă
Zile lucrate în
condiții deosebi-
te
DD
N
2
Conține număr zile lu-
crate de asigurat în con-
diții deosebite de muncă
Zile lucrate în
condiții speciale
SS
N
2
Conține număr zile lu-
crate de asigurat în con-
diții speciale de muncă
Total zile pres-
tații
PP
N
2
Conține numărul total de
zile în care asiguratul a
beneficiat de prestații de
asigurări sociale (numă-
rul total zile lucrătoare
aferente prestației acor-
date, inclusiv cele în
condiții deosebite)
câmpurile TT, NN, DD, SS, PR
Total venit rea-
lizat de asigurat
TV
N
10
Conține venitul total
realizat de asigurat
Venit realizat
de asigurat în
condiții normale
TVN
N
10
Conține venitul realizat
de asigurat în condiții
normale de muncă
Venit realizat
de asigurat în
condiții deosebite
TVD
N
10
Conține venitul realizat
de asigurat în condiții
deosebite de muncă
Venit realizat
de asigurat în
condiții speciale
TVS
N
10
Conține venitul realizat
de asigurat în condiții
speciale de muncă
CAS datorat de
asigurat
CASAT
N
9
Conține Contribuția de
asigurări sociale reținută
de la asigurat
Total prestații
de asigurări
sociale
CASTOT
N
9
Conține cuantumul aferent
prestațiilor de asigurări
sociale, exclusiv ajutorul
de deces
Prestații supor-
tate din BASS
BASS
N
9
Conține cuantumul aferent
prestațiilor de asigurări
sociale suportat din Buge-
tul asigurărilor sociale
de stat, exclusiv ajutorul
de deces
Cod unic de în-
registrare (CUI)
angajator per-
soane fizice
CNPA
N
13
Conține Codul unic de în-
registrare atribuit prin
Certificatul de înregis-
trare angajatorilor per-
soane fizice și care re-
prezintă codul numeric
personal al angajatorului
Norma zilnică de
lucru
NORMA
N
1
Se completează cu progra-
mul normal de lucru spe-
cific locului de muncă al
asiguratului, exprimat în
ore. Prin program normal
de lucru se înțelege pro-
gramul prevăzut la art.109
alin.(1) din Legea 53/2003
sau programul normal de
de lucru sub 8 ore stabi-
lit cu respectarea preve-
derilor Legii 31/1991 sau
alin.(2) din art. 109 din
Codul Muncii.
Norma zilnică poate să fie
de 8, 7 sau 6 ore.
Tipul declarației
TIPD
C
1
Se completează cu R pentru
declarația rectificativă,
spațiu în rest
Declarația rectificativă
se completează astfel:
a. anexa a11 se completea-
ză numai pentru pozi-
țiile modificate față
de declarația inițială
(înregistrarile cu mo-
dificări față de decla-
rația inițială, înre-
gistrări noi față de
declarația inițială)
b. anexa a12 se recalcu-
lează, ținând cont de
modificările efectuate
față de declarația
inițială.
Tip rectificare
TIPR
C
1
Se completează cu urmă-
toarele caractere:
M - modificare sume, zile,
CNP sau nume asigurat pen-
tru asigurații raportați
anterior,
A - adăugare asigurat nou
S - ștergere asigurat
existent în declarația
anterioară
Nume înainte de
rectificare
NUMEANT
C
29
Nume înainte de rectifica-
re, se completează numai
dacă se modifică numele
(TIPR=M), spațiu în rest
CNP înainte de
rectificare
CNPANT
N
13
CNP înainte de rectifica-
re, se completează numai
dacă se modifică CNP-ul
(TIPR+M), 0 în rest
Fișierul A12.DBF sau A12.TXT (ANEXA 1.2) conține o singură înregistrare cu date centralizatoare referitoare la obligațiile de plată ale angajatorului și are următoarea structura:
Denumire
câmp
Tip
câmp
Lung.
Explicații
Anul
AN
N
4
Se completează cu anul
pentru care se întocmește
declarația
Luna
LN
N
2
Se completează cu luna
anului pentru care se în-
tocmește declarația
Ziua lichidării
drepturilor sala-
riale
DCZZ
N
2
Se completează cu ziua
lichidării drepturilor
salariale
Luna lichidării
drepturilor sala-
riale
DCLL
N
2
Se completează cu luna
lichidării drepturilor
salariale
Anul lichidării
drepturilor sala-
riale
DCAA
N
4
Se completează cu anul
lichidării drepturilor
salariale
Denumire angaja-
torului
DEN
C
29
Conține denumirea angaja-
torului
Codul unic de în-
registrare (CUI)/
CF pentru angaja-
tori persoane ju-
ridice
CF
N
10
Se completează partea nu-
merică a codului unic de
înregistrare/codului fis-
cal atribuit angajatorilor
- persoane juridice
Cod județ din Nr.
de înmatriculare
în Registrul Co-
merțului
RJ
C
3
Conține primele trei ca-
ractere din numărul de în-
matriculare în registrul
comerțului al angajatoru-
lui
Nr. de înregis-
trare din Regis-
trul Comerțului
RN
N
5
Conține caracterele 4-8
din numărul de înmatricu-
lare în registrul comerțu-
lui al angajatorului (nr.
în RC)
Anul din Nr. de
înmatriculare în
Registrul Comer-
țului
RA
N
4
Conține ultimele patru
caractere din numărul de
înmatriculare în regis-
trul comerțului al anga-
jatorului
Număr mediu
NRM
N
8.2
Numărul mediu de asigurați
se calculează cu 2 zeci-
male prin rotunjire mate-
matică. Lungimea câmpului
este 8.2 (5 cifre partea
întreagă, respectiv 2
cifre partea zecimală)
Ex.: dacă din calcul re-
zultă 10,172895, atunci
numărul mediu de asigurați
este 10,17;
Dacă din calcul rezultă
10,175110, atunci numărul
mediu de asigurați este
10,18
Notații: A=Norma zilnică l B=Norma zilnică 2 C=Norma zilnică 3 Σ (Suma) se calculează după număr zile lucrate.
Formula pentru calculul numărului mediu de asigurați este:
NRM =[Σ (Nr. asigurați cu contract de muncă cu normă întreagă* A * Zile
lucrate) + Σ (Nr. Asigurați cu contract de muncă cu timp parțial * 2 ore *
Zile lucrate)+...... + Σ (Nr. Asigurați cu contract de muncă cu timp
parțial * 7 ore * Nr. Zile lucrate)] /(Zile lucrătoare din lună * A)] +
[Σ (Nr. asigurați cu contract de muncă cu normă întreagă*B * Zile lucrate)+
Σ (Nr. Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile
lucrate)+......+ Σ (Nr. Asigurați cu contract de muncă cu timp parțial *
6 ore * Zile lucrate)] /(Nr. Zile lucrătoare din lună * B)+
[Σ (Nr. asigurați cu contract de muncă cu normă întreagă*C * Zile lucrate)+
Σ (Nr. Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile
lucrate)+......+ Σ (Nr. Asigurați cu contract de muncă cu timp parțial *
5 ore * Zile lucrate)] /(Zile lucrătoare din lună * C)
Norma zilnică poate să fie de 8, 7 sau 6 ore (câmpul NORMA).
Ex.: Norma 1=8 ore Norma 2 = 7 ore O firmă are 9 angajați în luna martie 2003, din care: - cu norma l 3 angajați lucrează 21 zile l angajat lucrează 10 zile și 11 zile este în concediu medical l angajat lucrează 21 zile cu contract de muncă cu timp parțial 3 ore l angajat lucrează 18 zile cu contract de muncă cu timp parțial 2 ore - cu norma 2 l angajat lucrează 21 zile l angajat lucrează 15 zile și 6 zile este în concediu medical l angajat lucrează 21 zile cu contract de muncă cu timp parțial 4 ore NRM=[(((3*8*21)+(1*8*10)+(1*3*21)+(l*2*18))/(21*8))+ (((1*7*21)+(1*7*15)+(1*4*21))/(21*7))] = 6.35 Rotunjirea aritmetică se efectuează la rezultatul final.
Total fond sala-
rii realizate
FS
N
13
Conține total fond de sa-
larii brute realizate pe
unitate
Total salarii
brute realizate
în condiții nor-
male de muncă
FSN
N
13
Conține total salarii
brute realizate în condi-
ții normale de muncă
Total salarii
brute realizate
în condiții deo-
sebite de muncă
FSD
N
13
Conține total salarii
brute realizate în condi-
ții deosebite de muncă
Total salarii
brute realizate
în condiții spe-
ciale de muncă
FSS
N
13
Conține total salarii
brute realizate în condi-
ții speciale de muncă
Total contribuții
individuale de
asigurări sociale
de virat
CASS
N
13
Conține total Contribuție
individuală de asigurări
sociale de virat
Total CAS datorat
de angajator
CASAN
N
13
Conține total Contribuție
de asigurări sociale da-
torate de angajator
Total cuantum
prestații de asi-
gurări sociale de
suportat din BASS
BASS
N
13
Conține total cuantum
prestații de asigurări
sociale de suportat din
Bugetul asigurărilor so-
ciale de stat, inclusiv
ajutorul de deces
CASS conform art.
54 din OUG nr.
150 / 2002
CASS145
N
13
Conține Contribuția de
asigurări de sănătate afe-
rente Concediilor medicale
conform art. 54 alin. 2
din OUG nr. 150/2002
Total CAS anga-
jator de virat
CASVIR
N
13
Conține total CAS anga-
jator de virat
Formula de calcul pentru
2001-2003:
CASVIR=CASS+CASAN-BASS-
CASS145
Formula de calcul pentru
2004:
CASVIR=CASAN-CASS145-BASS
Număr total de
file de la ANEXA
1.1
NRF
N
3
Conține număr file de la
ANEXA 1.1
Banca
B1
C
16
Filiala
F1
C
16
Cont
C1
C
35
Banca
B2
C
16
Filiala
F2
C
16
Cont
C2
C
35
Banca
B3
C
16
Filiala
F3
C
16
Cont
C3
C
35
Banca
B4
C
16
Filiala
F4
C
16
Cont
C4
C
35
Codul unic de în-
registrare (CUI)/
CF pentru angaja-
tori persoane ju-
ridice
CNPA
N
13
Conține Codul unic de în-
registrare atribuit prin
Certificatul de inregis-
trare angajatorilor per-
soane fizice și care re-
prezintă codul numeric
personal al angajatorului
Contribuție asi-
gurări pentru ac-
cidente de muncă
și boli profesio-
nale (art. 140
Legea 346/2002)
CAAMBP
N
13
Conține contribuție asigu-
rări pentru accidente de
muncă și boli profesionale
(art. 140 Legea 346/2002),
calculat la total fond sa-
larii brute(din anexa nr.
1.2)
Localitatea(oras,
comună)
A_LOCA
C
21
Adresa sediu angajator -
localitate (oraș sau
comună)
- se completează obliga-
toriu
Strada (strada,
satul)
A_STR
C
21
Adresa sediu angajator -
strada sau sat
- dacă se completează
orașul, se completează
obligatoriu și strada
Număr
A_NR
C
7
Adresa sediu angajator -
număr
Bloc
A_BL
C
5
Adresa sediu angajator -
bloc
Scara
A_SC
C
4
Adresa sediu angajator -
scara
Etaj
A_ET
C
2
Adresa sediu angajator -
etaj
Apartament
A_AP
C
4
Adresa sediu angajator -
apartament
Telefon
TELEFON
N
10
Telefon de legătură an-
gajator
Județ
A_JUD
C
3
Adresa sediu angajator -
Cod județ
- se completează obliga-
toriu(*
Sector
A_SECT
N
2
Adresa sediu angajator -
sector (numai pentru
București)
E-mail
E_MAIL
C
45
Adresa e-mail angajator
Tipul declarației
TIPD
C
1
Se completează cu R pentru
declarația rectificativă,
spațiu în rest.
Declarația rectificativă
pentru anexa a12 se com-
pletează astfel:
- se recalculează a12 ți-
nând cont de modificările
efectuate în anexa a11
față de declarația ini-
țială.
Nr. cazuri indem-
nizație pentru
incapacitate tem-
porară de muncă
NRCAZB
N
5
Nr. total cazuri indemni-
zație pentru incapacitate
temporară de muncă la
nivel de unitate
Nr. cazuri acci-
dente de muncă
și boli profesi-
onale
NRCAZA
N
5
Nr. total cazuri accidente
de muncă și boli profesi-
onale la nivel de unitate
Nr. cazuri preve-
nire îmbolnăviri
NRCAZP
N
5
Nr. total cazuri preveni-
re îmbolnăviri la nivel de
unitate = suma de cazuri
de:
- trecere temporară în
altă muncă
- reducerea timpului de
muncă
- carantina
Nr. cazuri sar-
cină și lăuzie
NRCAZL
N
5
Nr. total cazuri sarcina
și lăuzie la nivel de
unitate
Nr. cazuri în-
grijire copil
bolnav
NRCAZI
N
5
Nr. total cazuri îngrijire
copil bolnav la nivel de
unitate
Nr. cazuri creș-
tere copil până
la 2 ani/3 ani
NRCAZC
N
5
Nr. total cazuri creștere
copil până la 2 ani/3 ani
la nivel de unitate
Nr. cazuri aju-
toare de deces
NRCAZD
N
5
Nr. total cazuri ajutoare
de deces la nivel de
unitate
Nr. cazuri în-
demnizație de
risc maternal
NRCAZR
N
5
Nr. total cazuri indemni-
zație de risc maternal la
nivel de unitate
Nr. total zile
prestații indem-
nizație pentru
incapacitate tem-
porară de muncă
NRPPB
N
6
Nr. total zile lucrătoare
indemnizație pentru inca-
pacitate temporară de mun-
că la nivel de unitate din
certificatele medicale
Nr. total zile
prestații acci-
dente de muncă
și boli profesio-
nale
NRPPA
N
6
Nr. total zile lucrătoare
prestații accidente de
muncă și boli profesionale
la nivel de unitate din
certificatele medicale
Nr. total zile
prestații preve-
nire îmbolnăviri
NRPPP
N
6
Nr. total zile lucrătoare
prestații prevenire îm-
bolnăviri la nivel de
unitate din certificatele
medicale
Nr. total zile
prestații sarcină
și lăuzie
NRPPL
N
6
Nr. total zile lucrătoare
prestații sarcină și
lăuzie la nivel de
unitate din certificatele
medicale
Nr. total zile
prestații îngri-
jire copil bolnav
NRPPI
N
6
Nr. total zile lucrătoare
prestații îngrijire co-
pil bolnav la nivel de
unitate din certificatele
medicale
Nr. total zile
prestații creș-
tere copil până
la 2 ani/3 ani
NRPPP
N
6
Nr. total zile lucrătoare
prestații creștere copil
până la 2 ani/3 ani
la nivel de unitate
Nr. total zile
prestații indem-
nizație de risc
maternal
NRPPR
N
6
Nr. total zile lucrătoare
prestații indemnizații
de risc maternal la nivel
de unitate din certifica-
tele medicale
Suma prestații
pentru indemniza-
ție pentru inca-
pacitate tempora-
ră de muncă
SUMAB
N
12
Suma prestații indemniza-
ție pentru incapacitate
temporară de muncă la
nivel de unitate suportate
din BASS
Suma prestații
pentru accidente
de muncă și boli
profesionale
SUMAA
N
12
Suma prestații pentru ac-
cidente de muncă și boli
profesionale la nivel de
unitate suportate din BASS
Suma prestații
pentru prevenire
îmbolnăviri
SUMAP
N
12
Suma prestații pentru pre-
venire îmbolnăviri la ni-
vel de unitate suportate
din BASS
Suma prestații
pentru sarcină
și lăuzie
SUMAL
N
12
Suma prestații pentru sar-
cină și lăuzie la nivel
de unitate suportate din
BASS
Suma prestații
pentru îngrijire
copil bolnav
SUMAI
N
12
Suma prestații pentru în-
grijire copil bolnav la
nivel de unitate suportate
din BASS
Suma prestații
pentru creștere
copil până la 2
ani/3 ani
SUMAC
N
12
Suma prestații pentru
creștere copil până la 2
ani/3 ani la nivel de uni-
tate suportate din BASS
Suma ajutoare
de deces
SUMAD
N
12
Suma totală ajutoare de
deces la nivel de unitate
suportate din BASS
Suma prestații
pentru indemni-
zație de risc
maternal
SUMAR
N
12
Suma prestații pentru în-
demnizație de risc mater-
nal la nivel de unitate
suportate din BASS
Total PP din all = NRPPB+ NRPPA+ NRPPP+ NRPPL+ NRPPI+ NRPPC+ NRPPR
Total BASS din all = SUMAB+SUMAA+SUMAP+SUMAL+SUMAI+SUMAC+ SUMAR
BASS din a12 = SUMAB+SUMAA+SUMAP+SUMAL+SUMAI+SUMAC+ SUMAD+SUMAR
versiunea anterioară a programului)
*Codurile de județe
Cod județ
Denumire județ
011
Alba
021
Arad
031
Argeș
041
Bacău
051
Bihor
061
Bistrița
071
Botoșani
081
Brașov
091
Brăila
101
Buzău
111
Caraș Severin
121
Cluj
131
Constanța
141
Covasna
151
Dâmbovița
161
Dolj
171
Galați
181
Gorj
191
Harghita
201
Hunedoara
211
Ialomița
221
Iași
231
Giurgiu
241
Maramureș
251
Mehedinți
261
Mureș
271
Neamț
281
Olt
291
Prahova
301
Satu Mare
311
Sălaj
321
Sibiu
331
Suceava
341
Teleorman
351
Timiș
361
Tulcea
371
Vaslui
381
Vâlcea
391
Vrancea
401
Călărași
411
București
471
Ilfov
-----------
