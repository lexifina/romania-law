# Anexa 2
STANDARD pentru transmiterea informațiilor Informațiile vor fi transmise într-un fișier format text ASCII, în care înregistrarea se termină cu "carriage return" și "linefeed". Separatorul dintre câmpuri va fi virgula, iar delimitatorul pentru câmpurile de tip caracter va fi # (câmpul începe și se termină cu #). Ordinea câmpurilor din structura fișierelor este obligatorie, indiferent dacă acestea se completează sau nu se completează. Fișierul text va avea obligatoriu următoarea denumire:
- NNNNNNNNNN = codul de identificare fiscală al unității centrale;
- LL = luna de raportare;
- AAAA = anul de raportare;
- pn = p1 pentru raportarea 01-15 a lunii
= p2 pentru raportarea 15-30/31 a lunii
Fișierul va avea următoarea structură:
Descrierea câmpului Tipul câmpului Lungimea maximă Explicații
Codul de identificare fiscală al unității bancare Numeric 10 Se completează codul de identificare fiscală al unității bancare (sediul central, sucursală, agenție, etc.). Se completează în mod obligatoriu.
Codul de identificare fiscală al clientului persoană fizică Numeric 13 Se completează codul de identificare fiscală al clientului (cod numeric personal/număr de identificare fiscală). Se completează în mod obligatoriu.
Numele, prenumele clientului persoană fizică Caracter 200 Se completează numele și prenumele clientului (câmpul începe și se termină cu @).
Cod IBAN Caracter 20 Se completează codul IBAN corespunzător contului de card al clientului persoană fizică (câmpul începe și se termină cu @).
Data deschiderii contului de card Data 10 Se completează data deschiderii contului de card, în formatul ZZ/LL/AAAA.
Data închiderii contului de card Data 10 Se completează data închiderii contului de card, în formatul ZZ/LL/AAA. un caracter. --------
