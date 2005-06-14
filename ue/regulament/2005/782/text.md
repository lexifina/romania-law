15/Volumul 14 | RO | Jurnalul Ofícial al Uniunii Europene | 235
32005R0782
L 131/26 | JURNALUL OFÍCIAL AL UNIUNII EUROPENE |
REGULAMENTUL (CE) NR. 782/2005 AL COMISIEI
din 24 mai 2005
de stabilire a formatului pentru transmiterea rezultatelor privind statisticile asupra deșeurilor
(Text cu relevanță pentru SEE)
COMISIA COMUNITĂȚILOR EUROPENE,
având în vedere Tratatul de instituire a Comunității Europene,
având în vedere Regulamentul (CE) nr. 2150/2002 al Parlamentului European și al Consiliului din 25 noiembrie 2002 privind statisticile asupra deșeurilor(1), în special articolul 6 litera (e),
întrucât:
(1) În temeiul articolului 6 din Regulamentul (CE) nr. 2150/2002, Comisia trebuie să adopte măsurile de punere în aplicare a respectivului regulament.
(2) În conformitate cu articolul 6 litera (e) din Regulamentul (CE) nr. 2150/2002, Comisia trebuie să stabilească formatul adecvat pentru transmiterea rezultatelor de către statele membre.
(3) Măsurile prevăzute de prezentul regulament sunt conforme cu avizul Comitetului pentru programul statistic instituit prin Decizia nr. 89/382/CEE, Euratom a Consiliului(2),
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Formatul adecvat pentru transmiterea către Comisie (Eurostat) a rezultatelor privind statisticile asupra deșeurilor se stabilește în anexa la prezentul regulament.
Statele membre utilizează acest format pentru datele privind anul de referință 2004 și anii următori.
Articolul 2
Statele membre transmit Comisiei (Eurostat) datele și metadatele solicitate de Regulamentul (CE) nr. 2150/2002 în format electronic, în conformitate cu un standard de schimb propus de Comisie (Eurostat).
Articolul 3
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 24 mai 2005.
Pentru Comisie
Joaquín ALMUNIA
Membru al Comisiei
(1) JO L 332, 9.12.2002, p. 1, regulament astfel cum a fost modificat ultima dată de Regulamentul (CE) nr. 574/2004 al Comisiei (JO L 90, 27.3.2004, p. 15).
(2) JO L 181, 28.6.1989, p. 47.
ANEXĂ
FORMATUL PENTRU TRANSMITEREA REZULTATELOR PRIVIND STATISTICILE ASUPRA DEȘEURILOR
Datele trebuie transmise în mod independent de sistem. Datele se transmit în conformitate cu un standard de schimb propus de Comisie (Eurostat).
Seturi de date
Domeniul reglementat de Regulamentul (CE) nr. 2150/2002 privind statisticile asupra deșeurilor cuprinde cinci seturi de date:
— Producere de deșeuri (GENER)
— Incinerare (INCIN)
— Operațiuni care pot conduce la recuperare (RECOV)
— Eliminare (DISPO)
— Numărul și capacitatea instalațiilor de recuperare și eliminare; acoperirea geografică a sistemului de colectare a deșeurilor pe regiune NUTS 2 (REGIO)
Pentru fiecare set de date trebuie transmis un fișier. Numele fișierului conține șase componente:
Domeniu | 5 | Valoare: WASTE
Set | 5 | GENER, INCIN, RECOV, DISPO, REGIO
Periodicitate | 2 | Valoare: A2
Cod de țară | 2 | Codul de două litere al țărilor (a se vedea lista A)
An | 4 | Anul de referință (primul an de referință 2004)
Perioadă | 4 | Valoare: 0000 (zero, zero, zero, zero) pentru datele anuale
Componentele numelui fișierului sunt separate printr-un liniuță de subliniere. Se utilizează un format bazat pe text. De exemplu, setul de date privind producerea de deșeuri din Belgia în 2004 va avea denumirea WASTE_GENER_A2_BE_2004_0000.
Valori lipsă
Nu trebuie să existe valori lipsă în variabilele de clasificare (categorie de deșeuri, activitate economică, regiune NUTS 2, tip de instalație de tratare a deșeurilor). Trebuie furnizate intrări pentru fiecare combinație de variabile de clasificare. Toate intrările pentru care nu s-a efectuat combinația trebuie trimise cu o valoare fixată la 0 (zero). Cu toate acestea, intrările pentru care nu există date disponibile trebuie furnizate cu valoarea codificată corespunzător ca fiind lipsă (codată cu litera „M”). Valorile lipsă trebuie explicate în raportul privind calitatea; este posibil ca ele să se datoreze, de exemplu, metodelor folosite. Este important să se facă distincție între valorile zero reale și valorile lipsă, întrucât nu pot fi calculate agregate cu date lipsă. În cazul în care o valoare nu este logic posibilă, celula trebuie să conțină codul „L”; este, de exemplu, cazul nămolurilor din efluenții industriali rezultați din activitatea casnică. Pentru a facilita verificarea coerenței și corectarea erorilor trebuie transmise și valorile totale.
Confidențialitate
Datele confidențiale trebuie transmise și marcate corespunzător ca fiind confidențiale. Caracterul confidențial al datelor se bazează pe politica națională de confidențialitatea. În general, informațiile pot fi confidențiale în cazul în care identitatea furnizorului informațiilor poate fi divulgată. Este cazul informațiilor care provin de la unul sau doi respondenți sau dacă unul sau doi respondenți domină datele. În general, datele provenite de la autoritățile publice nu sunt considerate ca fiind confidențiale.
Trebuie indicată, de asemenea, confidențialitatea secundară. Confidențialitatea secundară trebuie aplicată în așa fel încât (sub)totalurile să rămână disponibile pentru publicare. Comisia (Eurostat) utilizează informațiile confidențiale pentru a calcula agregatele (UE) fără a divulga informațiile confidențiale la nivel de țară.
Măsuri
Câmpurile trebuie să fie alfanumerice, adică nu trebuie să conțină separatori sau simboluri zecimale, cu excepția valorii datelor. Cantitățile de deșeuri sunt exprimate în mii de tone pe an, cu trei zecimale. Virgula trebuie utilizată ca simbol zecimal. Metoda de estimare nu permite întotdeauna precizia de trei cifre. În acest caz, valoarea trebuie furnizată numai cu cifrele semnificative. Pentru toate categoriile de deșeuri, cantitatea se bazează pe deșeuri umede (normale); pentru producția de nămol (numerele deșeurilor 11, 12, 40), cantitatea se calculează, de asemenea, în mii de tone de substanță uscată. Și în cazul setului de date privind tratarea deșeurilor, nămolul trebuie măsurat atât ca deșeu umed (normal), cât și ca substanță uscată. Această dispoziție se aplică numai în cazul în care nămolul este un articol separat; este cazul nămolurilor obișnuite (număr 12) din setul de date privind incinerarea și eliminarea.
Numărul instalațiilor de tratare a deșeurilor se exprimă printr-un număr întreg. Se folosesc mai multe unități de măsură pentru a descrie capacitatea de tratare a deșeurilor în funcție de tipul operațiunii de recuperare sau eliminare (a se vedea lista 1). Pentru a facilita comparația, se preferă furnizarea capacității de incinerare în mii de tone. Țările care pot furniza capacitatea de incinerare și în terajouli (1012 jouli) sunt invitate să facă acest lucru. Țările care nu pot furniza capacitatea de incinerare în terajouli trebuie să specifice că respectiva valoare lipsește (cu ajutorul codului „M”). Capacitatea de recuperare se măsoară în mii de tone. Capacitatea de eliminare trebuie exprimată în metri cubi sau în tone, în funcție de tipul de eliminare. Numai valorile măsurate în mii de tone sunt furnizate sub formă de numere reale cu trei zecimale, toate celelalte valori trebuind exprimate sub formă de numere întregi.
Sfera de cuprindere a sistemului de colectare a deșeurilor menajere în amestec cu alte deșeuri similare trebuie indicată ca procent din populație sau ca procent din numărul locuințelor.
Revizuiri
Seturile de date trebuie transmise în fișiere separate conținând toate intrările. De exemplu, setul de date privind producerea de deșeuri conține 51 de categorii de deșeuri pentru 21 grupuri NACE măsurate ca deșeuri umede și 3 categorii de deșeuri pentru 21 grupuri NACE măsurate ca substanță uscată. Setul conține 1 134 intrări.
De asemenea, datele revizuite trebuie trimise într-un set complet, celulele revizuite fiind marcate corespunzător (R). Datele provizorii sunt marcate cu simbolul P. Datele provizorii sunt întotdeauna supuse revizuirii. Atât datele provizorii, cât și cele revizuite trebuie explicate în raportul de calitate.
Set 1: Producere de deșeuri
Câmp | Lungime maximă | Valori
Domeniu | 8 | Valoare: WASTE
Set | 6 | Valoare: GENER (setul conține 51 × 21 intrări măsurate ca deșeu umed și 3 × 21 intrări măsurate ca substanță uscată pe țară)
Cod de țară | 2 | Codul de două litere al țărilor (a se vedea lista A)
An | 4 | Anul de referință (primul an de referință 2004)
Numărul deșeului | 2 | Codul care face trimitere la CED-Stat versiunea 3 (a se vedea lista B)
Număr de activitate | 2 | Codul care face trimitere la NACE (a se vedea lista C)
Umed/Uscat | 1 | Pentru toate categoriile de deșeuri cantitatea în deșeu umed (normal) (cod W); pentru nămol (număr de deșeu 11, 12, 40) de asemenea cantitatea în substanță uscată (cod D)
Deșeu produs | 12 | Cantitatea în mii de tone pe an. Cantitatea este exprimată printr-un număr real cu trei zecimale. Virgula trebuie folosită ca simbol zecimal. De exemplu: 19,876. Acest câmp trebuie să conțină întotdeauna o valoare. În cazul în care nu s-a efectuat combinația, valoarea este 0 (zero). Datele lipsă trebuie indicate prin codul „M”. Imposibilitatea logică a unei combinații este indicată prin codul „L”
Indicator de actualizare | 1 | Pentru a indica datele provizorii (P) sau datele revizuite (R), nu se completează în celelalte cazuri
Indicator de confidențialitate | 1 | Indică datele confidențiale (a se vedea lista D)
Setul 2: Incinerare
Câmp | Lungime maximă | Valori
Domeniu | 8 | Valoare: WASTE
Set | 6 | Valoare: INCIN (setul conține 17 × 2 intrări măsurate ca deșeu umed și 1 × 2 intrări măsurate ca substanță uscată pe regiune NUTS 1)
Cod de țară | 2 | Codul de două litere al țărilor (a se vedea lista A)
An | 4 | Anul de referință (primul an de referință 2004)
Cod NUTS 1 | 3 | Codul regional în conformitate cu clasificarea NUTS din Regulamentul (CE) nr. 1059/2003 al Parlamentului European și al Consiliului(1); totalul național trebuie furnizat folosind codul TT
Numărul deșeului | 2 | Codul care face trimitere la CED-Stat versiunea 3 (a se vedea lista E)
Operațiune de recuperare sau eliminare | 1 | Codul care face trimitere la anexele la Directiva 75/442/CEE(2) a Consiliului (a se vedea lista F); numai operațiunile 1 și 2 intră în acest set
Umed/Uscat | 1 | Pentru toate categoriile de deșeuri cantitatea în deșeu umed (normal) (cod W); pentru nămol (număr de deșeu 12) de asemenea cantitatea în substanță uscată (cod D)
Deșeu incinerat | 12 | Cantitatea în mii de tone pe an. Cantitatea este exprimată printr-un număr real cu trei zecimale. Virgula trebuie folosită ca simbol zecimal. De exemplu: 19,876. Acest câmp trebuie să conțină întotdeauna o valoare. În cazul în care nu s-a efectuat combinația, valoarea este 0 (zero). Datele lipsă trebuie indicate prin codul „M”. Imposibilitatea logică a unei combinații este indicată prin codul „L”
Indicator de actualizare | 1 | Pentru a indica datele provizorii (P) sau datele revizuite (R), nu se completează în celelalte cazuri
Indicator de confidențialitate | 1 | Indică datele confidențiale (a se vedea lista D)
Setul 3: Operațiuni care pot conduce la recuperare (excluzând recuperarea energiei)
Câmp | Lungime maximă | Valori
Domeniu | 8 | Valoare: WASTE
Set | 6 | Valoare: RECOV (setul conține 20 de intrări pe regiune NUTS 1)
Cod de țară | 2 | Codul de două litere al țărilor (a se vedea lista A)
An | 4 | Anul de referință (primul an de referință 2004)
Cod NUTS 1 | 3 | Codul regional în conformitate cu clasificarea NUTS din Regulamentul (CE) nr. 1059/2003; totalul național trebuie furnizat folosind codul TT
Numărul deșeului | 2 | Codul care face trimitere la CED-Stat versiunea 3 (a se vedea lista G)
Operațiune de recuperare sau eliminare | 1 | Codul care face trimitere la anexele la Directiva 75/442/CEE (a se vedea lista F); numai operațiunea 3 intră în acest set
Umed/Uscat | 1 | Pentru toate categoriile de deșeuri cantitatea în deșeu umed (normal) (cod W)
Deșeu recuperat | 12 | Cantitatea în mii de tone pe an. Cantitatea este exprimată printr-un număr real cu trei zecimale. Virgula trebuie folosită ca simbol zecimal. De exemplu: 19,876. Acest câmp trebuie să conțină întotdeauna o valoare. În cazul în care nu s-a efectuat combinația, valoarea este 0 (zero). Datele lipsă trebuie indicate prin codul „M”. Imposibilitatea logică a unei combinații este indicată prin codul „L”
Indicator de actualizare | 1 | Pentru a indica datele provizorii (P) sau datele revizuite (R), nu se completează în celelalte cazuri
Indicator de confidențialitate | 1 | Indică datele confidențiale (a se vedea lista D)
Setul 4: Eliminare (alta decât incinerarea)
Câmp | Lungime maximă | Valori
Domeniu | 8 | Valoare: WASTE
Set | 6 | Valoare: DISPO (setul conține 19 × 2 intrări măsurate ca deșeu umed și 1 × 2 intrări măsurate ca substanță uscată pe regiune NUTS 1)
Cod de țară | 2 | Codul de două litere al țărilor (a se vedea lista A)
An | 4 | Anul de referință (primul an de referință 2004)
Cod NUTS 1 | 3 | Codul regional în conformitate cu clasificarea NUTS din Regulamentul (CE) nr. 1059/2003; totalul național trebuie furnizat folosind codul TT
Numărul deșeului | 2 | Codul care face trimitere la CED-Stat versiunea 3 (a se vedea lista H)
Operațiune de recuperare sau eliminare | 1 | Codul care face trimitere la anexele la Directiva 75/442/CEE (a se vedea lista F); numai operațiunile 4 și 5 intră în acest set
Umed/Uscat | 1 | Pentru toate categoriile de deșeuri cantitatea în deșeu umed (normal) (cod W); pentru nămol (număr de deșeu 12) de asemenea cantitatea în substanță uscată (cod D)
Deșeu eliminat | 12 | Cantitatea în mii de tone pe an. Cantitatea este exprimată printr-un număr real cu trei zecimale. Virgula trebuie folosită ca simbol zecimal. De exemplu: 19,876. Acest câmp trebuie să conțină întotdeauna o valoare. În cazul în care nu s-a efectuat combinația, valoarea este 0 (zero). Datele lipsă trebuie indicate prin codul „M”. Imposibilitatea logică a unei combinații este indicată prin codul „L”
Indicator de actualizare | 1 | Pentru a indica datele provizorii (P) sau datele revizuite (R), nu se completează în celelalte cazuri
Indicator de confidențialitate | 1 | Indică datele confidențiale (a se vedea lista D)
Setul 5: Numărul și capacitatea instalațiilor de recuperare și eliminare și populația deservită de sistemul de colectare pe regiune
Câmp | Lungime maximă | Valori
Domeniu | 8 | Valoare: WASTE
Set | 6 | Valoare: REGIO (setul conține 14 intrări pe regiune NUTS 2)
Cod de țară | 2 | Codul de două litere al țărilor (a se vedea lista A)
An | 4 | Anul de referință (primul an de referință 2004)
Cod NUTS 2 | 4 | Codul regional în conformitate cu clasificarea NUTS din Regulamentul (CE) nr. 1059/2003; totalul național trebuie furnizat folosind codul TT
Operațiune de recuperare sau eliminare | 1 | Codul care face trimitere la anexele la Directiva 75/442/CEE (a se vedea lista F); nu se completează în cazul populației deservite de sistemul de colectare
Variabilă | 1 | Numărul instalațiilor (N), capacitatea (C) sau populația deservită de sistemul de colectare (P)
Unitate de măsură | 1 | Codul pentru unitatea de măsură a capacității în funcție de tipul operațiunii de recuperare sau eliminare (a se vedea lista I); pentru numărul de instalații codul N, pentru populația deservită de sistemul de colectare codul P (populație) sau D (locuințe)
Valoare | 12 | Toate valorile, numărul instalațiilor, procentul de populație sau locuințe deservit de sistemul de colectare și capacitatea se exprimă sub formă de numere întregi. Acest câmp trebuie să conțină întotdeauna o valoare. În cazul în care nu s-a efectuat combinația, valoarea este 0 (zero). Datele lipsă trebuie indicate prin codul „M”. Imposibilitatea logică a unei combinații este indicată prin codul „L”
Indicator de actualizare | 1 | Pentru a indica datele provizorii (P) sau datele revizuite (R), nu se completează în celelalte cazuri
Indicator de confidențialitate | 1 | Indică datele confidențiale (a se vedea lista D)
Lista A – Coduri de țări
Belgia | BE
Republica Cehă | CZ
Danemarca | DK
Germania | DE
Estonia | EE
Grecia | EL
Spania | ES
Franța | FR
Irlanda | IE
Italia | IT
Cipru | CY
Letonia | LV
Lituania | LT
Luxemburg | LU
Ungaria | HU
Malta | MT
Țările de Jos | NL
Austria | AT
Polonia | PL
Portugalia | PT
Slovenia | SI
Slovacia | SK
Finlanda | FI
Suedia | SE
Regatul Unit | UK
Bulgaria | BG
Croația | HR
România | RO
Turcia | TR
Islanda | IS
Liechtenstein | LI
Norvegia | NO
Lista B – Categorii de deșeuri
CED-Stat/versiunea 3 (JO L 90, 27.3.2004, p. 15)
Descriere | Cod | Periculoase | Numărul deșeului
Solvenți uzați | 01.1 | H | 1
Deșeuri acide, alcaline sau saline | 01.2 | | 2
Deșeuri acide, alcaline sau saline | 01.2 | H | 3
Uleiuri uzate | 01.3 | H | 4
Catalizatori uzați | 01.4 | | 5
Catalizatori uzați | 01.4 | H | 6
Deșeuri de la prepararea produselor chimice | 02 | | 7
Deșeuri de la prepararea produselor chimice | 02 | H | 8
Depuneri și reziduuri chimice | 03.1 | | 9
Depuneri și reziduuri chimice | 03.1 | H | 10
Nămol din efluenți industriali | 03.2 | | 11
Nămol din efluenți industriali | 03.2 | H | 12
Deșeuri medicale și biologice | 05 | | 13
Deșeuri medicale și biologice | 05 | H | 14
Deșeuri metalice | 06 | | 15
Deșeuri metalice | 06 | H | 16
Deșeuri de sticlă | 07.1 | | 17
Deșeuri de sticlă | 07.1 | H | 18
Deșeuri de hârtie și cartoane | 07.2 | | 19
Deșeuri de cauciuc | 07.3 | | 20
Deșeuri de materiale plastice | 07.4 | | 21
Deșeuri de lemn | 07.5 | | 22
Deșeuri de lemn | 07.5 | H | 23
Deșeuri textile | 07.6 | | 24
Deșeuri ce conțin PCB | 07.7 | H | 25
Echipamente casate (exclusiv vehicule scoase din uz și deșeuri de baterii și acumulatori) | 08 (exclusiv 08.1, 08.41) | | 26
Echipamente casate (exclusiv vehicule scoase din uz și deșeuri de baterii și acumulatori) | 08 (exclusiv 08.1, 08.41) | H | 27
Vehicule scoase din uz | 08.1 | | 28
Vehicule scoase din uz | 08.1 | H | 29
Deșeuri de baterii și acumulatori | 08.41 | | 30
Deșeuri de baterii și acumulatori | 08.41 | H | 31
Deșeuri animale și vegetale (exclusiv deșeuri rezultate din prepararea produselor alimentare și deșeuri de produse alimentare și exclusiv materiale fecale, urină și gunoi de grajd) | 09 (exclusiv 09.11, 09.3) | | 32
Deșeuri animale rezultate din prepararea produselor alimentare și deșeuri de produse alimentare | 09.11 | | 33
Materiale fecale, urină și gunoi de grajd | 09.3 | | 34
Deșeuri menajere și similare | 10.1 | | 35
Materiale amestecate și materiale nediferențiate | 10.2 | | 36
Materiale amestecate și materiale nediferențiate | 10.2 | H | 37
Reziduuri de sortare | 10.3 | | 38
Reziduuri de sortare | 10.3 | H | 39
Nămoluri obișnuite (exclusiv deșeuri de la dragare) | 11 (exclusiv 11.3) | | 40
Deșeuri de la dragare | 11.3 | | 41
Deșeuri minerale (exclusiv reziduuri de ardere, soluri contaminate și deșeuri de la dragare poluate) | 12 (exclusiv 12.4, 12.6) | | 42
Deșeuri minerale (exclusiv reziduuri de ardere, soluri contaminate și deșeuri de la dragare poluate) | 12 (exclusiv 12.4, 12.6) | H | 43
Reziduuri de ardere | 12.4 | | 44
Reziduuri de ardere | 12.4 | H | 45
Soluri contaminate și deșeuri de la dragare poluate | 12.6 | H | 46
Deșeuri solidificate, stabilizate sau vitrificate | 13 | | 47
Deșeuri solidificate, stabilizate sau vitrificate | 13 | H | 48
Total, nepericuloase | | | TN
Total, periculoase | | H | TH
Total, general | | | TT
Lista C – Număr de activitate
Categorie NACE rev. 1.1 [Regulamentul (CEE) nr. 3037/90 al Consiliului](3) | Descriere | Număr de activitate
A | Agricultură, vânătoare și silvicultură | 1
B | Pescuit | 2
C | Industria extractivă | 3
DA | Industria alimentară, a băuturilor și a tutunului | 4
DB + DC | Industria textilă și a confecțiilor Industria pielăriei și marochinăriei | 5
DD | Industria lemnului și a produselor din lemn | 6
DE | Industria celulozei, hârtiei și produselor din hârtie; editare și tipărire | 7
DF | Industria de prelucrare a țițeiului, cocsificarea cărbunelui și tratarea combustibililor nucleari | 8
DG + DH | Industria chimică, a produselor chimice și a fibrelor sintetice și artificiale Industria cauciucului și a produselor din materiale plastice | 9
DI | Industria altor produse minerale nemetalice | 10
DJ | Industria metalurgică și de prelucrare a metalelor | 11
DK + DL + DM | Industria construcției de mașini și echipamente Industria echipamentelor electrice și optice Industria echipamentelor de transport | 12
DN (exclusiv 37) | Alte industrii prelucrătoare | 13
E | Energie electrică, gaze și apă | 14
F | Construcții | 15
G-Q (exclusiv 51.57 și 90) | Alte activități economice (servicii) | 16
37 | Reciclare | 17
51.57 | Comerț en gros de deșeuri și reziduri | 18
90 | Asanarea și îndepărtarea gunoaielor; salubritate și activități similare | 19
HH | Deșeuri menajere | 20
Total | | TA
Lista D – Indicator de confidențialitate
Prea puține întreprinderi | A | De exemplu, 1 sau 2 întreprinderi în cadrul populației
O singură întreprindere domină datele | B | Suficiente întreprinderi, dar o singură întreprindere generează/tratează, de exemplu, peste 70 %
Două întreprinderi domină datele | C | Suficiente întreprinderi, dar două întreprinderi generează/tratează, de exemplu, peste 70 %
Date confidențiale din motiv de confidențialitate secundară | D | Nu confidențiale prin ele însele (indicator A, B, C), dar pentru a preveni divulgarea indirectă a unor date confidențiale
Valoarea nu este confidențială | Gol |
Lista E – Categorii de deșeuri pentru incinerare
Numărul deșeului | CED-Stat/versiunea 3 (JO L 90, 27.3.2004, p. 15) | Deșeuri periculoase/nepericuloase
Cod | Descriere
1 | 01 + 02 + 03 | Deșeuri chimice (deșeuri de compuși chimici + deșeuri de la prepararea produselor chimice + alte deșeuri chimice) | Nepericuloase
2 | 01 + 02 + 03 exclusiv 01.3 | Deșeuri chimice, exclusiv uleiuri uzate (deșeuri de compuși chimici + deșeuri de la prepararea produselor chimice + alte deșeuri chimice) | Periculoase
3 | 01.3 | Uleiuri uzate | Periculoase
4 | 05 | Deșeuri medicale și biologice | Nepericuloase
5 | 05 | Deșeuri medicale și biologice | Periculoase
6 | 07.7 | Deșeuri ce conțin PCB | Periculoase
7 | 10.1 | Deșeuri menajere și similare | Nepericuloase
8 | 10.2 | Materiale amestecate și materiale nediferențiate | Nepericuloase
9 | 10.2 | Materiale amestecate și materiale nediferențiate | Periculoase
10 | 10.3 | Reziduuri de sortare | Nepericuloase
11 | 10.3 | Reziduuri de sortare | Periculoase
12 | 11 | Nămoluri obișnuite | Nepericuloase
13 | 06 + 07 + 08 + 09 + 12 + 13 | Alte deșeuri (deșeuri metalice + deșeuri nemetalice + echipamente casate + deșeuri animale și vegetale + deșeuri minerale + deșeuri solidificate, stabilizate sau vitrificate) | Nepericuloase
14 | 06 + 07 + 08 + 09 + 12 + 13 exclusiv 07.7 | Alte deșeuri (deșeuri metalice + deșeuri nemetalice exclusiv deșeuri ce conțin PCB + echipamente casate + deșeuri animale și vegetale + deșeuri minerale + deșeuri solidificate, stabilizate sau vitrificate) | Periculoase
TN | | Total, nepericuloase | Nepericuloase
TH | | Total, periculoase | Periculoase
TT | | Total, general |
Lista F – Operațiuni de recuperare și eliminare; codurile fac trimitere la codurile din anexele la Directiva 75/442/CEE
Operațiune | Cod | Tipuri de operațiuni de recuperare și eliminare
Incinerare
1 | R1 | Utilizare principală ca și combustibil sau alt mijloc de producere a energiei
2 | D10 | Incinerare pe sol
Operațiuni care pot conduce la recuperare (exclusiv recuperarea energiei)
3 | R2 + | Recuperarea/regenerarea solvenților
R3 + | Reciclarea/recuperarea substanțelor organice care nu se folosesc ca solvenți (inclusiv operațiuni de compostare și alte procese de transformare biologică)
R4 + | Reciclarea/recuperarea metalelor și compușilor metalici
R5 + | Reciclarea/recuperarea altor materii anorganice
R6 + | Regenerarea acizilor sau bazelor
R7 + | Recuperarea produselor folosite la captarea agenților poluanți
R8 + | Recuperarea produselor din catalizatori
R9 + | Regenerarea uleiurilor sau alte metode de refolosire a acestora
R10 + | Împrăștierea îngrășămintelor pe sol în folosul agriculturii sau în scopuri ecologice
R11+ | Utilizarea deșeurilor obținute în urma oricăreia dintre operațiunile menționate numerotate R1-R10
Operațiuni de eliminare
4 | D1 + | Depozitarea pe sol și în sol (de exemplu, depozite, etc.)
D3 + | Injectarea la adâncime (de exemplu, injectarea reziduurilor pompabile în puțuri, saline sau falii geologice naturale, etc.)
D4 + | Descărcarea pe suprafețe (de exemplu, descărcarea de deșeuri lichide sau de nămoluri în depresiuni, iazuri sau lagune, etc.)
D5 + | Depozite special proiectate (de exemplu, dispunerea în celule etanșe separate, acoperite și izolate unele de altele și de mediul înconjurător, etc.)
D12 | Depozitare permanentă (de exemplu, amplasarea de containere într-o mină, etc.)
5 | D2 + | Tratarea în mediu terestru (de exemplu, biodegradarea deșeurilor lichide sau a nămolurilor în sol, etc.)
D6 + | Evacuarea în mediul acvatic, exceptând mările și oceanele
D7 + | Evacuarea în mări sau oceane, inclusiv îngroparea în solul marin
Lista G – Categorii de deșeuri pentru operațiuni care pot conduce la recuperare (exclusiv recuperarea de energie)
Numărul deșeului | CED-Stat/versiunea 3 (JO L 90, 27.3.2004, p. 15) | Deșeuri periculoase/nepericuloase
Cod | Descriere
1 | 01.3 | Uleiuri uzate | Periculoase
2 | 06 | Deșeuri metalice | Nepericuloase
3 | 06 | Deșeuri metalice | Periculoase
4 | 07.1 | Deșeuri de sticlă | Nepericuloase
5 | 07.1 | Deșeuri de sticlă | Periculoase
6 | 07.2 | Deșeuri de hârtie și cartoane | Nepericuloase
7 | 07.3 | Deșeuri de cauciuc | Nepericuloase
8 | 07.4 | Deșeuri de plastic | Nepericuloase
9 | 07.5 | Deșeuri de lemn | Nepericuloase
10 | 07.6 | Deșeuri textile | Nepericuloase
11 | 09 exclusiv 09.11, 09.3 | Deșeuri animale și vegetale (exclusiv deșeuri animale rezultate din prepararea produselor alimentare și deșeuri de produse alimentare; exclusiv materii fecale, urină și gunoi de grajd) | Nepericuloase
12 | 09.11 | Deșeuri animale rezultate din prepararea produselor alimentare și deșeuri de produse alimentare | Nepericuloase
13 | 09.3 | Materii fecale, urină și gunoi de grajd | Nepericuloase
14 | 12 | Deșeuri minerale | Nepericuloase
15 | 12 | Deșeuri minerale | Periculoase
16 | 01 + 02 + 03 + 05 + 08 + 10 + 11 + 13 | Alte deșeuri (deșeuri de compuși chimici + deșeuri de la prepararea produselor chimice + alte deșeuri chimice + deșeuri medicale și biologice + echipamente casate + deșeuri obișnuite compuse + nămoluri obișnuite + deșeuri solidificate, stabilizate sau vitrificate) | Nepericuloase
17 | 01 + 02 + 03 + 05 + 07.5 + 07.7 + 08 + 10 + 11 + 13 exclusiv 01.3 | Alte deșeuri (deșeuri de compuși chimici exclusiv uleiuri uzate + deșeuri de la prepararea produselor chimice + alte deșeuri chimice + deșeuri medicale și biologice + deșeuri de lemn + deșeuri ce conțin PCB + echipamente casate + deșeuri obișnuite compuse + nămoluri obișnuite + deșeuri solidificate, stabilizate sau vitrificate) | Periculoase
TN | | Total, nepericuloase | Nepericuloase
TH | | Total, periculoase | Periculoase
TT | | Total, general |
Lista H – Categorii de deșeuri pentru eliminare (altele decât cele pentru incinerare)
Numărul deșeului | CED-Stat/versiunea 3 (JO L 90, 27.3.2004, p. 15) | Deșeuri periculoase/nepericuloase
Cod | Descriere
1 | 01 + 02 + 03 | Deșeuri chimice (deșeuri de compuși chimici + deșeuri de la prepararea produselor chimice + alte deșeuri chimice) | Nepericuloase
2 | 01 + 02 + 03 exclusiv 01.3 | Deșeuri chimice exclusiv uleiuri uzate (deșeuri de compuși chimici + deșeuri de la prepararea produselor chimice + alte deșeuri chimice) | Periculoase
3 | 01.3 | Uleiuri uzate | Periculoase
4 | 09 exclusiv 09.11, 09.3 | Deșeuri animale și vegetale (exclusiv deșeuri rezultate din prepararea produselor alimentare și deșeuri de produse alimentare; exclusiv materii fecale, urină și gunoi de grajd) | Nepericuloase
5 | 09.11 | Deșeuri animale rezultate din prepararea produselor alimentare și deșeuri de produse alimentare | Nepericuloase
6 | 09.3 | Materii fecale, urină și gunoi de grajd | Nepericuloase
7 | 10.1 | Deșeuri menajere și similare | Nepericuloase
8 | 10.2 | Materiale amestecate și materiale nediferențiate | Nepericuloase
9 | 10.2 | Materiale amestecate și materiale nediferențiate | Periculoase
10 | 10.3 | Reziduuri de sortare | Nepericuloase
11 | 10.3 | Reziduuri de sortare | Periculoase
12 | 11 | Nămoluri obișnuite | Nepericuloase
13 | 12 | Deșeuri minerale | Nepericuloase
14 | 12 | Deșeuri minerale | Periculoase
15 | 05 + 06 + 07 + 08 + 13 | Alte deșeuri Deșeuri medicale și biologice + deșeuri metalice + deșeuri nemetalice + echipamente casate + deșeuri solidificate, stabilizate sau vitrificate) | Nepericuloase
16 | 05 + 06 + 07 + 08 + 13 | Alte deșeuri Deșeuri medicale și biologice + deșeuri metalice + deșeuri nemetalice + echipamente casate + deșeuri solidificate, stabilizate sau vitrificate) | Periculoase
TN | | Total, nepericuloase | Nepericuloase
TH | | Total, periculoase | Periculoase
TT | | Total, general |
Lista I – Unități de măsură de capacitate
Operațiune | Unitate de măsură de capacitate | Cod unitate de măsură
1 | Mii de tone pe an cu trei zecimale | t
| Terajouli pe an (1012) | j
2 | Mii de tone pe an cu trei zecimale | t
| Terajouli pe an (1012) | j
3 | Mii de tone pe an cu trei zecimale | t
4 | Metri cubi pe an | m
5 | Mii de tone pe an cu trei zecimale | t
(1) JO L 154, 21.6.2003, p. 1.
(2) JO L 194, 25.7.1975, p. 39. Directivă astfel cum a fost modificată ultima dată de Regulamentul (CE) nr. 1882/2003 al Parlamentului European și al Consiliului (JO L 284, 31.10.2003, p. 1).
(3) JO L 293, 24.10.1990, p. 1. Regulamentul astfel cum a fost modificat ultima dată de Regulamentul (CE) nr. 1882/2003 al Parlamentului European și al Consiliului.
