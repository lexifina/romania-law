# Anexa 4 la normă Raport tranzacționare
NR
Denumire
Format
Descriere
1
Cod tranzacție
4!a
Cod tranzacție conform tabel 1
"Categorii tranzacții și corespon-
dența cu codurile operațiunilor
SaFIR"
2
Cod operațiune
3!n
Cod operațiune, conform regulilor
sistemului SaFIR Anexa 8
3
Ora tranzacției
HHMM
Ora și minutul la care s-a încheiat
tranzacția
4
Data tranzacției
YYYYMMDD
Data la care s-a încheiat tranzacția
5
Data scadenței
YYYYMMDD
Data la care se va iniția decontarea
tranzacției
6
ADEL
YYYYMMDD
Data limită pentru decontarea fon-
durilor pentru tranzacțiile cu
titluri, denominate în valută
7
Identificatorul
emisiuni
e12!c[4*35x]
Cod ISIN
8
Identificator
vânzător
4!a2!a2!c[3!c]
Cod BIC
9
Cont vânzător
4!a1!n
Simbol cont SaFIR
10
Categorie client
2!n
În cazul în care vânzătorul este un
client al intermediarului, conform
tabelului 2 "Clasificare Clienți"
11
Identificator
cumpărător
4!a2!a2!c[3!c]
Cod BIC
12
Cont cumpărător
4!a1!n
Simbol cont SaFIR
13
Categorie client
1!n
În cazul în care cumpărătorul este
un client al intermediarului, con-
form tabelului 2 - "Clasificare
Clienți"
14
Randament
15d
Pentru tranzacțiile LTR se va
specifică rata repo
Pentru tranzacțiile IDR câmpul nu
se va completa
15
Preț net
15d
16
Preț brut
15d
17
Suma de decontat
15d
18
Cod monedă
3!a
Cod monedă în care se efectuează
tranzacția: RON, USD, EUR
19
Contract standardizat
Acronimul contractului standardizat
conform tabelului 3, "Acronim
contract standardizat";
20
Nr. contract
16!a
Numărul contractului; se aplică
pentru tranzacțiile FWT), IDR, LTR,
SBB, PLEX
21
Confirmare
35!a
Câmp descriptiv care descrie modul
în care s-a derulat confirmarea
(tel, postă electronică etc.)
22
Modul de încheiere a
tranzacției
35!a
Câmp descriptiv care precizează
modalitatea de încheiere a tranzac-
ției: telefonic, Reuters, etc.
23
Comentarii
35!a
Câmp descriptiv care poate conține
alte informații
Tabel 1 - Categorii tranzacții raportate și corespondența cu codurile operațiunilor SaFIR
Tip tranzacție
Cod tranzacție
Cod SaFIR
Vânzări - Cumpărări spot
SPOT
802
Vânzări - Cumpărări today
TD
802
Vânzări - Cumpărări tomorrow
TM
802
Vânzări - Cumpărări forward
FWD
802
Repo/Reverse repo în cadrul zilei
primul pas
IDR1
810
Repo/Reverse repo în cadrul zilei
pasul doi
IDR2
813
Repo/Reverse repo pe termen
lung primul pas
LTR1
811
Repo/Reverse repo pe termen
lung pasul doi
LTR2
814
Sell- buyback/buy-sellback
primul pas
SBB1
802
Sell-buyback/buy-sellback pasul
doi
SBB2
802
Executări de gajuri prin vânzare
PLEX
823
Tabel 2 - Clasificare clienți
Categorie
Client:
Subcategorie
Client
Descriere Client
1
Persoane juridice rezidente
11
Companii de asigurare
12
Fonduri de investiții
13
Case de brokeraj
14
ANL
15
Fonduri de garantare
16
Camera de Comerț
17
Companii nefinanciare
18
Burse de Valori
19
Altele
2
Persoane fizice rezidente
3
Persoane juridice ne-rezidente
4
Persoane fizice ne-rezidente
Tabel 3 - Acronim contract standardizat
Contract
Acronim
Exemple
Contract cadru standardizat
propus sau încheiat cu
Banca Națională a României
NBR4!a, unde
4!a: reprezintă codi-
ficarea tranzacției
conform tabelului 1
NBRIDR: contract cadru
aferent tranzacțiilor
repo/reverse repo cu
decontare în aceeași zi
conform Regulamentului nr.
10/2005 privind facilită-
țile acordate de Banca
Națională a României în
scopul fluidizării decon-
tărilor
Contract nestandardizat,
agreat bilateral de
participanții care încheie
tranzacția
4!a: reprezintă codi-
ficarea tranzacției
conform tabelului 1
SBB: contract aferent
tranzacțiilor sell-buyback
/buy-sellback, agreat
bilateral
REPO: contract aferent
tranzacțiilor repo/reverse
repo, agreat bilateral
---------
