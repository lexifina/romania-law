# Anexa 3
Formatul de raportare a datelor 3.1. Informația despre ordinele clienților se va raporta în continuare conform Circularei nr. 31/29 iulie 1994, anexele nr. 1A-1C. 3.2. Lista centralizatoare furnizată de către Banca Naționala a României, pentru a fi citită de către societățile bancare, va fi un fisier în format DBF (DBase4, FoxPro) și va conține următoarele cîmpuri:
Nume câmp Tip Lungime Observații
Data D 8 data raportării, în format zz/ll/aa
Nume C 40 numele agentului economic
CodSic C 15 codul SICOMEX al agentului economic
NrFisc C 15 numărul fiscal
NOTĂ: Fisierul se va numi LISTA-C.DBF. 3.3. Lista cu conturile valutare ale clienților se va raporta într-un fisier format DBF (DBase4, FoxPro) și va conține următoarele cîmpuri:
Nume câmp Tip Lungime Observații
Data D 8 data raportării, în format zz/ll/aa
Banca C 4 codul băncii raportoare, conform Circularei nr. 31/29 iulie 1994
Nume C 40 numele agentului economic
CodSic C 15 codul SICOMEX al agentului economic
NrFisc C 15 numărul fiscal
TipCont C 1 tip cont (v. pct. 3.4)
CodCont C 20 numărul contului
Valuta C 3 codul valutei, conform Circularei nr. 31/29 iulie 1994
Suma N 18.2 soldul contului
NOTĂ: Fisierul se va numi CONTURI.DBF. 3.4. În funcție de tipul contului, în câmpul TipCont se va înscrie: A pentru cont curent; B pentru cont depozit la vedere C pentru cont depozit la termen; D pentru cont depozite colaterale pentru acreditive import; E pentru cont depozite colaterale pentru garanții emise; F pentru cont de credite la intern; G pentru alte conturi ----------------------
