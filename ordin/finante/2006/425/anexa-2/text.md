# Anexa nr. 2
Anexa II ──────── (anexa nr. IV la Ordinul nr. 546/2005) ────────────────────────────────────── CONDIȚIILE pentru transmiterea fișelor fiscale pe cale electronică Informațiile din fisele fiscale pot fi transmise fie:
a) în fisier format text ASCII, în care fiecare înregistrare (linie) se termina cu "carriage return" și "linefeed".
Nu se admit în cadrul înregistrărilor (liniilor) diacritice (caractere românești) și caractere de control, cu excepția celor menționate anterior. Separatorul dintre campuri va fi virgula, iar delimitatorul campurilor de tip caracter (alfanumeric) va fi #.
b) în fisier format DBF - DataBaseFile (dbase, Fox, Visual Fox, etc).
Ordinea campurilor din structura fisierului este obligatorie, indiferent dacă acestea se completeaza sau nu. Fisierul (text sau DBF) va avea obligatoriu denumirea 210_2006_CIF (unde CIF=cod de identificare fiscala angajator) și va contine: - o înregistrare (linie) cu datele de identificare ale angajatorului - cate o înregistrare (linie) pentru fiecare angajat care a obținut venituri din salarii la functia de baza sau în afara functiei de baza Inregistrarile fisierului vor avea urmatoarea structura:
Camp
Tip
Lung.
max.
Explicatie
TIP
Numeric
1
se completeaza cu:
0 pentru datele angajatorului
1 pentru angajat cu venituri la
functia de baza
2 pentru angajat cu venituri în
afara functiei de baza
COD
Numeric
13
Se completeaza codul de identificare
fiscala al angajatorului (pentru
TIP=0) sau al angajatului (pentru
TIP=1 sau 2)
DENUMIRE
Character
70
se completeaza denumirea angajatorului
(pentru TIP=0) sau numele și prenumele
angajatului (pentru TIP=1 sau 2)
ADRESA
Character
100
se completeaza adresa angajatorului
(pentru TIP=0) sau a angajatului(pentru
TIP=1 sau 2)
RECTIF
Character
1
se completeaza cu X, dacă este fisa
fiscala rectificativa
MISDIPL
Character
1
se completeaza cu X, dacă angajatul a
fost trimis în cursul anului în misiune
permanenta în strainatate
TV1
Character
1
se completeaza cu X, în functie de tipul
venitului, numai pentru TIP=2
TV2
Character
1
se completeaza cu X, în functie de tipul
venitului, numai pentru TIP=2
TV3
Character
1
se completeaza cu X, în functie de tipul
venitului, numai pentru TIP=2
TV4
Character
1
se completeaza cu X, în functie de tipul
venitului, numai pentru TIP=2
TV5
Character
1
se completeaza cu X, în functie de tipul
venitului, numai pentru TIP=2
TV6
Character
1
se completeaza cu X, în functie de tipul
venitului, numai pentru TIP=2
TV7
Character
1
se completeaza cu X, în functie de tipul
venitului, numai pentru TIP=2
DATA_ANGAJ
Date
8
se completeaza, dacă angajarea a avut
loc în timpul anului fiscal de referința
în formatul ZZ/LL/AAAA
DATA_INCET
Date
8
se completeaza, dacă încetarea activi-
tatii a avut loc în timpul anului fiscal
de referința, în formatul ZZ/LL/AAAA
CNP_1
Numeric
13
Se completeaza codul de identificare
fiscala al persoanei în întreținere 1
L1_1
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 1
L2_1
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 1
L3_1
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 1
L4_1
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 1
L5_1
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 1
L6_1
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 1
L7_1
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 1
L8_1
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 1
L9_1
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 1
L10_1
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 1
L11_1
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 1
L12_1
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 1
CNP_2
Numeric
13
Se completeaza codul de identificare
fiscala al persoanei în întreținere 2
L1_2
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 2
L2_2
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 2
L3_2
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 2
L4_2
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 2
L5_2
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 2
L6_2
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 2
L7_2
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 2
L8_2
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 2
L9_2
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 2
L10_2
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 2
L11_2
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 2
L12_2
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 2
CNP_3
Numeric
13
Se completeaza codul de identificare
fiscala al persoanei în întreținere 3
L1_3
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 3
L2_3
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 3
L3_3
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 3
L4_3
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 3
L5_3
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 3
L6_3
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 3
L7_3
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 3
L8_3
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 3
L9_3
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 3
L10_3
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 3
L11_3
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 3
L12_3
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 3
CNP_4
Numeric
13
Se completeaza codul de identificare
fiscala al persoanei în întreținere 4
L1_4
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 4
L2_4
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 4
L3_4
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 4
L4_4
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 4
L5_4
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 4
L6_4
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 4
L7_4
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 4
L8_4
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 4
L9_4
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 4
L10_4
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 4
L11_4
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 4
L12_4
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 4
CNP_5
Numeric
13
Se completeaza codul de identificare
fiscala al persoanei în întreținere 5
L1_5
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 5
L2_5
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 5
L3_5
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 5
L4_5
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 5
L5_5
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 5
L6_5
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 5
L7_5
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 5
L8_5
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 5
L9_5
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 5
L10_5
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 5
L11_5
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 5
L12_5
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 5
CNP_6
Numeric
13
Se completeaza codul de identificare
fiscala al persoanei în întreținere 6
L1_6
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 6
L2_6
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 6
L3_6
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 6
L4_6
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 6
L5_6
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 6
L6_6
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 6
L7_6
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 6
L8_6
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 6
L9_6
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 6
L10_6
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 6
L11_6
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 6
L12_6
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 6
CNP_7
Numeric
13
Se completeaza codul de identificare
fiscala al persoanei în întreținere 7
L1_7
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 7
L2_7
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 7
L3_7
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 7
L4_7
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 7
L5_7
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 7
L6_7
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 7
L7_7
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 7
L8_7
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 7
L9_7
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 7
L10_7
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 7
L11_7
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 7
L12_7
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 7
CNP_8
Numeric
13
Se completeaza codul ele identificare
fiscala al persoanei în întreținere 8
L1_8
Character
1
Se completeaza cu X pentru luna 1 pentru
persoana 8
L2_8
Character
1
Se completeaza cu X pentru luna 2 pentru
persoana 8
L3_8
Character
1
Se completeaza cu X pentru luna 3 pentru
persoana 8
L4_8
Character
1
Se completeaza cu X pentru luna 4 pentru
persoana 8
L5_8
Character
1
Se completeaza cu X pentru luna 5 pentru
persoana 8
L6_8
Character
1
Se completeaza cu X pentru luna 6 pentru
persoana 8
L7_8
Character
1
Se completeaza cu X pentru luna 7 pentru
persoana 8
L8_8
Character
1
Se completeaza cu X pentru luna 8 pentru
persoana 8
L9_8
Character
1
Se completeaza cu X pentru luna 9 pentru
persoana 8
L10_8
Character
1
Se completeaza cu X pentru luna 10
pentru persoana 8
L11_8
Character
1
Se completeaza cu X pentru luna 11
pentru persoana 8
L12_8
Character
1
Se completeaza cu X pentru luna 12
pentru persoana 8
DEDU_1
Numeric
10
Deduceri personale pentru luna 1
ALTDED_1
Numeric
10
Alte deduceri pentru luna 1
VENIT_1
Numeric
10
Venit baza de calcul pentru luna 1
IMPOZIT_1
Numeric
10
Impozit calculat și retinut pentru
luna 1
DEDU_2
Numeric
10
Deduceri personale pentru luna 2
ALTDED_2
Numeric
10
Alte deduceri pentru luna 2
VENIT_2
Numeric
10
Venit baza de calcul pentru luna 2
IMPOZIT_2
Numeric
10
Impozit calculat și retinut pentru
luna 2
DEDU_3
Numeric
10
Deduceri personale pentru luna 3
ALTDED_3
Numeric
10
Alte deduceri pentru luna 3
VENIT_3
Numeric
10
Venit baza de calcul pentru luna 3
IMPOZIT_3
Numeric
10
Impozit calculat și retinut pentru
luna 3
DEDU_4
Numeric
10
Deduceri personale pentru luna 4
ALTDED_4
Numeric
10
Alte deduceri pentru luna 4
VENIT_4
Numeric
10
Venit baza de calcul pentru luna 4
IMPOZIT_4
Numeric
10
Impozit calculat și retinut pentru
luna 4
DEDU_5
Numeric
10
Deduceri personale pentru luna 5
ALTDED_5
Numeric
10
Alte deduceri pentru luna 5
VENIT_5
Numeric
10
Venit baza de calcul pentru luna 5
IMPOZIT_5
Numeric
10
Impozit calculat și retinut pentru
luna 5
DEDU_6
Numeric
10
Deduceri personale pentru luna 6
ALTDED_6
Numeric
10
Alte deduceri pentru luna 6
VENIT_6
Numeric
10
Venit baza de calcul pentru luna 6
IMPOZIT_6
Numeric
10
Impozit calculat și retinut pentru
luna 6
DEDU_7
Numeric
10
Deduceri personale pentru luna 7
ALTDED_7
Numeric
10
Alte deduceri pentru luna 7
VENIT_7
Numeric
10
Venit baza de calcul pentru luna 7
IMPOZIT_7
Numeric
10
Impozit calculat și retinut pentru
luna 7
DEDU_8
Numeric
10
Deduceri personale pentru luna 8
ALTDED_8
Numeric
10
Alte deduceri pentru luna 8
VENIT_8
Numeric
10
Venit baza de calcul pentru luna 8
IMPOZIT_8
Numeric
10
Impozit calculat și retinut pentru
luna 8
DEDU_9
Numeric
10
Deduceri personale pentru luna 9
ALTDED_9
Numeric
10
Alte deduceri pentru luna 9
VENIT_9
Numeric
10
Venit baza de calcul pentru luna 9
IMPOZIT_9
Numeric
10
Impozit calculat și retinut pentru
luna 9
DEDU_10
Numeric
10
Deduceri personale pentru luna 10
ALTDED_10
Numeric
10
Alte deduceri pentru luna 10
VENIT_10
Numeric
10
Venit baza de calcul pentru luna 10
IMPOZIT_10
Numeric
10
Impozit calculat și retinut pentru
luna 10
DEDU_11
Numeric
10
Deduceri personale pentru luna 11
ALTDED_11
Numeric
10
Alte deduceri pentru luna 11
VENIT_11
Numeric
10
Venit baza de calcul pentru luna 11
IMPOZIT_11
Numeric
10
Impozit calculat și retinut pentru
luna 11
DEDU_12
Numeric
10
Deduceri personale pentru luna 12
ALTDED_12
Numeric
10
Alte deduceri pentru luna 12
VENIT_12
Numeric
10
Venit baza de calcul pentru luna 12
IMPOZIT_12
Numeric
10
Impozit calculat și retinut pentru
luna 12
IMPOZ1T_13
Numeric
10
Impozit anual
BURSA_PL
Numeric
10
Bursa plătită
BURSA_AD
Numeric
10
Bursa admisa la restituire
______________
