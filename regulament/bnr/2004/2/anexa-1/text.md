# Anexa 1
ANEXA Nr. 1
STRUCTURA
codurilor IBAN atribuite în România
│RO│ │XX│ │yyyy│ │ZZZZZZZZZZZZZZZZ│
└┬─┘ └─┬┘ └─┬──┘ └───────┬────────┘
│ │ │ │ 16 caractere care identifică în mod unic unitatea teritorială a instituției și contul
│ │ │ └──> clientului deschis la respectiva unitate teritorială (alfanumerice, majuscule)
│ │ │
│ │ │ 4 caractere de identificare a instituției (alfabetice, majuscule), reprezentând primele patru
│ │ └──> caractere ale codului BIC al instituției
│ │
│ └──> 2 caractere de verificare (numerice, de la 0 la 9)
│
└──> codul de țară (2 caractere alfabetice, majuscule) - pentru România este RO.
ANEXA Nr. 2
METODA DE CALCULARE
a caracterelor de verificare
Pasul preliminar: Se creează un cod IBAN artificial pe baza codului de țară, a codului băncii și a codului contului clientului, punându-se "00" în locul caracterelor de verificare.
EXEMPLU: RO00AAAA1B31007593840000
Pasul 1: Se mută primele patru caractere (codul de țară și falsul cod de verificare) la dreapta codului IBAN.
EXEMPLU: RO00AAAA1B31007593840000 devine AAAA1B31007593840000RO00
Pasul 2: Se face conversia literelor în numere, conform tabelei următoare:
────────────────────────────────────────────────────────────────────────────────
A = 10 G = 16 M = 22 S = 28 Y = 34
────────────────────────────────────────────────────────────────────────────────
B = 11 H = 17 N = 23 T = 29 Z = 35
────────────────────────────────────────────────────────────────────────────────
C = 12 I = 18 O = 24 U = 30
────────────────────────────────────────────────────────────────────────────────
D = 13 J = 19 P = 25 V = 31
────────────────────────────────────────────────────────────────────────────────
E = 14 K = 20 Q = 26 W = 32
────────────────────────────────────────────────────────────────────────────────
F = 15 L = 21 R = 27 X = 33
────────────────────────────────────────────────────────────────────────────────
EXEMPLU: AAAA1B31007593840000RO00 devine 1010101011131007593840000272400
Pasul 3: Se aplică algoritmul MOD 97-10 (conform ISO 7064). Se împarte numărul obținut la 97 și restul se scade din 98. Dacă rezultatul este de un singur caracter, se pune un zero înaintea acestuia.
EXEMPLU: Restul împărțirii numărului 1010101011131007593840000272400 la 97 este 49.
Prin scădere se obține: 98 - 49 = 49, care reprezintă caracterele de verificare pentru respectivul cod IBAN, care astfel devine: R049AAAA1B31007593840000.
ANEXA Nr. 3
METODA DE VALIDARE
a unui cod IBAN
Pas preliminar: În cazul în care codul IBAN este prezentat pe suport hârtie, se convertește formatul acestuia la formatul electronic prin ștergerea spațiilor de separare.
EXEMPLU: un cod IBAN de tipul RO49 AAAA 1B31 0075 9384 0000 devine RO49AAAA1B31007593840000.
Pasul 1: Se mută primele patru caractere (simbolizând codul de țară și caracterele de verificare) la dreapta codului IBAN.
EXEMPLU: RO49AAAA1B31007593840000 devine AAAA1B31007593840000RO49.
Pasul 2: Se face conversia literelor în numere, conform tabelei de conversie cuprinse în anexa nr. 2.
EXEMPLU: AAAA1B31007593840000RO49 devine 1010101011131007593840000272449
Pasul 3: Se aplică algoritmul MOD 97-10 (conform ISO 7064). Pentru ca cele 2 caractere de verificare să fie corecte (codul IBAN să fie corect), restul împărțirii numărului astfel obținut la 97 trebuie să fie 1.
EXEMPLU: Restul împărțirii lui 1010101011131007593840000272449 la 97 este 1.
27
