# Anexa IV
INSTRUCȚIUNI pentru transmitere pe cale electronică Transmiterea pe cale electronică a declarațiilor plătitorilor de venit privitoare la beneficiarii de venit, cod 208, 209, 210, 211, 212 și 213 1. Condiții generale Declarațiile plătitorilor de venit privitoare la peste douăzeci de persoane fizice beneficiare de venit se vor depune numai în format electronic. În această categorie intra declarațiile cod 208, 209, 210, 211, 212 și 213. Declarațiile în format electronic ale plătitorilor de venit se depun la aceleași termene ca și declarațiile pe formulare tipărite (208, 209, 210, 211, 212 și 213) la unitățile în a căror rază teritorială își au sediul plătitorii de venit care asigura reținerea la sursa a impozitelor prevăzute în aceste declarații. 2. Condiții tehnice standard pentru formatul electronic al declarațiilor plătitorilor de venit Declarațiile în format electronic vor fi transmise la unitatea fiscală în a carei raza teritorială se afla sediul/domiciliul plătitorului de venit, numai pe suport tip discheta FD 3,5" format Microsoft DOS sau CD-ROM, în dublu exemplar. Suporturile vor fi etichetate cu informațiile următoare: - codul fiscal al plătitorului de venit; - codul formularului de declarație; - setul 1 sau setul 2 (copia); - numărul suportului magnetic în cadrul setului de suporturi de exemplu: 1/3, 2/3, 3/3, dacă setul are 3 suporturi). În acest caz plătitorii de venit vor prezenta pe hârtie și un borderou însoțitor privitor la conținutul declarației. Suportul magnetic va conține doua fisiere de tip text ASCII pentru fiecare tip de declarație, care vor avea în mod obligatoriu următoarele denumiri și conținut: DIPVE. TXT conține datele de identificare a plătitorului de venit; DACPF. TXT conține datele aferente beneficiarilor de venit. Informațiile din fisiere se înscriu în format text ASCII (cod zecimal 10, 13, 35, 44, 48-57, 65-90 și 97-122). Nu se admit în cadrul fisierului semne diacritice, caractere de control etc., altele decât cele menționate anterior. Fisierul este format din înregistrări, fiecare înregistrare terminată cu perechea ASCII "carriage return" (cod zecimal 13) și "linefeed" (cod zecimal 10). Înregistrarea este formată din câmpuri, fiecare camp, cu excepția ultimului, fiind terminat cu "comma" ASCII (cod zecimal 44). Campurile numerice pot conține numai caractere ASCII cod zecimal 48-57. Campurile de tip numeric vor fi completate fără zerouri (cod ASCII 48) la stanga (aliniat stanga). Campurile tip caracter (alfanumeric) pot conține numai caractere ASCII cod zecimal 48-57, 65-90 și 97-122. Suplimentar conținutul câmpului tip caracter (alfanumeric) se încadrează între delimitatori "number sign" ASCII (cod zecimal 35). Ordinea campurilor din structura fisierelor este obligatorie, indiferent dacă acestea se completează sau nu. În descrierea de mai jos "Tip camp" are următoarea semnificație: N - numeric C - caracter (alfanumeric). Descrierea organizării înregistrărilor din fisiere: Fisierul DIPVE.TXT conține o singura înregistrare cu datele de identificare a plătitorului de venit, în următoarea structura:
-------------------------------------------------------------------------------
Tipul
Lungi- câmpului mea
Explicații ------------------------------------------------------------------------------- Anul fiscal
N 4
Se completează cu anul fiscal pentru care se întocmește declarația. Cod fiscal
N 10
Conține codul fiscal al plătitorului de venit. Denumire
C
Conține denumirea plătitorului de venit. Localitate
C Județ
C Strada
C Nr.
C Cod poștal
N Bloc
C Scara
C Etaj
C Ap.
C Sector
N Telefon
N Fax
N Cod formular de declarație
C 3
Se completează codul formularului de declarație. -------------------------------------------------------------------------------
Se completează adresa plătitorului de venit.
Fisierul DACPF.TXT va conține câte o înregistrare pentru fiecare beneficiar de venit în următoarea structura:
-------------------------------------------------------------------------------
Tipul
Lungi- câmpului mea
Explicații ------------------------------------------------------------------------------- Cod beneficiar de venit N 13
Se completează codul numeric personal sau numărul de identificare fiscală a beneficiarului de venit. Nume
C
Se completează numele beneficiarului de venit. Prenume
C
Se completează prenumele beneficia- rului de venit. Total venituri
N 18
Se completează cu:
- totalul veniturilor încasate de beneficiarul de venit, aferente anului expirat - pentru formularele tipărite 208, 209, 210 și 211;
- totalul venitului brut realizat de beneficiarul de venit în anul expirat
- pentru formularul tipărit 212;
- totalul venitului impozabil din pensii, realizat în anul expirat - pentru formularul tipărit 213; Impozitul reținut
N 18
Se completează cu totalul impozitului reținut pentru anul expirat. -------------------------------------------------------------------------------
Se completează în lei.
BORDEROU DE ÎNSOȚIRE a suportului cu declarațiile plătitorilor de venit pe anul...... Cod fiscal xxxxxxxxxx Denumire xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Adresa xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Declarație xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Cod xxx formular de declarație Am prezentat declarația pe suport discheta/CD-ROM. Am predat în total.... bucăți FD 3,5" CD-ROM, inscriptionate cu "Cod fiscal........", "Cod formular de declarație........" pentru: Numărul total al Totalul impozitului beneficiarilor de venit Totalul veniturilor reținut xxxxxxxxxxxx xxxxxxxxxxxx xxxxxxxxxxxx Sub sancțiunile aplicate faptei de fals în acte publice, declar că datele din aceasta declarație sunt corecte și complete. Numele și prenumele............................................... Funcția........................................................... Semnatura și ștampila plătitorului de venit....................... --------
