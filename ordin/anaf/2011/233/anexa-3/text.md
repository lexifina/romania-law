# Anexa 4
INSTRUCȚIUNI privind depunerea în format electronic a formularului 205 "Declarație informativă privind impozitul reținut la sursă, pe beneficiari de venit", cod 14.13.01.13/I Declarația informativă 205 se depune la organul fiscal în format electronic, însoțită de borderoul centralizator listat. Formatul electronic al declarației informative 205 se poate obține prin folosirea programului de asistență elaborat de Agenția Națională de Administrare Fiscală și se transmite organului fiscal competent, pe suport magnetic sau optic. Programul de asistență este distribuit contribuabililor, gratuit, de unitățile fiscale teritoriale sau poate fi descărcat de pe portalul Agenției Naționale de Administrare Fiscală. Informațiile din declarația informativă 205 vor fi transmise într-un fișier format text ASCII, în care fiecare înregistrare (linie) se termină cu "carriage return" și "linefeed". Separatorul dintre câmpuri va fi virgula. Fișierul text conține două tipuri de înregistrări. Prima înregistrare va conține informațiile:
- anul fiscal (4 caractere numerice)
- câmpul compus din tipul declarației și modul de plată a impozitului, (2 caractere numerice)
unde:
▪ primul caracter poate fi:
1 - pentru declarație inițială
2 - pentru declarație rectificativă
▪ al II-lea caracter poate fi:
1 - pentru plată anticipată
2 - pentru impozit final
- codul de identificare fiscală a plătitorului de venit (13 caractere numerice)
- natura veniturilor codificată conform listei (2 caractere numerice)
- total impozit reținut de plătitor (12 caractere numerice)
Următoarele înregistrări vor conține informațiile:
- codul numeric personal (13 caractere numerice)
- baza de calcul a impozitului (12 caractere numerice)
- impozitul reținut (12 caractere numerice)
- câmpul numeric de rezervă (12 caractere numerice)
- câmpul numeric de rezervă (12 caractere numerice)
Lista veniturilor cu regim de reținere la sursă:
COD
01. Venituri din drepturi de proprietate intelectuală
02. Venituri din vânzarea bunurilor în regim de consignație
03. Venituri obținute în baza unui contract de agent
04. Venituri obținute în baza unui contract de comision sau mandat comercial
05. Venituri din activități de expertiză contabilă și tehnică, judiciară și extrajudiciară
06. Venituri din activități desfășurate în baza contractelor/convențiilor civile încheiate potrivit Codului civil
07. Venituri din dividende
08. Venituri din dobânzi
09. Venituri din premii și jocuri de noroc
10. Câștiguri din transferul valorilor mobiliare, în cazul societăților închise, și al părților sociale
11. Venituri sub forma câștigurilor din operațiuni de vânzare-cumpărare de valută la termen, pe bază de contract, precum și orice alte operațiuni similare
12. Câștiguri din transferul titlurilor de valoare, altele decât părțile sociale și valorile mobiliare în cazul societăților închise, deținute mai mult de 365 de zile, realizate în perioada 01.01-30.06.2010
13. Venituri din pensii
14. Venituri din lichidare
15. Câștiguri din transferul titlurilor de valoare, altele decât părțile sociale și valorile mobiliare în cazul societăților închise, deținute mai puțin de 365 de zile inclusiv, realizate în perioada 01.01-30.06.2010
16. Venituri din activități agricole
17. Alte venituri
Numele fișierului text este format astfel:
D205_aaaa_xy_nnnnnnnnnnnnn_ss.txt, unde:
aaaa - anul înregistrării venitului (&gt;= 2010);
xy - precizări privind declarația și modul de plată a impozitului;
x = I - pentru declarație inițială;
R - pentru declarație rectificativă;
y = A - pentru plată anticipată;
F - pentru impozit final;
nnnnnnnnnnnnn - codul de identificare fiscală;
ss - natura veniturilor codificată conform listei.
Exemplu:
Fișierul cu numele D205_2010_IF_2222_09.txt, unde:
aaaa = 2010, I - pentru declarație inițială, F - pentru impozit final,
nnnnnnnnnnnnn = 2222, ss = 09 și conținutul:
- prima înregistrare:
2010, 12, 2222, 09, 600,
unde 12 e format din: 1 - pentru declarație inițială, 2 - pentru impozit final;
- următoarele înregistrări:
1111111111126, 1000, 100,,
1111111111134, 2000, 200,,
1111111111150, 3000, 300,,
INSTRUCȚIUNI privind depunerea în format electronic a formularului 206 "Declarație informativă privind câștigurile/pierderile din transferul titlurilor de valoare, altele decât părțile sociale și valorile mobiliare în cazul societăților închise", cod 14.13.01.13/t.v.1 Declarația informativă 206 se depune la organul fiscal în format electronic, însoțită de borderoul centralizator listat. Formatul electronic al declarației informative 206 se poate obține prin folosirea programului de asistență elaborat de Agenția Națională de Administrare Fiscală și se transmite organului fiscal competent pe suport magnetic sau optic. Programul de asistență este distribuit contribuabililor, gratuit, de unitățile fiscale teritoriale sau poate fi descărcat de pe portalul Agenției Naționale de Administrare Fiscală. Informațiile din declarația informativă 206 vor fi transmise într-un fișier format text ASCII, în care fiecare înregistrare (linie) se termină cu "carriage return" și "linefeed". Separatorul dintre câmpuri va fi virgula.
Fișierul text conține două tipuri de înregistrări:
Prima înregistrare va conține informațiile:
- anul fiscal (4 caractere numerice)
- câmpul compus din tipul declarației și modul de plată a impozitului, unde: (2 caractere numerice)
▪ primul caracter poate fi:
1 - pentru declarație inițială
2 - pentru declarație rectificativă
▪ al II-lea caracter, completat cu "1" (pentru plată anticipată)
- codul de identificare fiscală a plătitorului de venit (13 caractere numerice)
- natura veniturilor, câmp completat cu "18" (2 caractere numerice)
- total (total câștiguri - total pierderi) (12 caractere numerice)
Următoarele înregistrări vor conține informațiile:
- codul numeric personal (13 caractere numerice)
- total câștiguri (12 caractere numerice)
- total pierderi (12 caractere numerice)
- câmp numeric de rezervă (12 caractere numerice)
- câmp numeric de rezervă (12 caractere numerice)
Numele fișierului text este format astfel:
D206_aaaa_xy_nnnnnnnnnnnnn_18.txt unde,
aaaa - anul înregistrării venitului (&gt;= 2010);
xy - precizări privind declarația și modul de plată a impozitului;
x = I - declarație inițială sau R - declarație rectificativă;
y = A - plată anticipată;
nnnnnnnnnnnnn - codul de identificare fiscală;
18 - natura veniturilor.
Exemplu:
Fișierul cu numele D206_2010_IA_2222_18.txt, unde:
aaaa = 2010, I - declarație inițială, A - plată anticipată,
nnnnnnnnnnnnn = 2222, 18 = natura veniturilor și conținutul:
- prima înregistrare:
2010, 11, 2222, 18, 634,
unde 11 e format din: 1 = declarație inițială, 1 = plată anticipată;
- următoarele înregistrări:
1111111111126, 100, 200,,
1111111111134, 500, 0,,
1111111111150, 234, 0,,
