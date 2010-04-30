# Anexa 9
ALGORITMUL DE CALCUL al cifrei de control "modulo 10" 1. Pentru a se calcula cifra de control a crotaliei se numerotează cele 11 cifre ale codului crotaliei începând de la dreapta la stânga. 2. Cifrele de pe rândul 2 "Număr crotalie":
a) se înmulțesc cu cifra 3 numai cele de pe coloanele impare;
b) se înmulțesc cu cifra 1 numai cele de pe coloanele pare;
c) rezultatele înmulțirii cifrelor prevăzute la lit. a) și b) se însumează.
3. Rezultatul obținut ca urmare a însumării prevăzute la pct. 2 lit. c) se împarte la cifra 10. 4. Restul împărțirii prevăzute la pct. 3 se scade din cifra 10 și astfel se obține cifra de control. Exemplu: Tabel de calcul al cifrei de control
Indicator impar/par
11
10
9
8
7
6
5
4
3
2
1
Număr crotalie
0
3
4
7
4
0
3
6
5
3
0
Multiplicator
3
1
3
1
3
1
3
1
3
1
3
Produse
0
3
12
7
12
0
9
6
15
3
0
Suma produselor
0+
3+
12+
7+
12+
0+
9+
6+
15+
3+
0
Rezultat
67, modulo 10 67:10 = 6 rest 7
Cifra de control
10-7 = 3
Cod crotalie
0 3 (3) 4 7 4 0 3 6 5 3 0
