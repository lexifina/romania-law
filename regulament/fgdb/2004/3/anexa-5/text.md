# Anexa 4
LISTA DE PLATĂ a compensațiilor pentru depozitele garantate Lista de plată a compensațiilor pentru depozitele garantate, aflate în evidență la instituția de credit în faliment, se întocmește, separat pentru persoane fizice, persoane fizice autorizate și persoane juridice de către Fond, pe baza Listei depozitelor la data indisponibilizării acestora, primită, potrivit prevederilor art. 6 din prezentul regulament, de la lichidatorul instituției de credit. Aceasta se remite instituției de credit mandatate pentru efectuarea plății, sub forma unei baze de date. Baza de date se prezintă sub formă de tabele care vor avea următoarea structură:
1. Tabelul de plată a persoanelor fizice garantare - LIST_PL_PF - include suma compensației cuvenite titularilor de depozite persoane fizice.
Denumire câmp Tip câmp Lung Explicații
Unitate Unit_ic C 4 Conține codul unității instituției de credit în faliment
Nume titular Nume C 20 Conține numele titularului
Inițiala tatălui I_ C 3 Conține inițiala tatălui titularului
Prenume titular Prenume C 20 Conține prenumele titularului
Serie act identitate Ai_seria C 3 Conține seria actului de identitate al titularului
Nr. act identitate Ai_nr C 10 Conține numărul actului de identitate al titularului
Cod numeric personal Cnp C 13 Conține codul numeric personal al titularului
Nerezident Nerezident L 1 Se completează "T" pentru cetățenii străini nerezidenți în România
Adresa Adresa C 80 Conține adresa titularului
Compensația cuvenită Suma N 19,2 Suma compensației cuvenite titularului de depozit
Identificatorul unic al înregistrării (numărul curent) Cod_fond C 10 Câmp format astfel:
2 digiți - numărul listei transmise de Fond
8 digiți - poziția titularului în lista deponenților
Data plății data_pl D 8 Instituția de credit plătitoare va completa data la care efectuează plata către beneficiarul de compensație (zz/ll/aaaa)
Suma plătită Suma_pl N 19,2 Suma compensației plătite efectiv titularului de depozit sau reprezentantului acestuia
Unitatea plătitoare Unit_pl C 4 Codul unității instituției de credit mandatate care a efectuat plata
Observații Obs C 100 Se înscriu eventualele neconcordanțe între datele de identificare din lista și datele reale constatate de instituția de credit plătitoare (dacă se încadrează în condițiile de plată), sau numele, prenumele și datele de identificare ale reprezentantului titularului (împuternicit, moștenitor, etc.)
----------
* La trecerea la leul greu, sumele cuvenite și plătite vor fi exprimate cu două zecimale. Până la acel moment suma de plată este rotunjită la întreg -1 leu.
2. Tabelul de plată a persoanelor fizice autorizate garantare -
LIST_PL_PFA - include suma compensației cuvenite titularilor de depozite persoane fizice autorizate.
Denumire câmp Tip câmp Lung Explicații
Unitate Unit_ic C 4 Conține codul unității instituției de credit în faliment
Denumire persoană fizică autorizată Den_pfa C 20 Denumire persoană fizică autorizată
Identificator fiscal Cui C 9 Conține codul unic de înregistrare/codul fiscal atribuit persoanei juridice
Nr. de înregistrare la registrul comerțului sau a autorizației de funcționare RC C 13 Nr. de înregistrare la registrul comerțului sau alt registru sau numărul autorizației de funcționare al persoanei fizice autorizate, după caz
Nume titular Nume C 20 Conține numele titularului
Inițiala tatălui I_ C 3 Conține inițiala tatălui titularului
Prenume titular Prenume C 20 Conține prenumele titularului
Serie act identitate Ai_seria C 3 Conține seria actului de identitate al titularului
Nr. act identitate Ai_nr C 10 Conține numărul actului de identitate al titularului
Cod numeric personal Cnp C 13 Conține codul numeric personal al titularului
Nerezident Nerezident L 1 Se completează "T" pentru cetățenii străini nerezidenți în România
Adresa Adresa C 80 Conține adresa titularului
Compensația cuvenită Suma N 19,2 Suma compensației cuvenite titularului de depozit
Identificatorul unic al înregistrării (numărul curent) Cod_fond C 10 Câmp format astfel:
2 digiți - numărul listei transmise de Fond
8 digiți - poziția titularului în lista deponenților
Data plății data_pl D 8 Instituția de credit plătitoare va completa data la care efectuează plata către beneficiarul de compensație (zz/ll/aaaa)
Suma plătită Suma_pl N 19,2 Suma compensației plătite efectiv titularului de depozit sau reprezentantului acestuia
Unitatea plătitoare Unit_pl C 4 Codul unității instituției de credit mandatate care a efectuat plata
Observații Obs C 100 Se înscriu eventualele neconcordanțe între datele de identificare din lista și datele reale constatate de instituția de credit plătitoare (dacă se încadrează în condițiile de plată), sau numele, prenumele și datele de identificare ale reprezentantului titularului (împuternicit, moștenitor, etc.)
-----------
* La trecerea la leul greu, sumele cuvenite și plătite vor fi exprimate cu două zecimale. Până la acel moment suma de plată este rotunjită la întreg - 1 leu.
3. Tabelul persoanelor juridice garantare - LIST_PL_PJ - include suma compensației cuvenite titularilor de depozite persoane juridice.
Denumire câmp Tip câmp Lung Explicații
Unitate Unit_ic C 4 Conține codul unității instituției de credit în faliment
Denumirea persoanei juridice sau entității fără personalitate juridică Nume C 20 Conține denumirea persoanei juridice sau entității fără personalitate juridică beneficiare
Identificator fiscal Cui C 9 Conține codul unic de înregistrare/codul fiscal atribuit persoanei juridice sau entității fără personalitate juridică beneficiare
Nr. de înregistrare la registrul comerțului sau autorizației de funcționare RC C 13 Nr. de înregistrare la registrul comerțului al persoanei juridice respectiv numărul autorizației de funcționare pentru entitățile fără personalitate juridică beneficiare
Adresa Adresa C 80 Conține adresa persoanei juridice sau entității fără personalitate juridică
Compensația cuvenită Suma N 19,2 Suma compensației cuvenite titularului de depozit
Identificatorul unic al înregistrării (numărul curent) Cod_fond C 10 Câmp format astfel:
2 digiți - numărul listei transmise de Fond
9 digiți - poziția titularului în lista deponenților
Cont Cont C 35 Agentul de plată va completa numărul contului curent și unitatea bancară unde este deschis acesta în care s-a făcut plata pe baza cererii beneficiarului de compensație
Banca Banca C 16
Filiala băncii Filiala C 16
Data plății data_pl D 8 Agentul de plată va completa data la care efectuează plata către beneficiarul de compensație
Suma plătită Suma_pl N 19,2 Suma compensației plătite efectiv persoanei juridice beneficiare
Unitatea plătitoare Unit_pl C 4 Codul unității care a efectuat plata
Observații Obs C 100 Se înscriu diferențele între datele de identificare din lista de plată și datele reale constatate de agentul de plată
--------
* La trecerea la leul greu, sumele cuvenite și plătite vor fi exprimate cu două zecimale. Până la acel moment suma de plată este rotunjită la întreg - 1 leu.
4. Tabelul unităților instituției de credit mandatate să efectueze plata compensațiilor - UNIT_PL - conține denumirea unităților instituției de credit prin care se face plata.
Denumire câmp Tip câmp Lung Explicații
Unitate Unit_pl C 4 Conține codul unității instituției de credit mandatate
Denumire unitate Den_unit C 30 Conține denumirea unității instituției de credit mandatate
Adresa Adr C 70 Conține adresa unității instituției de credit mandatate
