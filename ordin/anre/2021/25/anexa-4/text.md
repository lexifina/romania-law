# Anexa nr. 3 la contract
FORMAT-CADRU al datelor de măsurare transmise de OD furnizorului în vederea decontării consumului de energie electrică la clienții finali
Nr. crt.
Denumire câmp
Caracter câmp
Tip câmp
Dimensiune maximă câmp
Format
Observații
1.
Distribuitor
Obligatoriu
Caracter 50
2.
Furnizor
Obligatoriu
Caracter 50
3.
Client final
Obligatoriu
Caracter 50
4.
Cod Client final
Obligatoriu
Caracter 10
5.
Număr contract de distribuție
Obligatoriu
Caracter 20
6.
Dată contract de distribuție
Obligatoriu
Dată 10
7.
Periodicitate citire loc de consum
Obligatoriu
Caracter 15
Lunar/ Altă perioadă
8.
Mod stabilire cantitate energie electrică activă
Obligatoriu
Caracter 12
Citire/Autocitire/ Estimare
9.
POD
Obligatoriu
Caracter 90
10.
Loc de consum
Obligatoriu
Caracter 20
11.
Nivel de tensiune punct de delimitare
Obligatoriu
Caracter 15
JT/MT/IT
12.
Nivel de tensiune punct de măsurare
Obligatoriu
Caracter 15
JT/MT/IT
13.
Perioadă de facturare/decontare_De La
Obligatoriu
Dată 10
14.
Perioadă de facturare/ decontare_Până La
Obligatoriu
Dată 10
15.
Perioadă citire_De la
Obligatoriu
Dată 10
16.
Perioadă citire_Până La
Obligatoriu
Dată 10
17.
Serie contor
Obligatoriu
Caracter 50
18.
Cadran/Registru
Obligatoriu
Caracter 5
EA/EAP//ERI/ERC
19.
Mod de determinare energie reactivă pe curbă de consum
Obligatoriu
Caracter 5
DA/NU
20.
Index vechi
Obligatoriu
Numeric 20
21.
Index nou
Obligatoriu
Numeric 20
22.
Diferență indexe
Obligatoriu
Numeric 20
23.
Constantă
Obligatoriu
Numeric 15
24.
Cantitate măsurată
Obligatoriu
Numeric 20
25.
Cantitate estimată
Obligatoriu
Numeric 20
26.
Pierderi datorate necoincidenței punctelor de decontare și de măsurare [kWh/kVARh]
Obligatoriu
Numeric 20
27.
Corecții
Obligatoriu
Numeric 20
28.
Motiv alte corecții
Opțional
Caracter 30
29.
Perioadă recalculare_De la
Obligatoriu
Dată 10
30.
Perioadă recalculare_Până la
Obligatoriu
Dată 10
31.
Total cantitate energie activă [kWh]
Obligatoriu
Numeric 20
32.
Total cantitate energie reactivă facturată (energie reactivă de înmulțit cu tarif)
Obligatoriu
Numeric 20
33.
Total cantitate energie reactivă facturată (energie reactivă de înmulțit cu tarif x 3)
Obligatoriu
Numeric 20
34.
Cos ɸ
Obligatoriu
Numeric 10
Numai în cazul în care se măsoară energia reactivă
35.
UM
Obligatoriu
Caracter 5 kWh/kVARh
36.
Profil specific de consum
Obligatoriu
Caracter 10
Numai în cazul în care există profil la 15 minute
37.
ID Curbă agregată
Obligatoriu
Caracter 90
Numai pentru energiile active
NOTE: 1.
Datele de decontare pentru fiecare client se evidențiază prin completarea liniilor în tabel.
2.
Completarea datelor se realizează cu respectarea formatării câmpurilor.
3.
Câmpurile 7, 8, 11, 12, 18, 19, 35 și 37 se completează prin alegerea uneia dintre opțiunile specificate în coloana „Format”.
4.
Câmpurile 6, 13, 14, 15, 16, 29 și 30 se completează cu format de tip zz.ll.aaaa.
5.
Câmpurile 20, 21, 22 și 34 se completează cu 4 zecimale după separator de tip „punct”.
6.
Câmpurile 23, 24, 25, 26, 27, 31 și 32 se completează cu valoare rotunjită, fără zecimale.
