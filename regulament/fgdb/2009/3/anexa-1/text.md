# Anexa
LISTA DEPONENȚILOR GARANTAȚI la data de............... Lista deponenților garantați la instituția de credit, persoane fizice și persoane juridice, inclusiv entități fără personalitate juridică, se întocmește de aceasta, conform prevederilor incidente ale art. 3 și 4 din regulament, sub forma unei baze de date. Baza de date se prezintă sub formă de tabele, care vor avea următoarea structură: 1. Tabelul persoanelor fizice garantate - LIST_DEP_PF - va include totalitatea sumelor deponenților persoane fizice garantați de Fondul de garantare a depozitelor în sistemul bancar, denumit în continuare Fondul. Sumele de la toate unitățile instituției de credit sunt cumulate într-o singură poziție (nu se includ în listă persoanele fizice ale căror depozite menționate în Lista depozitelor negarantate - anexa la Ordonanța Guvernului nr. 39/1996 privind înființarea și funcționarea Fondului de garantare a depozitelor în sistemul bancar, republicată, cu modificările și completările ulterioare, denumită în continuare ordonanța, nu sunt garantate ori datorate de Fond).
Denumire câmp
Tip
câmp
Lung
Explicații
Unitate
Unit_ic
C
4
Conține codul intern al unității
instituției de credit
Nume deponent garantat
Nume
C
50
Conține numele deponent garantat
Prenume deponent garantat
Prenume
C
50
Conține prenumele deponent garantat
Seria și numărul
actului de identitate
Ai
C
20
Conține seria și numărul actului de
identitate al deponentului garantat
(care poate fi buletin de identi-
tate, carte de identitate ori alt
act de identitate emis conform
legii și pașaport)
Cod numeric personal
Cnp
C
13
Conține codul numeric personal al
deponentului garantat
Nerezident
Nerezident
L
1
Se completează "N" pentru cetățenii
străini nerezidenți în România
Adresa
Adresa
C
150
Conține adresa domiciliului
deponentului garantat
Obligațiile instituției
de credit față de
deponentul garantat
Depozit
N
19,2
Soldul tuturor depozitelor la data
de referință
Obligațiile de plată
exigibile ale deponentu-
lui garantat față de
instituția de credit
Credit
N
19,2
Soldul creanțelor de plată
exigibile la data de referință ale
instituției de credit asupra
deponentului
Compensația de plătit
Compensatie
N
19,2
Diferența pozitivă între câmpul
"Depozit" și câmpul "Credit"; dacă
este negativă se înscrie 0.
Identificatorul unic al
înregistrării (numărul
curent)
Cod_lich
C
13
Câmp format astfel:
4 digiți - Codul unității
instituției de credit
9 digiți - Poziția deponentului
în listă
2. Tabelul persoanelor juridice garantate - LIST_DEP_PJ - include totalitatea sumelor titularilor persoane juridice (inclusiv entitățile fără personalitate juridică) care sunt garantate de Fond. Sumele de la toate unitățile instituției de credit sunt cumulate într-o singură poziție (nu se includ în listă persoanele juridice ale căror depozite menționate în Lista depozitelor negarantate - anexa la ordonanță nu sunt garantate ori datorate de Fond).
Denumire câmp
Tip
câmp
Lung
Explicații
Unitate
Unit_ic
C
4
Conține codul intern al unității
instituției de credit
Denumirea persoanei
juridice sau entității
fără personalitate
juridică
Nume
C
100
Conține denumirea persoanei
juridice
Identificator fiscal
Cui
C
15
Conține codul unic de înregistrare/
codul fiscal atribuit persoanei
juridice
Numărul de înregistrare
la registrul comerțului
sau al autorizației de
funcționare
RC
C
20
Numărul de înregistrare la regis-
trul comerțului sau alt registru
sau numărul autorizației de funcți-
onare al persoanei juridice, după
caz
Adresa
Adresa
C
150
Conține adresa sediului
persoanei juridice
Obligațiile instituției
de credit față de
persoana juridică sau
entitatea fără persona-
litate juridică
Depozit
N
19,2
Soldul tuturor depozitelor la data
de referință
Obligațiile de plată
exigibile ale persoanei
juridice sau entității
fără personalitate
juridică față de
instituția de credit
Credit
N
19,2
Soldul creanțelor de plată
exigibile la data de referință ale
instituției de credit asupra
deponentului
Compensația de plătit
Compensatie
N
19,2
Diferența pozitivă între câmpul
"Depozit" și câmpul "Credit"; dacă
este negativă, se înscrie 0.
Identificatorul unic al
înregistrării (numărul
curent)
Cod_lich
C
12
Câmp format astfel:
4 digiți - Codul unității
instituției de credit
8 digiți - Poziția deponentului
în listă
3. Tabelul unităților instituției de credit - UNIT_IC - conține denumirea unităților instituției de credit.
Denumire câmp
Tip
câmp
Lung
Explicații
Unitate
Unit_ic
C
4
Conține codul intern al unității
instituției de credit
Denumirea unității
Den_unit
C
30
Conține denumirea unității
instituției de credit
Adresa
Adr
C
70
Conține adresa sediului unității
instituției de credit
------
