# Anexă
STANDARD pentru transmiterea informațiilor
Informațiile vor fi transmise într-un fișier format text ASCII, în care înregistrarea se termină cu "carriage return" și "linefeed". Separatorul dintre câmpuri va fi virgula, iar delimitatorul pentru câmpurile de tip caracter va fi #.
Ordinea câmpurilor din structura fișierelor este obligatorie, indiferent dacă acestea se completează sau nu se completează.
Fișierul text va avea obligatoriu următoarea denumire:
NNNNNNNNNN - LLAAAA.TXT, unde:
- NNNNNNNNNN = codul de înregistrare fiscală al unității centrale a societății bancare/al sucursalei, agenției, după caz;
- LL = luna de raportare;
- AAAA = anul de raportare.
Fișierul va avea următoarea structură:
Descrierea câmpului Tipul câmpului Lungimea maximă Explicații
Codul de înregistrare fiscală al unității bancare N 10 Se completează codul de înregistrare fiscală al unității bancare (sediu central, sucursală, agenție etc.) care este în relație cu clientul
Codul de înregistrare fiscală al clientului N 13 Se completează codul de înregistrare fiscală al clientului (cod unic de înregistrare/cod fiscal/cod numeric personal/număr de identificare fiscală)
Denumirea clientului C 200 Se completează denumirea/numele și prenumele clientului
Numărul/ C 20 Se completează numărul sau codul clientului
Codul clientului
Data începerii relației cu banca D 10 Se completează data deschiderii primului cont, în formatul ZZ/LL/AAAA
Data încetării relației cu banca D 10 Se completează data închiderii tuturor conturilor, în formatul ZZ/LL/AAAA
--------------
-------------
