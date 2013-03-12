# Anexa 1
Anexă
la normă FIȘIER CONTRIBUȚII
Câmp Tip Descriere
CNP TEXT - 13 caractere
NUME ȘI PRENUME TEXT - 50 caractere
CONTRIBUȚIE_BRUTA NUMERIC - 2 zecimale
DATA_CONVERTIRII DATA - AAAA-LL-ZZ
NR_UNITATI_FOND*) NUMERIC - 6 zecimale
FOND TEXT - 8 caractere
---------
Notă
...
*) Numărul de unități de fond ale participantului, după convertirea contribuției aferente lunii respective.
FIȘIER UNITĂȚI DE FOND
Câmp Tip Descriere
FOND TEXT - 8 caractere
VALOARE_UNITATE_FOND NUMERIC - 6 zecimale
DATA_CONVERTIRII DATA - AAAA-LL-ZZ
NUMAR_TOTAL_UNITATI_FOND NUMERIC - 6 zecimale
FIȘIER STARE
Câmp Tip Descriere
CNP TEXT - 13 caractere
STARE TEXT - 1 caracter T - transferat D - decedat I - invalid P - pensionat
TRANSFER_IN_FOND TEXT - 8 caractere Completat doar pentru evenimentul T
DATA_EVENIMENT DATA - AAAA-LL-ZZ
1. Tipul fișierelor pentru raportare va fi CSV. 2. Denumirea fișierelor va fi următoarea:
a) pentru fișier contribuții: FC_xxxxxxxx_aaaa.csv ...
b) pentru fișier unități de fond: FUF_ xxxxxxxx_aaaa.csv ...
c) pentru fișier stare: FS_ xxxxxxxx_aaaa.csv ...
unde: xxxxxxxx = codul înscris în Registrul Comisiei al fondului de pensii private care raportează informațiile; aaaa = anul la care se face referire în raportarea informațiilor. ---------
