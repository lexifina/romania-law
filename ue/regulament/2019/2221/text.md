REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2019/2221 AL COMISIEI
din 12 decembrie 2019
de modificare a Regulamentului de punere în aplicare (UE) nr. 612/2013 în ceea ce privește datele înregistrate în mesajele referitoare la înregistrarea operatorilor economici și a antrepozitelor fiscale în registrele naționale și în registrul central
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) nr. 389/2012 al Consiliului din 2 mai 2012 privind cooperarea administrativă în domeniul accizelor și de abrogare a Regulamentului (CE) nr. 2073/2004 (1), în special articolul 22,
întrucât:
(1) Anexa I la Regulamentul de punere în aplicare (UE) nr. 612/2013 al Comisiei (2) stabilește structura și conținutul mesajelor referitoare la înregistrarea operatorilor economici și a antrepozitelor fiscale în registrele naționale și în registrul central.
(2) Pentru a asigura coerența între structura mesajelor de cerere obișnuită definite în Regulamentul de punere în aplicare (UE) nr. 612/2013 și în Regulamentul de punere în aplicare (UE) 2016/323 al Comisiei (3), valorile posibile pentru elementul de date „Tipul cererii” ar trebui să fie modificate în tabelul 1 din anexa I la Regulamentul de punere în aplicare (UE) nr. 612/2013, pentru a ține seama de modificările aduse cerințelor de date conținute într-o nouă versiune a sistemului informatizat instituit prin Decizia nr. 1152/2003/CE a Parlamentului European și a Consiliului (4).
(3) Explicația din coloana F din tabelul 1 din anexa I la Regulamentul de punere în aplicare (UE) nr. 612/2013 ar trebui actualizată pentru a furniza o identificare clară a elementului de date „Valoare” în cazul în care codul de tip „Criteriu primar” este stabilit la valoarea „46 = Tip de transport”.
(4) Sunt necesare alte corecții tehnice în tabelul 1 din anexa I la Regulamentul de punere în aplicare (UE) nr. 612/2013 pentru a conferi claritate și precizie dispozițiilor aplicabile.
(5) Prin urmare, Regulamentul de punere în aplicare (UE) nr. 612/2013 ar trebui modificat în consecință.
(6) Pentru a alinia data de aplicare a prezentului regulament la data de aplicare a unei noi versiuni a sistemului informatizat instituit prin Decizia nr. 1152/2003/CE, prezentul regulament ar trebui să se aplice de la 13 februarie 2020.
(7) Măsurile prevăzute de prezentul regulament sunt conforme cu avizul Comitetului pentru accize,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Anexa I la Regulamentul de punere în aplicare (UE) nr. 612/2013 se modifică în conformitate cu anexa la prezentul regulament.
Articolul 2
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Se aplică de la 13 februarie 2020.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 12 decembrie 2019.
Pentru Comisie
Președintele
Ursula VON DER LEYEN
(1) JO L 121, 8.5.2012, p. 1.
(2) Regulamentul de punere în aplicare (UE) nr. 612/2013 al Comisiei din 25 iunie 2013 privind funcționarea registrului operatorilor economici și al antrepozitelor fiscale, statisticile conexe și raportarea în temeiul Regulamentului (UE) nr. 389/2012 al Consiliului privind cooperarea administrativă în domeniul accizelor (JO L 173, 26.6.2013, p. 9).
(3) Regulamentul de punere în aplicare (UE) 2016/323 al Comisiei din 24 februarie 2016 de stabilire a unor norme detaliate referitoare la cooperarea și schimbul de informații între statele membre în ceea ce privește mărfurile aflate în regim suspensiv de accize în conformitate cu Regulamentul (UE) nr. 389/2012 al Consiliului (JO L 66, 11.3.2016, p. 1).
(4) Decizia nr. 1152/2003/CE a Parlamentului European și a Consiliului din 16 iunie 2003 privind informatizarea circulației și a controlului produselor supuse accizelor (JO L 162, 1.7.2003, p. 5).
ANEXĂ
În anexa I la Regulamentul (CE) nr. 612/2013, tabelul 1 se înlocuiește cu următorul text:
[menționată la articolul 4 alineatul (5), la articolul 7 alineatul (2) și la articolul 8 alineatul (2)]
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Tipul cererii | R | | Valorile posibile sunt: 1 | = | (rezervat) 2 | = | Cerere de date de referință 3 | = | (rezervat) 4 | = | (rezervat) 5 | = | Cerere de resincronizare a registrului operatorilor economici 6 | = | Cerere de recuperare a unei liste de e-AD-uri 7 | = | Cerere de statistici SEED | n1
| b | Denumirea mesajului cererii | C | — «R» dacă <Tipul cererii> este «2» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | Valorile posibile sunt: «C_COD_DAT» | = | Listă comună de coduri «C_PAR_DAT» | = | Parametrii comuni ai sistemului «ALL» | = | Pentru o structură completă | a..9
| c | Biroul solicitant | R | | [a se vedea lista de coduri 5 din anexa II la Regulamentul (CE) nr. 684/2009] | an8
| d | Identificator de corelare a cererii | C | — «R» dacă <Tipul cererii> este «2», «5», «6» sau «7» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | Valoarea atributului <Identificator de corelare a cererii> este unică pentru fiecare stat membru. | an..44
| e | Data de începere | C | Pentru 1e și f: — «R» dacă <Tipul cererii> este «2» sau «5» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | | Data
| f | Data de încetare | C | | Data
| g | Data unică | C | — «R» dacă <Tipul cererii> este «2» sau «5» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | | Data
2 | CEREREA LISTEI e-DA | C | — «R» dacă <Tipul cererii> este «6» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Codul statului membru | R | | [a se vedea lista de coduri 3 din anexa II la Regulamentul (CE) nr. 684/2009] | a2
2.1 | AC_CRITERIU PRIMAR | R | | | 99x
| a | Codul tipului de criteriu primar | R | | Valorile posibile sunt: 1 | = | ARC 2 | = | Marca comercială a produsului 3 | = | Categorii de produse accizabile care fac obiectul deplasării 4 | = | (rezervat) 5 | = | (rezervat) 6 | = | (rezervat) 7 | = | (rezervat) 8 | = | Orașul destinatarului 9 | = | Orașul expeditorului 10 | = | Orașul garantului 11 | = | (rezervat) 12 | = | Orașul locului de livrare 13 | = | Orașul antrepozitului fiscal de expediere 14 | = | Orașul transportatorului 15 | = | Codul NC al produsului 16 | = | Data facturii 17 | = | Codul de acciză al destinatarului 18 | = | Codul de acciză al expeditorului 19 | = | Codul de acciză al garantului 20 | = | (rezervat) 21 | = | (rezervat) 22 | = | Codul de acciză al antrepozitului fiscal de destinație 23 | = | Codul de acciză al antrepozitului fiscal de expediere 24 | = | (rezervat) 25 | = | Codul produsului accizabil 26 | = | Durata călătoriei 27 | = | Statul membru destinatar 28 | = | Statul membru de expediere 29 | = | Numele destinatarului 30 | = | Numele expeditorului 31 | = | Denumirea garantului 32 | = | (rezervat) 33 | = | Denumirea locului de livrare 34 | = | Denumirea antrepozitului fiscal de expediere 35 | = | Denumirea transportatorului 36 | = | Numărul facturii 37 | = | Codul poștal al destinatarului 38 | = | Codul poștal al expeditorului 39 | = | Codul poștal al garantului 40 | = | (rezervat) 41 | = | Codul poștal al locului de livrare 42 | = | Codul poștal al antrepozitului fiscal de expediere 43 | = | Codul poștal al transportatorului 44 | = | Cantitatea de mărfuri (în corpul e-AD) 45 | = | Numărul de referință local, adică un număr de serie atribuit de expeditor 46 | = | Tipul transportului 47 | = | (rezervat) 48 | = | (rezervat) 49 | = | Codul de TVA al destinatarului 50 | = | (rezervat) 51 | = | Codul de TVA al transportatorului 52 | = | Schimbarea destinației (numărul de ordine ≥ 2) | n..2
2.1.1 | AC_VALOARE PRIMARĂ | O | | | 99x
| a | Valoare | R | | Dacă <Codul tipului de criteriu primar> este «46» (Tipul de transport), se va folosi un <Cod Mod de transport> existent din lista <MODURI DE TRANSPORT>. | an..255
3 | CERERE_STA | C | — «R» dacă <Tipul cererii> este «7» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Tip de statistică | R | | Valorile posibile sunt: 1 | = | Operatori economici activi și inactivi 2 | = | Expirări iminente 3 | = | Operatori economici pe tip și antrepozite fiscale 4 | = | Activitate legată de accize 5 | = | Modificări ale autorizațiilor de accize | n1
3.1 | Codul LISTA STATELOR MEMBRE | R | | | 99x
| a | Codul statului membru | R | | [a se vedea lista de coduri 3 din anexa II la Regulamentul (CE) nr. 684/2009] | a2
4 | PERIOADĂ_STA | C | — «R» dacă <Tipul cererii> este «7» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Anul | R | | | n4
| b | Semestrul | C | Pentru 4 b, c și d: Următoarele trei câmpuri de date sunt opționale și exclusive: — <Semestru> — <Trimestru> — <Lună> Și anume, dacă unul dintre aceste câmpuri de date este completat, atunci celelalte două câmpuri de date nu se aplică | Valorile posibile sunt: 1 | = | primul semestru 2 | = | al doilea semestru | n1
| c | Trimestru | C | Valorile posibile sunt: 1 | = | primul trimestru 2 | = | al doilea trimestru 3 | = | al treilea trimestru 4 | = | al patrulea trimestru | n1
| d | Luna | C | Valorile posibile sunt: 1 | = | ianuarie 2 | = | februarie 3 | = | martie 4 | = | Aprilie 5 | = | mai 6 | = | iunie 7 | = | iulie 8 | = | August 9 | = | septembrie 10 | = | octombrie 11 | = | noiembrie 12 | = | decembrie | n..2
5 | REF_CERERE | C | — «R» dacă <Tipul cererii> este «2» — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Indicatorul «Criterii comune de evaluare a riscurilor» | O | | Valorile posibile sunt: 0 | = | Nu sau Fals 1 | = | Da sau Adevărat | n1
5.1 | Codul LISTA CODURILOR | O | | | 99x
| a | Lista codurilor solicitată | O | | Valorile posibile sunt: 1 | = | Unități de măsură 2 | = | Tipuri de evenimente 3 | = | Tipuri de dovezi 4 | = | (rezervat) 5 | = | (rezervat) 6 | = | Coduri lingvistice 7 | = | State membre 8 | = | Coduri de țară 9 | = | Coduri de ambalaje 10 | = | Motivele raportului de primire sau ale raportului de control nesatisfăcător 11 | = | Motive ale întreruperii 12 | = | (rezervat) 13 | = | Moduri de transport 14 | = | Unități de transport 15 | = | Zone vitivinicole 16 | = | Coduri de manipulare a vinului 17 | = | Categorii de produse accizabile 18 | = | Produse accizabile 19 | = | Coduri NC 20 | = | Corespondențe cod NC – produs accizabil 21 | = | Motive de anulare 22 | = | Motivele alertei sau respingerii e-AD 23 | = | Justificări privind întârzierea 24 | = | (rezervat) 25 | = | Persoane care prezintă evenimentul 26 | = | Motive de refuz 27 | = | Motive privind întârzierea rezultatului 28 | = | Acțiunile aferente cererii 29 | = | Motivele cererii 30 | = | (rezervat) 31 | = | (rezervat) 32 | = | (rezervat) 33 | = | (rezervat) 34 | = | Motivele care împiedică acțiunea decooperare administrativă 35 | = | (rezervat) 36 | = | Tipul documentului 37 | = | (rezervat) 38 | = | (rezervat) 39 | = | Motivele cererii de închidere manuală 40 | = | Motivele respingerii închiderii manuale” | n..2
