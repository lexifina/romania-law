# Anexa 1
Anexa 1
la procedură Lista consultanților fiscali care sunt înscriși ca membri activi în Registrul consultanților fiscali și al societăților de consultanță fiscală și care au dreptul de exercitare a profesiei de consultant fiscal
*Font 7* ┌────────────┬──────────────┬───────┬─────────────┬────────────┬────────────┬─────────┬────────┬─────────┬───────────┐ │
Data
│
Numele și │CNP/NIF│
CIF
│
Numărul │
Data
│ Numărul │Stare**)│ Data
│
Data
│ │transmiterii│
prenumele │
│societății de│legitimației│legitimației│ștampilei│
│validării│invalidării│ │
│consultantului│
│ consultanță │
│
│
│
│
│
│ │
│
fiscal
│
│ fiscală*) │
│
│
│
│
│
│ ├────────────┼──────────────┼───────┼─────────────┼────────────┼────────────┼─────────┼────────┼─────────┼───────────┤ │
│
│
│
│
│
│
│
│
│
│ ├────────────┼──────────────┼───────┼─────────────┼────────────┼────────────┼─────────┼────────┼─────────┼───────────┤ │
│
│
│
│
│
│
│
│
│
│ └────────────┴──────────────┴───────┴─────────────┴────────────┴────────────┴─────────┴────────┴─────────┴───────────┘
Notă
...
──────────
*) Se referă la societatea de consultanță fiscală cu care consultantul fiscal respectiv are relații de salariat sau de asociat/acționar sau administrator.
**) Câmpul poate avea doar valorile "V" și "I", unde V = valid, I = invalid; când câmpul Stare este "V" se completează doar câmpul "Data validării", dacă este "I" se completează doar câmpul "Data invalidării".
──────────
La prima transmitere a datelor, lista va conține membrii Camerei Consultanților Fiscali valizi la acea dată (este considerat membru valid membrul Camerei Consultanților Fiscali care are dreptul de exercitare a profesiei de consultant fiscal). La prima transmitere a datelor nu se completează informația referitoare la data invalidării. Standard la anexa nr. 1 pentru fișierele transmise de Camera Consultanților Fiscali către Agenția Națională de Administrare Fiscală Fișierele vor fi de tip ascii CSV. Câmpurile sunt separate de caracterul virgulă ",". Câmpurile de tip Character sunt delimitate de diez "#". Fișierele nu trebuie să conțină linii goale. Fișierele vor avea denumirea: ccf_a1_zzllaaaahhmiss.csv, unde: zzllaaaahhmiss reprezintă data transmiterii.
*Font 9* ┌────────────────────┬─────────┬────────┬──────────────────────────────────────────────────┐ │ Denumirea câmpului │
Tipul │Lungimea│
Observații
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Data_transmitere
│Date
│
14 │Data transmiterii în format zzllaaaahhmiss
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Nume
│Character│
200 │Nume și prenume consultant
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │CNP/NIF
│Numeric │
13 │Codul numeric personal/Numărul de identificare
│ │
│
│
│fiscală al consultantului
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │CIF
│Numeric │
10 │Cod de identificare fiscală societate de
│ │
│
│
│consultanță fiscală
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Nr_legitimatie
│Numeric │
10 │Număr legitimație
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Data_legitimatie
│Date
│
8 │Dată legitimație în format zzllaaaa
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Nr_stampila
│Numeric │
10 │Număr ștampilă
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Stare
│Character│
1 │Stare
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Data_validare
│Date
│
8 │Dată validare
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────────────────┤ │Data_invalidare
│Date
│
8 │Dată invalidare
│ └────────────────────┴─────────┴────────┴──────────────────────────────────────────────────┘
Exemplu: ccf_a1_20092014131525.csv 20092014131525,#iIonescu Ion#,1234567890123,19,11,19012012,11,#V#,02022012, 20092014131525,#iPopescu Pop#,1234567890124"22,29012014,22,#V#,03032014, 20092014131525,#Marinescu Marin#,1234567890125"33,01012014,33,#V#,01012014,15092014
Anexa 2
la procedură Lista consultanților fiscali pentru care s-au constatat inadvertențe față de datele furnizate inițial de Camera Consultanților Fiscali
┌────┬─────────────┬───────────────────────┬─────────────────────────┐ │Nr. │
Data
│ Numele și prenumele
│ Codul numeric personal │ │crt.│transmiterii │ consultantului fiscal │ al consultantului fiscal│ ├────┼─────────────┼───────────────────────┼─────────────────────────┤ │
│
│
│
│ └────┴─────────────┴───────────────────────┴─────────────────────────┘
Standard la anexa nr. 2 pentru fișierele transmise de Agenția Națională de Administrare Fiscală către Camera Consultanților Fiscali Fișierele vor fi de tip ascii CSV. Câmpurile sunt separate de caracterul virgulă ",". Câmpurile de tip Character sunt delimitate de diez "#". Fișierele nu trebuie să conțină linii goale. Fișierele vor avea denumirea: ccf_a2_zzllaaaahhmiss.csv, unde: zzllaaaahhmiss reprezintă data transmiterii.
┌────────────────────┬─────────┬────────┬──────────────────────────────────────┐ │ Denumirea câmpului│ Tipul
│Lungimea│
Observații
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────┤ │Data_transmitere
│Date
│
14
│Data transmiterii în format
│ │
│
│
│zzllaaaahhmiss
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────┤ │Nume
│Character│ 200
│Nume și prenume consultant
│ ├────────────────────┼─────────┼────────┼──────────────────────────────────────┤ │CNP
│Numeric │
13
│CNP consultant
│ └────────────────────┴─────────┴────────┴──────────────────────────────────────┘
Exemplu: ccf_a2_01102014131525.csv 01102014131525,#iVasilescu Vasile#,1234567890126 01102014131525,#iGeorgescu George#,1234567890127 01102014131525,#Cristescu Cristian#,1234567890128 ----
