# Anexa nr. 2
Anexa II (Anexa nr. IV la Ordinul nr. 546/2005) CONDIȚII pentru transmiterea fișelor fiscale pe cale electronică Informațiile din fișele fiscale pot fi transmise fie:
a) în fișier format text ASCII, în care fiecare înregistrare (linie) se termină cu "carriage return" și "linefeed".
Nu se admit în cadrul înregistrărilor (liniilor) diacritice (caractere românești) și caractere de control, cu excepția celor menționate anterior. Separatorul dintre câmpuri va fi virgula, iar delimitatorul câmpurilor de tip caracter (alfanumeric) va fi #.
b) în fișier format DBF - DataBaseFile (dbase, Fox, Visual Fox, etc).
Ordinea câmpurilor din structura fișierului este obligatorie, indiferent dacă acestea se completează sau nu. Fișierul (text sau DBF) va avea obligatoriu denumirea 210_2007_CIF (unde CIF=cod de identificare fiscală angajator) și va conține: - o înregistrare (linie) cu datele de identificare ale angajatorului - câte o înregistrare (linie) pentru fiecare angajat care a obținut venituri din salarii la funcția de bază sau în afara funcției de bază. Înregistrările fișierului vor avea următoarea structură:
Den. câmp Tip câmp
Lung.
Explicație max.
-----------------------------------------
TIP
Numeric 1 - se completează cu: 0 pt. înregistrare angajator 1 pt. înregistrare angajat cu ven. la funcția de bază 2 pt. înregistrare angajat cu ven. în afara funcției de bază
COD
Numeric 13 - se completează codul de identificare fiscală al angajatorului (pentru TIP = 0) sau al angajatului (pentru TIP = 1 sau 2)
DENUMIRE
Caracter 70 - se completează denumirea angajatorului (pentru
TIP = 0) sau numele și prenumele angajatului (pentru TIP = 1 sau 2)
ADRESA
Caracter 100 - se completează adresa angajatorului (pentru TIP = 0) sau a angajatului (pentru TIP = 1 sau 2)
RECTIF
Caracter 1 - se completează cu X, dacă este fișă fiscală rectificativă
MISDIPL
Caracter 1 - se completează cu X, dacă angajatul a fost trimis în cursul anului în misiune permanentă în străinătate
TV1
Caracter 1 - se completează cu X, în funcție de tipul venitului, numai pentru TIP = 2
TV2
Caracter 1 - se completează cu X, în funcție de tipul venitului, numai pentru TIP = 2
TV3
Caracter 1 - se completează cu X, în funcție de tipul venitului, numai pentru TIP = 2
TV4
Caracter 1 - se completează cu X, în funcție de tipul venitului, numai pentru TIP = 2
TV5
Caracter 1 - se completează cu X, în funcție de tipul venitului, numai pentru TIP = 2
TV6
Caracter 1 - se completează cu X, în funcție de tipul venitului, numai pentru TIP = 2
TV7
Caracter 1 - se completează cu X, în funcție de tipul venitului, numai pentru TIP = 2
DATA_ANGAJ Date 8 - ZZ/LL/AAAA
DATA_INCET Date 8 - ZZ/LL/AAAA
CNP_1
Numeric 13 - cod de identificare fiscală pers. în întreținere 1
L1_1
Caracter 1 - "X" pt.luna 01 pers. 1
L2_1
Caracter 1 - "X" pt.luna 02 pers. 1
L3_1
Caracter 1 - "X" pt.luna 03 pers. 1
L4_1
Caracter 1 - "X" pt.luna 04 pers. 1
L5_1
Caracter 1 - "X" pt.luna 05 pers. 1
L6_1
Caracter 1 - "X" pt.luna 06 pers. 1
L7_1
Caracter 1 - "X" pt.luna 07 pers. 1
L8_1
Caracter 1 - "X" pt.luna 08 pers. 1
L9_1
Caracter 1 - "X" pt.luna 09 pers. 1
L10_1
Caracter 1 - "X" pt.luna 10 pers. 1
L11_1
Caracter 1 - "X" pt.luna 11 pers. 1
L12_1
Caracter 1 - "X" pt.luna 12 pers. 1...
CNP_8
Numeric 13 - cod de identificare fiscală pers. în întreținere 8
L1_8
Caracter 1 - "X" pt.luna 01 pers. 8
L2_8
Caracter 1 - "X" pt.luna 02 pers. 8
L3_8
Caracter 1 - "X" pt.luna 03 pers. 8
L4_8
Caracter 1 - "X" pt.luna 04 pers. 8
L5_8
Caracter 1 - "X" pt.luna 05 pers. 8
L6_8
Caracter 1 - "X" pt.luna 06 pers. 8
L7_8
Caracter 1 - "X" pt.luna 07 pers. 8
L8_8
Caracter 1 - "X" pt.luna 08 pers. 8
L9_8
Caracter 1 - "X" pt.luna 09 pers. 8
L10_8
Caracter 1 - "X" pt.luna 10 pers. 8
L11_8
Caracter 1 - "X" pt.luna 11 pers. 8
L12_8
Caracter 1 - "X" pt.luna 12 pers. 8
DEDU_1
Numeric 10 - Deduceri personale pentru luna 01
ALTDED_1
Numeric 10 - Alte deduceri pentru luna 01
VENIT_1
Numeric 10 - Venit bază de calcul pentru luna 01
IMPOZIT_1 Numeric 10 - Impozit calculat și reținut pentru luna 01....
DEDU_6
Numeric 10 - Deduceri personale pentru luna 06
ALTDED_6
Numeric 10 - Alte deduceri pentru luna 06
VENIT_6
Numeric 10 - Venit bază de calcul pentru luna 06
IMPOZIT_6 Numeric 10 - Impozit calculat și reținut pentru luna 06....
DEDU_12
Numeric 10 - Deduceri personale pentru luna 12
ALTDED_12 Numeric 10 - Alte deduceri pentru luna 12
VENIT_12
Numeric 10 - Venit bază de calcul pentru luna 12
IMPOZIT_12 Numeric 10 - Impozit calculat și reținut pentru luna 12
VENIT_13
Numeric 10 - Venit anual
IMPOZIT_13 Numeric 10 - Impozit anual
-------
