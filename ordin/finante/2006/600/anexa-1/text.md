# Anexa 1
STANDARD pentru transmiterea informațiilor Informațiile vor fi transmise într-un fișier format text ASCII, în care înregistrarea se termină cu "carriage return" și "linefeed". Separatorul dintre câmpuri va fi virgula, iar delimitatorul pentru câmpurile de tip caracter va fi # (câmpul începe și se termina cu #). Ordinea câmpurilor din structura fișierelor este obligatorie, indiferent dacă acestea se completează sau nu se completează. Fișierul text va avea obligatoriu următoarea denumire:
- NNNNNNNNNN = codul de identificare fiscală al unității centrale a societății bancare/al sucursalei, agenției, după caz;
- LL = luna de raportare;
- AAAA = anul de raportare;
- pn = p1 pentru raportarea 01-15 a lunii
= p2 pentru raportarea 15-30/31 a lunii
Fișierul va avea următoarea structură:
Descrierea câmpului Tipul câmpului Lungimea maximă Explicații
Codul de identificare fiscală al unității bancare Numeric 10 Se completează codul de identificare fiscală al unității bancare (sediul central, sucursala, agenție, etc.). Se completează în mod obligatoriu.
Codul de identificare fiscală al clientului Numeric 13 Se completează codul de identificare fiscală al clientului (cod unic de înregistrare fiscală/cod numeric personal/număr de identificare fiscală). Se completează în mod obligatoriu.
Denumirea clientului Caracter 200 Se completează denumirea/numele și prenumele clientului (câmpul începe și se termină cu @).
Numărul/codul clientului Caracter 20 Se completează numărul sau codul clientului (câmpul începe și se termină cu @).
Data începerii relației cu banca Data 10 Se completează data deschiderii primului cont de debit, în formatul ZZ/LL/AAAA.
Data încetării relației cu banca Data 10 Se completează data închiderii tuturor conturilor de debit, în formatul ZZ/LL/AAA. nici un caracter.
