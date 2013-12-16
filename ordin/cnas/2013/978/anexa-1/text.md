# Anexa
----- (Anexa nr. 2 la Ordinul nr. 633/2012) ------------------------------------- Informații scrise pe cipul cardului național de asigurări sociale de sănătate
Câmp Partiție business Tip date Lungime Memorie Observații business
min. max.
Device data A.1 Numar card 1 CHAR 16 16 octeți
A.2 Cod cip 1 CHAR 25 25 octeți
A.3 Versiune 1 HEX 2 2 octeți
Date de identificare B.1 Nume 1 UTF8 1 100 200 octeți
B.2 Prenume 1 UTF8 1 100 200 octeți
B.3 Data nasterii 1 CHAR
8 8 octeți Formatul propus ZZLLAAAA
B.4 CNP 1 CHAR 13 13 octeți
Date administrative C.1 Numar de asigurat 1 UTF8 20 20 40 octeți
C.2 Spatiu pentru extensii ulterioare 1 N/A
256 octeți Rezervat informații ID emitent card
C.3 Spatiu pentru extensii ulterioare 2 N/A
32 octeți Rezervat informații status asigurat
C.4 Nume medic de familie II UTF8 1 180 180 octeți
C.5 Prenume medic de familie II UTF8 1 200 200 octeți
C.6 Cod medic de familie II UTF8 6 10 20 octeți
C.7 Telefon medic familie II CHAR 10 16 16 octeți
C.8 Persoana de contact II LST 0 2 432 octeți Maximum două persoane de contact. Se vor stoca numele și prenumele în același câmp. Maximum două numere de telefon ale persoanelor de contact
LNume prenume persoana de contact II UTF8 1 200
LNumar telefon persoana de contact II CHAR 10 16
C.9 Spatiu pentru extensii ulterioare 3 II UTF8 0 528 336 octeți Alocat pentru date administrative
Date clinice primare D.1 Grupa sanguina - vezi Nota* III CHAR 3 3 octeți
D.2 Rh - vezi Nota* III CHAR 1 1 octet
D.3 Spatiu pentru extensii ulterioare 4 III
2048 octeți
D.4 Status donator organe III CHAR 1 1 octet
D.5 Spatiu pentru extensii ulterioare 5 N/A
640 octeți Alocat pentru bilete de trimitere medicale
D.6 Diagnostice medicale cu risc vital - vezi Nota** IV LST 0 10 80 octeți Maximum 10 diagnostice. Se vor stoca numai codurile diagnosticelor.
LCod Diagnostic IV CHAR 5 8
D.7 Boli cronice - vezi Nota** IV LST 0 20 160 octeți Maximum 20 diagnostice. Se vor stoca numai codurile diagnosticelor.
LCod Boala Cronica IV CHAR 5 8
Extensii clinice E.1 Spatiu pentru extensii ulterioare 6 IV
5120 octeți Alocat pentru date clinice
E.2 Spatiu pentru extensii ulterioare 7 N/A
576 octeți Alocat pentru prescripția electronică
E.3 Spațiu pentru extensii ulterioare 8 N/A
102 octeți Alocat pentru status prescripția electronică
F.1 Dezvoltari ulterioare V
3072 octeți
Security data G.1 Certificate digitale VI
2048 octeți
G.2 Chei private VI
2048 octeți
G.3 PIN. Transport VI CHAR 3 3 octeți
G.4 PIN. CardHolder VI CHAR 4 12 12 octeți
G.5 Certificat digital necalificat MAI VII
2048 octeți Se va utiliza aceeași pereche de chei privată/publică (G.2) pentru ambele cereri de certificat digital (G.1 și G.5).
Dezvoltari ulterioare H.O Partitie dezvoltari ulterioare 2 VIII
7898 octeți
----- Nota (referire la grupa sanguină și Rh) - Valorile celor două câmpuri se pot grupa într-o singură codificare cu valoarea Char(1), descrierea acestora fiind stocată într-un nomenclator de definire a codurilor. Alternativ, cele două valori se pot gru pa într-un singur câmp, cu valoare Char(1), menținându-se nomenclatorul de definire a codurilor create. Nota (referire la diagnostice medicale cu risc vital și boli cronice, în conformitate cu prevederile stabilite prin ordin comun al ministrului sănătății și al președintelui Casei Naționale de Asigurări de Sănătate) - Dacă la codificare se foloseșt e ICD-10 (International Statistical Classification of Diseases and Related Health Problems), fiecare cod are un necesar de Varchar2(5). Dacă la codificare se folosește SNOMED-CT (Systematized Nomenclature of Medicine Clinical Terms), fiecare cod are un n ecesar de Char(8). -----
