# Anexa 3
INSTRUCȚIUNI pentru transmiterea pe cale electronică a formularului 205 "Declarație informativă privind impozitul reținut la sursă și câștigurile/ pierderile realizate, pe beneficiari de venit", cod 14.13.01.13/I Formularul 205 "Declarație informativă privind impozitul reținut la sursă și câștigurile/pierderile realizate, pe beneficiari de venit" se depune în format electronic, pe suport magnetic sau optic, însoțit de situația centralizatoare prevăzută la secțiunea a II-a "Date recapitulative", în format hârtie. Formatul electronic se poate obține prin folosirea programului de asistență elaborat de Agenția Națională de Administrare Fiscală. Programul de asistență este distribuit contribuabililor gratuit de unitățile fiscale teritoriale sau poate fi descărcat de pe portalul Agenției Naționale de Administrare Fiscală. Informațiile din declarația informativă 205 vor fi transmise într-un fișier format text ASCII, în care fiecare înregistrare (linie) se termină cu "carriage return" și "linefeed". Separatorul dintre câmpuri va fi virgula. Fișierul text conține două tipuri de înregistrări: Prima înregistrare va conține informațiile: 1 - an fiscal N(4) 2 - stare declarație (1 - inițială/2 - rectificativă) N(1) 3 - codul de identificare fiscală a plătitorului de venit N(13) 4 - total câștig N(15) 5 - total pierdere N(15) 6 - câmp de rezervă N(15) 7 - câmp de rezervă N(15) 8 - total bază de calcul a impozitului N(15) 9 - total impozit reținut N(15) Următoarele înregistrări vor conține informațiile: 1 - tip de venit (nomenclator) N(2) 2 - natură impozit (1 - anticipat/2 - final) N(1) 3 - CNP/NIF N(13) 4 - câștig N(15) 5 - pierdere N(15) 6 - câmp de rezervă N(15) 7 - câmp de rezervă N(15) 8 - baza de calcul a impozitului N(15) 9 - impozit reținut N(15) Lista veniturilor cu regim de reținere la sursă:
COD
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
a) venituri din drepturi de proprietate intelectuală;
b) venituri din vânzarea bunurilor în regim de consignație;
c) venituri obținute în baza unui contract de agent;
d) venituri obținute în baza unui contract de comision sau mandat
comercial;
e) venituri din activități de expertiză contabilă și tehnică, judiciară
și extrajudiciară;
f) venituri din activități desfășurate în baza contractelor/convențiilor
civile încheiate potrivit Codului civil;
g) venituri din activități independente realizate într-o formă de
asociere cu o persoană juridică;
h) venituri sub forma câștigurilor din operațiuni de vânzare-cumpărare
de valută la termen, pe bază de contract, precum și orice alte
operațiuni similare;
i) câștiguri din transferul titlurilor de valoare, altele decât părțile
sociale și valorile mobiliare în cazul societăților închise;
j) venituri din dividende;
k) venituri din dobânzi;
l) câștiguri din transferul valorilor mobiliare, în cazul societăților
închise și a părților sociale;
m) venituri din lichidarea persoanei juridice;
n) venituri din premii și jocuri de noroc;
o) venituri din pensii;
p) venituri din activități agricole;
r) venituri din alte surse.
Numele fișierului text este format astfel: D205_aaaa_I/R_cif.txt, unde: aaaa - anul înregistrării venitului (> = 2011) I/R - precizări privind starea declarației (I-inițială/R-rectificativă) cif - codul de identificare fiscală Exemplul 1 (inițială): Fișierul cu numele D205_2011_I_2222.txt, unde: aaaa = 2010, I - declarație inițială, cif = 2222 și conținutul: - prima înregistrare 2011,1,2222, t4,t5,,,t8,t9 - următoarele înregistrări 01,2,1111111111126, v4,v5,,,v8,v9 Exemplul 2 (rectificativă): Fișierul cu numele D205_2011_R_2222.txt, unde: aaaa = 2010, R - declarație rectificativă, cif = 2222 și conținutul: - prima înregistrare 2011,2,2222,t4,t5,,,t8,t9 - următoarele înregistrări 01,2,1111111111126,0,0,,,0,0 (ștergere) 02,2,1111111111126, v4,v5,,,v8,v9 (adăugare)
