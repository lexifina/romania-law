# Anexa 5
------- la regulament ------------ Tabelul 1 - Secțiuni de monitorizare a apelor de suprafața
Atribut Domeniu/ Nume Definiție Tip Lungime Restricții
Forma FORMA
Geometrie (puncte)
Nume NUME Nume folosit local Serie 100 Obligatoriu
Codul corp apă BDY_CD Codul unic al corpului de apă care se monitorizează Serie 24 Obligatoriu. Vezi ghid-gis: codificarea Râuri/Lacuri/Ape tranzitorii
Cod European EU_CD Codul unic al secțiunii la nivel european Serie 24 Obligatoriu.
Vezi ghid-gis.
Cod Stat membru MS_CD Cod unic al secțiunii la nivel de stat Serie 22 Obligatoriu.
Vezi ghid-gis.
Localizare LOCALIZARE Denumire receptor/poziția Serie 50 Obligatoriu
Se precizează:
Nume receptor/poziția
Direcție de Apă D_A Nume Direcție de Apă Text 15 Obligatoriu
Ex: Someș-Tisa
Subsistem SUBSISTEM Domeniul monitorizat Serie 3 Obligatoriu
Se precizează:
R - râuri
L - lacuri
AT - ape tranzitorii
AC - ape costiere
Mediu de investigație MEDINVEST Mediul de investigare Serie 1 Obligatoriu Se precizează:
A - apă
S - sedimente
B - biocenoză
Tip secțiune TIP_SECT
Text 2 Obligatoriu Se precizează:
E = existent
P = propus
EP = secțiune propusă, dar deja existentă în cadrul SNMCA
Directive/ Convenții DIR_CONV
Serie 20 Obligatoriu Se precizează:
- Nr. Directivei (ex: 75/440/EEC)
- Numele convenției (ex: CD - Convenția Dunării, CMN - Convenția Mării Negre)
- EUROWATERNET
Data completării INS_CAND Momentul introduceri datelor Data YYYY MM DD Obligatoriu
Completat de INS_CINE Acronimul operatorului Serie 15 Obligatoriu
Adâncime ADÂNCIME Adâncimea în metri Număr 4 Obligatoriu, numai pentru lacuri
Drinking DE BĂUT Tip secțiune Serie 1 Obligatoriu (Y, N)
Investigație INVEST Tip secțiune Serie 1 Obligatoriu (Y, N)
Operațional OPERAT Tip secțiune Serie 1 Obligatoriu (Y, N)
Habitat HABITAT Tip secțiune Serie 1 Obligatoriu (Y, N)
Supraveghere SUPRAVEG Tip secțiune Serie 1 Obligatoriu (Y, N)
Referință REFERINȚA Tip secțiune Serie 1 Obligatoriu (Y, N)
Tabelul 2 - Secțiuni de monitorizare a corpurilor de apa
Atribut Domeniu/Nume Definiție Tip Lungime Restricții
SW Cod Stație SWSTN_CD Cod secțiune de monitorizare a apelor de suprafață Serie 24 Obligatoriu. Vezi ghid-GIS: stații de monitoring de suprafață
RW Cod Corp RWBODY_CD Codul corpului de apă de sprafață - râu - care se monitorizează Serie 24 Obligatoriu. Vezi ghid-GIS:
Tabelul 3 - Secțiuni de monitorizare a lacurilor
Atribut Domeniu/Nume Definiție Tip Lungime Restricții
SW Stație Cod SWSTN_CD Cod secțiune de monitorizare a apelor de suprafață Serie 24 Obligatoriu. Vezi ghid-gis: stații de monitoring
LW Cod Corp LWBODY_CD Codul corpului de apă de suprafață - lac - care se monitorizează Serie 24 Obligatoriu. Vezi ghid-gis: corp de apă de lac
Tabelul 4 - Secțiuni de monitorizare a apelor de tranzitie
Atribut Domeniu/Nume Definiție Tip Lungime Restricții
SW Cod Stație SWSTN_CD Cod secțiune de monitorizare a apelor de suprafața Scrie 24 Obligatoriu. Vezi ghid-gis: Surface Monitoring Station
TW Cod Corp TWBODY_CD Codul corpului de apă de suprafață - tranzitorie - care se monitorizează Serie 24 Obligatoriu. Vezi ghid-gis: Apă de Tranziție
Tabelul 5 - Secțiuni de monitorizare a apelor costiere
Atribut Domeniu/Nume Definiție Tip Lungime Restricții
SW Cod Stație SWSTN_CD Cod secțiune de monitorizare a apelor de suprafață Serie 24 Obligatoriu. Vezi ghid-gis: stații de monitoring
TW Cod Corp TWBODY_CD Codul corpului de apă de suprafață - apă costieră - care se monitorizează Serie 24 Obligatoriu. Vezi ghid-gis: ape de coastă
Tabelul 6 - Secțiuni de monitorizare a apelor subterane
Atribut Domeniu/Nume Definiție Tip Lungime Restricții
Shape FORMAT
Geometrie (puncte)
Nume NUME Nume folosit local Serie 100 Obligatoriu
Cod European EU_CD Codul unic al secțiunii la nivel european Serie 24 Obligatoriu Vezi ghid-gis.
Cod Stat membru MS_CD Cod unic al secțiunii la nivel de stat Serie 22 Obligatoriu Vezi ghid-gis.
Localizare LOCALIZARE denumirea stratului acvifer Serie 25 Obligatoriu Ex: Frățești
Direcție de Apă D_A Nume Direcție de Apă Serie 15 Obligatoriu Ex: Someș-Tisa
Subsistem SUBSISTEM Domeniul monitorizat Serie 3 Obligatoriu Se precizează: AS-Ape subterane
Tip secțiune TIP_SECT
Serie 2 Obligatoriu
Se precizează:
E = existent
P = propus
EP = secțiune propusă, dar deja existentă în cadrul SNMCA
Directive/ Convenții DIR_CONV
Serie 20 Obligatoriu Se precizează:
- Nr. Directivei (ex: 80/68/EEC)
- Numele convenției (ex: CD - Convenția Dunării)
- EUROWATERNET
Dată completare INS_CAND Momentul introduceri datelor Data YYYYMMDD Obligatoriu
Completat de INS_CINE Acronimul operatorului Serie 15 Obligatoriu
Nivel NIVEL Tip secțiune Serie 1 Obligatoriu (Y, N)
Operațional OPERAT Tip secțiune Serie 1 Obligatoriu (Y, N)
Supraveghere SUPRAVEG Tip secțiune Serie 1
Obligatoriu (Y, N)
Adâncime ADÂNCIME Adâncime în metri Număr 4
Obligatoriu
Tabelul 7 - Secțiuni de monitorizare a apelor subterane
Atribut Domeniu/Nume Definiție Tip Lungime Restricții
GW Cod Stație GWSTN_CD Cod secțiune de monitorizare a apelor de suprafață Serie 24 Obligatoriu. Vezi ghid-gis: stații de monitoring
GW Cod Corp GWBODY_CD Codul corpului de apă subterană care se monitorizează Serie 24 Obligatoriu. Vezi ghid-gis: corp de apă subterană
NOTĂ: Atributele boldate sunt cerințe pentru sistemul de raportare la UE, exprimate în limbajul corespunzător. Tabel 8 - Secțiuni de monitorizare a apelor uzate
Tip date Nume atribut Lungime câmp Semnificație/Observație
FID
Identificator GIS (apare implicit)
Entitate Punct
Entitate punct
Indicator numeric ID
Numărul de ordine al înregistrării în tabela de atribute (după receptor - în ordine alfabetică)
Denumire evacuare NUME Text, 50 caractere Numele secțiunii/evacuării (Ex.: Electronică, colector 2)
Cod European EU_CD Text, 24 caractere Codul unic al secțiunii la nivel european Vezi ghid-gis
Cod stat membru MS_CD Text, 22 caractere Codul unic al secțiunii la nivel de stat Vezi ghid-gis
Nume agent economic UTILIZATOR Text, 50 caractere Se precizează numele utilizatorului de apă (Ex. S.C. ELECTRONICA S.A.)
Localitate LOCALIT Text, 30 caractere Se precizează, numele localității (Ex.: București)
Județ JUDEȚ Text, 20 caractere Se precizează numele județului (Ex.: Giurgiu)
Direcție de Ape D_A Text, 20 caractere Se precizează denumirea Direcției de Apă
Subsistem SUBSISTEM Text, 2 caractere Se precizează: AU - Ape uzate
Receptor/râu- lac RECEPTOR Text, 20 caractere Numele receptorului în care se evacuează apa uzată (ex.: Siret)
Cod corp de apă receptor WBODY_CD Text, 24 caractere Codul corpului de apă în care se evacuează Vezi ghid-gis
Identificator cadastral ID_CADASTR Text, 20 caractere
Debit evacuat/ autorizat DEBIT_E_A Text, 15 caractere Unitatea de măsură utilizată este l/s (Ex.: 48/50)
Tip secțiune TIP_SECT Text, 2 caractere Se precizează: E = existent P = propus EP = secțiune propusă, dar deja monitorizată
NOTĂ: Se vor folosi datele din formatul EVACUARI, după cum urmează; NAME corespunde Denumire evacuare UTILIZATOR corespunde cu Nume agent ec. LOCALIT corespunde cu Localitate D_A corespunde cu B.II. RECEPTOR corespunde cu Curs de apa-evacuare ID CADASTR corespunde cu Identificator cadastral Tabelul 9 - Secțiuni de monitorizare și parametrii de calitate ai apelor
Nr. crt. Name Subsistem Mediu de investigare Parametrii/Indicatorii analizați Frecvența
Pentru completarea tabelului nr. 9 se recomanda următoarele simboluri: Name: Numele secțiunii (a se completa identic cu tabelele prezentate anterior) Subsistem; R - râuri L - lacuri AT - ape tranzitorii AC - ape costiere AS - ape subterane AU - ape uzate Mediul de investigare: A - apa S - sedimente, MS - materii în suspensie B - biocenoza Parametrii/indicatorii analizati - se va preciza pachetele standard de analize, precum și alte substanțe caracteristice în secțiune funcție de presiunile existente: B-biologici (ex.: B: Fitoplancton: abundenta, diversitate, biomasa) Ba-bacteriologici (ex. Ba: coliformi totali, coliformi fecali) HM-hidromorfologici (ex.: HM: debit, nivel, viteza) FC - fizico-chimici generali (ex.: FC: pH, temperatura, azot total) PS-poluanti specifici bazinului hidrografic (ex.: PS: fenoli, cianuri, nichel) SP-substanțe prioritare/prioritar periculoase (ex.: SP: atrazin, plumb, diuron) Frecventa de monitoring (ex.: 12/an; 1/an; 1/3 ani)
