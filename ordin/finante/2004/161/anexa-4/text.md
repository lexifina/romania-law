# Anexa 4
CONDIȚII pentru transmiterea fiselor fiscale pe cale electronică Informațiile din fisele fiscale (FF1 și FF2) pot fi transmise fie:
a) în fișiere format text ASCII, în care fiecare înregistrare (linie) se termina cu "carriage return" și "linefeed". Nu se admit în cadrul înregistrărilor (liniilor) diacritice (caractere românești) și caractere de control, cu excepția celor menționate anterior. Separatorul dintre câmpuri va fi virgula, iar delimitatorul câmpurilor de tip caracter (alfanumeric) va fi #.
b) în fișiere format DBF - DataBaseFile (dbase, Fox, Visual Fox, etc).
Ordinea câmpurilor din structura fișierelor este obligatorie, indiferent dacă acestea se completează sau nu. În descrierea de mai jos "Tip câmp" are următoarea semnificație: N numeric C caracter (alfanumeric) D data. Fișierele (text sau DBF) vor avea obligatoriu următoarele denumiri și vor conține:
REP_aaaa TXT sau
REP_aaaa. DBF
date de identificare angajator
FFl_aaaa.TXT sau
FFl_aaaa.DBF
(funcția de baza)
date de identificare angajați, total coeficienți de
deducere, coeficienți de deducere pentru situația proprie
a angajatului, venit net, impozit reținut, impozit pe
veniturile din salarii cu impunere finala, venit scutit,
informații privind operațiunile de
regularizare efectuate
DED_aaaa.TXT sau
DED_aaaa.DBF
date de identificare persoana în întreținere, coeficienți
de deducere suplimentara pentru persoanele aflate în
întreținerea angajaților
FF2_aaaa.TXT sau
FF2_aaaa.DBF
date de identificare angajați, tip venit, venit baza de
calcul, impozit reținut
Unde "aaaa" reprezintă anul fiscal de referința (de ex. REP_2002.TXT, REP_2002.DBF, FF1_2002.TXT, FF1_2002.DBF, DED_2002.TXT, DED_2002.DBF, FF2_2002.TXT, FF2_2002.DBF). REP_aaaa.TXT sau REP_aaaa.DBF va conține o singura înregistrare (linie) cu datele de identificare ale angajatorului în următoarea structura:
Denumire câmp Descriere câmp Tip câmp Lungime maximă Explicații
Cod_ang Cod angajator N 13 - se completează codul de înregistrare fiscală sau codul unic de înregistrare al angajatorului, dacă angajatorul este persoana juridică
- se completează codul numeric personal sau numărul de înregistrare fiscală al angajatorului, dacă angajatorul este persoană fizică
Denumire Denumire/ Nume și Prenume C 160 - se completează denumirea angajatorului persoana juridică sau numele și prenumele angajatorului persoană fizică
Județ Județ/sector C 20 - pentru Municipiul București se completează sectorul
Localitate Localitate C 50
Strada Strada C 50
Nr Număr C 10
Bloc Bloc C 10
Scara Scara C 10
Ap Ap C 10
Cod poștal Cod poștal N 10
Telefon Telefon C 10
Fax Fax C 10
Email E-mail C 50
FF1_aaaa.TXT sau FF1_aaaa.DBF va conține cate o înregistrare (linie) pentru fiecare angajat care a obținut venituri din salarii la funcția de baza, în următoarea structura:
Denumire câmp Descriere câmp Tip câmp Lungime maximă Explicații
Cnp_ang Cod angajat N 13 - se completează codul numeric personal sau numărul de identificare fiscală al angajatului
Nume Nume C 40
Prenume Prenume C 40
Județ Județ/sector C 20 - pentru Municipiul București se completează sectorul
Localitate Localitate C 50
Strada Strada C 50
Nr Număr C 10
Bloc Bloc C 10
Scara Scara C 10
Ap Ap C 10
Cod_poștal Cod poștal N 10
Rectific Fișa fiscală rectificativă C 1 - se completează cu X, dacă este fișa fiscală rectificativă
Nu_plata Nu poate fi efectuată plata/restituirea de către angajator a diferențelor de impozit, înscrise la rd. 10 și 11. Cap. VI, către angajat C 1 - se completează cu X, dacă nu poate fi efectuată plata/restituirea de către angajator a diferențelor de impozit, înscrise la rd. 10 și 11, Cap. VI, către angajat
Pers_mis Personal trimis în misiune permanentă în străinătate C 1 - se completează cu X pentru personalul trimis în misiune permanentă în străinătate
Alte_surse Angajații permanenți care au alte surse de venit ce se cuprind în venitul anual global impozabil sau solicită deduceri potrivit art. 86 alin. (1), altele decât lit. b) și g) din Legea nr. 571/2003 C 1 - se completează cu X pentru Angajații permanenți care au alte surse de venit ce se cuprind în venitul anual global impozabil sau solicită deduceri potrivit art. 86 alin. (1), altele decât lit. b) și g) din Legea nr. 571/2003
Pers_deced Persoana decedată C 1 Persoana decedată
Invalid_I Invalid gr. I, handicap grav C 1 - se completează cu X, în funcție de situația angajatului
Invalid_II Invalid gr. II, handicap accentuat C 1 - se completează cu X, în funcție de situația angajatului
Data_angaj Data angajării D 10 - se completează, dacă angajarea a avut loc în timpul anului fiscal de referință, în formatul ZZ/LL/AAAA
Data_incet Data încetării activității D 10 - se completează, dacă încetarea activității a avut loc în timpul anului fiscal de referință, în formatul ZZ/LL/AAAA
Coef_T_01 Total coeficient de deducere pentru luna Ianuarie N 42 - se completează în formatul 9.99
Coef_T_02 Total coeficient de deducere pentru luna Februarie N 42 - se completează în formatul 9.99
Coef_T_03 Total coeficient de deducere pentru luna Martie N 42 - se completează în formatul 9.99
Coef_T_04 Total coeficient de deducere pentru luna Aprilie N 42 - se completează în formatul 9.99
Coef_T_05 Total coeficient de deducere pentru luna Mai N 42 - se completează în formatul 9.99
Coef_T_06 Total coeficient de deducere pentru luna Iunie N 42 - se completează în formatul 9.99
Coef_T_07 Total coeficient de deducere pentru luna Iulie N 42 - se completează în formatul 9.99
Coef_T_08 Total coeficient de deducere pentru luna August N 42 - se completează în formatul 9.99
Coef_T_09 Total coeficient de deducere pentru luna Septembrie N 42 - se completează în formatul 9.99
Coef_T_10 Total coeficient de deducere pentru luna Octombrie N 42 - se completează în formatul 9.99
Coef_T_11 Total coeficient de deducere pentru luna Noiembrie N 42 - se completează în formatul 9.99
Coef_T_12 Total coeficient de deducere pentru luna Decembrie N 42 - se completează în formatul 9.99
Coef_P_01 Coeficient de deducere personală pentru luna Ianuarie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_02 Coeficient de deducere personală pentru luna Februarie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_03 Coeficient de deducere personală pentru luna Martie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_04 Coeficient de deducere personală pentru luna Aprilie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_05 Coeficient de deducere personală pentru luna Mai N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_06 Coeficient de deducere personală pentru luna Iunie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_07 Coeficient de deducere personală pentru luna Iulie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_08 Coeficient de deducere personală pentru luna August N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_09 Coeficient de deducere personală pentru luna Septembrie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_10 Coeficient de deducere personală pentru luna Octombrie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_11 Coeficient de deducere personală pentru luna Noiembrie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Coef_P_12 Coeficient de deducere personală pentru luna Decembrie N 42 - se completează în funcție de dreptul de deducere și de situația angajatului, în formatul 9.99
Venit_01 Venit net pentru luna Ianuarie N 12 - se completează conform statului de salarii
Impozit_01 Impozit reținut pentru luna Ianuarie N 12 - se completează conform statului de salarii
Venit_02 Venit net pentru luna Februarie N 12 - se completează conform statului de salarii
Impozit_02 Impozit reținut pentru luna Februarie N 12 - se completează conform statului de salarii
Venit_03 Venit net pentru luna Martie N 12 - se completează conform statului de salarii
Impozit_03 Impozit reținut pentru luna Martie N 12 - se completează conform statului de salarii
Venit_04 Venit net pentru luna Aprilie N 12 - se completează conform statului de salarii
Impozit_04 Impozit reținut pentru luna Aprilie N 12 - se completează conform statului de salarii
Venit_05 Venit net pentru luna Mai N 12 - se completează conform statului de salarii
Impozit_05 Impozit reținut pentru luna Mai N 12 - se completează conform statului de salarii
Venit_06 Venit net pentru luna Iunie N 12 - se completează conform statului de salarii
Impozit_06 Impozit reținut pentru luna Iunie N 12 - se completează conform statului de salarii
Venit_07 Venit net pentru luna Iulie N 12 - se completează conform statului de salarii
Impozit_07 Impozit reținut pentru luna Iulie N 12 - se completează conform statului de salarii
Venit_08 Venit net pentru luna August N 12 - se completează conform statului de salarii
Impozit_08 Impozit reținut pentru luna August N 12 - se completează conform statului de salarii
Venit_09 Venit net pentru luna Septembrie N 12 - se completează conform statului de salarii
Impozit_09 Impozit reținut pentru luna Septembrie N 12 - se completează conform statului de salarii
Venit_10 Venit net pentru luna Octombrie N 12 - se completează conform statului de salarii
Impozit_10 Impozit reținut pentru luna Octombrie N 12 - se completează conform statului de salarii
Venit_11 Venit net pentru luna Noiembrie N 12 - se completează conform statului de salarii
Impozit_11 Impozit reținut pentru luna Noiembrie N 12 - se completează conform statului de salarii
Venit_12 Venit net pentru luna Decembrie N 12 - se completează conform statului de salarii
Impozit_12 Impozit reținut pentru luna Decembrie N 12 - se completează conform statului de salarii
Venit_13 Total venit net N 12
Impozit_13 Total impozit reținut N 12
Nr_luni Număr luni pentru care s-au acordat cheltuieli profesionale N 2
Ch_acord Cheltuieli profesionale acordate N 12 - se completează conform statului de salarii
Ct_sind_st Cotizația de sindicat plătită prin reținere pe stat (D1) N 12 - se completează conform statului de salarii
Ct_sind_or Cotizația de sindicat plătită la organizația sindicală (D2) N 12
Ch_cuven Cheltuieli profesionale recalculate N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare
Venit_rec Venit net recalculat N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare
Deduceri Deduceri personale cuvenite N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare
Venit_baza Venit anual baza de calcul N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare
Cotiz_sind Cotizația de sindicat plătită (D1 + D2) N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare și este suma (D1+D2)
Imp_anual Impozit anual N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare
Dif_plata Diferența impozit rămas de achitat de către angajat N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare
Dif_restit Diferența impozit de restituit angajatului N 12 - se completează numai pentru angajații cărora li s-au efectuat operațiunile de regularizare
Venit_fm Venit din salarii cu impunere finală N 12 - se completează numai pentru veniturile din salarii stabilite prin hotărâri judecătorești
Imp_fin Impozit pe venitul din salarii cu impunere finală N 12 - se completează numai pentru veniturile din salarii stabilite prin hotărâri judecătorești
DED_aaaa.TXT sau DED_aaaa.DBF ----------------------------- va conține cate o înregistrare (linie) pentru fiecare persoana aflata în întreținere a unui angajat.
Denumire câmp Descriere câmp Tip câmp Lungime maximă Explicații
Cnp_ang Cod angajat N 13 - se completează codul numeric personal sau numărul de identificare fiscală al angajatului
Cnp_pers Cod persoană în întreținere N 13 - se completează codul numeric personal sau numărul de identificare fiscală al persoanei în întreținere
Nume Nume C 40
Prenume Prenume C 40
Soț Soț/soție C 1 - se completează cu X, în funcție de calitatea persoanei aflate în întreținere
Copil Copil C 1 - se completează cu X, în funcție de calitatea persoanei aflate în întreținere
Alta Alta C 1 - se completează cu X, în funcție de calitatea persoanei aflate în întreținere
Invalid_I Invalid gr I, handicap grav C 1 - se completează cu X, în funcție de situația persoanei aflate în întreținere
Invalid_II Invalid gr II, handicap accentuat C 1 - se completează cu X, în funcție de situația persoanei aflate în întreținere
Coef_01 Coeficient de deducere pentru luna Ianuarie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_02 Coeficient de deducere pentru luna Februarie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_03 Coeficient de deducere pentru luna Martie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_04 Coeficient de deducere pentru luna Aprilie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_05 Coeficient de deducere pentru luna Mai N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_06 Coeficient de deducere pentru luna Iunie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_07 Coeficient de deducere pentru luna Iulie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_08 Coeficient de deducere pentru luna August N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_09 Coeficient de deducere pentru luna Septembrie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_10 Coeficient de deducere pentru luna Octombrie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_11 Coeficient de deducere pentru luna Noiembrie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
Coef_12 Coeficient de deducere pentru luna Decembrie N 42 - se completează în funcție de calitatea și situația persoanei aflate în întreținere, în formatul 9.99
FF2_aaaa.TXT sau FF2_aaaa.DBF ----------------------------- va conține cate o înregistrare (linie) pentru fiecare angajat care obține venituri din salarii altele decât cele de la funcția de baza, în structura următoare:
Denumire câmp Descriere câmp Tip câmp Lungime maximă Explicații
Cnp_ang Cod angajat N 13 - se completează codul numeric personal sau numărul de identificare fiscală al angajatului
Nume Nume C 40
Prenume Prenume C 40
Județ Județ/sector C 20 - pentru Municipiul București se completează sectorul
Localitate Localitate C 50
Strada Strada C 50
Nr Număr C 10
Bloc Bloc C 10
Scara Scara C 10
Ap Ap C 10
Cod_postal Cod poștal N 10
Rectific Fișa fiscală rectificativă C 1 - se completează cu X, dacă este fișa fiscală rectificativă
AS1 AS1 C 1 - se completează cu X, în funcție de tipul venitului
AS2 AS2 C 1 - se completează cu X, în funcție de tipul venitului
AS3 AS3 C 1 - se completează cu X, în funcție de tipul venitului
AS4 AS4 C 1 - se completează cu X, în funcție de tipul venitului
AS5 AS5 C 1 - se completează cu X, în funcție de tipul venitului
AS6 AS6 C 1 - se completează cu X, în funcție de tipul venitului
AS7 AS7 C 1 - se completează cu X, în funcție de tipul venitului
Venit_01 Venit baza de calcul pentru luna Ianuarie N 12 se completează conform statului de salarii
Impozit_01 Impozit reținut pentru luna Ianuarie N 12 se completează conform statului de salarii
Venit_02 Venit baza de calcul pentru luna Februarie N 12 se completează conform statului de salarii
Impozit_02 Impozit reținut pentru luna Februarie N 12 se completează conform statului de salarii
Venit_03 Venit baza de calcul pentru luna Martie N 12 se completează conform statului de salarii
Impozit_03 Impozit reținut pentru luna Martie N 12 se completează conform statului de salarii
Venit_04 Venit baza de calcul pentru luna Aprilie N 12 se completează conform statului de salarii
Impozit_04 Impozit reținut pentru luna Aprilie N 12 se completează conform statului de salarii
Venit_05 Venit baza de calcul pentru luna Mai N 12 se completează conform statului de salarii
Impozit_05 Impozit reținut pentru luna Mai N 12 se completează conform statului de salarii
Venit_06 Venit baza de calcul pentru luna Iunie N 12 se completează conform statului de salarii
Impozit_06 Impozit reținut pentru luna Iunie N 12 se completează conform statului de salarii
Venit_07 Venit baza de calcul pentru luna Iulie N 12 se completează conform statului de salarii
Impozit_07 Impozit reținut pentru luna Iulie N 12 se completează conform statului de salarii
Venit_08 Venit baza de calcul pentru luna August N 12 se completează conform statului de salarii
Impozit_08 Impozit reținut pentru luna August N 12 se completează conform statului de salarii
Venit_09 Venit baza de calcul pentru luna Septembrie N 12 se completează conform statului de salarii
Impozit_09 Impozit reținut pentru luna Septembrie N 12 se completează conform statului de salarii
Venit_10 Venit baza de calcul pentru luna Octombrie N 12 se completează conform statului de salarii
Impozit_10 Impozit reținut pentru luna Octombrie N 12 se completează conform statului de salarii
Venit_11 Venit baza de calcul pentru luna Noiembrie N 12 se completează conform statului de salarii
Impozit_11 Impozit reținut pentru luna Noiembrie N 12 se completează conform statului de salarii
Venit_12 Venit baza de calcul pentru luna Decembrie N 12 se completează conform statului de salarii
Impozit_12 Impozit reținut pentru luna Decembrie N 12 se completează conform statului de salarii
Venit_13 Total venit baza de calcul N 12
Impozit_13 Total impozit reținut N 12
Venit_fin Venit din salarii cu impunere finală N 12 - se completează numai pentru veniturile din salarii stabilite prin hotărâri judecătorești
Imp_fin Impozit pe venitul din salarii cu impunere finală N 12 - se completează numai pentru veniturile din salarii stabilite prin hotărâri judecătorești
