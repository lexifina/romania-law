REGULAMENTUL (UE) NR. 1089/2010 AL COMISIEI
din 23 noiembrie 2010
de punere în aplicare a Directivei 2007/2/CE a Parlamentului European și a Consiliului în ceea ce privește interoperabilitatea seturilor și serviciilor de date spațiale
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Directiva 2007/2/CE a Parlamentului European și a Consiliului din 14 martie 2007 de instituire a unei infrastructuri pentru informații spațiale în Comunitatea Europeană (INSPIRE) (1), în special articolul 7 alineatul (1),
întrucât:
(1) Directiva 2007/2/CE prevede norme generale pentru instituirea unei infrastructuri pentru informații spațiale în Comunitatea Europeană. În cadrul infrastructurii respective, statelor membre li se solicită să pună la dispoziție seturi de date privind una sau mai multe dintre anexele la Directiva 2007/2/CE și serviciile de date spațiale corespondente, în conformitate cu modalitățile tehnice pentru interoperabilitatea și, atunci când este posibil, armonizarea seturilor și serviciilor de date spațiale.
(2) Modalitățile tehnice țin cont de cerințele în materie ale utilizatorilor, care le-au fost solicitate părților interesate în cadrul unei anchete pe această temă și care au rezultat din analizarea materialului de referință prezentat și a politicilor de mediu relevante ale Uniunii, precum și a politicilor sau activităților care pot avea un impact asupra mediului.
(3) Fezabilitatea modalităților tehnice și proporționalitatea acestora din punct de vedere al costurilor și beneficiilor potențiale au fost analizate de Comisie pe baza rezultatelor încercărilor comunicate de părțile interesate, a răspunsurilor primite de la statele membre prin intermediul punctelor de contact naționale referitoare la solicitarea de informații cu privire la aspectele legate de raportul cost-beneficiu, precum și a dovezilor incluse în studiile întreprinse de statele membre privind costurile și beneficiile infrastructurilor de date spațiale la nivel regional.
(4) Reprezentanților statelor membre, precum și altor persoane fizice sau juridice interesate de datele spațiale, inclusiv utilizatori, producători, furnizori de servicii cu valoare adăugată sau alte organisme coordonatoare li s-a oferit posibilitatea de a participa la elaborarea modalităților tehnice prin intermediul unor experți propuși, precum și de a evalua proiectul de norme privind punerea în aplicare printr-o consultare a părților interesate și un exercițiu pilot.
(5) Pentru a realiza interoperabilitatea și a beneficia de eforturile întreprinse de comunitățile de utilizatori și producători, standardele internaționale sunt integrate, atunci când este cazul, în conceptele și definițiile elementelor din categoriile de date spațiale enumerate în anexele I, II sau III la Directiva 2007/2/CE.
(6) Pentru a asigura interoperabilitatea și armonizarea în cadrul categoriilor de date spațiale, statele membre trebuie să îndeplinească cerințele cu privire la tipurile comune de date, identificarea obiectelor spațiale, metadatele pentru interoperabilitate, modelul generic de rețea și alte concepte și norme care se aplică tuturor categoriilor de date spațiale.
(7) Pentru a asigura interoperabilitatea și armonizarea în cadrul unei singure categorii de date spațiale, statele membre trebuie să utilizeze clasificările și definițiile obiectelor spațiale, atributele lor esențiale și rolurile de asociere, tipurile de date, domeniile de valori și normele specifice care se aplică categoriei individuale de date spațiale.
(8) Deoarece în prezentul regulament nu sunt incluse valorile din listele de coduri necesare punerii în aplicare a prezentului regulament, prezentul regulament se va aplica numai după ce valorile respective vor fi adoptate sub forma unui act juridic. Prin urmare, este oportună amânarea aplicabilității prezentului regulament.
(9) Măsurile prevăzute în prezentul regulament sunt conforme cu avizul comitetului instituit în temeiul articolului 22 din Directiva 2007/2/CE,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Obiect
Prezentul regulament stabilește cerințele privind modalitățile tehnice pentru interoperabilitatea și, atunci când este posibil, armonizarea seturilor și serviciilor de date spațiale corespunzătoare categoriilor enumerate în anexele I, II și III la Directiva 2007/2/CE.
Articolul 2
Definiții
În sensul prezentului regulament, se aplică următoarele definiții, precum și definițiile tematice prevăzute la anexa II:
1. „tip abstract” (abstract type) înseamnă un tip care nu poate fi instanțiat, dar care poate avea atribute și roluri de asociere,
2. „rol de asociere” (association role) înseamnă o valoare sau un obiect cu care un anumit tip stabilește o relație, astfel cum se prevede la articolul 8 alineatul (2) litera (b) din Directiva 2007/2/CE,
3. „atribut” (attribute) înseamnă caracteristica unui tip, astfel cum se prevede la articolul 8 alineatul (2) litera (c) din Directiva 2007/2/CE,
4. „tip candidat” (candidate type) înseamnă un tip care este deja utilizat ca parte a specificației unei categorii de date spațiale din anexa I la Directiva 2007/2/CE, dar care va fi integral specificat în categoria de date spațiale din anexa II sau III la Directiva 2007/2/CE, de care aparține sub raport tematic,
5. „listă de coduri” (code list) înseamnă o enumerare deschisă care poate fi extinsă,
6. „tip de date” (data type) înseamnă un descriptor al unui set de valori lipsite de identitate, în conformitate cu ISO 19103,
7. „enumerare” (enumeration) înseamnă un tip de date ale căror instanțe alcătuiesc o listă fixă de valori literale denumite. Atributele unui tip enumerat pot lua valori numai din lista respectivă,
8. „identificator de obiect extern” (external object identifier) înseamnă un identificator unic de obiecte care este publicat de organismul responsabil și care poate fi utilizat de aplicații externe cu trimitere la obiectul spațial,
9. „identificator” (identifier) înseamnă o secvență de caractere independentă din punct de vedere lingvistic, capabilă să identifice în mod unic și permanent elementul cu care este asociată, în conformitate cu EN ISO 19135,
10. „a instanția” (instantiate) înseamnă a crea un obiect care este conform cu definiția, atributele, rolurile de asociere și constrângerile specificate pentru tipul instanțiat,
11. „strat” (layer) înseamnă o unitate elementară de informații spațiale care poate fi cerută sub formă de hartă de la un server în conformitate cu EN ISO 19128,
12. „informații privind ciclul de viață” (life-cycle information) înseamnă un set de proprietăți ale unui obiect spațial care descriu caracteristicile temporale ale unei versiuni a unui obiect spațial sau schimbările între versiuni,
13. „element de metadate” (metadata element) înseamnă o unitate distinctă de metadate, în conformitate cu EN ISO 19115,
14. „pachet” (package) înseamnă un mecanism de uz general pentru organizarea elementelor în grupe,
15. „registru” (register) înseamnă un set de fișiere care conțin identificatori atribuiți elementelor cu descrieri ale elementelor asociate, în conformitate cu EN ISO 19135,
16. „tip de obiect spațial” (spatial object type) înseamnă o clasificare a obiectelor spațiale,
17. „stil” (style) înseamnă punerea în concordanță a tipurilor de obiecte spațiale și a proprietăților și constrângerilor acestora cu simbolurile parametrizate utilizate pentru desenul cartografic,
18. „subtip al” (sub-type of) înseamnă o relație între un tip mai specific și un tip mai general, în cadrul căreia tipul mai specific este pe deplin compatibil cu tipul mai general și conține informații suplimentare, adaptate pe baza ISO 19103,
19. „tip” (type) înseamnă un tip de obiect spațial sau un tip de date,
20. voidable (potențial nul) înseamnă că, pentru un atribut sau o rol de asociere, poate fi pusă la dispoziție o valoare void (nulă), dacă nicio valoare omoloagă nu este conținută în seturile de date spațiale administrate de statele membre sau dacă nicio valoare omoloagă nu poate fi derivată din valorile existente la un cost rezonabil. Dacă un atribut sau un rol de asociere nu este anulabil, celula din tabel care precizează voidability pentru aceasta este lăsată necompletată.
Articolul 3
Tipuri comune
Tipurile comune anumitor categorii enumerate în anexele I, II și III la Directiva 2007/2/CE sunt conforme cu definițiile și constrângerile și includ atributele și rolurile de asociere stabilite în anexa I.
Articolul 4
Tipuri pentru substituirea și clasificarea obiectelor spațiale
1. Statele membre trebuie să utilizeze tipurile de obiecte spațiale și tipurile de date, enumerările și listele de coduri asociate definite în anexa II pentru substituirea și clasificarea obiectelor spațiale din seturile de date care îndeplinesc condițiile prevăzute de articolul 4 din Directiva 2007/2/CE.
2. Tipurile de obiecte spațiale și tipurile de date trebuie să fie conforme cu definițiile și constrângerile și să includă atributele și rolurile de asociere stabilite în anexa II.
3. Enumerările utilizate pentru atributele sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date trebuie să fie conforme cu definițiile și să includă valorile stabilite în anexa II. Valorile de enumerare reprezintă coduri mnemonice pentru calculatoare, neutre din punct de vedere lingvistic.
4. Listele de coduri utilizate în atributele sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date trebuie să fie conforme cu definițiile stabilite în anexa II.
Articolul 5
Tipuri
1. Pentru toate tipurile definite în prezentul regulament, în titlul secțiunii care precizează cerințele pentru un anumit tip se indică între paranteze un nume neutru din punct de vedere lingvistic pentru calculatoare. Respectivul nume neutru din punct de vedere lingvistic este utilizat pentru a se face trimitere la tipul omolog din definiția unui atribut sau a unui rol de asociere.
2. Tipurile care reprezintă un sub-tip al altui tip trebuie să includă, de asemenea, toate atributele și rolurile de asociere ale tipului respectiv.
3. Tipurile abstracte nu trebuie instanțiate.
4. Tipurile candidat trebuie luate în considerare în timpul elaborării cerințelor pentru categoriile de date spațiale de care aparțin din punct de vedere tematic. În timpul elaborării, singura modificare admisă în specificația tipului candidat o reprezintă extinderea acestuia.
Articolul 6
Liste de coduri și enumerări
1. Listele de coduri trebuie să aparțină unuia dintre următoarele tipuri, astfel cum este prevăzut în anexa II:
(a) liste de coduri care sunt administrate într-un registru comun de liste de coduri și care nu pot fi extinse de statele membre;
(b) liste de coduri care pot fi extinse de statele membre.
2. În cazul în care un stat membru extinde o listă de coduri, valorile permise ale listei de coduri extinse sunt puse la dispoziție într-un registru.
3. Atributele sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date care au un tip de listă de coduri pot lua numai valori care sunt valide în conformitate cu registrul în care este administrată lista de coduri.
4. Atributele sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date care au un tip de enumerare pot lua valori numai din listele indicate pentru tipul de enumerare respectiv.
Articolul 7
Codificare
1. Toate regulile de codificare utilizate pentru a codifica date spațiale trebuie să fie conforme cu EN ISO 19118. Acestea trebuie să indice în special normele de conversie a schemelor aplicabile tuturor tipurilor de obiecte spațiale, tuturor atributelor, rolurilor de asociere, precum și structura utilizată pentru datele de ieșire.
2. Trebuie puse la dispoziție toate regulile de codificare utilizate pentru a codifica date spațiale.
Articolul 8
Actualizări
1. Statele membre pun la dispoziție periodic actualizări ale datelor.
2. Toate actualizările se realizează cel mai târziu la 6 luni după efectuarea de modificări în cadrul setului de date sursă, cu excepția cazului în care în anexa II se indică o perioadă diferită pentru o anumită categorie de date spațiale.
Articolul 9
Administrarea identificatorilor
1. Tipul de date „Identificator” definit în secțiunea 2.1 din anexa I se utilizează ca tip pentru identificatorul de obiect extern al unui obiect spațial.
2. Identificatorul de obiect extern pentru identificarea unică a obiectelor spațiale nu trebuie modificat pe parcursul ciclului de viață al unui obiect spațial.
Articolul 10
Ciclul de viață al obiectelor spațiale
1. Versiuni diferite ale aceluiași obiect spațial trebuie să fie întotdeauna instanțe ale aceluiași tip de obiect spațial.
2. Atributele „namespace” și „localId” ale identificatorului de obiect extern trebuie să rămână aceleași pentru versiuni diferite ale unui obiect spațial.
3. În cazul în care se utilizează atributele „beginLifespanVersion” și „endLifespanVersion”, valoarea „endLifespanVersion” nu trebuie să se afle înaintea valorii „beginLifespanVersion”.
Articolul 11
Sistemul de referință temporal
1. Se utilizează sistemul de referință temporal prestabilit menționat la punctul 5 din partea B a anexei la Regulamentul (CE) nr. 1205/2008 al Comisiei (2), cu excepția cazului în care, în anexa II, se indică alte sisteme de referință temporale pentru o anumită categorie de date spațiale.
2. Dacă se utilizează alte sisteme de referință temporale, acestea sunt specificate în metadatele seturilor de date.
Articolul 12
Alte cerințe și norme
1. Domeniul de valori al proprietăților spațiale definite în prezentul regulament trebuie limitat la schema spațială „Simple Feature”, astfel cum este definită în EN ISO 19125-1, în absența unor indicații contrare privind o anumită categorie sau un anumit tip de date spațiale.
2. Toate valorile măsurate se exprimă utilizând unități SI, în absența unor indicații contrare privind o anumită categorie sau un anumit tip de date spațiale.
3. În cazul în care se utilizează atributele „validFrom” și „validTo”, „valoarea validTo” nu trebuie să fie anterioară valorii „validFrom”.
4. În plus, se aplică toate cerințele tematice stabilite în anexa II.
Articolul 13
Metadatele necesare pentru interoperabilitate
Metadatele care descriu un set de date spațiale includ următoarele elemente de metadate necesare pentru interoperabilitate:
1. Sistem de referință de coordonate: descrierea sistemului (sistemelor) de referință de coordonate utilizat(e) în seturile de date.
2. Sistem de referință temporal: descrierea sistemului (sistemelor) de referință temporal (e) utilizat(e) în seturile de date.
Acest element este obligatoriu numai dacă setul de date spațiale conține informații temporale care nu fac trimitere la sistemul de referință temporal prestabilit.
3. Codificare: descrierea unui (unor) construct (constructe) a(le) limbajului de programare care specifică reprezentarea obiectelor de date într-un registru, fișier, mesaj, dispozitiv de stocare sau mijloc de transmisie.
4. Coerență topologică: corectitudinea caracteristicilor topologice ale datelor, codificate în mod explicit, astfel cum sunt descrise în cadrul scopului.
Acest element este obligatoriu numai dacă setul de date spațiale include tipuri din modelul generic de rețea („Generic Network Model„) și nu asigură o topologie a liniei mediane (conectivitatea între liniile mediane) pentru rețea.
5. Codificarea caracterelor: codificarea caracterelor utilizată în setul de date.
Acest element este obligatoriu numai dacă se utilizează o codificare care nu se bazează pe UTF-8.
Articolul 14
Reprezentare
1. Pentru descrierea seturilor de date spațiale prin utilizarea unui serviciu de vizualizare de rețea, astfel cum se prevede în Regulamentul nr. 976/2009 al Comisiei (3), trebuie puse la dispoziție următoarele elemente:
(a) straturile specificate în anexa II pentru categoria sau categoriile aferente setului de date;
(b) pentru fiecare strat, cel puțin un stil de reprezentare prestabilit, având cel puțin un titlu asociat și un identificator unic.
2. Pentru fiecare strat, anexa II definește următoarele elemente:
(a) un titlu lizibil al stratului, care urmează a fi utilizat pentru afișare pe interfața utilizatorului;
(b) tipul (tipurile) de obiecte spațiale care intră în alcătuirea stratului.
Articolul 15
Intrare în vigoare
Prezentul regulament intră în vigoare în [a douăzecea] zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Se aplică de la 15 decembrie 2010.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 23 noiembrie 2010.
Pentru Comisie
Președintele
José Manuel BARROSO
(1) JO L 108, 25.4.2007, p. 1.
(2) JO L 326, 4.12.2008, p. 12.
(3) JO L 274, 20.10.2009, p. 9.
ANEXA I
TIPURI COMUNE
1. TIPURI DEFINITE ÎN STANDARDELE EUROPENE ȘI INTERNAȚIONALE
| 1. | Pentru tipurile „Area”, „Boolean”, „CharacterString”, „DateTime”, „Distance”, „Integer”, „Length”, „Measure”, „Number”, „Sign” și „Velocity”, utilizate în definițiile atributelor și ale rolurilor de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date, se aplică definițiile prevăzute în ISO 19103.
| 2. | Pentru tipurile „GM_Curve”, „GM_MultiSurface”, „GM_Object”, „GM_Point”, „GM_Primitive” și „GM_Surface”, utilizate în atributele spațiale sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date, se aplică definițiile prevăzute în ISO 19107.
| 3. | Pentru tipul „TM_Period”, utilizat în definiții ale atributelor și ale rolurilor de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date, se aplică definițiile prevăzute în ISO 19108.
| 4. | Pentru tipurile „CI_Citation” și „MD_Resolution”, utilizate în definiții ale atributelor și ale rolurilor de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date, se aplică definițiile prevăzute în ISO 19115.
| 5. | Pentru tipurile „LocalisedCharacterString” și „URI”, utilizate în definiții ale atributelor și ale rolurilor de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date, se aplică definițiile prevăzute în ISO 19139.
2. TIPURI DE DATE COMUNE
2.1. Identificator (Identifier)
Identificatorul de obiect extern unic, publicat de organismul responsabil, care poate fi utilizat de aplicațiile externe pentru a face trimiteri la obiectul spațial.
Atribute ale tipului de date „Identifier”
Atribut | Definiție | Tip | Voidability
localId | Identificator local, atribuit de furnizorul de date. Identificatorul local este unic în cadrul spațiului de nume, adică nu există niciun alt obiect spațial care să aibă același identificator unic. | CharacterString |
namespace | Spațiu de nume care identifică în mod unic sursa de date a obiectului spațial. | CharacterString |
versionId | Identificatorul unei anumite versiuni a obiectului spațial, cu o lungime maximă de 25 de caractere. Dacă specificația unui anumit tip de obiect spațial cu un identificator de obiect extern include informații privind ciclul de viață, identificatorul de versiune este utilizat pentru a face distincția între versiunile unui obiect spațial. Identificatorul de versiune este unic în cadrul setului tuturor versiunilor unui obiect spațial. | CharacterString | voidable
Constrângerile tipului de date „Identifier”
Atributele „localId” și „namespace” utilizează numai următorul set de caractere: {„A” … „Z”, „a” … „z”, „0” … „9”, „_”, „.”, „–”}, adică sunt permise numai litere din alfabetul latin, cifre, caracter de subliniere („underscore”), punctul și liniuța („dash”).
3. ENUMERĂRI COMUNE
3.1. Poziție verticală (VerticalPositionValue)
Poziția relativ verticală a unui obiect spațial.
Valori permise pentru enumerarea „VerticalPositionValue”
Valoare | Definiție
onGroundSurface | Obiectul spațial se află la nivelul solului.
suspendedOrElevated | Obiectul spațial este suspendat sau înălțat.
underground | Obiectul spațial este subteran.
4. LISTE DE CODURI COMUNE
4.1. Starea instalațiilor (ConditionOfFacilityValue)
Starea unei instalații din punctul de vedere al finalizării și exploatării acesteia.
Această listă de coduri este administrată într-un registru comun de liste de coduri.
4.2. Codul de țară (CountryCode)
Codul de țară definit în Ghidul stilistic interinstituțional publicat de Oficiul pentru Publicații al Uniunii Europene.
5. MODELUL GENERIC DE REȚEA (GENERIC NETWORK MODEL)
5.1. Tipuri de obiecte spațiale
5.1.1. Trimitere încrucișată (CrossReference)
Reprezintă o trimitere între două elemente ale aceleiași rețele.
Roluri de asociere ale tipului de obiect spațial „CrossReference”
Rol de asociere | Definiție | Tip | Voidability
element | Elementele la care se face trimitere încrucișată | NetworkElement |
5.1.2. Legătură generalizată (GeneralisedLink)
Tip de bază abstract reprezentând un element de rețea liniară care poate fi utilizat ca țintă în referențierea liniară.
Acest tip este un subtip al „NetworkElement”.
Este vorba despre un tip abstract.
5.1.3. Intersecție denivelată (GradeSeparatedCrossing)
Indicator precizând care dintre două sau mai multe elemente care se intersectează este/sunt situat(e) dedesubt și care deasupra, de utilizat atunci când coordonatele de elevație nu sunt prezente sau nu sunt credibile.
Acest tip este un subtip al „NetworkElement”.
Roluri de asociere ale tipului de obiect spațial „GradeSeparatedCrossing”
Rol de asociere | Definiție | Tip | Voidability
element | Secvență de legături de intersecție. Ordinea acestora reflectă gradul de elevație; prima legătură este legătura cu cea mai joasă elevație. | Link |
5.1.4. Legătură (Link)
Element al unei rețele curbilinii care conectează două poziții și care reprezintă o cale omogenă în rețea. Pozițiile conectate se pot reprezenta sub formă de noduri.
Acest tip este un subtip al „GeneralisedLink”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „Link”
Atribut | Definiție | Tip | Voidability
centrelineGeometry | Geometrie care reprezintă linia mediană a legăturii. | GM_Curve |
fictitious | Indicator care precizează că geometria liniei mediane a legăturii este o linie dreaptă fără puncte de control intermediar – cu excepția cazului în care linia dreaptă reprezintă în mod corespunzător geografia la rezoluția setului de date. | Boolean |
Roluri de asociere ale tipului de obiect spațial „Link”
Rol de asociere | Definiție | Tip | Voidability
endNode | Nod terminal opțional al legăturii. Nodul terminal poate reprezenta aceeași instanță ca și nodul inițial. | Node |
startNode | Nod inițial opțional pentru această legătură. | Node |
5.1.5. Succesiune de legături (LinkSequence)
Un element de rețea care reprezintă o cale continuă fără ramificări în rețea. Elementul are un început și un sfârșit definite, iar fiecare poziție din succesiunea de legături este identificabilă cu ajutorul unui singur parametru, cum ar fi lungimea.
Acest tip este un subtip al „GeneralisedLink”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „LinkSequence”
Atribut | Definiție | Tip | Voidability
link | Ansamblul ordonat de legături direcționate care constituie secvența de legături. | DirectedLink |
5.1.6. Set de căi de legătură (LinkSet)
Ansamblu de secvențe de legături și/sau de legături individuale care deține o funcție sau o semnificație specifică în cadrul unei rețele.
Acest tip este un subtip al „NetworkElement”.
Acest tip este abstract.
Roluri de asociere ale tipului de obiect spațial „LinkSet”
Rol de asociere | Definiție | Tip | Voidability
link | Set de legături și secvențe de legături care constituie setul de legături. | GeneralisedLink |
5.1.7. Rețea (Network)
O rețea reprezintă un ansamblu de elemente de rețea.
Atribute ale tipului de obiect spațial „Network”
Atribut | Definiție | Tip | Voidability
geographicalName | Denumire geografică pentru această rețea. | GeographicalName | voidable
Roluri de asociere ale tipului de obiect spațial Network
Rol de asociere | Definiție | Tip | Voidability
elements | Ansamblu de elemente care constituie rețeaua. | NetworkElement |
5.1.8. Arie de rețea (NetworkArea)
Element bidimensional într-o rețea.
Acest tip este un subtip al „NetworkElement”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „NetworkArea”
Atribut | Definiție | Tip | Voidability
geometry | Reprezintă proprietățile geometrice ale ariei. | GM_Surface |
5.1.9. Conexiune de rețea (NetworkConnection)
Reprezintă o conexiune logică între două sau mai multe elemente de rețea din diferite rețele.
Acest tip este un subtip al „NetworkElement”.
Atribute ale tipului de obiect spațial „NetworkConnection”
Atribut | Definiție | Tip | Voidability
type | Clasificare a conexiunii de rețea. | ConnectionTypeValue | voidable
Roluri de asociere ale tipului de obiect spațial „NetworkConnection”
Rol de asociere | Definiție | Tip | Voidability
element | Elemente de rețea din diferite rețele | NetworkElement |
Constrângeri ale tipului de obiect spațial „NetworkConnection”
Toate elementele trebuie să se afle în rețele diferite.
5.1.10. Element de rețea (NetworkElement)
Tip abstract de bază reprezentând un element dintr-o rețea. Fiecare element dintr-o rețea este prevăzut cu funcții care prezintă interes în cadrul rețelei.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „NetworkElement”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea în cauză a obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea în cauză a obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
Roluri de asociere ale tipului de obiect spațial „NetworkElement”
Rol de asociere | Definiție | Tip | Voidability
inNetwork | Rețelele din care face parte un anumit element de rețea. | Network | voidable
5.1.11. Proprietate a rețelei (NetworkProperty)
Tip abstract de bază reprezentând fenomene localizate la nivelul sau de-a lungul unui element de rețea. Acest tip de bază este prevăzut cu proprietăți generale pentru asocierea fenomenelor aferente rețelei (proprietăți ale rețelei) cu elementele de rețea.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „NetworkProperty”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea în cauză a obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea în cauză a obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
networkRef | Referințe spațiale ale proprietății aferente rețelei. | NetworkReference | voidable
5.1.12. Nod (Node)
Reprezintă o poziție importantă în rețea care se află întotdeauna la începutul sau la sfârșitul unei legături.
Acest tip este un subtip al „NetworkElement”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „Node”
Atribut | Definiție | Tip | Voidability
geometry | Localizarea nodului. | GM_Point |
Roluri de asociere ale tipului de obiect spațial „Node”
Rol de asociere | Definiție | Tip | Voidability
spokeEnd | Legăturile care intră în nod. | Link | voidable
spokeStart | Legăturile care părăsesc nodul. | Link | voidable
5.2. Tipuri de date
5.2.1. Legătură direcționată (DirectedLink)
O legătură, fie în direcția pozitivă, fie în direcția negativă.
Atribute ale tipului de date „DirectedLink”
Atribut | Definiție | Tip | Voidability
direction | Indică concordanța (direcție pozitivă) sau neconcordanța (direcție negativă) legăturii direcționate cu direcția pozitivă a acesteia. | Sign |
Roluri de asociere ale tipului de date „DirectedLink”
Rol de asociere | Definiție | Tip | Voidability
link | Legătură | Link |
5.2.2. Referință de legătură (LinkReference)
Referință, în cadrul rețelei, la un element de rețea liniară.
Acest tip este un subtip al „NetworkReference”.
Atribute ale tipului de date „LinkReference”
Atribut | Definiție | Tip | Voidability
applicableDirection | Direcțiile legăturii generalizate cărora li se aplică referința. În cazul în care o proprietate nu se aplică unei direcții de-a lungul unei legături, dar reprezintă un fenomen de-a lungul unei legături, „inDirection” se referă la partea dreaptă pe direcția legăturii. | LinkDirectionValue | voidable
Constrângeri ale tipului de date „LinkReference”
Țintele referințelor liniare trebuie să fie elemente de rețea liniară. Cu alte cuvinte, dacă se utilizează referențierea liniară sau dacă direcția este relevantă, ținta referinței rețelei este o legătură sau o secvență de legături.
5.2.3. Referință de rețea (NetworkReference)
Referință la un element de rețea.
Roluri de asociere ale tipului de date „NetworkReference”
Rol de asociere | Definiție | Tip | Voidability
element | Elementul de rețea referențiat. | NetworkElement |
5.2.4. Referință liniară simplă (SimpleLinearReference)
Referință de rețea, limitată la o parte a unui element de rețea liniară. Partea respectivă reprezintă partea elementului de rețea situată între „fromPosition” și „toPosition”.
Acest tip este un subtip al „LinkReference”.
Atribute ale tipului de date „SimpleLinearReference”
Atribut | Definiție | Tip | Voidability
fromPosition | Poziția inițială a elementului liniar, exprimată ca distanță față de punctul inițial al elementului de rețea liniară, de-a lungul geometriei sale curbilinii. | Length |
offset | O ramificație de la geometria liniei mediane a legăturii generalizate, după caz; o ramificație pozitivă este orientată spre dreapta pe direcția legăturii, o ramificație negativă, spre stânga. | Length | voidable
toPosition | Poziția finală a elementului liniar, exprimată ca distanță față de punctul inițial al elementului de rețea liniară, de-a lungul geometriei sale curbilinii. | Length |
5.2.5. Referință punctuală simplă (SimplePointReference)
Referință de rețea, limitată la un punct pe un element de rețea liniară. Punctul reprezintă locazarea, pe elementul de rețea, a poziției „atPosition” situată de-a lungul rețelei.
Acest tip este un subtip al „LinkReference”.
Atribute ale tipului de date „SimplePointReference”
Atribut | Definiție | Tip | Voidability
atPosition | Poziția punctului, exprimată ca distanța față de punctul inițial al elementului de rețea liniară de-a lungul geometriei sale curbilinii. | Length |
offset | Ramificație de la geometria liniei mediane a legăturii generalizate, după caz; o ramificație pozitivă este orientată spre dreapta, pe direcția legăturii, o ramificație negativă, spre stânga. | Length | voidable
5.3. Liste de coduri
5.3.1. Tip de conexiune (ConnectionTypeValue)
Tipuri de conexiuni între diferite rețele.
Această listă de coduri este administrată într-un registru comun de liste de coduri.
5.3.2. Direcția legăturii (LinkDirectionValue)
Listă de valori pentru direcții aferente unei legături.
Această listă de coduri este administrată într-un registru comun de liste de coduri.
ANEXA II
CERINȚE PRIVIND CATEGORIILE DE DATE SPAȚIALE ENUMERATE ÎN ANEXA I LA DIRECTIVA 2007/2/CE
1. SISTEME DE REFERINȚĂ DE COORDONATE
1.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
— „datum” înseamnă un parametru sau un set de parametri care definesc poziția originii, scara și orientarea unui sistem de coordonate, în conformitate cu EN ISO 19111,
— „datum geodezic” înseamnă un punct de referință care descrie relația unui sistem de coordonate cu Pământul, în conformitate cu EN ISO 19111,
— „sistem de coordonate” înseamnă un set de reguli matematice care determină modul în care urmează să se atribuie coordonate punctelor, în conformitate cu EN ISO 19111,
— „sistem de referință de coordonate” înseamnă un sistem de coordonate care este corelat cu lumea reală printr-un datum, în conformitate cu EN ISO 19111. Prezenta definiție include sistemele de coordonate bazate pe coordonatele geodezice sau carteziene, precum și sistemele de coordonate bazate pe proiecții cartografice.
— „proiecție cartografică” înseamnă o transformare a coordonatelor, bazată pe o relație biunivocă, dintr-un sistem geodezic de coordonate într-un plan, bazat pe același datum, în conformitate cu EN ISO 19111,
— „sistem de referință de coordonate compus” înseamnă un sistem de referință de coordonate care, pentru a descrie o poziție, utilizează alte două sisteme de coordonate de referință, unul pentru componenta orizontală, iar celălalt pentru componenta verticală, în conformitate cu EN ISO 19111,
— „sistem geodezic de coordonate” înseamnă un sistem de coordonate în care poziția este specificată prin latitudine geodezică, longitudine geodezică și (în cazurile tridimensionale) prin înălțime elipsoidală, în conformitate cu EN ISO 19111.
1.2. Datum pentru sistemele de referință de coordonate tridimensionale și bidimensionale
Pentru sistemele de referință de coordonate tridimensionale și bidimensionale și pentru componenta orizontală a sistemelor de referință de coordonate compuse, utilizate pentru punerea la dispoziție a seturile de date spațiale, datumul utilizat este acela al sistemului de referință terestru european din 1989 (European Terrestrial Reference System 1989 - ETRS89), în regiuni aflate în sfera sa de aplicare spațială, sau datumul sistemului de referință terestru internațional (International Terrestrial Reference System - ITRS) sau al altor sisteme de coordonate geodezice de referință conforme cu ITRS, în regiuni localizate în afara sferei de aplicare spațială a ETRS89. A fi conform cu ITRS înseamnă că definiția sistemului se bazează pe definiția ITRS și că între cele două sisteme există o relație bine documentată, în conformitate cu EN ISO 19111.
1.3. Sisteme de referință de coordonate
Seturile de date spațiale sunt puse la dispoziție prin utilizarea a cel puțin unuia dintre sistemele de referință de coordonate specificate în secțiunile 1.3.1, 1.3.2 și 1.3.3, cu excepția cazului în care se aplică una dintre condițiile specificate în secțiunea 1.3.4.
1.3.1. Sisteme de referință de coordonate tridimensionale
— Coordonate carteziene tridimensionale bazate pe un datum specificat în secțiunea 1.2 și care utilizează parametrii elipsoidului din sistemul geodezic de referință 1980 (Geodetic Reference System 1980 - GRS80).
— Coordonate geodezice tridimensionale (latitudine, longitudine și înălțime elipsoidală) bazate pe un datum specificat în secțiunea 1.2 și care utilizează parametrii elipsoidului GRS80.
1.3.2. Sisteme de referință de coordonate bidimensionale
— Coordonate geodezice bidimensionale (latitudine și longitudine) bazate pe un datum specificat în secțiunea 1.2 și care utilizează parametrii elipsoidului GRS80.
— Coordonate plane care utilizează sistemul de referință de coordonate ETRS89 prin proiecția azimutală echivalentă Lambert.
— Coordonate plane care utilizează sistemul de referință de coordonate ETRS89 prin proiecția conică conformă Lambert.
— Coordonate plane care utilizează sistemul de referință de coordonate ETRS89 prin proiecție Transversală Mercator.
1.3.3. Sisteme de referință de coordonate compuse
| 1. | În cazul componentei orizontale a sistemelor de referință de coordonate compuse, se utilizează unul dintre sistemele de referință de coordonate specificate în secțiunea 1.3.2.
| 2. | În cazul componentei verticale se utilizează unul dintre următoarele sistemele de referință de coordonate: — În cazul componentei verticale terestre, se utilizează sistemul european de referință verticală (European Vertical Reference System - EVRS) pentru exprimarea, în funcție de gravitație, a altitudinilor localizate în sfera de aplicare spațială a acestui sistem. Alte sisteme de referință verticală corelate cu câmpul gravitațional terestru sunt utilizate pentru exprimarea, în funcție de gravitație, a altitudinilor aflate în afara sferei de aplicare spațială a EVRS. — În cazul componentei verticale în atmosferă liberă, se folosește presiunea barometrică, convertită în înălțime, în conformitate cu standardul ISO 2533:1975 (Atmosfera standard internațională).
1.3.4. Alte sisteme de referință de coordonate
Există o serie de excepții în cazul cărora se pot utiliza alte sisteme de referință de coordonate decât cele prevăzute în secțiunile 1.3.1, 1.3.2 sau 1.3.3, și anume:
1. Se pot specifica alte sisteme de referință de coordonate pentru categoriile specifice de date spațiale din prezenta anexă.
2. Pentru regiunile situate în afara Europei continentale, statele membre pot defini sisteme de referință de coordonate corespunzătoare.
Codurile și parametrii geodezici necesari pentru a descrie astfel de sisteme de referință de coordonate și pentru a permite operațiile de conversie și transformare trebuie să facă obiectul unei documentări, generându-se un identificator în conformitate cu EN ISO 19111 și ISO 19127.
1.4. Sisteme de referință de coordonate utilizate pentru serviciul de vizualizare de rețea (View Network Service)
Pentru afișarea seturilor de date spațiale cu ajutorul serviciului de vizualizare de rețea, astfel cum este prevăzut în Regulamentul (CE) nr. 976/2009, sunt disponibile cel puțin sistemele de referință de coordonate pentru coordonatele geodezice bidimensionale (latitudine, longitudine).
1.5. Identificatorii sistemului de referință de coordonate
| 1. | Parametrii și identificatorii sistemului de coordonate de referință trebuie administrați într-unul sau mai multe registre comune pentru sisteme de coordonate de referință.
| 2. | Numai identificatorii incluși într-un registru comun trebuie folosiți pentru a face trimitere la sistemele de referință de coordonate enumerate în prezenta secțiune.
2. SISTEME DE CAROIAJE SPAȚIALE
2.1. Definiții
Pe lângă definițiile stabilite în articolul 2, se aplică următoarele definiții:
— „caroiaj” înseamnă o rețea alcătuită din două sau mai multe seturi de curbe în care elementele fiecărui set intersectează elementele celuilalt set într-o manieră algoritmică,
— „celulă de caroiaj” înseamnă o celulă delimitată de curbele caroiajului,
— „punct de caroiaj” înseamnă un punct localizat la intersecția a două sau mai multe curbe dintr-un caroiaj.
2.2. Caroiaje
În cadrul INSPIRE, se utilizează caroiajul specificat în secțiunea 2.2.1, cu excepția cazului în care se aplică una dintre condițiile specificate în secțiunea 2.2.2.
2.2.1. Caroiaj pentru analiză și raportare spațială paneuropeană
Caroiajul definit în prezenta secțiune este utilizată într-un cadru georeferențial în care sunt necesare rețele cu locații fixe și clar definite ale celulelor de caroiaj echivalente.
Caroiajul se bazează pe sistemul de referință de coordonate ETRS89 prin proiecție azimutală echivalentă Lambert (ETRS89-LAEA) cu centrul proiecției în punctul 52° N, 10° E și ajustarea coordonatelor estice: x0 = 4 321 000 m, ajustarea coordonatelor nordice: y0 = 3 210 000 m.
Originea caroiajului coincide cu punctul de referință relativ al sistemului de referință de coordonate ETRS89-LAEA (x = 0, y = 0).
Punctele de caroiaj ale caroiajelor bazate pe ETRS89-LAEA trebuie să coincidă cu punctele de caroiaj ale caroiajului în cauză.
Caroiajul este ierarhizat, cu rezoluții de 1 m, 10 m, 100 m, 1 000 m, 10 000 m și 100 000 m.
Caroiajul este orientat sud-nord, vest-est.
Caroiajul este desemnat ca Grid_ETRS89-LAEA. În scopul identificării unui nivel individual de rezoluție se adaugă dimensiunea celulei în metri.
Punctul de referință al unei celule de caroiaj este colțul stâng inferior al celulei respective.
Pentru referențierea și identificarea neechivocă a unei celule de caroiaj, în cadrul ETRS89-LAEA se utilizează codul celulei alcătuit din dimensiunea celulei și coordonatele colțului stâng inferior al celulei. Dimensiunea celulei se notează în metri („m”) pentru dimensiuni ale celulei de până la 100 m sau în kilometri („km”) pentru dimensiuni ale celulei mai mari sau egale cu 1 000 m. Valorile coordonatelor nord și ale coordonatelor est se divid prin 10n, unde n reprezintă numărul de zero-uri din valoarea dimensiunii celulei.
2.2.2. Alte caroiaje
Există o serie de excepții în cazul cărora se pot utiliza alte caroiaje decât cele prevăzute în secțiunea 2.2.1, și anume:
1. Se pot specifica alte caroiaje pentru categorii specifice de date spațiale din prezenta anexă. În acest caz, datele modificate prin utilizarea unui astfel de caroiaj specific categoriei folosesc standarde în care definiția caroiajului este inclusă împreună cu datele sau corelată prin referințe.
2. Pentru referențierea caroiajului în regiuni situate în afara Europei continentale, statele membre pot defini propriul caroiaj pe baza unui sistem geodezic de coordonate de referință, conform cu ITRS și o proiecție azimutală echivalentă Lambert, urmărind aceleași principii ca și cele stabilite pentru caroiajul specificat în secțiunea 2.2.1. În acest caz, se creează un identificator pentru sistemul de coordonate de referință.
3. DENUMIRI GEOGRAFICE
3.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru schimbul și clasificarea obiectelor spațiale din seturile de date corelate cu categoria de date spațiale „Denumiri geografice”:
— Loc denumit
3.1.1. Loc denumit (NamedPlace)
Orice entitate reală la care se face referire cu ajutorul unuia sau mai multor nume proprii.
Atribute ale tipului de obiect spațial „NamedPlace”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Geometrie asociată locului denumit. Această specificație a datelor nu limitează tipurile de geometrie. | GM_Object |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
leastDetailedViewingResolution | Rezoluție, exprimată ca invers al unei scări indicative sau ca distanță la sol, dincolo de care locul denumit și denumirea (denumirile) asociată(e) acestuia nu mai trebuie afișate într-un serviciu de vizualizare de bază. | MD_Resolution | voidable
localType | Caracterizarea tipului de entitate desemnată printr-o denumire sau prin denumiri geografice, astfel cum a/au fost definită(e) de furnizorul de date, redactată(e) în cel puțin una din limbile oficiale ale Uniunii Europene. | LocalisedCharacterString | voidable
mostDetailedViewingResolution | Rezoluție, exprimată ca invers al unei scări indicative sau ca distanță la sol, dincoace de care locul denumit și denumirea (denumirile) asociată(e) acestuia nu mai trebuie afișate într-un serviciu de vizualizare de bază. | MD_Resolution | voidable
name | Denumirea locului denumit. | GeographicalName |
relatedSpatialObject | Identificator al unui obiect spațial care reprezintă aceeași entitate, dar care apare în alte categorii ale INSPIRE, dacă este cazul. | Identifier | voidable
type | Caracterizare a tipului de entitate desemnată prin denumirea (denumirile) geografică (geografice). | NamedPlaceTypeValue | voidable
3.2. Tipuri de date
3.2.1. Denumire geografică (GeographicalName)
Substantiv propriu aplicat unei entități din lumea reală.
Atribute ale tipului de date „GeographicalName”
Atribut | Definiție | Tip | Voidability
grammaticalGender | Clasă de substantive reflectate în comportamentul cuvintelor asociate. | GrammaticalGenderValue | voidable
grammaticalNumber | Categorie gramaticală de substantive care exprimă distincții la cuantificare. | GrammaticalNumberValue | voidable
language | Limba denumirii, redactată sub forma unui cod de trei litere, în conformitate cu ISO 639-3 sau ISO 639-5. | CharacterString | voidable
nameStatus | Informații calitative care permit să se discearnă credibilitatea care trebuie acordată denumirii în ceea ce privește standardizarea și/sau pertinența acestuia. | NameStatusValue | voidable
nativeness | Informații care permit să se recunoască dacă denumirea este cea care este/a fost utilizată în regiunea în care este situat obiectul spațial la momentul în care denumirea este/era în uz. | NativenessValue | voidable
pronunciation | Pronunția adecvată, corectă sau standard (standard în cadrul comunității lingvistice vizate) a denumirii geografice. | PronunciationOfName | voidable
sourceOfName | Sursa de date din care provine denumirea geografică și din care aceasta este integrată în setul de date în cadrul căruia este furnizată/publicată. În cazul anumitor obiecte spațiale denumite, acest atribut se poate referi din nou la setul de date destinat publicării, dacă nu este disponibilă nicio altă informație. | CharacterString | voidable
spelling | Modul adecvat de scriere a denumirii geografice. | SpellingOfName |
3.2.2. Pronunția denumirii (PronunciationOfName)
Pronunția adecvată, corectă sau literară (literară în cadrul comunității lingvistice vizate) a unei denumiri.
Atribute ale tipului de date „PronunciationOfName ”
Atribut | Definiție | Tip | Voidability
pronunciationIPA | Pronunția adecvată, corectă sau standard (standard în cadrul comunității lingvistice vizate) a unei denumiri, exprimată cu ajutorul alfabetului fonetic internațional (International Phonetic Alphabet - IPA). | CharacterString | voidable
pronunciationSoundLink | Pronunția adecvată, corectă sau standard (standard în cadrul comunității lingvistice vizate) a unei denumiri, exprimată cu ajutorul unui link către un fișier audio. | URI | voidable
Constrângeri ale tipului de date „PronunciationOfName”
Cel puțin unul dintre cele două atribute „pronunciationSoundLink” și „pronunciationIPA” nu este nul.
3.2.3. Ortografia denumirii (SpellingOfName)
Modalitatea de scriere corectă a unei denumiri.
Atribute ale tipului de date „SpellingOfName”
Atribut | Definiție | Tip | Voidability
script | Set de simboluri grafice (de exemplu, un alfabet) utilizat la scrierea denumirii, exprimat prin folosirea codurilor din patru litere definite în ISO 15924, dacă este cazul. | CharacterString | voidable
text | Modalitatea în care este scrisă denumirea. | CharacterString |
transliterationScheme | Metodă utilizată pentru conversia denumirilor între sisteme de scriere diferite. | CharacterString | voidable
3.3. Liste de coduri
3.3.1. Gen gramatical (GrammaticalGenderValue)
Genul gramatical al unei denumiri geografice.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
3.3.2. Număr gramatical (GrammaticalNumberValue)
Numărul gramatical al unei denumiri geografice.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
3.3.3. Statutul denumirii (NameStatusValue)
Statutul unei denumiri geografice, cu alte cuvinte informațiile care permit să se determine gradul de credibilitate care trebuie acordat denumirii în ceea ce privește standardizarea și/sau pertinența acesteia.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
3.3.4. Tipul de loc denumit (NamedPlaceTypeValue)
Tipul unui loc denumit.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
3.3.5. Origine (NativenessValue)
Originea unei denumiri geografice.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
3.4. Straturi
Strat pentru categoria de date spațiale „Geographical Names”
Numele stratului | Titlul stratului | Tip de obiect spațial
GN.GeographicalNames | Denumiri geografice | NamedPlace
4. UNITĂȚI ADMINISTRATIVE
4.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru schimbul și clasificarea obiectelor spațiale din seturile de date aferente categoriei de date spațiale „Unități administrative”:
— Frontieră administrativă
— Unitate administrativă
— Condominiu
— Regiune NUTS
4.1.1. Frontieră administrativă (AdministrativeBoundary)
Linie de demarcație între unități administrative.
Atribute ale tipului de obiect spațial „AdministrativeBoundary”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
country | Cod de țară alcătuit din două caractere, în conformitate cu Ghidul stilistic interinstituțional publicat de Oficiul pentru Publicații al Uniunii Europene. | CountryCode |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Reprezentare geometrică a liniei de demarcație. | GM_Curve |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
legalStatus | Statut juridic al frontierei administrative. | LegalStatusValue | voidable
nationalLevel | Nivelurile ierarhice ale tuturor unităților administrative din care face parte frontiera în cauză. | AdministrativeHierarchyLevel |
technicalStatus | Statutul tehnic al frontierei administrative. | TechnicalStatusValue | voidable
Roluri de asociere ale tipului de obiect spațial „AdministrativeBoundary”
Rol de asociere | Definiție | Tip | Voidability
admUnit | Unitățile administrative separate de frontiera administrativă. | AdministrativeUnit | voidable
4.1.2. Unitate administrativă (AdministrativeUnit)
Unitate administrativă în care un stat membru deține și/sau își exercită jurisdicția, în ceea ce privește guvernarea la nivel local, regional și național.
Atribute ale tipului de obiect spațial „AdministrativeUnit ”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
country | Codul de țară alcătuit din două caractere, în conformitate cu Ghidul stilistic interinstituțional publicat de Oficiul pentru Publicații al Uniunii Europene. | CountryCode |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Reprezentare geometrică a teritoriului acoperit de unitatea administrativă. | GM_MultiSurface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Denumire geografică națională oficială a unității administrative, redactată în mai multe limbi, după caz. | GeographicalName |
nationalCode | Identificator tematic corespunzător codurilor administrative naționale definite în fiecare țară. | CharacterString |
nationalLevel | Nivelul la care se situează unitatea administrativă în ierarhia administrativă națională. | AdministrativeHierarchyLevel |
nationalLevelName | Numele nivelului la care se situează unitatea administrativă în ierarhia administrativă națională. | LocalisedCharacterString | voidable
residenceOfAuthority | Centrul de administrație națională sau locală. | ResidenceOfAuthority | voidable
Roluri de asociere ale tipului de obiect spațial „AdministrativeUnit ”
Rol de asociere | Definiție | Tip | Voidability
administeredBy | Unitate administrativă situată la același nivel în ierarhia administrativă națională, care administrează această unitate administrativă. | AdministrativeUnit | voidable
boundary | Frontierele administrative dintre unitatea administrativă și toate unitățile adiacente acesteia. | AdministrativeBoundary | voidable
coAdminister | Unitate administrativă situată la același nivel în ierarhia administrativă națională care este coadministrată de această unitate administrativă. | AdministrativeUnit | voidable
condominium | Condominiu administrat de unitatea administrativă. | Condominium | voidable
lowerLevelUnit | Unități situate la un nivel inferior în ierarhia administrativă națională, care sunt administrate de unitatea administrativă | AdministrativeUnit | voidable
NUTS | Regiune NUTS care, din punct de vedere topologic, include unitatea administrativă. | NUTSRegion | voidable
upperLevelUnit | Unitate situată la un nivel superior în ierarhia administrativă națională, administrată de unitatea administrativă. | AdministrativeUnit | voidable
Constrângeri ale tipului de obiect spațial „AdministrativeUnit”
Rolul de asociere „condominiu” se aplică exclusiv unităților administrative pentru care „nationalLevel” = „ «1st order» ” (nivel de țară).
Nicio unitate situată la nivelul cel mai scăzut nu poate fi relaționată la unități situate la un nivel inferior.
Nicio unitate situată la nivelul cel mai înalt nu poate fi relaționată la unități situate la un nivel superior.
4.1.3. Condominiu (Condominium)
Teritoriu administrativ organizat independent de orice diviziune administrativă teritorială națională și administrată de două sau mai multe țări.
Atribute ale tipului de obiect spațial „Condominium”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Reprezentare geometrică a teritoriului acoperit de condominiu. | GM_MultiSurface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Denumire geografică oficială a condominiului, redactată în mai multe limbi, după caz. | GeographicalName | voidable
Roluri de asociere ale tipului de obiect spațial „Condominium”
Rol de asociere | Definiție | Tip | Voidability
admUnit | Unitate administrativă care administrează condominiul. | AdministrativeUnit | voidable
4.1.4. Regiune NUTS (NUTSRegion)
Unitate teritorială de statistică definită în cadrul Regulamentului (CE) nr. 1059/2003 al Parlamentului European și al Consiliului din 26 mai 2003.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Unități statistice” din anexa III la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „NUTSRegion”
Atribut | Definiție | Tip | Voidability
NUTSCode | Cod unic al unității teritoriale pentru statistică definit în cadrul Regulamentului (CE) nr. 1059/2003 al Parlamentului European și al Consiliului din 26 mai 2003. | CharacterString |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Reprezentare geometrică a teritoriului acoperit de regiunea NUTS. | GM_MultiSurface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
4.2. Tipuri de date
4.2.1. Reședința autorității (ResidenceOfAuthority)
Tip de date reprezentând numele și poziția unei reședințe a autorității.
Atribute ale tipului de date „ResidenceOfAuthority”
Atribut | Definiție | Tip | Voidability
geometry | Poziția reședinței autorității. | GM_Point | voidable
name | Numele reședinței autorității. | GeographicalName |
4.3. Enumerări
4.3.1. Statut juridic (LegalStatusValue)
Descrierea statutului juridic al frontierelor administrative.
Valori permise pentru enumerarea „LegalStatusValue”
Valoare | Definiție
agreed | Frontiera comună a fost convenită de unitățile administrative învecinate și este stabilă în prezent.
notAgreed | Frontiera comună nu a fost convenită deocamdată de unitățile administrative învecinate și poate fi supusă modificării.
4.3.2. Statut tehnic (TechnicalStatusValue)
Descrierea statutului tehnic al frontierelor administrative.
Valori permise pentru enumerarea „TechnicalStatusValue”
Valoare | Definiție
edgeMatched | Frontierele unităților administrative învecinate au același set de coordonate.
notEdgeMatched | Frontierele unităților administrative învecinate nu au același set de coordonate.
4.4. Liste de coduri
4.4.1. Nivel al ierarhiei administrative (AdministrativeHierarchyLevel)
Niveluri administrative în cadrul ierarhiei administrative naționale. Această listă de coduri reflectă nivelul structurilor administrative în cadrul piramidei ierarhice, care este bazat pe agregarea geometrică de teritorii și care nu descrie în mod necesar legătura de subordonare existentă între autoritățile administrative conexe.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
4.5. Cerințe specifice categoriei
| 1. | Fiecare apariție a unui tip de obiect spațial „AdministrativeUnit”, cu excepția unităților la nivel național reprezentând un stat membru și unitățile coadministrate, face referire cu precizie la o anumită unitate plasată la un nivel superior al ierarhiei administrative. Această corespondență se exprimă prin rolul de asociere „upperLevelUnit” al tipului de obiect spațial „AdministrativeUnit”.
| 2. | Fiecare apariție a unui tip de obiect spațial „AdministrativeUnit”, cu excepția celor situate la nivelul cel mai scăzut, face referire la unitățile de nivel inferior corespunzătoare acesteia. Această corespondență este exprimată prin rolul de asociere „lowerLevelUnit” a tipului de obiect spațial „AdministrativeUnit”.
| 3. | Dacă o unitate administrativă este coadministrată de două sau mai multe alte unități administrative, se utilizează rolul de asociere „administeredBy”. Unitățile care coadministrează unitatea respectivă trebuie să aplice rolul invers „coAdminister”.
| 4. | Unitățile administrative situate la același nivel în ierarhia administrativă nu trebuie să partajeze zone comune din punct de vedere conceptual.
| 5. | Aparițiile tipului de obiect spațial „AdministrativeBoundary” corespund limitelor din structura topologică a diagramei complete a frontierei (care include toate nivelurile).
| 6. | Este posibil ca extinderea spațială a unui condominiu să nu facă parte din geometria reprezentând extinderea spațială a unei unități administrative.
| 7. | Condominiile pot fi administrate numai de unități administrative la nivel național.
4.6. Straturi
Straturi pentru categoria de date spațiale „Administrative Units”
Numele stratului | Titlul stratului | Tip de obiect spațial
AU.AdministrativeUnit | Unitate administrativă | AdministrativeUnit
AU.AdministrativeBoundary | Frontieră administrativă | AdministrativeBoundary
AU.Condominium | Condominiu | Condominium
AU.NUTSRegion | Regiune NUTS | NUTSRegion
5. ADRESE
5.1. Definiții
Pe lângă definițiile stabilite în articolul 2, se aplică următoarele definiții:
— „obiect adresabil” înseamnă un obiect spațial căruia este pertinent să i se asocieze adrese.
5.2. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru schimbul și clasificarea obiectelor spațiale din seturile de date corelate cu categoria de date spațiale „Adrese”:
— Adresă
— Denumire de zonă de adrese
— Componenta adresei
— Denumirea unității administrative
— Indicativ poștal
— Denumirea magistralei
5.2.1. Adresă (Address)
Identificare a locației fixe a proprietății prin intermediul unei structuri ordonate de denumiri geografice și de identificatori.
Atribute ale tipului de obiect spațial „Address ”
Atribut | Definiție | Tip | Voidability
alternativeIdentifier | Identificator tematic extern al obiectului spațial de adresă, care permite interoperabilitatea cu sistemele sau aplicațiile moștenite existente. | CharacterString | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
locator | Desemnare sau denumire lizibile. | AddressLocator |
position | Poziția unui punct caracteristic care reprezintă locația adresei în conformitate cu o anumită specificație, inclusiv informații cu privire la originea poziției. | GeographicPosition |
status | Validitatea adresei în cadrul ciclului de viață (versiune) al obiectului spațial de adresă. | StatusValue | voidable
validFrom | Data și ora începând cu care această versiune a adresei a devenit sau va deveni valabilă în lumea reală. | DateTime | voidable
validTo | Data și ora la care această versiune a adresei a încetat sau va înceta să existe în lumea reală. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial „Address ”
Rol de asociere | Definiție | Tip | Voidability
building | Clădire căreia îi este atribuită sau cu care este asociată adresa respectivă. | Tip care urmează să fie specificat în categoria de date spațiale „Clădiri” | voidable
component | Indică faptul că elementul de adresă face parte din adresa respectivă. | AddressComponent |
parcel | Parcelă cadastrală căreia îi este atribuită sau cu care este asociată adresa respectivă. | CadastralParcel | voidable
parentAddress | Adresa principală (mamă) de care (sub)adresa respectivă este strâns legată. | Address | voidable
Constrângeri ale tipului de obiect spațial „Address”
O adresă trebuie să aibă un obiect spațial al cărui element de adresă corespunzător unității administrative este 1 (țară).
O adresă trebuie să aibă exact o poziție spațială implicită (atributul „default” al obiectului spațial „GeographicPosition” trebuie să fie „true”).
5.2.2. Denumire de zonă de adresă (AddressAreaName)
Element al adresei care reprezintă denumirea unei regiuni geografice sau a unei localități și care reunește un număr de obiecte adresabile pentru a facilita adresabilitatea, fără a fi unitate administrativă.
Acest tip este un subtip al „AddressComponent”.
Atribute ale tipului de obiect spațial „AddressAreaName”
Atribut | Definiție | Tip | Voidability
name | Substantiv propriu aplicat zonei de adresă. | GeographicalName |
Roluri de asociere ale tipului de obiect spațial „AddressAreaName”
Rol de asociere | Definiție | Tip | Voidability
namedPlace | Locul denumit pe care această denumire de zona de adresă îl reprezintă. | NamedPlace | voidable
5.2.3. Element de adresă (AddressComponent)
Identificator sau denumire geografică a unei regiuni geografice caracteristice, a unei locații, sau a unui alt obiect spațial care definește sfera de aplicare a unei adrese.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „AddressComponent”
Atribut | Definiție | Tip | Voidability
alternativeIdentifier | Identificator tematic extern al obiectului spațial al elementului de adresă, care permite interoperabilitatea cu sistemele sau aplicațiile existente. | CharacterString | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
status | Validitatea elementului de adresă în cadrul ciclului de viață (versiune) al obiectului spațial al elementului de adresă. | StatusValue | voidable
validFrom | Data și ora începând cu care versiunea elementului de adresă a devenit sau va deveni valabilă în lumea reală. | DateTime | voidable
validTo | Data și ora la care versiunea elementului de adresă a încetat/va înceta să existe în lumea reală. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial „AddressComponent”
Rol de asociere | Definiție | Tip | Voidability
situatedWithin | Un alt element de adresă în cadrul căruia se situează obiectul spațial reprezentat de acest element de adresă. | AddressComponent | voidable
5.2.4. Denumirea unității administrative (AdminUnitName)
Un element de adresă care reprezintă denumirea unei unități administrative în care un stat membru deține/își exercită jurisdicția, în ceea ce privește guvernarea locală, regională și națională.
Acest tip este un subtip al „AddressComponent”.
Atribute ale tipului de obiect spațial „AdminUnitName”
Atribut | Definiție | Tip | Voidability
level | Nivelul de administrare din ierarhia administrativă națională. | AdministrativeHierarchyLevel |
name | Denumire geografică oficială a unității administrative, redactată în diferite limbi, după caz. | GeographicalName |
Roluri de asociere ale tipului de obiect spațial „AdminUnitName”
Rol de asociere | Definiție | Tip | Voidability
adminUnit | Unitatea administrativă care reprezintă sursa conținutului denumirii unității administrative. | AdministrativeUnit | voidable
5.2.5. Indicativ poștal (PostalDescriptor)
Element de adresă care reprezintă identificarea unei subdiviziuni a adreselor și a punctelor de distribuire a corespondenței dintr-o țară, regiune sau oraș în scopuri poștale.
Acest tip este un subtip al „AddressComponent”.
Atribute ale tipului de obiect spațial „PostalDescriptor ”
Atribut | Definiție | Tip | Voidability
postCode | Cod creat și menținut în scopuri poștale pentru a identifica o subdiviziune a adreselor și a punctelor de distribuire a corespondenței. | CharacterString |
postName | Unul sau mai mult nume create și întreținute în scopuri poștale pentru a identifica o subdiviziune a adreselor și a punctelor de distribuire a corespondenței. | GeographicalName |
Constrângeri ale tipului de obiect spațial „PostalDescriptor”
Dacă nu există niciun cod poștal, este necesar un nume poștal.
Dacă nu există niciun nume poștal, este necesar un cod poștal.
5.2.6. Denumirea magistralei (ThoroughfareName)
Element de adresă care reprezintă denumirea unui pasaj sau a unei căi de la o locație la alta.
Acest tip este un subtip al „AddressComponent.”
Atribute ale tipului de obiect spațial „ThoroughfareName”
Atribut | Definiție | Tip | Voidability
name | Denumirea magistralei. | ThoroughfareNameValue |
Roluri de asociere ale tipului de obiect spațial „ThoroughfareName”
Rol de asociere | Definiție | Tip | Voidability
transportLink | Una sau mai multe căi de legătură ale rețelelor de transport cărora li s-a atribuit obiectul spațial al denumirii magistralei. | TransportLink | voidable
5.3. Tipuri de date
5.3.1. Localizator de adresă (AddressLocator)
Indicator lizibil pentru om sau denumire care permite unui utilizator sau unei aplicații să facă trimitere și să distingă o adresă de adresele învecinate, în cadrul sferei de aplicare a denumirii unei magistrale, a denumirii de zonă de adresă, a denumirii unității administrative sau a indicativului poștal, în care este situată adresa.
Atribute ale tipului de date „AddressLocator ”
Atribut | Definiție | Tip | Voidability
designator | Număr sau secvență de caractere care identifică în mod unic localizatorul în cadrul sferei (sferelor) de aplicare relevante. | LocatorDesignator |
level | Nivelul la care se referă localizatorul. | LocatorLevelValue |
name | Denumire geografică sau text descriptiv asociat unei proprietăți identificate de localizator. | LocatorName |
Roluri de asociere ale tipului de date „AddressLocator ”
Rol de asociere | Definiție | Tip | Voidability
withinScopeOf | Element de adresă care definește sfera de aplicare în cadrul căreia se atribuie localizatorul, în conformitate cu normele care asigură univocitatea. | AddressComponent | voidable
Constrângerile tipului de date „AddressLocator”
Dacă nu există un indicator, este necesară o denumire.
Dacă nu există o denumire, este necesar un indicator.
5.3.2. Reprezentarea adresei (AddressRepresentation)
Reprezentarea unui obiect spațial al unei adrese pentru utilizarea în schemele de aplicații externe care trebuie să includă, într-o manieră lizibilă, informațiile de bază privind adresa.
Atribute ale tipului de date „AddressRepresentation”
Atribut | Definiție | Tip | Voidability
addressArea | Denumirea sau denumirile unei regiuni geografice sau a (ale) unei localități și care reunește un număr de obiecte adresabile pentru a facilita adresabilitatea, fără a fi unitate administrativă. | GeographicalName | voidable
adminUnit | Denumirea sau denumirile unei unități administrative în care un stat membru deține și/sau își exercită jurisdicția, în ceea ce privește conducerea locală, regională și națională. | GeographicalName |
locatorDesignator | Număr sau șir de caractere care permite unui utilizator sau unei aplicații să interpreteze, să analizeze sintactic și să formateze localizatorul în cadrul sferei de aplicare relevante. Un localizator poate include mai mulți identificatori de localizator. | CharacterString |
locatorName | Substantiv propriu (proprii) aplicat(e) entității reale identificate de localizator. | GeographicalName |
postCode | Cod creat și administrat în scopuri poștale pentru a identifica o subdiviziune a adreselor și a punctelor de distribuire a corespondenței. | CharacterString | voidable
postName | Una sau mai multe denumiri create și menținute în scopuri poștale pentru a identifica o subdiviziune a adreselor și a punctelor de distribuire a corespondenței. | GeographicalName | voidable
thoroughfare | Denumirea sau denumirile unui pasaj sau a (ale) unei căi de la o locație la alta, de exemplu, o șosea sau o cale navigabilă. | GeographicalName | voidable
Roluri de asociere ale tipului de date „AddressRepresentation”
Rol de asociere | Definiție | Tip | Voidability
addressFeature | Trimitere la obiectul spațial de tip adresă. | Address | voidable
5.3.3. Poziția geografică (GeographicPosition)
Poziția unui punct caracteristic care reprezintă locația adresei în conformitate cu o anumită specificație, inclusiv informațiile cu privire la originea poziției.
Atribute ale tipului de date „GeographicPosition”
Atribut | Definiție | Tip | Voidability
default | Specifică dacă poziția trebuie considerată implicită sau nu. | Boolean |
geometry | Poziția punctului exprimată prin coordonate în sistemul spațial de referință ales. | GM_Point |
method | Prezentarea modului în care a fost creată sau derivată poziția geografică a adresei, și de către cine. | GeometryMethodValue | voidable
specification | Informații care definesc specificația utilizată pentru crearea sau derivarea acestei poziții geografice a adresei. | GeometrySpecificationValue | voidable
5.3.4. Identificator de localizator (LocatorDesignator)
Număr sau șir de caractere care identifică în mod unic localizatorul în cadrul sferei (sferelor) de aplicare relevant(e). Identificarea integrală a localizatorului poate include unul sau mai mulți identificatori de localizator.
Atribute ale tipului de date „LocatorDesignator”
Atribut | Definiție | Tip | Voidability
designator | Componentă de identificare a identificatorului de localizator compus din una sau mai multe cifre sau alte caractere. | CharacterString |
type | Tipul valorii localizatorului, care permite unei aplicații să interpreteze, să analizeze sintactic și să formateze adresa în conformitate cu anumite norme. | LocatorDesignatorTypeValue |
5.3.5. Denumire de localizator (LocatorName)
Nume propriu aplicat entității din lumea reală identificate cu ajutorul localizatorului.
Atribute ale tipului de date „LocatorName”
Atribut | Definiție | Tip | Voidability
name | Componenta de identificare a denumirii localizatorului. | GeographicalName |
type | Tipul valorii localizatorului, care permite unei aplicații să interpreteze, să analizeze sintactic și să formateze adresa în conformitate cu anumite norme. | LocatorNameTypeValue |
5.3.6. Componentă de denumire (PartOfName)
O parte din denumirea completă care rezultă din subîmpărțirea numelui magistralei în componente semantice distincte, prin utilizarea aceleiași limbi și aceluiași sistem de scriere ca și în cazul denumirii complete a magistralei.
Atribute ale tipului de date „PartOfName”
Atribut | Definiție | Tip | Voidability
part | Șir de caractere care exprimă partea distinctă a denumirii, prin utilizarea aceleiași limbi și a aceluiași sistem de scriere ca și în cazul denumirii complete a magistralei. | CharacterString |
type | Clasificare a componentei de denumire în conformitate cu semantica (sensul) acesteia în denumirea completă a magistralei. | PartTypeValue |
5.3.7. Valoarea denumirii magistralei (ThoroughfareNameValue)
Substantiv propriu aplicat magistralei care include în mod opțional o subîmpărțire a denumirii în părți.
Atribute ale tipului de date „ThoroughfareNameValue”
Atribut | Definiție | Tip | Voidability
name | Substantiv propriu aplicat magistralei. | GeographicalName |
nameParts | Una sau mai multe părți în care poate fi subîmpărțită denumirea magistralei. | PartOfName | voidable
5.4. Liste de coduri
5.4.1. Metoda geometrică (GeometryMethodValue)
Prezentarea modului în care a fost creată sau derivată poziția geografică a adresei, și de către cine.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
5.4.2. Specificația geometrică (GeometrySpecificationValue)
Informații care definesc specificația utilizată pentru crearea sau derivarea acestei poziții geografice a adresei.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
5.4.3. Tipul identificatorului de localizator (LocatorDesignatorTypeValue)
Descriere a semanticii identificatorului de localizator.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
5.4.4. Nivelul localizatorului (LocatorLevelValue)
Nivelul la care se referă localizatorul.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
5.4.5. Tipul denumirii de localizator (LocatorNameTypeValue)
Descrierea semanticii denumirii de localizator.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
5.4.6. Tipul părții (PartTypeValue)
Clasificarea părții denumirii în conformitate cu semantica sa în cadrul denumirii complete a magistralei.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
5.4.7. Statut (StatusValue)
Validitatea actuală a adresei din lumea reală sau a componentei adresei.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
5.5. Cerințe specifice categoriei
5.5.1. Poziția adresei
| 1. | În setul de date, poziția adresei trebuie reprezentată prin coordonatele locației actuale cu cea mai mare precizie posibilă. Va fi astfel vorba despre cele mai precise coordonate măsurate direct sau, în cazul în care nu există astfel de coordonate, despre coordonatele derivate dintr-unul din elementele de adresă, acordându-se prioritate elementului care permite determinarea cu cea mai mare precizie a poziției.
| 2. | Dacă o adresă are mai mult de o poziție, atributul „specification” se populează cu o valoare diferită pentru fiecare dintre aceste poziții.
5.5.2. Roluri de asociere
| 1. | Rolul de asociere „withinScopeOf” se completează pentru toți localizatorii atribuiți în conformitate cu normele care urmăresc să asigure univocitatea în cadrul unui element specific de adresă (adică denumirea magistralei, denumirea zonei de adresă, indicativul poștal sau denumirea unității administrative).
| 2. | Rolul de asociere „parentAddress” se completează pentru toate adresele care sunt corelate cu o adresă principală.
| 3. | O adresă trebuie să aibă legătură cu denumirea țării în care este situată. Mai mult, o adresă trebuie să aibă legături cu elementele de adresă suplimentare, necesare identificării și localizării fără ambiguitate a adresei în cauză.
5.6. Straturi
Strat pentru categoria de date spațiale „Adrese”
Numele stratului | Titlul stratului | Tip de obiect spațial
AD.Address | Adrese | Address
6. PARCELE CADASTRALE
6.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale din seturile de date corelate cu categoria de date spațiale „Parcele cadastrale”:
— Unitate funciară de bază
— Frontieră cadastrală
— Parcelă cadastrală
— Zonare cadastrală
Întotdeauna trebuie să fie puse la dispoziție parcele cadastrale.
Unitățile funciare de bază sunt puse la dispoziție de către statele membre în care limitele cadastrale unice sunt redactate exclusiv pentru unitățile funciare de bază și nu pentru parcele.
Frontierele cadastrale sunt puse la dispoziție de către statele membre în care se înregistrează informații cu o acuratețe absolută de poziționare pentru tipul de frontieră respectiv.
6.1.1. Unitate funciară de bază (BasicPropertyUnit)
Unitate funciară de bază care este înregistrată în cărțile sau registrele funciare sau echivalentele acestora. Aceasta se definește prin drepturi de proprietate funciară exclusive și omogene și poate fi alcătuită din una sau mai multe parcele adiacente sau separate din punct de vedere geografic.
Atribute ale tipului de obiect spațial „BasicPropertyUnit ”
Atribut | Definiție | Tip | Voidability
areaValue | Valoare înregistrată a suprafeței care oferă o cuantificare a suprafeței proiectate pe planul orizontal al parcelelor cadastrale care alcătuiesc unitatea funciară de bază. | Area | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
nationalCadastralReference | Identificator tematic la nivel național, în general codul național complet al unității funciare de bază. Acesta trebuie să asigure legătura cu registrul cadastral național sau cu echivalentul acestuia. | CharacterString |
validFrom | Data și ora oficiale la care unitatea funciară de bază a fost/va fi constituită legal. | DateTime | voidable
validTo | Data și ora oficiale la care unitatea funciară de bază a încetat / va înceta să fie folosită. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial „BasicPropertyUnit ”
Rol de asociere | Definiție | Tip | Voidability
administrativeUnit | Unitate administrativă la cel mai scăzut nivel administrativ care include respectiva unitate funciară de bază. | AdministrativeUnit | voidable
Constrângeri ale tipului de obiect spațial „BasicPropertyUnit”
Valoarea „areaValue” este exprimată în metri pătrați.
6.1.2. Frontiera cadastrală (CadastralBoundary)
Parte a conturului unei parcele cadastrale. O frontieră cadastrală poate fi partajată de două parcele cadastrale învecinate.
Atribute ale tipului de obiect spațial „CadastralBoundary ”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
estimatedAccuracy | Estimarea acurateței de poziționare absolută a frontierei cadastrale în cadrul sistemului de referință de coordonate INSPIRE utilizat. Acuratețea de poziționare absolută reprezintă valoarea medie a incertitudinilor de poziționare pentru un set de poziții, în care incertitudinile de poziționare reprezintă distanța dintre o poziție măsurată și ceea ce se consideră a fi poziția reală corespunzătoare. | Length | voidable
geometry | Geometria frontierei cadastrale. | GM_Curve |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
validFrom | Data și ora oficiale la care frontiera cadastrală a fost/va fi constituită legal. | DateTime | voidable
validTo | Data și ora oficiale la care frontiera cadastrală a încetat/ va înceta să fie folosită. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial „CadastralBoundary ”
Rol de asociere | Definiție | Tip | Voidability
parcel | Parcelă (parcele) cadastrală (cadastrale) delimitată(e) de această frontieră cadastrală. O frontieră cadastrală poate delimita una sau două parcele cadastrale. | CadastralParcel | voidable
Constrângeri ale tipului de obiect spațial „CadastralBoundary”
Valoarea „estimatedAccuracy” este exprimată în metri.
6.1.3. Parcela cadastrală (CadastralParcel)
Suprafețe definite prin registrele cadastrale sau echivalente ale acestora.
Atribute ale tipului de obiect spațial „CadastralParcel ”
Atribut | Definiție | Tip | Voidability
areaValue | Valoare înregistrată a suprafeței care exprimă cuantificarea suprafeței proiectate pe planul orizontal al parcelei cadastrale. | Area | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Geometria parcelei cadastrale. | GM_Object |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
label | Text folosit în mod uzual pentru afișarea identificării parcelei cadastrale. | CharacterString |
nationalCadastralReference | Identificator tematic la nivel național, în general codul național complet al parcelei cadastrale. Acesta trebuie să asigure legătura cu registrul cadastral național sau cu echivalentul acestuia. | CharacterString |
referencePoint | Un punct din interiorul parcelei cadastrale. | GM_Point | voidable
validFrom | Data și ora oficiale la care parcela cadastrală a fost/va fi constituită legal. | DateTime | voidable
validTo | Data și ora oficiale la care parcela cadastrală a încetat/va înceta să fie folosită. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial „CadastralParcel ”
Rol de asociere | Definiție | Tip | Voidability
administrativeUnit | Unitate administrativă la cel mai scăzut nivel administrativ cuprinzând această parcelă cadastrală. | AdministrativeUnit | voidable
basicPropertyUnit | Unitate (unități) funciară de bază cuprinzând această parcelă cadastrală. | BasicPropertyUnit | voidable
zoning | Zonare cadastrală la cel mai scăzut nivel cuprinzând această parcelă cadastrală. | CadastralZoning | voidable
Constrângeri ale tipului de obiect spațial „CadastralParcel”
Valoarea „areaValue” se exprimă în metri pătrați.
Tipul de geometrie trebuie să fie „GM_Surface” sau „GM_MultiSurface”.
6.1.4. Zonarea cadastrală (CadastralZoning)
Suprafețe intermediare utilizate pentru a împărți teritoriul național în parcele cadastrale.
Atribute ale tipului de obiect spațial „CadastralZoning ”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
estimatedAccuracy | Estimarea acurateței de poziționare absolută a parcelelor cadastrale în cadrul zonării cadastrale în sistemul de referință de coordonate INSPIRE utilizat. Acuratețea de poziționare absolută reprezintă valoarea medie a incertitudinilor de poziționare pentru un set de poziții, unde incertitudinile de poziționare reprezintă distanța dintre o poziție măsurată și ceea ce se consideră a fi poziția reală corespunzătoare. | Length | voidable
geometry | Geometria zonării cadastrale. | GM_MultiSurface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
label | Text folosit în mod uzual pentru afișarea identificării zonării cadastrale. | CharacterString |
level | Nivel al zonării cadastrale în cadrul ierarhiei cadastrale naționale. | CadastralZoningLevelValue | voidable
levelName | Numele nivelului zonării cadastrale în cadrul ierarhiei cadastrale naționale, în cel puțin una dintre limbile oficiale ale Uniunii Europene. | LocalisedCharacterString | voidable
name | Numele zonării cadastrale. | GeographicalName | voidable
nationalCadastalZoningReference | Identificator tematic la nivel național, în general codul național complet al zonării cadastrale. | CharacterString |
originalMapScaleDenominator | Numitorul din scara hărții în format hârtie originale (după caz) a cărei întindere îi corespunde zonarea cadastrală. | Integer | voidable
referencePoint | Punct în cadrul zonării cadastrale. | GM_Point | voidable
validFrom | Data și ora oficiale la care zonarea cadastrală a fost/va fi constituită legal. | DateTime | voidable
validTo | Data și ora oficiale la care zonarea cadastrală a încetat/ va înceta să fie folosită. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial „CadastralZoning ”
Rol de asociere | Definiție | Tip | Voidability
upperLevelUnit | Zonarea cadastrală de la nivelul imediat superior care include zonarea cadastrală în cauză. | CadastralZoning | voidable
Constrângeri ale tipului de obiect spațial „CadastralZoning”
Valoarea „estimatedAccuracy” se exprimă în metri.
O zonare cadastrală la nivel inferior trebuie inclusă într-o zonare la nivel superior.
6.2. Liste de coduri
6.2.1. Nivelul zonării cadastrale (CadastralZoningLevelValue)
Nivele ierarhice ale zonărilor cadastrale.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
6.3. Cerințe specifice categoriei
6.3.1. Reprezentarea geometrică
| 3. | Domeniul de valoare al proprietăților spațiale definite în prezenta secțiune nu este limitat la schema spațială „Entitate simplă” definită în EN ISO 19125-1.
| 4. | Dacă sunt furnizate frontierele cadastrale, frontierele care corespund conturului unei parcele cadastrale formează un inel (inele) închis(e).
6.3.2. Modelarea referințelor obiectului
Toate instanțele tipului de obiect spațial „CadastralParcel” au drept identificator tematic atributul „nationalCadastralReference”. Atributul respectiv trebuie să permită utilizatorilor să stabilească conexiuni cu drepturile, proprietarii și alte informații cadastrale din registrele cadastrale naționale sau echivalentele acestora.
6.3.3. Sisteme de referință de coordonate
Dacă datele corelate cu categoria de date spațiale „Parcele cadastrale” sunt puse la dispoziție în coordonate plane utilizând proiecția conică conformă a lui Lambert, datele respective sunt de asemenea puse la dispoziție sub forma a cel puțin unui sistem de referință de coordonate diferit, specificat în secțiunile 1.3.1, 1.3.2 și 1.3.3.
6.4. Norme de reprezentare
6.4.1. Straturi
Strat pentru categoria de date spațiale „Parcele cadastrale”
Numele stratului | Titlul stratului | Tip de obiect spațial
CP.CadastralParcel | Parcelă cadastrală | CadastralParcel
CP.CadastralZoning | Zonare cadastrală | CadastralZoning
CP.CadastralBoundary | Frontieră cadastrală | CadastralBoundary
7. REȚELE DE TRANSPORT
7.1. Definiții
Pe lângă definițiile stabilite în articolul 2, se aplică următoarele definiții:
— „punct de referință de aerodrom” înseamnă locația geografică desemnată a unui aerodrom, situată lângă centrul geometric inițial sau planificat al aerodromului și care în mod normal rămâne în locul stabilit inițial,
— „aeroport/eliport” înseamnă o suprafață delimitată pe uscat sau pe apă (inclusiv clădiri, instalații și echipamente) menită a fi utilizată, fie în totalitate, fie parțial, pentru sosirea, plecarea și deplasarea la sol a aeronavelor/elicopterelor,
— „rută cu apă adâncă” înseamnă o rută aflată într-o zonă desemnată între limite definite și care a făcut obiectul unor ridicări precise ce au permis analizarea fundului mării și a obstacolelor subacvatice în condițiile unei adâncimi minime de apă date.
— „conexiune intermodală” înseamnă o conexiune între două elemente din rețele de transport diferite care utilizează un mod diferit de transport, oferind posibilitatea de transbordare a elementelor transportate (persoane, mărfuri etc.) de la un mod de transport la altul,
— „element liniar” înseamnă un obiect unidimensional care este utilizat drept axă de-a lungul căreia se efectuează referențierea liniară,
— „referențiere liniară” înseamnă specificația unei locații în funcție de un obiect unidimensional, utilizată drept măsurătoare de-a lungul elementului respectiv (și, în mod facultativ, abatere de la acesta),
— „echipament de asistare a navigației” înseamnă un echipament fizic de asistare a navigației plasat pe suprafața terestră, de exemplu Very High Frequency Omnidirectional Radio Range (VOR), Distance Measuring Equipment (DME), localizator, Tactical Air Navigation Beacon (TACAN) etc., care servește la ghidarea în siguranță a traficului aerian pe rutele aeriene existente,
— „referențierea obiectului” înseamnă precizarea întinderii spațiale a unui obiect prin referirea la un obiect spațial existent sau la un ansamblu de obiecte spațiale,
— „gară de triaj” înseamnă o zonă traversată de un număr de șine paralele de cale ferată (de obicei mai mult de două) interconectate, care sunt utilizate pentru oprirea trenurilor în scopul încărcării/descărcării mărfurilor fără a întrerupe traficul pe o linie de cale ferată principală,
— „punct semnificativ” înseamnă o locație geografică specificată utilizată pentru a defini o rută „Air Traffic Service (ATS)”, traseul de zbor al unei aeronave sau în alte scopuri legate de navigație/ATS.
7.2. Structura categoriei de date spațiale „Rețele de transport”
Tipurile specificate pentru categoria de date spațiale „Rețele de transport” sunt structurate în următoarele grupuri:
— Elemente comune de transport
— Rețea de transport aerian
— Rețea de transport pe cablu
— Rețea de transport feroviar
— Rețea de transport rutier
— Rețea de transport pe apă
7.3. Elemente comune de transport
7.3.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu elementele comune de transport:
— Restricție de acces
— Starea instalației
— Autoritatea responsabilă cu întreținerea
— Bornă
— Autoritatea deținătoare
— Restricții pentru vehicule
— Direcția fluxului traficului
— Zonă de transport
— Legătură de transport
— Succesiune de legături de transport
— Set de legături de transport
— Rețea de transport
— Nod de transport
— Obiect de transport
— Punct de transport
— Proprietate a transportului
— Poziție verticală
7.3.1.1. Restricție de acces (AccessRestriction)
Restricție a accesului la un element de transport.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „AccessRestriction”
Atribut | Definiție | Tip | Voidability
restriction | Natura restricției de acces. | AccessRestrictionValue |
7.3.1.2. Starea instalației (ConditionOfFacility)
Statutul unui element de rețea de transport în ceea ce privește stadiul de terminare a lucrărilor și exploatarea acestuia.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „ConditionOfFacility”
Atribut | Definiție | Tip | Voidability
currentStatus | Valoarea statutului actual al elementului de rețea de transport în ceea ce privește stadiul de terminare a lucrărilor și exploatarea acestuia. | ConditionOfFacilityValue |
7.3.1.3. Autoritatea responsabilă cu întreținerea (MaintenanceAuthority)
Autoritatea responsabilă cu întreținerea elementului de transport.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „MaintenanceAuthority”
Atribut | Definiție | Tip | Voidability
authority | Identificarea autorității responsabile cu întreținerea. | CI_Citation |
7.3.1.4. Bornă (MarkerPost)
Indicator de referință amplasat de-a lungul unei căi dintr-o rețea de transport, în general la intervale regulate, care indică distanța de la începutul căii, sau de la un alt punct de referință, până la punctul în care se află indicatorul respectiv.
Acest tip este un subtip al „TransportPoint”.
Atribute ale tipului de obiect spațial „MarkerPost”
Atribut | Definiție | Tip | Voidability
location | Distanța de la începutul căii, sau de la un alt punct de referință, până la punctul în care se află indicatorul. | Distance |
Roluri de asociere ale tipului de obiect spațial „MarkerPost”
Rol de asociere | Definiție | Tip | Voidability
route | Rută dintr-o rețea de transport de-a lungul căreia este amplasată borna. | TransportLinkSet | voidable
7.3.1.5. Autoritatea deținătoare (OwnerAuthority)
Autoritatea care deține elementul de transport.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „OwnerAuthority”
Atribut | Definiție | Tip | Voidability
authority | Identificarea autorității deținătoare. | CI_Citation |
7.3.1.6. Restricții pentru vehicule (RestrictionForVehicles)
Restricții pentru vehicule pe un element de transport.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RestrictionForVehicles”
Atribut | Definiție | Tip | Voidability
measure | Măsura privind restricția. | Measure |
restrictionType | Tipul restricției. | RestrictionTypeValue |
7.3.1.7. Direcția fluxului traficului (TrafficFlowDirection)
Indică direcția fluxului traficului în funcție de direcția vectorului căii de transport.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „TrafficFlowDirection ”
Atribut | Definiție | Tip | Voidability
direction | Indică direcția fluxului traficului. | LinkDirectionValue |
Constrângeri ale tipului de obiect spațial „TrafficFlowDirection”
Această proprietate poate fi asociată numai cu un obiect spațial de tip „Link” sau „LinkSequence”.
7.3.1.8. Zonă de transport (TransportArea)
Suprafață care reprezintă întinderea spațială a unui element al unei rețele de transport.
Acest tip este un subtip al „NetworkArea”.
Acest tip este un subtip al „TransportObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportArea ”
Atribut | Definiție | Tip | Voidability
validFrom | Data de la care zona de transport a început să existe în lumea reală. | DateTime | voidable
validTo | Data de la care zona de transport nu mai există în lumea reală. | DateTime | voidable
Constrângeri ale tipului de obiect spațial „TransportArea”
Toate zonele de transport au un identificator de obiect extern.
7.3.1.9. Legătură de transport (TransportLink)
Obiect spațial liniar care descrie geometria și conectivitatea unei rețele de transport între două puncte din rețeaua respectivă.
Acest tip este un subtip al „Link”.
Acest tip este un subtip al „TransportObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportLink ”
Atribut | Definiție | Tip | Voidability
validFrom | Data de la care legătura de transport a început să existe în lumea reală. | DateTime | voidable
validTo | Data de la care legătura de transport nu mai există în lumea reală. | DateTime | voidable
Constrângeri ale tipului de obiect spațial „TransportLink”
Toate legăturile de transport au un identificator de obiect extern.
7.3.1.10. Succesiune de legături de transport (TransportLinkSequence)
Obiect spațial liniar, alcătuit dintr-un ansamblu ordonat de legături de transport, care reprezintă un traseu neîntrerupt din rețeaua de transport lipsită de ramificații. Elementul are un început și un sfârșit definite, fiecare poziție din succesiunea de legături de transport fiind identificabilă printr-un parametru unic, de exemplu lungimea. Acesta descrie un element al rețelei de transport, caracterizat prin unul sau mai mulți identificatori și/sau proprietăți.
Acest tip este un subtip al „LinkSequence”.
Acest tip este un subtip al „TransportObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportLinkSequence ”
Atribut | Definiție | Tip | Voidability
validFrom | Data de la care succesiunea de legături de transport a început să existe în lumea reală. | DateTime | voidable
validTo | Data de la care succesiunea de legături de transport nu mai există în lumea reală. | DateTime | voidable
Constrângeri ale tipului de obiect spațial „TransportLinkSequence”
O succesiune de legături de transport trebuie să fie alcătuită din legături de transport care aparțin aceleiași rețele de transport.
Toate succesiunile de legături de transport au un identificator de obiect extern.
7.3.1.11. Set de legături de transport (TransportLinkSet)
Ansamblu de succesiuni de legături de transport și/sau legături individuale de transport care are o funcție sau o semnificație specifică într-o rețea de transport.
Acest tip este un subtip al „LinkSet”.
Acest tip este un subtip al „TransportObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportLinkSet ”
Atribut | Definiție | Tip | Voidability
validFrom | Data de la care setul de legături de transport a început să existe în lumea reală. | DateTime | voidable
validTo | Data de la care setul de legături de transport nu mai există în lumea reală. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial „TransportLinkSet ”
Rol de asociere | Definiție | Tip | Voidability
post | Bornă de-a lungul unei rute dintr-o rețea de transport. | MarkerPost | voidable
Constrângeri ale tipului de obiect spațial „TransportLinkSet”
Un set de legături de transport trebuie să fie alcătuit din legături de transport și/sau succesiuni de legături de transport care aparțin aceleiași rețele de transport.
Toate seturile de legături de transport au un identificator de obiect extern.
7.3.1.12. Rețea de transport (TransportNetwork)
Ansamblu de elemente de rețea care aparțin unui singur mod de transport.
Acest tip este un subtip al „Network”.
Atribute ale tipului de obiect spațial „TransportNetwork”
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
typeOfTransport | Tip de rețea de transport, bazat pe tipul de infrastructură pe care o utilizează rețeaua. | TransportTypeValue |
7.3.1.13. Nod de transport (TransportNode)
Un obiect spațial punctual utilizat pentru conectivitate.
Acest tip este un subtip al „Node”.
Acest tip este un subtip al „TransportObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportNode ”
Atribut | Definiție | Tip | Voidability
validFrom | Data de la care nodul de transport a început să existe în lumea reală. | DateTime | voidable
validTo | Data de la care nodul de transport nu mai există în lumea reală. | DateTime | voidable
Constrângeri ale tipului de obiect spațial „TransportNode”
Toate nodurile de transport au un identificator de obiect extern.
7.3.1.14. Obiect de transport (TransportObject)
Bază de identificare pentru obiectele rețelei de transport în lumea reală.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportObject”
Atribut | Definiție | Tip | Voidability
geographicalName | Denumire geografică utilizată pentru identificarea obiectului rețelei de transport în lumea reală. Aceasta rerezintă „cheia” pentru a asocia în mod implicit diferite reprezentări ale obiectului. | GeographicalName | voidable
7.3.1.15. Punct de transport (TransportPoint)
Obiect spațial punctual – care nu este nod – care reprezintă poziția unui element de rețea de transport.
Acest tip este un subtip al „NetworkElement”.
Acest tip este un subtip al „TransportObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportPoint ”
Atribut | Definiție | Tip | Voidability
geometry | Localizarea punctului de transport. | GM_Point |
validFrom | Data de la care punctul de transport a început să existe în lumea reală. | DateTime | voidable
validTo | Data după care punctul de transport nu mai există în lumea reală. | DateTime | voidable
Constrângeri ale tipului de obiect spațial „TransportPoint”
Toate punctele de transport au un identificator de obiect extern.
7.3.1.16. Proprietate a transportului (TransportProperty)
Referință la o proprietate care se aplică rețelei. Proprietatea se poate aplica întregului element de rețea cu care este asociată sau – în cazul obiectelor spațiale liniare – poate fi descrisă prin utilizarea referențierii liniare.
Acest tip este un subtip al „NetworkProperty”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „TransportProperty ”
Atribut | Definiție | Tip | Voidability
validFrom | Data de la care proprietatea transportului a început să existe în lumea reală. | DateTime | voidable
validTo | Data după care proprietatea transportului nu mai există în lumea reală. | DateTime | voidable
Constrângeri ale tipului de obiect spațial „TransportProperty”
Toate proprietățile rețelei de transport au un identificator de obiect extern.
7.3.1.17. Poziție verticală (VerticalPosition)
Nivel vertical relativ la alte elemente de rețea de transport.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „VerticalPosition”
Atribut | Definiție | Tip | Voidability
verticalPosition | Poziție verticală relativă a elementului de transport. | VerticalPositionValue |
7.3.2. Enumerări
7.3.2.1. Tip de transport (TransportTypeValue)
Posibile tipuri de rețele de transport.
Valori permise pentru enumerarea „TransportTypeValue”
Valoare | Definiție
air | Este vorba despre o rețea de transport aerian.
cable | Este vorba despre o rețea de transport pe cablu.
rail | Este vorba despre o rețea de transport feroviar.
road | Este vorba despre o rețea de transport rutier.
water | Este vorba despre o rețea de transport pe apă.
7.3.3. Liste de coduri
7.3.3.1. Restricție de acces (AccessRestrictionValue)
Tipuri de restricții de acces pentru un element de transport.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.3.3.2. Tip de restricție (RestrictionTypeValue)
Posibile restricții pentru vehiculele care pot accesa un element de transport.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4. Rețeaua de transport aerian
7.4.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale asociate rețelei de transport aerian:
— Zona aerodromului
— Categoria aerodromului
— Nod de aerodrom
— Tip de aerodrom
— Legătură aeriană
— Succesiune de legături aeriene
— Nod aerian
— Rută aeriană
— Rută aeriană de legătură
— Zonă de spațiu aerian
— Zona platformei
— Starea instalației aeriene
— Punct desemnat
— Lungimea elementului
— Lățimea elementului
— Altitudinea terenului
— Procedură de apropiere instrumentală
— Limita de altitudine inferioară
— Asistarea navigației
— Legătură de procedură
— Zona pistei de aterizare și decolare
— Punctul de pe linia mediană a zonei pistei de aterizare și decolare
— Sosire instrumentală standard
— Plecare instrumentală standard
— Compoziția suprafeței
— Zona căii de rulare
— Zona prizei de contact și de decolare
— Limita superioară de altitudine
— Restricție de exploatare
7.4.1.1. Zona aerodromului (AerodromeArea)
Suprafață delimitată pe uscat sau pe apă, (incluzând clădiri, instalații și echipamente) menită a fi utilizată, fie în totalitate, fie parțial, pentru sosirea, plecarea și deplasarea la sol a aeronavelor și/sau a elicopterelor.
Acest tip este un subtip al „TransportArea”.
7.4.1.2. Categoria aerodromului (AerodromeCategory)
Categoria aerodromului din punctul de vedere al sferei de aplicare și importanța serviciilor de trafic aerian furnizate de și către aerodromul respectiv.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „AerodromeCategory ”
Atribut | Definiție | Tip | Voidability
aerodromeCategory | Valoare care arată categoria unui aerodrom. | AerodromeCategoryValue |
Constrângeri ale tipului de obiect spațial „AerodromeCategory”
Această proprietate poate fi asociată numai cu un obiect spațial care este nod de aerodromuri sau zonă a aerodromului.
7.4.1.3. Nod de aerodromuri (AerodromeNode)
Nod localizat pe un aeroport/eliport în punctul de referință al aerodromului, utilizat pentru reprezentarea simplificată a acestuia.
Acest tip este un subtip al „AirNode”.
Atribute ale tipului de obiect spațial „AerodromeNode”
Atribut | Definiție | Tip | Voidability
designatorIATA | Cod IATA al aerodromului (aeroport/eliport), alcătuit din trei litere. | CharacterString | voidable
locationIndicatorICAO | Indicator ICAO de amplasament al aerodromului (aeroport/eliport) alcătuit din patru litere, enumerat în ICAO DOC 7910. | CharacterString | voidable
Roluri de asociere ale tipului de obiect spațial „AerodromeNode”
Rol de asociere | Definiție | Tip | Voidability
controlTowers | Ansamblu de turnuri de control aparținând unui aerodrom (aeroport/eliport). | Tip care urmează a fi specificat în categoria de date spațiale „Buildings” | voidable
7.4.1.4. Tip de aerodrom (AerodromeType)
Cod care specifică tipul de aerodrom.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „AerodromeType ”
Atribut | Definiție | Tip | Voidability
aerodromeType | Tipul de aerodrom. | AerodromeTypeValue |
Constrângeri ale tipului de obiect spațial „AerodromeType”
Această proprietate poate fi asociată numai cu un obiect spațial care este nod de aerodromuri sau zonă a aerodromului.
7.4.1.5. Legătură aeriană (AirLink)
Obiect spațial liniar care descrie geometria și conectivitatea rețelei aeriene dintre două puncte din rețea.
Acest tip este un subtip al „TransportLink”.
Acest tip este abstract.
7.4.1.6. Succesiune de legături aeriene (AirLinkSequence)
Obiect spațial liniar, alcătuit dintr-un ansamblu ordonat de legături aeriene, care reprezintă un traseu neîntrerupt din rețeaua aeriană, fără ramificații.
Acest tip este un subtip al „TransportLinkSequence”.
7.4.1.7. Nod aerian (AirNode)
Nod care există într-o rețea aeriană.
Acest tip este un subtip al „TransportNode”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „AirNode”
Atribut | Definiție | Tip | Voidability
significantPoint | Atribut care indică dacă nodul aerian reprezintă sau nu un punct semnificativ. | Boolean |
7.4.1.8. Rută aeriană (AirRoute)
Rută specificată destinată să canalizeze fluxul traficului, necesară pentru prestarea de servicii de trafic aerian, de la sfârșitul fazei de decolare și urcare inițială până la începutul fazei de apropiere și aterizare.
Acest tip este un subtip al „TransportLinkSet”.
Atribute ale tipului de obiect spațial „AirRoute”
Atribut | Definiție | Tip | Voidability
airRouteType | Clasificarea rutei. | AirRouteTypeValue | voidable
designator | Cod sau indicator care identifică o rută aeriană. | CharacterString | voidable
7.4.1.9. Rută aeriană de legătură (AirRouteLink)
Porțiune a rutei care va fi urmată de obicei fără o oprire intermediară, astfel cum este definită de două puncte semnificative consecutive.
Acest tip este un subtip al „AirLink”.
Atribute ale tipului de obiect spațial „AirRouteLink”
Atribut | Definiție | Tip | Voidability
airRouteLinkClass | Clasa sau tipul legături de rută aeriană. | AirRouteLinkClassValue | voidable
7.4.1.10. Zona de spațiu aerian (AirspaceArea)
Volum definit în spațiu, descris ca proiecție orizontală cu limite verticale.
Acest tip este un subtip al „TransportArea”.
Atribute ale tipului de obiect spațial „AirspaceArea”
Atribut | Definiție | Tip | Voidability
AirspaceAreaType | Cod indicând structura generală sau caracteristicile unui anumit spațiu aerian. | AirspaceAreaTypeValue |
7.4.1.11. Zona platformei (ApronArea)
Zonă definită pe un aerodrom/eliport terestru, destinată staționării aeronavelor/elicopterelor în scopul îmbarcării sau debarcării pasagerilor, încărcării sau descărcării corespondenței sau mărfurilor, alimentării cu combustibil, staționării sau întreținerii.
Acest tip este un subtip al „TransportArea”.
7.4.1.12. Starea instalației aeriene (ConditionOfAirFacility)
Starea unui element de rețea de transport aerian din punctul de vedere al terminării lucrărilor și exploatării sale.
Acest tip este un subtip al „ConditionOfFacility”.
Constrângeri ale tipului de obiect spațial „ConditionOfAirFacility”
Această proprietate poate fi asociată numai cu un obiect spațial care este nod de aerodromuri, zonă a aerodromului sau zonă a pistei de decolare și de aterizare.
7.4.1.13. Punct desemnat (DesignatedPoint)
Locație geografică nemarcată de poziția unui sistem de radionavigație, utilizată pentru definirea unei rute ATS, a traiectoriei zborului unei aeronave sau pentru alte scopuri legate de navigație sau ATS.
Acest tip este un subtip al „AirNode”.
Atribute ale tipului de obiect spațial „DesignatedPoint”
Atribut | Definiție | Tip | Voidability
designator | Indicator codificat al punctului. | CharacterString | voidable
7.4.1.14. Lungimea elementului (ElementLength)
Lungimea fizică a elementului.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „ElementLength ”
Atribut | Definiție | Tip | Voidability
length | Lungimea fizică a elementului. | Measure |
Constrângeri ale tipului de obiect spațial „ElementLength”
Această proprietate poate fi asociată numai cu un obiect spațial care este zonă a pistei de decolare și de aterizare, zonă a pistei de rulare sau zonă a prizei de contact și de decolare.
7.4.1.15. Lățimea elementului (ElementWidth)
Lățimea fizică a elementului.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „ElementWidth ”
Atribut | Definiție | Tip | Voidability
width | Lățimea fizică a elementului. | Measure |
Constrângeri ale tipului de obiect spațial „ElementWidth”
Această proprietate poate fi asociată numai cu un obiect spațial care este zonă a pistei de decolare și de aterizare, zonă a pistei de rulare sau zonă a prizei de contact și de decolare.
7.4.1.16. Altitudinea terenului (FieldElevation)
Altitudine a aerodromului, exprimată ca distanța verticală dintre cel mai înalt punct al zonei de aterizare a unui aerodrom și nivelul mediu al mării.
Acest tip este un subtip al TransportProperty.
Atribute ale tipului de obiect spațial „FieldElevation ”
Atribut | Definiție | Tip | Voidability
altitude | Valoarea altitudinii terenului. | Measure |
Constrângeri ale tipului de obiect spațial „FieldElevation”
Această proprietate poate fi asociată numai cu un obiect spațial care este nod de aerodromuri sau zonă a aerodromului.
7.4.1.17. Procedură de apropiere instrumentală (InstrumentApproachProcedure)
O serie de manevre predeterminate efectuate exclusiv cu ajutorul instrumentelor de zbor, cu o marjă specificată de protecție împotriva obstacolelor de la punctul inițial de apropiere sau, după caz, de la începutul unei rute de sosire definite, până în punctul în care aterizarea poate fi efectuată și, ulterior, dacă aterizarea nu s-a finalizat, către o poziție în care se aplică criteriile privind înlăturarea obstacolelor fixe sau în zbor.
Acest tip este un subtip al „ProcedureLink”.
7.4.1.18. Limita inferioară de altitudine (LowerAltitudeLimit)
Altitudine care definește limita inferioară a unui obiect al unei rețele de transport aerian.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „LowerAltitudeLimit ”
Atribut | Definiție | Tip | Voidability
altitude | Valoarea limitei de altitudine. | Measure |
Constrângeri ale tipului de obiect spațial „LowerAltitudeLimit”
Această proprietate poate fi asociată numai cu un obiect spațial care este rută aeriană de legătură sau zonă a spațiului aerian.
7.4.1.19. Asistarea navigației (Navaid)
Unul sau mai multe echipamente de asistare a navigației cu care se realizează servicii de navigație.
Acest tip este un subtip al „AirNode”.
Atribute ale tipului de obiect spațial „Navaid”
Atribut | Definiție | Tip | Voidability
designator | Identificator codificat atribuit sistemului de asistare a navigației. | CharacterString | voidable
navaidType | Tip de serviciu de asistare a navigației. | NavaidTypeValue | voidable
7.4.1.20. Legătură de procedură (ProcedureLink)
O serie de manevre predeterminate în scopul evitării obstacolelor.
Acest tip este un subtip al „AirLink”.
7.4.1.21. Zona pistei de decolare și de aterizare (RunwayArea)
Zonă rectangulară definită pe un aeroport/eliport, pregătită pentru aterizarea și decolarea aeronavelor.
Acest tip este un subtip al „TransportArea”.
Atribute ale tipului de obiect spațial „RunwayArea”
Atribut | Definiție | Tip | Voidability
designator | Indicatorul textual complet al pistei de decolare și aterizare, utilizat pentru identificarea în mod exclusiv a acesteia, în cazul unui aerodrom/eliport cu mai multe piste. | CharacterString | voidable
runwayType | Tipul de pistă de decolare și de aterizare, fie pistă de decolare și de aterizare pentru avioane, fie zonă de apropiere finală și de decolare (FATO) pentru elicoptere. | RunwayTypeValue | voidable
7.4.1.22. Punctul de pe linia mediană a pistei de decolare și de aterizare (RunwayCentrelinePoint)
O poziție semnificativă din punct de vedere operațional pe linia mediană a direcției unei piste de decolare și aterizare.
Acest tip este un subtip al „AirNode”.
Atribute ale tipului de obiect spațial „RunwayCentrelinePoint”
Atribut | Definiție | Tip | Voidability
pointRole | Rolul punctului de-a lungul direcției liniei mediane a pistei de decolare și aterizare. | PointRoleValue |
7.4.1.23. Sosire instrumentală standard (StandardInstrumentArrival)
Rută de sosire desemnată pe baza regulilor de zbor instrumental (IFR), care face legătura între un punct semnificativ, de obicei situat pe o rută ATS, și un punct din care poate fi inițiată o procedură publicată de apropiere instrumentală.
Acest tip este un subtip al „ProcedureLink”.
Atribute ale tipului de obiect spațial „StandardInstrumentArrival”
Atribut | Definiție | Tip | Voidability
designator | Indicator textual al sosirii instrumentale standard. | CharacterString | voidable
7.4.1.24. Plecare instrumentală standard (StandardInstrumentDeparture)
Rută de plecare desemnată pe baza regulilor de zbor instrumental (IFR), care face legătura între aerodrom sau o anumită pistă de decolare și de aterizare a aerodromului, și un anumit punct semnificativ, situat de obicei pe o rută ATS desemnată, din care începe faza de zbor de croazieră.
Acest tip este un subtip al „ProcedureLink”.
Atribute ale tipului de obiect spațial „StandardInstrumentDeparture”
Atribut | Definiție | Tip | Voidability
designator | Indicator textual complet al plecării instrumentale standard. | CharacterString | voidable
7.4.1.25. Compoziția suprafeței (SurfaceComposition)
Compoziția suprafeței unui aerodrom/eliport.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „SurfaceComposition ”
Atribut | Definiție | Tip | Voidability
surfaceComposition | Cod care indică compoziția suprafeței unui aerodrom/eliport. | SurfaceCompositionValue |
Constrângeri ale tipului de obiect spațial „SurfaceComposition”
Această proprietate poate fi asociată numai cu un obiect spațial care este zonă a pistei de decolare și de aterizare, zonă a căii de rulare, zonă a platformei sau zonă de desprindere și de contact.
7.4.1.26. Zona căii de rulare (TaxiwayArea)
Traseu definit pe un aerodrom/eliport pentru rularea aeronavelor/elicopterelor și destinat să ofere o legătură între o parte și cealaltă a aeroportului.
Acest tip este un subtip al „TransportArea”.
Atribute ale tipului de obiect spațial „TaxiwayArea”
Atribut | Definiție | Tip | Voidability
designator | Indicator textual al căii de rulare. | CharacterString | voidable
7.4.1.27. Zona de desprindere și de contact (TouchDownLiftOff)
Zonă de susținere a sarcinilor, unde un elicopter poate ateriza sau de unde poate decola.
Acest tip este un subtip al „AirNode”.
Atribute ale tipului de obiect spațial „TouchDownLiftOff”
Atribut | Definiție | Tip | Voidability
designator | Indicator textual al zonei prizei de contact și de decolare. | CharacterString | voidable
7.4.1.28. Limită superioară de altitudine (UpperAltitudeLimit)
Altitudine care definește limita superioară a unui obiect al unei rețele de transport aerian.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „UpperAltitudeLimit ”
Atribut | Definiție | Tip | Voidability
altitude | Valoarea limitei de altitudine. | Measure |
Constrângeri ale tipului de obiect spațial „UpperAltitudeLimit”
Această proprietate poate fi asociată numai cu un obiect spațial care este rută aeriană de legătură sau zonă a spațiului aerian.
7.4.1.29. Restricție de exploatare (UseRestriction)
Restricții în utilizarea unui obiect de rețea aeriană.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „UseRestriction ”
Atribut | Definiție | Tip | Voidability
restriction | Tipul de restricție a exploatării pentru obiectul de rețea aeriană. | AirUseRestrictionValue |
Constrângeri ale tipului de obiect spațial „UseRestriction”
Această proprietate poate fi asociată numai cu un obiect spațial care reprezintă o rută aeriană, o conexiune aeriană (sau o conexiune aeriană specializată), un nod aerian (sau un nod aerian specializat) sau o zonă a aerodromului.
7.4.2. Liste de coduri
7.4.2.1. Categoria aerodromului (AerodromeCategoryValue)
Categorii posibile de aerodromuri în funcție de sfera de aplicare și importanța serviciilor de trafic aerian furnizate de și pentru aerodromurile respective.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.2. Tipul aerodromului (AerodromeTypeValue)
Cod care specifică dacă poziția unei anumite entități reprezintă un aerodrom sau un eliport.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.3. Clasa de rută aeriană de legătură (AirRouteLinkClassValue)
Tipul rutei din punct de vedere al navigației.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.4. Tipul rutei aeriene (AirRouteTypeValue)
Clasificarea rutei ca rută ATS sau rută nord-atlantică.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.5. Restricția de exploatare aeriană (AirUseRestrictionValue)
Restricția de exploatare pentru un obiect de rețea aeriană.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.6. Tipul de zonă a spațiului aerian (AirspaceAreaTypeValue)
Tipuri recunoscute de spațiu aerian.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.7. Tipul de asistare a navigației (NavaidTypeValue)
Tipuri de servicii de asistare a navigației.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.8. Rolul punctului (PointRoleValue)
Rolul punctului de pe linia mediană a pistei de decolare și de aterizare.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.9. Tipul pistei de decolare și aterizare (RunwayTypeValue)
Cod care introduce o distincție între pistele de decolare și de aterizare pentru avioane și FATO pentru elicoptere.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.4.2.10. Compoziția suprafeței (SurfaceCompositionValue)
Cod care indică compoziția unei suprafețe.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.5. Rețeaua de transport pe cablu
7.5.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu rețeaua de transport pe cablu:
— Cale de transport pe cablu
— Succesiune de legături de transport pe cablu
— Set de legături de transport pe cablu
— Nod de transport pe cablu
7.5.1.1. Cale de transport pe cablu (CablewayLink)
Obiect spațial liniar care descrie geometria și conectivitatea unei rețele de transport pe cablu între două puncte dintr-o rețea de transport pe cablu.
Acest tip este un subtip al „TransportLink”.
Atribute ale tipului de obiect spațial „CablewayLink”
Atribut | Definiție | Tip | Voidability
cablewayType | Tipul de transport pe cablu. | CablewayTypeValue | voidable
7.5.1.2. Succesiune de legături de transport pe cablu (CablewayLinkSequence)
Ansamblu ordonat de legături de transport pe cablu care sunt caracterizate de unul sau mai mulți identificatori tematici și/sau proprietăți.
Acest tip este un subtip al „TransportLinkSequence”.
7.5.1.3. Set de legături de transport pe cablu (CablewayLinkSet)
Ansamblu de succesiuni de legături de transport pe cablu și/sau căi de transport pe cablu individuale, care are o funcție sau semnificație specifică într-o rețea de transport pe cablu.
Acest tip este un subtip al „TransportLinkSet”.
7.5.1.4. Nod de rețea de transport pe cablu (CablewayNode)
Obiect spațial punctual care este utilizat pentru reprezentarea conectivității dintre două legături de transport pe cablu consecutive.
Acest tip este un subtip al „TransportNode”.
7.5.2. Liste de coduri
7.5.2.1. Tipul de transport pe cablu (CablewayTypeValue)
Posibile tipuri de transport pe cablu.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.6. Rețea de transport feroviar
7.6.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale vor fi utilizate pentru modificarea și clasificarea obiectelor spațiale asociate rețelei de transport feroviar:
— Viteză proiectată
— Ecartamentul nominal al liniilor
— Număr de linii
— Zonă de cale ferată
— Electrificarea unei căi ferate
— Linie de cale ferată
— Conexiune de cale ferată
— Succesiune de conexiuni de cale ferată
— Nod de cale ferată
— Zonă de gară feroviară
— Cod de gară feroviară
— Nod de gară feroviară
— Tipul de cale ferată
— Utilizare a căii ferate
— Zona gării de triaj
— Nod de gară de triaj
7.6.1.1. Viteză proiectată (DesignSpeed)
Specificația vitezei maxime pentru care este proiectată o linie de cale ferată.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „DesignSpeed ”
Atribut | Definiție | Tip | Voidability
speed | Specificația vitezei maxime pentru care este proiectată o linie de cale ferată. | Velocity |
Constrângeri ale tipului de obiect spațial „DesignSpeed”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport feroviar.
7.6.1.2. Ecartamentul nominal al liniilor (NominalTrackGauge)
Distanța nominală dintre cele două șine exterioare (ecartament) ale unei linii de cale ferată.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „NominalTrackGauge ”
Atribut | Definiție | Tip | Voidability
nominalGauge | Valoare unică de identificare a ecartamentului liniilor. | Measure | voidable
nominalGaugeCategory | Indicație privind clasificarea ecartamentului unei linii de cale ferată ca o categorie vagă în raport cu ecartamentul nominal standard european. | TrackGaugeCategoryValue | voidable
Constrângeri ale tipului de obiect spațial „NominalTrackGauge”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport feroviar.
7.6.1.3. Număr de linii (NumberOfTracks)
Număr de linii pentru un sector feroviar.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „NumberOfTracks ”
Atribut | Definiție | Tip | Voidability
minMaxNumberOfTracks | Indică dacă numărul de linii este calculat ca valoare minimă sau maximă. | MinMaxTrackValue | voidable
numberOfTracks | Numărul actual de linii. | Integer |
Constrângeri ale tipului de obiect spațial „NumberOfTracks”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport feroviar.
7.6.1.4. Zonă de cale ferată (RailwayArea)
Suprafață ocupată de o linie de cale ferată, inclusiv balastul.
Acest tip este un subtip al „TransportArea”.
7.6.1.5. Electrificare a unei căi ferate (RailwayElectrification)
Indică dacă o cale ferată este dotată cu un sistem electric pentru tracțiunea vehiculelor care se deplasează de-a lungul căii ferate respective.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RailwayElectrification ”
Atribut | Definiție | Tip | Voidability
electrified | Indică dacă o cale ferată este prevăzută cu un sistem electric pentru tracțiunea vehiculelor care se deplasează de-a lungul căii ferate respective. | Boolean |
Constrângeri ale tipului de obiect spațial „RailwayElectrification”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport feroviar.
7.6.1.6. Linie de cale ferată (RailwayLine)
Ansamblu de succesiuni de legături feroviare și sau legături feroviare individuale care sunt caracterizate de unul sau mai mulți identificatori tematici și/sau proprietăți.
Acest tip este un subtip al „TransportLinkSet”.
Atribute ale tipului de obiect spațial „RailwayLine”
Atribut | Definiție | Tip | Voidability
railwayLineCode | Cod atribuit unei linii de cale ferată, unic în cadrul unui stat membru. | CharacterString | voidable
7.6.1.7. Legătură feroviară (RailwayLink)
Obiect spațial liniar care descrie geometria și conectivitatea unei rețele feroviare între două puncte din rețeaua respectivă.
Acest tip este un subtip al „TransportLink”.
Atribute ale tipului de obiect spațial „RailwayLink”
Atribut | Definiție | Tip | Voidability
fictitious | Legătură feroviară care nu reprezintă o linie de cale ferată concretă și actuală, ci o traiectorie virtuală. | Boolean | voidable
7.6.1.8. Succesiune de legături feroviare (RailwayLinkSequence)
Obiect spațial liniar, alcătuit dintr-un ansamblu ordonat de legături feroviare, care reprezintă o cale continuă în rețeaua feroviară fără ramificări. Elementul are un început și un sfârșit definite, iar fiecare poziție din succesiunea de legături feroviare este identificabilă cu ajutorul unui singur parametru, cum ar fi lungimea. Acest obiect descrie un element al rețelei feroviare caracterizat de unul sau mai mulți identificatori tematici și/sau proprietăți.
Acest tip este un subtip al „TransportLinkSequence”.
7.6.1.9. Nod de cale ferată (RailwayNode)
Obiect spațial punctual care reprezintă un punct semnificativ de-a lungul rețelei de cale ferată sau care definește o intersecție de linii de cale ferată, utilizat pentru a descrie conectivitatea rețelei respective.
Acest tip este un subtip al „TransportNode”.
Atribute ale tipului de obiect spațial „RailwayNode”
Atribut | Definiție | Tip | Voidability
formOfNode | Funcția unui nod de cale ferată în cadrul rețelei feroviare. | FormOfRailwayNodeValue | voidable
7.6.1.10. Zona gării feroviare (RailwayStationArea)
Obiect spațial care este utilizat pentru reprezentarea limitelor topografice ale amenajărilor unei gări feroviare (construcții, gări de triaj, instalații și echipamente) destinate operațiunilor din cadrul gării feroviare respective.
Acest tip este un subtip al „TransportArea”.
7.6.1.11. Codul de gară feroviară (RailwayStationCode)
Cod unic atribuit unei gări feroviare.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RailwayStationCode ”
Atribut | Definiție | Tip | Voidability
stationCode | Cod unic atribuit unei gări feroviare. | CharacterString |
Constrângeri ale tipului de obiect spațial „RailwayStationCode”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport feroviar.
7.6.1.12. Nod de gară feroviară (RailwayStationNode)
Nod de cale ferată care reprezintă locația unei gări de-a lungul rețelei feroviare.
Acest tip este un subtip al „RailwayNode”.
Atribute ale tipului de obiect spațial „RailwayStationNode ”
Atribut | Definiție | Tip | Voidability
numberOfPlatforms | Valoare indicând numărul de peroane existente într-o gară feroviară. | Integer | voidable
Constrângeri ale tipului de obiect spațial „RailwayStationNode”
În cazul unui nod de gară feroviară, valoarea atributului „formOfNode” va fi întotdeauna „RailwayStop”.
7.6.1.13. Tipul de cale ferată (RailwayType)
Tipul de transport feroviar pentru care este proiectată linia.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RailwayType ”
Atribut | Definiție | Tip | Voidability
type | Tipul de transport feroviar pentru care este proiectată linia de cale ferată. | RailwayTypeValue |
Constrângeri ale tipului de obiect spațial „RailwayType”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport feroviar.
7.6.1.14. Utilizarea căii ferate (RailwayUse)
Utilizarea actuală a căii ferate.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RailwayUse ”
Atribut | Definiție | Tip | Voidability
use | Utilizarea actuală a căii ferate. | RailwayUseValue |
Constrângeri ale tipului de obiect spațial „RailwayUse”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport feroviar.
7.6.1.15. Zona gării de triaj (RailwayYardArea)
Obiect spațial areal care este utilizat pentru reprezentarea limitelor topografice ale unei gări de triaj.
Acest tip este un subtip al „TransportArea”.
7.6.1.16. Nod de gară de triaj (RailwayYardNode)
Nod de cale ferată care se află în zona unei gări de triaj.
Acest tip este un subtip al „RailwayNode”.
Constrângeri ale tipului de obiect spațial „RailwayYardNode”
În cazul nodului de gară de triaj, valoarea atributului „formOfNode” este întotdeauna „RailwayStop”.
7.6.2. Enumerări
7.6.2.1. Numărul minim sau maxim de linii (MinMaxTrackValue)
Valori care indică dacă numărul de linii este calculat ca număr maxim, minim sau mediu.
Valori permise pentru enumerarea „MinMaxTrackValue”
Valoare | Definiție
average | Numărul de linii reprezintă valoarea medie pentru o porțiune dată a rețelei feroviare.
maximum | Numărul de linii reprezintă valoarea maximă pentru o porțiune dată a rețelei feroviare.
minimum | Numărul de linii reprezintă valoarea minimă pentru o porțiune dată a rețelei feroviare.
7.6.2.2. Categoria ecartamentului liniilor (TrackGaugeCategoryValue)
Posibile categorii de căi ferate din punct de vedere al ecartamentului nominal al liniilor.
Valori permise pentru enumerarea „TrackGaugeCategoryValue”
Valoare | Definiție
broad | Proprietatea ecartamentului nominal al liniilor este mai largă decât ecartamentul standard.
standard | Proprietatea ecartamentului nominal al liniilor este egală cu standardul european (1 435 milimetri).
narrow | Proprietatea ecartamentului nominal al liniilor este mai îngustă decât ecartamentul standard.
notApplicable | Definiția proprietății ecartamentului nominal al liniilor nu este aplicabilă tipului respectiv de transport feroviar.
7.6.3. Liste de coduri
7.6.3.1. Forma nodului de cale ferată (FormOfRailwayNodeValue)
Posibile funcții ale nodului de cale ferată în cadrul rețelei feroviare.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.6.3.2. Tipul căii ferate (RailwayTypeValue)
Posibile tipuri de transport feroviar.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.6.3.3. Utilizarea căii ferate (RailwayUseValue)
Posibile utilizări ale căilor ferate.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7. Rețeaua de transport rutier
7.7.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu rețeaua de transport rutier:
— Drum „E”
— Forma drumului
— Categoria funcțională de drum
— Numărul benzilor de circulație
— Drum
— Zonă rutieră
— Legătură rutieră
— Succesiune de legături rutiere
— Denumirea drumului
— Nod rutier
— Zonă de servicii rutiere
— Tip de servicii rutiere
— Categoria suprafeței carosabile
— Lățimea drumului
— Limită de viteză
— Zona traficului de vehicule
7.7.1.1. Drum „E” (ERoad)
Ansamblu de succesiuni de legături rutiere și sau legături rutiere individuale reprezentând o rută care face parte din rețeaua internațională de drumuri europene, caracterizată prin numărul drumului european.
Acest tip este un subtip al „TransportLinkSet”.
Atribute ale tipului de obiect spațial „ERoad”
Atribut | Definiție | Tip | Voidability
europeanRouteNumber | Cod de identificare a rutei în cadrul rețelei internaționale de drumuri europene. Codul începe întotdeauna cu litera „E”, urmată de un număr format din una, două sau trei cifre. | CharacterString | voidable
7.7.1.2. Forma drumului (FormOfWay)
Clasificare bazată pe proprietățile fizice ale legăturii rutiere.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „FormOfWay ”
Atribut | Definiție | Tip | Voidability
formOfWay | Forma drumului din punct de vedere fizic. | FormOfWayValue |
Constrângeri ale tipului de obiect spațial „FormOfWay”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport rutier.
7.7.1.3. Categoria funcțională de drum (FunctionalRoadClass)
Clasificare bazată pe importanța rolului îndeplinit de drumul respectiv în cadrul rețelei rutiere.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „FunctionalRoadClass ”
Atribut | Definiție | Tip | Voidability
functionalClass | Clasă funcțională a legăturii rutiere în cadrul rețelei rutiere. | FunctionalRoadClassValue |
Constrângeri ale tipului de obiect spațial „FunctionalRoadClass”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport rutier.
7.7.1.4. Numărul benzilor de circulație (NumberOfLanes)
Numărul benzilor unui element rutier.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „NumberOfLanes ”
Atribut | Definiție | Tip | Voidability
direction | Indică direcția pentru care este valabil numărul de benzi respectiv. | LinkDirectionValue | voidable
minMaxNumberOfLanes | Indică dacă numărul de benzi este calculat ca valoare minimă sau maximă. | MinMaxLaneValue | voidable
numberOfLanes | Numărul de benzi. | Integer |
Constrângeri ale tipului de obiect spațial „NumberOfLanes”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport rutier.
7.7.1.5. Drum (Road)
Ansamblu de succesiuni de legături rutiere și/sau legături rutiere individuale caracterizate de unul sau mai mulți identificatori tematici și/sau proprietăți.
Acest tip este un subtip al „TransportLinkSet”.
Atribute ale tipului de obiect spațial „Road”
Atribut | Definiție | Tip | Voidability
localRoadCode | Cod de identificare atribuit drumului de către autoritatea rutieră locală. | CharacterString | voidable
nationalRoadCode | Numărul național al drumului. | CharacterString | voidable
7.7.1.6. Zona rutieră (RoadArea)
Suprafață care se extinde la limitele unui drum, incluzând zonele circulabile utilizate de vehicule și alte părți ale drumului respectiv.
Acest tip este un subtip al „TransportArea”.
7.7.1.7. Legătură rutieră (RoadLink)
Obiect spațial liniar care descrie geometria și conectivitatea unei rețele rutiere între două puncte din rețeaua respectivă. Legăturile rutiere pot fi reprezentate de drumuri, piste pentru bicicliști, șosele cu o singură bandă pe fiecare sens de circulație, șosele cu mai multe benzi pe fiecare sens de circulație și chiar traiectorii fictive care străbat piețele circulate.
Acest tip este un subtip al „TransportLink”.
7.7.1.8. Succesiune de legături rutiere (RoadLinkSequence)
Obiect spațial liniar, alcătuit dintr-un ansamblu ordonat de legături rutiere, care reprezintă o cale continuă în rețeaua rutieră fără ramificări. Elementul are un început și un sfârșit definite, iar fiecare poziție din succesiunea de legături rutiere este identificabilă cu ajutorul unui singur parametru, cum ar fi lungimea. Acest obiect descrie un element al rețelei rutiere, caracterizat de unul sau mai mulți identificatori tematici și/sau proprietăți.
Acest tip este un subtip al „TransportLinkSequence”.
7.7.1.9. Denumirea drumului (RoadName)
Denumirea unui drum, astfel cum a fost atribuită de autoritatea responsabilă.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RoadName ”
Atribut | Definiție | Tip | Voidability
name | Denumirea drumului. | GeographicalName |
Constrângeri ale tipului de obiect spațial „RoadName”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport rutier.
7.7.1.10. Nod rutier (RoadNode)
Obiect spațial punctual care este utilizat pentru a reprezenta fie conectivitatea între două legături rutiere fie un obiect spațial semnificativ, cum ar fi o stație de servicii sau o intersecție cu sens giratoriu.
Acest tip este un subtip al „TransportNode”.
Atribute ale tipului de obiect spațial „RoadNode”
Atribut | Definiție | Tip | Voidability
formOfRoadNode | Descrierea funcției unui nod rutier în cadrul rețelei de transport rutier. | FormOfRoadNodeValue | voidable
7.7.1.11. Zonă de servicii (RoadServiceArea)
Zonă alăturată unui drum și destinată furnizării de servicii speciale pentru drumul respectiv.
Acest tip este un subtip al „TransportArea”.
7.7.1.12. Tipul de servicii rutiere (RoadServiceType)
Descrierea tipului zonei de servicii și a amenajărilor disponibile.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RoadServiceType ”
Atribut | Definiție | Tip | Voidability
availableFacility | Amenajare care este disponibilă pentru o zonă de servicii dată. | ServiceFacilityValue |
type | Tipul zonei de servicii. | RoadServiceTypeValue |
Constrângeri ale tipului de obiect spațial „RoadServiceType”
Această proprietate poate fi asociată numai cu un obiect spațial de tip „RoadServiceArea” sau „RoadNode” (atunci când „formOfRoadNode” = „roadServiceArea”).
7.7.1.13. Categoria de suprafață carosabilă (RoadSurfaceCategory)
Specificație cu privire la starea suprafeței elementului rutier asociat. Aceasta indică dacă un drum este pavat sau nu.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RoadSurfaceCategory ”
Atribut | Definiție | Tip | Voidability
surfaceCategory | Tipul suprafeței drumului. | RoadSurfaceCategoryValue |
Constrângeri ale tipului de obiect spațial „RoadSurfaceCategory”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport rutier.
7.7.1.14. Lățimea drumului (RoadWidth)
Lățimea drumului, măsurată ca mărime medie.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „RoadWidth ”
Atribut | Definiție | Tip | Voidability
measuredRoadPart | Indică porțiunea de drum căreia i se aplică valoarea pentru atributul „lățime”. | RoadPartValue | voidable
width | Valoarea lățimii drumului. | Measure |
Constrângeri ale tipului de obiect spațial „RoadWidth”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport rutier.
7.7.1.15. Limită de viteză (SpeedLimit)
Limită pentru viteza unui vehicul pe un drum.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „SpeedLimit ”
Atribut | Definiție | Tip | Voidability
areaCondition | Limita de viteză depinde de condițiile de mediu. | AreaConditionValue | voidable
direction | Indică direcția pentru care este valabilă limita de viteză. | LinkDirectionValue | voidable
laneExtension | Numărul de benzi (inclusiv banda de pornire) pentru care se aplică limita de viteză. | Integer | voidable
speedLimitMinMaxType | Indică dacă limita de viteză este maximă sau minimă și dacă este recomandată. | SpeedLimitMinMaxValue |
speedLimitSource | Sursa limitei de viteză. | SpeedLimitSourceValue | voidable
speedLimitValue | Valoarea limitei de viteză. | Velocity |
startLane | Indicele primei benzi pentru care se aplică limita de viteză. Pentru țările în care se circulă pe partea dreaptă, indicele 1 se referă la banda cea mai din dreapta, iar indicele este majorat la stânga; pentru țările în care se circulă pe partea stângă, indicele 1 se referă la banda cea mai din stânga, iar indicele este majorat la dreapta. | Integer | voidable
validityPeriod | Perioada în care este valabilă limita de viteză. | TM_Period | voidable
vehicleType | Tipul de vehicul pentru care se aplică limita de viteză. | VehicleTypeValue | voidable
weatherCondition | Condițiile meteorologice de care depinde limita de viteză. | WeatherConditionValue | voidable
Constrângeri ale tipului de obiect spațial „SpeedLimit”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport rutier.
7.7.1.16. Zona pentru circulația vehiculelor (VehicleTrafficArea)
Zonă care reprezintă porțiunea unui drum utilizată pentru traficul normal al vehiculelor.
Acest tip este un subtip al „TransportArea”.
7.7.2. Enumerări
7.7.2.1. Clasă funcțională de drum (FunctionalRoadClassValue)
Valorile pentru clasificarea funcțională a drumurilor. Această clasificare are la bază importanța rolului îndeplinit de un drum în cadrul rețelei rutiere.
Valori permise pentru enumerarea „FunctionalRoadClassValue”
Valoare | Definiție
mainRoad | Cele mai importante drumuri în cadrul unei rețele date.
firstClass | Drumuri care ocupă locul al doilea ca importanță în cadrul unei rețele date.
secondClass | Drumuri care ocupă locul al treilea ca importanță în cadrul unei rețele date.
thirdClass | Drumuri care ocupă locul al patrulea ca importanță în cadrul unei rețele date.
fourthClass | Drumuri care ocupă locul al cincilea ca importanță în cadrul unei rețele date.
fifthClass | Drumuri care ocupă locul al șaselea ca importanță în cadrul unei rețele date.
sixthClass | Drumuri care ocupă locul al șaptelea ca importanță în cadrul unei rețele date.
seventhClass | Drumuri care ocupă locul al optulea ca importanță în cadrul unei rețele date.
eighthClass | Drumuri care ocupă locul al nouălea ca importanță în cadrul unei rețele date.
ninthClass | Drumuri cu importanța cea mai mică în cadrul unei rețele date.
7.7.2.2. Numărul minim sau maxim de benzi (MinMaxLaneValue)
Valori care indică dacă numărul de benzi este considerat ca valoare maximă, minimă sau medie.
Valori permise pentru enumerarea „MinMaxLaneValue”
Valoare | Definiție
maximum | Numărul de benzi reprezintă valoarea maximă pentru o porțiune dată a rețelei rutiere.
minimum | Numărul de benzi reprezintă valoarea minimă pentru o porțiune dată a rețelei rutiere.
average | Numărul de benzi reprezintă valoarea medie pentru o porțiune dată a rețelei rutiere.
7.7.2.3. Tipul limitei de viteză (SpeedLimitMinMaxValue)
Posibile valori care indică tipul unei limite de viteză.
Valori permise pentru enumerarea „SpeedLimitMinMaxValue”
Valoare | Definiție
maximum | Limita de viteză reprezintă o valoare maximă
minimum | Limita de viteză reprezintă o valoare minimă
recommendedMaximum | Limita de viteză reprezintă o valoare recomandată maximă
recommendedMinimum | Limita de viteză reprezintă o valoare recomandată minimă
7.7.3. Liste de coduri
7.7.3.1. Condiție aplicabilă zonei (AreaConditionValue)
Restricție a limitei de viteză în funcție de zonă.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.2. Forma nodului rutier (FormOfRoadNodeValue)
Funcțiile nodurilor rutiere.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.3. Forma drumului (FormOfWayValue)
Clasificare bazată pe proprietățile fizice ale legăturii rutiere.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.4. Porțiune de drum (RoadPartValue)
Indică porțiunea de drum căreia i se aplică valoarea unei măsurători.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.5. Tipul de servicii rutiere (RoadServiceTypeValue)
Tipuri de zone de servicii rutiere.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.6. Categoria de suprafață carosabilă (RoadSurfaceCategoryValue)
Valori care indică dacă un drum este pavat sau nu.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.7. Amenajări pentru servicii (ServiceFacilityValue)
Posibile amenajări pentru servicii, disponibile într-o zonă de servicii.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.8. Sursa limitei de viteză (SpeedLimitSourceValue)
Surse posibile pentru limitele de viteză.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.9. Tip de vehicule (VehicleTypeValue)
Tipuri posibile de vehicule.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.7.3.10. Condiții meteorologice (WeatherConditionValue)
Valori indicând condițiile meteorologice care influențează limitele de viteză.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.8. Rețeaua de transport pe apă
7.8.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu rețeaua de transport pe apă:
— Baliză
— Geamandură
— Clasa CEMT
— Starea instalației de transport pe apă
— Zona șenalului navigabil
— Traversarea cu feribotul
— Utilizarea feribotului
— Cale navigabilă interioară
— Cale navigabilă maritimă
— Zonă portuară
— Nod portuar
— Restricție pentru vehiculele de transport pe apă
— Sistem de separare a traficului
— Zonă în cadrul sistemului de separare a traficului
— Intersecție în cadrul sistemului de separare a traficului
— Bandă în cadrul sistemului de separare a traficului
— Sens giratoriu în cadrul sistemului de separare a traficului
— Separator în cadrul sistemului de separare a traficului
— Succesiune de legături de transport pe apă
— Nod al rețelei de transport pe apă
— Direcția fluxului traficului pe apă
— Cale navigabilă
— Legătură de cale navigabilă
— Nod al unei căi navigabile
7.8.1.1. Baliză (Beacon)
Obiect proeminent de construcție specială care formează un reper vizibil fix, cu rol în asistarea navigației sau care este utilizat în releveul hidrografic.
Acest tip este un subtip al „TransportPoint”.
7.8.1.2. Geamandură (Buoy)
Obiect plutitor ancorat pe fundul unei ape într-un loc anumit (însemnat pe harta maritimă), cu rol în asistarea navigației sau utilizat în alte scopuri specifice.
Acest tip este un subtip al „TransportPoint”.
7.8.1.3. Clasa CEMT (CEMTClass)
Clasificare a unei căi navigabile interioare în conformitate cu CEMT (Conferința Europeană a Miniștrilor Transporturilor).
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „CEMTClass ”
Atribut | Definiție | Tip | Voidability
CEMTClass | Valoare care indică clasificarea unei căi navigabile interioare în conformitate cu CEMT (Conferința Europeană a Miniștrilor Transporturilor). | CEMTClassValue |
Constrângeri ale tipului de obiect spațial „CEMTClass”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport pe apă.
7.8.1.4. Starea instalației de transport pe apă (ConditionOfWaterFacility)
Starea unui element al unei rețele de transport pe apă din punctul de vedere al terminării lucrărilor la acesta și al exploatării.
Acest tip este un subtip al „ConditionOfFacility”.
Constrângeri ale tipului de obiect spațial „ConditionOfWaterFacility”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport pe apă.
7.8.1.5. Zona șenalului navigabil (FairwayArea)
Principala porțiune utilizată pentru circulație a unei căi navigabile.
Acest tip este un subtip al „TransportArea”.
7.8.1.6. Traversarea cu feribotul (FerryCrossing)
Cale navigabilă specială menită să sprijine transportul de pasageri, vehicule sau alte încărcături/mărfuri pe țărmul opus al unui corp de apă și care este utilizată în mod normal ca o conexiune care leagă două sau mai multe noduri ale unei rețele de transport terestre.
Acest tip este un subtip al „Waterway”.
7.8.1.7. Utilizarea feribotului (FerryUse)
Tipul de transport efectuat prin traversarea cu feribotul.
Acest tip este un subtip al „TransportProperty”.
Atribute ale tipului de obiect spațial „FerryUse ”
Atribut | Definiție | Tip | Voidability
ferryUse | Valoare care indică tipul de transport efectuat prin traversarea cu feribotul. | FerryUseValue |
Constrângeri ale tipului de obiect spațial „FerryUse”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport pe apă.
7.8.1.8. Cale navigabilă interioară (InlandWaterway)
Cale navigabilă definită în secțiunea privind apele continentale interioare.
Acest tip este un subtip al „Waterway”.
7.8.1.9. Cale navigabilă maritimă (MarineWaterway)
Cale navigabilă definită în secțiunea privind apele maritime.
Acest tip este un subtip al „Waterway”.
Atribute ale tipului de obiect spațial „MarineWaterway”
Atribut | Definiție | Tip | Voidability
deepWaterRoute | Atribut care indică dacă calea navigabilă maritimă este o rută de apă adâncă. | Boolean | voidable
7.8.1.10. Zona portuară (PortArea)
Obiect spațial areal care este utilizat pentru reprezentarea limitelor fizice ale tuturor amenajărilor care alcătuiesc sectorul de pe uscat al unui port maritim sau interior.
Acest tip este un subtip al „TransportArea”.
7.8.1.11. Nod portuar (PortNode)
Obiect spațial punctual care este utilizat pentru a reprezenta într-o manieră simplificată un port maritim sau interior, localizat cu aproximație pe malul corpului de apă unde se află portul.
Acest tip este un subtip al „WaterNode”.
7.8.1.12. Restricție pentru vehiculele de transport pe apă (RestrictionForWaterVehicles)
Restricție privind vehiculele pe un element de transport pe apă.
Acest tip este un subtip al „RestrictionForVehicles”.
Constrângeri ale tipului de obiect spațial „RestrictionForWaterVehicles”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport pe apă.
7.8.1.13. Sistem de separare a traficului (TrafficSeparationScheme)
Sistem destinat să reducă riscul de coliziune în zone congestionate și/sau convergente prin separarea traficului care se desfășoară în sensuri opuse sau aproape opuse.
Acest tip este abstract.
Roluri de asociere ale tipului de obiect spațial „TrafficSeparationScheme”
Rol de asociere | Definiție | Tip | Voidability
component | Componentă a unui sistem de separare a traficului. | TrafficSeparationSchemeArea |
marineWaterRoute | Ansamblu de căi navigabile maritime asociate cu un sistem de separare a traficului. | MarineWaterway |
markerBeacon | Indicator care face parte dintr-un sistem de separare a traficului. | Beacon |
markerBuoy | Indicator care face parte dintr-un sistem de separare a traficului. | Buoy |
7.8.1.14. Zonă în cadrul sistemului de separare a traficului (TrafficSeparationSchemeArea)
Obiect spațial care face parte dintr-un sistem de separare a traficului.
Acest tip este un subtip al „TransportArea”.
Acest tip este abstract.
7.8.1.15. Intersecție în cadrul sistemului de separare a traficului (TrafficSeparationSchemeCrossing)
Zonă definită în care se intersectează benzile de circulație.
Acest tip este un subtip al „TrafficSeparationSchemeArea”.
7.8.1.16. Bandă în cadrul sistemului de separare a traficului (TrafficSeparationSchemeLane)
Zonă cu limite definite pentru care s-a stabilit o desfășurare a traficului într-un singur sens.
Acest tip este un subtip al „TrafficSeparationSchemeArea”.
7.8.1.17. Sens giratoriu în cadrul sistemului de separare a traficului (TrafficSeparationSchemeRoundabout)
Sistem de separare a traficului în cadrul căruia traficul se desfășoară în sens invers acelor de ceasornic în jurul unui punct sau al unei zone specificate.
Acest tip este un subtip al „TrafficSeparationSchemeArea”.
7.8.1.18. Separator în cadrul sistemului de separare a traficului (TrafficSeparationSchemeSeparator)
Zonă care separă benzile pe care navele înaintează în sensuri opuse sau aproape opuse; sau care separă benzile desemnate pentru clase particulare de nave care se deplasează în același sens.
Acest tip este un subtip al „TrafficSeparationSchemeArea”.
7.8.1.19. Succesiune de legături de transport pe apă (WaterLinkSequence)
Obiect spațial liniar, alcătuit dintr-un ansamblu ordonat de legături de căi navigabile și/sau cursuri de apă (după caz), care reprezintă un traseu în rețeaua de transport pe apă, fără ramificații.
Acest tip este un subtip al „TransportLinkSequence”.
7.8.1.20. Nod al rețelei de transport pe apă (WaterNode)
Obiect spațial punctual care este utilizat pentru a reprezenta conectivitatea dintre două legături de transport pe apă diferite, sau dintre o legătură de transport pe apă și o legătură de curs de apă, în cadrul rețelei de transport pe apă.
Acest tip este un subtip al „TransportNode”.
Acest tip este abstract.
7.8.1.21. Direcția fluxului traficului pe apă (WaterTrafficFlowDirection)
Indică direcția fluxului traficului de transport pe apă raportată la direcția vectorului conexiunii de transport pe apă.
Acest tip este un subtip al „TrafficFlowDirection”.
Constrângeri ale tipului de obiect spațial „WaterTrafficFlowDirection”
Această proprietate poate fi asociată numai cu un obiect spațial care face parte dintr-o rețea de transport pe apă.
7.8.1.22. Cale navigabilă (Waterway)
Ansamblu de succesiuni de legături de transport pe apă și/sau legături de căi navigabile și/sau de cursuri de apă individuale (după caz), caracterizate de unul sau mai mulți identificatori tematici și/sau proprietăți, care îndeplinește rolul de rută navigabilă în cadrul unui corp de apă (oceane, mări, râuri, lacuri, canale naturale sau artificiale).
Acest tip este un subtip al „TransportLinkSet”.
Acest tip este abstract.
7.8.1.23. Legătură de cale navigabilă (WaterwayLink)
Obiect spațial liniar care descrie geometria sau conectivitatea rețelei de transport pe apă între două noduri consecutive ale unor căi navigabile sau cursuri de apă. Acesta reprezintă o secțiune liniară printr-un corp de apă utilizat pentru transport.
Acest tip este un subtip al „TransportLink”.
7.8.1.24. Nod al unei căi navigabile (WaterwayNode)
Obiect spațial punctual care este utilizat pentru a reprezenta conectivitatea între două legături de căi navigabile diferite, sau dintre o legătură de cale navigabilă și o legătură de curs de apă, în cadrul rețelei de transport pe apă.
Acest tip este un subtip al „WaterNode”.
Atribute ale tipului de obiect spațial „WaterwayNode”
Atribut | Definiție | Tip | Voidability
formOfWaterwayNode | Descrierea funcției unui nod al căii navigabile în cadrul rețelei de transport pe apă. | FormOfWaterwayNodeValue | voidable
7.8.2. Enumerări
7.8.2.1. Clasa CEMT (CEMTClassValue)
Clasificare a căilor navigabile interioare în conformitate cu Rezoluția nr. 92/2 a CEMT (Conferința Europeană a Miniștrilor Transporturilor).
Valori permise pentru enumerarea „CEMTClassValue”
Valoare | Definiție
I | Cale navigabilă interioară aparținând clasei CEMT I, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
II | Cale navigabilă interioară aparținând clasei CEMT II, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
III | Cale navigabilă interioară aparținând clasei CEMT III, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
IV | Cale navigabilă interioară aparținând clasei CEMT IV, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
Va | Cale navigabilă interioară aparținând clasei CEMT Va, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
Vb | Cale navigabilă interioară aparținând clasei CEMT Vb, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
VIa | Cale navigabilă interioară aparținând clasei CEMT VIa, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
VIb | Cale navigabilă interioară aparținând clasei CEMT VIb, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
VIc | Cale navigabilă interioară aparținând clasei CEMT VIc, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
VII | Cale navigabilă interioară aparținând clasei CEMT VII, definită de Conferința Europeană a Miniștrilor Transporturilor, Rezoluția nr. 92/2 - Tabelul 1.
7.8.3. Liste de coduri
7.8.3.1. Utilizarea feribotului (FerryUseValue)
Tipuri de transport efectuate de un feribot.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.8.3.2. Tipul nodului de cale navigabilă (FormOfWaterwayNodeValue)
Funcția unui nod de cale navigabilă în cadrul rețelei de transport pe apă.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
7.9. Cerințe specifice categoriei
7.9.1. Coerența între seturile de date spațiale
| 1. | Reprezentările liniei mediane și a nodurilor rețelelor de transport sunt situate întotdeauna în perimetrul reprezentării aceluiași obiect.
| 2. | Conectivitatea între rețelele de transport dincolo de frontierele de stat și – acolo unde este cazul – dincolo de frontierele regionale (și seturile de date) din statele membre trebuie stabilită și întreținută de autoritățile respective, utilizând mecanismele de conectivitate transfrontalieră pevăzute de tipul „NetworkConnection”.
7.9.2. Modelarea referințelor obiectelor
| 1. | Atunci când se utilizează referențierea liniară pentru datele privind rețelele de transport, poziția proprietăților la care se face referire, raportată la legături sau la succesiunea de legături, este exprimată sub formă de distanțe măsurate de-a lungul geometriei date pentru obiectul (obiectele) de legătură fundamental(e).
| 2. | O conexiune intermodală face întotdeauna trimitere la două elemente care aparțin unor rețele diferite.
7.9.3. Reprezentarea geometrică
| 1. | Extremitățile legăturilor de transport trebuie conectate peste tot unde există o intersecție între fenomenele lumii reale pe care le reprezintă. La intersecția elementelor de rețea nu trebuie realizate conexiuni, atunci când nu este posibilă trecerea de la un element la altul.
| 2. | În cadrul unui set de date privind rețelele de transport care conține noduri, nodurile respective sunt prezente doar acolo unde legăturile de transport pe apă se conectează sau se termină.
7.9.4. Modelarea referințelor obiectelor
Rețelele de transport pe apă folosesc din nou, acolo unde există și unde este posibil, geometria liniei mediane a rețelei de transport pe apă din categoria „Hidrografie”. Prin urmare, referențierea obiectului este utilizată pentru a lega cursul de apă destinat transportului de geometria existentă a rețelei de transport pe apă din categoria „Hidrografie”.
7.9.5. Linii mediane
Liniile mediane ale obiectelor „Drum” și „Cale ferată” intră în sfera obiectului fizic real pe care acestea îl reprezintă, dacă legătura este prezentată ca nefiind „fictitious”.
7.9.6. Asigurarea conectivității rețelei
| 1. | Acolo unde există o conexiune într-o rețea de transport, toate extremitățile conectate ale legăturii și nodul opțional care fac parte din conexiunea respectivă trebuie poziționate la o distanță față de fiecare dintre acestea mai mică decât toleranța la conectivitate.
| 2. | Extremitățile și nodurile legăturii care nu sunt conectate trebuie să fie separate de o distanță superioară toleranței la conectivitate.
| 3. | În cazul seturilor de date pentru care sunt prezente atât legăturile de căi de transport cât și nodurile, poziția relativă a nodurilor și extremităților legăturii, în funcție de toleranța la conectivitate specificată, corespunde asocierilor care există între acestea în cadrul setului de date.
7.10. Straturi
Straturi pentru categoria de date spațiale „Transport networks”
Numele stratului | Titlul stratului | Tip (tipuri) de obiect spațial
TN.CommonTransportElements.TransportNode | Nod de transport generic | TransportNode
TN.CommonTransportElements.TransportLink | Legătură de transport generic | TransportLink
TN.CommonTransportElements.TransportArea | Zonă de transport generic | TransportArea
TN.RoadTransportNetwork.RoadLink | Legătură rutieră | RoadLink
TN.RoadTransportNetwork.VehicleTrafficArea | Zonă de circulație a vehiculelor | VehicleTrafficArea
TN.RoadTransportNetwork.RoadServiceArea | Zonă de servicii rutiere | RoadServiceArea
TN.RoadTransportNetwork.RoadArea | Zonă rutieră | RoadArea
TN.RailTransportNetwork.RailwayLink | Legătură feroviară | RailwayLink
TN.RailTransportNetwork.RailwayStationArea | Zona gării | RailwayStationArea
TN.RailTransportNetwork.RailwayYardArea | Zona gării de triaj | RailwayYardArea
TN.RailTransportNetwork.RailwayArea | Zona căii ferate | RailwayArea
TN.WaterTransportNetwork.WaterwayLink | Legătură de cale navigabilă | WaterwayLink
TN.WaterTransportNetwork.FairwayArea | Zona șenalului navigabil | FairwayArea
TN.WaterTransportNetwork.PortArea | Zona portuară | PortArea
TN.AirTransportNetwork.AirLink | Legătură aeriană | AirLink
TN.AirTransportNetwork.AerodromeArea | Zona aerodromului | AerodromeArea
TN.AirTransportNetwork.RunwayArea | Zona pistei de decolare și de aterizare | RunwayArea
TN.AirTransportNetwork.AirspaceArea | Zona spațiului aerian | AirspaceArea
TN.AirTransportNetwork.ApronArea | Zona platformei | ApronArea
TN.AirTransportNetwork.TaxiwayArea | Zona pistei de rulare | TaxiwayArea
TN.CableTransportNetwork.CablewayLink | Cale de transport pe cablu | CablewayLink
8. HIDROGRAFIE
8.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
— „acvifer” înseamnă unul sau mai multe straturi subterane de rocă sau alte tipuri de straturi geologice cu o porozitate și o permeabilitate suficiente pentru a permite fie trecerea unui curent semnificativ de apă subterană, fie captarea de cantități importante de apă subterană,
— „ape subterane” înseamnă toate apele care se găsesc sub suprafața solului în zona de saturație și care vin în contact direct cu solul sau cu subsolul,
— „sub-bazin” înseamnă orice zonă în care toate scurgerile de apă converg, printr-o rețea de râuri, fluvii și, eventual, lacuri, către un anumit punct al unui curs de apă.
8.2. Structura categoriei de date spațiale „Hidrografie”
Tipurile specificate pentru categoria de date spațiale „Hidrografie” sunt organizate în următoarele categorii:
— Bază hidrografică
— Rețea hidrografică
— Ape cu acțiune hidrofizică
— Notificare hidrografică
8.3. Bază hidrografică
8.3.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu bază hidrografică:
— Obiect hidrografic
8.3.1.1. Obiect hidrografic (HydroObject)
Bază de identificare pentru obiecte hidrografice reale (inclusiv cele artificiale).
Acest tip este abstract.
Atribute ale tipului de obiect spațial „HydroObject”
Atribut | Definiție | Tip | Voidability
geographicalName | Denumire spațială utilizată pentru identificarea obiectului hidrografic din lumea reală. Aceasta furnizează „cheia” pentru a asocia în mod implicit diferite reprezentări ale obiectului. | GeographicalName | voidable
hydroId | Identificator utilizat pentru identificarea obiectului hidrografic din lumea reală. Acesta furnizează „cheia” pentru a asocia în mod implicit diferite reprezentări ale obiectului. | HydroIdentifier |
Roluri de asociere ale tipului de obiect spațial „HydroObject”
Rol de asociere | Definiție | Tip | Voidability
relatedHydroObject | Obiect hidrografic înrudit reprezentând aceeași entitate din lumea reală. | HydroObject | voidable
8.3.2. Tipuri de date
8.3.2.1. Identificator hidrografic (HydroIdentifier)
Identificator hidrografic tematic.
Atribute ale tipului de date „HydroIdentifier”
Atribut | Definiție | Tip | Voidability
classificationScheme | Descriere a sistemului de identificare utilizat (național, european, etc.). | CharacterString |
localId | Identificator local, atribuit de o autoritate oarecare. | CharacterString |
namespace | Indicator al sferei de aplicare a identificatorului local. | CharacterString |
8.4. Rețea hidrografică
8.4.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu rețeaua hidrografică:
— Nod hidrografic
— Legătură de curs de apă
— Succesiune de legături de cursuri de apă
— Intersectare de cursuri de apă cu fluxuri separate
8.4.1.1. Nod hidrografic (HydroNode)
Nod în cadrul rețelei hidrografice.
Acest tip este un subtip al „Node”.
Acest tip este un subtip al „HydroObject”.
Atribute ale tipului de obiect spațial „HydroNode”
Atribut | Definiție | Tip | Voidability
hydroNodeCategory | Natura nodului hidrografic. | HydroNodeCategoryValue | voidable
8.4.1.2. Legătură de curs de apă (WatercourseLink)
Segment al unui curs de apă în cadrul unei rețele hidrografice.
Acest tip este un subtip al „Link”.
Acest tip este un subtip al „HydroObject”.
Atribute ale tipului de obiect spațial „WatercourseLink”
Atribut | Definiție | Tip | Voidability
flowDirection | Direcția curgerii apei în cadrul tronsonului, ținând cont de digitalizarea geometriei tronsonului respectiv. | LinkDirectionValue | voidable
length | Lungimea tronsonului de rețea. | Length | voidable
8.4.1.3. Succesiune de legături de cursuri de apă (WatercourseLinkSequence)
Succesiune de legături de cursuri de apă reprezentând un traiect fără ramificații în cadrul unei rețele hidrografice.
Acest tip este un subtip al „LinkSequence”.
Acest tip este un subtip al „HydroObject”.
8.4.1.4. Intersectare de cursuri de apă cu fluxuri separate (WatercourseSeparatedCrossing)
Element al rețelei hidrografice utilizat pentru a indica intersectarea fără interacțiune de cursuri de apă cu fluxuri separate.
Acest tip este un subtip al „GradeSeparatedCrossing”.
Acest tip este un subtip al „HydroObject”.
8.4.2. Liste de coduri
8.4.2.1. Categoria de nod hidrografic (HydroNodeCategoryValue)
Definește categoriile pentru diferite tipuri de noduri din cadrul rețelei hidrografice.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
8.5. Ape cu acțiune hidrofizică
8.5.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu categoria „ape cu acțiune hidrofizică”:
— Intersecție
— Dig sau baraj
— Bazin de drenaj
— Rambleu
— Căderi
— Punct fluvial
— Vad
— Punct de interes hidrografic
— Centrală hidroelectrică
— Teren inundat
— Limita uscat-apă
— Ecluză
— Obiect artificial
— Regiune oceanică
— Conductă
— Stație de pompare
— Praguri
— Bazin hidrografic
— Țărm
— Construcții pe țărm
— Deversor
— Apă stătătoare
— Apă de suprafață
— Curs de apă
— Zonă umedă
8.5.1.1. Intersecție (Crossing)
Obiect artificial care permite trecerea apei pe deasupra sau pe dedesubtul unui obstacol.
Acest tip este un subtip al „ManMadeObject”.
Atribute ale tipului de obiect spațial „Crossing”
Atribut | Definiție | Tip | Voidability
type | Tip de intersectare fizică. | CrossingTypeValue | voidable
8.5.1.2. Dig sau baraj (DamOrWeir)
Barieră transversală permanentă situată pe un curs de apă, utilizată pentru reținerea apei sau pentru controlul debitului acesteia.
Acest tip este un subtip al „ManMadeObject”.
8.5.1.3. Bazin de drenaj (DrainageBasin)
Zonă care dispune de o evacuare obișnuită pentru scurgerile de suprafață.
Acest tip este un subtip al „HydroObject”.
Atribute ale tipului de obiect spațial „DrainageBasin ”
Atribut | Definiție | Tip | Voidability
area | Dimensiunea bazinului de drenaj. | Area | voidable
basinOrder | Număr (sau cod) care exprimă gradul de ramificație/derivație într-un sistem de bazine de drenaj. | HydroOrderCode | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Geometria bazinului de drenaj, ca suprafață. | GM_Surface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
origin | Originea bazinului de drenaj. | OriginValue | voidable
Roluri de asociere ale tipului de obiect spațial „DrainageBasin ”
Rol de asociere | Definiție | Tip | Voidability
outlet | Evacuarea (evacuările) apelor de suprafață ale unui bazin de drenaj. | SurfaceWater | voidable
containsBasin | Sub-bazin mai mic inclus într-un bazin mai mare. | DrainageBasin | voidable
Constrângeri ale tipului de obiect spațial „DrainageBasin”
Un bazin fluvial nu poate fi inclus în niciun alt bazin.
8.5.1.4. Rambleu (Embankment)
Colină alungită din pământ sau din alt material, înălțată de om.
Acest tip este un subtip al „ManMadeObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de risc natural” din anexa III la Directiva 2007/2/CE.
8.5.1.5. Căderi (Falls)
Porțiune verticală descendentă a unui curs de apă, la nivelul căreia apa cade de la o anumită înălțime.
Acest tip este un subtip al „FluvialPoint”.
Atribute ale tipului de obiect spațial „Falls”
Atribut | Definiție | Tip | Voidability
height | Distanță măsurată de la punctul cel mai de jos al bazei la nivelul solului sau al apei (porțiune de coborâre/porțiune în aval) până la cel mai înalt punct al obiectului spațial. | Length | voidable
8.5.1.6. Punct fluvial (FluvialPoint)
Punct de interes hidrografic care influențează debitul unui curs de apă.
Acest tip este un subtip al „HydroPointOfInterest”.
Acest tip este abstract.
8.5.1.7. Vad (Ford)
Porțiune puțin adâncă a unui curs de apă, utilizată ca drum de traversare.
Acest tip este un subtip al „ManMadeObject”.
8.5.1.8. Punct de interes hidrografic (HydroPointOfInterest)
Loc natural în care apa apare, dispare sau își modifică debitul.
Acest tip este un subtip al „HydroObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „HydroPointOfInterest”
Rol de asociere | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Geometria punctului de interes hidrografic, reprezentată ca punct, curbă sau suprafață. | GM_Primitive | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
levelOfDetail | Rezoluție, exprimată ca invers al unei scări indicatoare sau ca distanță la nivelul solului. | MD_Resolution |
8.5.1.9. Centrală hidroelectrică (HydroPowerPlant)
Instalație pentru producerea energiei electrice cu ajutorul apei în mișcare.
Acest tip este un subtip al „ManMadeObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Resurse energetice” din anexa III la Directiva 2007/2/CE.
8.5.1.10. Teren inundat (InundatedLand)
Suprafață acoperită periodic de apa provenită din inundații, cu excepția apelor de maree.
Acest tip este un subtip al „HydroObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de risc natural” din anexa III la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „InundatedLand”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Geometria terenului inundat, sub forma unei suprafețe. | GM_Surface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
inundationReturnPeriod | Perioada medie (în ani) care se scurge în mod normal între două fenomene de inundație. | Number | voidable
inundationType | Tipul unui teren susceptibil de a fi inundat, în funcție de cauza inundării sale. | InundationValue | voidable
8.5.1.11. Limita uscat-apă (LandWaterBoundary)
Linia unde o suprafață de pământ vine în contact cu un corp de apă.
Atribute ale tipului de obiect spațial „LandWaterBoundary”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Geometria limitei uscat-apă, sub forma unei curbe. | GM_Curve |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
origin | Sursa limitei uscat-apă. | OriginValue | voidable
waterLevelCategory | Nivelul apei care definește limita uscat-apă. | WaterLevelValue | voidable
8.5.1.12. Ecluză (Lock)
Spațiu închis cu o pereche de porți sau cu o serie de porți, utilizat pentru ridicarea sau coborârea navelor în timpul trecerii de la un nivel la altul al apei.
Acest tip este un subtip al „ManMadeObject”.
8.5.1.13. Obiect făcut de om (ManMadeObject)
Obiect artificial amplasat într-un corp de apă și care deține una din următoarele tipuri de funcții: - reține apa; - reglează cantitatea de apă; - modifică cursul apei; - permite cursurilor de apă să se intersecteze.
Acest tip este un subtip al „HydroObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „ManMadeObject”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
condition | Starea activităților de planificare, construire, reparare și/sau întreținere a structurilor și/sau a echipamentelor, cuprinzând o instalație și/sau situate într-un anumit loc, considerată în ansamblu. | ConditionOfFacilityValue | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Geometria obiectului artificial, reprezentată ca punct, curbă sau suprafață. | GM_Primitive | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
levelOfDetail | Rezoluție, exprimată ca invers al unei scări indicatoare sau ca distanță la nivelul solului. | MD_Resolution |
8.5.1.14. Regiune oceanică (OceanRegion)
Una din cele trei mari regiuni ale Oceanului Planetar, fiecare având subzone și zone periferice asociate și fiind supusă unui regim de curgere independent.
Acest tip este un subtip al „HydroObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Regiuni marine” din anexa III la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „OceanRegion”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Geometria regiunii oceanice, reprezentată ca suprafață. | GM_Surface | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
Roluri de asociere ale tipului de obiect spațial „OceanRegion”
Rol de asociere | Definiție | Tip | Voidability
foreshore | Porțiune a litoralului sau a plajei care se află între nivelul mediu al apei la reflux și limita superioară a zonei de acțiune normală a valurilor. | Shore | voidable
8.5.1.15. Conductă (Pipe)
Țeavă destinată transportului de solide, lichide sau gaze.
Acest tip este un subtip al „ManMadeObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Servicii de utilitate publică și servicii publice” din anexa III la Directiva 2007/2/CE.
8.5.1.16. Stație de pompare (PumpingStation)
Instalație pentru deplasarea solidelor, lichidelor sau a gazelor cu ajutorul presiunii sau al aspirației.
Acest tip este un subtip al „ManMadeObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Servicii de utilitate publică și servicii publice” din anexa III la Directiva 2007/2/CE.
8.5.1.17. Praguri (Rapids)
Porțiuni ale unui râu cu un curent accelerat în care râul respectiv coboară panta albiei cu rapiditate și fără oprire, suficient pentru a forma o cascadă.
Acest tip este un subtip al „FluvialPoint”.
8.5.1.18. Bazin hidrografic (RiverBasin)
Zonă în care toate scurgerile de apă converg, printr-o rețea de râuri, fluvii și, eventual, lacuri, către mare, în care se varsă printr-o singură gură de vărsare, un singur estuar sau o singură deltă.
Acest tip este un subtip al „DrainageBasin”.
8.5.1.19. Țărm (Shore)
Fâșie îngustă de pământ în contact imediat cu un corp de apă, incluzând zona dintre nivelul fluxului și cel al refluxului.
Acest tip este un subtip al „HydroObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Acoperire terestră” din anexa II la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „Shore”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
composition | Tipul (tipurile) principale de materiale care alcătuiesc un obiect spațial, cu excepția suprafeței acestuia. | ShoreTypeValue | voidable
delineationKnown | Indicație conform căreia delimitarea (de exemplu, limite și informații) unui obiect spațial este cunoscută. | Boolean | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Geometria țărmului, reprezentată ca suprafață. | GM_Surface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
8.5.1.20. Construcții pe țărm (ShorelineConstruction)
Structură artificială care este legată de uscatul care mărginește un corp de apă și fixată în poziție.
Acest tip este un subtip al „ManMadeObject”.
8.5.1.21. Deversor (Sluice)
Canal deschis, înclinat, echipat cu o poartă pentru regularizarea debitului apei.
Acest tip este un subtip al „ManMadeObject”.
8.5.1.22. Apă stătătoare (StandingWater)
Corp de apă înconjurat în întregime de uscat.
Acest tip este un subtip al „SurfaceWater”.
Atribute ale tipului de obiect spațial „StandingWater ”
Atribut | Definiție | Tip | Voidability
elevation | Altitudine de deasupra nivelului mediu al mării. | Length | voidable
meanDepth | Adâncime medie a corpului de apă. | Length | voidable
surfaceArea | Suprafața corpului de apă. | Area | voidable
Constrângeri ale tipului de obiect spațial „StandingWater”
Geometria apei stătătoare poate fi o suprafață sau un punct.
8.5.1.23. Apă de suprafață (SurfaceWater)
Orice masă de cale navigabilă interioară cunoscută.
Acest tip este un subtip al „HydroObject”.
Acest tip este abstract.
Atribute ale tipului de obiect spațial „SurfaceWater”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Geometria apei de suprafață: - curbă sau suprafață pentru un curs de apă; - punct sau suprafață pentru o apă stătătoare. | GM_Primitive |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
levelOfDetail | Rezoluție, exprimată ca invers al unei scări indicatoare sau ca distanță la nivelul solului. | MD_Resolution |
localType | Indică denumirea „locală” pentru tipul de apă de suprafață. | LocalisedCharacterString | voidable
origin | Originea apei de suprafață. | OriginValue | voidable
persistence | Gradul de persistență a apei. | HydrologicalPersistenceValue | voidable
tidal | Identifică dacă apa de suprafață este afectată de apa de maree. | Boolean | voidable
Roluri de asociere ale tipului de obiect spațial „SurfaceWater”
Rol de asociere | Definiție | Tip | Voidability
bank | Mal(uri) asociat(e) apelor de suprafață. | Shore | voidable
drainsBasin | Bazin(e) drenat(e) de ape de suprafață. | DrainageBasin | voidable
neighbour | Asociere cu o altă instanță a acelorași ape de suprafață din lumea reală dintr-un set de date diferit. | SurfaceWater | voidable
8.5.1.24. Curs de apă (Watercourse)
Curs de apă curgătoare natural sau artificial.
Acest tip este un subtip al „SurfaceWater”.
Atribute ale tipului de obiect spațial „Watercourse ”
Atribut | Definiție | Tip | Voidability
condition | Situația activităților de planificare, construire, reparare și/sau întreținere a cursului de apă. | ConditionOfFacilityValue | voidable
delineationKnown | Indicație conform căreia delimitarea (de exemplu, limite și informații) unui obiect spațial este cunoscută. | Boolean | voidable
length | Lungimea cursului de apă. | Length | voidable
level | Localizare verticală a cursului de apă față de nivelul solului. | VerticalPositionValue | voidable
streamOrder | Număr (sau cod) care exprimă gradul de ramificație într-un sistem de cursuri de apă. | HydroOrderCode | voidable
width | Lățimea cursului de apă (reprezentată ca interval) de-a lungul lungimii acestuia. | WidthRange | voidable
Constrângeri ale tipului de obiect spațial „Watercourse”
Geometria cursului de apă poate fi reprezentată ca o curbă sau ca o suprafață.
Un atribut de stare poate fi specificat numai pentru un curs de apă artificial.
8.5.1.25. Zonă umedă (Wetland)
Zonă slab drenată sau inundată periodic, în care solul este saturat cu apă iar dezvoltarea vegetației este favorizată.
Acest tip este un subtip al „HydroObject”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Acoperire terestră” din anexa II la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „Wetland”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
geometry | Geometria zonei umede, reprezentată ca suprafață. | GM_Surface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
localType | Furnizează o denumire „locală” pentru tipul de zonă umedă. | LocalisedCharacterString | voidable
tidal | Identifică dacă zona umedă este afectată de apa de maree. | Boolean | voidable
8.5.2. Tipuri de date
8.5.2.1. Cod de ordine hidrografică (HydroOrderCode)
„Cod de ordine” semnificativ din punct de vedere hidrografic utilizat pentru ordonarea ierarhizată a cursurilor de apă și a bazinelor de drenaj.
Atribute ale tipului de date „HydroOrderCode”
Atribut | Definiție | Tip | Voidability
order | Număr (sau cod) care exprimă gradul de ramificație sau diviziune dintr-un sistem de cursuri de apă sau de bazine de drenaj. | CharacterString |
orderScheme | Descrierea conceptului de ordonare. | CharacterString |
scope | Indicator al sferei de aplicare sau al originii unui cod de ordine (inclusiv dacă este vorba de un cod de ordine național, supranațional sau european). | CharacterString |
8.5.2.2. Domeniul de variație a lățimii (WidthRange)
Domeniul de variație a lățimii orizontale a cursului de apă de-a lungul lungimii acestuia.
Atribute ale tipului de date „WidthRange”
Atribut | Definiție | Tip | Voidability
lower | Limita inferioară a lățimii. | Length |
upper | Limita superioară a lățimii. | Length |
8.5.3. Enumerări
8.5.3.1. Origine (OriginValue)
Tip de enumerare care specifică un set de categorii de „origine” hidrografică (naturală, artificială) pentru diferite obiecte hidrografice.
Valori permise pentru enumerarea „OriginValue”
Value | Definition
natural | Indicație că un obiect spațial este natural.
manMade | Indicație că un obiect spațial este artificial.
8.5.4. Liste de coduri
8.5.4.1. Tipul de intersectare (CrossingTypeValue)
Tipuri de intersectare fizică a cursurilor de apă artificiale.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
8.5.4.2. Persistență hidrologică (HydrologicalPersistenceValue)
Categorii ale persistenței hidrologice a unui corp de apă.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
8.5.4.3. Inundație (InundationValue)
Tip de teren susceptibil de a fi inundat.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de risc natural” din anexa III la Directiva 2007/2/CE.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
8.5.4.4. Tip de țărm (ShoreTypeValue)
Categorii ale compoziției țărmului.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Acoperire terestră” din anexa II la Directiva 2007/2/CE.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
8.5.4.5. Nivelul apei (WaterLevelValue)
Informații privind mareea/nivelul apei la care se raportează adâncimile și înălțimile.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
8.6. Notificare hidrografică
8.6.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale corelate cu categoria „Notificare hidrografică”:
— Ape costiere DCA (Water Framework Directive – Directiva-cadru privind apa)
— Corp de apă subterană DCA
— Lac DCA
— Râu DCA
— Râu sau lac DCA
— Corp de apă de suprafață DCA
— Apă de tranziție DCA
— Corp de apă DCA
8.6.1.1. Ape costiere DCA (WFDCoastalWater)
Ape de suprafață situate în partea interioară a unei linii care are fiecare punct situat la o distanță de o milă marină față de punctul cel mai apropiat de linia de bază de la care se măsoară întinderea apelor teritoriale și care, acolo unde este cazul, se extinde până la limita exterioară a unei ape de tranziție.
Acest tip este un subtip al „WFDSurfaceWaterBody”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Constrângeri ale tipului de obiect spațial „WFDCoastalWater”
Geometria apelor costiere trebuie să fie o suprafață.
8.6.1.2. Corp de apă subterană DCA (WFDGroundWaterBody)
Volum distinct de apă subterană din interiorul unuia sau mai multor acvifere.
Acest tip este un subtip al „WFDWaterBody”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „WFDGroundWaterBody”
Atribut | Definiție | Tip | Voidability
geometry | Geometria corpului de apă subterană DCA. | GM_Primitive | voidable
8.6.1.3. Lac DCA (WFDLake)
Corp de apă stătătoare interioară de suprafață.
Acest tip este un subtip al „WFDRiverOrLake”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Constrângeri ale tipului de obiect spațial „WFDLake”
Geometria unui lac trebuie să fie o suprafață.
8.6.1.4. Râu DCA (WFDRiver)
Corp de apă interioară care curge în mare parte pe suprafața solului, dar care poate curge și în subsol pe o porțiune a cursului său.
Acest tip este un subtip al „WFDRiverOrLake”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Constrângeri ale tipului de obiect spațial „WFDRiver”
Geometria unui râu trebuie să fie o curbă.
Este posibil ca atributele „main” (principal) și „large” (mare) să nu fie specificate pentru canalele artificiale.
8.6.1.5. Râu sau lac DCA (WFDRiverOrLake)
Clasă abstractă conținând atributele comune pentru un râu sau lac DCA.
Acest tip este un subtip al „WFDSurfaceWaterBody”.
Acest tip este abstract.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „WFDRiverOrLake”
Atribut | Definiție | Tip | Voidability
large | Râuri cu o zonă de captare > 50 000 km2; sau râuri și afluenții principali care au o zonă de captare cuprinsă între 5 000 km2 și 50 000 km2. Lacuri care au o suprafață > 500 km2. | Boolean | voidable
main | Râuri care au o zonă de captare > 500 km2. Lacuri care au o suprafață > 10 km2. | Boolean | voidable
8.6.1.6. Corp de apă de suprafață DCA (WFDSurfaceWaterBody)
Parte distinctă și semnificativă a unei ape de suprafață.
Acest tip este un subtip al „WFDWaterBody”.
Acest tip este abstract.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „WFDSurfaceWaterBody ”
Atribut | Definiție | Tip | Voidability
artificial | „Corp de apă artificial” înseamnă un corp de apă de suprafață creat de o activitate umană. | Boolean |
geometry | Geometria corpului de apă de suprafață DCA: - suprafață pentru apele costiere DCA; - suprafață pentru o apă de tranziție DCA; - curbă pentru un râu DCA; - suprafață pentru un lac DCA. | GM_Primitive |
heavilyModified | „Corp de apă puternic modificat” înseamnă un corp de apă de suprafață al cărui caracter este fundamental modificat ca urmare a modificărilor fizice cauzate de activitatea umană, după cum a fost stabilit de statele membre în conformitate cu dispozițiile anexei II la DCA. | Boolean |
representativePoint | Punct reprezentativ al corpului de apă DCA. | GM_Point | voidable
Constrângeri ale tipului de obiect spațial „WFDSurfaceWaterBody”
Atributul „heavilyModified” permis numai dacă obiectul spațial nu este artificial.
8.6.1.7. Apă de tranziție DCA (WFDTransitionalWater)
Corpuri de apă de suprafață aflate în vecinătatea gurilor de râu, care au un caracter parțial salin ca urmare a învecinării cu apele costiere, dar care sunt puternic influențate de fluxurile de apă dulce.
Acest tip este un subtip al „WFDSurfaceWaterBody”.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Constrângeri ale tipului de obiect spațial „WFDTransitionalWater”
Geometria apei tranziționale trebuie să fie o suprafață.
8.6.1.8. Corp de apă conform DCA (WFDWaterBody)
Clasă abstractă reprezentată de un corp de apă de suprafață sau un corp de apă subterană DCA.
Acest tip este un subtip al „HydroObject”.
Acest tip este abstract.
Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale „Zone de administrare/restricție/reglementare și unități de raportare” din anexa III la Directiva 2007/2/CE.
Atribute ale tipului de obiect spațial „WFDWaterBody”
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
8.7. Cerințe specifice categoriei
8.7.1. Coerența între seturile de date spațiale
| 1. | Legăturile, liniile mediane și nodurile hidrografice trebuie situate întotdeauna în perimetrul reprezentării zonei aceluiași obiect.
| 2. | Conectivitatea între rețelele de transport dincolo de frontierele de stat și – acolo unde este cazul – dincolo de frontierele regionale (și seturile de date) din statele membre trebuie asigurată și întreținută de autoritățile respective, utilizând mecanismele de conectivitate transfrontalieră furnizate de tipul „NetworkConnection”.
| 3. | Toate atributele obiectelor din cadrul acestui sistem trebuie să fie identice cu proprietatea echivalentă a obiectului respectiv, utilizată pentru obligațiile de raportare stabilite în temeiul Directivei 2000/60/CE.
8.7.2. Administrarea identificatorilor
| 1. | Dacă denumirea geografică este utilizată drept ID hidrologic unic pentru un obiect în această specificație, atunci aceasta trebuie să derive, atunci când este posibil, dintr-un registru toponimic paneuropean sau dintr-o altă sursă competentă paneuropeană.
| 2. | Atributul „localId” al identificatorului de obiect extern al unui obiect spațial este același cu ID-ul utilizat pentru obligațiile de raportare stabilite în temeiul Directivei 2000/60/CE.
8.7.3. Modelarea referințelor obiectelor
| 1. | Dacă același obiect din lumea reală reprezentat într-un set de date este pus la dispoziție cu ajutorul unor obiecte spațiale aparținând mai multor sisteme de aplicare „Hidrografie”, atunci aceste obiecte spațiale vor purta aceeași denumire geografică unică sau același identificator tematic hidrografic.
| 2. | Atunci când se utilizează referențierea liniară pentru datele privind rețeaua hidrografică, poziția proprietăților la care se face referire, raportată la legături sau la succesiunea de legături, este exprimată ca distanțe măsurate de-a lungul geometriei indicate pentru obiectul sau obiectele de legătură aferente.
8.7.4. Reprezentare geometrică
| 1. | În cazul furnizării de obiecte spațiale cu diferite rezoluții spațiale, rezoluția spațială respectivă trebuie specificată pentru fiecare obiect spațial în parte, utilizând, acolo unde este cazul, atributul „levelOfDetail”.
| 2. | Legăturile de cursuri de apă se intersectează acolo unde există o conexiune între fenomenele din lumea reală pe care le reprezintă. La intersectarea elementelor de rețea nu trebuie să se realizeze intersecții, atunci când nu este posibilă trecerea apei de la un element în altul.
| 3. | În cadrul unui set de date referitoare la o rețea hidrografică care conține noduri, nodurile respective nu trebuie să fie prezente decât la nivelul conexiunilor sau al extremităților legăturilor de cursuri de apă.
| 4. | Geometria trebuie să fie aceeași cu cea utilizată pentru obligațiile de notificare stabilite în temeiul Directivei 2000/60/CE.
8.7.5. Utilizarea atributului „DelineationKnown”
| 1. | Atributul „delineationKnown” nu trebuie utilizat pentru a indica dacă acuratețea/precizia unei geometrii date este scăzută; această indicație trebuie furnizată prin utilizarea elementului (elementelor) adecvat(e) privind calitatea datelor.
| 2. | Atributul „delineationKnown” nu este utilizat pentru a indica o modificare în timp a geometriei atunci când modificarea respectivă este cunoscută.
8.7.6. Linii mediane
Liniile mediane ale obiectelor corespunzătoare cursurilor de apă trebuie să intre în sfera obiectului fizic din lumea reală pe care îl reprezintă, dacă legătura de curs de apă este prezentată ca nefiind „fictitious”.
8.7.7. Asigurarea conectivității rețelei
| 1. | Acolo unde există o conexiune într-o rețea hidrografică, toate limitele conectate ale legăturii și nodul opțional care face parte din conexiunea respectivă trebuie poziționate la o distanță mai mică decât toleranța la conectivitate față de fiecare dintre acestea.
| 2. | Distanța dintre extremitățile legăturii și nodurile care nu sunt conectate trebuie să fie mai mare decât toleranța la conectivitate.
| 3. | În cazul seturilor de date care includ atât legăturile cât și nodurile de rețea de transport, poziția relativă a nodurilor și extremităților legăturilor față de toleranța la conectivitate specificată trebuie să corespundă asocierilor existente între acestea în cadrul setului de date.
8.8. Straturi
Straturi pentru categoria de date spațiale „Hidrografie”
Numele stratului | Titlul stratului | Tip (tipuri) de obiect spațial
HY.PhysicalWaters.Waterbodies | Corp de apă | Watercourse, StandingWater
HY.PhysicalWaters.LandWaterBoundary | Limita uscat-apă | LandWaterBoundary
HY.PhysicalWaters.Catchments | Captare | DrainageBasin, RiverBasin
HY.Network | Rețea hidrografică | HydroNode, WatercourseLink
HY.PhysicalWaters.HydroPointOfInterest | Punct de interes hidrografic | Rapids, Falls
HY.PhysicalWaters.ManMadeObject | Obiect artificial | Crossing, DamOrWeir, Sluice, Lock, Ford, ShorelineConstruction
HY.HydroObject | Țărm, Zonă umedă | Shore, Wetland
HY.Reporting.WFDRiver | Râu DCA | WFDRiver
HY.Reporting. WFDLake | Lac DCA | WFDLake
HY.Reporting. WFDTransitionalWater | Apă de tranziție DCA | WFDTransitionalWater
HY.Reporting. WFDCoastalWater | Apă costieră DCA | WFDCoastalWater
HY.OceanRegion | Regiune oceanică | OceanRegion
9. ZONE PROTEJATE
9.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt utilizate pentru modificarea și clasificarea obiectelor spațiale din seturile de date corelate cu categoria de date spațiale „Zone protejate”:
— Zonă protejată
9.1.1. Zonă protejată (ProtectedSite)
Zonă desemnată sau administrată în temeiul unui cadru legislativ internațional, comunitar sau național, în scopul atingerii unor obiective specifice de conservare.
Atribute ale tipului de obiect spațial „ProtectedSite”
Atribut | Definiție | Tip | Voidability
geometry | Geometrie care definește limitele zonei protejate. | GM_Object |
inspireID | Identificator de obiect extern al obiectului spațial. | Identifier |
legalFoundationDate | Data la care a fost înființată în mod legal zona protejată. Aceasta reprezintă data la care a fost înființat obiectul din lumea reală și nu data la care a fost creată reprezentarea acestuia într-un sistem de informare. | DateTime | voidable
legalFoundationDocument | Un URL sau citarea textului cu trimitere la actul juridic prin care a fost înființată zona protejată. | CI_Citation | voidable
siteDesignation | Desemnarea (Tipul desemnării) zonei protejate. | DesignationType | voidable
siteName | Denumirea zonei protejate. | GeographicalName | voidable
siteProtectionClassification | Clasificarea zonei protejate în funcție de obiectivul protejării. | ProtectionClassificationValue | voidable
9.2. Tipuri de date
9.2.1. Tipul desemnării (DesignationType)
Tip de date proiectat să conțină o desemnare a zonei protejate, incluzând sistemul de desemnare utilizat și valoarea în cadrul sistemului respectiv.
Atribute ale tipului de date „DesignationType ”
Atribut | Definiție | Tip | Voidability
designation | Desemnarea reală a zonei. | DesignationValue |
designationScheme | Sistemul din care provine codul de desemnare. | DesignationSchemeValue |
percentageUnderDesignation | Proporție a zonei care intră în sfera desemnării. Aceasta este utilizată în special pentru clasificarea UICN. Atunci când nu se furnizează o anumită valoare pentru acest atribut, se presupune că aceasta este de 100 %. | Percentage |
Constrângeri ale tipului de date „DesignationType”
Zonele trebuie să utilizeze desemnări provenite dintr-un sistem de desemnare adecvat, iar valoarea codului de desemnare trebuie să fie în concordanță cu sistemul de desemnare.
9.3. Enumerări
9.3.1. Clasificare în funcție de protecție (ProtectionClassificationValue)
Clasificarea zonei protejate în funcție de obiectivul protecției.
Valori permise pentru enumerarea „ProtectionClassificationValue”
Valoare | Definiție
natureConservation | Zona este protejată în scopul conservării diversității biologice.
archaeological | Zona este protejată în scopul conservării patrimoniului arheologic.
cultural | Zona este protejată în scopul conservării patrimoniului cultural.
ecological | Zona este protejată în scopul menținerii stabilității ecologice.
landscape | Zona este protejată în scopul menținerii caracteristicilor peisajului.
environment | Zona este protejată în scopul menținerii stabilității mediului.
geological | Zona este protejată în scopul menținerii caracteristicilor geologice.
9.4. Liste de coduri
9.4.1. Sistem de desemnare (DesignationSchemeValue)
Sistem utilizat pentru atribuirea unei desemnări zonelor protejate.
Această listă de coduri poate fi extinsă de statele membre.
9.4.2. Desemnare (DesignationValue)
Tip abstract fundamental pentru listele de coduri conținând tipurile de clasificare și desemnare în conformitate cu sisteme diferite.
Acest tip este abstract.
9.4.3. Desemnare UICN (IUCNDesignationValue)
Listă de coduri pentru sistemul de clasificare al Uniunii Internaționale pentru Conservarea Naturii.
Acest tip este un subtip al „DesignationValue”.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
9.4.4. Desemnare în temeiul Registrului monumentelor naționale (NationalMonumentsRecordDesignationValue)
Listă de coduri pentru sistemul de clasificare a Registrului monumentelor naționale.
Acest tip este un subtip al „DesignationValue”.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
9.4.5. Desemnare Natura2000 (Natura2000DesignationValue)
Listă de coduri pentru sistemul de clasificare Natura2000, în conformitate cu Directiva 92/43/CEE a Consiliului (1) (Directiva „Habitate”).
Acest tip este un subtip al „DesignationValue”.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
9.4.6. Desemnare Ramsar (RamsarDesignationValue)
Listă de coduri pentru sistemul de desemnare prevăzut de Convenția asupra zonelor umede de importanță internațională (Convenția de la Ramsar).
Acest tip este un subtip al „DesignationValue”.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
9.4.7. Desemnare conform programului UNESCO „Omul și biosfera” (UNESCOManAndBiosphereProgrammeDesignationValue)
Listă de coduri pentru sistemul de clasificare al programului „Omul și biosfera”.
Acest tip este un subtip al „DesignationValue”.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
9.4.8. Desemnare conform patrimoniului mondial UNESCO (UNESCOWorldHeritageDesignationValue)
Listă de coduri pentru sistemul de desemnare a patrimoniului mondial.
Acest tip este un subtip al „DesignationValue”.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
9.5. Straturi
Strat pentru categoria de date spațiale „Zone protejate”
Numele stratului | Titlul stratului | Tip (tipuri) de obiect spațial
PS.ProtectedSite | Zone protejate | ProtectedSite
(1) JO L 206, 22.7.1992, p. 7.
