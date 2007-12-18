# Anexa 4
CONDIȚII pentru transmiterea fișelor fiscale pe cale electronică Informațiile din fișele fiscale pot fi transmise fie:
a) în fișier format text ASCII, în care fiecare înregistrare (linie) se termină cu "carriage return" și "linefeed".
Nu se admit în cadrul înregistrărilor (liniilor) diacritice (caractere românești) și caractere de control, cu excepția celor menționate anterior. Separatorul dintre câmpuri va fi virgula, iar delimitatorul câmpurilor de tip caracter (alfanumeric) va fi #.
b) în fișier format DBF - DataBaseFile (dbase, Fox, Visual Fox etc).
Ordinea câmpurilor din structura fișierului este obligatorie, indiferent dacă acestea se completează sau nu. Fișierul (text sau DBF) va avea obligatoriu denumirea 210_2008_CIF (unde CIF = cod de identificare fiscală angajator) și va conține: - o înregistrare (linie) cu datele de identificare ale angajatorului; - câte o înregistrare (linie) pentru fiecare angajat care a obținut venituri din salarii la funcția de bază sau în afara funcției de bază. Înregistrările fișierului vor avea următoarea structură:
Câmp
Tip
Lungime
maximă
Explicație
TIP
Numeric
1
Se completează cu:
0 pentru datele angajatorului
1 pentru angajat cu venituri la funcția de bază
2 pentru angajat cu venituri în afara funcției de
bază
COD
Numeric
13
Se completează codul de identificare fiscală al
angajatorului (pentru TIP=0) sau al
angajatului (pentru TIP=1 sau 2)
DENUMIRE
Character
70
Se completează denumirea angajatorului
(pentru TIP=0) sau numele și prenumele
angajatului (pentru TIP=1 sau 2)
ADRESA
Character
100
Se completează adresa angajatorului
(pentru TIP=0) sau a angajatului (pentru
TIP=1 sau 2)
RECTIF
Character
1
Se completează cu X, dacă este fișă fiscală
rectificativă
MISDIPL
Character
1
Se completează cu X, dacă angajatul a fost trimis
în cursul anului în misiune permanentă în
străinătate
TV1
Character
1
Se completează cu X, în funcție de tipul
venitului, numai pentru TIP=2
TV2
Character
1
Se completează cu X, în funcție de tipul
venitului, numai pentru TIP=2
TV3
Character
1
Se completează cu X, în funcție de tipul
venitului, numai pentru TIP=2
TV4
Character
1
Se completează cu X, în funcție de tipul
venitului, numai pentru TIP=2
TV5
Character
1
Se completează cu X, în funcție de tipul
venitului, numai pentru TIP=2
TV6
Character
1
Se completează cu X, în funcție de tipul
venitului, numai pentru TIP=2
TV7
Character
1
Se completează cu X, în funcție de tipul
venitului, numai pentru TIP=2
DATA_ANGAJ
Date
8
Se completează, dacă angajarea a avut loc în
timpul anului fiscal de referință, în
formatul ZZ/LL/AAAA
DATA_INCET
Date
8
Se completează, dacă încetarea activității a avut
loc în timpul anului fiscal de referință, în
formatul ZZ/LL/AAAA
CNP_1
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 1
L1_1
Character
1
Se completează cu X pentru luna 1 pentru
persoana 1
L2_1
Character
1
Se completează cu X pentru luna 2 pentru
persoana 1
L3_1
Character
1
Se completează cu X pentru luna 3 pentru
persoana 1
L4_1
Character
1
Se completează cu X pentru luna 4 pentru
persoana 1
L5_1
Character
1
Se completează cu X pentru luna 5 pentru
persoana 1
L6_1
Character
1
Se completează cu X pentru luna 6 pentru
persoana 1
L7_1
Character
1
Se completează cu X pentru luna 7 pentru
persoana 1
L8_1
Character
1
Se completează cu X pentru luna 8 pentru
persoana 1
L9_1
Character
1
Se completează cu X pentru luna 9 pentru
persoana 1
L10_1
Character
1
Se completează cu X pentru luna 10 pentru
persoana 1
L11_1
Character
1
Se completează cu X pentru luna 11 pentru
persoana 1
L12_1
Character
1
Se completează cu X pentru luna 12 pentru
persoana 1
CNP_2
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 2
L1_2
Character
1
Se completează cu X pentru luna 1 pentru
persoana 2
L2_2
Character
1
Se completează cu X pentru luna 2 pentru
persoana 2
L3_2
Character
1
Se completează cu X pentru luna 3 pentru
persoana 2
L4_2
Character
1
Se completează cu X pentru luna 4 pentru
persoana 2
L5_2
Character
1
Se completează cu X pentru luna 5 pentru
persoana 2
L6_2
Character
1
Se completează cu X pentru luna 6 pentru
persoana 2
L7_2
Character
1
Se completează cu X pentru luna 7 pentru
persoana 2
L8_2
Character
1
Se completează cu X pentru luna 8 pentru
persoana 2
L9_2
Character
1
Se completează cu X pentru luna 9 pentru
persoana 2
L10_2
Character
1
Se completează cu X pentru luna 10 pentru
persoana 2
L11_2
Character
1
Se completează cu X pentru luna 11 pentru
persoana 2
L12_2
Character
1
Se completează cu X pentru luna 12 pentru
persoana 2
CNP_3
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 3
L1_3
Character
1
Se completează cu X pentru luna 1 pentru
persoana 3
L2_3
Character
1
Se completează cu X pentru luna 2 pentru
persoana 3
L3_3
Character
1
Se completează cu X pentru luna 3 pentru
persoana 3
L4_3
Character
1
Se completează cu X pentru luna 4 pentru
persoana 3
L5_3
Character
1
Se completează cu X pentru luna 5 pentru
persoana 3
L6_3
Character
1
Se completează cu X pentru luna 6 pentru
persoana 3
L7_3
Character
1
Se completează cu X pentru luna 7 pentru
persoana 3
L8_3
Character
1
Se completează cu X pentru luna 8 pentru
persoana 3
L9_3
Character
1
Se completează cu X pentru luna 9 pentru
persoana 3
L10_3
Character
1
Se completează cu X pentru luna 10 pentru
persoana 3
L11_3
Character
1
Se completează cu X pentru luna 11 pentru
persoana 3
L12_3
Character
1
Se completează cu X pentru luna 12 pentru
persoana 3
CNP_4
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 4
L1_4
Character
1
Se completează cu X pentru luna 1 pentru
persoana 4
L2_4
Character
1
Se completează cu X pentru luna 2 pentru
persoana 4
L3_4
Character
1
Se completează cu X pentru luna 3 pentru
persoana 4
L4_4
Character
1
Se completează cu X pentru luna 4 pentru
persoana 4
L5_4
Character
1
Se completează cu X pentru luna 5 pentru
persoana 4
L6_4
Character
1
Se completează cu X pentru luna 6 pentru
persoana 4
L7_4
Character
1
Se completează cu X pentru luna 7 pentru
persoana 4
L8_4
Character
1
Se completează cu X pentru luna 8 pentru
persoana 4
L9_4
Character
1
Se completează cu X pentru luna 9 pentru
persoana 4
L10_4
Character
1
Se completează cu X pentru luna 10 pentru
persoana 4
L11_4
Character
1
Se completează cu X pentru luna 11 pentru
persoana 4
L12_4
Character
1
Se completează cu X pentru luna 12 pentru
persoana 4
CNP_5
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 5
L1_5
Character
1
Se completează cu X pentru luna 1 pentru
persoana 5
L2_5
Character
1
Se completează cu X pentru luna 2 pentru
persoana 5
L3_5
Character
1
Se completează cu X pentru luna 3 pentru
persoana 5
L4_5
Character
1
Se completează cu X pentru luna 4 pentru
persoana 5
L5_5
Character
1
Se completează cu X pentru luna 5 pentru
persoana 5
L6_5
Character
1
Se completează cu X pentru luna 6 pentru
persoana 5
L7_5
Character
1
Se completează cu X pentru luna 7 pentru
persoana 5
L8_5
Character
1
Se completează cu X pentru luna 8 pentru
persoana 5
L9_5
Character
1
Se completează cu X pentru luna 9 pentru
persoana 5
L10_5
Character
1
Se completează cu X pentru luna 10 pentru
persoana 5
L11_5
Character
1
Se completează cu X pentru luna 11 pentru
persoana 5
L12_5
Character
1
Se completează cu X pentru luna 12 pentru
persoana 5
CNP_6
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 6
L1_6
Character
1
Se completează cu X pentru luna 1 pentru
persoana 6
L2_6
Character
1
Se completează cu X pentru luna 2 pentru
persoana 6
L3_6
Character
1
Se completează cu X pentru luna 3 pentru
persoana 6
L4_6
Character
1
Se completează cu X pentru luna 4 pentru
persoana 6
L5_6
Character
1
Se completează cu X pentru luna 5 pentru
persoana 6
L6_6
Character
1
Se completează cu X pentru luna 6 pentru
persoana 6
L7_6
Character
1
Se completează cu X pentru luna 7 pentru
persoana 6
L8_6
Character
1
Se completează cu X pentru luna 8 pentru
persoana 6
L9_6
Character
1
Se completează cu X pentru luna 9 pentru
persoana 6
L10_6
Character
1
Se completează cu X pentru luna 10 pentru
persoana 6
L11_6
Character
1
Se completează cu X pentru luna 11 pentru
persoana 6
L12_6
Character
1
Se completează cu X pentru luna 12 pentru
persoana 6
CNP_7
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 7
L1_7
Character
1
Se completează cu X pentru luna 1 pentru
persoana 7
L2_7
Character
1
Se completează cu X pentru luna 2 pentru
persoana 7
L3_7
Character
1
Se completează cu X pentru luna 3 pentru
persoana 7
L4_7
Character
1
Se completează cu X pentru luna 4 pentru
persoana 7
L5_7
Character
1
Se completează cu X pentru luna 5 pentru
persoana 7
L6_7
Character
1
Se completează cu X pentru luna 6 pentru
persoana 7
L7_7
Character
1
Se completează cu X pentru luna 7 pentru
persoana 7
L8_7
Character
1
Se completează cu X pentru luna 8 pentru
persoana 7
L9_7
Character
1
Se completează cu X pentru luna 9 pentru
persoana 7
L10_7
Character
1
Se completează cu X pentru luna 10 pentru
persoana 7
L11_7
Character
1
Se completează cu X pentru luna 11 pentru
persoana 7
L12_7
Character
1
Se completează cu X pentru luna 12 pentru
persoana 7
CNP_8
Numeric
13
Se completează codul de identificare fiscală al
persoanei în întreținere 8
L1_8
Character
1
Se completează cu X pentru luna 1 pentru
persoana 8
L2_8
Character
1
Se completează cu X pentru luna 2 pentru
persoana 8
L3_8
Character
1
Se completează cu X pentru luna 3 pentru
persoana 8
L4_8
Character
1
Se completează cu X pentru luna 4 pentru
persoana 8
L5_8
Character
1
Se completează cu X pentru luna 5 pentru
persoana 8
L6_8
Character
1
Se completează cu X pentru luna 6 pentru
persoana 8
L7_8
Character
1
Se completează cu X pentru luna 7 pentru
persoana 8
L8_8
Character
1
Se completează cu X pentru luna 8 pentru
persoana 8
L9_8
Character
1
Se completează cu X pentru luna 9 pentru
persoana 8
L10_8
Character
1
Se completează cu X pentru luna 10 pentru
persoana 8
L11_8
Character
1
Se completează cu X pentru luna 11 pentru
persoana 8
L12_8
Character
1
Se completează cu X pentru luna 12 pentru
persoana 8
VBRUT_1
Numeric
10
Venit brut pentru luna 1
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
Venit bază de calcul pentru luna 1
IMPOZIT_1
Numeric
10
Impozit calculat și reținut pentru luna 1
VBRUT_2
Numeric
10
Venit brut pentru luna 2
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
Venit bază de calcul pentru luna 2
IMPOZIT_2
Numeric
10
Impozit calculat și reținut pentru luna 2
VBRUT_3
Numeric
10
Venit brut pentru luna 3
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
Venit bază de calcul pentru luna 3
IMPOZIT_3
Numeric
10
Impozit calculat și reținut pentru luna 3
VBRUT_4
Numeric
10
Venit brut pentru luna 4
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
Venit bază de calcul pentru luna 4
IMPOZIT_4
Numeric
10
Impozit calculat și reținut pentru luna 4
VBRUT_5
Numeric
10
Venit brut pentru luna 5
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
Venit bază de calcul pentru luna 5
IMPOZIT_5
Numeric
10
Impozit calculat și reținut pentru luna 5
VBRUT_6
Numeric
10
Venit brut pentru luna 6
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
Venit bază de calcul pentru luna 6
IMPOZIT_6
Numeric
10
Impozit calculat și reținut pentru luna 6
VBRUT_7
Numeric
10
Venit brut pentru luna 7
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
Venit bază de calcul pentru luna 7
IMPOZIT_7
Numeric
10
Impozit calculat și reținut pentru luna 7
VBRUT_8
Numeric
10
Venit brut pentru luna 8
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
Venit bază de calcul pentru luna 8
IMPOZIT_8
Numeric
10
Impozit calculat și reținut pentru luna 8
VBRUT_9
Numeric
10
Venit brut pentru luna 9
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
Venit bază de calcul pentru luna 9
IMPOZIT_9
Numeric
10
Impozit calculat și reținut pentru luna 9
VBRUT_10
Numeric
10
Venit brut pentru luna 10
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
Venit bază de calcul pentru luna 10
IMPOZIT_10
Numeric
10
Impozit calculat și reținut pentru luna 10
VBRUT_11
Numeric
10
Venit brut pentru luna 11
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
Venit bază de calcul pentru luna 11
IMPOZIT_11
Numeric
10
Impozit calculat și reținut pentru luna 11
VBRUT_12
Numeric
10
Venit brut pentru luna 12
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
Venit bază de calcul pentru luna 12
IMPOZIT_12
Numeric
10
Impozit calculat și reținut pentru luna 12
VBRUT_13
Numeric
10
Venit brut anual
IMPOZIT_13
Numeric
10
Impozit anual
DEDU_13
Numeric
10
Deduceri personale anuale
ALTDED_13
Numeric
10
Alte deduceri anuale
VENIT_13
Numeric
10
Venit bază de calcul anual
