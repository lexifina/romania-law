# Anexa 2
LISTA DEPOZITELOR la data indisponibilizării acestora Lista depozitelor deținute de persoane fizice, persoane fizice autorizate și persoane juridice la instituția de credit în faliment se întocmește de lichidatorul acesteia, conform prevederilor art. 6 din prezentul Regulament, sub forma unei baze de date. Baza de date se prezintă sub formă de tabele care vor avea următoarea structură: 1. Tabelul persoanelor fizice garantate - LIST_DEP_PF - va include totalitatea sumelor titularilor de cont persoane fizice care sunt garantate de Fond. Sumele de la toate unitățile instituției de credit sunt cumulate într-o singură poziție (nu se includ în listă persoanele fizice ale căror depozite menționate în anexa nr. 1 la prezentul regulament, nu sunt garantate de Fond).
Denumire câmp Tip Câmp Lung Explicații
Unitate Unit_ic C 4 Conține codul unității instituției de credit în faliment
Nume titular Nume C 20 Conține numele titularului
Inițiala tatălui I_ C 3 Conține inițiala tatălui titularului, dacă există
Prenume titular Prenume C 20 Conține prenumele titularului
Serie act identitate Ai_seria C 3 Conține seria actului de identitate al titularului (care poate fi buletin de identitate, carte de identitate ori alt act de identitate emis conform legii și pașaport)
Nr. act identitate Ai_nr C 10 Conține numărul actului de identitate al titularului
Cod numeric personal Cnp C 13 Conține codul numeric personal al titularului
Nerezident Nerezident L 1 Se completează "T" pentru cetățenii străini nerezidenți în România
Adresa Adresa C 80 Conține adresa titularului
Obligațiile instituției de credit față de titular Depozit N 19,2 Soldul obligațiilor instituției de credit fată de titular
Obligațiile titularului față de instituția de Credit credit N 19,2 Soldul obligațiilor titularului față de instituția de credit
Identificatorul unic al înregistrării (numărul curent) Cod_lich C 13 Câmp format astfel:
2 digiți - numărul listei transmise de lichidator
4 digiți - Codul unității instituției de credit
7 digiți - Poziția titularului în listă
Pentru prima listă primii 2 digiți vor fi "01"
2. Tabelul persoanelor fizice autorizate garantate - LIST_DEP_PFA - va include totalitatea sumelor titularilor de cont persoane fizice autorizate care sunt garantate de Fond. Sumele de la toate unitățile instituției de credit sunt cumulate într-o singură poziție (nu se includ în listă persoanele fizice ale căror depozite menționate în anexa nr. 1 la prezentul regulament, nu sunt garantate de Fond).
Denumire câmp Tip câmp Lung Explicații
Unitate Unit_ic C 4 Conține codul unității instituției de credit în faliment
Denumire persoană fizică autorizată Den_pfa C 20 Denumire persoană fizică autorizată
Identificator fiscal Cui C 9 Conține codul unic de înregistrare/codul fiscal atribuit persoanei juridice
Nr. de înregistrare la registrul comerțului sau a autorizației de funcționare RC C 13 Nr. de înregistrare la registrul comerțului sau alt registru sau numărul autorizației de funcționare al persoanei fizice autorizate, după caz
Nume titular Nume C 20 Conține numele titularului
Inițiala tatălui I_ C 3 Conține inițiala tatălui titularului, dacă există
Prenume titular Prenume C 20 Conține prenumele titularului
Serie act identitate Ai_seria C 3 Conține seria actului de identitate al titularului (care poate fi buletin de identitate, carte de identitate ori alt act de identitate emis conform legii și pașaport)
Nr. act identitate Ai_nr C 10 Conține numărul actului de identitate al titularului
Cod numeric personal Cnp C 13 Conține codul numeric personal al titularului
Nerezident Nerezident L 1 Se completează "T" pentru cetățenii străini nerezidenți în România
Adresa Adresa C 80 Conține adresa titularului
Obligațiile instituției de credit față de titular Depozit N 19,2 Soldul obligațiilor instituției de credit față de titular
Obligațiile titularului față de instituția de Credit credit N 19,2 Soldul obligațiilor titularului față de instituția de credit
Identificatorul unic al înregistrării (numărul curent) Cod_lich C 13 Câmp format astfel:
2 digiți - numărul listei transmise de lichidator
4 digiți - Codul unității instituției de credit
7 digiți - Poziția titularului în listă
Pentru prima listă primii 2 digiți vor fi "01"
3. Tabelul persoanelor juridice garantate - LIST_DEP_PJ - include totalitatea sumelor titularilor persoane juridice (inclusiv entitățile fără personalitate juridică) care sunt garantate de Fond. Sumele de la toate unitățile instituției de credit sunt cumulate într-o singură poziție (nu se includ în listă persoanele juridice ale căror depozite menționate în anexa nr. 1 la prezentul regulament, nu sunt garantate de Fond).
Denumire câmp Tip câmp Lung Explicații
Unitate Unit_ic C 4 Conține codul unității instituției de credit în faliment
Denumirea persoanei juridice sau entității fără personalitate juridică Nume C 20 Conține denumirea persoanei juridice
Identificator fiscal Cui C 9 Conține codul unic de înregistrare/codul fiscal atribuit persoanei juridice
Nr. de înregistrare la registrul comerțului sau a autorizației de funcționare RC C 13 Nr. de înregistrare la registrul comerțului sau alt registru sau numărul autorizației de funcționare al persoanei juridice, după caz
Adresa Adresa C 80 Conține adresa persoanei juridice
Obligațiile instituției de credit față de persoana juridică sau entitatea fără personalitate juridică Depozit N 19,2 Soldul obligațiilor instituției de credit față de persoana juridică
Obligațiile persoanei juridice sau entității fără personalitate juridică față de instituția de Credit credit N 19,2 Soldul obligațiilor persoanei juridice față de instituția de credit
Identificatorul unic al înregistrării (numărul curent) Cod_lich C 13 Câmp format astfel:
2 digiți - numărul listei transmise de lichidator
4 digiți - Codul unității instituției de credit
7 digiți - Poziția persoanei juridice în lista deponenților
Pentru prima listă primii 2 digiți vor fi "01".
4. Tabelul unităților instituției de credit - UNIT-IC - conține denumirea unităților instituției de credit.
Denumire câmp Tip câmp Lung Explicații
Unitate Unit_ic C 4 Conține codul unității instituției de credit în faliment
Denumire unitate Den_unit C 30 Conține denumirea unității instituției de credit în faliment
Adresa Adr C 70 Conține adresa unității instituției de credit în faliment
Instituția de credit în faliment
