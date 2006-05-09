11/Volumul 45 | RO | Jurnalul Ofícial al Uniunii Europene | 284
32006R0601
L 106/7 | JURNALUL OFÍCIAL AL UNIUNII EUROPENE
REGULAMENTUL (CE) NR. 601/2006 AL COMISIEI
din 18 aprilie 2006
de punere în aplicare al Regulamentului (CE) nr. 184/2005 al Parlamentului European și al Consiliului în ceea ce privește formatul și procedura de transmitere de date
COMISIA COMUNITĂȚILOR EUROPENE,
având în vedere Tratatul de instituire a Comunității Europene,
având în vedere Regulamentul (CE) nr. 184/2005 al Parlamentului European și al Consiliului din 12 ianuarie 2005 privind statisticile comunitare ale balanței de plăți, ale comerțului internațional cu servicii și ale investițiilor străine directe(1), în special articolul 7,
întrucât:
(1) Regulamentul (CE) nr. 184/2005 stabilește un cadru comun pentru producerea sistematică de statistici comunitare ale balanței de plăți, ale comerțului internațional de servicii și ale investițiilor străine directe.
(2) Este necesar să se stabilească formatul și procedura de transmitere a datelor necesare în vederea elaborării unor statistici armonizate și comparabile între statele membre, în vederea reducerii riscurilor de eroare în ceea ce privește transmiterea de date și a reducerii termenelor necesare pentru prelucrarea datelor culese și pentru punerea lor la dispoziția utilizatorilor. Prin urmare, este necesar să se definească normele de punere în aplicare pentru completarea instrucțiunilor din vademecumul balanței de plăți Eurostat, astfel cum au fost revizuite anual.
(3) Măsurile prevăzute de prezentul regulament sunt conforme cu avizul Comitetului pentru balanța de plăți, instituit prin Regulamentul (CE) nr. 184/2005,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Transmiterea de date
Statele membre transmit datele Comisiei (Eurostat) sub formă electronică, prin intermediul punctului de intrare unic administrat de Comisie (Eurostat).
Comisia (Eurostat) pune la dispoziție o documentație detaliată privind punctul de intrare unic menționat anterior și oferă linii directoare pentru punerea în aplicare a unor abordări compatibile în materie de transmitere de date.
Articolul 2
Formatul datelor
Statele membre utilizează formatul „Gesmes”, în conformitate cu standardele privind schimburile de date, definite de Comisie (Eurostat). Comisia (Eurostat) pune la dispoziție o documentație detaliată privind standardele în cauză și oferă linii directoare pentru punerea lor în aplicare, în conformitate cu cerințele prezentului regulament.
Nu se poate folosi nici un format individual de date.
Articolul 3
Specificații tehnice privind formatul datelor
Specificațiile tehnice privind structura datelor sunt prezentate în detaliu în anexa la prezentul regulament.
Articolul 4
Intrarea în vigoare
Prezentul regulament întră în vigoare în cea de-a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 18 aprilie 2006.
Pentru Comisie
Joaquín ALMUNIA
Membru al Comisiei
(1) JO L 35, 8.2.2005, p. 23.
ANEXĂ
Specificații tehnice privind structura datelor
INTRODUCERE
Standardizarea structurilor fișierelor de date este esențială pentru prelucrarea eficientă a acestora. Este vorba de o etapă indispensabilă pentru furnizarea de date în conformitate cu standardele de schimb definite de Comisie (Eurostat). Formatul Gesmes este singurul autorizat pentru transmiterea, de către statele membre către Comisie (Eurostat), a statisticilor privind balanța de plăți.
SERII DE DATE
Următoarele cinci serii de date sunt utilizate pentru transmiterea de date privind balanța de plăți:
Identificatorul seriei | Descriere
BOP_EUR_Q | Euro-indicatori
BOP_FDI_A | Investiții străine directe
BOP_ITS_A | Comerț internațional de servicii
BOP_POS_A | Poziții de investiții străine directe
BOP_Q_Q | Statistici trimestriale
STRUCTURA DATELOR, LISTA DE CODURI ȘI ATRIBUTELE
Prezenta secțiune oferă o imagine de ansamblu privind structura datelor, lista de coduri și atributele care trebuie să fie folosite. Cea mai recentă versiune a vademecumului balanței de plăți Eurostat conține valorile atributelor disponibile.
(1) Frecvența
(a) Definiție: frecvența seriei
(b) Denumirea listei de coduri: CL_FREQ
(c) Format: AN1
(2) Zona de referință sau declarantul
(a) Definiție: țara sau grupul geografic/politic de țări afectate de fenomenul economic observat. Această entitate mai poartă numele de „declarant”.
(b) Denumirea listei de coduri: CL_AREA_EE
(c) Format: AN2
(d) Abrevieri folosite pentru tipul: COU țară, ECO zonă economică, GEO zonă geografică, ORG organizație internațională
(3) Indicatori de ajustare
(a) Definiție: indicarea unei corecții privind variațiile sezoniere și/sau numărul de zile lucrătoare
(b) Denumirea listei de coduri: CL_ADJUSTEMENT
(c) Format: AN1
(4) Tipuri de date
(a) Definiție: tipul de date (de exemplu stoc sau flux) pentru statisticile privind balanța de plăți
(b) Denumirea listei de coduri: CL_DATA_TYPE_BOP
(c) Format: AN1
(5) Post codat al balanței de plăți
(a) Definiție: post codat al defalcării balanței de plăți
(b) Denumirea listei de coduri: CL_BOP_ITEM
(c) Format: AN8
(d) Abrevieri folosite pentru tipul: STD componentă tip, MEM post pentru memorie, SUP informație suplimentară, XOE post Eurostat/OCDE sau Eurostat, ECB post BCE, IIP poziție pentru investițiile internaționale
(6) Defalcare în funcție de monedă
(a) Definiție: defalcare în funcție de monedă, a operațiunilor și a pozițiilor
(b) Denumirea listei de coduri: CL_CURR_BRKDWN
(c) Format: AN1
(7) Zonă echivalentă
(a) Definiție: țara sau grupul geografic/politic de țări afectate de fenomenul economic, în care zona de referință sau declarantul (ref_area) efectuează tranzacția
(b) Denumirea listei de coduri: CL_AREA_EE
(c) Format: AN2
(8) Moneda de denominare a seriei
(a) Definiție: moneda în care este denominată seria (monedă curentă, de exemplu EUR, ECU, USD sau monedă națională, etc.) sau drepturi de tragere speciale
(b) Denumirea listei de coduri: CL_SERIES_DENOM
(c) Format: AN1
(9) Activitate economică rezidentă
(a) Definiție: activitate economică rezidentă
(b) Denumirea listei de coduri: CL_BOP_EC_ACTIV_R1
(c) Format N4
(10) Activitate economică nerezidentă
(a) Definiție: activitate economică nerezidentă
(b) Denumirea listei de coduri: CL_BOP_EC_ACTIV_R1
(c) Format N4
(11) Statutul observației (obligatoriu)
(a) Definiție: informația privind calitatea valorii sau privind o valoare neobișnuită sau absentă
(b) Denumirea listei de coduri: CL_OBS_STATUS
(c) Format AN1
(12) Confidențialitatea observației (facultativ)
(a) Definiție: indicarea autorizației sau a lipsei acesteia de a publica observația în afara instituției destinatare
(b) Denumirea listei de coduri: CL_OBS_CONF
(c) Format AN1
(13) Expeditorul
(a) Definiție: entitate care trimite datele
(b) Denumirea listei de coduri: CL_ORGANISATION
(c) Format AN3
(14) Destinatarul
(a) Definiție: entitate care primește datele
(b) Denumirea listei de coduri: CL_ORGANISATION
(c) Format AN3
