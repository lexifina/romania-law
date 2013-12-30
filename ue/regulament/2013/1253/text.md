REGULAMENTUL (UE) NR. 1253/2013 AL COMISIEI
din 21 octombrie 2013
de modificare a Regulamentului (UE) nr. 1089/2010 de punere în aplicare a Directivei 2007/2/CE în ceea ce privește interoperabilitatea seturilor și serviciilor de date spațiale
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Directiva 2007/2/CE a Parlamentului European și a Consiliului din 14 martie 2007 de instituire a unei infrastructuri pentru informații spațiale în Comunitatea Europeană (INSPIRE) (1), în special articolul 7 alineatul (1),
întrucât:
(1) Regulamentul (UE) nr. 1089/2010 al Comisiei din 23 noiembrie 2010 de punere în aplicare a Directivei 2007/2/CE a Parlamentului European și a Consiliului în ceea ce privește interoperabilitatea seturilor și serviciilor de date spațiale (2) stabilește modalitățile tehnice pentru interoperabilitatea seturilor de date spațiale aferente categoriilor de date spațiale din anexa I la Directiva 2007/2/CE.
(2) Pentru a garanta deplina interoperabilitate a seturilor de date spațiale, este oportun să se stabilească modalitățile tehnice pentru interoperabilitatea seturilor de date spațiale aferente categoriilor de date spațiale din anexele II și III la Directiva 2007/2/CE.
(3) Pentru a asigura coerența globală a modalităților tehnice pentru interoperabilitatea seturilor de date spațiale incluse în prezentul regulament, actualele modalități tehnice pentru interoperabilitatea seturilor de date spațiale aferente categoriilor de date spațiale din anexa I la Directiva 2007/2/CE ar trebui modificate.
(4) În primul rând, ar trebui modificate cerințele privind listele de coduri pentru a permite o abordare flexibilă în ceea ce privește descrierea valorilor din listele de coduri la niveluri diferite de detaliu și pentru a prevedea modalitățile tehnice pentru utilizarea în comun a listelor de coduri extinse.
(5) În al doilea rând, limitarea proprietăților spațiale la schema spațială Simple Feature (Caracteristică simplă) ar trebui să fie mai flexibilă pentru a permite punerea la dispoziție, de asemenea, a datelor în 2,5D.
(6) În al treilea rând, ar trebui să se introducă un element de metadate suplimentar pentru a permite tipului de reprezentare spațială (spatial representation type) utilizat pentru un set de date.
(7) În al patrulea rând, categoria de date spațiale „Sisteme de caroiaj geografic” ar trebui extinsă pentru a include un caroiaj de rezoluție multiplă bazat pe coordonate geografice.
(8) În al cincilea rând, categoria de date spațiale „Unități administrative” ar trebui extinsă pentru a descrie unitățile administrative maritime.
(9) În al șaselea rând, pentru a evita suprapunerile cu tipurile de obiecte spațiale specificate pentru categoriile de date spațiale din anexele II și III la Directiva 2007/2/CE, anumite tipuri candidat ar trebui eliminate din categoriile de date spațiale „Unități administrative” și „Hidrografie”.
(10) Prin urmare, Regulamentul (UE) nr. 1089/2010 ar trebui modificat în consecință.
(11) Măsurile prevăzute de prezentul regulament sunt conforme cu avizul comitetului instituit în temeiul articolului 22 din Directiva 2007/2/CE,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Regulamentul (UE) nr. 1089/2010 se modifică după cum urmează:
(1) Articolul 2 se modifică după cum urmează:
(a) teza introductivă se înlocuiește cu următorul text:
„În sensul prezentului regulament, se aplică următoarele definiții, precum și definițiile tematice prevăzute în anexe:”
(b) punctul 4 se elimină;
(c) la punctul 6, „ISO 19103” se înlocuiește cu „ISO/TS 19103:2005”;
(d) la punctul 9, „EN ISO 19135” se înlocuiește cu „EN ISO 19135:2007”;
(e) la punctul 11, „EN ISO 19128” se înlocuiește cu „EN ISO 19128:2008”;
(f) la punctul 13, „EN ISO 19115” se înlocuiește cu „EN ISO 19115:2005/AC:2008”;
(g) la punctul 15, „EN ISO 19135” se înlocuiește cu „EN ISO 19135:2007”;
(h) la punctul 18, „ISO 19103” se înlocuiește cu „ISO/TS 19103:2005”;
(i) se adaugă următoarele puncte 21 - 30:
„21. | «proprietate» (property) înseamnă atribut sau rol de asociere,
22. «uniune» (union type) înseamnă un tip format din una și numai una dintre cele câteva alternative (enumerate ca «atribute membre»), în conformitate cu ISO/TS 19103:2005,
23. «clasă de asociere» (association class) înseamnă un tip care definește proprietăți suplimentare în ceea ce privește o relație între două alte tipuri,
24. «acoperire» (coverage) înseamnă un obiect spațial care acționează ca o funcție menită să returneze valori din intervalul său pentru orice poziție directă din domeniul său spațial, temporal sau spațio-temporal, în conformitate cu ISO 19123:2007,
25. «domeniu» (domain) înseamnă un set bine definit, în conformitate cu ISO/TS 19103:2005,
26. «interval» (range) înseamnă un set de valori de atribute de entități asociate printr-o funcție elementelor domeniului unei acoperiri, în conformitate cu EN ISO 19123:2007,
27. «caroiaj rectificat» (rectified grid) înseamnă un caroiaj pentru care există o transformare afină între coordonatele din grilă și coordonatele unui sistem de referință de coordonate, în conformitate cu EN ISO 19123:2007,
28. «caroiaj referențiabil» (referenceable grid) înseamnă un caroiaj asociat cu o transformare care poate fi utilizată pentru a converti valorile coordonatelor caroiajului în valori ale coordonatelor referențiate la un sistem de referință de coordonate extern, în conformitate cu EN ISO 19123:2007,
29. «structură în mozaic» (tessellation) înseamnă o compartimentare a unui spațiu într-un set de subspații adiacente având aceeași dimensiune ca și spațiul compartimentat. O structură în mozaic într-un spațiu 2D constă dintr-un set de poligoane nesuprapuse, care acoperă în întregime o regiune de interes,
30. «valoare mai restrânsă» (narrower value) înseamnă o valoare care are o relație ierarhică cu o valoare-mamă mai generală.”
(2) Articolul 4 se modifică după cum urmează:
(a) Punctul 1 se înlocuiește cu următorul text:
„1. Pentru schimbul de obiecte spațiale din seturile de date care îndeplinesc condițiile stabilite la articolul 4 din Directiva 2007/2/CE și pentru clasificarea acestora, statele membre utilizează tipurile de obiecte spațiale și tipurile de date, enumerările și listele de coduri asociate care sunt definite în anexele II, III și IV pentru categoriile la care se referă seturile de date.”
(b) Toate trimiterile la „anexa II” de la punctele 2 și 3 se înlocuiesc cu trimiteri la „anexe”.
(c) La punctul 3, a doua teză se înlocuiește cu următorul text: „Valorile de enumerare și valorile listelor de coduri sunt identificate în mod unic cu ajutorul codurilor mnemonice pentru computere, neutre din punct de vedere lingvistic. Valorile pot include, de asemenea, o denumire specifică unei limbi, care urmează să fie utilizată în interacțiunea umană.”
(3) La articolul 5, alineatul (4) se elimină.
(4) Articolul 6 se înlocuiește cu următorul text:
„Articolul 6
Liste de coduri și enumerări
1. Listele de coduri aparțin unuia dintre următoarele tipuri, astfel cum este prevăzut în anexe:
(a) liste de coduri ale căror valori permise includ doar valorile specificate în prezentul regulament;
(b) liste de coduri ale căror valori permise includ valorile specificate în prezentul regulament și valori mai restrânse definite de furnizorii de date;
(c) liste de coduri ale căror valori permise includ valorile specificate în prezentul regulament și valori suplimentare la orice nivel definit de furnizorii de date;
(d) liste de coduri, ale căror valori permise includ orice valori definite de furnizorii de date.
În sensul literelor (b), (c) și (d), în afara valorilor permise, furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE (INSPIRE Technical Guidance) relevant, disponibil pe site-ul web INSPIRE al Centrului Comun de Cercetare.
2. Listele de coduri pot fi ordonate ierarhic. Valorile din listele de coduri ierarhice pot avea o valoare-mamă mai generală. În cazul în care valorile valide dintr-o listă de coduri ierarhică sunt indicate într-un tabel din prezentul regulament, valorile-mamă trebuie enumerate în ultima coloană.
3. În cazul în care, pentru un atribut al cărui tip este o listă de coduri astfel cum se menționează la alineatul (1) literele (b), (c) sau (d), un furnizor de date furnizează o valoare care nu este specificată în prezentul regulament, valoarea respectivă și definiția aferentă sunt puse la dispoziție într-un registru.
4. Atributele sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date al căror tip este o listă de coduri pot lua doar valori care sunt permise în conformitate cu specificațiile din lista de coduri.
5. Atributele sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date care au un tip de enumerare pot lua valori doar din listele indicate pentru tipul de enumerare respectiv.”
(5) La articolul 8 alineatul (2) și la articolul 11 alineatul (1), trimiterile la „anexa II” se înlocuiesc cu trimiteri la „anexe”.
(6) Articolul 12 se modifică după cum urmează:
(a) Alineatul (1) se înlocuiește cu următorul text:
„1. Domeniul de valori al proprietăților spațiale definite în prezentul regulament trebuie limitat la schema spațială Simple Feature, astfel cum este definită în Herring, John R. (ed.), OpenGIS® Implementation Standard for Geographic information – Simple feature access – Part 1: Common architecture, version 1.2.1, Open Geospatial Consortium, 2011, în absența unor indicații contrare privind o anumită categorie sau un anumit tip de date spațiale.”
(b) Alineatul (2) se modifică după cum urmează:
„unități SI” se înlocuiesc cu „unități SI sau unități non-SI acceptate spre a fi utilizate împreună cu Sistemul Internațional de Unități”.
(7) La articolul 13, se introduce următorul punct 6:
„6. | Tip de reprezentare spațială: Metoda utilizată pentru a reprezenta informații geografice în spațiu.”
(8) Articolul 14 se modifică după cum urmează:
(a) Alineatul (2) litera (b) se înlocuiește cu următorul text:
„(b) | tipul (tipurile) de obiecte spațiale, sau un subset al acestuia, care constituie conținutul stratului.”
(b) Se adaugă următorul alineat (3):
„3. Pentru tipurile de obiecte spațiale ale căror obiecte pot fi clasificate utilizându-se un atribut cu valoare în lista de coduri, pot fi definite mai multe straturi. Fiecare dintre aceste straturi include obiectele spațiale care corespund unei singure valori specifice din lista de coduri. În definirea unor astfel de seturi de straturi din anexele II, III și IV, toate condițiile următoare trebuie îndeplinite:
(a) parametrul substituibil <ValoaredinListadeCoduri> reprezintă valorile din lista de coduri relevantă, prima literă fiind reprezentată cu majuscule;
(b) parametrul substituibil <denumire lizibilă de către om> reprezintă denumirea lizibilă de către om a valorilor din lista de coduri;
(c) tipul de obiect spațial include atributul și lista de coduri relevante, între paranteze;
(d) se dă un exemplu de strat.”
(9) Anexa I se modifică conform anexei I la prezentul regulament.
(10) Anexa II se modifică conform anexei II la prezentul regulament.
(11) Se adaugă anexa III, conform anexei III la prezentul regulament.
(12) Se adaugă anexa IV, conform anexei IV la prezentul regulament.
Articolul 2
Prezentul regulament intră în vigoare în [a douăzecea] zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre în conformitate cu tratatele.
Adoptat la Bruxelles, 21 octombrie 2013.
Pentru Comisie
Președintele
José Manuel BARROSO
(1) JO L 108, 25.4.2007, p. 1.
(2) JO L 323, 8.12.2010, p. 11.
ANEXA I
Anexa I la Regulamentul (UE) nr. 1089/2010 se modifică după cum urmează:
(1) Titlul se înlocuiește cu următorul text: „Tipuri comune, definiții și cerințe”.
(2) În tot cuprinsul textului, cu excepția cazului în care se prevede altfel în prezenta anexă, teza „Această listă de coduri nu poate fi extinsă de statele membre.” se înlocuiește cu teza „Valorile permise pentru această listă de coduri cuprind numai valorile din tabelul de mai jos.”
(3) În tot cuprinsul textului, în rubricile din toate tabelele care indică valorile din lista de coduri, textul „Valori permise pentru lista de coduri” se înlocuiește cu textul „Valori pentru lista de coduri”.
(4) Secțiunea 1 se înlocuiește cu următoarea secțiune:
„1. TIPURI DEFINITE ÎN STANDARDELE EUROPENE ȘI INTERNAȚIONALE
Următoarele tipuri comune, utilizate în atributele sau rolurile de asociere ale tipurilor de obiecte spațiale sau ale tipurilor de date, sunt definite după cum urmează:
(1) Pentru tipurile «Any», «Angle», «Area», «Boolean», «CharacterString», «Date», «DateTime», «Decimal», «Distance», «Integer», «Length», «Measure», «Number», «Probability», «Real», «RecordType», «Sign», «UnitOfMeasure», «Velocity» și «Volume» se aplică definițiile prevăzute în ISO/TS 19103:2005.
(2) Pentru tipurile «DirectPosition», «GM_Boundary», «GM_Curve», «GM_MultiCurve», «GM_MultiSurface», «GM_Object», «GM_Point», «GM_Primitive», «GM_Solid», «GM_Surface» și «GM_Tin», se aplică definițiile prevăzute în EN ISO 19107:2005.
(3) Pentru tipurile «TM_Duration», «TM_GeometricPrimitive», «TM_Instant», «TM_Object», «TM_Period» și «TM_Position», se aplică definițiile prevăzute în EN ISO 19108:2005/AC:2008.
(4) Pentru tipul «GF_PropertyType», se aplică definiția prevăzută în EN ISO 19109:2006.
(5) Pentru tipurile «CI_Citation», «CI_Date», «CI_RoleCode», «EX_Extent», «EX_VerticalExtent», «MD_Distributor», «MD_Resolution» și «URL», se aplică definițiile prevăzute în EN ISO 19115:2005/AC:2008.
(6) Pentru tipul «CV_SequenceRule», se aplică definiția prevăzute în EN ISO 19123:2007.
(7) Pentru tipurile «AbstractFeature», «Quantity» și «Sign», se aplică definițiile prevăzute în ISO 19136:2009.
(8) Pentru tipurile «LocalisedCharacterString», «PT_FreeText» și «URI», se aplică definițiile din CEN ISO/TS 19139:2009.
(9) Pentru tipul «LC_LandCoverClassificationSystem», se aplică definiția prevăzută în ISO 19144-2:2012.
(10) Pentru tipurile «GFI_Feature», «Location», «NamedValue», «OM_Observation», «OM_Process», «SamplingCoverageObservation», «SF_SamplingCurve», «SF_SamplingPoint», «SF_SamplingSolid», «SF_SamplingSurface» și «SF_SpatialSamplingFeature», se aplică definițiile prevăzute în ISO 19156: 2011.
(11) Pentru tipurile «Category», «Quantity», «QuantityRange» și «Time», se aplică definițiile din Robin, Alexandre (ed.), OGC®SWE Common Data Model Encoding Standard, version 2.0.0, Open Geospatial Consortium, 2011.
(12) Pentru tipurile «TimeValuePair» și «Timeseries», se aplică definițiile din Taylor, Peter (ed.), OGC® WaterML 2.0: Part 1 – Timeseries, v2.0.0, Open Geospatial Consortium, 2012.
(13) Pentru tipurile «CGI_LinearOrientation» și «CGI_PlanarOrientation», se aplică definițiile din CGI Interoperability Working Group, Geoscience Markup Language (GeoSciML), version 3.0.0, Commission for the Management and Application of Geoscience Information (CGI) of the International Union of Geological Sciences, 2011.”
(5) Secțiunea 2 se modifică după cum urmează:
(a) În secțiunea 2.1, următoarele constrângeri se elimină:
„ Constrângerile tipului de date «Identifier»
Atributele «localId» și «namespace» utilizează numai următorul set de caractere: {«A» … «Z», «a» … «z», «0» … «9», «_», «.», «-»}, adică sunt permise numai litere din alfabetul latin, cifre, caracter de subliniere, punctul și liniuța.”
(b) Se adaugă următoarele subsecțiuni 2.2 - 2.7:
„2.2 Parte asociată (RelatedParty)
O organizație sau o persoană cu un rol în ceea ce privește o resursă.
Atribute ale tipului de date «RelatedParty»
Atribut | Definiție | Tip | Voidability
individualName | Numele persoanei asociate. | PT_FreeText | voidable
organisationName | Numele organizației asociate. | PT_FreeText | voidable
positionName | Poziția părții în legătură cu o resursă, cum ar fi cea de șef de departament. | PT_FreeText | voidable
contact | Informații de contact pentru partea asociată. | Contact | voidable
role | Rolurile părții în raport cu o resursă, cum ar fi «proprietar». | PartyRoleValue | voidable
Constrângerile tipului de date «RelatedParty»
Trebuie să se furnizeze cel puțin numele persoanei, al organizației sau al poziției.
2.3 Contact (Contact)
Canalele de comunicare prin care este posibil să se obțină accesul la cineva sau la ceva.
Atribute ale tipului de date «Contact»
Atribut | Definiție | Tip | Voidability
address | O adresă furnizată ca text liber. | AddressRepresentation | voidable
contactInstructions | Instrucțiuni suplimentare cu privire la modul sau momentul în care poate fi contactată o persoană sau o organizație. | PT_FreeText | voidable
electronicMailAddress | O adresă de poștă electronică a organizației sau a persoanei. | CharacterString | voidable
hoursOfService | Perioadele de timp când poate fi contactată organizația sau persoana. | PT_FreeText | voidable
telephoneFacsimile | Numărul de fax al organizației sau al persoanei. | CharacterString | voidable
telephoneVoice | Numărul de telefon al organizației sau al persoanei. | CharacterString | voidable
website | Pagini furnizate pe World Wide Web de către o organizație sau o persoană. | URL | voidable
2.4 Citare de document (DocumentCitation)
Citare în scopul realizării de trimiteri clare la un document.
Atribute ale tipului de date «DocumentCitation»
Atribut | Definiție | Tip | Voidability
name | Numele documentului. | CharacterString |
shortName | Denumirea prescurtată sau titlul alternativ al documentului. | CharacterString | voidable
date | Data creării, publicării sau revizuirii documentului. | CI_Date | voidable
link | Legătură către o versiune online a documentului | URL | voidable
specificReference | Trimitere la o anumită parte a documentului. | CharacterString | voidable
2.5 Citare a legislației (LegislationCitation)
Citare în scopul realizării unei trimiteri clare la un act legislativ sau la o anumită parte a unui act legislativ.
Acest tip este un subtip al «DocumentCitation».
Atribute ale tipului de date «LegislationCitation»
Atribut | Definiție | Tip | Voidability
identificationNumber | Cod utilizat pentru a identifica instrumentul legislativ | CharacterString |
officialDocumentNumber | Numărul oficial al documentului, utilizat pentru a identifica în mod univoc instrumentul legislativ. | CharacterString |
dateEnteredIntoForce | Data la care instrumentul legislativ a intrat în vigoare. | TM_Position |
dateRepealed | Data la care instrumentul legislativ a fost abrogat. | TM_Position |
level | Nivelul la care instrumentul legislativ este adoptat. | LegislationLevelValue |
journalCitation | Citarea Jurnalul Oficial în care este publicat textul legislativ. | OfficialJournalInformation |
Constrângerile tipului de date «LegislationCitation»
În cazul în care atributul «link» este nul (void), trebuie să se furnizeze citarea Jurnalului Oficial.
2.6 Informații referitoare la Jurnalul Oficial (OfficialJournalInformation)
Citarea completă a localizării instrumentului legislativ în Jurnalul Oficial.
Atribute ale tipului de date «OfficialJournalInformation»
Atribut | Definiție | Tip | Voidability
officialJournalIdentification | Trimiterea la locul din Jurnalul Oficial unde a fost publicat instrumentul legislativ. Această trimitere este compusă din trei părți: — titlul Jurnalului Oficial — volumul și/sau seria — pagina (paginile) | CharacterString |
ISSN | Numărul internațional standard pentru publicații seriale (ISSN) este un număr format din opt cifre care identifică publicația periodică în care a fost publicat instrumentul legislativ. | CharacterString |
ISBN | Numărul internațional standardizat al cărții (ISBN) este un număr format din nouă cifre care identifică în mod univoc cartea în care a fost publicat instrumentul legislativ. | CharacterString |
linkToJournal | Link la o versiune online a Jurnalului Oficial | URL |
2.7 Identificator tematic (ThematicIdentifier)
Identificator tematic utilizat pentru a identifica în mod univoc obiectul spațial.
Atribute ale tipului de date «ThematicIdentifier»
Atribut | Definiție | Tip | Voidability
identifier | Identificator unic utilizat pentru a identifica obiectul spațial în cadrul schema de identificare specificată. | CharacterString |
identifierScheme | Identificator care definește schema utilizată pentru atribuirea identificatorului. | CharacterString” |
(6) Secțiunea 4 se modifică după cum urmează:
(a) Secțiunea 4.1 se înlocuiește cu următorul text:
„4.1 Stare a instalației (ConditionOfFacilityValue)
Starea unei instalații din punctul de vedere al finalizării și exploatării acesteia.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Valori ale listei de coduri «ConditionOfFacilityValue»
Valoare | Nume | Definiție
functional | funcțională | Instalația este funcțională.
projected | proiectată | Instalația este în curs de proiectare. Lucrările de construcție nu au început încă.
underConstruction | în construcție | Instalația este în construcție și nu este încă funcțională. Se aplică numai construcției inițiale a instalației și nu lucrărilor de întreținere.
disused | neutilizată | Instalația nu mai este utilizată, dar nu este în curs de dezafectare și nici nu a fost dezafectată.
decommissioned | dezafectată | Instalația nu mai este utilizată și este în curs de dezafectare sau a fost dezafectată.”
(b) În secțiunea 4.2 Cod de țară (CountryCode), teza „Această listă de coduri nu poate fi extinsă de către statele membre.” se elimină.
(c) Se adaugă următoarele subsecțiuni 4.3 – 4.6:
„4.3 Nivel al legislației (LegislationLevelValue)
Nivelul la care un act juridic sau o convenție a fost adoptat(ă).
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile indicate în Ghidul tehnic INSPIRE privind modelul conceptual generic INSPIRE.
4.4 Rol al părții (PartyRoleValue)
Rolurile părților care sunt asociate unei resurse sau sunt responsabile pentru aceasta.
Valorile permise pentru această listă de coduri cuprind valorile următoarelor liste de coduri sau alte liste de coduri indicate de furnizorii de date:
— Codul rolului (CI_RoleCode): Funcțiile îndeplinite de o parte responsabilă, în conformitate cu EN ISO 19115:2005/AC:2008.
— Rolul unei părți asociate (RelatedPartyRoleValue): Clasificarea rolurilor părții asociate, conform celor specificate în tabelul de mai jos.
Valori ale listei de coduri «RelatedPartyRoleValue»
Valoare | Nume | Definiție
authority | autoritate | O parte mandatată legal să supravegheze o resursă și/sau părți asociate resursei.
operator | operator | O parte care exploatează o resursă.
owner | proprietar | O parte care deține o resursă, și anume, căreia îi aparține resursa în sens juridic.
4.5 Nume standard în domeniul climei și al prognozei (CFStandardNamesValue)
Definiții ale fenomenelor observate în meteorologie și oceanografie.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile indicate în Ghidul tehnic INSPIRE privind modelul conceptual generic INSPIRE.
4.6 Gen (GenderValue)
Genul unei persoane sau al unui grup de persoane.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori ale listei de coduri «GenderValue»
Valoare | Nume | Definiție
female | feminin | O persoană sau un grup de persoane de sex feminin.
male | masculin | O persoană sau un grup de persoane de sex masculin.
unknown | necunoscută | O persoană sau un grup de persoane de sex necunoscut.”
(7) După secțiunea 5, se adaugă următoarele secțiuni 6, 7 și 8:
„6. MODEL DE ACOPERIRE (COVERAGE MODEL)
Modelul de acoperire INSPIRE constă din următoarele pachete:
— Acoperiri (Base)
— Acoperiri (Domain and Range)
6.1. Acoperiri (Base)
6.1.1. Tipuri de obiecte spațiale
Pachetul Acoperiri (Bază) conține tipul de obiect spațial «Coverage».
6.1.1.1. Acoperire (Coverage)
Obiect spațial care acționează ca o funcție menită să returneze valori din intervalul său pentru orice poziție directă din domeniul său spațial, temporal sau spațio-temporal.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «Coverage»
Atribut | Definiție | Tip | Voidability
metadata | Metadate specifice aplicației acoperirii. | Any |
rangeType | Descriere a structurii intervalului de valori. | RecordType |
6.2. Acoperiri (Domeniu și interval)
6.2.1. Tipuri de obiecte spațiale
Pachetul Acoperiri (Domeniu și interval) conține următoarele tipuri de obiecte spațiale:
— Acoperire (Reprezentare a domeniului și a intervalului) [Coverage (Domain And Range Representation)]
— Acoperire de tip caroiaj rectificat (Rectified Grid Coverage)
— Acoperire de tip caroiaj referențiabil (Referenceable Grid Coverage)
6.2.1.1. Acoperire (Reprezentare a domeniului și a intervalului) (CoverageByDomainAndRange)
Acoperire care tratează domeniul și intervalul ca proprietăți separate.
Acest tip este un subtip al entității «Coverage».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «CoverageByDomainAndRange»
Atribut | Definiție | Tip | Voidability
coverageFunction | Descriere a modului în care pot fi obținute valori ale intervalului în poziții din domeniul acoperirii. | CoverageFunction |
domainSet | Configurația domeniului acoperirii, din punctul de vedere al coordonatelor. | Any |
rangeSet | Set de valori asociate elementelor domeniului acoperirii prin intermediul unei funcții. | Any |
Constrângeri ale tipului de obiect spațial «CoverageByDomainAndRange»
Funcția «caroiaj» este valabilă doar pentru domenii care sunt caroiaje.
6.2.1.2. Acoperire de tip caroiaj rectificat (RectifiedGridCoverage)
Acoperire al cărei domeniu constă dintr-un caroiaj rectificat.
Acest tip este un subtip al «CoverageByDomainAndRange».
Constrângeri ale tipului de obiect spațial «RectifiedGridCoverage»
Domeniul este un caroiaj rectificat.
Punctele de caroiaj ale unei «RectifiedGridCoverage» trebuie să coincidă cu centrele celulelor caroiajelor geografice definite în secțiunea 2.2 din anexa II, indiferent de nivelul rezoluției.
6.2.1.3. Acoperire de tip caroiaj referențiabil (ReferenceableGridCoverage)
Acoperire al cărei domeniu constă dintr-un caroiaj referențiabil.
Acest tip este un subtip al «CoverageByDomainAndRange».
Constrângeri ale tipului de obiect spațial «ReferenceableGridCoverage»
Domeniul este un caroiaj referențiabil.
6.2.2. Tipuri de date
6.2.2.1. Funcție de acoperire (CoverageFunction)
Descriere a modului în care pot fi obținute valori ale intervalului în locații din domeniul acoperirii.
Acest tip este o uniune.
Atribute ale tipului uniune «CoverageFunction»
Atribut | Definiție | Tip | Voidability
ruleDefinition | O descriere formală sau informală a funcției de acoperire sub formă de text. | CharacterString |
ruleReference | O descriere formală sau informală a funcției de acoperire sub formă de trimitere. | URI |
gridFunction | Regulă de cartografiere a geometriilor caroiajului. | GridFunction |
6.2.2.2. Funcție a caroiajului (GridFunction)
O regulă explicită de cartografiere a geometriilor caroiajului.
Atribute ale tipului de date «GridFunction»
Atribut | Definiție | Tip | Voidability
sequenceRule | Descriere a modului în care punctele de caroiaj sunt ordonate pentru asocierea lor cu elementele valorilor din intervalul acoperirii. | CV_SequenceRule |
startPoint | Punctul de caroiaj care trebuie asociat primei înregistrări din intervalul acoperirii. | Integer |
7. MODELUL DE OBSERVĂRI (OBSERVATIONS MODEL)
Modelul INSPIRE bazat pe observări constă din următoarele pachete:
— Trimiteri referitoare la observări
— Procese
— Proprietăți observabile
— Observări specializate
7.1. Trimiteri referitoare la observări
7.1.1. Tipuri de obiecte spațiale
Pachetul «Trimiteri referitoare la observări» conține tipul de obiect spațial «Set de observări».
7.1.1.1. Set de observări (ObservationSet)
Leagă un set de «Observări».
Atribute ale tipului de obiect spațial «ObservationSet»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
extent | Informații despre extinderea spațială și temporală. | EX_Extent |
Roluri de asociere ale tipului de obiect spațial «ObservationSet»
Rol de asociere | Definiție | Tip | Voidability
member | O înregistrare a «ObservationSet». | OM_Observation |
7.2. Procese
7.2.1. Tipuri de obiecte spațiale
Pachetul «Procese» conține tipul de obiect spațial «Process».
7.2.1.1. Proces (Process)
Descriere a unui proces de observare.
Acest tip este un subtip al «OM_Process».
Atribute ale tipului de obiect spațial «Process»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier | voidable
name | Denumirea Procesului. | CharacterString | voidable
type | Tipul de proces. | CharacterString | voidable
documentation | Informații suplimentare (online/offline) asociate procesului. | DocumentCitation | voidable
processParameter | Parametru care controlează aplicarea procesului și, ca o consecință, rezultatele sale. | ProcessParameter | voidable
responsibleParty | Persoană sau organizație asociată procesului. | RelatedParty | voidable
7.2.2. Tipuri de date
7.2.2.1. Parametru de proces (ProcessParameter)
Descrierea parametrului dat.
Atribute ale tipului de date «ProcessParameter»
Atribut | Definiție | Tip | Voidability
name | Denumirea parametrului de proces. | ProcessParameterNameValue |
description | Descrierea parametrului de proces. | CharacterString |
7.2.3. Liste de coduri
7.2.3.1. Denumirea parametrului de proces (ProcessParameterNameValue)
O listă de coduri ale denumirilor parametrilor de proces.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
7.3. Proprietăți observabile
7.3.1. Tipuri de date
7.3.1.1. Constrângere (Constraint)
O constrângere privind o anumită proprietate, de exemplu lungimea de undă = 200nm.
Atribute ale tipului de date «Constraint»
Atribut | Definiție | Tip | Voidability
constrainedProperty | Proprietatea care face obiectul constrângerii, de exemplu, «culoare» în cazul în care constrângerea este «culoare = Blue». | PhenomenonTypeValue |
label | Un titlu lizibil de către om pentru constrângerea în ansamblu. | CharacterString |
7.3.1.2. Constrângere de categorie (CategoryConstraint)
O constrângere bazată pe o categorie descriptivă, de exemplu culoare = «roșu».
Acest tip este un subtip al «Constraint».
Atribute ale tipului de date «CategoryConstraint»
Atribut | Definiție | Tip | Voidability
comparison | Un operator de comparare. În cazul unei constrângeri de categorie, aceasta ar trebui să fie «egalCu» sau «neegalCU». | ComparisonOperatorValue |
value | Valoarea proprietății care face obiectul unei constrângeri, de exemplu «albastru» (dacă proprietatea constrânsă este culoarea). | CharacterString |
7.3.1.3. Constrângere de interval (RangeConstraint)
O constrângere de interval numeric aplicabilă unei proprietăți, de exemplu lungime de undă ≥ 300 nm și lungime de undă ≤ 600 nm.
Acest tip este un subtip al «Constraint».
Atribute ale tipului de date «RangeConstraint»
Atribut | Definiție | Tip | Voidability
value | Intervalul de valori numerice ale proprietății care face obiectul constrângerii. | RangeBounds |
uom | Unități de măsură utilizate în cazul constrângerii. | UnitOfMeasure |
7.3.1.4. Limite ale intervalului (RangeBounds)
Valorile limită de început și de sfârșit ale unui interval numeric (de exemplu, început ≥ 50, sfârșit ≤ 99).
Atribute ale tipului de date «RangeBounds»
Atribut | Definiție | Tip | Voidability
startComparison | Comparatorul utilizat pentru limita inferioară a intervalului (de exemplu «greaterThanOrEqualTo»). | ComparisonOperatorValue |
rangeStart | Limita inferioară a intervalului. | Real |
endComparison | Comparatorul utilizat pentru limita superioară a intervalului (de exemplu «lessThan»). | ComparisonOperatorValue |
rangeEnd | Limita superioară a intervalului. | Real |
7.3.1.5. Constrângere scalară (ScalarConstraint)
O constrângere scalară numerică aplicată unei proprietăți, de exemplu lungime ≥ 1 m.
Acest tip este un subtip al «Constraint».
Atribute ale tipului de date «ScalarConstraint»
Atribut | Definiție | Tip | Voidability
value | Valoarea numerică a proprietății care face obiectul constrângerii. | Real |
comparison | Comparatorul care trebuie utilizat în cazul constrângerii, de exemplu «greaterThan». | ComparisonOperatorValue |
uom | Unități de măsură utilizate în cazul constrângerii. | UnitOfMeasure |
7.3.1.6. Alte constrângeri (OtherConstraint)
O constrângere care nu este modelată în mod structurat, dar care poate fi descrisă cu ajutorul atributului de text liber «description».
Acest tip este un subtip al «Constraint».
Atribute ale tipului de date «OtherConstraint»
Atribut | Definiție | Tip | Voidability
description | O descriere a constrângerii. | CharacterString |
7.3.1.7. Măsură statistică (StatisticalMeasure)
O descriere a unei măsuri statistice, de exemplu «maxima zilnică».
Atribute ale tipului de date «StatisticalMeasure»
Atribut | Definiție | Tip | Voidability
label | Un titlu lizibil de către om pentru măsura statistică. | CharacterString |
statisticalFunction | O funcție statistică, de exemplu, media. | StatisticalFunctionTypeValue |
aggregationTimePeriod | Un interval temporal în care se calculează o statistică, de exemplu o zi, o oră. | TM_Duration |
aggregationLength | Un interval spațial unidimensional în care se calculează o statistică, de exemplu 1 metru. | Length |
aggregationArea | Un interval spațial bidimensional în care se calculează o statistică, de exemplu 1 metru pătrat | Area |
aggregationVolume | Un interval spațial tridimensional în care se calculează o statistică, de exemplu 1 metru cub. | Volume |
otherAggregation | Orice alt tip de agregare. | Any |
Roluri de asociere ale tipului de date «StatisticalMeasure»
Rol de asociere | Definiție | Tip | Voidability
derivedFrom | O măsură statistică poate fi derivată din alta, de exemplu temperaturile maxime lunare pot fi derivate din temperaturile medii zilnice. | StatisticalMeasure |
7.3.2. Enumerări
7.3.2.1. Operator de comparare (ComparisonOperatorValue)
O enumerare a operatorilor de comparare (de exemplu «mai mare decât»)
Valori ale enumerării «ComparisonOperatorValue»
Valoare | Definiție
equalTo | perfect egal cu
notEqualTo | nu este perfect egal cu
lessThan | mai mic de
greaterThan | mai mare decât
lessThanOrEqualTo | mai mic sau perfect egal cu
greaterThanOrEqualTo | mai mare sau perfect egal cu
7.3.3. Liste de coduri
7.3.3.1. Tipuri de fenomene (PhenomenonTypeValue)
O listă de coduri ale fenomenelor (de exemplu temperatură, viteza vântului).
Valorile permise pentru această listă de coduri cuprind valorile următoarelor liste de coduri sau alte liste de coduri indicate de furnizorii de date:
— Nume standard în domeniul climei și al prognozei (CFStandardNamesValue): Definiții ale fenomenelor observate în domeniul meteorologiei și al oceanografiei, conform secțiunii 4.5 din prezenta anexă.
— Numele de parametru de element de profil (ProfileElementParameterNameValue): Proprietăți despre care s-a observat că definesc elementul de profil, conform secțiunii 3.3.8 din anexa IV.
— Numele de parametru de obiect derivat de sol (SoilDerivedObjectParameterNameValue): Proprietăți asociate solului care pot fi derivate din sol și alte date, conform secțiunii 3.3.9 din anexa IV.
— Numele de parametru de profil de sol (SoilProfileParameterNameValue): Proprietăți despre care s-a observat că definesc profilul de sol, conform secțiunii 3.3.12 din anexa IV.
— Numele de parametru de sit al solului (SoilSiteParameterNameValue): Proprietăți despre care s-a observat că definesc situl de sol, conform secțiunii 3.3.13 din anexa IV.
— Componentă de referință a UE privind calitatea aerului (EU_AirQualityReferenceComponentValue): Definiții ale fenomenelor referitoare la calitatea aerului în contextul raportării în temeiul legislației Uniunii, conform secțiunii 13.2.1.1 din anexa IV.
— Tabelul 4.2 GRIB Code și Flags al WMO (GRIB_CodeTable4_2Value): Definiții ale fenomenelor observate în domeniul meteorologiei, conform secțiunii 13.2.1.2 din prezenta anexă.
— Utilizarea parametrului BODC P01 (BODC_P01ParameterUsageValue): Definiții ale fenomenelor observate în domeniul oceanografiei, conform secțiunii 14.2.1.1 din anexa IV.
7.3.3.2. Tipul funcțiilor statistice (StatisticalFunctionTypeValue)
O listă de coduri ale funcțiilor statistice (de exemplu maximum, minimum, mediu).
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
7.4. Observări specializate
7.4.1. Tipuri de obiecte spațiale
Pachetul «Observări specializate» conține următoarele tipuri de obiecte spațiale:
— Observare în caroiaj
— Observare în serii de caroiaje
— Observare punctuală
— Colecție de observări punctuale
— Observări punctuale multiple
— Observare de serie temporală într-un punct
— Observare după profil
— Observare după traiectorie
7.4.1.1. Observare în caroiaj (GridObservation)
Observare reprezentând un câmp în format caroiaj într-un singur moment în timp.
Acest tip este un subtip al «SamplingCoverageObservation».
Constrângeri ale tipului de obiect spațial «GridObservation»
«featureOfInterest» este un «SF_SamplingSolid or SF_SamplingSurface».
«phenomenonTime» este un «TM_Instant».
«result» este un «RectifiedGridCoverage» sau «RefererencableGridCoverage».
7.4.1.2. Observare în serii de caroiaje (GridSeriesObservation)
Observare reprezentând un câmp în format caroiaj în evoluție într-o succesiune de momente.
Acest tip este un subtip al «SamplingCoverageObservation».
Constrângeri ale tipului de obiect spațial «GridSeriesObservation»
«featureOfInterest» este un «SF_SamplingSolid».
«phenomenonTime» este un «TM_Period».
«result» este un «RectifiedGridCoverage» sau un «RefererencableGridCoverage».
7.4.1.3. Observare punctuală (PointObservation)
Observare reprezentând o măsurătoare a unei proprietăți într-un singur punct din timp și spațiu.
Acest tip este un subtip al «SamplingCoverageObservation».
Constrângeri ale tipului de obiect spațial «PointObservation»
«featureOfInterest» este un «SF_SamplingPoint».
«phenomenonTime» este un «TM_Instant».
7.4.1.4. Colecție de observări punctuale (PointObservationCollection)
O colecție de observări punctuale.
Acest tip este un subtip al «ObservationSet».
Constrângeri ale tipului de obiect spațial «PointObservationCollection»
Fiecare membru trebuie să fie un «PointObservation».
7.4.1.5. Observări punctuale multiple (MultiPointObservation)
Observare reprezentând un set de măsurători, toate efectuate exact în același moment, dar în locații diferite.
Acest tip este un subtip al «SamplingCoverageObservation».
Constrângeri ale tipului de obiect spațial «MultiPointObservation»
«featureOfInterest» este un «SF_SamplingCurve», «SF_SamplingSurface» sau «SF_SamplingSolid».
«phenomenonTime» este un «TM_Instant».
«result» este un «MultiPointCoverage».
7.4.1.6. Observare de serie temporală într-un punct (PointTimeSeriesObservation)
Observare reprezentând o serie cronologică de măsurători punctuale ale unei proprietăți, într-o locație fixă din spațiu.
Acest tip este un subtip al «SamplingCoverageObservation».
Constrângeri ale tipului de obiect spațial «PointTimeSeriesObservation»
«featureOfInterest» este un «SF_SamplingPoint».
«phenomenonTime» este un «TM_Period».
«result» este un «Timeseries».
7.4.1.7. Observare după profil (ProfileObservation)
Observare reprezentând măsurarea unei proprietăți de-a lungul unui profil vertical în spațiu la un moment dat.
Acest tip este un subtip al «SamplingCoverageObservation».
Constrângeri ale tipului de obiect spațial «ProfileObservation»
«featureOfInterest» este un «SF_SamplingCurve».
«phenomenonTime» este un «TM_Instant».
«result» este un «ReferenceableGridCoverage» sau un «RectifiedGridCoverage».
Domeniul spațial al rezultatului trebuie să conțină o axă, care trebuie să fie verticală.
7.4.1.8. Observare după traiectorie (TrajectoryObservation)
Observare reprezentând măsurarea unei proprietăți de-a lungul unei curbe șerpuite în timp și spațiu.
Acest tip este un subtip al «SamplingCoverageObservation».
Constrângeri ale tipului de obiect spațial «TrajectoryObservation»
«phenomenonTime» este un «TM_Period».
«result» este un «Timeseries».
Fiecare punct din «result» este un «TimeLocationValueTriple».
«featureOfInterest» este un «SF_Sampling Curve».
7.4.2. Tipuri de date
7.4.2.1. Triplă timp-locație-valoare (TimeLocationValueTriple)
Un set triplu alcătuit din timp, locație, valoare (măsurătoare). De exemplu, într-un punct de pe o traiectorie.
Acest tip este un subtip al «TimeValuePair».
Atribute ale tipului de date «TimeLocationValueTriple»
Atribut | Definiție | Tip | Voidability
location | Locație geografică în care valoarea este valabilă. | GM_Position |
7.5. Cerințe pentru observări
Atunci când tipul «OM_Observation» sau orice subtip al acestuia este utilizat pentru a pune la dispoziție date, se aplică următoarele cerințe:
(1) Tipul «Process» se utilizează pentru a indica procedura utilizată în cazul unui «OM_Observation».
(2) În cazul în care se face trimitere la un «EnvironmentalMonitoringFacility» de la un «OM_Observation», se furnizează un atribut «parameter», al cărui atribut «name» este «relatedMonitoringFeature» și al cărui atribut «value» este de tip «AbstractMonitoringFeature».
(3) Pentru toate codificările utilizate pentru întreg rezultatul «OM_Observation» sau doar pentru o parte a acestuia, trebuie să se pună la dispoziție o Interfață de programare a aplicațiilor (API) care să citească fișierul codificat. Această API trebuie să fie capabilă să facă publice informațiile necesare pentru realizarea obiectelor spațiale INSPIRE.
(4) Dacă atributul «processParameter» este prezent în proprietatea «procedure» a unui obiect «OM_Observation», valoarea sa (un nume) trebuie inclusă în atributul «parameter» al obiectului «OM_Observation».
8. MODELUL COMPLEXULUI DE ACTIVITĂȚI
Modelul complexului de activități INSPIRE conține pachetul «Complex de activități» (Activity Complex).
8.1. Complex de activități
8.1.1. Tipuri de obiecte spațiale
Pachetul «Complex de activități» conține tipul de obiect spațial «Complex de activități».
8.1.1.1. Complex de activități (ActivityComplex)
O singură unitate, atât din punct de vedere tehnic cât și economic, aflată sub controlul managerial al unei entități juridice (operatorul), acoperind activități ca cele enumerate în clasificarea NACE a Eurostat stabilită prin Regulamentul (CE) nr. 1893/2006 al Parlamentului European și al Consiliului (1). Complexul de activități trebuie să reprezinte întreaga zonă, din aceeași locație geografică sau din locații diferite, gestionată de același operator, inclusiv totalitatea infrastructurilor, echipamentelor și materialelor.
Atribute ale tipului de obiect spațial «ActivityComplex»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
thematicId | Identificator tematic al complexului de activități. | ThematicIdentifier |
geometry | Geometria utilizată pentru a defini extinderea sau poziția complexului de activități. | GM_Object |
function | Activități efectuate de complexul de activități. Funcția este descrisă de activitate și eventual completată cu informații cu privire la inputuri și outputuri ca rezultate ale acesteia. | Function |
name | Nume descriptiv al complexului de activități. | CharacterString | voidable
validFrom | Momentul în care complexul de activități a început să existe în lumea reală. | DateTime | voidable
validTo | Momentul în care complexul de activități nu mai există în lumea reală. | DateTime | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
8.1.2. Tipuri de date
8.1.2.1. Funcție (Function)
Funcția a ceva exprimată ca o activitate și ca input și/sau output opțional.
Atribute ale tipului de date «Function»
Atribut | Definiție | Tip | Voidability
activity | Descriere pe categorii a unor procese individuale sau a unei serii organizate de procese înrudite din punct de vedere tehnic, care sunt puse în funcțiune de o unitate economică de tip privat sau public, profit sau nonprofit. | EconomicActivityValue |
input | Orice material clasificat sau înregistrat care intră într-o unitate tehnică și economică, în conformitate cu funcția sa. | InputOutputValue | voidable
output | Orice material clasificat sau înregistrat care iese dintr-o unitate tehnică și economică, în conformitate cu funcția sa. | InputOutputValue | voidable
description | O descriere mai detaliată a funcției. | PT_FreeText | voidable
8.1.2.2. Capacitate (Capacity)
O cuantificare a unei abilități reale sau potențiale de a desfășura o activitate, care, de regulă, nu se modifică, nu se modifică adesea sau nu se modifică în mod semnificativ.
Atribute ale tipului de date «Capacity»
Atribut | Definiție | Tip | Voidability
activity | Descriere pe categorii a unor procese individuale sau a unei serii organizate de procese înrudite din punct de vedere tehnic, care sunt puse în funcțiune de o unitate economică de tip privat sau public, profit sau nonprofit. | EconomicActivityValue |
input | Informații cuantificabile referitoare la orice material clasificat sau înregistrat care intră într-o unitate tehnică și economică, în conformitate cu funcția sa. | InputOutputAmount |
output | Informații cuantificabile referitoare la orice material clasificat sau înregistrat care iese dintr-o unitate tehnică și economică, în conformitate cu funcția sa. | InputOutputAmount |
time | Durata de timp la care se referă capacitatea specificată, de exemplu 1 an pentru o capacitate anuală. | TM_Duration |
description | O descriere a capacității. | PT_FreeText | voidable
8.1.2.3. Cantitate de inputuri sau outputuri (InputOutputAmount)
Tipul, și după caz, cantitatea măsurabilă de material clasificat sau înregistrat care intră într-o unitate tehnică și economică sau iese din aceasta.
Atribute ale tipului de date «InputOutputAmount»
Atribut | Definiție | Tip | Voidability
inputOutput | Un material clasificat sau înregistrat care intră într-o unitate tehnică și economică sau iese din aceasta, în conformitate cu funcția sa. | InputOutputValue |
amount | Cantitatea (cum ar fi volumul sau masa) din materialul clasificat sau înregistrat care intră într-o unitate tehnică și economică sau iese din aceasta. | Measure | voidable
8.1.2.4. Autorizație (Permission)
Decizia oficială (aprobare oficială), prin care se acordă autorizația de a exploata întregul Complex de activități sau doar o parte a acestuia, sub rezerva respectării anumitor condiții care garantează că instalațiile sau părți ale acestora aflate pe același amplasament și exploatate de același operator respectă cerințele impuse de o autoritate competentă. O autorizație poate viza una sau mai multe funcții și poate stabili parametrii de capacitate. Termenul ar putea fi extins astfel încât să vizeze și alte tipuri de certificate sau de documente de o importanță deosebită în funcție de domeniul de aplicare (de exemplu ISO, EMAS, Standardele Naționale de Calitate etc.).
Atribute ale tipului de date «Permission»
Atribut | Definiție | Tip | Voidability
id | Referință de identificare a autorizației. | ThematicIdentifier |
relatedParty | Părțile care au legătură cu autorizația acordată pentru complexul de activități și care pot avea roluri foarte variate, între care se numără, printre altele, cel de autoritate competentă sau de societate. | RelatedParty | voidable
decisionDate | Referință temporală care completează definiția autorizației. | DateTime | voidable
dateFrom | Data începând cu care se aplică și este valabilă autorizația. | DateTime | voidable
dateTo | Data până la care se aplică și este valabilă autorizația. | DateTime | voidable
description | O descriere a autorizației. | PT_FreeText | voidable
permittedFunction | Funcție/funcții pentru care este acordată autorizația. | Function | voidable
permittedCapacity | Cantitatea maximă de intrări și/sau ieșiri specifice activității în conformitate cu autorizația. | Capacity | voidable
8.1.2.5. Descriere a complexului de activități (ActivityComplexDescription)
Informații suplimentare referitoare la un complex de activități, inclusiv descrierea, adresa, datele de contact și părțile asociate.
Atribute ale tipului de obiect spațial «ActivityComplexDescription»
Rol de asociere | Definiție | Tip | Voidability
description | O definiție complementară a «Complexului de activități» și caracteristicile sale. | PT_FreeText | voidable
address | O adresă pentru complexul de activități, și anume, o adresă la care au loc activitățile. | AddressRepresentation | voidable
contact | Date de contact pentru complexul de activități. | Contact | voidable
relatedParty | Informații referitoare la părțile care au legătură cu complexul de activități. Acestea pot avea roluri foarte variate, precum cel de proprietar, operator sau autoritate competentă. | RelatedParty | voidable
8.1.3. Liste de coduri
8.1.3.1. Activitate economică (EconomicActivityValue)
Clasificare a activităților economice.
Valorile permise pentru această listă de coduri cuprind valorile următoarelor liste de coduri sau alte liste de coduri indicate de furnizorii de date:
— Clasificarea UE a activităților economice (EconomicActivityNACEValue): activități economice conform valorilor din clasificarea NACE a Eurostat, astfel cum se menționează în Regulamentul (CE) nr. 1893/2006 al Parlamentului European și al Consiliului (2).
— Clasificarea UE a activităților economice în funcție de statistica în materie de deșeuri (EconomicActivityWasteStatisticsValue): Clasificarea activităților economice în conformitate cu secțiunea 8 din anexa I la Regulamentul (CE) nr. 2150/2002 (3).
— Clasificarea UE a operațiunilor de recuperare și eliminare a deșeurilor (WasteRecoveryDisposalValue): Clasificarea operațiunilor de recuperare și eliminare a deșeurilor în conformitate cu anexele I și II la Directiva 2008/98/CE a Parlamentului European și a Consiliului (4).
8.1.3.2. Input sau output (InputOutputValue)
Clasificarea inputurilor sau a outputurilor.
Valorile permise pentru această listă de coduri cuprind valorile următoarelor liste de coduri sau ale altor liste de coduri indicate de furnizorii de date.
— Clasificarea UE a produselor (ProductCPAValue): Clasificarea produselor în funcție de activitatea economică în conformitate cu Regulamentul (CE) nr. 451/2008 al Parlamentului European și al Consiliului (5).
— Clasificarea UE a deșeurilor (WasteValue): Clasificarea deșeurilor în conformitate cu Decizia 2000/532/CE (6).
8.2. Cerințe pentru complexele de activitate
În cazul în care un furnizor de date utilizează un subtip al «ActivityComplex» pentru a pune la dispoziție informații cu privire la starea, capacitatea fizică, autorizațiile și/sau informațiile suplimentare, trebuie utilizate listele de coduri și tipurile de date («ConditionOfFacilityValue», «Capacity», «Permission», «ActivityComplexDescription») relevante incluse în pachetul «Complex de activitate».”
(1) JO L 393, 30.12.2006, p. 1.
(2) JO L 393, 30.12.2006, p. 1.
(3) JO L 332, 9.12.2002, p. 1.
(4) JO L 312, 22.11.2008, p. 3.
(5) JO L 145, 4.6.2008, p. 65.
(6) JO L 226, 6.9.2000, p. 3.
ANEXA II
Anexa II la Regulamentul (UE) nr. 1089/2010 se modifică după cum urmează:
(1) În tot cuprinsul textului, teza „Această listă de coduri nu poate fi extinsă de către statele membre.” se înlocuiește cu teza „Valorile permise pentru această listă de coduri cuprind numai valorile din tabelul de mai jos.”
(2) În tot cuprinsul textului, în rubricile din toate tabelele care indică valorile din lista de coduri, textul „Valori permise pentru lista de coduri” se înlocuiește cu textul „Valori pentru lista de coduri”.
(3) În secțiunea 1.1, se adaugă următoarele liniuțe:
„— | «nivelul mediu al mării (MSL)» (MSL - mean sea level) înseamnă înălțimea medie a suprafeței mării la o stație de observare a mareelor, pentru toate stadiile mareei pe o perioadă de 19 ani, calculată, de obicei, pe baza citirilor orare ale înălțimii măsurate pornind de la un nivel de referință fix prestabilit (nivelul zero hidrografic).
— «mareea astronomică cea mai mică (LAT)» (LAT - lowest astronomical tide) înseamnă cel mai mic nivel al mareei previzibil a fi înregistrat în condiții meteorologice medii și în orice combinație de condiții astronomice.”
(4) Secțiunea 1.3.3 se modifică după cum urmează:
(a) a doua liniuță se înlocuiește cu următorul text:
„— | În cazul componentei verticale în atmosferă liberă, se utilizează presiunea barometrică, convertită în înălțime, în conformitate cu ISO 2533:1975 (Atmosfera standard internațională) sau alte sisteme de referință lineare sau parametrice. În cazul în care se utilizează alte sisteme de referință parametrice, acestea trebuie să fie descrise într-o trimitere accesibilă utilizându-se EN ISO 19111-2:2012.”
(b) se adaugă următoarele liniuțe:
„— | În cazul componentei verticale în zonele marine în care există o amplitudine semnificativă a mareelor (ape de maree), se utilizează ca suprafață de referință cea mai mică maree astronomică (LAT).
— În cazul componentei verticale în zonele marine fără o amplitudine semnificativă a mareelor, în largul oceanelor și, efectiv, în ape cu o adâncime mai mare de 200 de metri, se utilizează ca suprafață de referință nivelul mediu al mării (MSL) sau un nivel de referință bine definit apropiat de MSL.”
(5) Secțiunea 2.2 se modifică după cum urmează:
(a) Primul alineat se înlocuiește cu următorul text:
„Oricare dintre caroiajele cu locații fixe și clar stabilite, definite în secțiunile 2.2.1 și 2.2.2, se utilizează drept cadru georeferențial pentru a face datele în format caroiaj accesibile în INSPIRE, cu excepția existenței uneia dintre următoarele condiții:
(1) În anexele II-IV pot fi indicate și alte caroiaje pentru categorii specifice de date spațiale. În acest caz, datele schimbate prin utilizarea unui astfel de caroiaj specific categoriei utilizează standarde în care definiția caroiajului este fie inclusă împreună cu datele, fie corelată prin trimiteri.
(2) Pentru referențiere în regiuni situate în afara Europei continentale, statele membre pot defini propriul sistem de referință pe baza unui sistem de referință de coordonate geodezic în concordanță cu sistemul ITRS și a proiecției Lambert Azimuthal Equal Area, respectând aceleași principii precum cele stabilite pentru caroiajul indicat în secțiunea 2.2.1. În acest caz, se creează un identificator pentru sistemul de referință de coordonate.”
(b) Secțiunea 2.2.1 se modifică după cum urmează:
(1) titlul se înlocuiește cu „Caroiaj cu celule de suprafață egală”.
(2) tezele „Caroiajul definit în prezenta secțiune este utilizată într-un cadru georeferențial în care sunt necesare rețele cu locații fixe și clar definite ale celulelor de caroiaj echivalente.” și „Punctul de referință al unei celule de caroiaj este colțul stâng inferior al celulei respective.” se elimină.
(c) Secțiunea 2.2.2 se înlocuiește cu următorul text:
„2.2.2. Caroiaj geografic cu împărțire pe zone
| 1. | Atunci când datele în format caroiaj sunt furnizate cu ajutorul coordonatelor geodezice, astfel cum se specifică în secțiunea 1.3 din prezenta anexă, rețeaua multirezoluție definită în prezenta secțiune poate fi folosită drept cadru georeferențial.
| 2. | Nivelurile rezoluției sunt definite în tabelul 1.
| 3. | Caroiajul se bazează pe sistemul de referință de coordonate geodezic ETRS89-GRS80.
| 4. | Originea caroiajului coincide cu punctul de intersecție al Ecuatorului cu meridianul Greenwich (latitudine GRS80 φ=0; longitudine GRS80 λ=0).
| 5. | Caroiajul trebuie orientat pe direcțiile sud-nord și vest-est, în funcție de rețeaua definită de meridianele și paralelele elipsoidului GRS80.
| 6. | Pentru referențierea caroiajului în regiuni situate în afara Europei continentale, furnizorii de date pot defini propriul caroiaj pe baza unui sistem de referință de coordonate geodezic, conform ITRS, respectând aceleași principii precum cele stabilite pentru Grid_ETRS89-GRS80zn paneuropean. În acest caz, trebuie să se creeze un identificator pentru sistemul de referință de coordonate și un identificator omolog pentru caroiaj.
| 7. | Acest caroiaj trebuie împărțit în zone. Rezoluția sud-nord a caroiajului trebuie să aibă o spațiere unghiulară egală. Rezoluția vest-est a caroiajului se stabilește ca produsul dintre spațierea unghiulară și factorul zonei, astfel cum se definește în tabelul 1.
| 8. | Caroiajul trebuie desemnat Grid_ETRS89-GRS80zn_res, unde n reprezintă numărul zonei, iar res reprezintă dimensiunea celulei în unități unghiulare, astfel cum se indică în tabelul 1. Tabelul 1 Grid_ETRS89-GRS80 comun: Spațiere latitudinală (nivelul rezoluției) și spațiere longitudinală pentru fiecare dintre zone Niveluri de rezoluție | SPAȚIERE LATITUDINALĂ (în arcsecunde) | SPAȚIERE LONGITUDINALĂ (în arcsecunde) | Dimensiunea celulelor Zona 1 (Lat. 0°-50°) | Zona 2 (Lat. 50°-70°) | Zona 3 (Lat. 70°-75°) | Zona 4 (Lat. 75°-80°) | Zona 5 (Lat. 80°-90°) NIVEL 0 | 3 600 | 3 600 | 7 200 | 10 800 | 14 400 | 21 600 | 1 D NIVEL 1 | 3 000 | 3 000 | 6 000 | 9 000 | 12 000 | 18 000 | 50 M NIVEL 2 | 1 800 | 1 800 | 3 600 | 5 400 | 7 200 | 10 800 | 30 M NIVEL 3 | 1 200 | 1 200 | 2 400 | 3 600 | 4 800 | 7 200 | 20 M NIVEL 4 | 600 | 600 | 1 200 | 1 800 | 2 400 | 3 600 | 10 M NIVEL 5 | 300 | 300 | 600 | 900 | 1 200 | 1 800 | 5 M NIVEL 6 | 120 | 120 | 240 | 360 | 480 | 720 | 2 M NIVEL 7 | 60 | 60 | 120 | 180 | 240 | 360 | 1 M NIVEL 8 | 30 | 30 | 60 | 90 | 120 | 180 | 30 S NIVEL 9 | 15 | 15 | 30 | 45 | 60 | 90 | 15 S NIVEL 10 | 5 | 5 | 10 | 15 | 20 | 30 | 5 S NIVEL 11 | 3 | 3 | 6 | 9 | 12 | 18 | 3 S NIVEL 12 | 1,5 | 1,5 | 3 | 4,5 | 6 | 9 | 1 500 MS NIVEL 13 | 1 | 1 | 2 | 3 | 4 | 6 | 1 000 MS NIVEL 14 | 0,75 | 0,75 | 1,5 | 2,25 | 3 | 4,5 | 750 MS NIVEL 15 | 0,5 | 0,5 | 1 | 1,5 | 2 | 3 | 500 MS NIVEL 16 | 0,3 | 0,3 | 0,6 | 0,9 | 1,2 | 1,8 | 300 MS NIVEL 17 | 0,15 | 0,15 | 0,3 | 0,45 | 0,6 | 0,9 | 150 MS NIVEL 18 | 0,1 | 0,1 | 0,2 | 0,3 | 0,4 | 0,6 | 100 MS NIVEL 19 | 0,075 | 0,075 | 0,15 | 0,225 | 0,3 | 0,45 | 75 MS NIVEL 20 | 0,03 | 0,03 | 0,06 | 0,09 | 0,12 | 0,18 | 30 MS NIVEL 21 | 0,015 | 0,015 | 0,03 | 0,045 | 0,06 | 0,09 | 15 MS NIVEL 22 | 0,01 | 0,01 | 0,02 | 0,03 | 0,04 | 0,06 | 10 MS NIVEL 23 | 0,0075 | 0,0075 | 0,015 | 0,0225 | 0,03 | 0,045 | 7 500 MMS NIVEL 24 | 0,003 | 0,003 | 0,006 | 0,009 | 0,012 | 0,018 | 3 000 MMS FACTOR | — | 1 | 2 | 3 | 4 | 6 | —”
(6) Secțiunea 4 se înlocuiește cu următorul text:
„4. UNITĂȚI ADMINISTRATIVE
4.1. Structura categoriei de date spațiale «Unități administrative»
Tipurile indicate pentru categoria de date spațiale «Unități administrative» sunt structurate în următoarele pachete:
— Unități administrative
— Unități maritime
4.2. Unități administrative
4.2.1. Tipuri de obiecte spațiale
Pachetul «Unități administrative» conține următoarele tipuri de obiecte spațiale:
— Limită administrativă
— Unitate administrativă
— Condominium
4.2.1.1. Limită administrativă (AdministrativeBoundary)
Linie de demarcație între unități administrative.
Atribute ale tipului de obiect spațial «AdministrativeBoundary»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
country | Cod de țară alcătuit din două caractere, în conformitate cu Ghidul stilistic interinstituțional publicat de Oficiul pentru Publicații al Uniunii Europene. | CountryCode |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Reprezentare geometrică a liniei de demarcație. | GM_Curve |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
legalStatus | Statut juridic al limitei administrative. | LegalStatusValue | voidable
nationalLevel | Nivelurile ierarhice ale tuturor unităților administrative adiacente din care face parte limita în cauză. | AdministrativeHierarchyLevel |
technicalStatus | Statutul tehnic al limitei administrative. | TechnicalStatusValue | voidable
Roluri de asociere ale tipului de obiect spațial «AdministrativeBoundary»
Rol de asociere | Definiție | Tip | Voidability
admUnit | Unitățile administrative separate de limita administrativă. | AdministrativeUnit | voidable
4.2.1.2. Unitate administrativă (AdministrativeUnit)
Unitate administrativă în care un stat membru deține și/sau își exercită jurisdicția, în ceea ce privește guvernarea la nivel local, regional și național.
Atribute ale tipului de obiect spațial «AdministrativeUnit»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
country | Cod de țară alcătuit din două caractere, în conformitate cu Ghidul stilistic interinstituțional publicat de Oficiul pentru Publicații al Uniunii Europene. | CountryCode |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Reprezentare geometrică a teritoriului acoperit de unitatea administrativă. | GM_MultiSurface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Denumire geografică națională oficială a unității administrative, redactată în mai multe limbi, după caz. | GeographicalName |
nationalCode | Identificator tematic corespunzător codurilor administrative naționale definite în fiecare țară. | CharacterString |
nationalLevel | Nivelul la care se situează unitatea administrativă în ierarhia administrativă națională. | AdministrativeHierarchyLevel |
nationalLevelName | Numele nivelului la care se situează unitatea administrativă în ierarhia administrativă națională. | LocalisedCharacterString | voidable
residenceOfAuthority | Centrul pentru administrația națională sau locală. | ResidenceOfAuthority | voidable
Roluri de asociere ale tipului de obiect spațial «AdministrativeUnit»
Rol de asociere | Definiție | Tip | Voidability
administeredBy | Unitate administrativă situată la același nivel în ierarhia administrativă națională, care administrează această unitate administrativă. | AdministrativeUnit | voidable
boundary | Limitele administrative dintre unitatea administrativă și toate unitățile adiacente acesteia. | AdministrativeBoundary | voidable
coAdminister | Unitate administrativă situată la același nivel în ierarhia administrativă națională care este coadministrată de această unitate administrativă. | AdministrativeUnit | voidable
condominium | Condominiu administrat de unitatea administrativă. | Condominium | voidable
lowerLevelUnit | Unități situate la un nivel inferior în ierarhia administrativă națională, care sunt administrate de unitatea administrativă. | AdministrativeUnit | voidable
upperLevelUnit | Unitate situată la un nivel superior în ierarhia administrativă națională, administrată de unitatea administrativă. | AdministrativeUnit | voidable
Constrângeri ale tipului de obiect spațial «AdministrativeUnit»
Rolul de asociere «condominiu» se aplică exclusiv unităților administrative pentru care nationalLevel=«prim ordin» (nivel de țară).
Unitățile situate la nivelul cel mai scăzut nu pot fi asociate unităților situate la un nivel inferior.
Unitățile situate la nivelul cel mai înalt nu pot fi asociate unităților situate la un nivel superior.
4.2.1.3. Condominiu (Condominium)
Teritoriu administrativ organizat independent de orice diviziune administrativă teritorială națională și administrată de două sau mai multe țări.
Atribute ale tipului de obiect spațial «Condominium»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Reprezentare geometrică a teritoriului acoperit de condominiu. | GM_MultiSurface |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Denumire geografică oficială a condominiului, redactată în mai multe limbi, după caz. | GeographicalName | voidable
Roluri de asociere ale tipului de obiect spațial «Condominium»
Rol de asociere | Definiție | Tip | Voidability
admUnit | Unitate administrativă care administrează condominiul. | AdministrativeUnit | voidable
4.2.2. Tipuri de date
4.2.2.1. Reședință a autorității (ResidenceOfAuthority)
Tip de date reprezentând numele și poziția unei reședințe a autorității.
Atribute ale tipului de date «ResidenceOfAuthority»
Atribut | Definiție | Tip | Voidability
geometry | Poziția reședinței autorității. | GM_Point | voidable
name | Numele reședinței autorității. | GeographicalName |
4.2.3. Enumerări
4.2.3.1. Statut juridic (LegalStatusValue)
Descrierea statutului juridic al limitelor administrative.
Valori permise pentru enumerarea «LegalStatusValue»
Valoare | Definiție
agreed | Limita comună («edge-matched») a fost convenită între unitățile administrative învecinate și este în prezent stabilă.
notAgreed | Limita comună («edge-matched») nu a fost deocamdată convenită între unitățile administrative învecinate și poate fi supusă modificării.
4.2.3.2. Statut tehnic (TechnicalStatusValue)
Descrierea statutului tehnic al limitelor administrative.
Valori permise pentru enumerarea «TechnicalStatusValue»
Valoare | Definiție
edgeMatched | Limitele unităților administrative învecinate au același set de coordonate.
notEdgeMatched | Limitele unităților administrative învecinate nu au același set de coordonate.
4.2.4. Liste de coduri
4.2.4.1. Nivel al ierarhiei administrative (AdministrativeHierarchyLevel)
Niveluri administrative în cadrul ierarhiei administrative naționale. Această listă de coduri reflectă nivelul structurilor administrative în cadrul piramidei ierarhice, care este bazat pe agregarea geometrică de teritorii și care nu descrie în mod necesar legătura de subordonare existentă între autoritățile administrative conexe.
Această listă de coduri este administrată într-un registru comun al listelor de coduri.
4.3. Unități maritime
4.3.1. Tipuri de obiecte spațiale
Pachetul «Unități maritime» conține următoarele tipuri de obiecte spațiale:
— Linie de bază
— Frontieră maritimă
— Zonă maritimă
4.3.1.1. Linie de bază (Baseline)
Linia pornind de la care se măsoară limitele exterioare ale mării teritoriale și alte limite exterioare.
Atribute ale tipului de obiect spațial «Baseline»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «Baseline»
Rol de asociere | Definiție | Tip | Voidability
segment | Segment al unei linii de bază. | BaselineSegment |
4.3.1.2. Frontieră maritimă (MaritimeBoundary)
O linie care descrie separarea oricărui tip de jurisdicție maritimă.
Atribute ale tipului de obiect spațial «MaritimeBoundary»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Reprezentare geometrică a frontierei maritime. | GM_Curve |
country | Țara căreia îi aparține zona maritimă a acestei frontiere. | CountryCode |
legalStatus | Statutul juridic al acestei frontiere maritime. | LegalStatusValue | voidable
technicalStatus | Statutul tehnic al frontierei maritime. | TechnicalStatusValue | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
4.3.1.3. Zonă maritimă (MaritimeZone)
O centură de mare stabilită prin convenții și tratate internaționale, în care statul de coastă își exercită jurisdicția.
Atribute ale tipului de obiect spațial «MaritimeZone»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Reprezentare geometrică a ariei acoperite de această zonă maritime. | GM_MultiSurface |
zoneType | Tipul de zonă maritimă. | MaritimeZoneTypeValue |
country | Țara căreia îi aparține această zonă maritimă. | CountryCode |
name | Numele zonei maritime. | GeographicalName | voidable
beginLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifepanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «MaritimeZone»
Rol de asociere | Definiție | Tip | Voidability
baseline | Linia sau liniile de bază utilizate pentru delimitarea acestei zone maritime. | Baseline | voidable
boundary | Frontiera sau frontierele acestei zone maritime. | MaritimeBoundary | voidable
4.3.2. Tipuri de date
4.3.2.1. Segment al liniei de bază (BaselineSegment)
Segment al liniei de bază de la care se măsoară limitele exterioare ale mării teritoriale și anumite alte limite exterioare.
Atribute ale tipului de date «BaselineSegment»
Atribut | Definiție | Tip | Voidability
geometry | Reprezentare geometrică a segmentului liniei de bază. | GM_Curve |
segmentType | Tipul de linie de bază utilizat pentru acest segment. | BaselineSegmentTypeValue |
4.3.3. Liste de coduri
4.3.3.1. Tip al segmentului liniei de bază (BaselineSegmentTypeValue)
Tipurile de linii de bază utilizate pentru a măsura lățimea mării teritoriale.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valorile pentru lista de coduri «BaselineSegmentTypeValue»
Valoare | Nume | Definiție
normal | normal | Linia de bază normală pentru măsurarea lățimii mării teritoriale este linia refluxului de-a lungul coastei, astfel cum este indicată pe hărțile nautice detaliate recunoscute oficial de statul riveran.
straight | drept | Linia de bază pentru măsurarea lățimii mării teritoriale este linia de bază dreaptă obținută prin unirea punctelor adecvate.
archipelagic | arhipelagic | Linia de bază pentru măsurarea lățimii mării teritoriale este linia de bază dreaptă care unește punctele extreme ale insulelor cele mai îndepărtate și ale recifelor descoperite ale arhipelagului.
4.3.3.2. Tip de zonă maritimă (MaritimeZoneTypeValue)
Tipul de zonă maritimă.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valorile pentru lista de coduri «MaritimeZoneTypeValue»
Valoare | Nume | Definiție
internalWaters | Ape interioare | Apele situate între țărm și liniile de bază ale mării teritoriale a statului riveran.
territorialSea | Mare teritorială | O centură de mare cu o lățime definită de maximum 12 mile marine măsurate de la liniile de bază stabilite în conformitate cu Convenția Națiunilor Unite asupra dreptului mării.
contiguousZone | Zonă contiguă | O zonă contiguă unei mări teritoriale aparținând unui stat riveran, care nu poate să depășească 24 de mile marine de la liniile de bază de la care se măsoară lățimea mării teritoriale.
exclusiveEconomicZone | Zonă economică exclusivă | O zonă situată dincolo de marea teritorială a unui stat riveran și adiacentă acesteia, supusă regimului juridic specific în temeiul căruia drepturile și jurisdicția statului riveran și drepturile și libertățile altor state sunt reglementate de dispozițiile relevante ale Convenției Națiunilor Unite asupra dreptului mării.
continentalShelf | Platoul continental | O zonă maritimă situată dincolo de marea teritorială a unui stat riveran și adiacentă acesteia, a cărei frontieră exterioară este stabilită în conformitate cu articolul 76 din Convenția Națiunilor Unite asupra dreptului mării.
4.4. Cerințe specifice categoriei
| 1. | Fiecare instanță a unui tip de obiect spațial «AdministrativeUnit», cu excepția unității la nivel național reprezentând un stat membru și unitățile coadministrate, face referire cu precizie la o anumită unitate plasată la un nivel superior al ierarhiei administrative. Această corespondență se exprimă prin rolul de asociere «upperLevelUnit» al tipului de obiect spațial «AdministrativeUnit».
| 2. | Fiecare apariție a unui tip de obiect spațial «AdministrativeUnit», cu excepția celor situate la nivelul cel mai scăzut, face referire la unitățile lor de nivel inferior corespondente. Această corespondență se exprimă prin rolul de asociere «lowerLevelUnit» a tipului de obiect spațial «AdministrativeUnit».
| 3. | Dacă o unitate administrativă este coadministrată de două sau mai multe alte unități administrative, se utilizează rolul de asociere «administeredBy». Unitățile care coadministrează unitatea respectivă trebuie să aplice rolul invers «coAdminister».
| 4. | Unitățile administrative situate la același nivel în ierarhia administrativă nu trebuie să partajeze conceptual zone comune.
| 5. | Aparițiile tipului de obiect spațial «AdministrativeBoundary» corespund limitelor din structura topologică a diagramei complete a limitei (care include toate nivelurile).
| 6. | Este posibil ca extinderea spațială a unui condominiu să nu facă parte din geometria reprezentând extinderea spațială a unei unități administrative.
| 7. | Condominiile pot fi administrate numai de unități administrative la nivel național.
4.5. Straturi
Straturi pentru categoria de date spațiale «Administrative Units»
Numele stratului | Titlul stratului | Tip de obiect spațial
AU.AdministrativeUnit | Unitate administrativă | AdministrativeUnit
AU.AdministrativeBoundary | Limită administrativă | AdministrativeBoundary
AU.Condominium | Condominium | Condominium
AU.Baseline | Linie de bază | Baseline
AU.<CodeListValue>(1) Exemplu: AU.ContiguousZone | <nume lizibil de către om> Exemplu: Zonă contiguă | MaritimeZone (zoneType: MaritimeZoneTypeValue)
AU.MaritimeBoundary | Frontieră maritimă | MaritimeBoundary
(7) Secțiunea 8 se modifică după cum urmează:
(a) În secțiunea 8.2, liniuța „Notificare hidrografică” se elimină.
(b) În secțiunea 8.5.1, următoarele liniuțe se elimină:
— Centrală hidroelectrică
— Teren inundat
— Regiune oceanică
— Conductă
— Stație de pompare
(c) În secțiunea 8.5.1.4, teza „Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale «Zone de risc natural» din anexa III la Directiva 2007/2/CE.” se elimină.
(d) Secțiunea 8.5.1.9 „Centrală hidroelectrică (HydroPowerPlant)”, secțiunea 8.5.1.10 „Teren inundat (InundatedLand)”, secțiunea 8.5.1.14 „Regiune oceanică (OceanRegion)”, secțiunea 8.5.1.15 „Conductă (Pipe)”, secțiunea 8.5.1.16 „Stație de pompare (PumpingStation)”, secțiunea 8.5.4.3 „Inundație (InundationValue)” și secțiunea 8.6 „Notificare hidrografică” se elimină.
(e) Secțiunea 8.5.1.19 se modifică după cum urmează:
— Teza „Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale «Acoperire terestră» din anexa II la Directiva 2007/2/CE” se elimină.
— Rândul pentru atributul „geometrie” din tabelul cu atribute se înlocuiește cu următorul rând:
geometry | Geometria țărmului. | GM_MultiSurface |
(f) În secțiunea 8.5.1.24, după „Constrângeri ale tipului de obiect spațial „Watercourse” se adaugă următoarea constrângere:
„Țărmurile de pe fiecare parte a unui curs de apă trebuie furnizate (utilizându-se propietatea «bank») ca două obiecte «Shore» distincte.”
(g) În secțiunea 8.5.1.25, teza „Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale «Acoperire terestră» din anexa II la Directiva 2007/2/CE.” se elimină.
(h) În secțiunea 8.5.4.4, teza „Acest tip reprezintă un tip candidat care trebuie avut în vedere în cadrul categoriei de date spațiale «Acoperire terestră» din anexa II la Directiva 2007/2/CE.” se elimină.
(i) În secțiunea 8.8, tabelul se înlocuiește cu următorul tabel:
„Tipul stratului | Titlul stratului | Tipul (tipurile) de obiect spațial
HY.Network | Rețea hidrografică | HydroNode, WatercourseLink
HY.PhysicalWaters.Waterbodies | Corpuri de apă | Watercourse, StandingWater
HY.PhysicalWaters.LandWaterBoundary | Limitele uscat-apă | LandWaterBoundary
HY.PhysicalWaters.Catchments | Captări | DrainageBasin, RiverBasin
HY.PhysicalWaters.HydroPointOfInterest | Puncte de interes hidrografic | Rapids, Falls
HY.PhysicalWaters.ManMadeObject | Obiecte artificiale | Crossing, DamOrWeir, Embankment, Lock, Ford, ShorelineConstruction, Sluice
HY. PhysicalWaters.Wetland | Zone umede | Wetland
HY. PhysicalWaters.Shore | Țărmuri | Shore”
(1) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).”
ANEXA III
La Regulamentul (UE) nr. 1089/2010, se adaugă următoarea anexă III:
„ANEXA III
Cerințe privind categoriile de date spațiale enumerate în anexa II la Directiva 2007/2/CE
1. ELEVATION
1.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «model digital de elevație» (DEM) (digital elevation model - DEM) înseamnă «model digital de suprafață (DSM)» (DSM - Digital Surface Model) sau «model digital de teren (DTM)» (DTM - Digital Terrain Model).
(2) «model digital de suprafață» (DSM) (Digital Surface Model – DSM) înseamnă o suprafață care descrie forma tridimensională a suprafeței terestre, inclusiv toate caracteristicile statice așezate pe ea. Fenomenele temporare nu fac parte din suprafață, dar din cauza dificultăților tehnice de eliminare a acestora, unele dintre aceste caracteristici pot fi, de asemenea, prezente pe suprafață.
(3) «model digital de teren» (DTM) (Digital Terrain Model - DTM) înseamnă o suprafață care descrie forma tridimensională a suprafeței terestre necultivate, cu excepția, în măsura posibilului, a oricăror alte caracteristici ale acesteia
(4) «elevație» (elevation) înseamnă o proprietate dimensională, cu constrângere de verticalitate, a unui obiect spațial, constând dintr-o măsură absolută raportată la o suprafață bine definită care este considerată ca origine.
(5) «înălțime» (height) înseamnă o proprietate a elevației măsurată de-a lungul unei linii de plumb într-o direcție opusă câmpului gravitațional al Pământului (ascendentă).
(6) «adâncime» (depth) înseamnă o proprietate a elevației măsurată de-a lungul unei linii de plumb într-o direcție care coincide cu câmpul gravitațional al Pământului (descendentă).
1.2. Structura categoriei de date spațiale «Elevație»
Tipurile specificate pentru categoria de date spațiale «Elevație» sunt organizate în următoarele pachete:
— Elevație – Tipuri de bază (Elevation – Base Types)
— Elevație – Acoperire în caroiaj (Elevation – Grid Coverage)
— Elevație – Elemente vectoriale (Elevation – Vector Elements)
— Elevație – Rețea triunghiulară neregulată (Elevation – TIN)
Seturile de date spațiale care descriu morfologia elevației terenului trebuie puse la dispoziție cel puțin prin utilizarea tipurilor de obiecte spațiale incluse în pachetul «Elevation – Grid Coverage».
Seturile de date spațiale care descriu morfologia batimetriei trebuie puse la dispoziție cel puțin prin utilizarea tipurilor de obiecte spațiale incluse fie în pachetul «Elevation – Grid Coverage», fie în pachetul «Elevation – Vector Elements».
1.3. Elevație – Tipuri de bază
1.3.1. Enumerări
1.3.1.1. Tip de proprietate a elevației (ElevationPropertyTypeValue)
Tip de enumerare care determină proprietatea elevației care a fost măsurată sau calculată.
Valorile pentru enumerarea «ElevationPropertyTypeValue»
Valoare | Definiție
height | Proprietate a elevației măsurată de-a lungul unei linii de plumb în direcția opusă câmpului gravitațional al Pământului (ascendentă).
depth | Proprietate a elevației măsurată de-a lungul unei linii de plumb în direcția care coincide cu câmpul gravitațional al Pământului (descendentă).
1.3.1.2. Tip de suprafață (SurfaceTypeValue)
Tip de enumerare care determină suprafața elevației în raport cu aderența sa relativă la suprafața terestră necultivată.
Valori pentru enumerarea «SurfaceTypeValue»
Valoare | Definiție
DTM | Model digital de teren.
DSM | Model digital de suprafață.
1.4. Elevație – Acoperire în caroiaj
1.4.1. Tipuri de obiecte spațiale
Pachetul «Elevație – Acoperire în caroiaj» conține tipul de obiect spațial «Elevație – Acoperire în caroiaj».
1.4.1.1. Acoperire în caroiaj a elevației (ElevationGridCoverage)
Acoperirea continuă care, pentru a-și acoperi domeniul, utilizează o structură în mozaic sistematică bazată pe un caroiaj rectificat regulat cu patru laturi, și în care valoarea proprietății elevației este, de obicei, cunoscută pentru fiecare dintre punctele caroiajului care alcătuiesc domeniul respectiv.
Acest tip este un subtip al «RectifiedGridCoverage».
Atribute ale tipului de obiect spațial «ElevationGridCoverage»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
domainExtent | Extinderea domeniului spațio-temporal al acoperirii. | EX_Extent |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
propertyType | Atribut care determină proprietatea elevației reprezentată de acoperirea în caroiaj a elevației. | ElevationPropertyTypeValue |
surfaceType | Atribut care indică tipul de suprafață a elevației pe care îl descrie acoperirea în raport cu suprafața terestră necultivată. | SurfaceTypeValue |
Roluri de asociere ale tipului de obiect spațial «ElevationGridCoverage»
Rol de asociere | Definiție | Tip | Voidability
contributingElevationGridCoverage | Trimitere la acoperirile în caroiaj ale elevației, care alcătuiesc o acoperire agregată în caroiaj a elevației. Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «ElevationGridCoverageAggregation». | ElevationGridCoverage |
Constrângeri ale tipului de obiect spațial «ElevationGridCoverage»
Dimensiunea caroiajului trebuie să fie întotdeauna 2 pentru o acoperire în caroiaj a elevației.
«domainExtent» trebuie să fie cel puțin populat cu un subtip al «EX_GeographicExtent».
Trebuie să se furnizeze sistemul de referință de coordonate utilizat pentru a referenția caroiajul.
Toate instanțele «ElevationGridCoverage», la care se referă o instanță agregată a «ElevationGridCoverage», împărtășesc aceeași orientare a axelor caroiajului și aceeași spațiere a caroiajului în fiecare direcție.
Originea caroiajului trebuie descrisă în mod bidimensional.
Valorile intervalului trebuie descrise de tipul «Float».
1.4.2. Tipuri de date
1.4.2.1. Agregare a acoperirii în caroiaj a elevației (ElevationGridCoverageAggregation)
Caracteristicile geometrice ale agregării acoperirii în caroiaj a elevației.
Acest tip este o clasă de asociere.
Atribute ale tipului de date «ElevationGridCoverageAggregation»
Atribut | Definiție | Tip | Voidability
contributingFootprint | Reprezentare geometrică care delimitează zona geografică a acoperirii în caroiaj a elevației ce contribuie la acoperirea agregată în caroiaj a elevației. | GM_MultiSurface |
1.5. Elevație – Elemente vectoriale
1.5.1. Tipuri de obiecte spațiale
Pachetul «Elevație – Elemente vectoriale» conține următoarele tipuri de obiecte spațiale:
— Obiect vectorial de elevație
— Punct cotat
— Curbă de nivel
— Linie de discontinuitate
— Zonă goală
— Zonă izolată
1.5.1.1. Obiect vectorial de elevație (ElevationVectorObject)
Obiect spațial al elevației aparținând unui set de date vectoriale, care participă la descrierea proprietății elevației unei suprafețe din lumea reală. El constă dintr-o bază de identitate pentru toate obiectele vectoriale care pot fi incluse în setul de date de elevație.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «ElevationVectorObject»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
localDepthDatum | Identificarea unui sistem de referință de coordonate vertical local neinclus într-un registru, care se utilizează pentru a referenția măsurătorile de adâncime. | ChartDatum |
propertyType | Atribut care caracterizează obiectul vectorial de elevație ca o elevație a terenului sau ca un obiect spațial de batimetrie. Determină proprietatea elevației reprezentată de obiect. | ElevationPropertyTypeValue |
1.5.1.2. Punct cotat (SpotElevation)
Obiect spațial punctual care descrie elevația unei suprafețe terestre într-o locație specifică. Aceasta furnizează o singură valoare a proprietății elevației.
Acest tip este un subtip al «ElevationVectorObject».
Atribute ale tipului de obiect spațial «SpotElevation»
Atribut | Definiție | Tip | Voidability
classification | Clasă de punct cotat în conformitate cu specificația LAS a Societății americane pentru fotogrametrie și teledetecție (ASPRS). | SpotElevationClassValue | voidable
geographicalName | O denumire geografică utilizată pentru a identifica locația în lumea reală a fundului unui corp de apă desemnat printr-un nume, care este reprezentat de obiectul spațial de tip punct cotat. | GeographicalName | voidable
geometry | Reprezintă proprietățile geometrice ale obiectului spațial. | GM_Point |
propertyValue | Valoarea proprietății elevației obiectului spațial referențiată la un sistem de referință de coordonate vertical specific. | DirectPosition |
spotElevationType | Tipul punctului de elevație. | SpotElevationTypeValue | voidable
Constrângeri ale tipului de obiect spațial «SpotElevation»
Dimensiunea coordonatei valorii de proprietate este 1.
Valoarea de proprietate se exprimă cu referire la un sistem de referință de coordonate vertical.
1.5.1.3. Curbă de nivel (ContourLine)
Obiect spațial liniar compus dintr-un set de locații învecinate caracterizate prin prezența aceleiași valori a proprietății elevației. Acesta descrie, împreună cu alte curbe de nivel prezente în zonă, morfologia locală a suprafeței terestre.
Acest tip este un subtip al «ElevationVectorObject».
Atribute ale tipului de obiect spațial «ContourLine»
Atribut | Definiție | Tip | Voidability
contourLineType | Tipul curbei de nivel pentru un interval vertical standard (după caz). | ContourLineTypeValue | voidable
downRight | Proprietate care indică faptul că obiectul spațial curbă de nivel este digitalizat astfel încât înălțimea suprafeței de elevație să fie mai mică în partea dreaptă a curbei. | Boolean | voidable
geometry | Reprezintă proprietățile geometrice ale obiectului spațial. | GM_Curve |
propertyValue | Valoarea proprietății elevației obiectului spațial referențiată la un sistem de referință de coordonate vertical specific. | DirectPosition |
Constrângeri ale tipului de obiect spațial «ContourLine»
Dimensiunea coordonatei valorii de proprietate este 1.
Valoarea de proprietate se exprimă cu referire la un sistem de referință de coordonate vertical.
1.5.1.4. Linie de discontinuitate (BreakLine)
O linie cu caracteristici critice care descrie forma unei suprafețe de elevație și indică o discontinuitate a înclinării suprafeței (adică o modificare bruscă a pantei). Triunghiurile incluse în modelul TIN nu trebuie să o intersecteze.
Acest tip este un subtip al «ElevationVectorObject».
Atribute ale tipului de obiect spațial «BreakLine»
Atribut | Definiție | Tip | Voidability
breakLineType | Tipul de linie de discontinuitate din punctul de vedere al caracteristicii naturale sau artificiale pe care o reprezintă sau funcția specifică pe care o are în calcularea unui model digital de elevație (DEM). | BreakLineTypeValue |
geometry | Reprezintă proprietățile geometrice ale obiectului spațial. | GM_Curve |
manMadeBreak | Linie care reprezintă o discontinuitate de elevație cauzată de o construcție artificială prezentă pe terenul respectiv. | Boolean | voidable
1.5.1.5. Zonă goală (VoidArea)
Zonă a suprafeței terestre unde modelul de elevație este necunoscut din cauza lipsei datelor de intrare. Această zonă trebuie exclusă dintr-un DEM.
Acest tip este un subtip al «ElevationVectorObject».
Atribute ale tipului de obiect spațial «VoidArea»
Atribut | Definiție | Tip | Voidability
geometry | Reprezintă proprietățile geometrice ale obiectului spațial. | GM_Surface |
1.5.1.6. Zonă izolată (IsolatedArea)
Delimitarea unei zone a suprafeței terestre unde se regăsește o parte izolată a modelului de elevație. Împrejurimile sale exterioare nu sunt vizate de informații cu privire la elevație.
Acest tip este un subtip al «ElevationVectorObject».
Atribute ale tipului de obiect spațial «IsolatedArea»
Atribut | Definiție | Tip | Voidability
geometry | Reprezintă proprietățile geometrice ale obiectului spațial. | GM_Surface |
1.5.2. Tipuri de date
1.5.2.1. Nivel zero hidrografic (ChartDatum)
Sistem de referință de coordonate vertical local, care este utilizat pentru a referenția măsurătorile de adâncime și pentru a le descrie ca valori de proprietate.
Atribute ale tipului de date «ChartDatum»
Atribut | Definiție | Tip | Voidability
datumWaterLevel | Nivel al apei prin care se stabilește originea măsurătorilor de adâncime pentru nivelul zero hidrografic. | WaterLevelValue |
offset | Diferența relativă dintre înălțimea fiecărui punct de referință și înălțimea nivelului apei cu ajutorul căruia se determină nivelul zero hidrografic. | Measure |
referencePoint | Poziția (pozițiile) geografică (e) a (ale): - Cazul A: unui punct unic care se utilizează pentru a referenția valorile adâncimii din aria geografică a nivelului zero hidrografic. - Cazul B: unui set de puncte în care au loc măsurători ale nivelului apei pentru a determina nivelul apei aferent nivelului zero hidrografic. | GM_Point |
scope | Aria geografică în care datumul local de adâncime este practic utilizat. | EX_Extent |
1.5.3. Enumerări
1.5.3.1. Tip de curbă de nivel (ContourLineTypeValue)
Lista posibilelor categorii de curbe de nivel pe baza parametrului de echidistanță al setului de date.
Valorile pentru enumerarea «ContourLineTypeValue»
Valoare | Definiție
master | Curbă de nivel aflată la o distanță pe verticală care este un multiplu al parametrului de echidistanță (corespunzătoare unui anumit multiplu al echidistanței pe verticală a curbelor de nivel normale) asociată scalei nominale.
ordinary | Curbă de nivel la parametrul de echidistanță (corespunzător echidistanței pe verticală a curbelor de nivel normale) asociată scalei nominale și care nu este o curbă de nivel master.
auxiliary | O curbă de nivel suplimentară – care nu corespunde echidistanței verticale a curbelor de nivel normale – estimată sau interpolată pornind de la curbele de nivel înconjurătoare, utilizată în zone în care informațiile privind înălțimea destinate cartografierii elevației sunt insuficiente sau pentru a controla crearea modelului digital de elevație.
1.5.4. Liste de coduri
1.5.4.1. Tipul liniei de discontinuitate (BreakLineTypeValue)
Lista posibilelor valori de tip pentru liniile de discontinuitate, alcătuită pe baza caracteristicilor fizice ale liniei de discontinuitate [în suprafața elevației].
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Valori pentru lista de coduri «BreakLineTypeValue»
Valoare | Nume | Definiție
bottomOfSlope | baza pantei | Linie de discontinuitate care reprezintă limita inferioară a unei arii caracterizate de o pantă constantă a suprafeței de teren, care variază de regulă aproximativ între 2° și 40°.
changeInSlope | modificare a pantei | Linie de discontinuitate reprezentând un set de puncte adiacente, unde terenul înregistrează o modificare bruscă a pantei.
flatAreaBoundary | limită a zonei plate | Linia de discontinuitate care delimitează o parte izolată a teritoriului în care modelul de elevație trebuie constrâns la aceeași valoare a elevației.
formLine | form line | Linie de discontinuitate reprezentând o direcție locală în care suprafața elevației care face obiectul descrierii prezintă cea mai mare pantă.
topOfSlope | vârful pantei | Linie de discontinuitate reprezentând limita superioară a unei arii caracterizate de o pantă constantă a suprafeței de teren, care variază de regulă aproximativ între 2° și 40°.
1.5.4.2. Clasificarea punctului cotat (SpotElevationClassValue)
Valori posibile ale clasificării punctelor cotate determinate pe baza specificației LAS a Societății americane pentru fotogrametrie și teledetecție (ASPRS).
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile privind elevația specificate în Ghidul tehnic INSPIRE.
1.5.4.3. Tipul punctului cotat (SpotElevationTypeValue)
Valorile posibile pentru punctele cotate care descriu o particularitate a suprafeței.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Valorile pentru lista de coduri «SpotElevationTypeValue»
Valoare | Nume | Definiție
depression | depresiune | Punct care reprezintă o parte a reliefului terestru sau a suprafeței fundului unui corp de apă, situat la un nivel mai jos al elevației comparativ cu punctele înconjurătoare.
formSpot | form spot | Un punct cotat suplimentar, estimat sau interpolat pe baza înălțimilor înconjurătoare, în zone unde există puține informații referitoare la curbele de nivel sau alte tipuri de informații.
generic | generic | Obiect spațial de tip punct cotat care nu se potrivește descrierii niciunei alte valori din actuala listă de coduri.
pass | trecătoare | Punct al unei depresiuni situat la un nivel inferior în cadrul unei alinieri de vârfuri, deschisă de regulă de-a lungul liniei de creastă, care permite trecerea de pe o pantă a suprafeței pe alta.
summit | vârf | Cel mai înalt punct al unei proeminențe înregistrate în relieful unei suprafețe terestre sau al unei suprafețe a fundului unui corp de apă.
1.6. Elevație - TIN
1.6.1. Tipuri de obiecte spațiale
Pachetul «Elevație - TIN» conține tipul de obiect spațial «Elevație - TIN».
1.6.1.1. Elevație TIN (ElevationTIN)
Colecție de obiecte spațiale de elevație care formează o anumită structură în mozaic a spațiului bazată pe Triangulated Irregular Network (TIN – rețea triunghiulară neregulată) în conformitate cu geometria GM_Tin definită în ISO 19107: 2003. Componentele sale sunt reprezentate de un set de puncte de control ale căror valori de proprietate a elevației sunt cunoscute, precum și de un set de linii de discontinuitate și de linii de oprire.
Atribute ale tipului de obiect spațial «ElevationTIN»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometries | Reprezintă colecția de proprietăți geometrice ale obiectului spațial al elevației TIN. | GM_Tin |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
propertyType | Atribut care determină proprietatea elevației reprezentată de elevația TIN. | ElevationPropertyTypeValue |
surfaceType | Atribut care indică tipul de suprafață a elevației pe care îl descrie elevația TIN în raport cu suprafața terestră necultivată. | SurfaceTypeValue |
1.7. Cerințe specifice categoriei
1.7.1. Cerințe privind identificatorii de obiect extern
| (1) | Dacă datele privind elevația sunt actualizate pe baza unor noi date sursă, obiectele actualizate primesc un nou identificator de obiect extern.
1.7.2. Cerințe privind «Acoperirile în caroiaj ale elevației»
| (1) | Prin derogare de la cerința prevăzută în secțiunea 2.2 din anexa II, orice sistem de referință compatibil cu unul dintre următoarele sisteme de referință de coordonate poate fi utilizat pentru punerea la dispoziție a datelor altimetrice de tip caroiaj: — coordonate geodezice bidimensionale (latitudine și longitudine) bazate pe datumul specificat în secțiunea 1.2 din anexa II și care utilizează parametrii elipsoidului GRS80; — coordonate planimetrice definite de sistemul de referință și de coordonate ETRS89 Conic Conform Lambert; — coordonate planimetrice definite de sistemul de referință și de coordonate ETRS89 Transversal Mercator. Caroiajul specificat în secțiunea 2.2.1 din anexa II nu se utilizează.
| (2) | Atributul domainExtent al fiecărei instanțe ElevationGridCoverage trebuie să fie cel puțin populat cu un subtip al tipului the EX_GeographicExtent.
| (3) | Valorile de proprietate ale elevației incluse în intervalul unui singur «ElevationGridCoverage» trebuie referențiate la un singur sistem de referință de coordonate vertical și numai unul.
| (4) | Toate instanțele «ElevationGridCoverage», la care se referă o instanță «ElevationGridCoverage» agregată trebuie să fie compatibile. Acest lucru înseamnă că instanțele respective au același tip de interval, același sistem de referință de coordonate și aceeași rezoluție. Ele contribuie, de asemenea, la alinierea caroiajelor, adică punctele de caroiaj dintr-o instanță «ElevationGridCoverage» se aliniază cu punctele de caroiaj ale celorlalte instanțe «ElevationGridCoverage», astfel încât celulele caroiajului să nu se suprapună parțial.
| (5) | Amprentele contributorii ale oricăror două instanțe «ElevationGridCoverage» referențiate de aceeași instanță «ElevationGridCoverage» agregată sunt fie adiacente, fie disjuncte.
| (6) | Prin unirea amprentelor contributorii ale instanțelor «ElevationGridCoverage» referențiate de aceeași instanță «ElevationGridCoverage» agregată, se determină extinderea geografică (domainExtent) a instanței «ElevationGridCoverage» agregate.
| (7) | Pachetul «ElevationGridCoverage» este limitat la geometrii bidimensionale.
| (8) | Informații referitoare la momentele de achiziție a datelor din acoperirile în caroiaj ale elevației trebuie furnizate în cel puțin una dintre următoarele modalități: (a) prin furnizarea elementului de metadate «Temporal reference» pentru fiecare obiect spațial prin atributul de metadate al tipului de obiect spațial ElevationGridCoverage; (b) prin furnizarea elementului de metadate «Temporal reference» necesar conform Regulamentului (CE) nr. 1205/2008 ca extindere temporală.
1.7.3. Cerințe privind datele vectoriale de elevație
| (1) | În cazul în care sunt furnizate seturi de date vectoriale de elevație utilizându-se geometriile 2-D, componenta verticală (a treia dimensiune) trebuie furnizată ca valori ale proprietății de elevație în cadrul atributului «propertyValue».
| (2) | În cazul în care sunt furnizate seturi de date vectoriale de elevație utilizându-se geometriile 2.5-D, valorile proprietății de elevație trebuie incluse doar în cea de a treia coordonată (Z) a acestor geometrii.
1.7.4. Cerințe pentru rețelele triunghiulare neregulate de elevație
| (1) | Valorile de proprietate incluse într-o singură instanță a tipului de obiect spațial «ElevationTIN» (modelul TIN) trebuie referențiate la un singur sistem de referință de coordonate vertical și numai unul.
| (2) | Triunghiurile care intersectează o linie de oprire trebuie îndepărtate de pe o suprafață TIN, lăsând găuri în suprafață. În cazul în care, pe triunghiurile de la limitele suprafețelor, apar cazuri de coincidență, rezultatul trebuie să fie o modificare a limitelor suprafețelor.
| (3) | Obiectele spațiale vectoriale furnizate drept componente ale unei colecții TIN trebuie să îndeplinească normele generice în materie de consecvență prevăzute pentru obiectele vectoriale.
1.7.5. Cerințe privind sistemele de referință
| (1) | Pentru măsurarea adâncimii fundului mării în cazul în care există o amplitudine semnificativă a mareelor (ape de maree), se utilizează ca suprafață de referință cea mai mică maree astronomică (LAT).
| (2) | Pentru măsurarea adâncimii fundului mării în zonele marine în care există o amplitudine semnificativă a mareelor, în largul oceanelor și în ape cu o adâncime mai mare de 200 de metri, adâncimea fundului mării este referențiată la nivelul mediu al mării (MSL) sau la un nivel de referință bine definit apropiat de MSL.
| (3) | Înălțimea nivelului de referință la care se măsoară adâncimea fundului unui corp de apă interioară este referențiată la un sistem de referință vertical legat de gravitație. Este vorba de Sistemul de referință vertical european (EVRS) (EVRS - European Vertical Reference System) pentru zonele situate în aria geografică a EVRS sau de sistemul de referință vertical legat de gravitație identificat de statul membru în afara domeniului de aplicare al EVRS.
| (4) | Atunci când se furnizează un model integrat de elevație terestru-maritim, trebuie modelată doar o singură proprietate de elevație (înălțime sau adâncime), iar valorile sale trebuie referențiate la un singur sistem de referință de coordonate vertical.
1.7.6. Cerințe privind calitatea și coerența datelor
| (1) | În cazul în care, pentru a evalua un set de date de elevație, s-au utilizat alte măsuri decât măsurile ISO privind calitatea datelor, elementul de metadate «Filiație» trebuie să includă informații referitoare la aceste măsuri și, dacă este posibil, o trimitere la o resursă online unde sunt disponibile informații suplimentare.
| (2) | Obiectele spațiale conectate de tip curbă de nivel trebuie să aibă aceeași valoare a elevației atunci când sunt referențiate la același sistem de referință de coordonate vertical.
| (3) | Atunci când valorile elevației obiectelor spațiale de tip linie de discontinuitate sunt furnizate sub forma unor coordonate terțe (Z), punctul de intersecție dintre două obiecte spațiale de tip linie de discontinuitate trebuie să aibă aceeași valoare a elevației.
| (4) | Atunci când un obiect spațial de tip curbă de nivel și un obiect spațial de tip linie de discontinuitate reprezentate în cadrul aceluiași sistem de referință de coordonate vertical se intersectează, punctul de intersectare trebuie să aibă aceeași valoare a elevației [dacă valorile de elevație ale obiectelor spațiale de tip linie de discontinuitate sunt date de coordonata terță (Z)].
| (5) | Obiectele spațiale de tip curbă de nivel care au valori diferite ale elevației nu trebuie nici să se intersecteze, nici să se atingă atunci când sunt referențiate la același sistem de referință de coordonate vertical.
| (6) | Limita unui obiect spațial de tip zonă izolată nu trebuie să atingă limita externă a unui obiect spațial de tip zonă goală atunci când acestea sunt referențiate la același sistem de referință de coordonate vertical.
1.8. Straturi
Straturi pentru categoria de date spațiale «Elevație»
Numele stratului | Titlul stratului | Tip de obiect spațial
EL.BreakLine | Linie de discontinuitate | BreakLine
EL.ContourLine | Curbă de nivel | ContourLine
EL.IsolatedArea | Zonă izolată | IsolatedArea
EL.SpotElevation | Punct cotat | SpotElevation
EL.VoidArea | Zonă goală | VoidArea
EL.ElevationGridCoverage | Acoperire în caroiaj a elevației | ElevationGridCoverage
EL.ElevationTIN | Elevație TIN | ElevationTIN
2. ACOPERIREA TERENULUI (LAND COVER)
2.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «sistem de clasificare» (classification system) înseamnă un sistem pentru împărțirea obiectelor în clase, în conformitate cu ISO 19144-1:2012;
(2) «acoperire discretă» (discrete coverage) înseamnă o acoperire care returnează aceleași valori de atribut ale elementului pentru fiecare poziție directă în cadrul oricărui obiect spațial, temporal sau spațiotemporal unic din domeniul său, în conformitate cu EN ISO 19123:2007;
(3) «obiect al acoperirii terenului» (land cover object) înseamnă un obiect spațial (punct, pixel sau poligon) unde s-a observat acoperirea terenului;
(4) «legendă» (legend) înseamnă aplicarea unei clasificări într-o anumită zonă, utilizând o scară de cartografiere definită și un set specific de date;
(5) «unitate minimă de cartografiere» (minimal mapping unit) înseamnă cea mai mică suprafață a unui poligon care poate fi reprezentată într-un anumit set de date privind acoperirea terenului;
(6) «situație» (situation) înseamnă starea unui anumit obiect al acoperirii terenului la un moment dat.
2.2. Structura categoriei de date spațiale «Acoperirea terenului»
Tipurile indicate pentru categoria de date spațiale «Acoperirea terenului» sunt organizate în următoarele pachete:
— Nomenclatorul de acoperire a terenului (Land Cover Nomenclature)
— Vectorul de acoperire a terenului (Land Cover Vector)
— Raster de acoperire a terenului (Land Cover Raster)
2.3. Nomenclatorul de acoperire a terenului (Land Cover Nomenclature)
2.3.1. Tipuri de date
2.3.1.1. Nomenclatorul de acoperire a terenului (LandCoverNomenclature)
Informații privind nomenclatorul național, instituțional sau local de acoperire a terenului.
Atribute ale tipului de date «LandCoverNomenclature»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
responsibleParty | Parte responsabilă cu dezvoltarea și/sau menținerea nomenclatorului. | RelatedParty |
externalDescription | Document care descrie nomenclatorul utilizat în acest set de date. | DocumentCitation | voidable
embeddedDescription | O codificare integrată a sistemului de clasificare în conformitate cu ISO 19144-2. | LC_LandCoverClassificationSystem | voidable
nomenclatureCodeList | Un http URI care să indice lista de coduri aferentă nomenclatorului utilizat. | URI |
Constrângerile tipului de date «LandCoverNomenclature»
Trebuie să se furnizeze descrierea integrată sau descrierea externă.
2.3.2. Liste de coduri
2.3.2.1. Clasa de acoperire a terenului (LandCoverClassValue)
Lista de coduri sau clasificarea acoperirii terenului.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile și codurile întregi (a se utiliza pentru a reprezenta clase specifice de acoperire a terenului în intervalul de obiecte «LandCoverGridCoverage») menționate pentru lista de coduri «Componenta pură de acoperire a terenului» (PureLandCoverComponentValue) din Ghidul tehnic INSPIRE privind acoperirea terenului.
2.4. Vectorul de acoperire a terenului (Land Cover Vector)
2.4.1. Tipuri de obiecte spațiale
Pachetul «Vector de acoperire a terenului» conține următoarele tipuri de obiecte spațiale:
— Setul de date privind acoperirea terenului
— Unitatea de acoperire a terenului
2.4.1.1. Set de date privind acoperirea terenului (LandCoverDataset)
O reprezentare vectorială pentru datele privind acoperirea terenului.
Atribute ale tipului de obiect spațial «LandCoverDataset»
Atribut | Definiție | Tip | Voidability
name | Numele setului de date privind acoperirea terenului. | CharacterString |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
extent | Conține extinderea setului de date. | EX_Extent |
nomenclatureDocumentation | Informații referitoare la nomenclatorul utilizat în acest set de date. | LandCoverNomenclature |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care fenomenul a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care fenomenul nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «LandCoverDataset»
Rol de asociere | Definiție | Tip | Voidability
member | O unitate de acoperire a terenului care face parte din setul de date. | LandCoverUnit |
2.4.1.2. Unitate de acoperire a terenului (LandCoverUnit)
Un element individual al setului de date de acoperire a terenului reprezentat de un punct sau de o suprafață.
Atribute ale tipului de obiect spațial «LandCoverUnit»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
geometry | Reprezentare spațială a datelor de acoperire a terenului. | GM_Object |
landCoverObservation | Informații privind acoperirea terenului la un moment și într-un loc anume. | LandCoverObservation |
Constrângeri ale tipului de obiect spațial «LandCoverUnit»
Geometriile sunt reprezentate de puncte sau suprafețe.
2.4.2. Tipuri de date
2.4.2.1. Observarea acoperirii terenului (LandCoverObservation)
Informații privind acoperirea terenului interpretate la un moment și într-un loc anume.
Atribute ale tipului de date «LandCoverObservation»
Atribut | Definiție | Tip | Voidability
class | Alocarea unei clase de acoperire a terenului unei unități de acoperire a terenului cu ajutorul unui identificator de cod al clasificării. | LandCoverClassValue |
observationDate | Data de observare asociată unei observări. | DateTime | voidable
mosaic | Lista valorilor de clasificare care descriu în detaliu o unitate de acoperire a terenului, asociată cu procentaje. | LandCoverValue | voidable
Constrângeri ale tipului de obiect spațial «LandCoverObservation»
Suma tuturor atributelor «coveredPercentage» (procentaj acoperit) aferentă fiecărui «LandCoverObservation» trebuie să fie mai mică sau egală cu 100.
2.4.2.2. Acoperirea terenului (LandCoverValue)
Clasă generică de sprijin a valorii și procentajului acoperirii terenului.
Atribute ale tipului de date «LandCoverValue»
Atribut | Definiție | Tip | Voidability
class | Încadrarea unui obiect spațial de tip acoperire a terenului într-o clasă de acoperire a terenului prin intermediul unui identificator de cod al clasificării. | LandCoverClassValue |
coveredPercentage | Fragment al «LandCoverUnit» căruia i se aplică valoarea clasificării. | Integer | voidable
2.5. Raster de acoperire a terenului
2.5.1. Tipuri de obiecte spațiale
Pachetul «Raster de acoperire a terenului» conține tipul de obiect spațial «LandCoverGridCoverage».
2.5.1.1. Acoperire de tip caroiaj de acoperire a terenului (LandCoverGridCoverage)
O reprezentare raster a datelor de acoperire a terenului.
Acest tip este un subtip al «RectifiedGridCoverage».
Atribute ale tipului de obiect spațial «LandCoverGridCoverage»
Atribut | Definiție | Tip | Voidability
name | Denumirea acoperirii terenului. | CharacterString |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
extent | Conține extinderea setului de date. | EX_Extent |
nomenclatureDocumentation | Informații referitoare la nomenclatorul utilizat în această acoperire. | LandCoverNomenclature |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care fenomenul a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care fenomenul nu mai există în realitate. | DateTime | voidable
Constrângeri ale tipului de obiect spațial «LandCoverGridCoverage»
Valorile din interval trebuie să fie de tip Integer.
2.6. Cerințe specifice categoriei
Dacă pentru un tip de date «LandCoverNomenclature» se furnizează un atribut «onlineDescription», descrierea online referențiată trebuie să definească, pentru fiecare clasă, cel puțin un cod, un nume, o definiție și o valoare RGB ce urmează să fie utilizată pentru ilustrare. În cazul în care descrierea online prezintă nomenclatorul pentru un obiect «LandCoverGridCoverage», este de asemenea necesar ca pentru fiecare clasă să se furnizeze și un cod de caroiaj cu valoare de număr de tip Integer. Acest cod trebuie utilizat în intervalul «LandCoverGridCoverage» pentru a reprezenta clasa corespondentă.
2.7. Straturi
Straturi pentru categoria de date spațiale «Land Cover»
Numele stratului | Titlul stratului | Tip de obiect spațial
LC.LandCoverPoints | Puncte de acoperire a terenului | LandCoverUnit
LC.LandCoverSurfaces | Suprafețe de acoperire a terenului | LandCoverUnit
LC.LandCoverRaster | Raster de acoperire a terenului | LandCoverGridCoverage
3. ORTOIMAGINI
3.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «mozaic» (mosaic) înseamnă o imagine alcătuită din mai multe fotografii învecinate sau care se suprapun sau din imagini fuzionate.
(2) «agregare de ortoimagini» (orthoimage aggregation) înseamnă o combinație de subseturi aparținând mai multor acoperiri de ortoimagini omogene care formează o nouă acoperire cu ortoimagini.
(3) «raster» (raster) înseamnă un șablon, de regulă dreptunghiular, alcătuit din linii de scanare paralele care formează un afișaj pe un tub cu raze catodice sau care corespunde unui astfel de afișaj, în conformitate cu EN ISO 19123:2007.
3.2. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt indicate pentru categoria de date spațiale «Ortoimagini»:
— Acoperire de ortoimagini (Orthoimage Coverage)
— Element de mozaic (Mosaic Element)
— Element unic de mozaic (Single Mosaic Element)
— Element agregat de mozaic (Aggregated Mosaic Element)
3.2.1. Acoperire de ortoimagini (OrthoimageCoverage)
Imagine raster a suprafeței Pământului, care a fost corectată din punct de vedere geometric («ortorectificată») pentru a elimina distorsiunile cauzate de diferențele de elevație, înclinarea senzorului și, în mod opțional, de caracteristicile optice ale senzorului.
Acest tip este un subtip al «RectifiedGridCoverage».
Atribute ale tipului de obiect spațial «OrthoimageCoverage»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
domainExtent | Extinderea domeniului spațio-temporal al acoperirii. | EX_Extent |
footprint | Zonă geografică care conține date valide ale acoperirii de ortoimagini. | GM_MultiSurface | voidable
interpolationType | Metodă matematică care trebuie utilizată pentru a evalua o acoperire continuă, și anume pentru a determina valorile acoperirii în orice poziție directă din cadrul domeniului acoperirii. | InterpolationMethodValue |
name | Numele exprimat ca text liber al acoperirii de ortoimagini. | CharacterString | voidable
phenomenonTime | Descrierea duratei în timp a observării/achiziției imaginii (imaginilor) de intrare. | TM_Period | voidable
beginLifespanVersion | Poziție temporală la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | TM_Position | voidable
endLifespanVersion | Poziție temporală la care versiunea obiectului spațial a fost înlocuită sau restrasă din cadrul setului de date spațiale. | TM_Position | voidable
Roluri de asociere ale tipului de obiect spațial «OrthoimageCoverage»
Rol de asociere | Definiție | Tip | Voidability
contributingOrthoimageCoverage | Trimitere la acoperirile cu ortoimagini care alcătuiesc o acoperire agregată de ortoimagini. Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «OrthoimageAggregation». | OrthoimageCoverage |
mosaicElement | Reprezentare spațială a timpului de achiziție a unei acoperiri de ortoimagini provenind dintr-un mozaic. | MosaicElement | voidable
Constrângeri ale tipului de obiect spațial «OrthoimageCoverage»
Momentul de achiziționare a unei acoperiri de ortoimagini trebuie furnizat prin intermediul atributului «phenomenonTime» și a asocierii «mosaicElement».
Dimensiunea caroiajului care trebuie utilizată este întotdeauna 2.
Atributul «domainExtent» trebuie să fie cel puțin populat cu un subtip al «EX_GeographicExtent».
Trebuie să se furnizeze sistemul de referință de coordonate utilizat pentru a referenția caroiajul.
Toate instanțele «OrthoimageCoverage» la care se referă o instanță agregată a «OrthoimageCoverage» au aceeași orientare a axelor caroiajului și aceeași spațiere a caroiajului în fiecare direcție.
Originea caroiajului trebuie descrisă în mod bidimensional.
Valorile din interval trebuie descrise de tipul «Integer».
3.2.2. Element de mozaic (MosaicElement)
Tip abstract care identifică atât zona contributorie, cât și momentul achiziționării uneia sau mai multor imagini de intrare utilizate pentru a genera o acoperire de ortoimagini provenind dintr-un mozaic.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «MosaicElement»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Reprezentare geometrică care delimitează data și ora achiziționării imaginilor de intrare care contribuie la mozaicul final. | GM_MultiSurface |
phenomenonTime | Descrierea duratei în timp a observării/achiziției imaginii (imaginilor) de intrare. | TM_Period |
3.2.3. Element unic de mozaic (SingleMosaicElement)
Element de mozaic aferent unei singure imagini de intrare.
Acest tip este un subtip al «MosaicElement».
Atribute ale tipului de obiect spațial «SingleMosaicElement»
Atribut | Definiție | Tip | Voidability
imageSourceReference | Trimitere la imaginea de intrare. | CharacterString | voidable
3.2.4. Element agregat de mozaic (AggregatedMosaicElement)
Element de mozaic aferent mai multor imagini de intrare care au același moment de achiziționare la un nivel dat definit (de exemplu ziua, luna).
Acest tip este un subtip al «MosaicElement».
3.3. Tipuri de date
3.3.1. Agregare de ortoimagini (OrthoimageAggregation)
Caracteristicile geometrice ale agregării de ortoimagini.
Acest tip este o clasă de asociere.
Atribute ale tipului de date «OrthoimageAggregation»
Atribut | Definiție | Tip | Voidability
contributingFootprint | Reprezentare geometrică care delimitează zona geografică a unei acoperiri de ortoimagini care contribuie la acoperirea agregată de ortoimagini. | GM_MultiSurface |
3.4. Liste de coduri
3.4.1. Metoda interpolării (InterpolationMethodValue)
Listă de coduri care identifică metodele de interpolare care pot fi folosite pentru evaluarea acoperirilor de ortoimagini.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valorile pentru lista de coduri «InterpolationTypeValue»
Valoare | Nume | Definiție
nearestNeighbour | cel mai apropiat vecin | Interpolare prin metoda celui mai apropiat vecin
bilinear | biliniar | Interpolare biliniară
biquadratic | bicuadratic | Interpolare bicuadratică
bicubic | bicubic | Interpolare bicubică
3.5. Cerințe specifice categoriei
3.5.1. Cerințe privind identificatorii de obiect extern
| (1) | Dacă o ortoimagine este actualizată pe baza unei noi date sursă, obiectele actualizate primesc un nou identificator de obiect extern.
3.5.2. Cerințe pentru acoperiri de ortoimagini
| (1) | Prin derogare de la cerința prevăzută în secțiunea 2.2 din anexa II, orice sistem de referință compatibil cu unul dintre următoarele sisteme de referință de coordonate poate fi utilizat pentru punerea la dispoziție a datelor de tip caroiaj privind Ortoimaginile: — coordonate geodezice bidimensionale (latitudine și longitudine) bazate pe datumul specificat în secțiunea 1.2 din anexa II și care utilizează parametrii elipsoidului GRS80; — coordonate planimetrice definite de sistemul de referință și de coordonate ETRS89 Conic Conform Lambert; — coordonate planimetrice definite de sistemul de referință și de coordonate ETRS89 Transversal Mercator. Caroiajul specificat în secțiunea 2.2.1 din anexa II nu se utilizează.
| (2) | Amprenta unei instanțe «OrthoimageCoverage» este inclusă din punct de vedere spațial în sfera sa geografică descrisă prin intermediul proprietății «domainExtent».
| (3) | Tipul de valoare al proprietății de metadate specific tipului de obiect spațial «OrthoimageCoverage» se stabilește la «OM_Observation» atunci când se utilizează modelul de metadate «Observation and Measurement» definit în ISO 19156:2011.
| (4) | Toate instanțele «OrthoimageCoverage», la care se referă o instanță «OrthoimageCoverage» agregată, trebuie să fie coerente. Acest lucru înseamnă că instanțele respective au același tip de interval, același sistem de referință de coordonate și aceeași rezoluție. Ele contribuie, de asemenea, la alinierea caroiajelor, adică punctele de caroiaj dintr-o instanță «OrthoimageCoverage» se aliniază cu punctele de caroiaj ale celorlalte instanțe «OrthoimageCoverage», astfel încât celulele caroiajului să nu se suprapună parțial.
| (5) | Amprenta contributorie a unei instanțe «OrthoimageCoverage» referențiată de o instanță «OrthoimageCoverage» agregată trebuie inclusă din punct de vedere spațial în propria sa amprentă.
| (6) | Amprentele contributorii ale oricăror două instanțe «OrthoimageCoverage» referențiate de aceeași instanță «OrthoimageCoverage» agregată sunt fie adiacente, fie disjuncte.
| (7) | Prin unirea amprentelor contributorii ale instanțelor «OrthoimageCoverage» referențiate de aceeași instanță «OrthoimageCoverage» agregată, se determină amprenta instanței «OrthoimageCoverage» agregate.
3.5.3. Cerințe privind elementele de mozaic
| (1) | Toate elementele de mozaic legate de o instanță «OrthoimageCoverage» trebuie să fie de același tip, și anume, fie «SingleMosaicElement», fie «AggregatedMosaicElement».
| (2) | Geometriile care delimitează oricare două instanțe «MosaicElement» legate de aceeași instanță «OrthoimageCoverage» sunt fie adiacente, fie disjuncte.
| (3) | Unirea geometriilor care delimitează toate instanțele «MosaicElement» legate de aceeași instanță «OrthoimageCoverage» trebuie să includă amprenta acesteia și să fie inclusă în domeniul său geografic.
3.5.4. Cerințe privind sistemele de referință
| (1) | Datele referitoare la categoria de date spațiale «Ortoimagini» sunt limitate la geometriile bidimensionale.
| (2) | Numai sistemele de referință de coordonate bidimensionale sunt utilizate pentru a reprezenta seturile de date INSPIRE privind ortoimaginile.
3.5.5. Cerințe privind calitatea datelor
| (1) | Măsurile «eroarea rădăcinii medie pătrată în X (RMSE-x)» (RMSE-x - root mean square error in X) și «eroarea rădăcinii medie pătrată în Y (RMSE-y)» (RMSE-y - root mean square error in Y) sunt furnizate împreună atunci când sunt utilizate pentru a evalua poziția în caroiaj a datelor de ortoimagine.
3.6. Straturi
Straturi pentru categoria de date spațiale «Orthoimagery»
Numele stratului | Titlul stratului | Tip de obiect spațial
OI.OrthoimageCoverage | acoperire de ortoimagini | OrthoimageCoverage
OI.MosaicElement | element de mozaic | MosaicElement
4. GEOLOGIE (GEOLOGY)
4.1. Structura categoriei de date spațiale «Geologie»
Tipurile specificate pentru categoria de date spațiale «Geologie» sunt organizate în următoarele pachete:
— Geologie (Geology)
— Geofizică (Geophysics)
— Hidrogeologie (Hydrogeology)
4.2. Geologie
4.2.1. Tipuri de obiecte spațiale
Pachetul «Geologie» conține următoarele tipuri de obiecte spațiale:
— Caracteristică geomorfologică antropogenică
— Gaură de sondă
— Cută
— Colecție geologică
— Eveniment geologic
— Caracteristică geologică
— Structură geologică
— Unitate geologică
— Caracteristică geomorfologică
— Caracteristică cartografiată
— Interval cartografiat
— Caracteristică geomorfologică naturală
— Structură de dislocare prin forfecare
4.2.1.1. Caracteristică geomorfologică antropogenă (AnthropogenicGeomorphologicFeature)
O caracteristică geomorfologică (și anume, configurația terenului) care este rezultatul activității umane.
Acest tip este un subtip al «GeomorphologicFeature».
Atribute ale tipului de obiect spațial «AnthropogenicGeomorphologicFeature»
Atribut | Definiție | Tip | Voidability
anthropogenicGeomorphologicFeatureType | Termeni care descriu tipul de caracteristică geomorfologică. | AnthropogenicGeomorphologicFeatureTypeValue |
4.2.1.2. Gaură de sondă (Borehole)
O gaură de sondă reprezintă termenul general pentru orice puț îngust forat în sol.
Atribute ale tipului de obiect spațial «Borehole»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
boreholeLength | Distanța de-a lungul unei găuri de sondă. | Quantity | voidable
elevation | Înălțimea verticală deasupra datumului gurii de sondă. | DirectPosition | voidable
location | Amplasarea gurii de sondă. | GM_Point |
purpose | Scopul pentru care a fost forată gaura de sondă. | BoreholePurposeValue | voidable
downholeGeometry | Geometria fundului găurii de sondă. | GM_Curve | voidable
Roluri de asociere ale tipului de obiect spațial «Borehole»
Rol de asociere | Definiție | Tip | Voidability
logElement | Instanțe «MappedFeature» în 1D care constau în intervale înregistrate (interpretate) ale unei găuri de sondă. | MappedInterval | voidable
4.2.1.3. Cută (Fold)
Unul sau mai multe straturi, suprafețe sau linii curbate în mod sistematic dintr-un corp de rocă.
Acest tip este un subtip al «GeologicStructure».
Atribute ale tipului de obiect spațial «Fold»
Atribut | Definiție | Tip | Voidability
profileType | Tipul de cută. | FoldProfileTypeValue | voidable
4.2.1.4. Colecție geologică (GeologicCollection)
O colecție de obiecte geologice sau geofizice.
Atribute ale tipului de obiect spațial «GeologicCollection»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Numele colecției. | CharacterString |
collectionType | Tipul colecției. | CollectionTypeValue |
reference | O referință pentru colecție. | DocumentCitation | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «GeologicCollection»
Rol de asociere | Definiție | Tip | Voidability
geophObjectSet | Un membru «GeophObjectSet» al colecției geologice. | GeophObjectSet | voidable
geophObjectMember | Un «GeophObjectMember» al colecției geografice. | GeophObject | voidable
boreholeMember | Un membru «Borehole» al unei colecții geologice. | Borehole | voidable
mapMember | Un membru «MappedFeature» al unei colecții geologice. | MappedFeature | voidable
4.2.1.5. Eveniment geologic (GeologicEvent)
Un eveniment identificabil în care unul sau mai multe procese geologice acționează pentru a modifica entitățile geologice.
Atribute ale tipului de obiect spațial «GeologicEvent»
Atribut | Definiție | Tip | Voidability
name | Numele evenimentului geologic. | CharacterString | voidable
eventEnvironment | Cadrul fizic în care are loc evenimentul geologic. | EventEnvironmentValue | voidable
eventProcess | Procesul sau procesele care au avut loc în timpul evenimentului geologic. | EventProcessValue | voidable
olderNamedAge | Limită de vârstă mai veche a evenimentului geologic. | GeochronologicEraValue | voidable
youngerNamedAge | Limită de vârstă mai recentă a evenimentului geologic. | GeochronologicEraValue | voidable
4.2.1.6. Caracteristică geologică (GeologicFeature)
O caracteristică geologică conceptuală care se presupune că există în mod coerent în lume.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «GeologicFeature»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Numele caracteristicii geologice. | CharacterString | voidable
Roluri de asociere ale tipului de obiect spațial «GeologicFeature»
Rol de asociere | Definiție | Tip | Voidability
themeClass | O clasificare tematică a caracteristicii geologice. | ThematicClass | voidable
geologicHistory | O asociere care pune unul sau mai multe evenimente geologice în relație cu o caracteristică geologică pentru a descrie vârsta sau istoria geologică a acestora. | GeologicEvent | voidable
4.2.1.7. Structură geologică (GeologicStructure)
O configurație de materie terestră bazată pe o lipsă de omogenitate, un model sau o fractură descriptibilă a unui material terestru.
Acest tip este un subtip al «GeologicFeature».
Acest tip este abstract.
4.2.1.8. Unitate geologică (GeologicUnit)
Un volum de rocă cu caracteristici distincte.
Acest tip este un subtip al «GeologicFeature».
Atribute ale tipului de obiect spațial «GeologicUnit»
Atribut | Definiție | Tip | Voidability
geologicUnitType | Tipul de unitate geologică. | GeologicUnitTypeValue |
Roluri de asociere ale tipului de obiect spațial «GeologicUnit»
Rol de asociere | Definiție | Tip | Voidability
composition | Descrie compoziția unității geologice. | CompositionPart | voidable
4.2.1.9. Caracteristică geomorfologică (GeomorphologicFeature)
Un tip de obiect spațial abstract care descrie forma și tipul suprafeței terestre a Pământului (adică o configurație a terenului).
Acest tip este un subtip al «GeologicFeature».
Acest tip este abstract.
4.2.1.10. Caracteristică cartografiată (MappedFeature)
O reprezentare spațială a unei «GeologicFeature».
Atribute ale tipului de obiect spațial «MappedFeature»
Atribut | Definiție | Tip | Voidability
shape | Geometria caracteristicii cartografiate. | GM_Object |
mappingFrame | Suprafața pe care este proiectată caracteristica cartografiată. | MappingFrameValue |
Roluri de asociere ale tipului de obiect spațial «MappedFeature»
Rol de asociere | Definiție | Tip | Voidability
specification | O asociere descriptivă care pune caracteristica cartografiată în relație cu o caracteristică geologică teoretică. | GeologicFeature |
4.2.1.11. Interval cartografiat (MappedInterval)
Un tip special de caracteristică cartografiată care se prezintă sub forma unui interval unidimensional și care utilizează sistemul de referință spațial al găurii de sondă în care se găsește.
Acest tip este un subtip al «MappedFeature».
4.2.1.12. Caracteristică geomorfologică naturală (NaturalGeomorphologicFeature)
O caracteristică geomorfologică (și anume, o configurație a terenului) care a apărut ca urmare a unor procese terestre naturale.
Acest tip este un subtip al «GeomorphologicFeature».
Atribute ale tipului de obiect spațial «NaturalGeomorphologicFeature»
Atribut | Definiție | Tip | Voidability
naturalGeomorphologicFeatureType | Tipul de caracteristică geomorfologică naturală. | NaturalGeomorphologicFeatureTypeValue |
activity | Nivelul de activitate al caracteristicii geomorfologice naturale | GeomorphologicActivityValue | voidable
4.2.1.13. Structură de dislocare prin forfecare (ShearDisplacementStructure)
Structuri de la casante la ductile de-a lungul cărora a avut loc dislocarea.
Acest tip este un subtip al «GeologicStructure».
Atribute ale tipului de obiect spațial «ShearDisplacementStructure»
Atribut | Definiție | Tip | Voidability
faultType | Se referă la un vocabular de termeni care descriu tipul de structură de dislocare prin forfecare. | FaultTypeValue |
4.2.2. Tipuri de date
4.2.2.1. Parte de compoziție (CompositionPart)
Compoziția unei unități geologice din punctul de vedere al elementelor litologice constitutive.
Atribute ale tipului de date «CompositionPart»
Atribut | Definiție | Tip | Voidability
material | Materialul care cuprinde o parte sau totalitatea unității geologice. | LithologyValue |
proportion | Cantitate care precizează fracțiunea din unitatea geologică alcătuită din materialul respectiv. | QuantityRange | voidable
role | Relația dintre partea de compoziție și compoziția unității geologice în ansamblul său. | CompositionPartRoleValue |
4.2.2.2. Clasă tematică (ThematicClass)
Un clasificator tematic generic care să permită reclasificarea caracteristicilor geologice în clase definite de utilizatori în funcție de hărți tematice.
Atribute ale tipului de date «ThematicClass»
Atribut | Definiție | Tip | Voidability
themeClass | Valoarea clasei tematice. | ThematicClassValue |
themeClassification | Clasificarea utilizată | ThematicClassificationValue |
4.2.3. Liste de coduri
4.2.3.1. Tipul caracteristicii geomorfologice antropogene (AnthropogenicGeomorphologicFeatureTypeValue)
Tipuri de caracteristici geomorfologice antropogene.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «AnthropogenicGeomorphologicFeatureTypeValue»
Valoare | Nume | Definiție
artificialCollapsedDepression | depresiune prăbușită artificial | Un bazin format prin prăbușire, de regulă o depresiune închisă, care este rezultatul direct al unei subsidențe a suprafeței asociată unor activități subterane de minerit sau de excavare de tunel.
artificialDrainage | asanare artificială | Rețea construită de om, în principal pentru a reduce sau a controla nivelul local al pânzei freatice.
artificialLevee | dig artificial | Un baraj artificial construit de-a lungul unui curs de apă sau a unui braț marin cu scopul de a proteja terenurile de inundații sau de a canaliza cursul apei.
dredgedChannel | canal dragat | O zonă aproape liniară, cu apă adâncă, formată ca urmare a unei operațiuni de dragare în scopuri navigabile.
dump | haldă | O zonă cu acumulări sau grămezi netede sau neregulate de steril, de soluri sau de deșeuri în general, pe care nu pot crește plantele fără o regenerare majoră.
fill | rambleu | Depozite construite artificial de material solid natural și/sau de deșeuri, utilizate pentru a umple o depresiune, pentru a extinde țărmul către un corp de apă sau pentru construirea de diguri.
impactCraterAnthropogenic | crater de impact (antropogen) | O depresiune în general circulară sau eliptică, formată ca urmare a coliziunii în condiții de hiper-viteză dintre un proiectil sau obuz experimental și materiale pământoase sau de roci.
landfillSite | sit de depozitare a deșeurilor | Sit de depozitare a deșeurilor utilizat pentru depozitarea controlată de deșeuri la suprafață sau în subteran.
levelledLand | teren nivelat | O suprafață de teren, de obicei un câmp, care a fost nivelat sau aplatizat prin mijloace mecanice pentru a facilita desfășurarea practicilor de gestionare, cum ar fi irigarea prin inundare.
openpitMine | exploatare minieră de suprafață | O depresiune relativ extinsă, formată ca urmare a lucrărilor de excavare de material și a redistribuirii straturilor de copertă asociate operațiunilor de extracție minieră de suprafață.
pit | balastieră | O depresiune, șanț sau puț excavat pentru a aduna pietriș, nisip sau alte materiale necesare construirii de drumuri sau altor lucrări de construcție; un tip de groapă de împrumut.
quarry | carieră | Zone de excavare, aflate sub cerul liber, de unde se extrage de obicei piatră.
reclaimedLand | terenuri recuperate | O suprafață de teren formată din pământ de umplere care a fost amplasată și modelată astfel încât să aproximeze contururile naturale și care face parte, de regulă, din eforturile de regenerare a terenurilor ca urmare a operațiunilor de extracție minieră. Sau o suprafață de teren, de regulă submersată în starea sa inițială, care a fost protejată de structuri artificiale și drenată în scopuri agricole sau în alte scopuri.
reservoirLake | lac de acumulare | Un corp de apă interioară cu apă stătătoare permanentă, de obicei apă dulce, care ocupă o depresiune de pe suprafața terestră, închisă printr-un baraj.
spoilBank | depozit de steril | Un dâmb, o movilă sau o altă acumulare artificială de depozite resturi de rocă și depozite de steril scoase din șanțuri, mine sau ca urmare a altor excavări.
subsidenceAreaAnthropogenic | zonă de subsidență (anttropogenă) | O zonă supusă unui proces de subsidență cauzat de activități antropogene, de exemplu, minierit subteran, lucrări de excavare de tuneluri sau exploatarea resurselor de ape subterane.
4.2.3.2. Scopul găurii de sondă (BoreholePurposeValue)
Scopurile pentru care a fost forată o gaură de sondă.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «BoreholePurposeValue»
Valoare | Nume | Definiție | Parent
geologicalSurvey | expertiză geologică | Examinare generală a entităților geologice ale unei zone. |
explorationExploitationRawMaterial | prospectarea și exploatarea materiei prime | Descoperirea și identificarea resurselor minerale, inclusiv evaluarea importanței și a potențialului lor economic. |
explorationExploitationEnergyResources | prospectarea și exploatarea resurselor energetice | Examinarea subterană în ceea ce privește disponibilitatea resurselor energetice fosile și planificarea extracției acestora. |
hydrocarbonProduction | producția de hidrocarburi | Producția de petrol și/sau de gaze. | explorationExploitationRawMaterial
hydrocarbonExploration | explorarea hidrocarburilor | Prospectare desfășurată într-o zonă nouă, cu scopul de a verifica existența unui nou teren petrolifer, a unui nou depozit, a unui zăcământ mai adânc sau mai puțin adânc. | explorationExploitationRawMaterial
hydrocarbonAppraisal | evaluarea hidrocarburilor | Evaluarea caracteristicilor unei acumulări dovedite de hidrocarburi. | explorationExploitationRawMaterial
geothermalEnergy | energie geotermală, schimbătoare de căldură geotermale | Prospectare aferentă utilizării resurselor de energie geotermală și proiectarea de pompe de căldură geotermale. | explorationExploitationRawMaterial
heatStorage | stocare a căldurii | Forarea unui puț care să permită utilizarea suprafeței subterane în scopul stocării de căldură. | geothermalEnergy
mineralExplorationExtraction | prospectare și extracție de minerale | Forarea unui puț în scopul localizării și/sau al extracției de resurse minerale din subteran, de regulă prin injectarea și/sau extracția de fluide ce conțin minerale. | explorationExploitationRawMaterial
explorationExploitationNonmetallicMineralDeposits | prospectare și exploatare de zăcăminte minerale nemetalice | Prospectare în ceea ce privește disponibilitatea și planificarea excavării zăcămintelor minerale nemetalice, în principal pentru construcții, piatră de construcție, ciment, industria ceramică sau industria sticlăriei. | explorationExploitationRawMaterial
disposal | depozitare | Un puț, adesea un puț de petrol sau de gaze epuizat, în care deșeurile lichide pot fi injectate în vederea eliminării lor în siguranță. |
explorationNaturalUndergroundStorage | prospectare a spațiului natural de depozitare subterană | Examinarea capacității zonelor subterane de a stoca diverse materiale. |
waterSupply | alimentare cu apă | Alimentare cu apă în general. |
drinkingWaterSupply | alimentare cu apă potabilă | Construirea de puțuri pentru apa potabilă. | waterSupply
industrialWaterSupply | alimentare cu apă industrială | Construirea de puțuri pentru alimentarea cu apă indsutrială. | waterSupply
aquaculture | aquaculture | Alimentare cu apă în scopul acvaculturii. | waterSupply
irrigation | irigare | Construirea de puțuri în scopul irigării. | waterSupply
emergencyWaterSupply | aimentare cu apă pentru situații de urgență | Construirea de puțuri pentru alimentarea cu apă pentru situații de urgență. | waterSupply
contingencyWaterSupply | alimentare cu apă pentru situații neprevăzute | Rezerve de alimentare cu apă pentru situații de deficit de apă. | waterSupply
geophysicalSurvey | analiză geofizică | Examinarea proprietăților geofizice ale zonelor subterane. |
shotHole | gaură de mină | În cazul analizelor seismice, găurile de mină se încarcă cu explozibil. | geophysicalSurvey
flowingShot | gaură de mină cu revărsare | O gaură de mină cu revărsare este o gaură forată în scopuri seismice, care a penetrat o sursă de apă subterană cu o presiune suficient de mare pentru a provoca «revărsarea» prin gaură. | shotHole
hydrogeologicalSurvey | expertiză hidrogeologică, managementul apei | Examinarea fluxului și proprietăților chimice ale apelor subterane, a transportului de particule, de substanțe dizolvate și de energie, precum și managementul utilizării durabile a resurselor de apă subterană. |
geotechnicalSurvey | expertiză geotehnică, caracterizare a sitului | Investigațiile geotehnice efectuate pentru a obține informații privind proprietățile fizice și mecanice ale solului și rocilor din apropierea unui sit, cu scopul de a proiecta lucrări de terasament și fundații pentru structurile propuse, precum și de a repara daunele aduse terasamentelor și structurilor cauzate de condițiile subterane. |
geochemicalSurvey | expertiză geochimică, analize | Examinarea proprietăților chimice ale formațiunilor de rocă și ale fluidelor din porii rocilor. |
pedologicalSurvey | expertiză pedologică | Investigare menită să caracterizeze tipuri de soluri. |
environmentalMonitoring | monitorizare a mediului | Monitorizarea chimiei apelor subterane și a nivelului apelor subterane. |
pollutionMonitoring | monitorizare poluării | Monitorizarea siturilor cunoscute ca fiind afectate de poluare. | environmentalMonitoring
waterQualityMonitoring | monitorizarea calității apei | Monitorizare având drept scop evaluarea naturii și distribuției poluanților și contaminanților din apele subterane; natura și distribuția componentelor chimice care se găsesc în mod natural; condițiile hidrologice subterane și proprietățile hidraulice ale straturilor în raport cu circulația poluanților și a contaminanților. | environmentalMonitoring
groundwaterLevelMonitoring | monitorizare a nivelului apelor subterane | Instalarea unui nivelmetru pentru înregistrarea modificărilor nivelului apelor subterane. | environmentalMonitoring
dewatering | asecare | Asecarea constă în îndepărtarea apei din materiale solide sau din sol prin separare umedă, centrifugare, filtrare sau prin procedee similare de separare a apei de solide. Evacuarea sau drenarea apei din albia unui râu, de pe un șantier, dintr-un cheson sau dintr-un puț de mină, prin pompare sau evaporare. |
mitigation | atenuare | Reducerea nivelului apelor subterane pentru a le împiedica să intre în contact cu siturile poluate. | asecare
remediation | remediere | Remediere în general. Eliminarea poluării sau a contaminanților din apele subterane, din sol și din alte roci. |
thermalCleaning | barbotaj, curățare termică | Un tip de remediere. Curățarea la fața locului a solului cu ajutorul căldurii, al aburilor. | remediation
recharge | reîncărcare | (a) Puțuri de reîncărcare a acviferelor: Utilizate pentru reîncărcarea acviferelor epuizate prin injectarea de apă provenită dintr-o multitudine de surse, cum ar fi lacuri, pâraie, stații de tratare a apelor uzate gospodărești, alte acvifere etc. (b) Puțuri de împiedicare a pătrunderii apei sărate: Utilizate pentru injectarea de apă în acviferele cu apă proaspătă pentru a preveni pătrunderea apei sărate în acestea. (c) Puțuri de control al subsidenței: Utilizate pentru a injecta fluide într-o zonă fără zăcăminte de petrol sau de gaze, cu scopul de a reduce sau elimina subsidența asociată cu supraexploatarea apei proaspete. |
4.2.3.3. Tipul colecției (CollectionTypeValue)
Tipurile colecțiilor de obiecte geologice și geofizice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «CollectionTypeValue»
Valoare | Nume | Definiție
boreholeCollection | colecția de găuri de sondă | Colecție de găuri de sondă
geologicalModel | model geologic | Colecție de obiecte pentru un model spațial geologic în 3D
geologicalMap | hartă geologică | Colecție de elemente pentru o hartă geologică care descrie unități geologice, caracteristici structurale geomorfologice etc.
geophysicalObjectCollection | colecție de obiecte geofizice | Colecție de obiecte geofizice
4.2.3.4. Rolul părții de compoziție (CompositionPartRoleValue)
Rolurile pe care o parte de compoziție le joacă în cadrul unei unități geologice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «CompositionPartRoleValue»
Valoare | Nume | Definiție | Parent
onlyPart | parte unică | Întreaga unitate descrisă este alcătuită dintr-o parte sau dintr-un constituent unic. |
partOf | arte a | Rolul părții din unitatea geologică nu este cunsocut în amănunt. |
facies | facies | Reprezintă un anumit corp de rocă care constituie o variantă laterală a unei unități litostratigrafice sau o variantă a unei unități litodemice. | partOf
inclusion | incluziune | Constituentul unității geologice se dispune ca mase cu limite în general ascuțite incluse într-o matrice formată din alte materiale. | partOf
lithosome | lithosome | Un tip de corp de rocă care are multiple apariții într-o singură unitate geologică. O masă de rocă cu un caracter uniform, caracterizată de geometrie, compoziție și structură internă. | partOf
stratigraphicPart | parte stratigrafică | O parte a unei unități geologice care ocupă o anumită poziție stratigrafică în cadrul unității geologice. | partOf
unspecifiedPartRole | rol nespecificat al părții | Parte a unei unități geologice cu rol nespecificat. | partOf
4.2.3.5. Condițiile evenimentului (EventEnvironmentValue)
Termeni ce caracterizează mediile geologice în care au loc evenimente geologice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Furnizorii de date pot, de asemenea, să utilizeze valorile mai restrânse specificate pentru această listă de coduri în Ghidul tehnic INSPIRE referitor la Geologie.
Valori pentru lista de coduri «EventEnvironmentValue»
Valoare | Nume | Definiție
earthInteriorSetting | structura interioară a pământului | Condițiile geologice din zona solidă a Pământului.
earthSurfaceSetting | structura suprafeței pământului | Condițiile geologice de pe suprafața solidă a Pământului.
extraTerrestrialSetting | structura extraterestrială | Material care își are originea în afara Pământului sau a atmosferei sale.
tectonicallyDefinedSetting | structură definită tectonic | Structură definită de relațiile cu plăcile tectonice de la suprafața sau din interiorul Pământului.
4.2.3.6. Procesul evenimentului (EventProcessValue)
Termeni care desemnează procesul sau procesele care au avut loc în timpul unui eveniment.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Furnizorii de date pot, de asemenea, să utilizeze valorile mai restrânse specificate pentru această listă de coduri în Ghidul tehnic INSPIRE referitor la Geologie.
Valori pentru lista de coduri «EventProcessValue»
Valoare | Nume | Definiție
bolideImpact | impact cu un bolid | Impactul unui corp extraterestru cu suprafața Pământului.
deepWaterOxygenDepletion | epuizarea oxigenului din apele adânci | Proces de scoatere a oxigenului din zona de profunzime a unui corp de apă.
deformation | deformare | Mișcare a formațiunilor de roci prin dislocare de-a lungul zonelor de falie sau de forfecare sau o modificare a formei unui corp de material terestru.
diageneticProcess | proces diagenetic | Orice proces chimic, fizic sau biologic care afectează un material terestru sedimentar după depunerea inițială sau în timpul sau după litificare, cu excepția dezagregării și a metamorfismului.
extinction | extincție | Proces de dispariție a unei specii sau a unui taxon superior, astfel încât nu mai există nicăieri și în nicio înregistrare fosilă ulterioară.
geomagneticProcess | proces geomagnetic | Proces care duce la modificarea câmpului magnetic al Pământului.
humanActivity | activitate umană | Procese de modificare umană a Pământului pentru a produce caracteristici geologice.
magmaticProcess | proces magmatic | Un proces care implică rocă topită (magmă).
metamorphicProcess | proces metamorfic | Ajustare mineralogică, chimică și structurală a rocilor solide la condițiile fizice și chimice care diferă de condițiile de formare a rocilor în cauză și care se petrece în general la adâncime, sub zonele de suprafață caracterizate de dezagregare și cimentare.
seaLevelChange | modificare a nivelului mării | Proces de modificare a nivelului mediu al mării în raport cu un datum.
sedimentaryProcess | proces sedimentar | Un fenomen care modifică distribuția sau proprietățile fizice ale sedimentelor la suprafața Pământului sau aproape de aceasta.
speciation | speciere | Proces care duce la apariția de noi specii.
tectonicProcess | proces tectonic | Procese asociate cu interacțiunea dintre plăcile rigide care formează scoarța Pământului sau cu deformarea acestora.
weathering | dezagregare | Procesul sau grupul de procese prin care materialele terestre expuse la agenții atmosferici de la suprafața terestră sau din apropierea acesteia suferă modificări în ceea ce privește culoarea, textura, compoziția, fermitatea sau forma, cu transportarea unor cantități mici de material dislocat sau modificat sau chiar fără transportarea de astfel de materiale. Printre aceste procese se numără, de regulă oxidarea, hidratarea și levigarea constituenților solubili.
4.2.3.7. Tip de falie (FaultTypeValue)
Termeni care desemnează tipul de structură de dislocare prin forfecare.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Furnizorii de date pot, de asemenea, să utilizeze valorile mai restrânse specificate pentru această listă de coduri în Ghidul tehnic INSPIRE referitor la Geologie.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «FaultTypeValue»
Valoare | Nume | Definiție | Parent
fault | fault | O suprafață discretă sau o zonă de suprafețe discrete, cu o oarecare grosime, care separă două mase de rocă, și de-a lungul căreia una dintre mase s-a deplasat față de cealaltă. |
extractionFault | falie de extracție | O falie ale cărei două părți s-au apropiat în mod considerabil în direcția perpendiculară pe falie. | fault
highAngleFault | falie cu înclinare mare | Falie care se înclină la cel puțin 45 de grade peste mai mult de jumătate din amploarea sa recunoscută, pentru care alunecarea sau separarea nu este precizată în mod explicit. | fault
lowAngleFault | falie cu înclinare mică | Falie care se înclină mai puțin de 45 de grade pe mai mult de jumătate din amploarea sa recunoscută. | fault
obliqueSlipFault | falie oblică | Falie cu un vector de alunecare care prezintă un raport între deplasarea pe orizontală și deplasarea pe verticală de 10 la 1 și de 1 la 10 în cel puțin o locație de-a lungul urmei cartografiate a faliei. | fault
reverseFault | falie inversă | Falie al cărei vector de alunecare are o componentă de deplasare pe verticală de peste 10 ori mai mare decât componenta de deplasare pe orizontală în cel puțin o locație de-a lungul urmei cartografiate a faliei, iar falia se înclină constant în același sens, blocul din acoperiș (de deasupra planului de falie) deplasându-se ascendent față de blocul din culcuș (de sub planul de falie) pe cel puțin jumătate din urma cartografiată a faliei. | fault
scissorFault | falie de forfecare | Falie a cărei săritură sau pas crește față de un punct ințial, dar în sensuri opuse în cele două direcții de o parte și de alta a punctului inițial pe lungimea faliei (de-a lungul faliei, blocul din acoperiș devine blocul din culcuș). | fault
strikeSlipFault | falie de decroșare | Falie al cărei vector de alunecare are o componentă de deplasare pe orizontală de peste 10 ori mai mare decât componenta de deplasare pe verticală în cel puțin o locație de-a lungul urmei cartografiate a faliei. | fault
4.2.3.8. Tipul de profil al cutei (FoldProfileTypeValue)
Termeni care indică tipul de cută.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «FoldProfileTypeValue»
Valoare | Nume | Definiție
anticline | anticlinal | O cută, a cărei parte convexă este orientată în sus, al cărei miez conține rocile mai vechi din punct de vedere stratigrafic.
antiform | antiformă | Orice cută cu partea convexă în sus sau orice cută concavă cu partea concavă în jos.
syncline | sinclinal | O cută al cărei miez conține rocile cele mai tinere din punct de vedere stratigrafic; ea este, în general, concavă și orientată în sus.
synform | sinformă | Orice cută ale cărei flancuri se închid în partea de jos.
4.2.3.9. Eră geocronologică (GeochronologicEraValue)
Termeni care indică unități de timp geologic recunoscute.
Valorile permise pentru această listă de coduri cuprind valorile indicate în Cohen, K.M., Finney, S. & Gibbard, P.L., International Chronostratigraphic Chart, August 2012, International Commission on Stratigraphy of the International Union of Geological Sciences, 2012, precum și valorile suplimentare la orice nivel definit de furnizorii de date.
Furnizorii de date pot utiliza valorile suplimentare pentru rocile din Precambrian și din Cuaternar indicate în Ghidul tehnic INSPIRE privind geologia.
4.2.3.10. Tipul de unitate geologică (GeologicUnitTypeValue)
Termeni care descriu tipul de unitate geologică.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «GeologicUnitTypeValue»
Valoare | Nume | Definiție | Parent
geologicUnit | unitate geologică | Tip de unitate geologică necunoscută, nespecificată, irelevantă sau un anumit tip neinclus în vocabular. |
allostratigraphicUnit | unitate alostratigrafică | Unitate geologică definită de suprafețe limită. Nu este neapărat stratificată. | geologicUnit
alterationUnit | unitate de alterare | Unitatea geologică definită printr-un proces de alterare. | geologicUnit
biostratigraphicUnit | unitate biostratigrafică | Unitate geologică definită pe baza conținutului fosil. | geologicUnit
chronostratigraphicUnit | unitate cronostratigrafică | Unitate geologică care include toate rocile formate în timpul unui anumit interval de timp geologic | geologicUnit
geophysicalUnit | unitate geofizică | Unitate geologică definită de caracteristicile sale geofizice. | geologicUnit
magnetostratigraphicUnit | unitate magnetostratigrafică | Unitate geologică definită de caracteristici magnetice. | geophysicalUnit
lithogeneticUnit | unitate litogenetică | Unitatea geologică definită de geneză. Geneza se manifestă prin proprietăți materiale, dar materialul nu constituie proprietatea definitorie. | geologicUnit
artificialGround | sol artificial | Unitate geologică definită de geneză care implică o acțiune umană directă de depunere sau modificare a materialului. | lithogeneticUnit
excavationUnit | unitate de excavare | Unitate geologică definită de geneză artificială care implică excavare. | lithogeneticUnit
massMovementUnit | unitate de mișcare a masei | Unitate geologică apărută ca urmare a deplasării descendente a materialelor sub influența gravitației, caracterizată de tipul de mișcare care dă naștere la depuneri, precum și de modul în care diferitele tipuri de mișcare prezente în depunere sunt legate în timp și spațiu. | lithogeneticUnit
lithologicUnit | unitate litologică | Unitate geologică definită de litologie, indiferent de legăturile cu alte unități. | geologicUnit
lithostratigraphicUnit | unitate litostratigrafică | Unitate geologică definită pe baza proprietăților litologice distinctive și observabile sau a combinației de proprietăți litologice și relații stratigrafice. | geologicUnit
lithodemicUnit | unitate litodemică | Unitate litostratigrafică care nu este stratificată | lithostratigraphicUnit
lithotectonicUnit | unitate litotectonică | Unitate geologică definită pe baza caracteristicilor structurale sau de deformare, a relațiilor reciproce, a originii sau a evoluției istorice. Materialul conținut poate fi magmatic, sedimentar sau metamorfic. | geologicUnit
deformationUnit | unitate de deformare | Unitate litotectonică definită de un stil de deformare sau de o structură geologică caracteristică observabilă în afloriment. | lithotectonicUnit
pedostratigraphicUnit | unitate pedostratigrafică | Unitate geologică care reprezintă un singur orizont pedologic dintr-o secvență de straturi (consolidată sau neconsolidată). | geologicUnit
polarityChronostratigraphicUnit | unitate cronostratigrafică influențată de polaritate | Unitate geologică, definită de polaritatea magnetică primară înregistrată odată cu depunerea sau cristalizarea rocii în timpul unui anumit interval de timp geologic. | geologicUnit
4.2.3.11. Activitate geomorfologică (GeomorphologicActivityValue)
Termeni care indică nivelul de activitate al unei caracteristici geomorfologice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «GeomorphologicActivityValue»
Valoare | Nume | Definiție
active | activ | Un proces geomorfologic care este în prezent în desfășurare sau care a fost reactivat de scurt timp în mod convențional.
dormant | stagnant | Un proces geomorfologic care nu a dat semne de activitate de un timp scurt, din punct de vedere convențional, și care ar putea fi reactivat cu ajutorul cauzelor inițiale sau declanșat cu ajutorul unor cauze induse cum ar fi activitățile antropogene.
reactivated | reactivat | Un proces geomorfologic reactivat este un proces geomorfologic activ care a stagnat.
stabilised | stabilizat | Un proces geomorfologic stabilizat este un proces inactiv care a fost protejat de cauzele sale inițiale cu ajutorul unor măsuri corective.
inactive | inactiv | Un proces geomorfologic relict sau fosil.
4.2.3.12. Litologie (LithologyValue)
Termen care descrie litologia.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Furnizorii de date pot, de asemenea, să utilizeze valorile mai restrânse specificate pentru această listă de coduri în Ghidul tehnic INSPIRE referitor la Geologie.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «LithologyValue»
Valoare | Nume | Definiție | Parent
compoundMaterial | material compozit | Un material terestru alcătuit dintr-o agregare de particule de material terestru, cu posibilitatea de a include și alte materiale compozite. |
anthropogenicMaterial | material antropogen | Material cunoscut ca fiind de origine artificială (legată de activitatea umană); informații insuficiente pentru a-l clasifica mai în detaliu. | compoundMaterial
anthropogenicConsolidatedMaterial | material antropogen consolidat | Material consolidat cunoscut ca fiind de origine artificială (legată de activitatea umană). | anthropogenicMaterial
anthropogenicUnconsolidatedMaterial | material antropogen neconsolidat | Material neconsolidat cunoscut ca fiind de origine artificială (legată de activitatea umană). | anthropogenicMaterial
breccia | brecie | Material grosier alcătuit din fragmente de roci colțuroase; fragmentele prezintă de regulă margini ascuțite și colțuri neuzate. | compoundMaterial
compositeGenesisMaterial | material de geneză compozită | Material aflat într-o stare de consolidare nedeterminată, format prin modificarea geologică a materialelor preexistente în cadrul altor procese decât cele magmatice și sedimentare. | compoundMaterial
compositeGenesisRock | rocă de geneză compozită | Rocă formată prin modificarea geologică a rocilor preexistente în cadrul altor procese decât cele magmatice și sedimentare. | compositeGenesisMaterial
faultRelatedMaterial | material format prin faliere | Material format ca urmare a unei falieri casante, alcătuit dintr-o matrice mai mare de 10 %; matricea reprezintă un material cu aspect granular fin produs prin reducere tectonică granulometrică. | compositeGenesisMaterial
impactGeneratedMaterial | material generate de impact | Material care conține caracteristici specifice unui metamorfism șoc, cum ar fi caracteristicile deformării microscopice planare în granule sau în fragmentele conice de rocă fracturată, considerate ca fiind rezultatul impactului bolizilor extratereștri. Printre aceste materiale se numără brecia și rocile topite. | compositeGenesisMaterial
materialFormedInSurficialEnvironment | material format in mediu de suprafață | Material care este rezultatul proceselor de dezagregare ce afectează rocile sau depunerile preexistente, similar rocilor hidrotermice sau metasomatice, însă format în condiții de temperatură și presiune ambientale specifice suprafeței Pământului. | compositeGenesisMaterial
rock | rock | Agregat consolidat format din unul sau mai multe materiale terestre, dintr-un corp de materie minerală nediferențiată sau dintr-un material organic solid. | compoundMaterial
aphanite | afanit | Rocă prea fin granulată pentru a fi clasificată mai în detaliu. | rock
sedimentaryRock | rocă sedimentară | Rocă formată prin acumularea și cimentarea de material detritic solid depus cu ajutorul aerului, apei sau gheții sau ca urmare a altor agenți naturali, cum ar fi precipitarea din soluție, acumularea de material organic sau din procese biogene, inclusiv secreții ale diverselor organisme. | rock
tuffite | tufit | Rocă alcătuită în proporție de peste 50 % din particule de origine piroclastică sau epiclastică nedeterminată și în proporție de sub 75 % din particule de origine clar piroclastică. | rock
sedimentaryMaterial | material sedimentar | Material format prin acumularea de material detritic solid depozitat prin aer, apă sau gheață sau material care s-a acumulat cu ajutorul altor agenți naturali precum precipitarea chimică din soluție sau secreții ale diverselor organisme. | compoundMaterial
carbonateSedimentaryMaterial | material sedimentar carbonat | Material sedimentar în cazul căruia cel puțin 50 % dintre constituenții primari și/sau recristalizați sunt alcătuiți din unul (sau mai mulți) dintre mineralele carbonate: calcit, aragonit și dolomită, în particule de origine intrabazinală. | sedimentaryMaterial
chemicalSedimentaryMaterial | material sedimentar chimic | Material sedimentar care constă, în proporție de cel puțin 50 % din materialul obținut ca urmare a proceselor chimice neorganice din cadrul bazinului depozițional. Acest material include clasele de sedimente silicioase, carbonate, evaporit, bogate în fier și fosfatice. | sedimentaryMaterial
clasticSedimentaryMaterial | material sedimentar detritic | Material sedimentar aflat într-o stare de consolidare nespecificată în care cel puțin 50 % dintre particulele constituente provin din eroziune, dezagregare sau din deplasarea în masă a materialelor terestre preexistente, și care este transportat la locul depozițional de agenți mecanici, cum ar fi apa, vântul, gheața și gravitația. | sedimentaryMaterial
nonClasticSiliceousSedimentaryMaterial | material sedimentar silicios non-detritic | Material sedimentar care constă în proporție de cel puțin 50 % din material mineral silicat, depozitat prin procesele biologice sau chimice direct la suprafața depozițională sau prezent sub formă de particule obținute prin procese chimice sau biologice în bazinul depozițional. | sedimentaryMaterial
organicRichSedimentaryMaterial | material sedimentar bogat în conținut organic | Material sedimentar în care cel puțin 50 % din materialul sedimentar primar este carbon organic. | sedimentaryMaterial
igneousMaterial | material magmatic | Material terestru format ca urmare a proceselor magmatice, de exemplu pătrunderea și răcirea magmei în scoarță, erupții vulcanice. | compoundMaterial
fragmentalIgneousMaterial | material magmatic detritic | Material magmatic aflat într-o stare de consolidare nespecificată, în care peste 75 % din rocă constă din fragmente produse ca urmare a unui proces magmatic de formare de roci. | igneousMaterial
acidicIgneousMaterial | material magmatic acid | Material magmatic cu un conținut de SiO2 în proporție de peste 63 %. | igneousMaterial
basicIgneousMaterial | material magmatic bazic | Material magmatic cu un conținut de SiO2 în proporție 45-52 %. | igneousMaterial
igneousRock | rocă magmatică | Rocă formată ca urmare a unor procese magmatice, de exemplu pătrunderea și răcirea magmei în scoarță sau erupțiile vulcanice. | igneousMaterial
intermediateCompositionIgneousMaterial | material magmatic de compoziție intermediară | Material magmatic cu un conținut de SiO2 în proporție de 52-63 %. | igneousMaterial
unconsolidatedMaterial | material neconsolidat | «CompoundMaterial» alcătuit dintr-o agregare de particule care nu aderă unele la altele în mod suficient de puternic pentru ca agregatul să poată fi considerat un solid în sine. | compoundMaterial
naturalUnconsolidatedMaterial | material neconsolidat natural | Material neconsolidat cunoscut ca fiind de origine naturală, nu umană. | unconsolidatedMaterial
sediment | sediment | Material neconsolidat constând dintr-o agregare de particule transportate sau depozitate cu ajutorul aerului, al apei sau al gheții, sau care s-a acumulat cu ajutorul altor agenți naturali, precum precipitarea chimică, și care se formează în straturi la suprafața Pământului. | naturalUnconsolidatedMaterial
4.2.3.13. Cadru de cartografiere (MappingFrameValue)
Termeni care indică suprafața pe care se proiectează «MappedFeature».
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «MappingFrameValue»
Valoare | Nume | Definiție
baseOfQuaternary | baza cuaternarului | Baza materialului sedimentar în mare parte neconsolidat din perioada cuaternară.
surfaceGeology | geologie de suprafață | Rocă de bază și sedimente superficiale care ar fi vizibile dacă s-ar îndepărta solul de deasupra sau dacă ar fi expuse la suprafața topografică.
topOfBasement | partea superioară a bazei (top of basement) | Suprafață a scoarței terestre aflată sub depunerile sedimentare sau vulcanice sau o unitate de rocă transportată prin mijloace tectonice.
topOfBedrock | partea superioară a rocii de bază (top of bedrock) | Suprafață superioară a rocii de regulă solide, care poate fi fie expusă la suprafața topografică, fie acoperită de alte depuneri neconsolidate.
4.2.3.14. Tipul caracteristicii geomorfologice naturale (NaturalGeomorphologicFeatureTypeValue)
Termeni care descriu tipul de caracteristică geomorfologică naturală.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «NaturalGeomorphologicFeatureTypeValue»
Valoare | Nume | Definiție
naturalGeomorphologicFeature | caracteristică geomorfologică naturală | O caracteristică geomorfologică produsă de dinamica naturală.
drainagePattern | model de drenaj | Configurația sau dispunerea cursurilor de apă dintr-o zonă, inclusiv a rigolelor sau a zonelor de scurgere canalizate de prim ordin, a afluenților de ordin superior și a principalelor cursuri de apă.
constructionalFeature | caracteristică de construcție | Loc al unei forme de teren a cărei origine, formă, poziție sau caracter general se datorează proceselor depoziționale (aluvionare), cum ar fi acumularea de sedimente
destructionalFeature | caracteristică de distrucție | Loc al unei forme de teren a cărei origine, formă, poziție sau caracter general se datorează îndepărtării de material în urma unor procese de erodare și dezagregare (degradare) rezultate din uzura parțială sau completă a suprafeței terestre.
degradationFeature | caracteristică de degradare | O caracteristică geomorfologică care rezultă din uzura parțială sau completă și din coborârea sau reducerea în general a suprafeței Pământului ca urmare a proceselor naturale de dezagregare și eroziune, și care poate implica procese de transport de sedimente.
relic | relict | O formă de teren care a supraviețuit degradării sau dezintegrării sau care a rămas după dispariția celei mai mari părți a substanței sale, cum ar fi un fragment de insulă.
exhumedFeature | caracteristică exhumată | Forme de teren, suprafețe geomorfologice sau paleosoluri care au fost îngropate în trecut și care au fost din nou expuse prin eroziunea învelișului acoperitor.
buriedFeature | caracteristică îngropată | Forme de teren, suprafețe geomorfologice sau paleosoluri acoperite de sedimente mai tinere.
pediment | pediment | O suprafață de eroziune ușor înclinată, situată la poalele unei coline sau ale unui povârniș, de obicei cu un profil ușor concav orientat în sus, care intersectează roca sau straturile de sediment ce se extind până sub platourile adiacente.
erosional | caracteristici de eroziune | O suprafață de teren modelată prin acțiuni erozive, datorate în special apelor curgătoare.
hill | colină | Un termen generic pentru o ridicătură a suprafaței terestre, care se înalță între cel puțin 30 și 300 de metri deasupra zonelor de câmpie înconjurătoare, având de obicei un vârf nominal în raport cu versanții limită, un contur bine definit și rotunjit și versanți cu o declivitate de regulă mai mare de 15 %.
interfluve | interfluviu | O componentă geomorfologică a dealurilor constând din cea mai înaltă, relativ plană sau ușor înclinată parte a unui deal; muchiile zonelor înalte pot îngusta platoul sau pot fuziona, dând astfel naștere la o formă puternic convexă.
crest | creastă | O componentă geomorfologică a dealurilor constând din versanții convecși (perpendiculari pe contur) care formează zona de vârf, aproximativ liniară, a unui deal, lanț de dealuri sau a altor regiuni înalte în care muchiile s-au întâlnit astfel încât nu a mai rămas decât un vârf mic sau vârful a dispărut complet; ea este dominată de eroziune, eroziune de versant și de procese de mișcare în masă și de sedimentare
headSlope | taluz amonte | O componentă geomorfologică a dealurilor constând dintr-o parte concavă lateral a unei coaste de deal, aflată în special la capătul unui canal de drenaj, caracterizată de cursuri de apă de suprafață convergente.
sideSlope | versant lateral | O componentă geomorfologică a dealurilor care constă dintr-o parte plană lateral a unei coaste de deal, caracterizată de cursuri de apă de suprafață predominant paralele. În general, curbele de nivel formează linii drepte.
noseSlope | nose slope | O componentă geomorfologică a dealurilor constând din capătul proeminent (parte convexă lateral) al unei coaste de deal, caracterizată de cursuri de apă de suprafață divergente; în general, curbele de nivel formează curbe convexe.
freeFace | față liberă | O componentă geomorfologică a delurilor și munților care constă dintr-un afloriment de roci golașe din care cad fragmente de rocă și alte sedimente pe versantul coluvial aflat imediat mai jos, și care sunt amplasate în general mai în pantă decât unghiul de repaus al acestuia; cel mai adesea, această componentă geomorfologică se întâlnește în poziții de coastă și în pante și poate include, parțial sau în întregime, un o pantă convexă sau un versant lateral.
baseSlope | fund de pantă (base slope) | O componentă geomorfologică a dealurilor constând dintr-o pantă concavă până la liniară (perpendiculară pe curba de nivel) care, indiferent de forma laterală, reprezintă o porțiune care formează un șorț sau un colț la baza unui versant dominată de procese coluviale și de eroziune de versant și de sedimente.
mountain | munte | Un termen generic pentru o zonă ridicată a suprafeței terestre, care se ridică la peste 300 de metri deasupra zonelor de câmpie înconjurătoare, având de obicei o suprafață nominală a vârfului în raport cu pantele abrupte (o declivitate de peste 25 %) alcătuită dintr-o cantitate considerabilă de roci golașe expuse sau nu.
mountaintop | vârf de munte | O componentă geomorfologică a munților constând din cea mai înaltă, relativ plană sau ușor înclinată, parte a munților, caracterizată de versanți relativ scurți și simpli alcătuiți din roci golașe, reziduuri sau din sedimente coluviale transportate pe distanță scurtă.
mountainslope | versant de munte | O parte a unui munte situată între vârf și poale.
mountainflank | flanc de munte | O componentă geomorfologică a munților caracterizată de pante foarte lungi și complexe cu declivități relativ ridicate și alcătuită din mantale sedimentare coluviale foarte diverse, din aflorimente de roci sau zone terigene structurate (structural benches).
mountainbase | bază a muntelui | O componentă geomorfologică a munților care constă dintr-o fâșie sau dintr-un con coluvial puternic până la ușor concav situat la baza versanților munților.
depression | depresiune | Orice parte relativ scufundată a suprafeței terestre; în special o zonă situată la altitudine joasă, înconjurată de un teren mai ridicat.
plain | câmpie | Orice zonă plană, mică sau mare, de elevație joasă; în speță, o regiune extinsă cu o suprafață relativ netedă și plană sau ușor ondulată, cu puține neregularități, sau deloc, însă caracterizată uneori de o declivitate considerabilă, și aflată de obicei la altitudine joasă în raport cu zonele înconjurătoare.
tectonicStructural | caracteristici structurale și tectonice | Peisaje și forme de teren geomorfologice asociate structurilor de roci de bază locale sau regionale sau mișcării scoarței terestre; precum și peisaje și forme de relief geomorfologice asociate predominant eroziunii hidrice, însă excluzând eroziunea perenă, eroziunea ce afectează cursurile de apă (de exemplu fluvială, fluvio-glaciară) sau eroziunea eoliană.
volcanic | caracteristici vulcanice | Peisaje și forme de relief geomorfologice asociate proceselor de profunzime (magmatice) prin care magma și gazele aferente străbat scoarța și sunt împinse la suprafața terestră și în atmosferă.
hydrothermal | caracteristici hidrotermale | Peisaje și forme de relief geomorfologice asociate proceselor hidrotermale.
erosionSurface | suprafață de eroziune | Peisaje și forme de relief geomorfologice asociate predominant eroziunii hidrice, însă excluzând eroziunea perenă, eroziunea ce afectează cursurile de apă (de exemplu fluvială, fluvio-glaciară) sau eroziunea eoliană.
slopeGravitational | caracteristici ale pantelor și gravitaționale | Peisaje și forme de relief geomorfologice asociate mediilor în pantă; peisaje și forme de relief geomorfologice apărute ca urmare a acțiunii forței gravitaționale.
nivalPeriglacialPermafrost | caracteristici nivale, periglaciare și legate de permafrost | Peisaje și forme de relief geomorfologice asociate zăpezii, mediilor neglaciare și cu climă rece; peisaje și forme de relief geomorfologice care își fac apariția în vecinătatea ghețarilor și calotelor glaciare; peisaje și forme de relief geomorfologice specifice terenurilor, solurilor sau rocilor care sunt expuse, timp de cel puțin doi ani, la temperaturi de cel mult 0° C.
glacial | caracteristici glaciare, fluvio-glaciare, glaciolacustre și glaciomarine | Peisaje și forme de relief geomorfologice specifice mediilor glaciar, fluvio-glaciar, glaciolacustru și gaciomarin.
eolian | caracteristici eoliene | Peisaje și forme de relief geomorfologice specifice mediilor dominate de vânt
marineLittoralCoastalWetland | caracteristici specifice zonelor umede marine, litorale și costiere | Peisaje și forme de relief geomorfologice specifice dinamicii valurilor și mareelor produse în medii din zonele marine, marine de mică adâncime, marine din apropierea țărmului și litorale, precum și cele specifice zonelor umede cu vegetație și/sau de mică adâncime.
karstChemicalWeathering | caracteristici legate de carst și de dezagregare chimică | Peisaje și forme de relief geomorfologice dominate de disoluția mineralelor și, în mod frecvent, de drenajul subteran.
alluvialFluvial | caracteristici aluviale și fluviale | Peisaje și forme de relief geomorfologice specifice cursurilor de apă concentrate (scurgeri în albie).
lacustrine | caracteristici lacustre | Peisaje și forme de relief geomorfologice specifice corpurilor de apă continentale permanente (lacuri).
impact | caracteristici ale impacturilor | Peisaje și forme de relief geomorfologice specifice impactului materialelor extraterestre cu suprafața Pământului.
4.2.3.15. Clasă tematică (ThematicClassValue)
Valori pentru clasificarea tematică a caracteristicilor geologice.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
4.2.3.16. Clasificare tematică (ThematicClassificationValue)
Listă de clasificări tematice ale caracteristicilor geologice.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
4.3. Geofizică (Geophysics)
4.3.1. Tipuri de obiecte spațiale
Pachetul «Geofizică» conține următoarele tipuri de obiecte spațiale:
— Campanie
— Măsurare geofizică
— Obiect geofizic
— Set de obiecte geofizice
— Profil geofizic
— Stație geofizică
— Culoar geofizic
4.3.1.1. Campanie (Campaign)
Activitate geofizică care se extinde pe o perioadă de timp și într-o zonă limitată, vizând realizarea de măsurători geofizice, procesarea rezultatelor sau a modelelor.
Acest tip este un subtip al «GeophObjectSet».
Atribute ale tipului de obiect spațial «Campaign»
Atribut | Definiție | Tip | Voidability
campaignType | Tip de activitate în vederea producerii de date. | CampaignTypeValue |
surveyType | Tip de investigație geofizică. | SurveyTypeValue |
client | Partea pentru care au fost create datele. | RelatedParty | voidable
contractor | Partea care a creat datele. | RelatedParty | voidable
Constrângeri ale tipului de obiect spațial «Campaign»
Atributul «formă» trebuie să fie de tip «GM_Surface».
4.3.1.2. Obiect geofizic (GeophObject)
O clasă generică pentru obiectele geofizice.
Acest tip este un sub-tip al «SF_SpatialSamplingFeature».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «GeophObject»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
citation | Citare din documentația specifică geofizicii. | DocumentCitation |
projectedGeometry | Proiecția în 2D a caracteristicii pe suprafața solului (ca punct, curbă sau poligon de delimitare reprezentativ) care să fie utilizat de un serviciu de vizualizare INSPIRE menit să afișeze localizarea pe o hartă a obiectului spațial. | GM_Object |
verticalExtent | Extinderea verticală a gamei de interese. | EX_VerticalExtent | voidable
distributionInfo | Metadate de distribuție. | MD_Distributor | voidable
largerWork | Identificator al unui set de date de lucru mai mare, de regulă o campanie sau un proiect. | Identifier | voidable
Constrângeri ale tipului de obiect spațial «GeophObject»
Atributul «projectedGeometry» trebuie să fie de tip «GM_Point», «GM_Curve» sau «GM_Surface».
4.3.1.3. Măsurătoare geofizică (GeophMeasurement)
Un tip generic de obiect spațial pentru măsurători geofizice.
Acest tip este un subtip al «GeophObject».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «GeophMeasurement»
Atribut | Definiție | Tip | Voidability
relatedModel | Identificator al modelului geofizic care a fost creat ca urmare a măsurătorii. | Identifier | voidable
platformType | Platformă de pe care s-a efectuat măsurătoarea. | PlatformTypeValue |
relatedNetwork | Numele unei rețele de observare naționale sau internaționale căreia îi aparține facilitatea sau căreia îi sunt raportate datele măsurate. | NetworkNameValue | voidable
4.3.1.4. Set de obiecte geofizice (GeophObjectSet)
O clasă generică pentru colecții de obiecte geofizice.
Acest tip este un sub-tip al «SF_SpatialSamplingFeature».
Atribute ale tipului de obiect spațial «GeophObjectSet»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
citation | Citare din documentația specifică geofizicii. | DocumentCitation |
verticalExtent | Extinderea verticală a gamei de interese. | EX_VerticalExtent | voidable
distributionInfo | Metadate de distribuție. | MD_Distributor | voidable
projectedGeometry | Proiecția în 2D a caracteristicii pe suprafața solului (ca punct, curbă sau poligon de delimitare reprezentativ) care să fie utilizat de un serviciu de vizualizare INSPIRE menit să afișeze obiectul spațial pe o hartă. | GM_Object |
largerWork | Identificator al unui set de date de lucru mai mare. | Identifier | voidable
Constrângeri ale tipului de obiect spațial «GeophObjectSet»
Atributul «projectedGeometry» trebuie să fie de tip «GM_Point», «GM_Curve» sau «GM_Surface».
4.3.1.5. Profil geofizic (GeophProfile)
O măsurare geofizică georeferențiată la o curbă.
Acest tip este un subtip al «GeophMeasurement».
Atribute ale tipului de obiect spațial «GeophProfile»
Atribut | Definiție | Tip | Voidability
profileType | Tipul de profil geofizic. | ProfileTypeValue |
Constrângeri ale tipului de obiect spațial «GeophProfile»
Atributul «formă» trebuie să fie de tip «GM_Curve».
4.3.1.6. Stație geofizică (GeophStation)
Măsurare geofizică georeferențiată la un punct unic.
Acest tip este un subtip al «GeophMeasurement».
Atribute ale tipului de obiect spațial «GeophStation»
Atribut | Definiție | Tip | Voidability
stationType | Tip de stație geofizică. | StationTypeValue |
stationRank | Stații geofizice pot face parte dintr-un sistem ierarhic. Clasificarea este proporțională cu importanța stației. | StationRankValue | voidable
Constrângeri ale tipului de obiect spațial «GeophStation»
Atributul «formă» trebuie să fie de tip «GM_Point».
4.3.1.7. Culoar geofizic (GeophSwath)
O măsurare geofizică georeferențiată la o suprafață.
Acest tip este un subtip al «GeophMeasurement».
Atribute ale tipului de obiect spațial «GeophSwath»
Atribut | Definiție | Tip | Voidability
swathType | Tip de culoar geofizic. | SwathTypeValue |
Constrângeri ale tipului de obiect spațial «GeophSwath»
Atributul «formă» trebuie să fie de tip «GM_Surface».
4.3.2. Liste de coduri
4.3.2.1. Tipul de campanie (CampaignTypeValue)
Un tip de campanie geofizică.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «CampaignTypeValue»
Valoare | Nume | Definiție
measurement | măsurare | Campanie de colectare de date de teren.
4.3.2.2. Numele rețelei (NetworkNameValue)
Numele unei rețele geofizice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «NetworkNameValue»
Valoare | Nume | Definiție
GSN | GSN | Global Seismographic Network
IMS | IMS | IMS Seismological network
INTERMAGNET | INTERMAGNET | International Real-time Magnetic Observatory Network
UEGN | UEGN | Unified European Gravity Network
WDC | WDC | World Data Center
4.3.2.3. Tipul de platformă (PlatformTypeValue)
O platformă pe care s-a efectuat colectarea de date.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «PlatformTypeValue»
Valoare | Nume | Definiție
ground | sol | Măsurătoare efectuată la sol.
landVehicle | vehicul de teren | Măsurătoare efectuată dintr-un vehicul de teren.
fixedWingAirplane | aeronavă cu aripă fixă | Măsurătoare efectuată de la bordul unei aeronave cu aripă fixă.
helicopter | elicopter | Măsurătoare efectuată din elicopter.
seafloor | fund de mare | Măsurare efectuată pe fundul mării.
researchVessel | navă de cercetare | Măsurătoare efectuată de la bordul unei nave.
satellite | satelit | Măsurătoare efectuată din satelit.
4.3.2.4. Tipul de profil (ProfileTypeValue)
Tipul de profil geofizic.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «ProfileTypeValue»
Valoare | Nume | Definiție
boreholeLogging | diagrafia a sondei | Măsurătoare geofizică de-a lungul axei unei găuri de sondă efectuată cu un dispozitiv special de carotaj.
multielectrodeDCProfile | profil continuu multi-electrozi | Măsurare a rezistivității în CC și/sau a capacității de încărcare (efect IP) efectuată de-a lungul unui profil cu un set mai mare de electrozi. Cunoscută și ca tomografia rezistivității în 2D.
seismicLine | linie seismică | Măsurătoare geofizică utilizată la înregistrarea răspunsului acustic al surselor seismice de-a lungul unei linii pentru a defini proprietățile seismice într-o secțiune transversală a Pământului.
4.3.2.5. Rangul stației (StationRankValue)
O clasificare a stației geofizice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «StationRankValue»
Valoare | Nume | Definiție
observatory | observator | Facilitate de monitorizare permanentă cu un program de observare continuă.
secularStation | stație seculară | Stație de bază menită să înregistreze variațiile pe termen lung ale câmpului fizic observat.
1stOrderBase | bază de prim ordin | Stație de bază de cea mai mare precizie administrată de o anumită autoritate. Este utilizată de către observatori ale unei terțe părți pentru a lega măsurătorile relative la rețeaua absolută.
2ndOrderBase | bază de rangul al doilea | Stație de bază de mare precizie de importanță mai mică, administrată de o autoritate. Este utilizată de către observatori ale unei terțe părți pentru a lega măsurătorile relative la rețeaua absolută.
4.3.2.6. Tipul de stație (StationTypeValue)
Un tip de stație geofizică.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valorile pentru lista de coduri «StationTypeValue»
Valoare | Nume | Definiție
gravityStation | stație gravimetrică | Stație geofizică responsabilă cu observarea câmpului gravitațional.
magneticStation | stație magnetică | Stație geofizică responsabilă cu observarea câmpului magnetic.
seismologicalStation | stație seismologică | Stație geofizică responsabilă cu observarea evenimentelor seismologice caracterizate de mișcări puternice (cutremure) sau a zgomotului ambiental.
verticalElectricSounding | sondaj electric vertical | Stație geofizică de măsurare a rezistivității electrice subterane și/sau a modificărilor capacității de încărcare (IP) la adâncime, utilizând un dispozitiv cvadripolar (AMNB) și curent continuu. Cunoscut și sub denumirea de VES.
magnetotelluricSounding | sondaj magnetoteluric | Stație geofizică responsabilă cu măsurarea modificărilor rezistivității electrice subterană, utilizând variațiile naturale ale câmpului electromagnetic. Cunoscut și sub denumirea de sondaj MT.
4.3.2.7. Tipul investigației (SurveyTypeValue)
Un tip de investigație geofizică sau de set de date geofizice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «SurveyTypeValue»
Valoare | Nume | Definiție
airborneGeophysicalSurvey | prospecțiune geofizică aeriană | Campanie de măsurători aeriene geofizice.
groundGravitySurvey | prospecțiunea densității solului | Campanie de măsurători ale densității solului.
groundMagneticSurvey | prospecțiune magnetică a solului | Campanie de măsurători magnetice ale solului.
3DResistivitySurvey | prospecțiune în 3D a rezistivității | Campanie de măsurători multielectrod 3D în curent continuu.
seismologicalSurvey | prospecțiune seismică | Campanie de măsurători seismologice.
4.3.2.8. Tipul de culoar (SwathTypeValue)
Un tip de culoar geofizic.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «SwathTypeValue»
Valoare | Nume | Definiție
3DSeismics | prospecțiune seismică în 3D | Măsurătoare geofizică utilizată pentru înregistrarea răspunsului acustic al surselor seismice într-o zonă, cu scopul de a defini distribuția proprietății seismice în 3D într-un volum de sol.
4.4. Hidrogeologie (Hydrogeology)
4.4.1. Tipuri de obiecte spațiale
Pachetul «Hidrogeologie» conține următoarele tipuri de obiecte spațiale:
— Puț activ
— Acviclud
— Acvifer
— Sistem de acvifere
— Acvitard
— Corp de apă subterană
— Obiect hidrogeologic
— Obiect hidrogeologic artificial
— Obiect hidrogeologic natural
— Unitate hidrogeologică
4.4.1.1. Puț activ (ActiveWell)
Un puț care influențează resursele de apă subterană ale acviferului.
Acest tip este un subtip al «HydrogeologicalObjectManMade».
Atribute ale tipului de obiect spațial «ActiveWell»
Atribut | Definiție | Tip | Voidability
activityType | Tipul de activitate desfășurată de puț. | ActiveWellTypeValue |
Roluri de asociere ale tipului de obiect spațial «ActiveWell»
Rol de asociere | Definiție | Tip | Voidability
groundWaterBody | «GroundWaterBody» din care «ActiveWell» extrage resursele de apă subterană. | GroundWaterBody | voidable
environmentalMonitoringFacility | «EnvironmentalMonitoringFacility» asociată. | EnvironmentalMonitoringFacility | voidable
borehole | Gaura de foraj pe care se bazează «ActiveWell». | Borehole | voidable
4.4.1.2. Acviclud (Aquiclude)
Un corp de rocă impermeabil sau un strat de sedimente, care acționează ca o barieră în calea fluxului de ape subterane.
Acest tip este un subtip al «HydrogeologicalUnit».
4.4.1.3. Acvifer (Aquifer)
Un strat umed subteran de rocă permeabilă cu conținut de apă sau un strat de materiale neconsolidate (pietriș, nisip, aluviuni sau argilă) din care se poate extrage apă subterană cu ajutorul unei sonde de apă.
Acest tip este un subtip al «HydrogeologicalUnit».
Atribute ale tipului de obiect spațial «Aquifer»
Atribut | Definiție | Tip | Voidability
aquiferType | Tipul de acvifer. | AquiferTypeValue |
mediaType | Clasificarea mediului străbătut de fluxul de ape subterane. | AquiferMediaTypeValue |
isExploited | Indică dacă apele subterane din acvifer sunt exploatate de puțuri sau captări. | Boolean | voidable
isMainInSystem | Indică dacă acviferul este principalul acfiver bun din sistemul de acvifere. | Boolean | voidable
vulnerabilityToPollution | O valoare sau un interval al indicelui sau interval care determină gradul potențial de risc pentru acvifer apărut din cauza structurii geologice, a condițiilor hidrogeologice și a existenței unei surse reale sau potențiale de contaminare. | QuantityValue | voidable
permeabilityCoefficient | Volumul unui fluid necomprimabil care va curge într-o unitate de timp printr-o celulă elementară a unei rețele cubice a unei substanțe poroase peste care se menține o diferență de presiune pe unitate. | QuantityValue | voidable
storativityCoefficient | Capacitatea unui acvifer de stocare a apei. | QuantityValue | voidable
hydroGeochemicalRockType | Tipul de rocă din punctul de vedere al compomentelor solubile ale rocii și al infuenței hidrogeochimice exercitate de acestea asupra apelor subterane. | HydroGeochemicalRockTypeValue | voidable
Roluri de asociere ale tipului de obiect spațial «Aquifer»
Rol de asociere | Definiție | Tip | Voidability
aquitard | Acvitardul (acvitardele) care separă acviferele. | Aquitard | voidable
hydrogeologicalObject | «HydrogeologicalObject(s)» asociat(e) acviferului. | HydrogeologicalObject | voidable
aquiferSystem | «AquiferSystem» specific în care apare Acvitardul. | AquiferSystem | voidable
4.4.1.4. Sistem de acvifere (AquiferSystem)
O colecție de acvifere și acvitarde, care constituie împreună mediul apelor subterane - «vase comunicante», care sunt sau pot fi umplute cu apă.
Acest tip este un subtip al «HydrogeologicalUnit».
Atribute ale tipului de obiect spațial «AquiferSystem»
Atribut | Definiție | Tip | Voidability
isLayered | Indică dacă «AquiferSystem» constă din mai mult de un strat. | Boolean | voidable
Roluri de asociere ale tipului de obiect spațial «AquiferSystem»
Rol de asociere | Definiție | Tip | Voidability
aquitard | Acvitardul (acvitardele) care fac parte din «AquiferSystem». | Aquitard | voidable
aquiclude | Un acviclud care include «AquiferSystem». | Aquiclude | voidable
aquifer | Acviferul (acviferele) care fac parte din «AquiferSystem». | Aquifer | voidable
4.4.1.5. Acvitard (Aquitard)
Un strat saturat, dar foarte slab permeabil, care obstrucționează circulația apei subterane.
Acest tip este un subtip al «HydrogeologicalUnit».
Atribute ale tipului de obiect spațial «Aquitard»
Atribut | Definiție | Tip | Voidability
approximatePermeabilityCoefficient | Volumul unui fluid necomprimabil care va curge într-o unitate de timp printr-o celulă elementară a unei rețele cubice a unei substanțe poroase peste care se menține o diferență de presiune pe unitate. | QuantityValue | voidable
approximateStorativityCoefficient | Capacitatea unui acvifer de stocare a apei. | QuantityValue | voidable
Roluri de asociere ale tipului de obiect spațial «Aquitard»
Rol de asociere | Definiție | Tip | Voidability
aquiferSystem | «AquiferSystem» din care face parte «Aquitard». | AquiferSystem | voidable
aquifer | Acviferele separate de acvitard. | Aquifer | voidable
4.4.1.6. Corp de apă subterană (GroundWaterBody)
Un volum distinct de apă subterană din cadrul unui acvifer sau al unui sistem de acvifere, care este izolat hidraulic de corpurile de apă subterană învecinate.
Atribute ale tipului de obiect spațial «GroundWaterBody»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
approximateHorizontalExtend | Geometria care definește limitele «GroundWaterBody». | GM_Surface | voidable
conditionOfGroundWaterBody | Gradul aproximativ de schimbare care afectează apele subterane ca urmare a activității umane. | ConditionOfGroundwaterValue |
mineralization | Una dintre principalele caracteristici chimice ale apei. Valoarea este suma tuturor componentelor de concentrație chimică a apei. | WaterSalinityValue | voidable
piezometricState | Indică starea piezometrică a pânzei freeatice «GroundwaterBody». | PiezometricState | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «GroundWaterBody»
Rol de asociere | Definiție | Tip | Voidability
activeWell | «ActiveWell» care schimbă starea «GroundwaterBody» prin extracția de resurse subterane. | ActiveWell | voidable
aquiferSystem | «AquiferSystem» care include «GroundWaterBody». | AquiferSystem | voidable
hydrogeologicalObjectNatural | Un «HydrogeologicalObjectNatural» care interacționează cu «GroundwaterBody». | HydrogeologicalObjectNatural | voidable
observationWell | Puțurile de observare care monitorizează «GroundWaterBody». | EnvironmentalMonitoringFacility | voidable
4.4.1.7. Obiect hidrogeologic (HydrogeologicalObject)
O clasă abstractă pentru dispozitive artificiale sau caracteristici naturale care interacționează cu sistemul hidrogeologic.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «HydrogeologicalObject»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Geometrie care definește localizarea spațială a «HydrogeologicalObject». | GM_Primitive |
name | Numele sau codul «HydrogeologicalObject». | PT_FreeText | voidable
description | Descrierea «HydrogeologicalObject». | PT_FreeText | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «HydrogeologicalObject»
Rol de asociere | Definiție | Tip | Voidability
aquifer | Acviferul în cadrul căruia apare «HydrogeologicalObject». | Aquifer | voidable
4.4.1.8. Obiect hidrogeologic artificial (HydrogeologicalObjectManMade)
Un obiect hidrogeologic artificial.
Acest tip este un subtip al «HydrogeologicalObject».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «HydrogeologicalObjectManMade»
Atribut | Definiție | Tip | Voidability
validFrom | Data și ora oficiale la care obiectul hidrogeologic a fost/va fi constituit legal. | DateTime | voidable
validTo | Data și ora oficiale la care obiectul hidrogeologic a încetat/ va înceta să fie utilizat. | DateTime | voidable
statusCode | Un cod care definește statutul oficial al unui obiect hidrogeologic artificial. | StatusCodeTypeValue | voidable
4.4.1.9. Obiect hidrogeologic natural (HydrogeologicalObjectNatural)
Obiect hidrogeologic care a fost creat prin procese naturale.
Acest tip este un subtip al «HydrogeologicalObject».
Atribute ale tipului de obiect spațial «HydrogeologicalObjectNatural»
Atribut | Definiție | Tip | Voidability
naturalObjectType | Tipul de obiect hidrogeologic natural. | NaturalObjectTypeValue |
waterPersistence | Gradul de persistență a cursului de apă. | WaterPersistenceValue | voidable
approximateQuantityOfFlow | O valoare aproximativă care definește randamentul de apă aferent unui obiect hidrogeologic natural. | QuantityValue | voidable
Roluri de asociere ale tipului de obiect spațial «HydrogeologicalObjectNatural»
Rol de asociere | Definiție | Tip | Voidability
groundWaterBody | «GroundWateBody» cu care interacționează obiectul hidrogeologic natural. | GroundWaterBody | voidable
4.4.1.10. Unitate hidrogeologică (HydrogeologicalUnit)
O parte a litosferei caracterizată de parametri distinctivi pentru stocarea și conducția apei.
Acest tip este un subtip al «GeologicUnit».
Atribute ale tipului de obiect spațial «HydrogeologicalUnit»
Atribut | Definiție | Tip | Voidability
description | Descrierea «HydrogeologicalObject». | PT_FreeText | voidable
approximateDepth | Adâncimea aproximativă a evenimentului «HydrogeologicalUnit». | QuantityValue | voidable
approximateThickness | Grosimea aproximativă a «HydrogeologicalUnit». | QuantityValue | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «HydrogeologicalUnit»
Rol de asociere | Definiție | Tip | Voidability
geologicStructure | Pune unul sau mai multe «HydrogeologicalUnit(s)» în relație cu o «GeologicStructure». | GeologicStructure | voidable
4.4.2. Tipuri de date
4.4.2.1. Suprafață hidrogeologică (HydrogeologicalSurface)
O suprafață care reprezintă tabelul interpolat referitor la apele subterane sau o altă suprafață, pentru o zonă locală sau regională.
Acest tip este o uniune.
Atribute ale tipului uniune «HydrogeologicalSurface»
Atribut | Definiție | Tip | Voidability
surfaceRectifiedGrid | O suprafață al cărei domeniu este un caroiaj rectificat. | RectifiedGridCoverage |
surfaceReferenceableGrid | Suprafață al cărei domeniu constă dintr-un caroiaj referențiabil. | ReferenceableGridCoverage |
surfacePointCollection | Suprafață hidrogeologică reprezentată de o colecție de observări în puncte. | PointObservationCollection |
4.4.2.2. Stare piezometrică (PiezometricState)
Stare piezometrică a unui «GroundWaterBody»
Atribute ale tipului de date «PiezometricState»
Atribut | Definiție | Tip | Voidability
observationTime | Data și ora de observare a stării apelor subterane. | DateTime |
piezometricSurface | O suprafață care reprezintă nivelul până la care va crește apa în puțuri tubate. | HydrogeologicalSurface |
4.4.2.3. Valoare cantitativă (QuantityValue)
Un container de date cu o singură valoare cantitativă sau o serie de valori cantitative.
Acest tip este o uniune.
Atribute ale tipului de uniune «QuantityValue»
Atribut | Definiție | Tip | Voidability
singleQuantity | Componentă scalară cu reprezentare zecimală și o unitate de măsură utilizată pentru a depozita valoarea unei cantități permanente. | Quantity |
quantityInterval | Pereche de zecimale având scopul de a specifica un interval cantitativ cu ajutorul unei unități de măsură. | QuantityRange |
4.4.3. Liste de coduri
4.4.3.1. Tipul de puț activ (ActiveWellTypeValue)
Tipuri de puțuri active.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valorile pentru lista de coduri «ActiveWellTypeValue»
Valoare | Nume | Definiție
exploitation | exploatare | Extracția de apă subterană dintr-un acvifer pentru a fi utilizată în diverse scopuri (domestic, industrial, alimentarea cu apă și altele).
recharge | reîncărcare | (a) Puțuri de reîncărcare a acviferelor: Utilizate pentru reîncărcarea acviferelor epuizate prin injectarea de apă provenită dintr-o multitudine de surse, cum ar fi lacuri, pâraie, stații de tratare a apelor uzate gospodărești, alte acvifere etc. (b) Puțuri de împiedicare a pătrunderii apei sărate: Utilizate pentru injectarea de apă în acviferele cu apă proaspătă pentru a preveni pătrunderea apei sărate în acestea. (c) Puțuri de control al subsidenței: Utilizate pentru a injecta fluide într-o zonă fără zăcăminte de petrol sau de gaze, cu scopul de a reduce sau elimina subsidența asociată cu supraexploatarea apei proaspete.
dewatering | asecare | Îndepărtarea apei din materiale solide sau din solul unui acvifer, în scopul scăderii nivelului pânzei freatice, de exemplu în timpul fazei de dezvoltare a sitului unui proiect major de construcții, ca urmare a creșterii nivelului pânzei freatice. Implică, de obicei, utilizarea pompelor de «epuizment».
decontamination | decontaminare | Puț utilizat în sistemele de decontaminare care reduc poluarea dintr-un acvifer.
disposal | depozitare | Un puț, adesea un puț de petrol sau de gaze epuizat, în care deșeurile lichide pot fi injectate în vederea eliminării lor. Puțurile pentru depozitarea deșeurilor lichide fac obiectul unor cerințe de reglementare pentru a evita contaminarea acviferelor cu apă dulce.
waterExploratory | explorare a apei | Un puț forat pentru a căuta noi ape subterane.
thermal | energie termică | Un puț utilizat pentru a extrage apa termală necesară diverselor activități termale (de exemplu, balneologia).
observation | observare | Un puț utilizat în scopuri de observare.
4.4.3.2. Tipul mediilor acvifere (AquiferMediaTypeValue)
Valori care descriu caracteristicile mediului acvifer.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «AquiferMediaTypeValue»
Valoare | Nume | Definiție
fractured | fracturat | Acviferele fisurate sunt roci în care apele subterane circulă prin fisuri, articulații sau fracturi în roca de altfel solidă.
porous | poros | Mediile poroase sunt acele acvifere care constau din agregate de particule individuale, cum ar fi nisip sau pietriș, scurgerile de ape subterane apărând și curgând printre spațiile libere dintre granulele individuale.
karstic | carstic | Acviferele carstice sunt acvifere fisurate, în cazul cărora fisurile și fracturile au fost lărgite prin dizolvare, creând canale largi sau chiar caverne.
compound | compozit | O combinație de acvifer poros, carstic și/sau fisurat
karsticAndFractured | carstic și fisurat | O combinație de acvifere carstice și fisurate.
porousAndFractured | poros și fisurat | O combinație de acvifere poroase și fisurate.
4.4.3.3. Tipul de acvifer (AquiferTypeValue)
Tipuri de acvifere.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «AquiferTypeValue»
Valoare | Nume | Definiție
confinedSubArtesian | subartezian delimitat | Un acvifer care conține apă între două limite relativ impermeabile. Nivelul apei al unui puț care captează apă dintr-un acfiver limitat se situează deasupra limitei superioare a acviferului limitat și poate fi mai mare sau mai mic decât pânza freatică care poate fi prezentă în materialul de deasupra. Nivelul apei nu depășește suprafața solului.
confinedArtesian | artezian delimitat | Un acvifer care conține apă între două limite relativ impermeabile. Nivelul apei al unui puț care captează apă dintr-un acfiver limitat se situează deasupra limitei superioare a acviferului limitat și poate fi mai mare sau mai mic decât pânza freatică care poate fi prezentă în materialul de deasupra. Nivelul apei depășește suprafața solului, contribuind la crearea unui puț artezian.
unconfined | nedelimitat | Un acvifer conținând apă care nu este sub presiune. Nivelul apei dintr-un puț este același cu nivelul pânzei freatice din afara puțului.
4.4.3.4. Starea apei subterane (ConditionOfGroundwaterValue)
Valori care indică gradul aproximativ de modificare a stării naturale a apei subterane.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «ConditionOfGroundwaterValue»
Valoare | Nume | Definiție
natural | natural | Cantitatea sau calitatea apei subterane depinde doar de factorii naturali.
lightlyModified | ușor modificat | Cantitatea sau calitatea apei subterane depinde în mare parte de factorii naturali, fiind însă influențate de activitatea umană
modified | modificat | Cantitatea sau calitatea apei subterane este modificată de activitatea umană.
stronglyModified | puternic modificată | Cantitatea sau calitatea apei subterane este modificată de activitatea umană, iar valorile unei serii de parametri depășesc standardele pentru apa potabilă.
unknown | necunoscută | Starea naturală a apei subterane nu este cunoscută.
4.4.3.5. Tipul de rocă hidrogeochimică (HydroGeochemicalRockTypeValue)
Valori care să descrie starea hidrogeochimică a mediului de ape subterane.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «HydroGeochemicalRockTypeValue»
Valoare | Nume | Definiție
silicatic | silicatic | Tip hidrochimic silicatic de ape subterane.
carbonatic | carbonatic | Tip hidrochimic carbonatic de ape subterane.
sulfatic | sulfatic | Tip hidrochimic sulfatic de ape subterane.
chloridic | cloridic | Tip hidrochimic cloridic de ape subterane.
organic | organic | Tip hidrochimic organic de ape subterane.
4.4.3.6. Tipul de obiecte naturale (NaturalObjectTypeValue)
Tipurile de obiecte hidrogeologice naturale.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «NaturalObjectTypeValue»
Valoare | Nume | Definiție
spring | izvor | Orice situație naturală în care fluxurile naturale de ape subterane curg la suprafața pământului. Astfel, un izvor reprezintă un sit unde suprafața acviferului întâlnește suprafața solului.
seep | infiltrație | Un loc umed sau chiar ud în care apele subterane ies la suprafață dintr-un acvifer subteran.
swallowHole | dolină | O depresiune sau cavitate naturală în suprafața terestră, cunoscută și sub denumirile de ponor, pâlnie de eroziune, dolină sau cenotă, este în principal determinată de procese carstice – dizolvarea chimică a rocilor carbonate - sau de procese de inundare, de exemplu a gresiei calcaroase.
fen | turbărie minerotrofă | Teren jos acoperit parțial sau complet cu apă și care este caracterizat de un sol alcalin și turbos și floră specifică (precum rogoz și și trestie).
notSpecified | nespecificat | Locuri nespecificate în care apele subterane se ridică la suprafață.
4.4.3.7. Tipul codului de stare (StatusCodeTypeValue)
Valori care descriu starea obiectelor hidrogeologice artificiale.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «StatusCodeTypeValue»
Valoare | Nume | Definiție
abandonedDry | abandonat, uscat | Abandonat din cauza lipsei de apă.
abandonedInsufficient | abandonate, apă insuficientă | Abandonat din cauza cantității insuficiente de apă.
abandonedQuality | abandonat, slabă calitate a apei | Abandonat din motive de calitate a apei.
deepened | adâncit | Adâncimea de foraj a crescut.
new | nou | Gaura de foraj construită pe un site neutilizat anterior.
notInUse | neutilizat | Nu mai este utilizat în niciun scop.
reconditioned | recondiționat | Un puț care a făcut obiectul unor lucrări de remediere pentru a-i îmbunătăți funcționarea.
standby | standby | Noțiune abstractă utilizată numai în cazul în care celelalte noțiuni nu sunt disponibile.
unfinished | neterminat | Foraj sau construcție care nu a fost finalizată.
unknown | necunoscută | Statut necunoscut sau nedefinit.
4.4.3.8. Persistența apei (WaterPersistenceValue)
Tipuri de persistență hidrologică a apei.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «WaterPersistenceValue»
Valoare | Nume | Definiție
intermittent | intermitent | Plin și/sau care curge într-o anumită parte a anului.
seasonal | sezonier | Plin și/sau care curge în anumite perioade ale anului, de exemplu, toamna/iarna.
perennial | peren | Plin și/sau care curge continuu pe parcursul anului, întrucât patul apei se află sub pânza freatică.
notSpecified | nespecificat | Tipul de persistență hidrologică a apei care nu este specificat.
ephemeral | efemer | Plin și/sau care se scurge în timpul pecipitațiilor sau imediat după acestea.
4.4.3.9. Salinitatea apei (WaterSalinityValue)
O listă de coduri care indică clasele de salinitate a apei.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «WaterSalinityValue»
Valoare | Nume | Definiție
ultraFreshWater | apă foarte dulce | Apă cu salinitate foarte redusă. Salinitatea este echivalentă sau aproape echivalentă cu cea a apei de ploaie.
freshWater | apă dulce | Apă dulce înseamnă corpuri de apă precum iazuri, lacuri, râuri și pâraie care conțin concentrații scăzute de săruri dizolvate.
brackishWater | apă salmastră | Apă salmastră înseamnă apă cu o salinitate mai mare decât cea a apei dulci, dar nu la fel de mare precum cea a apei de mare. Ea poate proveni din amestecul de apă de mare cu apă potabilă, cum este cazul în estuare, sau poate apărea în acvifere fosile salmastre.
salineWater | apă salină | Apă salină înseamnă apă cu o concentrație semnificativă de săruri dizolvate. Apa de mare are o salinitate de aproximativ 35 000 ppm, echivalentul a 35 g/l.
brineWater | saramură | Saramura este saturată sau aproape saturată cu sare.
4.5. Straturi
Straturi pentru categoria de date spațiale «Geologie»
Numele stratului | Titlul stratului | Tip de obiect spațial
GE.GeologicUnit | Unități geologice | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tipul GeologicUnit)
GE. <ValoaredinListadeCoduri>(1) | <nume lizibil de către om> | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tipul GeologicFeature și care sunt clasificate cu ajutorul proprietății themeClass) în conformitate cu aceeași clasificare tematică)
Exemplu: GE.ShrinkingAndSwelling Clays | Exemplu: Argile care se contractă și bentonit | (themeClassification: ThematicClassificationValue)
GE.GeologicFault | Falii geologice | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tip „ShearDisplacementStructure”)
GE.GeologicFold | Cute geologice | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tipul Fold)
GE.GeomorphologicFeature | Caracteristici geomorfologice | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tip GeomorphologicFeature)
GE.Borehole | Găuri de sondă | Borehole
GE.Aquifer | Acvifere | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tip Aquifer)
GE.Aquiclude | Acviclude | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tip Aquiclude)
GE.Aquitard | Acvitarde | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tip Aquitard)
GE.AquiferSystems | Sisteme de acvifere | MappedFeature (obiecte spațiale a căror proprietate de specificare este de tip AquiferSystem)
GE.Groundwaterbody | Corpuri de apă subterană | Groundwaterbody
GE.ActiveWell | Puțuri active | ActiveWell
GE. <ValoaredinListadeCoduri>(2) | <nume lizibil de către om> | GeophStation (stationType: StationTypeValue)
Exemplu: GE.gravityStation | Exemplu: Stații responsabile cu gravitația |
GE. <ValoaredinListadeCoduri>(3) | <nume lizibil de către om> | GeophStation (profilType: ProfileTypeValue)
Exemplu: GE.seismicLine | Exemplu: Linii seismice |
GE. <ValoaredinListadeCoduri>(4) | <nume lizibil de către om> | GeophStation (surveyType: SurveyTypeValue)
Exemplu: GE.groundGravitySurvey | Exemplu: Prospecțiuni ale densității solului |
GE. <ValoaredinListadeCoduri>(5) | <nume lizibil de către om> | Campaign (surveyType: SurveyTypeValue)
Exemplu: GE.groundMagneticSurvey | Exemplu: Prospecțiuni magnetice ale solului |
GE.Geophysics.3DSeismics | Prospecțiune seismică în 3D | GeophSwath
(1) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(2) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(3) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(4) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(5) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).”
ANEXA IV
La Regulamentul (UE) nr. 1089/2010, se adaugă următoarea anexă IV:
„ANEXA IV
Cerințe privind categoriile de date spațiale enumerate în anexa III la Directiva 2007/2/CE
1. UNITĂȚI STATISTICE (STATISTICAL UNITS)
1.1. Structura categoriei de date spațiale «Unități statistice»
Tipurile indicate pentru categoria de date spațiale «Unități statistice» sunt structurate în următoarele pachete:
— Baza unităților statistice
— Vector al unităților statistice
— Caroiaj al unităților statistice
1.2. Baza unităților statistice
1.2.1. Tipuri de obiecte spațiale
Pachetul «Baza unităților statistice» conține tipul de obiect spațial «Unitate statistică».
1.2.1.1. Unitate statistică (StatisticalUnit)
Unitate de diseminare și utilizare a informațiilor statistice.
Acest tip este abstract.
1.3. Vector al unităților statistice
1.3.1. Tipuri de obiecte spațiale
Pachetul «Vector» conține următoarele tipuri de obiecte spațiale:
— Unitate statistică vectorială
— Unitate statistică zonală
— Partiție statistică
— Evoluție
1.3.1.1. Unitate statistică vectorială (VectorStatisticalUnit)
Unitate statistică reprezentată ca geometrie de tip vector (punct, linie sau suprafață).
Acest tip este un subtip al «StatisticalUnit».
Atribute ale tipului de obiect spațial «VectorStatisticalUnit»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
thematicId | Identificator descriptiv de obiect unic aplicat obiectelor spațiale într-o categorie de informații definită. | ThematicIdentifier |
country | Codul țării căreia îi aparține obiectul. | CountryCode |
geographicalName | Denumirile geografice posibile ale obiectului. | GeographicalName |
validityPeriod | Perioada în care se presupune că unitatea statistică ar trebui să fie sau nu utilizată. | TM_Period |
referencePeriod | Perioada în care se presupune că datele ar trebui să prezinte o imagine a împărțirii teritoriale în unități statistice. | TM_Period |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «VectorStatisticalUnit»
Rol de asociere | Definiție | Tip | Voidability
geometry | Reprezentări geometrice ale unității statistice vectoriale. | VectorStatisticalUnitGeometry |
evolutions | Toate evoluțiile prin care a trecut unitatea statistică. | Evolution | voidable
Constrângeri ale tipului de obiect spațial «VectorStatisticalUnit»
Unități statistice vectoriale cu o instanță de geometrie de referință a GM_MultiSurface trebuie să fie instanțe ale clase specializate AreaStatisticalUnit.
1.3.1.2. Unitate statistică zonală (AreaStatisticalUnit)
Unitate statistică de tip vector având o geometrie de referință zonală.
Acest tip este un subtip al «VectorStatisticalUnit».
Atribute ale tipului de obiect spațial «AreaStatisticalUnit»
Atribut | Definiție | Tip | Voidability
areaValue | Suprafața geometriei de referință. | Area |
landAreaValue | Suprafața părții situate deasupra apei. | Area | voidable
livableAreaValue | Suprafața părții locuibile. | Area | voidable
Roluri de asociere ale tipului de obiect spațial «AreaStatisticalUnit»
Rol de asociere | Definiție | Tip | Voidability
administrativeUnit | Unități administrative utilizate pentru a construi unitatea statistică zonală. | AdministrativeUnit | voidable
lowers | Unități statistice zonale ale următorului nivel inferior. | AreaStatisticalUnit | voidable
uppers | Unități statistice zonale ale următorului nivel superior. | AreaStatisticalUnit | voidable
successors | Succesorii unității statistice zonale. | AreaStatisticalUnit | voidable
predecessors | Predecesorii unității statistice zonale. | AreaStatisticalUnit | voidable
tesselation | Structura în rețea alcătuită din unități. | StatisticalTessellation | voidable
Constrângeri ale tipului de obiect spațial «AreaStatisticalUnit»
Geometria de referință a unităților statistice zonale ar trebui să fie o «GM_MultiSurface».
1.3.1.3. Partiție statistică (StatisticalTessellation)
O structură în mozaic compusă din unități statistice zonale.
Atribute ale tipului de obiect spațial «StatisticalTessellation»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
Roluri de asociere ale tipului de obiect spațial «StatisticalTessellation»
Rol de asociere | Definiție | Tip | Voidability
units | Unitățile care alcătuiesc o structură în mozaic. | AreaStatisticalUnit | voidable
lower | Structura statistică în mozaic de la nivelul imediat inferior. | StatisticalTessellation | voidable
upper | Structura statistică în mozaic de la nivelul imediat superior. | StatisticalTessellation | voidable
1.3.1.4. Evoluție (Evolution)
Reprezentare a evoluției unității statistice vectoriale.
Atribute ale tipului de obiect spațial «Evolution»
Atribut | Definiție | Tip | Voidability
date | Data la care a avut loc modificarea. | DateTime |
evolutionType | Tipul de evoluție. | EvolutionTypeValue |
areaVariation | Variația zonei în timpul evoluției. Acest atribut trebuie populat numai în cazul în care tipul este «modificare». | Area | voidable
populationVariation | Variația populației în timpul evoluției. Acest atribut trebuie populat numai în cazul în care tipul este «modificare». | Integer | voidable
Roluri de asociere ale tipului de obiect spațial «Evolution»
Rol de asociere | Definiție | Tip | Voidability
finalUnitVersions | Toate versiunile finale ale unității vizate de evoluție. | VectorStatisticalUnit | voidable
units | Toate unitățile vizate de evoluție. | VectorStatisticalUnit | voidable
initialUnitVersions | Toate versiunile inițiale ale unității vizate de evoluție. | VectorStatisticalUnit | voidable
Constrângeri ale tipului de obiect spațial «Evolution»
Reprezentările evoluției trebuie să fie coerente cu versiunile obiectelor în cauză.
O evoluție cu al cărei «typeValue» este «creație» nu trebuie să aibă versiuni inițiale ale unității statistice și trebuie să aibă o singură versiune finală.
O evoluție al cărei «typeValue» este «eliminare» trebuie să aibă o singură versiune inițială a unității statistice și nicio versiune finală.
O evoluție al cărei «typeValue» este «agregare» trebuie să aibă cel puțin două versiuni inițiale ale unității statistice (unitățile ce urmează a fi agregate) și o singură versiune finală (agregarea rezultată).
O evoluție al cărei «typeValue» este «modificare» trebuie să aibă o singură versiune inițială a unității statistice și nicio versiune finală.
O evoluție al cărei «typeValue» este «disociere» trebuie să aibă o singură versiune inițială a unității statistice (unitatea care trebuie divizată) și cel puțin două veriuni finale (unitățile care rezultă în urma disocierii).
1.3.2. Tipuri de date
1.3.2.1. Geometria unității vectoriale statistice (VectorStatisticalUnitGeometry)
Un reprezentare geometrică pentru unitățile vectoriale statistice.
Atribute ale tipului de date «VectorStatisticalUnitGeometry»
Atribut | Definiție | Tip | Voidability
geometry | Geometria. | GM_Object |
geometryDescriptor | Descriptorul geometriei unității statistice. | GeometryDescriptor |
1.3.2.2. Descriptorul geometriei (GeometryDescriptor)
Un descriptor pentru geometria unității statistice vectoriale.
Atribute ale tipului de date «GeometryDescriptor»
Atribut | Definiție | Tip | Voidability
geometryType | Tipul de geometrie. | GeometryTypeValue |
mostDetailedScale | Scara cea mai detaliată pentru care se presupune că geometria generalizată este adecvată (exprimată ca inversul unei scări indicative). | Integer |
leastDetailedScale | Scara cea mai puțin detaliată pentru care se presupune că geometria generalizată este adecvată (exprimată ca inversul unei scări indicative). | Integer |
Constrângerile tipului de date «GeometryDescriptor»
Câmpurile mostDetailedScale și leastDetailedScale sunt furnizate numai pentru descriptori ai geometriei cu o tip generalisedGeometry.
În cazul în care este furnizată, mostDetailedScale trebuie să fie mai mică decât leastDetailedScale.
1.3.3. Liste de coduri
1.3.3.1. Tipul de geometrie (GeometryTypeValue)
Valorile codurilor pentru tipurile de geometrie.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «GeometryTypeValue»
Valoare | Nume | Definiție
referenceGeometry | geometrie de referință | Geometria descrisă este geometria de referință.
pointLabel | point label | Geometria descrisă este o geometrie în puncte pentru etichetare.
centerOfGravity | centru de gravitație | Geometria descrisă este o geometrie a punctului situată în centrul de gravitație al unității.
generalisedGeometry | geometrie generalizată | O geometrie generalizată a unității statistice.
other | altele | Alt tip de geometrie.
1.3.3.2. Tipul de evoluție (EvolutionTypeValue)
Valorile de cod pentru tipurile de evoluție.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile privind unitățile statistice specificate în Ghidul tehnic INSPIRE.
1.4. Caroiaj al unităților statistice
1.4.1. Tipuri de obiecte spațiale
Pachetul «Caroiaj» conține următoarele tipuri de obiecte spațiale:
— Celulă a caroiajului statistic
— Caroiaj statistic
1.4.1.1. Celulă a caroiajului statistic (StatisticalGridCell)
Unitate de diseminare sau utilizare a informațiilor statistice care sunt reprezentate sub forma unei celule de caroiaj.
Acest tip este un subtip al «StatisticalUnit».
Atribute ale tipului de obiect spațial «StatisticalGridCell»
Atribut | Definiție | Tip | Voidability
code | Un cod de celulă. | CharacterString | voidable
geographicalPosition | Poziția geografică din colțul din stânga jos al celulei de caroiaj. | DirectPosition | voidable
gridPosition | Poziționarea celulei de caroiaj în interiorul caroiajului pe baza coordonatelor caroiajului. | GridPosition | voidable
geometry | Geometria celulei de caroiaj. | GM_Surface | voidable
Roluri de asociere ale tipului de obiect spațial «StatisticalGridCell»
Rol de asociere | Definiție | Tip | Voidability
lowers | Celulele imediat inferioar ale caroiajului statistic. | StatisticalGridCell | voidable
upper | Celulele imediat superioare ale caroiajului statistic. | StatisticalGridCell | voidable
grid | Caroiajul format din celule. | StatisticalGrid |
Constrângeri ale tipului de obiect spațial «StatisticalGridCell»
Celula trebuie poziționată în interiorul caroiajului, în funcție de lățimea și înălțimea sa.
Trebuie să se furnizeze cel puțin unul dintre codurile «atribute», «geographicalPosition», «gridPosition» sau «geometrie».
În cazul în care sunt furnizate mai multe reprezentări spațiale (cod, geographicalPosition, gridPosition și geometrie), acestea trebuie să fie consecvente.
Codul este format din:
(1) O parte a sistem de referință de coordonate, reprezentată de cuvântul CRS, urmată de codul EPSG.
(2) O parte care corespunde rezoluției și poziției:
— În cazul în care sistemul de referință de coordonate este proiectat, cuvântul RES urmat de rezoluția caroiajului în metri și litera m. Urmează litera N, urmată de valoarea ordonatei în metri și litera E, urmată de valoarea abscisei în metri.
— În cazul în care sistemul de referință de coordonate nu este proiectat, cuvântul RES urmat de rezoluția caroiajului în grade-minute-secunde, urmat de cuvântul dms. Urmează cuvântul LON urmat de valoarea longitudinii în grade-minute-secunde și cuvântul LAT urmat de valoarea latitudinii în grade-minute-secunde.
În ambele cazuri, poziția dată va fi poziția colțului din stânga jos al celulei.
1.4.1.2. Caroiaj statistic (StatisticalGrid)
Un caroiaj alcătuit din celule statistice.
Atribute ale tipului de obiect spațial «StatisticalGrid»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
EPSGCode | Codul EPSG de identificare a Sistemului de referință de coordonate al caroiajului. | Integer |
resolution | Rezoluția caroiajului. | StatisticalGridResolution |
origin | Poziția punctului de origine al caroiajului din cadrul sistemului de referință de coordonate specificat (dacă este definită). | DirectPosition |
width | Lățimea caroiajului, exprimată în numărul de celule (dacă este definită). | Integer |
height | Înălțimea caroiajului, exprimată în numărul de celule (dacă este definită). | Integer |
Roluri de asociere ale tipului de obiect spațial «StatisticalGrid»
Rol de asociere | Definiție | Tip | Voidability
cells | Celulele care alcătuiesc un caroiaj. | StatisticalGridCell |
lower | Caroiajul statistic imediat inferior. | StatisticalGrid | voidable
upper | Caroiajul statistic imediat superior. | StatisticalGrid | voidable
Constrângeri ale tipului de obiect spațial «StatisticalGrid»
În cazul în care sistemul de referință de coordonate este unul proiectat, rezoluția va fi reprezentată de o lungime. În caz contrar, aceasta va fi reprezentată de un unghi.
1.4.2. Tipuri de date
1.4.2.1. Poziție în caroiaj (GridPosition)
Poziția unei celule de caroiaj în cadrul unui caroiaj.
Atribute ale tipului de date «GridPosition»
Atribut | Definiție | Tip | Voidability
x | Poziția celulei pe axa orizontală, începând din partea stângă, înspre dreapta, de la 0 la lățimea -1 a caroiajului. | Integer |
y | Poziția celulei pe axa verticală, începând din partea de jos înspre partea de sus, de la 0 la înălțimea -1 a caroiajului. | Integer |
1.4.2.2. Rezoluția caroiajului statistic (StatisticalGridResolution)
O valoare a rezoluției unității statistice.
Acest tip este o uniune.
Atribute ale tipului uniune «StatisticalGridResolution»
Atribut | Definiție | Tip | Voidability
lengthResolution | Rezoluție axială. | Length |
angleResolution | Rezoluție unghiulară. | Angle |
1.5. Cerințe specifice categoriei
| (1) | Trebuie pusă la dispoziție, de asemenea, cel puțin geometria unităților statistice, pentru care sunt disponibile date statistice în temeiul directivei INSPIRE. Această cerință se aplică temelor INSPIRE care se referă la unități statistice.
| (2) | Pentru utilizare paneuropeană, se recurge la caroiajul cu celule de suprafață egală definit în secțiunea 2.2.1 din anexa II.
| (3) | Datele statistice se referă la unitatea lor statistică prin intermediul identificatorului de obiect exterm al unității (inspireId) sau al identificatorului tematic (pentru unitățile vectoriale) sau al codului unității (pentru celulele de caroiaj).
| (4) | Datele statistice trebuie să se refere la o versiune specifică a unei unități statistice.
1.6. Straturi
Straturi pentru categoria de date spațiale «Statistical Units»
Numele stratului | Titlul stratului | Tip de obiect spațial
SU.VectorStatisticalUnit | Unități statistice vectoriale | VectorStatisticalUnit
SU.StatisticalGridCell | Celule ale caroiajului statistic | StatisticalGridCell
2. CLĂDIRI
2.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «date în 2D» (2D data) înseamnă date în cazul cărora geometria obiectelor spațiale este reprezentată în spațiu bidimensional.
(2) «date în 2,5D» (2.5D data) înseamnă date în cazul cărora geometria obiectelor spațiale este reprezentată în spațiu tridimensional cu constrângerea că, pentru fiecare poziție (X,Y), există doar un singur Z.
(3) «date în 3D» (3D data) înseamnă date în cazul cărora geometria obiectelor spațiale este reprezentată în spațiu tridimensional.
(4) «componentă a clădirii» (building component) înseamnă orice subdiviziune sau element al unei clădiri.
2.2. Structura categoriei de date spațiale «Clădiri»
Tipurile specificate pentru categoria de date spațiale «Clădiri» sunt organizate în următoarele pachete:
— Baza clădirilor
— Clădiri în 2D
— Clădiri în 3D
2.3. Baza clădirilor
2.3.1. Tipuri de obiecte spațiale
Pachetul «Baza clădirilor» conține următoarele tipuri de obiecte spațiale:
— Construcție proiectată
— Clădire proiectată
— Clădire
— Parte a clădirii
2.3.1.1. Construcție proiectată (AbstractConstruction)
Tip de obiect spațial abstract care grupează proprietățile semantice ale clădirilor, părților clădirilor.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractConstruction»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Numele construcției. | GeographicalName | voidable
dateOfConstruction | Data construcției. | DateOfEvent | voidable
dateOfDemolition | Data demolării. | DateOfEvent | voidable
dateOfRenovation | Data ultimei renovări majore. | DateOfEvent | voidable
elevation | Proprietate dimensională constrânsă pe verticală constând dintr-o măsură absolută referențiată față de o suprafață bine definită, luată de regulă ca origine (geoid, nivelul apei, etc.) | Elevation | voidable
externalReference | Trimitere la un sistem de informații extern care conține orice informație referitoare la obiectul spațial. | ExternalReference | voidable
heightAboveGround | Înălțimea de la sol. | HeightAboveGround | voidable
conditionOfConstruction | Starea construcției. | ConditionOfConstructionValue | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
2.3.1.2. Clădire proiectată (AbstractBuilding)
Tip de obiect spațial abstract care grupează proprietățile semantice comune ale tipurilor de obiecte spațiale «Building» și «BuildingPart».
Acest tip este un subtip al «AbstractConstruction».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractBuilding»
Atribut | Definiție | Tip | Voidability
buildingNature | Caracteristică a clădirii care, de regulă, o face să prezinte interes pentru aplicații de cartografiere. Caracteristica respectivă poate fi legată de aspectul fizic și/sau de funcția clădirii. | BuildingNatureValue | voidable
currentUse | Activitate găzduită în clădire. Acest atribut se referă în principal la clădirile care găzduiesc activități umane. | CurrentUse | voidable
numberOfDwellings | Numărul de locuințe. | Integer | voidable
numberOfBuildingUnits | Numărul tronsoanelor de clădire prezente în clădire. O «BuildingUnit» este o subdiviziune a «Building» cu propriul său acces blocabil din exterior sau dintr-un spațiu comun (adică nu dintr-o altă «BuildingUnit»), care este elementară, independentă din punct de vedere funcțional și care poate fi vândută, dată spre închiriere, moștenită etc. | Integer | voidable
numberOfFloorsAboveGround | Numărul etajelor de deasupra solului. | Integer | voidable
2.3.1.3. Clădire (Building)
O «Clădire» este o construcție închisă situată la suprafața solului și/sau în subteran, utilizată sau menită a fi utilizată pentru adăpostirea oamenilor, animalelor sau lucrurilor sau pentru producerea de bunuri economice. O clădire se referă la orice structură permanentă construită sau montată pe teren.
Acest tip este un subtip al «AbstractBuilding».
Acest tip este abstract.
Roluri de asociere ale tipului de obiect spațial «Building»
Rol de asociere | Definiție | Tip | Voidability
parts | Părțile din care este alcătuită clădirea. | BuildingPart | voidable
2.3.1.4. Parte a clădirii (BuildingPart)
O «BuildingPart» este o subdiviziune a unei «Clădiri», care ar putea fi considerată o clădire în sine.
Acest tip este un subtip al «AbstractBuilding».
Acest tip este abstract.
2.3.2. Tipuri de date
2.3.2.1. Utilizare actuală (CurrentUse)
Acest tip de date permite detalierea utilizării (utilizărilor) actuală.
Atribute ale tipului de date «CurrentUse»
Atribut | Definiție | Tip | Voidability
currentUse | Utilizare curentă. | CurrentUseValue |
procentaj | Proporția, exprimată în procente, dedicată utilizării curente. | Integer |
Constrângeri ale tipului de date «CurrentUse»
Totalul tuturor procentajelor trebuie să fie mai mic sau egal cu 100.
2.3.2.2. Data evenimentului (DateOfEvent)
Acest tip de date include diversele modalități posibile de a defini data unui eveniment.
Atribute ale tipului de date «DateOfEvent»
Atribut | Definiție | Tip | Voidability
anyPoint | Data și ora oricărui moment al evenimentului, între începutul și sfârșitul său. | DateTime | voidable
beginning | Data și ora când a început evenimentul. | DateTime | voidable
end | Data și ora când s-a încheiat evenimentul. | DateTime | voidable
Constrângeri ale tipului de date «DateOfEvent»
Trebuie să se furnizeze cel puțin unul dintre atributele «beginning», «end» sau «anyPoint».
În cazul în care este furnizat, atributul «beginning» nu poate fi enumerat după atributul «anyPoint» și atributul «end», iar atributul «anyPoint» nu poate fi enumerat după atributul «end».
2.3.2.3. Cotă (Elevation)
Acest tip de date include însăși valoarea elevației și informații cu privire la modul în care a fost măsurată.
Atribute ale tipului «Elevation»
Atribut | Definiție | Tip | Voidability
elevationReference | Element unde a fost măsurată cota. | ElevationReferenceValue |
elevationValue | Valoarea cotei. | DirectPosition |
2.3.2.4. Trimitere externă (ExternalReference)
Trimitere la un sistem de informații extern care conține orice informație referitoare la obiectul spațial.
Atribute ale tipului de date «ExternalReference»
Atribut | Definiție | Tip | Voidability
informationSystem | Identificator de resurse uniform al sistemului de informații extern. | URI |
informationSystemName | Numele sistemului de informații extern. | PT_FreeText |
reference | Identificator tematic al obiectului spațial sau al oricărei informații referitoare la obiectul spațial. | CharacterString |
2.3.2.5. Înălțimea de la sol (HeightAboveGround)
Distanța verticală dintre un punct de referință inferior și unul superior.
Atribute ale tipului de date «HeightAboveGround»
Atribut | Definiție | Tip | Voidability
heightReference | Element utilizat ca punct de referință superior. | ElevationReferenceValue | voidable
lowReference | Element utilizat ca punct de referință inferior. | ElevationReferenceValue | voidable
status | Modul în care a fost măsurată înălțimea. | HeightStatusValue | voidable
value | Valoarea înălțimii de la sol. | Length |
Constrângeri ale tipului de date «HeightAboveGround»
Valoarea «HeightAboveGround» se exprimă în metri.
2.3.2.6. Geometria în 2D a clădirii (BuildingGeometry2D)
Aceste tipuri de date includ geometria clădirii și metadatele referitoare la elementul clădirii captat și la modalitatea de captare.
Atribute ale tipului de date «BuildingGeometry2D»
Atribut | Definiție | Tip | Voidability
geometry | Reprezentare geometrică în 2D sau în 2,5D. | GM_Object |
horizontalGeometryEstimatedAccuracy | Acuratețea de poziționare absolută estimată pentru coordonatele (X,Y) ale geometriei clădirii în cadrul sistemului oficial de referință de coordonate INSPIRE. Acuratețea de poziționare absolută reprezintă valoarea medie a incertitudinilor poziționale pentru un set de poziții, unde incertitudinile poziționale reprezintă distanța dintre o poziție măsurată și ceea ce se consideră a fi poziția reală corespunzătoare. | Length | voidable
horizontalGeometryReference | Element al clădirii care a fost captat prin coordonate (X,Y). | HorizontalGeometryReferenceValue |
referenceGeometry | Geometria care urmează să fie luată în considerare de serviciile de vizualizare, pentru ilustrare. | Boolean |
verticalGeometryEstimatedAccuracy | Acuratețea de poziționare absolută estimată pentru coordonatele Z ale geometriei clădirii, în cadrul sistemului oficial de referință de coordonate INSPIRE. Acuratețea de poziționare absolută reprezintă valoarea medie a incertitudinilor poziționale pentru un set de poziții, unde incertitudinile poziționale reprezintă distanța dintre o poziție măsurată și ceea ce se consideră a fi poziția reală corespunzătoare. | Length | voidable
verticalGeometryReference | Element al clădirii care a fost captat prin coordonate verticale. | ElevationReferenceValue |
Constrângeri ale tipului de date «BuildingGeometry2D»
Geometria trebuie să fie de tip «GM_Point» sau «GM_Surface» sau «GM_MultiSurface».
Valoarea «horizontalGeometryEstimatedAccuracy» trebuie exprimată în metri.
Pentru exact un element de «BuildingGeometry», valoarea atributului «referenceGeometry» trebuie să fie «Adevărat» (True).
Valoarea «verticalGeometryEstimatedAccuracy» se exprimă în metri.
2.3.3. Liste de coduri
2.3.3.1. Tipul clădirii (BuildingNatureValue)
Valori care indică tipul unei clădiri.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «BuildingNatureValue»
Valoare | Nume | Definiție
arch | arcadă | O structură artificială sub forma unei arcade.
bunker | buncăr | Un edificiu, parțial subteran, menit a fi utilizat sau chiar utilizat de armată fie pentru amplasarea centrelor de comandă/control, fie pentru instalarea de campamente militare.
canopy | copertină | Un acoperiș care oferă adăpost lucrurilor aflate dedesubt. Acoperișurile de protecție pot fi cadre de sine stătătoare deasupra cărora se atașează un înveliș sau pot fi legate sau suspendate în exteriorul unei clădiri.
caveBuilding | construcție tip pivniță | Un spațiu care găzduiește activități umane sau economice, care este de regulă mărginit de pereți din piatră, la care se adaugă o serie de pereți construiți artificial și care poate conține structuri comparabile cu structurile interioare ale clădirilor de sine stătătoare.
chapel | capelă | Un loc de cult creștin, de obicei mai mic decât o biserică.
castle | castel | O clădire ornată și fortificată de mari dimensiuni, de obicei construită cu scopul de a constitui o reședință privată sau de a oferi protecție.
church | biserică | Clădire sau o structură al cărei scop principal este de a facilita practica religioasă a unei comunități creștine.
dam | baraj | Barieră transversală permanentă situată pe un curs de apă, utilizată pentru reținerea apei sau pentru controlul debitului acesteia.
greenhouse | seră | O clădire adesea construită în principal din material transparent (de exemplu: sticlă), în care temperatura și umiditatea pot fi controlate în vederea cultivării și/sau a protejării plantelor.
lighthouse | far | Un turn conceput să emită un turn lumină dintr-un sistem de lămpi și lentile.
mosque | moschee | Clădire sau o structură al cărei scop principal este de a facilita practica religioasă a unei comunități musulmane.
shed | magazie | O clădire construită din material ușor, prevăzută cu una sau mai multe părți laterale deschise, utilizată în general în scopuri de depozitare.
silo | siloz | O structură de depozitare de mari dimensiuni, în general cilindrică, utilizată pentru depozitarea în vrac.
stadium | stadion | Un loc sau un edificiu destinat desfășurării de competiții sportive, de concerte sau de alte evenimente, care constă dintr-un câmp sau dintr-o scenă, încercuit(ă) parțial sau complet de o structură menită să le permită spectatorilor să ocupe locuri în picioare sau pe scaune și să vizioneze evenimentul.
storageTank | rezervor de depozitare | Un container utilizat de obicei pentru depozitarea de lichide și gaze comprimate.
synagogue | sinagogă | Clădire sau o structură al cărei scop principal este de a facilita practica religioasă a unei comunități evreiești sau samaritene.
temple | templu | Clădire sau o structură al cărei scop principal este de a facilita practicile religioase.
tower | turn | O structură relativ înaltă și îngustă, care poate fi de sine stătătoare sau care poate face parte dintr-o altă structură.
windmill | moară de vânt | O clădire care convertește energia eoliană într-o mișcare de rotație prin intermediul unor vele sau lame reglabile.
windTurbine | turbină eoliană | Un turn și echipamentele aferente care generează energie electrică din energie eoliană.
2.3.3.2. Starea construcției (ConditionOfConstructionValue)
Valori care indică starea unei construcții.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «ConditionOfConstructionValue»
Valoare | Nume | Definiție
declined | degradată | Construcție care nu poate fi utilizată în condiții normale, deși principalele sale elemente (pereți, acoperiș) sunt încă prezente.
demolished | demolată | Construcția a fost demolată. Nu mai există rămășițe vizibile.
functional | funcțională | Construcția este funcțională.
projected | proiectată | Construcția este în curs de proiectare. Lucrările de construcție nu au început încă.
ruin | ruină | Construcția a fost parțial demolată, iar unele elemente principale (acoperiș, pereți) au fost distruse. Există unele resturi vizibile ale construcției.
underConstruction | în construcție | Construcția este în construcție, nefiind încă funcțională. Se aplică numai lucrărilor inițiale de construcție a construcției și nu lucrărilor de întreținere.
2.3.3.3. Utilizare curentă (CurrentUseValue)
Valori care indică utilizarea curentă.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «CurrentUseValue»
Valoare | Nume | Definiție | Parent value
residential | residential | Clădirea (sau o componentă a clădirii) este utilizată în scopuri rezidențiale. |
individualResidence | reședință individuală | Clădirea (sau o componentă a clădirii) găzduiește o singură locuință. | residential
collectiveResidence | reședință colectivă | Clădirea (sau o componentă a clădirii) găzduiește mai mult de o locuință. | residential
twoDwellings | două locuințe | Clădirea (sau o componentă a clădirii) găzduiește două locuințe. | collectiveResidence
moreThanTwoDwelling | cu mai mult de două locuințe | Clădirea (sau o componentă a clădirii) găzduiește cel puțin 3 locuințe. | collectiveResidence
residenceForCommunities | reședință pentru comunități | Clădirea (sau o componentă a clădirii) găzduiește o reședință pentru comunități. | residential
agriculture | agricultură | Clădirea (sau o componentă a clădirii) este utilizată în scopul desfășurării de activități agricole. |
industrial | industrial | Clădirea (sau o componentă a clădirii) este utilizată pentru activități din sectorul secundar (industrial). |
commerceAndServices | comerț și servicii | Clădirea (sau o componentă a clădirii) este utilizată în scopul desfășurării oricăror tipuri de prestări de servicii. Această valoare vizează clădirile și componentele clădirilor destinate desfășurării de activități din sectorul terțiar (comercial și servicii). |
office | birou | Clădirea (sau o componentă a clădirii) găzduiește birouri. | commerceAndServices
trade | comerț | Clădirea (sau o componentă a clădirii) găzduiește activități comerciale. | commerceAndServices
publicServices | servicii publice | Clădirea (sau o componentă a clădirii) găzduiește servicii publice. Serviciile publice sunt servicii terțiare furnizate în beneficiul cetățenilor. | commerceAndServices
ancillary | dependință | O clădire (sau o componentă a clădirii) de mici dimensiuni, care este utilizată numai în legătură cu o altă clădire mai mare (sau cu o componentă a clădirii) și care, în general, nu dobândește aceleași funcții și caracteristici ca și clădirea (sau componenta clădirii) de care este legată. |
2.3.3.4. Valoarea de referință a cotei (ElevationReferenceValue)
Lista elementelor posibile luate în considerare pentru a capta o geometrie verticală.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «ElevationReferenceValue»
Valoare | Nume | Definiție
aboveGroundEnvelope | anvelopa de deasupra solului | Cota a fost captată la nivelul limitei maxime a anvelopei de deasupra solului a construcției.
bottomOfConstruction | fundația construcției | Cota a fost captată la nivelul de jos a părții utilizabile a construcției.
entrancePoint | punct de acces | Cota a fost captată la intrarea în construcție, în general în partea de jos a ușii de la intrare.
generalEave | punct al cornișei (general eave) | Cota a fost înregistrată la nivelul cornișei, oriunde între nivelurile cele mai joase și cele mai înalte ale cornișei construcției.
generalGround | punct al solului | Cota a fost înregistrată la nivelul solului, oriunde între punctul cel mai jos și punctul cel mai de sus ale construcției.
generalRoof | punct al acoperișului | Cota a fost înregistrată la nivelul acoperișului, oriunde între nivelul cel mai de jos al marginii acoperișului și partea cea mai înaltă a construcției.
generalRoofEdge | punct al marginii acoperișului | Cota a fost înregistrată la nivelul marginii acoperișului, oriunde între marginea inferioară și marginea superioară a acoperișului construcției.
highestEave | cornișa superioară | Cota a fost înregistrată la nivelul superior al cornișei construcției.
highestGroundPoint | cel mai înalt punct de la sol | Cota a fost înregistrată în punctul fix superior al construcției.
highestPoint | cel mai înalt punct | Cota a fost înregistrată în punctul cel mai înalt al construcției, inclusiv al instalațiilor, cum ar fi coșurile de fum și antenele.
highestRoofEdge | marginea superioară a acoperișului | Cota a fost înregistrată la nivelul cel mai înalt al marginii acoperișului construcției.
lowestEave | cornișa inferioară | Cota a fost înregistrată la nivelul inferior al cornișei construcției.
lowestFloorAboveGround | etajul cel mai de jos de la sol | Cota a fost captată la nivelul celui mai de jos etaj de la sol.
lowestGroundPoint | cel mai jos punct de la sol | Cota a fost înregistrată la nivelul celui mai jos punct de la sol al construcției.
lowestRoofEdge | cea mai joasă margine a acoperișului | Cota a fost înregistrată la nivelul cel mai de jos al cornișei construcției.
topOfConstruction | partea superioară a construcției | Cota a fost înregistrată la nivelul superior al construcției.
2.3.3.5. Statutul înălțimii (HeightStatusValue)
Valori care indică metoda utilizată pentru a înregistra o înălțime.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «HeightStatusValue»
Valoare | Nume | Definiție
estimated | estimată | Înălțimea a fost estimată fără a fi măsurată.
measured | măsurată | Înălțimea a fost măsurată (în mod direct sau indirect).
2.3.3.6. Valoarea de referință a geometriei orizontale (HorizontalGeometryReferenceValue)
Valori care indică elementul luat în considerare pentru a înregistra o geometrie orizontală.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «HorizontalGeometryReferenceValue»
Valoare | Nume | Definiție
aboveGroundEnvelope | anvelopa de deasupra solului | Geometria orizontală a clădirii a fost captată cu ajutorul anvelopei de deasupra solului a clădirii, respectiv al întinderii maxime de la sol a clădirii.
combined | combinată | Geometria orizontală a clădirii s-a obținut prin combinarea geometriilor părților clădirii care o alcătuiesc, în cazul în care geometriile părților clădirii au referințe geometrice orizontale diferite.
entrancePoint | punct de acces | Geometria clădirii este reprezentată de un punct situat la intrarea în clădire.
envelope | anvelopă | Geometria orizontală a clădirii a fost captată cu ajutorul întregii anvelope a clădirii, respectiv al întinderii maxime a clădirii la suprafață și în subteran.
footPrint | amprenta de la sol | Geometria orizontală a clădirii a fost captată cu ajutorul amprentei de la sol a clădirii, adică al extinderii sale la nivelul solului.
lowestFloorAboveGround | etajul cel mai de jos de la sol | Geometria orizontală a clădirii a fost captată utilizându-se cel mai de jos etaj de la sol al clădirii.
pointInsideBuilding | punct în interiorul clădirii | Geometria orizontală a clădirii este reprezentată de un punct situat în interiorul clădirii.
pointInsideCadastralParcel | punct în interiorul parcelei cadastrale | Geometria orizontală a clădirii este reprezentată de un punct situat în interiorul parcelei căreia îi aparține clădirea.
roofEdge | marginea acoperișului | Geometria orizontală a clădirii a fost captată utilizându-se marginile acoperișului clădirii.
2.4. Clădiri în 2D
2.4.1. Tipuri de obiecte spațiale
Pachetul «Clădirii în 2D» conține următoarele tipuri de obiecte spațiale:
— Building
— Parte a clădirii
2.4.1.1. Clădire (Building)
O «Clădire» este o construcție închisă situată la suprafața solului și/sau în subteran, utilizată sau menită a fi utilizată pentru adăpostirea oamenilor, animalelor sau lucrurilor sau pentru producerea de bunuri economice. O clădire se referă la orice structură construită sau montată pe situl său de manieră permanentă.
Acest tip este un subtip al pachetului «Baza clădirilor».
Atribute ale tipului de obiect spațial «Building»
Atribut | Definiție | Tip | Voidability
geometry2D | Reprezentare geometrică în 2D sau în 2,5D a clădirii. | BuildingGeometry2D |
Constrângeri ale tipului de obiect spațial «Building»
Un singur atribut de tip «geometry2D» trebuie să fie o geometrie de referință, și anume o «geometry2D» cu un atribut «referenceGeometry» setat ca «true».
Părțile clădirii trebuie reprezentate utilizându-se tipul «BuildingPart» din pachetul «Buildings2D».
2.4.1.2. Parte a clădirii (BuildingPart)
O «BuildingPart» este o subdiviziune a unei «Clădiri», care ar putea fi considerată o clădire în sine.
Acest tip este un subtip al «BuildingPart» din pachetul «Baza clădirilor».
Atribute ale tipului de obiect spațial «BuildingPart»
Atribut | Definiție | Tip | Voidability
geometry2D | Reprezentare geometrică în 2D sau în 2,5D a părții clădirii. | BuildingGeometry2D |
Constrângeri ale tipului de obiect spațial «BuildingPart»
Un singur atribut de tip «geometry2D» trebuie să fie o geometrie de referință, și anume atributul «referenceGeometry» trebuie setat ca «true».
2.5. Clădiri în 3D
2.5.1. Tipuri de obiecte spațiale
Pachetul «Clădirii în 3D» conține următoarele tipuri de obiecte spațiale:
— Clădire
— Parte a clădirii
2.5.1.1. Clădire (Building)
O «Clădire» este o construcție închisă situată la suprafața solului și/sau în subteran, utilizată sau menită a fi utilizată pentru adăpostirea oamenilor, animalelor sau lucrurilor sau pentru producerea de bunuri economice. O clădire se referă la orice structură construită sau montată pe situl său de manieră permanentă.
Acest tip este un subtip al «Building» din pachetul «Baza clădirilor».
Atribute ale tipului de obiect spațial «Building»
Atribut | Definiție | Tip | Voidability
geometry2D | Reprezentare geometrică în 2D sau în 2,5D. | BuildingGeometry2D | voidable
geometry3DLoD1 | Reprezentare geometrică în 3D la nivelul 1 de detaliu (LoD), alcătuită din reprezentarea generalizată a limitei exterioare prin suprafețele laterale verticale și poligoanele orizontale de bază. | BuildingGeometry3DLoD1 | —
geometry3DLoD2 | Reprezentare geometrică în 3D la nivelul 2 de detaliu (LoD), formată din reprezentarea generalizată a limitei exterioare prin suprafețele verticale laterale și o formă prototipică de acoperiș sau acoperitoare (dintr-o listă prestabilită de forme de acoperișuri) | BuildingGeometry3DLoD2 | —
geometry3DLoD3 | Reprezentare geometrică în 3D la nivelul 3 de detaliu (LoD), formată din reprezentarea detaliată a limitei exterioare (inclusiv proeminențele, elementele de fațadă și nișele de fereastră), precum și din forma acoperișului (inclusiv lucarnele, coșurile de fum). | BuildingGeometry3DLoD | —
geometry3DLoD4 | Reprezentare geometrică în 3D la nivelul 4 de detaliu (LoD), formată din reprezentarea detaliată a limitei exterioare (inclusiv proeminențele, elementele de fațadă și nișele de fereastră), precum și din forma acoperișului (inclusiv lucarnele, coșurile de fum). | BuildingGeometry3DLoD | —
Constrângeri ale tipului de obiect spațial «Building»
În cazul în care o «Clădire» nu dispune de «BuildingParts», trebuie să se furnizeze cel puțin atributele «geometry3DLoD1» sau «geometry3DLoD2» sau «geometry3DLoD3» sau «geometry3DLoD4».
Părțile clădirii sunt reprezentate utilizându-se tipul «BuildingPart» din pachetul «Buildings2D».
2.5.1.2. Parte a clădirii (BuildingPart)
O «BuildingPart» este o subdiviziune a unei «Clădiri», care ar putea fi considerată o clădire în sine.
Acest tip este un subtip al «BuildingPart» din pachetul «Baza clădirilor».
Atribute ale tipului de obiect spațial «BuildingPart»
Atribut | Definiție | Tip | Voidability
geometry2D | Reprezentare geometrică în 2D sau în 2,5D. | BuildingGeometry2D | voidable
geometry3DLoD1 | Reprezentare geometrică în 3D la nivelul 1 de detaliu (LoD), alcătuită din reprezentarea generalizată a limitei exterioare prin suprafețele laterale verticale și poligoanele orizontale de bază. | BuildingGeometry3DLoD1 | —
geometry3DLoD2 | Reprezentare geometrică în 3D la nivelul 2 de detaliu (LoD), formată din reprezentarea generalizată a limitei exterioare prin suprafețele verticale laterale și o formă prototipică de acoperiș sau acoperitoare (dintr-o listă prestabilită de forme de acoperișuri) | BuildingGeometry3DLoD2 | —
geometry3DLoD3 | Reprezentare geometrică în 3D la nivelul 3 de detaliu (LoD), formată din reprezentarea detaliată a limitei exterioare (inclusiv proeminențele, elementele de fațadă și nișele de fereastră), precum și din forma acoperișului (inclusiv lucarnele, coșurile de fum). | BuildingGeometry3DLoD | —
geometry3DLoD4 | Reprezentare geometrică în 3D la nivelul 4 de detaliu (LoD), formată din reprezentarea detaliată a limitei exterioare (inclusiv proeminențele, elementele de fațadă și nișele de fereastră), precum și din forma acoperișului (inclusiv lucarnele, coșurile de fum). | BuildingGeometry3DLoD | —
Constrângeri ale tipului de obiect spațial «BuildingPart»
Trebuie să se furnizeze cel puțin unul dintre atributele «geometry3DLoD1» sau «geometry3DLoD2» sau «geometry3DLoD3» sau «geometry3DLoD4».
2.5.2. Tipuri de date
2.5.2.1. Geometria clădirii în 3D la orice nivel de detaliu (BuildingGeometry3DLoD)
Tip de date care grupează geometria în 3D a unei clădiri sau a unei părți de clădire și metadatele aferente acestei geometrii.
Atribute ale tipului de date «BuildingGeometry3DLoD»
Atribut | Definiție | Tip | Voidability
geometryMultiSurface | Reprezentare de tip MultiSurface a limitei exterioare, care ar putea - comparativ cu o reprezentare de tip solid – să nu fie exactă din punct de vedere topologic. În speță, suprafața solului ar putea lipsi. | GM_MultiSurface |
geometrySolid | Reprezentare a limitei exterioare cu ajutorul unui solid. | GM_Solid |
terrainIntersection | Linie sau multilinie acolo unde obiectul spațial (Building, BuildingPart) intersectează planul de reprezentare a terenului. | GM_MultiCurve | voidable
horizontalGeometryEstimatedAccuracy | Acuratețea de poziționare absolută estimată pentru coordonatele (X,Y) ale geometriei, în cadrul sistemului oficial de referință de coordonate INSPIRE. Acuratețea de poziționare absolută reprezintă valoarea medie a incertitudinilor poziționale pentru un set de poziții, unde incertitudinile poziționale reprezintă distanța dintre o poziție măsurată și ceea ce se consideră a fi poziția reală corespunzătoare. | Length | voidable
verticalGeometryEstimatedAccuracy | Acuratețea de poziționare absolută estimată pentru coordonata Z- a geometriei, în cadrul sistemului oficial de referință de coordonate INSPIRE. Acuratețea de poziționare absolută reprezintă valoarea medie a incertitudinilor poziționale pentru un set de poziții, unde incertitudinile poziționale reprezintă distanța dintre o poziție măsurată și ceea ce se consideră a fi poziția reală corespunzătoare. | Length | voidable
verticalGeometryReference3DBottom | Nivelul înălțimii la care se referă înălțimea inferioară a modelului (valoarea-Z a poligonului orizontal inferior). | ElevationReferenceValue |
Constrângeri ale tipului de date «BuildingGeometry3DLoD»
Trebuie să se furnizeze fie atributul «geometryMultiSurface», fie atributul «geometrySolid».
2.5.2.2. Geometria clădirii în 3D la nivelul 1 de detaliu (BuildingGeometry3DLoD1)
Tip de date care grupează metadate specifice aferente geometriei în 3D, atunci când sunt furnizate ca urmare a unei reprezentări LoD1.
Acest tip este un subtip al «BuildingGeometry3DLoD».
Atribute ale tipului de date «BuildingGeometry3DLoD1»
Atribut | Definiție | Tip | Voidability
horizontalGeometryReference | Element captat prin coordonatele (X,Y) ale geometriei de tip MultiSurface sau de tip solid LoD1. | HorizontalGeometryReferenceValue |
verticalGeometryReference3DTop | Nivelul înălțimii la care se referă înălțimea superioară a modelului (valoarea-Z a poligonului orizontal superior). | ElevationReferenceValue |
Constrângeri ale tipului de date «BuildingGeometry3DLoD1»
Unui atribut «horizontalGeometryReference» nu trebuie să i se asocieze niciuna dintre valorile «entrancePoint», «pointInsideBuilding» sau «pointInsideCadastralParcel».
2.5.2.3. Geometria clădirii în 3D la nivelul 2 de detaliu (BuildingGeometry3DloD2)
Tip de date care grupează metadate specifice aferente geometriei în 3D, atunci când sunt furnizate ca urmare a unei reprezentări LoD2.
Acest tip este un subtip al «BuildingGeometry3DLoD».
Atribute ale tipului de date «BuildingGeometry3DLoD2»
Atribut | Definiție | Tip | Voidability
horizontalGeometryReference | Element captat prin coordonatele (X,Y) ale geometriei de tip MultiSurface sau de tip solid LoD2. | HorizontalGeometryReferenceValue |
Constrângeri ale tipului de date «BuildingGeometry3DLoD2»
Unui atribut «horizontalGeometryReference» nu trebuie să i se asocieze niciuna dintre valorile «entrancePoint», «pointInsideBuilding» sau «pointInsideCadastralParcel».
2.6. Cerințe specifice categoriei
| (1) | Prin derogare de la articolul 12 alineatul (1), domeniul de valori al proprietăților spațiale utilizate în pachetul «Clădiri în 3D» nu este restricționat.
2.7. Straturi
Straturi pentru categoria de date spațiale «Buildings»
Numele stratului | Titlul stratului | Tip de obiect spațial
BU.Building | Clădiri | Construcție (din pachetul «Clădiri în 2D»)
BU.BuildingPart | Părți ale clădirilor | BuildingPart (din pachetul «Clădiri în 2D»)
Pentru pachetul «Clădiri în 3D» nu sunt definite straturi.
3. SOL (SOIL)
3.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt indicate pentru categoria de date spațiale «Sol»:
— Profil de sol derivat
— Profil de sol observat
— Element de profil
— Unitate de sol
— Obiect derivat de sol
— Orizont de sol
— Strat de sol
— Parcelă de sol
— Profil de sol
— Sit de sol
— Acoperire pentru categoria de sol
— Acoperire descriptivă pentru categoria de sol
3.1.1. Profil de sol derivat (DerivedSoilProfile)
Un profil de sol nelocalizat care servește ca profil de referință pentru un anumit tip de sol din anumite zone geografice.
Acest tip este un subtip al «SoilProfile».
Roluri de asociere ale tipului de obiect spațial «DerivedSoilProfile»
Rol de asociere | Definiție | Tip | Voidability
isDerivedFrom | Link la unul sau la mai multe profiluri de sol observat pe baza cărora s-a obținut acest profil. | ObservedSoilProfile | voidable
3.1.2. Profil de sol observat (ObservedSoilProfile)
O reprezentare a unui profil de sol care se regăsește într-o locație anume și care este descris pe baza observărilor dintr-un puț de prospectare sau dintr-o gaură de sondă.
Acest tip este un subtip al «SoilProfile».
Roluri de asociere ale tipului de obiect spațial «ObservedSoilProfile»
Rol de asociere | Definiție | Tip | Voidability
location | Localizarea unui profil observat reprezintă parcela de sol. | SoilPlot |
3.1.3. Element de profil (ProfileElement)
Un tip de obiect spațial abstract care grupează straturi și/sau orizonturi de sol în scopuri funcționale/operaționale.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «ProfileElement»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
particleSizeFraction | Parte minerală a solului, fracționată în funcție de dimensiune (diametru), limitele particulelor. Aceasta indică ce cantitate de materialul din sol mineral este compus din particule de sol de dimensiunile specificate. | ParticleSizeFractionType | voidable
profileElementDepthRange | Adâncime superioară și inferioară a elementului de profil (strat sau orizont), măsurată de la suprafața (0 cm) unui profil de sol (în cm). | RangeType |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «ProfileElement»
Rol de asociere | Definiție | Tip | Voidability
isPartOf | Link la profilul de sol din care face parte elementul de profil. | SoilProfile |
profileElementObservation | Observarea unei proprietăți a solului care caracterizează elementul de profil (strat sau orizont). | OM_Observation | voidable
Constrângeri ale tipului de obiect spațial «ProfileElement»
Pentru a completa proprietatea «featureOfInterest» a observațiilor referitoare la elementul de profil ale unui obiect «ProfileElement», trebuie să se utilizeze același obiect «ProfileElement».
«observedProperty» a observației referitoare la elementul de profil trebuie specificată utilizându-se o valoare din lista de coduri «ProfileElementParameterNameValue».
Rezultatul observării elementului de profil trebuie să se încadreze în una dintre următoarele categorii: Number; RangeType; CharacterString.
3.1.4. Unitate de sol (SoilBody)
Parte a solului de acoperire care este delimitată și omogenă din punctul de vedere al anumitor proprietăți și modele spațiale ale solului.
Atribute ale tipului de obiect spațial «SoilBody»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Geometrie care definește limitele unității de sol. | GM_MultiSurface |
soilBodyLabel | Etichetă de identificare a unității de sol în conformitate cu cadrul de referință specificat (metadate). | CharacterString | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «SoilBody»
Rol de asociere | Definiție | Tip | Voidability
isDescribedBy | Legătura la un profil de sol derivat care caracterizează unitatea de sol, eventual în combinație cu alte profiluri de sol derivate. Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «DerivedProfilePresenceInSoilBody». | DerivedSoilProfile | voidable
3.1.5. Obiect derivat de sol (SoilDerivedObject)
Un tip de obiect spațial necesar reprezentării de obiecte spațiale cu o proprietate legată de sol provenită dintr-unul sau mai multe soluri și eventual din alte proprietăți nelegate de sol.
Atribute ale tipului de obiect spațial «SoilDerivedObject»
Atribut | Definiție | Tip | Voidability
geometry | Geometria care definește obiectul derivat de sol. | GM_Object |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
Roluri de asociere ale tipului de obiect spațial «SoilDerivedObject»
Rol de asociere | Definiție | Tip | Voidability
isBasedOnSoilDerivedObject | Legătura la un obiect derivat de sol pe ale cărui proprietăți de bazează valoarea derivată. | SoilDerivedObject | voidable
isBasedOnObservedSoilProfile | Legătura la un profil de sol observat pe ale cărui proprietăți se bazează valoarea derivată. | ObservedSoilProfile | voidable
isBasedOnSoilBody | Legătura la o unitate de sol pe ale cărui proprietăți se bazează valoarea derivată. | SoilBody | voidable
soilDerivedObjectObservation | Observarea unei proprietăți a solului în vederea caracterizării obiectului derivat de sol. | OM_Observation | voidable
Constrângeri ale tipului de obiect spațial «SoilDerivedObject»
Pentru a completa proprietatea «featureOfInterest» a observării obiectului derivat de sol, trebuie să se utilizeze obiectul «SoilDerivedObject».
«observedProperty» a observării obiectului derivat de sol trebuie specificat cu ajutorul unei valori din lista de coduri «SoilDerivedObjectParameterNameValue».
Rezultatul obiectului derivat de sol trebuie să aparțină unei dintre următoarele categorii: Number; RangeType; CharacterString.
3.1.6. Orizont de sol (SoilHorizon)
Domeniu al unui sol cu o anumită extindere verticală, mai mult sau mai puțin paralel cu suprafața și omogen în ceea ce privește majoritatea caracteristicilor morfologice și analitice, apărute într-un strat de material-mamă ca urmare a proceselor pedogenice sau alcătuit din reziduuri organice sedimentate provenite de la plante aflate în proces de creștere (turbă).
Acest tip este un subtip al «ProfileElement».
Atribute ale tipului de obiect spațial «SoilHorizon»
Atribut | Definiție | Tip | Voidability
FAOHorizonNotation | Desemnarea orizontului de sol. | FAOHorizonNotationType | voidable
otherHorizonNotation | Desemnarea orizontului de sol în conformitate cu un anumit sistem de clasificare. | OtherHorizonNotationType | voidable
3.1.7. Strat de sol (SoilLayer)
Domeniu al unui sol cu o anumită extindere verticală dezvoltată ca urmare a unor procese nepedogenice, prezentând o schimbare de structură și/sau de compoziție în raport cu părțile contingue eventual plasate deasupra sau dedesubt, sau o grupare de orizonturi de sol sau de alte subdomenii cu un obiectiv specific.
Acest tip este un subtip al «ProfileElement».
Atribute ale tipului de obiect spațial «SoilLayer»
Atribut | Definiție | Tip | Voidability
layerType | Atribuirea unui strat în conformitate cu conceptul care se potrivește tipului respectiv. | LayerTypeValue |
layerRockType | Tipul materialului în care s-a dezvoltat stratul. | LithologyValue | voidable
layerGenesisProcess | Ultimul proces nepedogenic (geologic sau antropogen) care a dus la crearea compoziției materiale stratului și la structura internă a acestuia. | EventProcessValue | voidable
layerGenesisEnvironment | Cadrul în care a avut loc ultimul proces nepedogenic (geologic sau antropogen) care a dus la crearea compoziției materiale stratului și la structura internă a acestuia. | EventEnvironmentValue | voidable
layerGenesisProcessState | Indiciu conform căruia procesul specificat în «layerGenesisProcess» este în curs de desfășurare sau a încetat să existe în trecut. | LayerGenesisProcessStateValue | voidable
Constrângeri ale tipului de obiect spațial «SoilLayer»
Atributele «layerGenesisProcess», «layerGenesisEnvironment», «layerGenesisProcessState» și «layerRockType» trebuie furnizate numai în cazul în care «layerType» are valoarea «geogen».
3.1.8. Parcelă de sol (SoilPlot)
Un loc în care are loc o anumită prospectare a solului.
Atribute ale tipului de obiect spațial «SoilPlot»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
soilPlotLocation | O trimitere la o locație terestră; aceasta poate fi o locație punctuală identificată cu ajutorul coordonatelor sau o descriere a locației utilizând text sau un identificator. | Location |
soilPlotType | Oferă informații despre tipul de teren unde are loc observarea solului. | SoilPlotTypeValue |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «SoilPlot»
Rol de asociere | Definiție | Tip | Voidability
locatedOn | Legătura la situl de sol unde se află parcela de sol sau căreia aceasta îi aparține. | SoilSite | voidable
observedProfile | Legătura la profilul de sol observat pentru care parcela de sol oferă informații privind localizarea. | ObservedSoilProfile | voidable
3.1.9. Profil de sol (SoilProfile)
O descriere a solului care este caracterizat de o succesiune verticală de elemente de profil.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «SoilProfile»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
WRBSoilName | Identificarea profilul de sol. | WRBSoilNameType | voidable
otherSoilName | Identificarea profilului de sol în conformitate cu un sistem specific de clasificare. | OtherSoilNameType | voidable
localIdentifier | Identificator unic al profilului de sol atribuit de furnizorul de date din setul de date. | CharacterString | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care fenomenul a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care fenomenul nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «SoilProfile»
Rol de asociere | Definiție | Tip | Voidability
isDescribedBy | Elementele de profil (straturi și/sau orizonturi) care constituie profilul de sol. | ProfileElement | voidable
soilProfileObservation | Observarea unei proprietăți a solului în vederea caracterizării profilului de sol. | OM_Observation | voidable
Constrângeri ale tipului de obiect spațial «SoilProfile»
Pentru a completa proprietatea «featureOfInterest» a observărilor după profilul de sol a unui obiect «SoilProfile», trebuie să se utilizeze același obiect «SoilProfile».
«observedProperty» a observării după profilul de sol trebuie specificată utilizându-se o valoare din lista de coduri «SoilProfileParameterNameValue».
Rezultatul observării după profilul de sol trebuie să se încadreze în una dintre următoarele categorii: Number; RangeType; CharacterString.
3.1.10. Sit de sol (SoilSite)
O porțiune a unei zone mai ample de cercetare, studiere sau monitorizare, unde se desfășoară o prospectare specifică a solului.
Atribute ale tipului de obiect spațial «SoilSite»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Geometria care definește situl de sol. | GM_Object |
soilInvestigationPurpose | Indiciu cu privire la motivele desfășurării unei investigări. | SoilInvestigationPurposeValue |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care fenomenul a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care fenomenul nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «SoilSite»
Rol de asociere | Definiție | Tip | Voidability
isObservedOnLocation | Link la o locație (locații) în care a avut loc investigarea sitului de sol. | SoilPlot | voidable
soilSiteObservation | Observarea unei proprietăți a solului în vederea caracterizării sitului de sol. | OM_Observation | voidable
Constrângeri ale tipului de obiect spațial «SoilSite»
Pentru a indica proprietatea «featureOfInterest» a observărilor de sit de sol ale unui obiect «SoilSite», trebuie să se utilizeze același obiect «SoilSite».
«observedProperty» a observării de sit de sol trebuie specificată utilizându-se o valoare din lista de coduri «SoilSiteParameterNameValue».
Rezultatul observării de sit de sol trebuie să se încadreze în una dintre următoarele categorii: Number; RangeType; CharacterString.
Rezultatul observării sitului de sol trebuie să fie de tipul «SoilObservationResult».
3.1.11. Acoperire pentru categoria de sol (SoilThemeCoverage)
Un tip de obiect spațial care deține valori pentru o proprietate, pe baza unuia sau mai multor parametri privind sau nu solul în cadrul domeniului său spațial, temporal și spațiotemporal.
Acest tip este un subtip al «RectifiedGridCoverage».
Atribute ale tipului de obiect spațial «SoilThemeCoverage»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime |
domainExtent | Atributul «domainExtent» conține extinderea domeniului spațio-temporal al acoperirii. Extinderea poate fi indicată atât în spațiu, cât și în timp. | EX_Extent |
validTimeFrom | «ValidTime» specifică fereastra de timp pentru care au fost captate măsurători în vederea calculării proprietății tematice a solului relevantă pentru perioada respectivă. Momentul lansării definește momentul începerii perioadei. | Date | voidable
validTimeTo | «ValidTime» specifică fereastra de timp pentru care au fost captate măsurători în vederea calculării proprietății tematice a solului relevantă pentru perioada respectivă. Momentul finalizării definește momentul încetării perioadei. | Date | voidable
soilThemeParameter | O proprietate legată de sol (categoria de sol) reprezentată de această acoperire. | SoilThemeParameterType |
Roluri de asociere ale tipului de obiect spațial «SoilThemeCoverage»
Rol de asociere | Definiție | Tip | Voidability
isDescribedBy | Această asociere permite ca o anumită «SoilThemeCoverage» să aibă o «Acoperire» conexă care nu are sens fără acoperirea de bază. | SoilThemeDescriptiveCoverage | voidable
Constrângeri ale tipului de obiect spațial «SoilThemeCoverage»
Valorile «rangeSet» trebuie să se încadreze într-una dintre următoarele categorii: Number; RangeType; CharacterString.
3.1.12. Acoperire descriptivă pentru categoria de sol (SoilThemeDescriptiveCoverage)
Un tip de obiect spațial care este asociat acoperirii pentru categoria de sol și care deține informații suplimentare referitoare la valorile unei proprietăți ale domeniului de aplicare al categoriei de sol.
Acest tip este un subtip al «RectifiedGridCoverage».
Atribute ale tipului de obiect spațial «SoilThemeDescriptiveCoverage»
Atribut | Definiție | Tip | Voidability
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime |
domainExtent | Atributul «domainExtent» conține extinderea domeniului spațio-temporal al acoperirii. Extinderea poate fi indicată atât în spațiu, cât și în timp. | EX_Extent |
soilThemeDescriptiveParameter | O proprietate descriptivă pentru proprietatea legată de sol (categoria de sol) care este reprezentată de «SoilThemeCoverage» său conex. | SoilThemeDescriptiveParameterType |
Roluri de asociere ale tipului de obiect spațial «SoilThemeDescriptiveCoverage»
Rol de asociere | Definiție | Tip | Voidability
isDescribing | Această asociere permite ca o anumită «SoilThemeCoverage» să aibă o «Acoperire» conexă care nu are sens fără acoperirea de bază. | SoilThemeCoverage |
Constrângeri ale tipului de obiect spațial «SoilThemeDescriptiveCoverage»
Valorile «rangeSet» trebuie să se încadreze într-una dintre următoarele categorii: Number; RangeType; CharacterString.
3.2. Tipuri de date
3.2.1. Prezență de profil derivat în unitatea de sol (DerivedProfilePresenceInSoilBody)
Tipul de date care indică intervalul procentajului (exprimat cu limite inferioare și superioare) ocupat de profilul derivat din corpul de sol.
Acest tip este o clasă de asociere.
Atribute ale tipului de date «DerivedProfilePresenceInSoilBody»
Atribut | Definiție | Tip | Voidability
derivedProfilePercentageRange | Interval care definește procentajul minim și maxim al suprafeței unității de sol reprezentat de un anumit profil de sol derivat. | RangeType | voidable
3.2.2. Tipul FAO de notare a orizontului (FAOHorizonNotationType)
O clasificare a unui orizont în conformitate cu sistemul de clasificare a orizontului specificat în Guidelines for soil description, 4th edition, Food and Agriculture Organization of the United Nations, Rome, 2006.
Atribute ale tipului de date «FAOHorizonNotationType»
Atribut | Definiție | Tip | Voidability
FAOHorizonDiscontinuity | Numărul utilizat pentru a indica o discontinuitate în notarea orizontului. | Integer |
FAOHorizonMaster | Simbol al orizontului principal din notarea orizontului. | FAOHorizonMasterValue |
FAOPrime | Un prim și un prim dublu pot fi utilizați pentru a conota simbolul de orizont principal al celui mai mic dintre două (prim) sau trei (dublu prim) orizonturi având prefixe numerice arabe identice și combinații de litere. | FAOPrimeValue |
FAOHorizonSubordinate | Desemnări ale distincțiilor și caracteristicilor secundare ale orizonturilor și straturilor principale au la bază caracteristici de profil observabile pe teren și sunt atribuite cu ocazia descrierii solului la fața locului. | FAOHorizonSubordinateValue |
FAOHorizonVertical | Numărul de ordine al subdiviziunii verticale din notarea orizontului. | Integer |
isOriginalClassification | Valoarea booleană pentru a indica dacă notarea FAO a orizontului a fost notarea inițială utilizată la descrierea orizontului. | Boolean |
3.2.3. Alt tip de notare a orizontului (OtherHorizonNotationType)
O clasificare a orizontului de sol în conformitate cu un sistem specific de clasificare.
Atribute ale tipului de date «OtherHorizonNotationType»
Atribut | Definiție | Tip | Voidability
horizonNotation | Notare care caracterizează orizontul de sol în conformitate cu un sistem specific de clasificare. | OtherHorizonNotationTypeValue |
isOriginalClassification | Valoare booleană care indică dacă notarea FAO a orizontului a fost sistemul inițial de notare utilizat la descrierea orizontului. | Boolean |
3.2.4. Alt tip de nume pentru sol (OtherSoilNameType)
O identificare a profilului de sol în conformitate cu un sistem specific de clasificare.
Atribute ale tipului de date «OtherSoilNameType»
Atribut | Definiție | Tip | Voidability
soilName | Numele profilului de sol în conformitate cu un sistem specific de clasificare. | OtherSoilNameTypeValue |
isOriginalClassification | Valoare booleană pecare indică dacă sistemul de clasificare specificat a fost sistemul de clasificare original utilizat la descrierea profilului. | Boolean |
3.2.5. Particle Size Fraction Type (ParticleSizeFractionType)
Parte a solului care este alcătuită din particule minerale de sol având o dimensiunea din gama dimensiunilor specificate.
Atribute ale tipului de date «ParticleSizeFractionType»
Atribut | Definiție | Tip | Voidability
fractionContent | Procentaj din fracțiunea definită. | Number |
fractionParticleSizeRange | Limitele inferioară și superioară ale dimensiunii particulei fracțiunii definite (exprimată în μm). | RangeType |
3.2.6. Tip de interval (RangeType)
Interval de valori definit de o limită superioară și una inferioară.
Atribute ale tipului de date «RangeType»
Atribut | Definiție | Tip | Voidability
upperValue | Valoarea care definește limita superioară a unei anumite proprietăți. | Real |
lowerValue | Valoarea care definește limita inferioară a unei anumite proprietăți. | Real |
uom | Unitatea de măsură utilizată pentru a exprima valorile intervalului. | UnitOfMeasure |
Constrângeri ale tipului de date «RangeType»
Cel puțin una dintre valori nu trebuie să fie goală.
3.2.7. Tipul de parametru descriptiv al categoriei de sol (SoilThemeDescriptiveParameterType)
Un tip de date care pune la dispoziție o proprietate descriptivă pentru proprietatea legată de sol (categoria de sol) care este reprezentată de «SoilThemeCoverage» său conex.
Atribute ale tipului de date «SoilThemeDescriptiveParameterType»
Atribut | Definiție | Tip | Voidability
soilThemeDescriptiveParameterName | Numele parametrului care să furnizeze informații suplimentare privind valorile «SoilThemeCoverage» conex. | CharacterString |
uom | Unitatea de măsură utilizată pentru a exprima «soilThemeDescriptiveParameter». | UnitOfMeasure |
3.2.8. Tipul de parametru al categoriei de sol (SoilThemeParameterType)
O proprietate legată de sol (categoria de sol) reprezentată de această acoperire. Aceasta este alcătuită dintr-un nume de parametru provenind dintr-o listă de coduri «SoilDerivedObjectParameterNameValue» și o unitate de măsură utilizată la exprimarea parametrului respectiv.
Atribute ale tipului de date «SoilThemeParameterType»
Atribut | Definiție | Tip | Voidability
soilThemeParameterName | Numele parametrului reprezentat de «soilThemeCoverage». | SoilDerivedObjectParameterNameValue |
uom | Unitatea de măsură utilizată pentru a exprima «soilThemeParameter». | UnitOfMeasure |
3.2.9. Tipul grupului de calificativi WRB (WRBQualifierGroupType)
Un tip de date menit să definească grupul unui calificativ și a eventualului (eventualilor) său (săi) specificator(i), locul și poziția sa în ceea ce privește (World Reference Base (WRB) Reference Soil Group (RSG) [Grupul de soluri de referință (RSG) din baza de referință mondială (WRB)] căruia îi aparține în conformitate cu World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.
Atribute ale tipului de date «WRBQualifierGroupType»
Atribut | Definiție | Tip | Voidability
qualifierPlace | Atribut menit să indice amplasarea calificativului în ceea ce privește Grupul de soluri de referință (RSG) din WRB. Acesta poate fi amplasat înaintea RSG, respectiv cu rol de «prefix», sau după RSG, respectiv cu rol de «sufix». | WRBQualifierPlaceValue |
qualifierPosition | Număr menit să indice poziția unui calificativ în ceea ce privește Grupul de referință WRB privind solul căruia îi aparține, precum și în ceea ce privește amplasarea sa față de acesta (RSG), respectiv ca prefix sau sufix. | Integer |
WRBqualifier | Element de nume al WRB, al doilea nivel de clasificare. | WRBQualifierValue |
WRBspecifier | Cod care indică gradul de exprimare a unui calificativ sau intervalul de adâncime căruia i se aplică calificativul. | WRBSpecifierValue |
3.2.10. Tipul de nume al solului conform WRB (WRBSoilNameType)
O identificare a profilului solului în conformitate cu World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.
Atribute ale tipului de date «WRBSoilNameType»
Atribut | Definiție | Tip | Voidability
WRBQualifierGroup | Grupul unui calificativ și eventualul (eventualii) său (săi) specificator(i), locul și poziția sa în ceea ce privește «WRBReferenceSoilGroup» căruia îi aparține. | WRBQualifierGroupType |
WRBReferenceSoilGroup | Primul nivel de clasificare al Bazei mondiale de referință pentru resursele de sol. | WRBReferenceSoilGroupValue |
isOriginalClassification | Valoare booleană menită să indice dacă sistemul de clasificare WRB a fost primul sistem de clasificare care a descris profilul de sol. | Boolean |
Roluri de asociere ale tipului de date «WRBSoilNameType»
Rol de asociere | Definiție | Tip | Voidability
over | O asociere menită să indice faptul că, în cadrul clasificării WRB, un profil de sol.acoperă un alt sol dezvoltat mai vechi | WRBSoilNameType |
3.3. Liste de coduri
3.3.1. FAO Horizon Master (FAOHorizonMasterValue)
O listă de coduri a părții principale a notării orizontului.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în Guidelines for soil description, 4th edition, Food and Agriculture Organization of the United Nations, Rome, 2006, pp. 67-77.
3.3.2. FAO Horizon Subordinate (FAOHorizonSubordinateValue)
O listă de coduri cuprizând desemnări ale distincțiilor și caracteristicilor subordonate din cadrul orizonturilor și straturilor master care au la bază caracteristici de profil observabile pe teren și care sunt aplicate cu ocazia descrierii solului la fața locului.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în Guidelines for soil description, 4th edition, Food and Agriculture Organization of the United Nations, Rome, 2006, pp. 67-77.
3.3.3. FAO Prime (FAOPrimeValue)
Un prim și un prim dublu pot fi utilizați pentru a conota simbolul de orizont principal al celui mai mic dintre două (prim) sau trei (dublu prim) orizonturi având prefixe numerice arabe identice și combinații de litere.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în Guidelines for soil description, 4th edition, Food and Agriculture Organization of the United Nations, Rome, 2006, pp. 67-77.
3.3.4. Alt tip de notare a orizontului (OtherHorizonNotationTypeValue)
O clasificare a orizontului de sol în conformitate cu un sistem specific de clasificare.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
3.3.5. Alt tip de nume pentru sol (OtherSoilNameTypeValue)
O identificare a profilului de sol în conformitate cu un sistem specific de clasificare.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
3.3.6. Starea procesului de geneză a straturilor (LayerGenesisProcessStateValue)
Un indiciu conform căruia procesul specificat în «layerGenesisProcess» este în curs de desfășurare sau a încetat.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valorile pentru lista de coduri «LayerGenesisProcessStateValue»
Valoare | Nume | Definiție
ongoing | în curs de desfășurare | Procesul a început în trecut și este încă activ.
terminated | încheiat | Procesul nu mai este activ.
3.3.7. Tipul de strat (LayerTypeValue)
O clasificare a unui strat în conformitate cu conceptul care se potrivește scopului.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valorile pentru lista de coduri «LayerTypeValue»
Valoare | Nume | Definiție
depthInterval | interval de adâncime | Intervalul fix de adâncime în care este descris solul și/sau sunt prelevate probe.
geogenic | geogenic | Domeniu al profilului de sol compus din materialul care rezultă din același proces nepedogenic, de exemplu sedimentarea, care ar putea indica o neconformitate față de eventuale domenii supraadiacente sau subadiacente.
subSoil | subsol | Material de sol natural aflat sub stratul de sol vegetal și care acoperă materialul-mamă nealterat.
topSoil | strat de sol vegetal | Partea superioară a unui sol natural care are de regulă o culoare închisă și un conținut mai ridicat de materie organică și nutrienți comparativ cu orizonturile (minerale) de sub el, cu excepția stratului de humus.
3.3.8. Nume de parametru de element de profil (ProfileElementParameterNameValue)
Proprietăți despre care se poate observa că definesc elementul de profil.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «ProfileElementParameterNameValue»
Valoare | Nume | Definiție | Parent value
chemicalParameter | parametru chimic | Parametri chimici despre care s-a observat că definesc elementul de profil. |
physicalParameter | parametru fizic | Parametri fizici despre care s-a observat că definesc elementul de profil. |
biologicalParameter | parametru biologic | Parametri biologici despre care s-a observat că definesc elementul de profil. |
organicCarbonContent | conținut de carbon organic | Porțiune a solului, măsurată ca și carbon în forme organice, cu excepția mecarofaunei și a mezofaunei vii și a țesutului vegetal viu. | chemicalParameter
nitrogenContent | conținut de azot | Conținutul total de azot din sol, inclusiv formele organice și anorganice. | chemicalParameter
pHValue | valoare pH | Valoarea pH a elementului de profil. | chemicalParameter
cadmiumContent | conținut de cadmiu | Conținutul de cadmiu al elementului de profil. | chemicalParameter
chromiumContent | conținut de crom | Conținutul de crom al elementului de profil. | chemicalParameter
copperContent | conținut de cupru | Conținutul de cupru al elementului de profil. | chemicalParameter
leadContent | conținut de plumb | Conținutul de plumb al elementului de profil. | chemicalParameter
mercuryContent | conținut de mercur | Conținutul de mercur al elementului de profil. | chemicalParameter
nickelContent | conținut de nichel | Conținutul de nichel al elementului de profil. | chemicalParameter
3.3.9. Numele de parametru de obiect derivat de sol (SoilDerivedObjectParameterNameValue)
Proprietățile legate de sol care pot fi derivate din date privind solul și din alte date.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «SoilDerivedObjectParameterNameValue»
Valoare | Nume | Definiție | Parent value
chemicalParameter | parametru chimic | Parametri chimici care pot fi obținuți din alte date privind solul. |
physicalParameter | parametru fizic | Parametri fizici care pot fi obținuți din alte date privind solul. |
biologicalParameter | parametru biologic | Parametri biologici care pot fi derivați din alte date privind solul. |
potentialRootDepth | adâncime potențială a rădăcinilor | Adâncimea potențială a profilului de sol în care se dezvoltă rădăcini (în cm). | physicalParameter
availableWaterCapacity | capacitatea de apă disponibilă | Cantitatea de apă pe care o poate stoca un sol și care poate fi utilizată de plante, bazată pe adâncimea potențială a rădăcinilor. | physicalParameter
carbonStock | stoc de carbon | Masa totală a carbonului din sol pentru o anumită adâncime. | chemicalParameters
waterDrainage | drenarea apei | Clasa de derenare naturală a apei căreia îi aparține profilul de sol. | physicalParameter
organicCarbonContent | conținut de carbon organic | Porțiune a solului, măsurată ca și carbon în forme organice, cu excepția mecarofaunei și a mezofaunei vii și a țesutului vegetal viu. | chemicalParameter
nitrogenContent | conținut de azot | Conținutul total de azot din sol, inclusiv formele organice și anorganice. | chemicalParameter
pHValue | valoare pH | Valoarea pH a obiectului derivat de sol. | chemicalParameter
cadmiumContent | conținut de cadmiu | Conținutul de cadmiu al obiectului derivat de sol. | chemicalParameter
chromiumContent | conținut de crom | Conținutul de crom al obiectului derivat de sol. | chemicalParameter
copperContent | conținut de cupru | Conținutul de cupru al obiectului derivat de sol. | chemicalParameter
leadContent | conținut de plumb | Conținutul de plumb al obiectului derivat de sol. | chemicalParameter
mercuryContent | conținut de mercur | Conținutul de mercur al obiectului derivat de sol. | chemicalParameter
nickelContent | conținut de nichel | Conținutul de nichel al obiectului derivat de sol. | chemicalParameter
zincContent | conținut de zinc | Conținutul de zinc al obiectului derivat de sol. | chemicalParameter
3.3.10. Scopul prospectării solului (SoilInvestigationPurposeValue)
O listă de coduri cu valori posibile care să indice motivele pentru realizarea prospectării.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «SoilInvestigationPurposeValue»
Valoare | Nume | Definiție
generalSoilSurvey | prospectare generală a solului | Caracterizarea solului cu selectarea imparțială a locației de prospectare.
specificSoilSurvey | prospectare specifică a solului | Investigarea proprietăților solului în locații alese conform unui scop anume.
3.3.11. Tipul de parcelă de sol (SoilPlotTypeValue)
O listă de coduri cu termeni care precizează pe ce tip de Parcelă de solse realizează observarea solului.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «SoilPlotTypeValue»
Valoare | Nume | Definiție
borehole | gaură de foraj | Pătrunderea în subteran însoțită de îndepărtarea de sol/material de rocă, cu utilizarea, de exemplu, a unui instrument gol sub formă de tub, având drept scop realizarea unor descrieri de profil, eșantionare și/sau încercări pe teren.
sample | eșantion | Excavare însoțită de îndepărtarea materialului de sol ca eșantion de sol, fără a se realiza descrierea niciunui profil de sol.
trialPit | puț de prospectare | Excavarea sau orice altă expunere a solului, întrprinsă cu scopul de a realiza descrieri de profil, eșentionare și/sau încercări de teren.
3.3.12. Nume de parametru de profil de sol (SoilProfileParameterNameValue)
Proprietăți despre care se poate observa că definesc profilul de sol.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «SoilProfileParameterNameValue»
Valoare | Nume | Definiție | Parent value
chemicalParameter | parametru chimic | Parametri chimici despre care s-a observat că definesc profilul de sol. |
physicalParameter | parametru fizic | Parametri fizici despre care s-a observat că definesc profilul de sol. |
biologicalParameter | parametru biologic | Parametri biologici despre care s-a observat că definesc profilul de sol. |
potentialRootDepth | adâncime potențială a rădăcinilor | Adâncimea potențială a profilului de sol în care se dezvoltă rădăcini (în cm). | physicalParameter
availableWaterCapacity | capacitatea de apă disponibilă | Cantitatea de apă pe care o poate stoca un sol și care poate fi utilizată de plante, bazată pe adâncimea potențială a rădăcinilor. | physicalParameter
carbonStock | stoc de carbon | Masa totală a carbonului din sol pentru o anumită adâncime. | chemicalParameters
waterDrainage | drenarea apei | Clasa de drenare naturală internă a apei din profilul de sol. | physicalParameter
3.3.13. Numele de parametru de sit al solului (SoilSiteParameterNameValue)
Proprietăți despre care se poate observa că definesc situl de sol.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Valori pentru lista de coduri «SoilSiteParameterNameValue»
Valoare | Nume | Definiție
chemicalParameter | parametru chimic | Parametri chimici despre care s-a observat că definesc situl de sol.
physicalParameter | parametru fizic | Parametri fizici despre care s-a observat că definesc situl de sol.
biologicalParameter | parametru biologic | Parametri biologici despre care s-a observat că definesc situl de sol.
3.3.14. Locul calificativului WRB (WRBQualifierPlaceValue)
O listă de coduri cu valori care indică plasarea calificativului ținând cont de Grupul de soluri de referință WRB. Acesta poate fi amplasat înaintea RSG, respectiv cu rol de «prefix», sau după RSG, respectiv cu rol de «sufix».
Valorile permise pentru această listă de coduri includ doar valorile «prefix» și «sufix», în conformitate cu regulile de stabilire a numelui specificate în World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.
3.3.15. Calificativi WRB (WRBQualifierValue)
O listă de coduri ale calificativelor posibile existente în Baza mondială de referință pentru resursele de soluri.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.
3.3.16. Grupul de soluri de referință (RSG) din WRB (WRBReferenceSoilGroupValue)
O listă de coduri ale posibilelor grupuri de soluri de referință (adică primul nivel de clasificare al Bazei mondiale de referință pentru resursele de sol).
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.
3.3.17. Specificatori WRB (WRBSpecifierValue)
O listă de coduri ale posibililor specificatori.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în World reference base for soil resources 2006, first update 2007, World Soil Resources Reports No. 103, Food and Agriculture Organization of the United Nations, Rome, 2007.
3.4. Cerințe specifice categoriei
| (1) | Valorile din listele de coduri ierarhice de prim nivel «ProfileElementParameterNameValue», «SoilDerivedObjectParameterNameValue», «SoilProfileParameterNameValue», «SoilSiteParameterNameValue» («chemicalParameter», «biologicalParameter», «physicalParameter») servesc doar structurării; se vor utiliza doar valori de nivel inferior.
| (2) | Atunci când este nevoie de un parametru descriptiv suplimentar pentru obiectul derivat de sol, se utilizează atributul de parametru al tipului de obiect spațial «OM_Observation».
| (3) | Pentru un set de date trebuie să se utilizeze doar o clasificare «Alt tip de notare a orizontului».
| (4) | Pentru un set de date trebuie să se utilizeze doar o clasificare «Alt tip de nume al solului».
3.5. Straturi
Straturi pentru categoria de date spațiale «Soil»
Numele stratului | Titlul stratului | Tip de obiect spațial
SO.SoilBody | Soluri | SoilBody
SO.ObservedSoilProfile | Profiluri de sol observat | ObservedSoilProfile, SoilPlot
SO.SoilSite | Situri ale solului | SoilSite
SO.<ValoaredinListadeCoduri>(1) | <nume lizibil de către om> | SoilDerivedObject (basePhenomenon: SoilDerivedObjectParameterNameValue)
Exemplu: Conținut de carbon organic | Exemplu: SO. OrganicCarbonContent |
SO.<ValoaredinListadeCoduri>Acoperire(2) | <nume lizibil de către om> | SoilThemeCoverage (soilThemeParameter / soilThemeParameterName: SoilDerivedObjectParameterNameValue)
Exemplu: SO. OrganicCarbonContentCoverage | Exemplu: Acoperirea conținutului de carbon organic
4. UTILIZAREA TERENULUI (LAND USE)
4.1. Definiții
Pe lângă definițiile stabilite în articolul 2, se aplică următoarele definiții:
(1) «utilizare existentă a terenului» (existing land use) înseamnă o descriere obiectivă a utilizării și funcțiilor unui teritoriu, astfel cum a fost și este în continuare în realitate.
(2) «utilizare caroiată existentă a terenului» (gridded existing land use) înseamnă o descriere obiectivă sub forma unui caroiaj (imagine) regulat ortorectificat a utilizării și funcțiilor unui teritoriu, astfel cum au fost și sunt în continuare în realitate.
(3) «sistem de clasificare ierarhică INSPIRE a utilizării terenului (HILUCS)» [Hierarchical INSPIRE Land Use Classification System (HILUCS)] înseamnă un sistem de clasificare pe mai multe niveluri pentru utilizarea terenului, al cărui utilizare este obligatorie la nivelul cel mai adecvat.
(4) «unitate minimă de interes» (minimum unit of interest) înseamnă cea mai mică suprafață poligonală pentru obiectele utilizării terenului luate în considerare în cadrul setului de date.
(5) «utilizare planificată a terenului» (planned land use) înseamnă planuri spațiale, definite de autoritățile reponsabile cu planificarea spațială, care descriu posibila utilizare în viitor a terenului.
(6) «utilizare eșantionată existentă a terenului» (sampled existing land use) înseamnă o descriere obiectivă a utilizării și a funcțiilor unui teritoriu [precum au fost și sunt în continuare] în realitate, astfel cum s-a observat într-o locație eșantionată.
(7) «zonare» (zoning) înseamnă o divizare în care este descrisă utilizarea planificată a terenului, explicitându-se astfel drepturile și interdicțiile referitoare la noi construcții, care se aplică în cadrul fiecărui element al diviziunii.
4.2. Structura categoriei de date spațiale «Utilizarea terenului»
Tipurile indicate pentru categoria de date spațiale «Acoperirea terenului» sunt organizate în următoarele pachete:
— Nomenclatorul utilizării terenului (Land Use Nomenclature)
— Utilizare existentă a terenului (Existing land use)
— Utilizare caroiată existentă a terenului (Gridded existing land use)
— Utilizare eșantionată existentă a terenului (Sampled existing land use)
— Utilizarea planificată a terenului (Planned land use)
4.3. Nomenclatorul utilizării terenului
4.3.1. Tipuri de date
4.3.1.1. Procentaj HILUCS (HILUCSPercentage)
Procentaj al obiectului utilizării terenului acoperit de această prezență HILUCS.
Atribute ale tipului de date «HILUCSPercentage»
Atribut | Definiție | Tip | Voidability
hilucsValue | Categoria HILUCS pentru acest procentaj HILUCS. | HILUCSValue |
percentage | Procentaj al obiectului utilizării terenului acoperit de această prezență HILUCS. | Integer |
4.3.1.2. Prezență HILUCS (HILUCSPresence)
Prezența uneia sau a mai multor valori HILUCS într-o zonă, indicată fie ca procentajul acoperit pentru fiecare valoare, fie ca valorile enumerate în ordinea importanței lor.
Acest tip este o uniune.
Atribute ale tipului de uniune «HILUCSPresence»
Atribut | Definiție | Tip | Voidability
orderedList | listă ordonată a prezenței valorii utilizării terenului | HILUCSValue |
percentageList | lista procentajului din valoarea utilizării terenului | HILUCSPercentage |
4.3.1.3. Procentaj specific (SpecificPercentage)
Procentajul dintr-un obiect al utilizării terenului acoperit de o prezență specifică.
Atribute ale tipului de date «SpecificPercentage»
Atribut | Definiție | Tip | Voidability
specificValue | Categorie specifică a valorii pentru acest procentaj specific. | LandUseClassificationValue |
percentage | Procentajul dintr-un obiect al utilizării terenului acoperit de această prezență specifică. | Integer |
4.3.1.4. Prezență specifică (SpecificPresence)
Prezența uneia sau a mai multor valori de clasificare a utilizării terenului dintr-o zonă, în conformitate cu lista de coduri pusă la dispoziție de furnizorul de date, indicată fie ca procentajul acoperit pentru fiecare valoare sau valori enumerate în ordinea importanței lor.
Acest tip este o uniune.
Atribute ale tipului de uniune «SpecificPresence»
Atribut | Definiție | Tip | Voidability
orderedList | listă ordonată a valorii utilizării terenului | LandUseClassificationValue |
percentageList | lista procentajului din valoarea utilizării terenului | SpecificPercentage |
4.3.2. Liste de coduri
4.3.2.1. HILUCS (HILUCSValue)
Listă a categoriilor de utilizare a terenului care se utilizează în Utilizarea terenului INSPIRE.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «HILUCSValue»
Valoare | Nume | Definiție | Parent value
1_PrimaryProduction | producție primară | Sunt incluse zonele în care industriile producătoare agregă, ambalează, purifică sau procesează produsele primare în apropierea producătorilor primari, în special dacă materiile prime sunt neadecvate pentru comercializare sau dacă este prea dificil să fie transportate pe distanțe lungi. |
1_1_Agriculture | agricultură | Producția de culturi (plante, ciuperci, etc.) și de produse de origine animală în vederea fabricării de alimente, al comercializării, al consumului propriu sau în scopuri industriale. Sunt incluse instalații pentru biocombustibili și creșterea culturilor în câmp deschis, precum și în sere. De asemenea, în această categorie intră și terenurile scoase temporar din circuitul agricol în cadrul rotației culturilor. Este inclusă și pregătirea produselor pentru piețele primare, lucrările de construcție pe teren (de exemplu terasarea terenului agricol, drenarea, pregătirea câmpurilor de orez), precum și lucrările de îngrijire și întreținere a peisajului. | 1_PrimaryProduction
1_1_1_CommercialAgriculturalProduction | producție agricolă comercială | Teren arabil, culturi permanente și pășuni în scopuri agricole (atât semănate, cât și fânțe naturale). Produsele pot fi utilizate pentru hrana umană sau animală sau pentru producția de bioenergie. | 1_1_Agriculture
1_1_2_FarmingInfrastructure | infrastructură agricolă | Clădiri aferente exploatațiilor agricole, infrastructură de creștere a animalelor (adăposturi pentru animale și infrastructura de procesare aparținând fermelor), clădiri de depozitare a gunoiului de grajd și alte tipuri de infrastructură agricolă (de exemplu clădiri legate de activitățile de manipulare a instalațiilor și de procesare desfășurate în cadrul exploatațiilor agricole). | 1_1_Agriculture
1_1_3_AgriculturalProductionForOwnConsumption | producție agricolă pentru consumul propriu | Cultivarea de plante sau creșterea de animale pentru consumul propriu (grădini de zarzavat, grajduri private pentru animale etc.) | 1_1_Agriculture
1_2_Forestry | silvicultură | Producția de lemn rotund și de alte produse primare pe bază de lemn. Pe lângă producția de lemn, activitățile forestiere au drept rezultat produse care sunt supuse unei procesări minime, cum ar fi lemnul de foc, mangalul și lemnul rotund utilizate într-o formă neprelucrată (de exemplu proptele pentru susținere, lemnul pentru celuloză etc.). Sunt incluse, de asemenea, pepinierele de arbori de pădure, zonele de depozitare și de transport legate de exploatarea forestieră, arborii și plantele lemnoase pentru biocombustibili. Aceste activități pot fi desfășurate în pădurile naturale sau cultivate. | 1_PrimaryProduction
1_2_1_ForestryBasedOnShortRotation | silvicultură pe bază de rotație scurtă | Zone forestiere în care perioada de rotație a unei generații de arbori este de cel mult 50 de ani, după care pădurea este regenerată natural sau artificial prin plantare sau însămânțare. Plantațiile de arbori (producția de lemn pentru celuloză) și lemnul utilizat pentru producția de biomasă aparțin de asemenea acestei categorii. | 1_2_Forestry
1_2_2_ForestryBasedOnIntermediateOrLongRotation | silvicultură bazată pe rotație medie sau lungă | Zone forestiere în care perioada de rotație a unei generații de arbori este de peste 50 de ani, după care pădurea este regenerată natural sau artificial prin plantare sau însămânțare. | 1_2_Forestry
1_2_3_ForestryBasedOnContinuousCover | silvicultură bazată pe acoperire continuă | Zone forestiere în care gestionarea și regenerarea pădurilor se bazează pe creșterea continuă a arborilor. | 1_2_Forestry
1_3_MiningAndQuarrying | exploatare minieră și exploatare în carieră | Exploatare minieră și exploatare în carieră sub forma extracției de minerale și materiale prezente în mod natural ca solide (cărbune, minereuri, pietriș, nisip, sare), lichide (petrol), gaze (gaze naturale) sau biomasă (turbă). Extracția se poate realiza prin diferite metode, cum ar fi mineritul sau exploatarea în carieră subterană sau de suprafață, exploatarea puțurilor etc. | 1_PrimaryProduction
1_3_1_MiningOfEnergyProducingMaterials | exploatarea minieră a materialelor producătoare de energie | Exploatarea minieră și extracția de cărbune, lignit, turbă, petrol, gaze naturale, uraniu și toriu. | 1_3_MiningAndQuarrying
1_3_2_MiningOfMetalOres | exploatarea minieră a minereurilor metalifere | Exploatarea minieră a fierului și a altor metale neferoase (cu excepția uraniului și a toriului). | 1_3_MiningAndQuarrying
1_3_3_OtherMiningAndQuarrying | alte activități de exploatare minieră și exploatare în carieră | Exploatarea în carieră de piatră, nisip, argilă, substanțe chimice, îngrășăminte minerale, producția de sare și alte activități de exploatare minieră și de exploatare în carieră. | 1_3_MiningAndQuarrying
1_4_AquacultureAndFishing | acvacultură și pescuit | Pescuit și acvacultură profesionale. | 1_PrimaryProduction
1_4_1_Aquaculture | aquaculture | Crescătorii de pește și situri de creștere. | 1_4_AquacultureAndFishing
1_4_2_ProfessionalFishing | pescuit profesionist | Zone cu apă utilizate pentru pescuitul profesionist. | 1_4_AquacultureAndFishing
1_5_OtherPrimaryProduction | alte producții primare | Vânătoare profesionistă, colectarea de produse forestiere nelemnoase care cresc în natură, creșterea animalelor migratoare și orice alte producții primare neincluse în valorile «1_1_Agriculture», «1_2_Forestry», «1_3_MiningAndQuarrying», «1_4_AquacultureAndFishing» sau oricare din valorile lor mai restrânse. | 1_PrimaryProduction
1_5_1_Hunting | vânătoare | Vânătoare profesionistă. Zonele pot fi îngrădite sau deschise. | 1_5_OtherPrimaryProduction
1_5_2_ManagementOfMigratoryAnimals | gestionarea animalelor migratoare | Îngrijirea și hrănirea animalelor migratoare, precum reni și cervide. | 1_5_OtherPrimaryProduction
1_5_3_PickingOfNaturalProducts | culegerea de produse naturale | Culegerea de produse naturale nelemnoase, cum ar fi bacele necultivate, mușchi, lichenii etc.) în scopuri comerciale. | 1_5_OtherPrimaryProduction
2_SecondaryProduction | producție secundară | Activități industriale și de fabricare care, cu ajutorul producției provenite din sectorul primar, produc bunuri finite și produse intermediare pentru alte sectoare. Sunt incluse, de asemenea, zonele de depozitare și transport legate direct de activitățile de fabricare. Printre sectoarele industriale acoperite de această categorie se numără: agroalimentar, textil și de pielărie, lemn și produse din lemn, celuloză, hârtie, publicare, tipărire, înregistrare, petrolul și alți combustibili, substanțele chimice, produsele chimice, fibrele artificiale, cauciucul și produsele din plastic, produsele minerale nemetalice, metalele bază și produsele metalice, utilajele și echipamentele, echipamentele electrice și optice, echipamentul de transport și mobilele. |
2_1_RawIndustry | industria de materii prime | Activități industriale responsabile cu transformarea producției provenite din sectorul primar în produse primare fabricate. | 2_SecondaryProduction
2_1_1_ManufacturingOfTextileProducts | fabricarea de produse textile | Pregătirea și filarea fibrelor textile, a ațelor de cusut, țeserea de materiale textile, tăbăcirea și finisarea pieilor. | 2_1_RawIndustry
2_1_2_ManufacturingOfWoodAndWoodBasedProducts | fabricarea lemnului și a produselor pe bază de lemn | Tăierea și rindeluirea lemnului, fabricarea de placaje, contraplacaje, contraplacaje lamelate, panouri din fibre, produse de tâmplărie și dulgherie, produse din plută, paie și produse pentru împletire. | 2_1_RawIndustry
2_1_3_ManufacturingOfPulpPaperAndPaperProducts | industria produselor din celuloză și produse din hârtie | Fabricarea de celuloză, hârtie, carton, bunuri sanitare pe bază de hârtie, tapete. | 2_1_RawIndustry
2_1_4_ManufacturingOfCokeRefinedPetroleumProductsAndNuclearFuel | fabricarea de produse de cocserie, de produse din petrol rafinat și de combustibili nucleari | Fabricarea de produse de cocserie, de produse din petrol rafinat și prelucrarea combustibililor nucleari. | 2_1_RawIndustry
2_1_5_ManufacturingOfChemicalsChemicalProductsManMadeFibers | industria substanțelor chimice, produselor chimice și a fibrelor artificiale | Fabricarea de substanțe chimice de bază, de substanțte agro-chimice, de vopsele, produse farmaceutice, săpun, detergenți, lipiciuri, de alte produse chimice și de fibre artificiale. | 2_1_RawIndustry
2_1_6_ManufacturingOfBasicMetalsAndFabricatedMetals | industria metalelor industriale și a metalelor | Fabricarea, prelucrarea și turnarea fierului, oțelului și a metalelor neferoase și prețioase industriale. Această categorie include, de asemenea, fabricarea produselor metalice. | 2_1_RawIndustry
2_1_7_ManufacturingOfNonMetallicMineralProducts | fabricarea de produse minerale nemetalice | Fabricarea de sticlă, cărămizi, ceramică, beton, ciment, var, ipsos, tăierea și modelarea rocilor și alte produse minerale nemetalice. | 2_1_RawIndustry
2_1_8_ManufacturingOfRubberPlasticProducts | fabricarea de produse din cauciuc și plastic | Fabricarea de anvelope, tuburi, de ambalaje din materiale plastice și de alte produse din cauciuc și mase plastice. | 2_1_RawIndustry
2_1_9_ManufacturingOfOtherRawMaterials | fabricarea de alte materii prime | Producția de materii prime neincluse în niciuna dintre celelalte valori mai restrânse ale «2_1_rawindustry». | 2_1_RawIndustry
2_2_HeavyEndProductIndustry | industria grea | Fabricarea de produse grele din materii prime. | 2_SecondaryProduction
2_2_1_ManufacturingOfMachinery | industria utilajelor | Fabricarea utilajelor de producție, agricole, forestiere și a altor tipuri de utilaje (cu excepția aeronavelor și a vehiculelor), a armelor, muniției și a aparaturii casnice. | 2_2_HeavyEndProductIndustry
2_2_2_ManufacturingOfVehiclesAndTransportEquipment | fabricarea de vehicule și echipamente de transport | Fabricarea autovehiculelor, aeronavelor, navelor spațiale, vapoarelor, bărcilor, echipament de cale ferată și de tramvai, motocicletelor, bicicletelor și a altor echipamente de transport. | 2_2_HeavyEndProductIndustry
2_2_3_ManufacturingOfOtherHeavyEndProducts | fabricarea altor produse finite grele | Producția de alte produse finite grele neincluse în niciuna dintre celelalte valori mai restrânse ale «2_2_HeavyEndProductIndustry». | 2_2_HeavyEndProductIndustry
2_3_LightEndProductIndustry | industria ușoară | Activități care transformă produsele primare fabricate în produse fabricate ușoare. | 2_SecondaryProduction
2_3_1_ManufacturingOfFoodBeveragesAndTobaccoProducts | fabricarea de băuturi, alimente și produse din tutun | Fabricarea cărnii, a peștelui, a fructelor și a legumelor, a uleiurilor și grăsimilor sau a produselor derivate, a produselor lactate, a produselor de morărit și a produselor din amidon, a furajelor pentru animale, a altor produse alimentare, a băuturilor și a produselor din tutun. | 2_3_LightEndProductIndustry
2_3_2_ManufacturingOfClothesAndLeather | fabricarea de îmbrăcăminte și articole din piele | Fabricarea articolelor de îmbrăcăminte, a hainelor din piele, a accesoriilor, vopsirea blănurilor și fabricarea produselor din blană, a bagajelor, genților, a produselor de marochinărie și a încălțămintei. | 2_3_LightEndProductIndustry
2_3_3_PublishingAndPrinting | industria publicării și a tipăririi | Publicarea și tipărirea de cărți, ziare, reviste și publicarea și reproducerea înregistrărilor sonore. | 2_3_LightEndProductIndustry
2_3_4_ManufacturingOfElectricalAndOpticalEquipment | fabricarea de echipamente electrice și optice | Fabricarea echipamentelor de birou, a calculatoarelor, a motoarelor, generatoarelor, a aparaturii de control și distribuție a energiei electrice, a firelor și cablurilor, a acumulatoarelor, bateriilor, lămpilor, aparatelor radio, televizoarelor, telefoanelor, valvelor și tuburilor electronice, a instrumentelor medicale, optice și de precizie, a ceasurilor și a altor echipamente electrice și optice. | 2_3_LightEndProductIndustry
2_3_5_ManufacturingOfOtherLightEndProducts | fabricarea altor produse finite ușoare | Fabricarea mobilierului, a bijuteriilor, a instrumentelor muzicale, a articolelor sportive, a jocurilor, jucăriilor și a altor produse diverse. | 2_3_LightEndProductIndustry
2_4_EnergyProduction | producția de energie | Producția de energie. | 2_SecondaryProduction
2_4_1_NuclearBasedEnergyProduction | producția de energie pe bază nucleară | Centrale nucleare. | 2_4_EnergyProduction
2_4_2_FossilFuelBasedEnergyProduction | producția de energie pe bază de combustibili fosili | Centrale electrice care utilizează combustibili fosili (cărbune, petrol, gaze naturale, turbă și alți combustibili fosili). | 2_4_EnergyProduction
2_4_3_BiomassBasedEnergyProduction | producție de energie pe bază de biomasă | Centrală electrică cu combustie care utilizează combustibili pe bază de biomasă (lemn și alți combustibili solizi și lichizi pe bază de plante, biogaz și alți biocombustibili). | 2_4_EnergyProduction
2_4_4_RenewableEnergyProduction | producția de energie din surse regenerabile | Hidroenergie, energie solară, eoliană, termică (aero, geo și hidro), maremotrică, energia valurilor și alte tipuri de energie din surse regenerabile (cu excepția energiei din biomasă, care este acoperită de valoarea «2_4_3_BiomassBasedEnergyProduction»). | 2_4_EnergyProduction
2_5_OtherIndustry | alte industrii | Producția de alte produse industriale neincluse în niciuna dintre celelalte valori mai restrânse ale «2_secondaryproduction». | 2_SecondaryProduction
3_TertiaryProduction | producție terțiară | Servicii care reprezintă produse pentru alte întreprinderi și alți consumatori, atât servicii publice, cât și private. Sunt incluse comerțul angro și cu amănuntul, servicii de reparație, hoteluri și restaurante, servicii financiare, servicii imobiliare, servicii de afaceri, servicii de închiriere, administrație publică, servicii de apărare și asigurări sociale, educație, sănătate și asistență socială, precum și alte servicii comunitare, sociale și personale. |
3_1_CommercialServices | servicii comerciale | Furnizarea de servicii comerciale. | 3_TertiaryProduction
3_1_1_WholesaleAndRetailTradeAndRepairOfVehiclesAndPersonalAndHouseholdGoods | comerțul angro și cu amănuntul și reparația autovehiculelor și a bunurilor personale și de uz casnic | Comerțul angro și cu amănuntul de autovehicule, combustibil, materii prime agricole, animale vii, minereuri, metale, substanțe chimice, lemn, utilaje, nave, mobilier, articole de uz casnic, textile, produse alimentare, băuturi, produse din tutun, produse farmaceutice, bunuri la mâna a doua, alte produse, deșeuri și fier vechi. Această categorie cuprinde, de asemenea, repararea vehiculelor, a bunurilor personale și de uz casnic. | 3_1_CommercialServices
3_1_2_RealEstateServices | servicii imobiliare | Furnizarea de servicii imobiliare și de închiriere. | 3_1_CommercialServices
3_1_3_AccommodationAndFoodServices | servicii de cazare și de alimentație publică | Servicii hoteliere, servicii de sate de vacanță, de camping, de restaurant, de bar și servicii de cantină. | 3_1_CommercialServices
3_1_4_OtherCommercialServices | alte servicii comerciale | Alte servicii neincluse în niciuna dintre celelalte valori mai restrânse ale «3_1_CommercialServices», cum ar fi servicii de înfrumusețare și de bunăstare. | 3_1_CommercialServices
3_2_FinancialProfessionalAndInformationServices | servicii financiare, profesionale și de informare | Furnizarea de servicii financiare, profesionale sau de informare. | 3_TertiaryProduction
3_2_1_FinancialAndInsuranceServices | servicii financiare și de asigurări | Furnizarea de servicii bancare, de credit, de asigurare și de alte servicii financiare. | 3_2_FinancialProfessionalAndInformationServices
3_2_2_ProfessionalTechnicalAndScientificServices | servicii profesionale, tehnice și științifice | Consultanță informatică, consultanță în materie de prelucrare de date, cercetare și dezvoltare, consultanță juridică, de contabilitate, gestionarea afacerilor, arhitecturală, inginerie, publicitate, testare, prospectare, precum și alte servicii profesionale. | 3_2_FinancialProfessionalAndInformationServices
3_2_3_InformationAndCommunicationServices | servicii de informare și comunicare | Servicii de publicare, înregistrare sonoră, program TV, producție de filme, de radio, telecomunicații și radiodifuziune, informatice și de prelucrare a datelor. | 3_2_FinancialProfessionalAndInformationServices
3_2_4_AdministrativeAndSupportServices | servicii administrative și de asistență | Servicii de agenție de turism, închiriere, curățare, securitate și alte servicii administrative și de asistență. | 3_2_FinancialProfessionalAndInformationServices
3_2_5_OtherFinancialProfessionalAndInformationServices | alte servicii financiare, profesionale și de informare | Alte servicii financiare, profesionale și de informare neincluse în niciuna dintre celelalte valori mai restrânse ale «3_2_FinancialProfessionalAndInformationServices». | 3_2_FinancialProfessionalAndInformationServices
3_3_CommunityServices | servicii comunitare | Furnizarea de servicii pentru comunitate. | 3_TertiaryProduction
3_3_1_PublicAdministrationDefenceAndSocialSecurityServices | servicii de administrație publică, apărare și de securitate socială | Furnizarea de servicii administrative generice, de apărare, justiție, securitate publică, stingerea incendiilor și servicii obligatorii de securitate socială. | 3_3_CommunityServices
3_3_2_EducationalServices | servicii educaționale | Furnizarea de servicii de educație primară, secundară și înaltă pentru adulți, și alte servicii educaționale. | 3_3_CommunityServices
3_3_3_HealthAndSocialServices | servicii de sănătate și asistență socială | Furnizarea de servicii de sănătate umană și animală, precum și de servicii de asistență socială. | 3_3_CommunityServices
3_3_4_ReligiousServices | servicii religioase | Furnizarea de servicii religioase. | 3_3_CommunityServices
3_3_5_OtherCommunityServices | alte servicii comunitare | Alte servicii comunitare, de exemplu cimitirele. | 3_3_CommunityServices
3_4_CulturalEntertainmentAndRecreationalServices | servicii culturale, de divertisment și de recreare | Furnizarea de servicii culturale, de divertisment și de recreare. | 3_TertiaryProduction
3_4_1_CulturalServices | servicii culturale | Furnizarea de servicii artistice, de bibliotecă, de muzeu, de grădini zoologice și botanice, de situri istorice și alte servicii culturale. | 3_4_CulturalEntertainmentAndRecreationalServices
3_4_2_EntertainmentServices | servicii de divertisment | Servicii de parcuri de distracții, de parcuri tematice, de pariuri și jocuri de noroc, precum și alte servicii de divertisment. | 3_4_CulturalEntertainmentAndRecreationalServices
3_4_3_SportsInfrastructure | infrastructură sportivă | Infrastructură sportivă, precum stadioane, piscine, săli de sport, fitness, stațiuni de schi, terenuri de golf și alte infrastructuri sportive. | 3_4_CulturalEntertainmentAndRecreationalServices
3_4_4_OpenAirRecreationalAreas | zone de recreare în aer liber | Zone de recreare în aer liber, de exemplu parcuri urbane, terenuri de joacă, parcuri naționale, precum și zone naturale utilizate în scopuri recreative. | 3_4_CulturalEntertainmentAndRecreationalServices
3_4_5_OtherRecreationalServices | alte servicii de recreare | Alte servicii de recreare neincluse în nici una dintre celelalte valori mai restrânse ale «3_4_CulturalEntertainmentAndRecreationalServices». | 3_4_CulturalEntertainmentAndRecreationalServices
3_5_OtherServices | alte servicii | Furnizarea de alte servicii neincluse în nici una dintre celelalte valori mai restrânse ale «3_TertiaryProduction». | 3_TertiaryProduction
4_TransportNetworksLogisticsAndUtilities | logistică și utilități ale rețelelor de transport | Infrastructura și rețelele de bază ale societății. Toate celelalte sectoare utilizează infrastructura și rețelele pentru a produce bunuri și servicii, ele fiind totodată vitale pentru zonele rezidențiale. Printre acestea se numără alimentarea cu apă, colectarea apei, tratarea și reciclarea apelor uzate și a deșeurilor, transportul, rețelele, depozitarea și comunicarea. |
4_1_TransportNetworks | rețele de transport | Infrastructura din domeniul transporturilor. | 4_TransportNetworksLogisticsAndUtilities
4_1_1_RoadTransport | transport rutier | Zone utilizate pentru transportul rutier, de exemplu căi rutiere, parcări, stații de benzină. | 4_1_TransportNetworks
4_1_2_RailwayTransport | transport feroviar | Zone utilizate pentru transportul feroviar, de exemplu căile ferate, gările feroviare și stațiile de triaj etc. | 4_1_TransportNetworks
4_1_3_AirTransport | transport aerian | Zone utilizate pentru transportul aerian, de exemplu aeroporturi și servicii conexe. | 4_1_TransportNetworks
4_1_4_WaterTransport | transport pe apă | Zone utilizate pentru transportul pe apă, de exemplu porturi, râuri, docuri și servicii conexe. | 4_1_TransportNetworks
4_1_5_OtherTransportNetwork | alte rețele de transport | Zone utilizate pentru alte transporturi, neincluse în nici una dintre celelalte valori mai restrânse ale «4_1_TransportNetworks». | 4_1_TransportNetworks
4_2_LogisticalAndStorageServices | servicii logistice și de depozitare | Zone utilizate pentru servicii de depozitare și logistice separate (care nu sunt legate direct de sectoarele industriale). | 4_TransportNetworksLogisticsAndUtilities
4_3_Utilities | utilități | Infrastructură aferentă utilităților. | 4_TransportNetworksLogisticsAndUtilities
4_3_1_ElectricityGasAndThermalPowerDistributionServices | Servicii de distribuție a electricității, gazelor și a energiei termice | Zone utilizate pentru distribuția de electricitate, gaz și energie termică, inclusiv conductele folosite pentru transportul de petrol și gaz. | 4_3_Utilities
4_3_2_WaterAndSewageInfrastructure | infrastructura de apă și canalizare | Zone utilizate pentru extracția, colectarea, purificarea, depozitarea și distribuția apei, colectarea și tratarea apelor uzate (inclusiv conductele). | 4_3_Utilities
4_3_3_WasteTreatment | tratarea deșeurilor | Zone utilizate pentru colectarea, tratarea și reciclarea deșeurilor. | 4_3_Utilities
4_3_4_OtherUtilities | alte utilități | Zone utilizate pentru alte utilități, neincluse în nici una dintre celelalte valori mai restrânse ale «4_3_Utilities». | 4_3_Utilities
5_ResidentialUse | utilizare rezidențială | Zone utilizate pentru adăpostirea oamenilor. Formele de adăpostire variază în mod semnificativ între zonele rezidențiale, și în interiorul acestora. Printre aceste Zone se numără locuințele unifamiliale, locuințele rezidențiale multifamiliale sau locuințele mobile din orașe și din zonele rurale, în cazul în care nu sunt legate de producția primară. Se permite utilizarea terenului în condiții de densitate mare și de densitate mică. Această categorie include, de asemenea, zonele rezidențiale combinate cu alte utilizări compatibile, precum și alte zone rezidențiale. |
5_1_PermanentResidentialUse | utilizare rezidențială permanentă | Zone rezidențiale dominate de case unifamiliale înconjurate de grădini și/sau de curți, o combinație de case individuale, semidetașate, case terasate, reședințe citadine, case individuale în linie și de blocuri utilizate ca reședințe permanente. | 5_ResidentialUse
5_2_ResidentialUseWithOtherCompatibleUses | utilizare rezidențială cu alte utilizări compatibile | Zone rezidențiale combinate cu alte utilizări compatibile (de ex. diverse servicii, industrie ușoară etc.). | 5_ResidentialUse
5_3_OtherResidentialUse | alte utilizări rezidențiale | Zone utilizate predominant pentru locuințe temporare (tabere pentru migranți), reședințe de vacanță (căsuțe de vacanță) etc. | 5_ResidentialUse
6_OtherUses | alte utilizări | Zone neincluse în valorile «1_PrimaryProduction», «2_SecondaryProduction»«3_TertiaryProduction»«4_TransportNetworksLogisticsAndUtilities», «5_ResidentialUse transportnetworkslogisticsandutilities», sau în niciuna dintre valorile lor mai restrânse sau Zonele aflate în construcție. |
6_1_TransitionalAreas | zone de tranziție | Zone aflate în construcție. Această categorie este folosită numai pentru utilizarea existentă a terenului și nu pentru utilizarea planificată a terenului. | 6_OtherUses
6_2_AbandonedAreas | zone abandonate | Zone agricole, rezidențiale și industriale, de transport și de infrastructură de bază abandonate. Zona aparține categoriei de zone abandonate dacă nu este în curs de utilizare și nu mai poate fi utilizată în scopul inițial fără lucrări majore de reparație sau renovare. | 6_OtherUses
6_3_NaturalAreasNotInOtherEconomicUse | zone naturale unde nu se practică alte utilizări economice | Zone care sunt în stare naturală și unde nu se practică alte utilizări economice. | 6_OtherUses
6_3_1_LandAreasNotInOtherEconomicUse | zone de uscat unde nu se practică alte utilizări economice | Zone care sunt în stare naturală, de exemplu terenuri împădurite, cu arbuști, pășuni, zone umede, terenuri aride, unde nu se practică nicio altă utilizare socio-economică. Printre acestea se numără zone cu statutul de planificare «zonă naturală». Zonele protejate pot aparține acestei categorii sau, dacă există alte utilizări, și altor categorii. Ariile protejate sunt întotdeauna marcate printr-un statut suplimentar de «zonă protejată». | 6_3_NaturalAreasNotInOtherEconomicUse
6_3_2_WaterAreasNotInOtherEconomicUse | zone cu apă unde nu se practică alte utilizări economice | Zone cu apă unde nu se practică alte utilizări socio-economice. | 6_3_NaturalAreasNotInOtherEconomicUse
6_4_AreasWhereAnyUseAllowed | zone unde se permite orice utilizare | Zone unde se permite orice utilizare în cadrul utilizării planificate a terenului (Planned land use - PLU). | 6_OtherUses
6_5_AreasWithoutAnySpecifiedPlannedUse | zone fără o utilizare planificată specifică | Zone despre care utilizarea planificată a terenului (Planned land use - PLU) nu precizează nicio utilizare, de exemplu zone în afara sferei de acțiune a planului. | 6_OtherUses
6_6_NotKnownUse | utilizare necunoscută | Zone unde utilizarea terenului nu se cunoaște. | 6_OtherUses
4.3.2.2. Clasificarea utilizării terenului (LandUseClassificationValue)
Listăa categoriilor de utilizare a terenului care se utilizează în Utilizarea terenurilor INSPIRE și care sunt aprobate la nivel național sau local.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
4.4. Utilizare existentă a terenului
4.4.1. Tipuri de obiecte spațiale
Pachetul privind utilizarea existentă a terenului conține următoarele tipuri de obiecte spațiale:
— Setul de date privind utilizarea existentă a terenului
— Obiectul utilizării existente a terenului
4.4.1.1. Set de date privind utilizarea existentă a terenului (ExistingLandUseDataSet)
Un set de date privind utilizarea existentă a terenului este o colecție de zone despre care sunt furnizate informații referitoare la utilizările existente (prezente și trecute) ale terenului.
Atribute ale tipului de obiect spațial «ExistingLandUseDataSet»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
extent | Limita uniunii geometrice a tuturor instanțelor tipului de obiect spațial «ExistingLandUseObject». | GM_MultiSurface |
name | Nume al setului de date lizibil de către om. | CharacterString |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care setul de date referitoare la utilizarea existentă a terenului a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care acest set de date referitoare la utilizarea existentă a terenului nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «ExistingLandUseDataSet»
Rol de asociere | Definiție | Tip | Voidability
member | Trimitere la «LandUseObjects» care aparțin acestui «ExistingLandUseDataSet» | ExistingLandUseObject |
4.4.1.2. Obiect al utilizării existente a terenului (ExistingLandUseObject)
Un obiect al utilizării existente a terenului descrie utilizarea terenului unei zone caracterizată de o combinație omogenă de tipuri de utilizare a terenului.
Atribute ale tipului de obiect spațial «ExistingLandUseObject»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Reprezentare geometrică a zonei spațiale acoperită de acest obiect. | GM_MultiSurface |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
hilucsPresence | Prezența efectivă a unei categorii de utilizare a terenului conform HILUCS în cadrul obiectului. | HILUCSPresence | voidable
hilucsLandUse | Categoriile HILUCS de utilizare a terenului care sunt prezente în acest obiect al utilizării existente a terenului. | HILUCSValue |
specificLandUse | Categoria de utilizare a terenului în conformitate cu nomenclatorul specific acestui set de date. | LandUseClassificationValue | voidable
specificPresence | Prezența efectivă a unei categorii de utilizare a terenului în cadrul obiectului. | SpecificPresence | voidable
observationDate | Data observării asociată unei descrieri. | Date | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care fenomenul a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care fenomenul nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «ExistingLandUseObject»
Rol de asociere | Definiție | Tip | Voidability
dataSet | Setul de date referitoare la utilizarea existentă a terenului căruia îi aparține acest obiect al utilizării terenului. | ExistingLandUseDataSet |
4.5. Utilizare a terenului în modul caroiaj
4.5.1. Tipuri de obiecte spațiale
Pachetul privind utilizarea terenului în mod caroiaj conține tipul de obiect spațial «Caroiajul utilizării existente a terenului».
4.5.1.1. Caroiajul utilizării existente a terenului (ExistingLandUseGrid)
Un caroiaj al utilizării existente a terenului este o colecție de pixeli despre care sunt furnizate informații referitoare la utilizările existente (prezente și trecute) ale terenului. Pentru clasificare trebuie să se folosească un sistem HILUCS.
Acest tip este un subtip al «RectifiedGridCoverage».
Atribute ale tipului de obiect spațial «ExistingLandUseGrid»
Atribut | Definiție | Tip | Voidability
name | Nume al setului de date lizibil de către om. | CharacterString |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
extent | Conține extinderea setului de date. | EX_Extent |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Data inițială începând cu care acest caroiaj constituie o reprezentare validă a realității. | DateTime | voidable
validTo | Momentul începând cu care acest caroiaj nu mai constituie o reprezentare validă a realității. | DateTime | voidable
Constrângeri ale tipului de obiect spațial «ExistingLandUseGrid»
Valorile «rangeSet» trebuie să fie de tipul «CategoryOrNilReason».
Intervalul se bazează fie pe HILUCS, fie pe un sistem specific de clasificare a utilizării terenului definit de către furnizorul de date.
4.6. Utilizare eșantionată a terenului
4.6.1. Tipuri de obiecte spațiale
Pachetul privind utilizarea eșantionată a terenului conține următoarele tipuri de obiecte spațiale:
— Eșantion de utilizare existentă a terenului
— Set de date «Utilizarea eșantionată existentă a terenului»
4.6.1.1. Eșantion de utilizare existentă a terenului (ExistingLandUseSample)
Descrierea utilizării existente a terenului din locul respectiv.
Atribute ale tipului de obiect spațial «ExistingLandUseSample»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
location | Locație unde se prelevează eșantionul de utilizare a terenului. | GM_Point |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
hilucsLandUse | Categoriile HILUCS de utilizare a terenului care sunt prezente în eșantionul de utilizare existentă a terenului. | HILUCSValue |
hilucsPresence | Prezența efectivă a unei categorii de utilizare a terenului conform HILUCS în cadrul obiectului. | HILUCSPresence | voidable
specificLandUse | Categoria de utilizare a terenului în conformitate cu nomenclatorul specific acestui set de date. | LandUseClassificationValue | voidable
observationDate | Data observării asociată unei descrieri. | Date | voidable
specificPresence | Prezența efectivă a unei categorii de utilizare a terenului în cadrul obiectului. | SpecificPresence | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care fenomenul a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care fenomenul nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «ExistingLandUseSample»
Rol de asociere | Definiție | Tip | Voidability
dataset | Setul de date căruia îi aparține acest eșantion. | SampledExistingLandUseDataSet |
4.6.1.2. Set de date «Utilizarea eșantionată existentă a terenului» (SampledExistingLandUseDataSet)
Un set de date «Utilizarea eșantionată existentă a terenului» este o colecție de locații despre care sunt furnizate informații referitoare la utilizările existente (prezente și trecute) ale terenului.
Atribute ale tipului de obiect spațial «SampledExistingLandUseDataSet»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
extent | Carcasa convexă a tuturor instanțelor tipului de obiect spațial «ExistingLandUseSample». | GM_MultiSurface |
name | Nume al setului de date lizibil de către om. | CharacterString |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Data inițială începând cu care acest set de date este valabil în realitate. | DateTime | voidable
validTo | Momentul începând cu care setul de date nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «SampledExistingLandUseDataSet»
Rol de asociere | Definiție | Tip | Voidability
member | Trimitere la membrii setului de date privind utilizarea eșantionată existentă a terenului. | ExistingLandUseSample |
4.7. Utilizare planificată a terenului
4.7.1. Tipuri de obiecte spațiale
Pachetul privind utilizarea planificată a terenului conține următoarele tipuri de obiecte spațiale:
— Documentație oficială
— Plan spațial
— Reglementare suplimentară
— Element de zonare
4.7.1.1. Documentație oficială (OfficialDocumentation)
Documentația oficială care alcătuiește planul spațial; poate cuprinde legislația aplicabilă, adaptările, elementele cartografice, elementele descriptive care pot fi asociate cu planul spațial complet, un element de zonare sau o reglementare suplimentară. În unele state membre, reglementarea textuală efectivă va face parte din setul de date (și poate fi inclusă în atributul «regulationText»), în timp ce în alte state membre, textul nu va face parte din setul de date, ci va fi referențiat printr-o trimitere la un document sau la un act juridic. Trebuie să se furnizeze cel puțin una dintre cele trei valori «voidable».
Atribute ale tipului de obiect spațial «OfficialDocumentation»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
legislationCitation | Trimitere la documentul care conține textul reglementării. | LegislationCitation | voidable
regulationText | Textul reglementării. | CharacterString | voidable
planDocument | Citarea de planuri scanate și de desene structurale, care pot fi georeferențiate sau nu. | DocumentCitation | voidable
Constrângeri ale tipului de obiect spațial «OfficialDocumentation»
Cel puțin unul dintre atributele «legislationCitation», «regulationText» sau «planDocument» trebuie populat cu o valoare nenulă (non-void).
4.7.1.2. Plan spațial (SpatialPlan)
Un set de documente care indică o direcție strategică pentru dezvoltarea unei zone geografice date și care prezintă politicile, prioritățile, programele și alocările de terenuri care vor implementa direcția strategică și care influențează distribuția oamenilor și a activităților în spații de diferite scări. Planurile spațiale pot fi elaborate pentru planificarea urbană, planificarea regională, planificarea ecologică, amenajarea peisajului, planurile spațiale naționale sau planificarea spațială la nivelul Uniunii.
Atribute ale tipului de obiect spațial «SpatialPlan»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
extent | Uniune geometrică a tuturor instanțelor obiectului spațial «typesZoningElement» și «SupplementaryRegulation» Atunci când un «SpatialPlan» este compus doar dintr-un document, atributul constă din limita imaginii cartografice care conține informațiile referitoare la utilizarea terenului (adică extinderea hărții utilizării terenului). | GM_MultiSurface |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
officialTitle | Denumirea oficială a planului spațial. | CharacterString |
levelOfSpatialPlan | Nivelul unităților administrative acoperite de plan. | LevelOfSpatialPlanValue |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Data inițială începând cu care acest plan spațial este valabil în realitate. | DateTime | voidable
validTo | Momentul începând cu care planul spațial nu mai există în realitate. | DateTime | voidable
alternativeTitle | Denumirea alternativă (neoficială) a planului spațial. | CharacterString | voidable
planTypeName | Denumirea dată de statul membru tipului de plan. | PlanTypeNameValue |
processStepGeneral | Indicație generală a etapei din procesul de planificare prin care trece în prezent planul. | ProcessStepGeneralValue | voidable
backgroundMap | Identificarea hărții contextuale care a fost utilizată pentru elaborarea acestui plan. | BackgroundMapValue | voidable
ordinance | Trimitere la ordonanța administrativă relevantă. | OrdinanceValue | voidable
Roluri de asociere ale tipului de obiect spațial «SpatialPlan»
Rol de asociere | Definiție | Tip | Voidability
officialDocument | Legătura la documentele oficiale care se referă la planul spațial. | OfficialDocumentation | voidable
member | Trimitere la «ZoningElements» care aparțin acestui «SpatialPlan». | ZoningElement |
restriction | Legături la reglementările suplimentare care oferă informații și/sau care stabilesc restricții privind utilizarea terenului/apei ce vin în completarea zonării ca parte a acestui plan spațial. | SupplementaryRegulation |
4.7.1.3. Reglementare suplimentară (SupplementaryRegulation)
Un obiect spațial (punct, linie sau poligon) al unui plan spațial, care oferă informații suplimentare și/sau prevede restricții privind utilizarea terenului/apei, necesare din motive de planificare spațială sau pentru a formaliza normele externe definite de textul juridic.
Atribute ale tipului de obiect spațial «SupplementaryRegulation»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Geometria suprafeței de teren în cazul căreia se aplică reglementarea suplimentară. | GM_Object |
validFrom | Data inițială începând cu care această versiune a reglementării suplimentare este valabilă în realitate. | DateTime | voidable
validTo | Data începând cu care reglementarea suplimentară nu mai este valabilă. | DateTime | voidable
regulationNature | Natura juridică a reglementării utilizării terenului. | RegulationNatureValue |
specificSupplementaryRegulation | Trimitere la o categorie de reglementare suplimentară prevăzută într-un nomenclator specific de reglementări suplimentare furnizate de furnizorul de date. | SpecificSupplementaryRegulationValue | voidable
supplementaryRegulation | Codul reglementării suplimentare din lista ierarhică de coduri ale reglementărilor suplimentare convenită la nivel european. | SupplementaryRegulationValue |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
processStepGeneral | Indicație generală a etapei din procesul de planificare prin care trece în prezent reglementarea suplimentară. | ProcessStepGeneralValue | voidable
backgroundMap | Identificarea hărții contextuale care a fost utilizată pentru elaborarea reglementării suplimentare. | BackgroundMapValue | voidable
dimensioningIndication | Specificații privind dimensionarea care sunt adăugate la dimensionarea elementelor de zonare care se suprapun cu geometria reglementării suplimentare. | DimensioningIndicationValue | voidable
inheritedFromOtherPlans | Indiciu privind posibilitatea ca reglementarea suplimentară să fie moștenită dintr-un altplan spațial. | Boolean | voidable
specificRegulationNature | Natura juridică a reglementării utilizării terenului dintr-o perspectivă națională. | CharacterString | voidable
name | Denumirea oficială a reglementării suplimentare. | CharacterString | voidable
Roluri de asociere ale tipului de obiect spațial «SupplementaryRegulation»
Rol de asociere | Definiție | Tip | Voidability
officialDocument | Legătura la reglementările textuale care corespund acestei reglementări suplimentare. | OfficialDocumentation | voidable
plan | Legătura la planul din care face parte această reglementare suplimentară. | SpatialPlan |
4.7.1.4. Element de zonare (ZoningElement)
Un obiect spațial care este omogen în ceea ce privește utilizările terenului pe baza unei zonări care separă un set de utilizări ale terenului de un altul.
Atribute ale tipului de obiect spațial «ZoningElement»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Geometria acestui element de zonare. | GM_MultiSurface |
validFrom | Data la care fenomenul a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care fenomenul nu mai există în realitate. | DateTime | voidable
hilucsLandUse | Clasa de utilizare a terenului care ocupă o poziție dominantă în cadrul acestui obiect al utilizării terenului. | HILUCSValue |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
hilucsPresence | Prezența efectivă a unei categorii de utilizare a terenului în cadrul obiectului. | HILUCSPresence | voidable
specificLandUse | Categoria de utilizare a terenului în conformitate cu nomenclatorul specific acestui set de date. | LandUseClassificationValue | voidable
specificPresence | Prezența efectivă a unei categorii de utilizare a terenului în cadrul obiectului. | SpecificPresence | voidable
regulationNature | Natura juridică a indicației de utilizare a terenului. | RegulationNatureValue |
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
processStepGeneral | Indicația generală a etapei din procesul de planificare prin care trece în prezent elementul de zonare. | ProcessStepGeneralValue | voidable
backgroundMap | Identificarea hărții contextuale care a fost utilizată pentru elaborarea acestui element de zonare. | BackgroundMapValue | voidable
dimensioningIndication | Specificații cu privire la dimensionarea dezvoltărilor urbane. | DimensioningIndicationValue | voidable
Roluri de asociere ale tipului de obiect spațial «ZoningElement»
Rol de asociere | Definiție | Tip | Voidability
plan | «SpatialPlan» căruia îi aparține acest «ZoningElement». | SpatialPlan |
officialDocument | Reglementare textuală care face parte din acest element de zonare. | OfficialDocumentation | voidable
4.7.2. Tipuri de date
4.7.2.1. Hartă contextuală (BackgroundMapValue)
Informații privind harta care a fost utilizată ca și context în definirea unui plan spațial, a unui element de zonare sau a unei reglementări suplimentare.
Atribute ale tipului de date «BackgroundMapValue»
Atribut | Definiție | Tip | Voidability
backgroundMapDate | Data hărții contextuale utilizate. | DateTime |
backgroundMapReference | Trimitere la harta contextuală care a fost utilizată. | CharacterString |
backgroudMapURI | URI care face referire la serviciul care furnizează harta contextuală. | URI | voidable
4.7.2.2. Indicație de dimensionare evaluată ca și caracter (DimensioningIndicationCharacterValue)
Indicație de dimensionare a cărei valoare este de tipul «CharacterString».
Acest tip este un subtip al «DimensioningIndicationValue».
Atribute ale tipului de date «DimensioningIndicationCharacterValue»
Atribut | Definiție | Tip | Voidability
value | Valoarea indicațiilor de dimensionare. | CharacterString |
4.7.2.3. Indicație de dimensionare evaluată ca număr întreg (DimensioningIndicationIntegerValue)
Indicație de dimensionare a cărei valoare este de tipul «întreg» (integer).
Acest tip este un subtip al «DimensioningIndicationValue».
Atribute ale tipului de date «DimensioningIndicationIntegerValue»
Atribut | Definiție | Tip | Voidability
value | Valoarea indicațiilor de dimensionare. | Integer |
4.7.2.4. Indicație de dimensionare evaluată ca măsură (DimensioningIndicationMeasureValue)
Indicație de dimensionare a cărei valoare este o măsură (measure).
Acest tip este un subtip al «DimensioningIndicationValue».
Atribute ale tipului de date «DimensioningIndicationMeasureValue»
Atribut | Definiție | Tip | Voidability
value | Valoarea indicațiilor de dimensionare. | Measure |
4.7.2.5. Indicație de dimensionare evaluată ca reală (DimensioningIndicationRealValue)
Indicație de dimensionare a cărei valoare este un număr real.
Acest tip este un subtip al «DimensioningIndicationValue».
Atribute ale tipului de date «DimensioningIndicationRealValue»
Atribut | Definiție | Tip | Voidability
value | Valoarea indicațiilor de dimensionare. | Real |
4.7.2.6. Indicație de dimensionare (DimensioningIndicationValue)
Specificații cu privire la dimensionarea dezvoltărilor urbane.
Atribute ale tipului de date «DimensioningIndicationValue»
Atribut | Definiție | Tip | Voidability
indicationReference | Descriere a indicației de dimensionare. | CharacterString |
4.7.2.7. Ordonanță (OrdinanceValue)
Trimitere la ordonanță administrativă. Ordonanța este un regulament/normă adoptată de o autoritate care este mandatată, din punct de vedere legal, să dea o astfel de ordonanță.
Atribute ale tipului de date «OrdinanceValue»
Atribut | Definiție | Tip | Voidability
ordinanceDate | Data ordonanței administrative relevante. | DateTime |
ordinanceReference | Trimitere la ordonanța administrativă relevantă. | CharacterString |
4.7.3. Liste de coduri
4.7.3.1. Nivelul planului spațial (LevelOfSpatialPlanValue)
Ierarhia teritorială a planului.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «LevelOfSpatialPlanValue»
Valoare | Nume | Definiție
infraLocal | infralocal | Un plan care acoperă doar o parte a unei municipalități.
local | local | Plan la nivel municipal, corespunzătoare unui nivel mai scăzut de administrare echivalent cu LAU2, astfel cum se prevede în anexa III la Regulamentul (CE) nr. 1059/2003 al Parlamentului European și al Consiliului(3).
supraLocal | supralocal | Un plan care cuprinde mai multe municipalități (în întregime sau parțial).
infraRegional | infraregional | Un plan care cuprinde mai multe unități infraadministrative într-o singură regiune administrativă.
regional | regional | Plan la nivel regional [echivalentul NUTS2 al Nomenclatorului EUROSTAT al unităților statistice, astfel cum prevede Regulamentul (CE) nr. 1059/2003].
supraRegional | supraregional | Un plan care cuprinde mai multe regiuni administrative.
national | national | Plan la nivel de stat membru.
other | altele | Alt nivel al planului spațial.
4.7.3.2. Etapă generală a procesului (ProcessStepGeneralValue)
Indicație generală a etapei din procesul de planificare prin care trece în prezent planul.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «ProcessStepGeneralValue»
Valoare | Nume | Definiție
adoption | în curs de adoptare | Plan aflat în curs de adoptare din punct de vedere juridic.
elaboration | în curs de elaborare | Plan aflat în curs de elaborare.
legalForce | obligatoriu din punct de vedere juridic sau activ | Plan deja adoptat și obligatoriu din punct de vedere juridic sau activ.
obsolete | declasat | Plan care a fost înlocuit de un alt plan sau care nu mai este în vigoare.
4.7.3.3. Natura reglementării (RegulationNatureValue)
Natura juridică a indicației de utilizare a terenului.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «RegulationNatureValue»
Valoare | Nume | Definiție
bindingForDevelopers | obligatorie pentru dezvoltatori | Indicația de utilizare a terenului este obligatorie numai pentru entitatea responsabilă cu dezvoltarea unei zone.
bindingOnlyForAuthorities | obligatorie doar pentru autorități | Indicația de utilizare a terenului este obligatorie numai pentru anumite autorități.
generallyBinding | obligatorie în general | Indicația de utilizare a terenului este obligatorie pentru toți cei implicați.
nonBinding | neobligatorie | Indicația de utilizare a terenului nu este obligatorie.
definedInLegislation | definită în legislație | Indicația de utilizare a terenului este definită de legislație.
4.7.3.4. Denumirea tipului de plan (PlanTypeNameValue)
Tipuri de planuri astfel cum sunt definite de statele membre. Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
4.7.3.5. Reglementare suplimentară specifică (SpecificSupplementaryRegulationValue)
Categoria reglementării suplimentare furnizate ca parte a unui nomenclator specific al reglementărilor suplimentare pus la dispoziție de furnizorul de date.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
4.7.3.6. Reglementare suplimentară (SupplementaryRegulationValue)
Tipuri de condiții și constrângeri în ceea ce privește planurile spațiale.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile privind elevația specificate în Ghidul tehnic INSPIRE privind utilizarea terenului.
4.8. Cerințe specifice categoriei
| (1) | Orice set de date privind utilizarea va atribui fiecărui poligon, pixel sau locație un tip de utilizare a terenului din cadrul Sistemului de clasificare ierarhică INSPIRE a utilizării terenului (HILUCS) la cel mai adecvat și mai detaliat nivel ierarhic.
| (2) | Tipul de obiect spațial «CoverageByDomainAndRange» trebuie să fie numai de subtipurile «GridCoverage».
| (3) | În cazul în care o zonă a fost instituită pentru a reglementa utilizarea planificată a terenului și definită în cadrul unui plan spațial obligatoriu din punct de vedere juridic, aceasta intră în sfera de aplicare a categoriei «Utilizarea terenului» și trebuie codificată ca o «SupplementaryRegulation». Cu toate acestea, în cazul în care zona a fost stabilită prin cerință legislativă însă e anu a fost defnită în cadrul unui plan spațial obligatoriu din punct de vedere juridic, aceasta trebuie codificată ca o «ManagementRestrictionOrRegulationZone».
| (4) | Pe baza sistemului de referință de coordonate orizontale INSPIRE, fiecare stat membru definește o proiecție sau un set de proiecții adecvate pentru lucrul cu parcelele cadastrale subiacente pe teritoriul național și în zonele transfrontaliere, după caz, pentru un «SpatialPlan». O proiecție este adecvată dacă ea oferă puține modificări liniare (în mod ideal, mai puțin de 50 cm pe 500 m) și, astfel, le permite utilizatorilor să măsoare suprafețele și distanțele în mod semnificativ. Această proiecție sau set de proiecții trebuie să fie definite în acord cu țările învecinate. Această proiecție sau set de proiecții trebuie să fie bine documentate pentru a permite transformarea din și în sistemul comun de referință de coordonate. Documentația trebuie să fie furnizată în conformitate cu ISO 19111, care prevede modul în care trebuie să fie descris un sistem de referință de coordonate proiectat.
| (5) | Utilizarea elementului comun de metadate «Rezoluție spațială» (Spatial Resolution) [în conformitate cu secțiunea 6.2 din Partea B a anexei la Regulamentul (CE) nr. 1205/2008] este limitată la furnizarea unei distanțe de rezoluție.
| (6) | Furnizorii de date trebuie să includă următoarele cuvinte-cheie în plus față de cuvintele-cheie obligatorii definite în Regulamentul (CE) nr. 1205/2008/CE: (a) Unul dintre următoarele cuvinte-cheie neutre din punct de vedere lingvistic pentru a descrie tipul setului de date privind utilizare terenului: «ExistingLandUse», «SampledExistingLandUse», «GriddedExistingLandUse», «PlannedLandUse». (b) Dacă setul de date conține obiecte «SpatialPlan», un cuvânt-cheie care să descrie nivelul unităților administrative vizate de plan, astfel cum se definește în lista de coduri «LevelOfSpatialPlan».
4.9. Straturi
Straturi pentru categoria de date spațiale «Land Use»
Numele stratului | Titlul stratului | Tip de obiect spațial
LU.ExistingLandUse | Obiecte ale utilizării existente a terenului în conformitate cu sistemul ierarhic de clasificare INSPIRE a utilizării terenului, la nivelul cel mai adecvat | ExistingLandUseObject
LU.SpatialPlan | Extinderea unui plan spațial | SpatialPlan
LU.ZoningElement | Obiecte «zonare» de planificare spațială în conformitate cu sistemul ierarhic de clasificare INSPIRE a utilizării terenului, la nivelul cel mai adecvat | ZoningElement
LU.SupplementaryRegulation | Reglementări care completează zonarea și care afectează utilizarea terenului | SupplementaryRegulation
5. SĂNĂTATE ȘI SIGURANȚĂ UMANĂ (HUMAN HEALTH AND SAFETY)
5.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt specificate pentru categoria de date spațiale «Sănătate umană și siguranță»:
— Date statistice privind sănătatea
— Marker biologic
— Boală
— Statistica stării generale de sănătate
— Statistica serviciilor de sănătate
— Valoare măsurată a factorului de mediu determinant al stării de sănătate
— Date statistice referitoare la factorii de mediu determinanți ai stării de sănătate
5.1.1. Date statistice privind sănătatea (HealthStatisticalData)
Date legate de sănătatea umană, de la date privind bolile înregistrate și problemele de sănătate conexe (în conformitate cu listele de coduri acceptate la nivel internațional, cum ar fi ICD-10), exprimate ca morbiditate și mortalitate, la date privind starea generală de sănătate (BMI, percepția sănătății proprii etc.), date privind serviciile de sănătate (cheltuieli de sănătate, cazuri zilnice etc.), precum și date privind markerii biologici; toate acestea sunt indici statistici agregați la diferite unități statistice, colectați/raportați în diverse grupuri de populație. Includerea datelor de biomonitorizare umană oferă ocazia de a explora potențialele legături directe sau indirecte între sănătatea umană și mediu.
Acest tip este abstract.
Roluri de asociere ale tipului de obiect spațial «HealthStatisticalData»
Rol de asociere | Definiție | Tip | Voidability
aggregationUnit | Unitate statistică la care se referă datele statistice privind sănătatea. | StatisticalUnit |
5.1.2. Marker biologic (Biomarker)
Un marker biologic (al expunerii) reprezintă concentrația unei substanțe chimice, a metabolitului său sau este produsul unei interacțiuni dintre o substanță chimică și o anumită moleculă sau celulă țintă măsurată într-un compartiment al unui organism.
Acest tip este un subtip al «HealthStatisticalData».
Atribute ale tipului de obiect spațial «Biomarker»
Atribut | Definiție | Tip | Voidability
biomarkerName | Acesta este identificatorul unic pentru un marker biologic, furnizând informații privind substanța chimică determinantă și matricea în care a fost determinată substanța respectivă. | BiomarkerType |
biomarkerStatisticalParameter | Sinteza statistică a unui studiu de biomonitorizare umană, reprezentând cele mai importante caracteristici statistice ale unui marker biologic măsurate în cadrul studiului în cauză. | BiomarkerStatisticalParameterType |
referencePeriod | Perioada de timp la care sunt referențiate datele. | ReferencePeriodType |
ageRange | Intervalul de vârstă al unei subpopulații specifice exprimat ca vârsta de început și un interval, exprimat în mod alternativ în ani, luni sau săptămâni. | AgeRangeType |
gender | Genul populației analizate. | GenderValue |
Roluri de asociere ale tipului de obiect spațial «Biomarker»
Rol de asociere | Definiție | Tip | Voidability
refersTo | datele privind markerii biologici descrise de metadate | BiomarkerThematicMetadata |
5.1.3. Boală (Disease)
Informații statistice referitoare la patologii legate direct sau indirect de calitatea mediului.
Acest tip este un subtip al «HealthStatisticalData».
Atribute ale tipului de obiect spațial «Disease»
Atribut | Definiție | Tip | Voidability
ageRange | Intervalul de vârstă al unei subpopulații specifice exprimat ca vârsta de început și un interval, exprimat în mod alternativ în ani, luni sau săptămâni. | AgeRangeType | voidable
diseaseMeasure | Diferite moduri de raportare a datelor privind bolile și problemele de sănătate conexe ale unei populații. | DiseaseMeasure |
gender | Genul populației analizate. | GenderValue | voidable
referencePeriod | Perioada de timp la care sunt referențiate datele. | ReferencePeriodType |
pathology | Tipul patologiei. | ICDValue |
COD | Date privind cauzele de deces (COD) care oferă informații privind structura mortalității pe cauze de boală și care constituie un element major al informațiilor din domeniul sănătății publice. | CODValue |
Constrângeri ale tipului de obiect spațial «Disease»
Atributul «COD» trebuie furnizat numai dacă atributul «diseaseMeasureType» al lui «diseaseMeasure» are o valoare care reprezintă mortalitate.
Cel puțin unul dintre atributele patologie și «COD» nu trebuie să fie goale.
5.1.4. Statistica stării generale de sănătate (GeneralHealthStatistics)
Cifre cu privire la unele aspecte ale sănătății unei populații sau unei zone. În scopul acestui model de date, datele privind «starea generală de sănătate» cuprind aspecte precum percepția sănătății proprii, distribuția demografică a diverselor probleme de sănătate, fumătorii etc., exprimate ca numere, ponderi și procentaje neprelucrate, structurate în funcție de sex, vârstă și/sau alți factori socio-economici, culturali, etnici sau de altă natură.
Acest tip este un subtip al «HealthStatisticalData».
Atribute ale tipului de obiect spațial «GeneralHealthStatistics»
Atribut | Definiție | Tip | Voidability
ageRange | Intervalul de vârstă al unei subpopulații specifice exprimat ca vârsta de început și un interval, exprimat în mod alternativ în ani, luni sau săptămâni. | AgeRangeType | voidable
gender | Genul populației analizate. | GenderValue | voidable
generalHealthName | Indicatorul stării de sănătate. | GeneralHealthTypeValue |
generalHealthValue | O exprimare numerică exprimare a unui indice/indicator de sănătate. | Real |
referencePeriod | Perioada de timp la care sunt referențiate datele. | ReferencePeriodType |
5.1.5. Statistica serviciilor de sănătate (HealthServicesStatistic)
Date statistice privind îngrijirea sănătății sau serviciile de sănătate referitoare la nivelele NUTS 1 și NUTS 2 și nivelul comunal.
Acest tip este un subtip al «HealthStatisticalData».
Atribute ale tipului de obiect spațial «HealthServicesStatistic»
Atribut | Definiție | Tip | Voidability
healthServiceType | Tip de servicii de sănătate. | HealthServicesTypeValue |
healthServiceValue | Numărul serviciilor de sănătate analizate. | Real |
referencePeriod | Perioada de timp la care sunt referențiate datele. | ReferencePeriodType |
5.1.6. Valoarea măsurată a factorului de mediu determinant al stării de sănătate (EnvHealthDeterminantMeasure)
O măsurare grosieră efectuată într-un loc de interes pentru analiza factorului de sănătate umană.
Atribute ale tipului de obiect spațial «EnvHealthDeterminantMeasure»
Atribut | Definiție | Tip | Voidability
location | Localizarea măsurării. | GM_Object |
type | Tipul factorului de mediu determinant al stării de sănătate. | EnvHealthDeterminantTypeValue |
measureTime | Perioada de timp când a fost efectuată măsurarea. | TM_Period |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care informațiile vor începe să fie utilizate. | DateTime | voidable
validTo | Momentul în care informațiile vor înceta să fie utilizate. | DateTime | voidable
5.1.7. Date statistice referitoare la factorii de mediu determinanți ai stării de sănătate (EnvHealthDeterminantStatisticalData)
Date statistice care prezintă interes pentru analiza factorului de sănătate umană, care rezultă din agregarea măsurătorilor efectuate în cadrul unei unități statistice.
Acest tip este un subtip al «HealthStatisticalData».
Atribute ale tipului de obiect spațial «EnvHealthDeterminantStatisticalData»
Atribut | Definiție | Tip | Voidability
statisticalMethod | Tipul de metodă statistică utilizată pentru agregarea datelor neprelucrate ale măsurătorilor privind unitatea statistică. | StatisticalAggregationMethodValue |
type | Tipul factorului de mediu determinant al stării de sănătate. | EnvHealthDeterminantTypeValue |
Roluri de asociere ale tipului de obiect spațial «EnvHealthDeterminantStatisticalData»
Rol de asociere | Definiție | Tip | Voidability
measure | Măsurile | Measure |
5.2. Tipuri de date
5.2.1. Vârstă (Age)
Vârsta persoanelor poate fi exprimată în diverse moduri (de exemplu ani pentru adulți, luni sau săptămâni pentru sugari).
Acest tip este o uniune.
Atribute ale tipului uniune «Age»
Atribut | Definiție | Tip | Voidability
month | Perioadă de timp. | Integer |
week | Perioadă de timp. | Integer |
year | Perioadă de timp. | Integer |
5.2.2. Intervalul de vârstă (AgeRangeType)
Intervalul de vârstă al unei subpopulații specifice exprimat ca vârsta de început și un interval, exprimat în mod alternativ în ani, luni sau săptămâni.
Atribute ale tipului de date «AgeRangeType»
Atribut | Definiție | Tip | Voidability
startAge | Începutul intervalului de vârstă. | Age |
range | Durata intervalului de vârstă. | Age |
5.2.3. Parametrul statistic al markerilor biologici (BiomarkerStatisticalParameterType)
Un set de caracteristici statistice ale unui marker biologic măsurate pentru un marker biologic specific.
Atribute ale tipului de date «BiomarkerStatisticalParameterType»
Atribut | Definiție | Tip | Voidability
geometricMean | Media geometrică. | Measure |
CI95ofGM | Interval de încredere de 95 % din media geometrică. | Measure |
P50 | A 50-a percentilă sau valoarea medie. Valoare sub care se regăsesc 50 % din observații. | Measure |
P90 | A 90-a percentilă. Valoare sub care se regăsesc 90 % din observații. | Measure |
P95 | A 95-a percentilă. Valoare sub care se regăsesc 95 % din observații. | Measure |
CI95ofP95 | Interval de încredere de 95 % din a 95-a percentilă. | Measure |
maximum | Cea mai mare valoare a markerilor biologici determinată într-un participant individual în cadrul unui studiu de biomonitorizare. | Measure |
pinLOD | Proporția persoanelor fizice cu niveluri nedetectabile ale parametrului testat (sub limita de detecție). | Real |
LOQ | Limita de cuantificare. | Real |
numberOfParticipants | Numărul participanților care au furnizat probe ce au contribuit la calcularea parametrului statistic privind markerii biologici. | Integer |
5.2.4. Metadate tematice privind markerii biologici (BiomarkerThematicMetadata)
Metadate tematice care descriu scopul studiului, populația țintă și caracteristica domeniilor studiate.
Atribute ale tipului de date «BiomarkerThematicMetadata»
Atribut | Definiție | Tip | Voidability
studyType | Obiectivul studiului (pe bază de ipoteze, anchetă generală a populației, oportunist), atunci când aceste opțiuni sunt predefinite. | PT_FreeText |
areaType | Caracteristicile zonei de eșantionare (urbană, rurală, semi-urbană) atunci când aceste opțiuni sunt predefinite într-un studiu de biomonitorizare umană. | PT_FreeText |
specificSubPopulation | Caracteristicile populației incluse în eșantion în ceea ce privește vârsta, sexul, precum și alte caracteristici ale populației atunci când aceste opțiuni sunt predefinite într-un studiu de biomonitorizare umană. | PT_FreeText |
meanAge | Vârsta medie a subpopulației specifice. | Age |
Roluri de asociere ale tipului de date «BiomarkerThematicMetadata»
Rol de asociere | Definiție | Tip | Voidability
describedBy | Metadatele care sunt legate de datele privind markerii biologici | Biomarker |
5.2.5. Tipul de markeri biologici (BiomarkerType)
Un marker biologic este definit atât de o substanță chimică cuantificată sau determinată (de exemplu cadmiu, plumb), cât și de metabolitul său și de o matrice (de exemplu sânge, urină) utilizate în vederea cuantificării; de exemplu - cadmiu în urină, plumb în sânge.
Atribute ale tipului de date «BiomarkerType»
Atribut | Definiție | Tip | Voidability
chemical | Identificarea compusului după nume sau abreviere, formulă chimică, numărul CAS-PubChem sau orice alt număr care este cuantificat prin măsurare. | ChemicalValue |
matrix | Tipul materialului biologic sau al compartimentului organismului din care sunt prelevate eșantioane pentru a determina sau cuantifica un marker biologic. | MatrixValue |
5.2.6. Valoare măsurată a bolii (DiseaseMeasure)
Diferite moduri de raportare a datelor privind bolile și problemele de sănătate conexe ale unei populații.
Atribute ale tipului de date «DiseaseMeasure»
Atribut | Definiție | Tip | Voidability
diseaseMeasureType | Diferite moduri de raportare a datelor privind bolile și problemele de sănătate conexe ale unei populații. | DiseaseMeasureTypeValue |
value | Valoarea indicatorului măsurat al bolii. | Real |
5.2.7. Perioada de referință (ReferencePeriodType)
Perioada de timp la care se referă datele.
Atribute ale tipului de date «ReferencePeriodType»
Atribut | Definiție | Tip | Voidability
startDate | Începutul perioadei de referință. | Date |
endDate | Sfârșitul perioadei de referință. | Date |
5.2.8. Măsura concentrației (Concentration)
O măsură a concentrației în care se găsește o anumită componentă într-un mediu specificat.
Acest tip este un subtip al «Measure».
Atribute ale tipului «Concentration»
Atribut | Definiție | Tip | Voidability
uom | Unitatea de măsură. | UomConcentration |
5.2.9. Unitate de măsură pentru concentrație (UomConcentration)
O unitate de măsură pentru concentrația unei anumite componente într-un mediu specificat.
Acest tip este un subtip al «UnitOfMeasure».
Atribute ale tipului «UomConcentration»
Atribut | Definiție | Tip | Voidability
component | Componenta a cărei concentrație se măsoară. | ComponentTypeValue |
media | Factorul de mediu în care se măsoară concentrația. | MediaTypeValue |
5.2.10. Măsură a zgomotului (NoiseMeasure)
O măsură a intensității zgomotului.
Acest tip este un subtip al «Measure».
Atribute ale tipului «NoiseMeasure»
Atribut | Definiție | Tip | Voidability
uom | O unitate de măsură pentru intensitatea zgomotului. | UomNoise |
5.2.11. Unitate de măsură a zgomotului (UomNoise)
O unitate de măsură pentru intensitatea zgomotului.
Acest tip este un subtip al «UnitOfMeasure».
Atribute ale tipului «UomNoise»
Atribut | Definiție | Tip | Voidability
source | Tipul sursei de zgomot. | NoiseSourceTypeValue |
5.3. Liste de coduri
5.3.1. Cauza de deces (CODValue)
Date privind cauzele de deces (COD) care oferă informații privind tiparele de mortalitate și care constituie un element major al informațiilor din domeniul sănătății publice.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în Lista europeană a cauzelor de deces publicată de Eurostat.
5.3.2. Substanță chimică (ChemicalValue)
Denumirea substanței chimice.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.3. Tipul componentei de mediu a sănătății (ComponentTypeValue)
Un tip special de componentă (substanță chimică, specie biologică etc.) a cărei concentrație se măsoară în mediul înconjurător.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană, în special pentru componentele legate de calitatea apelor subterane, calitatea apelor din lacuri și râuri, calitatea aerului înconjurător și calitatea apei pentru scăldat.
5.3.4. Tipul valorii măsurate a bolii (DiseaseMeasureTypeValue)
Diferite moduri de raportare a datelor privind bolile și problemele de sănătate conexe ale unei populații.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.5. Tipul factorului de mediu determinant al stării de sănătate (EnvHealthDeterminantTypeValue)
Tipul factorului de mediu determinant al stării de sănătate.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.6. Tipul stării generale de sănătate (GeneralHealthTypeValue)
Tipul indicatorului stării de sănătate.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.7. Tipul serviciilor de sănătate (HealthServicesTypeValue)
Tipul indicatorului referitor la îngrijirea sănătății.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.8. Clasificarea internațională a bolilor (ICDValue)
Boală, astfel cum este definită în Clasificarea internațională a bolilor, a 10-a revizuire.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în cea de a 10-a revizuire a Clasificării statistice internaționale a bolilor și problemelor de sănătate conexe, publicată de World Health Organization (Organizația Mondială a Sănătății).
5.3.9. Matrice (MatrixValue)
Tipul de țesut uman sau compartiment pentru măsurarea markerilor biologici.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.10. Tipul factorului de mediu care influențează sănătătea (MediaTypeValue)
Factorul de mediu în care se măsoară concentrația unei componente a sănătății.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.11. Tipul sursei de zgomot (NoiseSourceTypeValue)
Valorile tipului sursei de zgomot.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.3.12. Metoda agregării statistice (StatisticalAggregationMethodValue)
Tipurile de metode statistice utilizate pentru agregarea datelor neprelucrate ale măsurătorilor privind unitatea statistică.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind sănătatea și siguranța umană.
5.4. Cerințe specifice categoriei
| (1) | Informații statistice privind categoria de date spațiale «Sănătate și siguranță umană» trebuie să se refere la obiecte spațiale, astfel cum sunt definite în cadrul categoriei de date spațiale «Unități statistice».
| (2) | Atunci când este posibil, lista de coduri «ICDValue» trebuie utilizată pentru a identifica denumirea bolii.
| (3) | Date neprelucrate ale măsurătorilor se bazează pe ISO/TS 19103:2005.
| (4) | Datele statistice referitoare la determinantul stării de sănătate trebuie modelate ca date statistice privind sănătatea caracterizate de o valoare a măsurătorii bazată pe ISO/TS 19103:2005 și o metodă de agregare statistică.
| (5) | Acoperirile determinantului stării de sănătate trebuie reprezentate prin utilizarea tipurilor de obiecte spațiale definite în secțiunea 6 din anexa I. Pentru acoperiri continue, trebuie să se utilizeze un subtip al clasei «CoverageByDomainAndRange», al cărui domeniu este limitat la valorile măsurătorilor pe baza ISO/TS 19103:2005.
5.5. Straturi
Straturi pentru categoria de date spațiale «Human Health and Safety»
Numele stratului | Titlul stratului | Tip de obiect spațial
HH.HealthStatisticalData | Date statistice privind sănătatea | StatisticalUnit
HH.HealthDeterminantMeasure | Valoarea măsurată a determinantului stării de sănătate | EnvHealthDeterminantMeasure
6. SERVICII DE UTILITATE PUBLICĂ ȘI SERVICII PUBLICE (UTILITY AND GOVERNMENTAL SERVICES)
6.1. Structura categoriei de date spațiale «Servicii de utilitate publică și servicii publice»
Tipurile specificate pentru categoria de date spațiale «Servicii de utilitate publică și servicii publice» sunt organizate în următoarele pachete:
— Elemente ale rețelei de utilitate publică comună
— Rețea de electricitate
— Rețea petrol-gaze-substanțe chimice
— Rețea de canalizare
— Rețea de energie termică
— Rețea de alimentare cu apă
— Unități de gestionare a mediului
— Servicii administrative și sociale publice (Administrative And Social Governmental Services)
6.2. Elemente ale rețelei de utilitate publică comună
6.2.1. Tipuri de obiecte spațiale
Pachetul «Elemente ale rețelei de utilitate publică comună» conține următoarele tipuri de obiecte spațiale:
— Rețea de utilități
— Element al rețelei de utilități
— Set de legături ale rețelei de utilități
— Nod al rețelei de utilități
— Container pentru noduri de utilități
— Dispozitiv auxiliar
— Dulap
— Cablu
— Tub
— Gură de acces
— Conductă
— Stâlp
— Turn
6.2.1.1. Rețea de utilități (UtilityNetwork)
Ansamblu de elemente de rețea care aparțin unui singur tip de rețea de utilități.
Atribute ale tipului de obiect spațial «UtilityNetwork»
Atribut | Definiție | Tip | Voidability
utilityNetworkType | Tipul sau categoria de rețea de utilități. | UtilityNetworkTypeValue |
authorityRole | Părți autorizate să gestioneze o rețea de utilități, cum ar fi responsabilii cu întreținerea, operatorii sau proprietarii. | RelatedParty |
utilityFacilityReference | Trimitere la o un complex de activități desfășurate în instalații care sunt legate de această rețea de utilități. | ActivityComplex | voidable
disclaimer | Text juridic care descrie clauzele de confidențialitate aplicabile informațiilor privind rețeaua de utilități. | PT_FreeText | voidable
Roluri de asociere ale tipului de obiect spațial «UtilityNetwork»
Rol de asociere | Definiție | Tip | Voidability
networks | O singură rețea secundară care poate fi considerată ca făcând parte dintr-o rețea de utilități de rang mai înalt. | UtilityNetwork | voidable
Constrângeri ale tipului de obiect spațial «UtilityNetwork»
Toate rețelele de utilități trebuie să aibă un identificator de obiect extern.
6.2.1.2. Element al rețelei de utilități (UtilityNetworkElement)
Tip de bază abstract reprezentând un element de rețea de utilități aparținând unei astfel de rețele. Fiecare element dintr-o rețea de utilități este prevăzut cu funcții care prezintă interes în cadrul rețelei respective.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «UtilityNetworkElement»
Atribut | Definiție | Tip | Voidability
currentStatus | Starea unui obiect al utilității din punctul de vedere al integrității și exploatării acestuia. | ConditionOfFacilityValue | voidable
validFrom | Momentul începând cu care elementul rețelei de utilități a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care elementul rețelei de utilități nu mai există în realitate. | DateTime | voidable
verticalPosition | Poziția verticală a obiectului utilității față de nivelul solului. | VerticalPositionValue | voidable
utilityFacilityReference | Trimitere la o un complex de activități care este asociat (conex) acestui element de rețea de utilități. | ActivityComplex | voidable
governmentalServiceReference | Trimitere la un obiect de serviciu public care este asociat (conex) acestui element de rețea de utilități. | GovernmentalService | voidable
6.2.1.3. Set de legături ale rețelei de utilități (UtilityLinkSet)
Ansamblu de succesiuni de legături și/sau de legături individuale care dețin o funcție sau o semnificație specifică în cadrul unei rețele de utilități.
Acest tip este un subtip al «UtilityNetworkElement».
Acest tip este un sub-tip al «LinkSet».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «UtilityLinkSet»
Atribut | Definiție | Tip | Voidability
utilityDeliveryType | Rețea de livrare a utilității, de exemplu transportul, distribuția, colectarea. | UtilityDeliveryTypeValue | voidable
warningType | Mecanism de avertizare vizibilă de suprafață utilizat pentru a indica un element al rețelei de utilități subterane. | WarningTypeValue | voidable
Constrângeri ale tipului de obiect spațial «UtilityLinkSet»
Un set de legături ale rețelei de utilități trebuie să fie alcătuit din legături sau succesiuni de legături care aparțin aceleiași rețele.
Toate seturile de legături ale rețelei de utilități trebuie să aibă un identificator de obiect extern.
6.2.1.4. Legătură de utilități (UtilityLink)
Obiect spațial liniar care descrie geometria și conectivitatea unei rețele de utilități între două puncte ale rețelei respective.
Acest tip este un subtip al «UtilityNetworkElement».
Acest tip este un subtip al «Link».
6.2.1.5. Succesiune de legături de utilități (UtilityLinkSequence)
Un obiect spațial liniar, alcătuit dintr-un ansamblu ordonat de legături de utilități, care reprezintă un traseu neîntrerupt din rețeaua de utilități, fără ramificații. Elementul are un început și un sfârșit definite și fiecare poziție din succesiunea de legături de utilități este identificabilă printr-un parametru unic.
Acest tip este un subtip al «UtilityNetworkElement».
Acest tip este un subtip al «LinkSequence».
6.2.1.6. Nod al rețelei de utilități (UtilityNode)
Un obiect spațial punctual utilizat pentru conectivitate.
Acest tip este un subtip al «UtilityNetworkElement».
Acest tip este un subtip al «Node».
Acest tip este abstract.
Constrângeri ale tipului de obiect spațial «UtilityNode»
Toate nodurile de utilități au un identificator de obiect extern.
6.2.1.7. Container pentru noduri de utilități (UtilityNodeContainer)
Un obiect spațial de tip punct care este utilizat pentru conectivitate și care poate conține, de asemenea, alte obiecte spațiale (neaparținând neapărat aceleiași rețele de utilități).
Acest tip este un subtip al «UtilityNetworkElement».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «UtilityNodeContainer»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Localizarea containerului pentru noduri de utilități. | GM_Point |
Roluri de asociere ale tipului de obiect spațial «UtilityNodeContainer»
Rol de asociere | Definiție | Tip | Voidability
nodes | Noduri de utilități conținute. | UtilityNode | voidable
6.2.1.8. Dispozitiv auxiliar (Appurtenance)
Un dispozitiv auxiliar este un obiect al nodului care este descris de tipul său (prin intermediul atributului «appurtenanceType»).
Acest tip este un subtip al «UtilityNode».
Atribute ale tipului de obiect spațial «Appurtenance»
Atribut | Definiție | Tip | Voidability
appurtenanceType | Tip de dispozitiv auxiliar conform clasificării de tip INSPIRE a dispozitivelor auxiliare. | AppurtenanceTypeValue | voidable
specificAppurtenanceType | Tip de dispozitiv auxiliar conform unei clasificări specifice pe domenii. | SpecificAppurtenanceTypeValue | voidable
6.2.1.9. Dulap (Cabinet)
Un obiect simplu de tipul unui dulap care poate conține obiecte de utilități care aparțin uneia sau mai multor rețele de utilități publice.
Acest tip este un subtip al «UtilityNodeContainer».
6.2.1.10. Cablu (Cable)
O legătură sau o succesiune de legături de utilități utilizate pentru a transporta energie electrică sau date dintr-o locație într-alta.
Acest tip este un subtip al «UtilityLinkSet».
Acest tip este abstract.
6.2.1.11. Tub (Duct)
O legătură sau o succesiune de legături de utilități utilizate pentru a proteja și a dirija calburi și conducte printr-o construcție de tip învelitoare de protecție.
Acest tip este un subtip al «UtilityLinkSet».
Atribute ale tipului de obiect spațial «Duct»
Atribut | Definiție | Tip | Voidability
ductWidth | Lățimea tubului. | Length | voidable
Roluri de asociere ale tipului de obiect spațial «Duct»
Rol de asociere | Definiție | Tip | Voidability
cables | Un tub poate conține unul sau mai multe cabluri. | Cable | voidable
ducts | Un singur tub sau un set de tuburi care constituie tubul intern. | Duct | voidable
pipes | Setul de conducte care constituie canalizarea multitubulară. | Pipe | voidable
Constrângeri ale tipului de obiect spațial «Duct»
Multiplicitatea atributului «utilityDeliveryType» este 0.
6.2.1.12. Gură de acces (Manhole)
Obiect simplu al containerului care poate conține obiecte care aparțin fie unei singure rețele de utilități, fie mai multor rețele de utilități.
Acest tip este un subtip al «UtilityNodeContainer».
6.2.1.13. Conductă (Pipe)
O legătură sau o succesiune de legături pentru transportul materialelor solide, lichide, al substanțelor chimice sau al gazelor dintr-o locație într-alta. O conductă poate fi, de asemenea, utilizată ca obiect menit să învelească mai multe cabluri (un mănunchi de cabluri) sau alte conducte (mai mici).
Acest tip este un subtip al «UtilityLinkSet».
Atribute ale tipului de obiect spațial «Pipe»
Atribut | Definiție | Tip | Voidability
pipeDiameter | Diametrul extern al conductei. | Measure | voidable
pressure | Presiunea de funcționare maximă permisă la care un produs este transportat printr-o conductă. | Measure | voidable
Roluri de asociere ale tipului de obiect spațial «Pipe»
Rol de asociere | Definiție | Tip | Voidability
cable | Cablul conținut de conductă. | Cable | voidable
pipe | Conductă conținută de conductă. | Pipe | voidable
6.2.1.14. Stâlp (Pole)
Un obiect simplu de tipul unui stâlp care poate transporta obiecte de utilități care aparțin fie rețelelor de utilități unice, fie celor multiple.
Acest tip este un subtip al «UtilityNodeContainer».
Atribute ale tipului de obiect spațial «Pole»
Atribut | Definiție | Tip | Voidability
poleHeight | Înălțimea stâlpului. | Length | voidable
6.2.1.15. Turn (Tower)
Un obiect simplu de tipul unui turn care poate transporta obiecte de utilități care aparțin fie unei singure rețele de utilități, fie mai multor rețele de utilități.
Acest tip este un subtip al «UtilityNodeContainer».
Atribute ale tipului de obiect spațial «Tower»
Atribut | Definiție | Tip | Voidability
towerHeight | Înălțimea turnului. | Length | voidable
6.2.2. Liste de coduri
6.2.2.1. Tip de dispozitiv auxiliar (AppurtenanceTypeValue)
Clasificarea dispozitivelor auxiliare.
Valorile permise pentru această listă de coduri cuprind valorile următoarelor liste de coduri sau alte liste de coduri indicate de furnizorii de date:
— Tip de dispozitiv auxiliar pentru electricitate (ElectricityAppurtenanceTypeValue): Clasificarea dispozitivelor auxiliare pentru electricitate, astfel cum se specifică în secțiunea 6.3.2.1.
— Tip de dispozitiv auxiliar pentru petrol, gaze și substanțe chimice (OilGasChemicalsAppurtenanceTypeValue): Clasificarea dispozitivelor auxiliare pentru petrol, gaze și substanțe chimice, astfel cum este specificat în secțiunea 6.4.2.1.
— Tip de dispozitiv auxiliar pentru canalizare (SewerAppurtenanceTypeValue): Clasificarea dispozitivelor auxiliare pentru canalizare, astfel cum se specifică în secțiunea 6.5.2.1.
— Tip de dispozitiv auxiliar pentru energie termică (ThermalAppurtenanceTypeValue): Clasificarea dispozitivelor auxiliare pentru energie termică, astfel cum se specifică în secțiunea 6.6.2.1.
— Tip de dispozitiv auxiliar pentru alimentare cu apă (WaterAppurtenanceTypeValue): Clasificarea dispozitivelor auxiliare pentru alimentare cu apă, astfel cum se specifică în secțiunea 6.7.2.1.
6.2.2.2. Tip de dispozitiv auxiliar specific (SpecificAppurtenanceTypeValue)
Clasificare specifică în funcție de domenii a dispozitivelor auxiliare.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
6.2.2.3. Tip de livrare a utilității (UtilityDeliveryTypeValue)
Clasificarea tipurilor de livrare a utilității.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «UtilityDeliveryTypeValue»
Valoare | Nume | Definiție
collection | colectare | Descrierea unui tip de rețea de utilități care livrează produsul său de utilități cu ajutorul procesului de colectare (de exemplu rețelele de utilități pentru canalizare, colectarea apelor uzate de la clienți)
distribution | distribuție | Descrierea unui tip de rețea de utilități care livrează produsul său de utilități cu ajutorul distribuției locale (de exemplu distribuția locală de electricitate), care este conectată direct la consumatori
private | privat | Descrierea unui tip de rețea de utilități care livrează produsul său de utilități prin intermediul unei rețele private de mici dimensiuni (de exemplu deținută de o companie privată)
transport | transport | Descrierea unui tip de rețea de utilități care livrează produsul său de utilități cu ajutorul unei rețele de transport de mari dimensiuni (de exemplu transportul pe distanțe lungi de produse de tipul petrolului, gazelor sau substanțelor chimice)
6.2.2.4. Tip de rețea de utilități (UtilityNetworkTypeValue)
Clasificarea tipurilor de rețele de utilități.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «UtilityNetworkTypeValue»
Valoare | Nume | Definiție
electricity | electricitate | Rețele de electricitate.
oilGasChemical | petrol, gaze sau substanțe chimice | Rețele de petrol, gaze sau substanțe chimice.
sewer | canalizare | Rețele de canalizare.
water | apă | Rețele de alimentare cu apă.
thermal | energie termică | Rețele de energie termică.
telecommunications | telecomunicații | Rețele de telecomunicații.
6.2.2.5. Tip de avertizare (WarningTypeValue)
Clasificarea tipurilor de avertizare.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «WarningTypeValue»
Valoare | Nume | Definiție
net | plasă | Plasă de avertizare pentru protecția cablurilor și a conductelor.
tape | panglică | Panglică indicatoare (cunoscută, de asemenea, sub denumirea de panglică de avertizare) este o panglică rezistentă din material plastic având o culoare de semnalizare sau o combinație de culori foarte contrastante (cum ar fi galben-negru sau roșu-alb).
concretePaving | pavaj din beton | Un set sau un pavaj din dale de pavaj sau din dale de beton care acoperă cablurile sau conductele.
6.3. Rețea de electricitate
6.3.1. Tipuri de obiecte spațiale
Pachetul «Rețea de electricitate» conține tipul de obiect spațial «Electricity Cable».
6.3.1.1. Cablu de electricitate (ElectricityCable)
O legătură de utilități sau o succesiune de legături de utilități utilizate pentru a transporta electricitate dintr-o locație într-alta.
Acest tip este un subtip al «Cable».
Atribute ale tipului de obiect spațial «ElectricityCable»
Atribut | Definiție | Tip | Voidability
operatingVoltage | Tensiunea electrică de utilizare sau funcționare a echipamentului care folosește electricitate. | Measure | voidable
nominalVoltage | Tensiunea electrică nominală a sistemului la punctul de livrare. | Measure | voidable
6.3.2. Liste de coduri
6.3.2.1. Tip de dispozitiv auxiliar pentru electricitate (ElectricityAppurtenanceTypeValue)
Clasificarea dispozitivelor auxiliare pentru electricitate.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «ElectricityAppurtenanceTypeValue»
Valoare | Nume | Definiție
electricityNode | nod al unei rețele de electricitate | Nod într-o rețea de electricitate.
capacitorControl | control al condensatorului electric | Control al condensatorului electric.
connectionBox | cutie de conexiuni | Cutie de conexiuni.
correctingEquipment | echipament de corecție | Echipament de corecție a factorului de putere.
deliveryPoint | punct de livrare | Punct de livrare.
dynamicProtectiveDevice | dispozitiv protector dinamic | Dispozitiv protector dinamic.
fuse | siguranță | Siguranță.
generator | generator | Generator.
loadTapChanger | comutator de ploturi în sarcină | Comutator de ploturi în sarcină.
mainStation | post de linie principală | Post de linie principală.
netStation | stație de rețea | Stație de rețea.
networkProtector | regulator de rețea | Regulator de rețea.
openPoint | punct deschis | Punct deschis.
primaryMeter | contor primar | Contor primar.
recloserElectronicControl | control electronic al dispozitivului automat de reanclanșare rapidă | Control electronic al dispozitivului automat de reanclanșare rapidă.
recloserHydraulicControl | control hidraulic al dispozitivului automat de reanclanșare rapidă | Control hidraulic al dispozitivului automat de reanclanșare rapidă.
regulatorControl | controlul regulatorului | Controlul regulatorului.
relayControl | controlul releului | Controlul releului.
sectionalizerElectronicControl | control electronic al secționatorului | Control electronic al secționatorului.
sectionalizerHydraulicControl | control hidraulic al secționatorului | Control hidraulic al secționatorului.
streetLight | lampă pentru iluminat stradal | Lampă pentru iluminat stradal.
subStation | post de transformare | Post de transformare.
switch | comutator | Comutator.
transformer | transformator | Transformator.
voltageRegulator | regulator de tensiune | Regulator de tensiune.
detectionEquipment | echipament de detectare | Echipament de detectare
monitoringAndControlEquipment | echipament de monitorizare și control | Echipament de monitorizare și control
6.4. Rețea petrol-gaze-substanțe chimice
6.4.1. Tipuri de obiecte spațiale
Pachetul «Rețea petrol-gaze-substanțe chimice» conține tipul de obiect spațial «Conductă de petrol, gaze și substanțe chimice».
6.4.1.1. Conductă de petrol, gaze și substanțe chimice (OilGasChemicalsPipe)
O conductă pentru transportul petrolului, gazelor sau al substanțelor chimice dintr-o locație într-alta.
Acest tip este un subtip al «Pipe».
Atribute ale tipului de obiect spațial «OilGasChemicalsPipe»
Atribut | Definiție | Tip | Voidability
oilGasChemicalsProductType | Tipul de produs din petrol, gaze sau substanțe chimice care este transportat prin conducte de petrol, gaze sau substanțe chimice. | OilGasChemicalsProductTypeValue | voidable
6.4.2. Liste de coduri
6.4.2.1. Tip de dispozitiv auxiliar pentru petrol, gaze și substanțe chimice (OilGasChemicalsAppurtenanceTypeValue)
Clasificarea dispozitivelor auxiliare pentru petrol, gaze și substanțe chimice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «OilGasChemicalsAppurtenanceTypeValue»
Valoare | Nume | Definiție
pump | Pompă | Pompă
gasStation | Stație de gaz | Stație de gaz
oilGasChemicalsNode | Nod al unei rețele de petrol, gaze sau substanțe chimice | Nod într-o rețea de petrol, gaze sau substanțe chimice
compression | Compresie | Compresie
terminal | Terminal | Terminal
deliveryPoint | Punct de livrare | Punct de livrare
frontier | Frontieră | Frontieră
productionRegion | Regiune de producție | Regiune de producție
plant | Uzină | Uzină
pumpingStation | Stație de pompare | Stație de pompare
storage | Stocare | Stocare
marker | Marker | Marker
6.4.2.2. Tip de produs din petrol, gaze și substanțe chimice (OilGasChemicalsProductTypeValue)
Clasificarea produselor din petrol, gaze și substanțe chimice.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind serviciile de utilități publică și serviciile publice.
6.5. Rețea de canalizare
6.5.1. Tipuri de obiecte spațiale
Pachetul «Rețea de canalizare» conține tipul de obiect spațial «Conductă de canalizare».
6.5.1.1. Conductă de canalizare (SewerPipe)
O conductă de canalizare utilizată pentru a transporta apele uzate (canalizare) dintr-o locație într-alta.
Acest tip este un subtip al «Pipe».
Atribute ale tipului de obiect spațial «SewerPipe»
Atribut | Definiție | Tip | Voidability
sewerWaterType | Tip de apă de canalizare. | SewerWaterTypeValue | voidable
6.5.2. Liste de coduri
6.5.2.1. Tip de dispozitiv auxiliar pentru canalizare (SewerAppurtenanceTypeValue)
Clasificarea dispozitivelor auxiliare pentru canalizare.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «SewerAppurtenanceTypeValue»
Valoare | Nume | Definiție
anode | anod | Anod.
barrel | cilindru | Cilindru.
barScreen | grătar din bare | Grătar din bare.
catchBasin | bazin de captare | Bazin de captare.
cleanOut | sifon (clean out) | Sifon.
dischargeStructure | structură de deversare | Structură de deversare.
meter | contor | Contor.
pump | pompă | Pompă.
regulator | regulator | Regulator.
scadaSensor | senzor SCADA | Senzor SCADA.
thrustProtection | regulator de presiune | Regulator de presiune.
tideGate | valvă anti-retur (tide gate) | Valvă anti-retur.
sewerNode | nod al unei rețele de canalizare | Nod într-o rețea de canalizare.
connection | racord | Racord.
specificStructure | structură specifică | Structură specifică.
mechanicAndElectromechanicEquipment | echipament mecanic și electromecanic | Echipament mecanic și electromecanic.
rainwaterCollector | colector de ape pluviale | Colector de ape pluviale.
watertankOrChamber | rezervor de apă sau cameră de echilibru | Rezervor de apă sau cameră de echilibru.
6.5.2.2. Tip de apă de canalizare (SewerWaterTypeValue)
Clasificarea tipurilor de ape de canalizare.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «SewerWaterTypeValue»
Valoare | Nume | Definiție
combined | combinată | Apă de canalizare combinată.
reclaimed | recuperată | Apă de canalizare recuperată.
sanitary | sanitară | Apă de canalizare sanitară.
storm | pluvială | Apă de canalizare pluvială.
6.6. Rețea de energie termică
6.6.1. Tipuri de obiecte spațiale
Pachetul «Rețea de energie termică» conține obiectul spațial «typeThermal Pipe».
6.6.1.1. Conductă de energie termică (ThermalPipe)
O conductă utilizată pentru a difuza încălzire sau răcire dintr-o locație într-alta.
Acest tip este un subtip al «Pipe».
Atribute ale tipului de obiect spațial «ThermalPipe»
Atribut | Definiție | Tip | Voidability
thermalProductType | Tipul de produs termic care este transportat prin conducta de energie termică. | ThermalProductTypeValue | voidable
6.6.2. Liste de coduri
6.6.2.1. Tip de dispozitiv auxiliar pentru energie termică (ThermalAppurtenanceTypeValue)
Clasificarea dispozitivelor auxiliare pentru energie termică.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind serviciile de utilități publice și serviciile publice.
6.6.2.2. Tip de produs termic (ThermalProductTypeValue)
Clasificarea produselor termice.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind serviciile de utilități publice și serviciile publice.
6.7. Rețea de alimentare cu apă
6.7.1. Tipuri de obiecte spațiale
Pachetul «Rețea de alimentare cu apă» conține tipul de obiect spațial «Conductă de apă».
6.7.1.1. Conductă de apă (WaterPipe)
O conductă de apă utilizată pentru a transporta apa dintr-o locație într-alta.
Acest tip este un subtip al «Pipe».
Atribute ale tipului de obiect spațial «WaterPipe»
Atribut | Definiție | Tip | Voidability
waterType | Tipul de apă. | WaterTypeValue | voidable
6.7.2. Liste de coduri
6.7.2.1. Tip de dispozitiv auxiliar pentru apă (WaterAppurtenanceTypeValue)
Clasificarea dispozitivelor auxiliare pentru apă.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «WaterAppurtenanceTypeValue»
Valoare | Nume | Definiție
waterNode | nod al unei rețele de apă | Nod într-o rețea de apă.
anode | anod | Anod.
clearWell | puț de decantare (clear well) | Puț de decantare.
controlValve | vană de reglaj | Vană de reglaj.
fitting | racord | Racord.
hydrant | hidrant | Hidrant.
junction | confluență | Confluență.
lateralPoint | punct lateral | Punct lateral.
meter | contor | Contor.
pump | pompă | Pompă.
pumpStation | stație de pompare | Stație de pompare.
samplingStation | stație de prelevare | Stație de prelevare.
scadaSensor | senzor SCADA | Senzor SCADA.
storageBasin | bazin de retenție | Bazin de retenție.
storageFacility | instalație de stocare | Instalație de stocare închisă.
surgeReliefTank | rezervor de echilibrare a presiunii | Rezervor de echilibrare a presiunii.
systemValve | supapă a sistemului | Supapă a sistemului.
thrustProtection | regulator de presiune | Regulator de presiune.
treatmentPlant | stație de tratare | Stație de tratare.
well | puț | Puț de producție.
pressureRelieveValve | supapă de reducere a presiunii | Supapă de reducere a presiunii.
airRelieveValve | supapă de aerisire | Supapă de aerisire.
checkValve | supapă de reținere | Supapă de reținere.
waterExhaustPoint | punct de evacuare a apei | Punct de evacuare a apei.
waterServicePoint | punct de alimentare cu apă | Punct de alimentare cu apă.
fountain | fântână | Fântână.
fireHydrant | hidrant | Hidrant.
pressureController | regulator de presiune | Regulator de presiune.
vent | aerisire | Aerisire.
recoilCheckValve | ventil de reținere | Ventil de reținere.
waterDischargePoint | punct de deversare a apei | Punct de deversare a apei.
6.7.2.2. Tip de apă (WaterTypeValue)
Clasificarea tipurilor de ape.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «WaterTypeValue»
Valoare | Nume | Definiție
potable | potabilă | Apă potabilă.
raw | brută | Apă brută.
salt | sărată | Apă sărată.
treated | tratată | Apă tratată.
6.8. Unități de gestionare a mediului
6.8.1. Tipuri de obiecte spațiale
Pachetul «Unități de gestionare a mediului» conține tipul de obiect spațial «Unitate de gestionare a mediului».
6.8.1.1. Unitate de gestionare a mediului (EnvironmentalManagementFacility)
O structură fizică proiectată, construită sau instalată pentru a îndeplini funcții specifice în ceea ce privește fluxurile de materiale cu impact asupra mediului, cum ar fi fluxurile de deșeuri și fluxurile de ape reziduale, sau o anumită zonă de uscat sau apă utilizată pentru a îndeplini astfel de funcții.
Acest tip este un subtip al «ActivityComplex».
Atribute ale tipului de obiect spațial «EnvironmentalManagementFacility»
Atribut | Definiție | Tip | Voidability
type | Tipul de unitate, cum ar fi o instalație sau un sit. | EnvironmentalManagementFacilityTypeValue | voidable
serviceHours | Ore de funcționare ale unității. | PT_FreeText | voidable
facilityDescription | Informații suplimentare referitoare la o unitate de gestionare a mediului, inclusiv adresa, datele de contact, părțile afiliate și o descriere sub forma unui text liber. | ActivityComplexDescription | voidable
physicalCapacity | O cuantificare a unei posibilități reale sau potențiale de a executa o activitate. | Capacity | voidable
permission | Decizie oficială (consimțământ oficial) prin care se acordă autorizația de a exploata o întreagă unitate de gestionare a mediului sau o parte a acesteia. | Permission | voidable
status | Statutul unității de gestionare a mediului, cum ar fi statutul operațional sau dezafectarea. | ConditionOfFacilityValue | voidable
Roluri de asociere ale tipului de obiect spațial «EnvironmentalManagementFacility»
Rol de asociere | Definiție | Tip | Voidability
parentFacility | O unitate-mamă, adică o unitate din care face parte unitatea în cauză. | EnvironmentalManagementFacility | voidable
6.8.2. Liste de coduri
6.8.2.1. Clasificarea unităților de mediu (EnvironmentalManagementFacilityTypeValue)
Clasificarea unităților de mediu, de exemplu situri și instalații.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Valori pentru lista de coduri «EnvironmentalManagementFacilityTypeValue»
Valoare | Nume | Definiție
site | Site | Toate terenurile dintr-o locație geografică distinctă, aflate sub controlul managerial al unei organizații care acoperă activități, produse și servicii.
installation | Instalație | O unitate tehnică, cum ar fi utilajele, instrumentele, un dispozitiv, un sistem instalat sau un echipament așezat în poziție sau conectat pentru a fi utilizat.
6.9. Servicii administrative și sociale publice (Administrative And Social Governmental Services)
6.9.1. Tipuri de obiecte spațiale
Pachetul «Servicii administrative și sociale publice» conține tipul de obiect spațial «Serviciu public».
6.9.1.1. Serviciu public (GovernmentalService)
Servicii administrative și sociale publice, cum ar fi administrațiile publice, siturile de protecție civilă, școlile și spitalele furnizate de organisme administrative publice sau de instituții private, în măsura în care acestea sunt incluse în domeniul de aplicare al Directivei 2007/2/CE. Acest domeniu de aplicare este pus în corespondență cu valorile din lista de coduri aferentă «ServiceTypeValue».
Atribute ale tipului de obiect spațial «GovernmentalService»
Atribut | Definiție | Tip | Voidability
areaOfResponsibility | Zona pe care o acoperă un serviciu. | AreaOfResponsibilityType | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
pointOfContact | Conține informațiile necesare pentru a avea acces la un serviciu și/sau informațiile inițiale cu privire la un serviciu. | Contact | voidable
serviceLocation | Locul în care este furnizat serviciul. | ServiceLocationType |
serviceType | Tipul de serviciu administrativ și public. | ServiceTypeValue |
6.9.2. Tipuri de date
6.9.2.1. Tipul ariei de responsabilitate (AreaOfResponsibilityType)
Set de tipuri pentru descrierea responsabilității în funcție de zonă.
Acest tip este o uniune.
Atribute ale tipului de date «AreaOfResponsibilityType»
Atribut | Definiție | Tip | Voidability
areaOfResponsibilityByAdministrativeUnit | Unitate administrativă care descrie extinderea geografică a responsabilității unui serviciu. | AdministrativeUnit |
areaOfResponsibilityByNamedPlace | Obiect geografic care descrie extinderea geografică a responsabilității unui serviciu. | NamedPlace |
areaOfResponsibilityByNetwork | Parte a unei rețele care descrie extinderea geografică a competenței unui serviciu. | NetworkReference |
areaOfResponsibilityByPolygon | Poligon care descrie extinderea geografică a responsabilității unui serviciu. | GM_MultiSurface |
6.9.2.2. Tipul localizării serviciului (ServiceLocationType)
Set de tipuri de trimiteri la localizarea unui serviciu.
Acest tip este o uniune.
Atribute ale tipului de uniune «ServiceLocationType»
Atribut | Definiție | Tip | Voidability
serviceLocationByAddress | Localizarea unui serviciu prin trimitere la o adresă. | Address |
serviceLocationByBuilding | Localizarea unui serviciu prin trimitere la o clădire. | Building |
serviceLocationByActivityComplex | Localizarea serviciului prin trimitere la un complex de activități. | ActivityComplex |
serviceLocationByGeometry | Localizarea unui serviciu prin trimitere la o geometrie. | GM_Object |
serviceLocationByUtilityNode | Localizarea unui serviciu prin trimitere la un nod aparținând unei rețele de utilități (apă, electricitate etc.), de exemplu, un hidrant sau un punct de apel de urgență. | UtilityNode |
6.9.3. Liste de coduri
6.9.3.1. Tipul serviciului (ServiceTypeValue)
Lista de coduri care conține o clasificare a serviciilor publice.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Valori pentru lista de coduri «ServiceTypeValue»
Valoare | Nume | Definiție | Parent Value
publicAdministrationOffice | birou al administrației publice | Birourile administrației publice (care nu sunt diferențiate suplimentar). |
generalAdministrationOffice | birou al administrației generale | Birourile administrației generale, de exemplu birourile primăriilor. | publicAdministrationOffice
specializedAdministrationOffice | birou al administrației specializate | Birourile administrației specializate care nu pot fi alocate următoarelor domenii: servicii sociale, educație, sănătate protecția mediului, ordine și protecția publică (de exemplu administrația responsabilă cu investigarea). | publicAdministrationOffice
publicOrderAndSafety | ordine și siguranță publică | Servicii de menținere a ordinii și siguranței publice. |
administrationForPublicOrderAndSafety | administrație pentru ordinea și siguranța publică | Birouri administrative responsabile cu ordinea și siguranța publică. | publicOrderAndSafety
policeService | serviciu de poliție | Servicii constând din desfășurarea de misiuni ale poliției. | publicOrderAndSafety
fireProtectionService | serviciu de pompieri | Servicii de prevenire și stingere a incendiilor; manevrarea corpurilor de pompieri auxiliare și prestarea de alte servicii de prevenire și stingere a incendiilor aflate în responsabilitatea autorităților publice; Desfășurarea sau contribuirea la programe de formare în materie de prevenire și stingere a incendiilor. | publicOrderAndSafety
fireStation | remiză de pompieri | Servicii constând dintr-o remiză care adăpostește pompieri, echipamentul și vehiculele acestora. | fireProtectionService
siren | sirenă | Dispozitiv staționar, adesea acționat electric, pentru producerea unui sunet penetrant de avertizare a publicului. | fireProtectionService
hydrant | hidrant | Puncte speciale de acces la apă ale rețelelor de alimentare cu apă care sunt special concepute și construite pentru a servi ca surse de apă la fața locului pentru combaterea incendiilor și alte servicii de urgență. | fireProtectionService
antiFireWaterProvision | alimentare cu apă pentru combaterea incendiilor | Locul, instalația sau zona desemnată de unde se furnizează apă pentru combaterea incendiilor. | fireProtectionService
fireDetectionAndObservationSite | sit de observare de detectare a incendiilor | Locul, instalația, construcția sau dispozitivul de detectare și observare a incendiilor. | fireProtectionService
rescueService | serviciu de salvare | Servicii de căutare și salvare a persoanelor, animalelor și bunurilor în situații de urgență. | publicOrderAndSafety
rescueStation | stație de salvare | Servicii constând din adăpostirea personalului tehnic, echipamentelor și a elementelor auxiliare aparținând echipelor de salvare. | rescueService
rescueHelicopterLandingSite | sit de aterizare a elicopterului de salvare | O zonă specială care poate fi utilizată de elicopterele de salvare pentru decolări și aterizări. | rescueService
marineRescueStation | stație de salvare marină | Servicii de coastă constând din clădiri, zone de amarare sau chei rezervate găzduirii echipelor de salvare marină și a echipamentului lor, nave și alte ambarcațiuni marine. | rescueService
civilProtectionSite | sit de protecție civilă | Sit care oferă populației civile protecție și adăpost împotriva dezastrelor și în situații de urgență. | publicOrderAndSafety
emergencyCallPoint | punct pentru apeluri de urgență | Amplasarea de telefoane într-o cutie sau pe un stâlp pentru a fi utilizate de conducătorii auto în situații de urgență. | publicOrderAndSafety
standaloneFirstAidEquipment | echipament autonom de prim ajutor | Element sau set de elemente sau echipamente de prim ajutor puse la dispoziția tuturor persoanelor în caz de necesitate, amplasate în locuri foarte vizibile și ușor accesibile. | publicOrderAndSafety
defence | defence | Servicii din domeniul apărării militare. | publicOrderAndSafety
barrack | baracă | Servicii constând din furnizarea de clădiri utilizate în special pentru găzduirea soldaților în garnizoană. | defence
camp | tabără | Loc situat de obicei la distanță de zonele urbane, unde sunt ridicate corturi sau simple clădiri (cabine) pentru adăpostirea sau pentru șederea temporară sau instruirea forțelor militare. | defence
environmentalProtection | protecția mediului | Serviciile constând din administrarea, supravegherea, inspecția, exploatarea sau sprijinirea activităților legate de protecția și conservarea mediului. |
administrationForEnvironmentalProtection | administrație responsabilă cu protecția mediului | Birouri administrative implicate în protecția mediului. | environmentalProtection
environmentalEducationCentre | centru de formare în materie de protecția mediului | Instituție implicată în dezvoltarea de programe și materiale pentru a spori gradul de sensibilizare cu privire la mediu și la dezvoltarea durabilă. | environmentalProtection
health | sănătate | Servicii implicate în aspecte legate de sănătate. |
administrationForHealth | administrație responsabilă cu sănătatea | Cuprinde unități implicate în principal în reglementarea activităților agențiilor care asigură îngrijirea sănătății și care sunt responsabile cu administrarea globală a politicii de sănătate. | health
medicalProductsAppliancesAndEquipment | produse, aparatură și echipamente medicale | Servicii din domeniul medicamentelor, protezelor, aparaturii și echipamentelor medicale și al altor produse legate de sănătate obținute de indivizi sau gospodării, cu sau fără rețetă, de obicei de la drogherii, farmaciști sau furnizori de echipamente medicale. Acestea sunt destinate consumului în afara unităților sau instituțiilor de sănătate. | health
outpatientService | servicii ambulatorii | Servicii medicale, dentare și paramedicale furnizate în cazul pacienților externi de medici, dentiști și de prestatorii de servicii paramedicale și auxiliare. Serviciile pot fi livrate la domiciliu, în unități de consult individuale sau de grup, în dispensare sau în clinici ambulatorii ale spitalelor etc. Printre serviciile ambulatorii se numără medicamentele, protezele, aparatura și echipamentele medicale și alte produse legate de sănătate furnizate direct pacienților externi de către medici, dentiști și prestatorii de servicii paramedicale și auxiliare. | health
generalMedicalService | servicii de medicină generală | Servicii de medicină generală prestate de clinici de medicină generală și de medici generaliști. | outpatientService
specializedMedicalServices | servicii de medicină specializată | Servicii de medicină specializată prestate de clinici medicale specializate și de medici de specialitate. Clinicile medicale specializate și medicii de specialitate diferă de clinicile de medicină generală și de medicii generaliști prin faptul că serviciile respective se limitează la tratarea unei stări, boli, proceduri medicale sau clase de pacienți specială. | outpatientService
paramedicalService | servicii paramedicale | Furnizarea de servicii paramedicale pacienților externi; Administrarea, inspecția, exploatarea sau sprijinirea serviciilor de sănătate prestate de clinici, supervizate de asistente, moașe, fizioterapeuți, ergoterapeuți, logopezi sau alt tip de personal paramedical, precum și de servicii de sănătate prestate de asistente, moașe și personal paramedical în încăperi nedestinate consultului, la domiciliul bolnavilor sau în alte instituții de natură non-medicală. | outpatientService
hospitalService | servicii spitalicești | Serviciile din domeniul spitalizării. Spitalizarea este definită ca situația în care un pacient este internat într-un spital pe durata tratamentului. Sunt incluse centrele de zi în regim spitalicesc și tratamentele spitalicești la domiciliu, precum și azilele pentru bolnavi în fază terminală. Spitalele sunt definite ca fiind acele instituții care oferă servicii medicale pacienților spitalizați sub supravegherea directă a unor medici calificați. | health
generalHospital | spital general | Servicii spitalicești care nu se limitează la o anumită specialitate medicală. | hospitalService
specializedHospital | spital specializat | Servicii spitalicești care se limitează la o anumită specialitate medicală. | hospitalService
nursingAndConvalescentHomeService | servicii la domiciliu de infirmerie și convalescență | Servicii pentru pacienți spitalizați adresate persoanelor aflate în perioada de recuperare după o intervenție chirurgicală sau o boală sau o afecțiune invalidantă care necesită, în principal, monitorizarea și administrarea de medicamente, fizioterapie și antrenament pentru a compensa pierderea unei funcții sau a odihnei. | hospitalService
medicalAndDiagnosticLaboratory | laborator medical și de diagnosticare | Cuprinde unități responsabile în principal cu furnizarea de servicii analitici sau de diagnosticare, inclusiv analiza fluidelor organismului și imagistică diagnostică, în general profesiunii medicale sau pacientului în urma trimiterii din partea unui medic. | health
education | educație | Servicii din domeniul învățământului. Printre aceste servicii se numără școli și colegii militare, în care programele de învățământ se aseamănă cu cele ale instituțiilor civile, colegiile de poliție care oferă învățământ general pe lângă formarea forțelor de poliție. |
administrationForEducation | administrație responsabilă cu educația | Birouri administrative responsabile cu aspecte educaționale. | education
earlyChildhoodEducation | educația infantilă | Servicii din domeniul educației preșcolare la nivelul 0 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
primaryEducation | învățământ primar | Servicii din domeniul învățământului primar la nivelul 1 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
lowerSecondaryEducation | învățământ secundar inferior | Servicii din domeniul învățământului secundar inferior la nivelul 2 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
upperSecondaryEducation | învățământ secundar superior | Servicii din domeniul învățământului secundar superior la nivelul 3 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
postSecondaryNonTertiaryEducation | învățământ postliceal neuniversitar | Servicii din domeniul învățământului doctoral sau echivalent la nivelul 4 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
shortCycleTertiaryEducation | învățământ superior de scurtă durată | Servicii din domeniul învățământului superior de scurtă durată la nivelul 5 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
bachelorOrEquivalentEducation | învățământ la nivel de bacalaureat sau echivalent | Servicii din domeniul învățământului la nivel de bacalaureat sau echivalent la nivelul 6 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
masterOrEquivalentEducation | învățământ la nivel de master sau echivalent | Servicii din domeniul învățământului la nivel de master sau echivalent la nivelul 7 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
doctoralOrEquivalentEducation | învățământ doctoral sau echivalent | Servicii din domeniul învățământului doctoral sau echivalent la nivelul 8 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
educationNotElsewhereClassified | învățământ neclasificat în altă parte | Serviciile din domeniul învățământului neclasificat în altă parte la nivelul 9 al ISCED-2011 (International Standard Classification of Education, 2011 revision). | education
subsidiaryServicesToEducation | servicii conexe educației | Servicii conexe educației, servicii legate de transport, alimente, cazare, îngrijire medicală și dentară și servicii conexe în principal pentru studenți, indiferent de nivel. | education
socialService | serviciu social | Servicii din domeniul protecției sociale. |
administrationForSocialProtection | administrație responsabilă cu protecția socială | Birouri administrative responsabile cu aspecte de protecție socială. | socialService
specializedServiceOfSocialProtection | servicii specializate de protecție socială | Diverse servicii specializate constând din transportul, îngrijire la domiciliu, îngrijire de zi și îngrijire pe timpul vacanțelor pentru persoanele cu handicap și pentru cele care necesită asistență. Servicii constând în special din educarea și oferirea de locuri de muncă persoanelor cu handicap. | socialService
housing | cazare | Servicii care implică punerea la dispoziție de orice domiciliu, reședință, facilitate sau incintă care oferă cazare temporară, provizorie sau permanentă unor diverse grupuri de persoane. | socialService
childCareService | servicii de îngrijire a copiilor | Servicii care constau din îngrijirea de zi a copiilor. | socialService
charityAndCounselling | asociații caritabile și de consiliere | Instituții și servicii care acordă prestații în natură și/sau consiliere pentru persoanele nevoiașe, de exemplu, pentru șomeri, persoanele defavorizate din punct de vedere social, victimele dezastrelor, victimele violenței și abuzurilor, persoanele cu potențial de sinucidere etc. | socialService
6.10. Straturi
Straturi pentru categoria de date spațiale «Servicii de utilități publică și servicii publice»
Numele stratului | Titlul stratului | Tip de obiect spațial
US.UtilityNetwork | Rețea de utilități | Appurtenance, Manhole, Tower, Pole, Cabinet, Duct, Pipe
US.ElectricityNetwork | Rețea de electricitate | Electricity Cable, Appurtenance (dacă fac parte dintr-o rețea de electricitate)
US. OilGasChemicalsNetwork | Rețea de petrol, gaze sau substanțe chimice | OilGasChemicalsPipe, Appurtenance (dacă fac parte dintr-o rețea de petrol, gaze sau substanțe chimice)
US.SewerNetwork | Rețea de canalizare | SewerPipe, Appurtenance (dacă fac parte dintr-o rețea de canalizare)
US.ThermalNetwork | Rețea de energie termică | ThermalPipe, Appurtenance (dacă fac parte dintr-o rețea de energie termică)
US.WaterNetwork | Rețea de alimentare cu apă | WaterPipe, Appurtenance (dacă fac parte dintr-o rețea de apă)
US. <ValoaredinListadeCoduri>(4) | <nume lizibil de către om> | GovernmentalService
Exemplu: US.PoliceService | Exemplu: Serviciu de poliție | (serviceType: ServiceTypeValue)
US.EnvironmentalManagementFacility | Unitate de gestionare a mediului | EnvironmentalManagementFacility
7. INSTALAȚII DE MONITORIZARE A MEDIULUI (ENVIRONMENTAL MONITORING FACILITIES)
7.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt specificate pentru categoria de date spațiale «Instalații de supraveghere a mediului»:
— Caracteristică de monitorizare abstractă
— Obiect de monitorizare abstractă
— Activitatea de monitorizare a mediului
— Instalație de monitorizare a mediului
— Rețea de monitorizare a mediului
— Program de monitorizare a mediului
— Capacitate de observare
— Perioadă de activitate operațională
7.1.1. Caracteristică de monitorizare abstractă (AbstractMonitoringFeature)
O clasă abstractă de bază pentru caracteristicile de monitorizare a mediului existente în lumea reală (EnvironmentalMonitoringNetwork, EnvironmentalMonitoringFacility).
Acest tip este un subtip al «AbstractMonitoringObject».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractMonitoringFeature»
Atribut | Definiție | Tip | Voidability
reportedTo | Informații privind implicarea «AbstractMonitoringFeature» în raportare. | ReportToLegalAct | voidable
Roluri de asociere ale tipului de obiect spațial «AbstractMonitoringFeature»
Rol de asociere | Definiție | Tip | Voidability
involvedIn | «EnvironmentalMonitoringActivity(s)» în care este implicată «AbstractMonitoringFeature». | EnvironmentalMonitoringActivity | voidable
hasObservation | Observare a emisiilor, a stării mediului înconjurător și a altor parametri ecosistemici (biodiversitate, condiții ecologice ale vegetației etc.) de către sau în numele autorităților publice al acest «AbstractMonitoringFeature». | OM_Observation | voidable
Constrângeri ale tipului de obiect spațial «AbstractMonitoringFeature»
Dacă observația (observațiile) se anexează la un «AbstractMonitoringFeature», acesta trebuie să aibă atașată o «ObservingCapability». «ObservingCapability» trebuie să se refere la același «Domain», «Phenomenon» și «ProcessUsed» ca și observația (observațiile).
7.1.2. Obiect de monitorizare abstractă (AbstractMonitoringObject)
O clasă abstractă de bază pentru obiectele de monitorizare a mediului.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractMonitoringObject»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
name | Denotație sub formă de text simplu a «AbstractMonitoringObject». | CharacterString | voidable
additionalDescription | Descriere sub formă de text simplu a informațiilor suplimentare care nu se încadrează în alte atribute. | CharacterString | voidable
mediaMonitored | Mediu ecologic monitorizat. | MediaValue |
legalBackground | Contextul juridic, în care se definește gestionarea și reglementarea «AbstractMonitoringObject». | LegislationCitation | voidable
responsibleParty | Partea responsabilă pentru «AbstractMonitoringObject». | RelatedParty | voidable
geometry | Geometrie asociată cu «AbstractMonitoringObject». Pentru instalații mobile, geometria reprezintă zona în care instalația ar trebui să efectueze măsurători. | GM_Object |
onlineResource | Un link către un document extern care furnizează informații suplimentare privind «AbstractMonitoringObject». | URL | voidable
purpose | Motivul pentru care a fost generat «AbstractMonitoringObject». | PurposeOfCollectionValue | voidable
Roluri de asociere ale tipului de obiect spațial «AbstractMonitoringObject»
Rol de asociere | Definiție | Tip | Voidability
observingCapability | O legătură care indică potențialul explicit al unui «AbstractMonitoringObject». Aceasta oferă o legătură clară între proprietatea observată, procedura utilizată și localizarea măsurătorii | ObservingCapability | voidable
broader | O legătură care indică un «AbstractMonitoringObject» mai larg (un nivel mai ridicat într-o structură ierarhică). Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «Hierarchy». | AbstractMonitoringObject | voidable
narrower | O legătură care indică «AbstractMonitoringObject(s)» mai restrânse (un nivel inferior într-o structură ierarhică). Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «Hierarchy». | AbstractMonitoringObject | voidable
supersedes | Într-o genealogie, «AbstractMonitoringObject(s)» care a (au) fost dezactivat/înlocuite cu un altul. | AbstractMonitoringObject | voidable
supersededBy | Într-o genealogie, «AbstractMonitoringObject(s)» activ(e) din nou, care înlocuiește (înlocuiesc) pe cel înlăturat. | AbstractMonitoringObject | voidable
7.1.3. Activitate de monitorizare a mediului (EnvironmentalMonitoringActivity)
Set specific de «AbstractMonitoringFeatures» utilizate pentru un anumit domeniu într-un interval de timp, zonă și scop coerente și concise. De obicei, informațiile colectate sunt tratate ca o singură etapă într-un program de monitorizare pe termen lung. Este o realizare concretă a unui «EnvironmentalMonitoringProgramme» dat.
Atribute ale tipului de obiect spațial «EnvironmentalMonitoringActivity»
Atribut | Definiție | Tip | Voidability
activityTime | Durata de viață a «EnvironmentalMonitoringActivity». | TM_Object | voidable
activityConditions | Descriere textuală a «EnvironmentalMonitoringActivity». | CharacterString | voidable
boundingBox | Caseta de delimitare în care are loc «EnvironmentalMonitoringActivity». | GM_Boundary | voidable
responsibleParty | Partea responsabilă pentru «EnvironmentalMonitoringActivity». | RelatedParty | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
onlineResource | O legătură către un document extern care furnizează informații suplimentare privind «EnvironmentalMonitoringActivity». | URL | voidable
Roluri de asociere ale tipului de obiect spațial «EnvironmentalMonitoringActivity»
Rol de asociere | Definiție | Tip | Voidability
setUpFor | «EnvironmentalMonitoringProgramme(s)» pentru care este stabilită «EnvironmentalMonitoringActivity». | EnvironmentalMonitoringProgramme | voidable
uses | Set specific de «AbstractMonitoringFeature(s)» implicat într-o «EnvironmentalMonitoringActivity». | AbstractMonitoringFeature | voidable
7.1.4. Instalație de monitorizare a mediului (EnvironmentalMonitoringFacility)
Un obiect georeferențiat direct care colectează sau prelucrează date despre obiecte ale căror proprietăți (de exemplu fizice, chimice, biologice sau alte aspecte ale condițiilor de mediu) sunt observate sau măsurate în mod repetat. O instalație de monitorizare a mediului poate găzdui, de asemenea, alte instalații de monitorizare a mediului.
Acest tip este un subtip al «AbstractMonitoringFeature».
Atribute ale tipului de obiect spațial «EnvironmentalMonitoringFacility»
Atribut | Definiție | Tip | Voidability
representativePoint | Locație reprezentativă pentru «EnvironmentalMonitoringFacility». | GM_Point | voidable
measurementRegime | Regim de măsurare | MeasurementRegimeValue | voidable
mobile | Se indică dacă «EnvironmentalMonitoringFacility» este mobilă (repoziționabilă) în timpul colectării observațiilor. | Boolean | voidable
resultAcquisitionSource | Sursă a colectării rezultatelor. | ResultAcquisitionSourceValue | voidable
specialisedEMFType | Clasificarea «EnvironmentalMonitoringFacilities» utilizate în general în funcție de domeniu și în condiții naționale. | SpecialisedEMFTypeValue | voidable
operationalActivityPeriod | Perioada (perioadele) în care «EnvironmentalMonitoringFacility» a funcționat. | TM_Object | voidable
Roluri de asociere ale tipului de obiect spațial «EnvironmentalMonitoringFacility»
Rol de asociere | Definiție | Tip | Voidability
relatedTo | Toate elementele de legătură tematice către o «Environmental Monitoring Facility». Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «AnyDomainLink». | EnvironmentalMonitoringFacility | voidable
belongsTo | Un element de legătură care indică «EnvironmentalMonitoringNetwork(s)» căruia îi aparține această «EnvironmentalMonitoringFacility». Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «NetworkFacility». | EnvironmentalMonitoringNetwork | voidable
Constrângeri ale tipului de obiect spațial «EnvironmentalMonitoringFacility»
Nu se poate ca și «Geometria» și «representativePoint» să fie goale.
7.1.5. Rețea de monitorizare a mediului (EnvironmentalMonitoringNetwork)
Grupare administrativă sau organizațională de «EnvironmentalMonitoringFacilities» gestionate în același mod pentru un scop specific și vizând un domeniu specific. Fiecare rețea respectă normele comune care vizează asigurarea coerenței observațiilor, în special în sensul «EnvironmentalMonitoringFacilities», selectarea parametrilor obligatorii, metodele de măsurare și regimul de măsurare.
Acest tip este un subtip al «AbstractMonitoringFeature».
Atribute ale tipului de obiect spațial «EnvironmentalMonitoringNetwork»
Atribut | Definiție | Tip | Voidability
organisationLevel | Nivel al organizației juridice căreia îi este afiliată «EnvironmentalMonitoringNetwork». | LegislationLevelValue | voidable
Roluri de asociere ale tipului de obiect spațial «EnvironmentalMonitoringNetwork»
Rol de asociere | Definiție | Tip | Voidability
contains | O legătură care indică «EnvironmentalMonitoringFacility(s)» inclus în această «EnvironmentalMonitoringNetwork». Asocierea are proprietăți suplimentare, astfel cum sunt definite în cadrul clasei de asociere «NetworkFacility». | EnvironmentalMonitoringFacility | voidable
7.1.6. Program de monitorizare a mediului (EnvironmentalMonitoringProgramme)
Cadru bazat pe documente de politică relevante care definesc obiectivul unui set de observații și/sau aplicarea pe teren a «AbstractMonitoringFeatures». De regulă, un program de monitorizare a mediului are o perspectivă pe termen lung pe o perioadă de cel puțin câțiva ani.
Acest tip este un subtip al «AbstractMonitoringObject».
Roluri de asociere ale tipului de obiect spațial «EnvironmentalMonitoringProgramme»
Rol de asociere | Definiție | Tip | Voidability
triggers | «EnvironmentalMonitoringActivity(s)» declanșată de «EnvironmentalMonitoringProgramme». | EnvironmentalMonitoringActivity | voidable
7.1.7. Capacitate de observare (ObservingCapability)
Capacitatea explicită a unui «AbstractMonitoringObject».
Atribute ale tipului de obiect spațial «ObservingCapability»
Atribut | Definiție | Tip | Voidability
observingTime | Descrie perioada de timp în care sunt de așteptat observații de la acest «AbstractMonitoringObject». Poate fi vorba numai de un moment de inițiere a realizării de măsurători sau un interval. | TM_Object | voidable
processType | Tipul de obiect utilizat pentru a descrie acest proces. | ProcessTypeValue | voidable
resultNature | Starea rezultatului furnizat. | ResultNatureValue | voidable
onlineResource | O legătură către un document extern care oferă mai multe informații despre un model de date care respectă ISO 19156 - Observations and Measurements – și utilizat pentru a stoca sau a face schimb de observațiile și măsurătorile necesare | URL | voidable
Roluri de asociere ale tipului de obiect spațial «ObservingCapability»
Rol de asociere | Definiție | Tip | Voidability
observedProperty | Proprietatea care este observată sau măsurată în aceste «AbstractMonitoringObject». | GF_PropertyType |
featureOfInterest | Această caracteristică este obiectul real ale cărui proprietăți se află sub observație sau este o caracteristică care servește la eșantionarea obiectului real. | GFI_Feature | voidable
procedure | Legătură către procesul utilizat pentru a genera rezultatul. «OM_Process» trebuie să fie adecvat proprietății observate. Ca un corolar, detaliile privind proprietatea observată sunt limitate de procedura utilizată. | OM_Process |
7.2. Tipuri de date
7.2.1. Orice legătură tematică (AnyDomainLink)
Orice legătură tematică la o «EnvironmentalMonitoringFacility» care nu este ierarhică și nici nu este asociată cu o noțiune de genealogie.
Acest tip este o clasă de asociere.
Atribute ale tipului de date «AnyDomainLink»
Atribut | Definiție | Tip | Voidability
Comment | Informații suplimentare privind legătura tematică. | CharacterString | voidable
7.2.2. Ierarhie (Hierarchy)
Legătură ierarhică între «AbstractMonitoringObjects».
Acest tip este o clasă de asociere.
Atribute ale tipului de date «Hierarchy»
Atribut | Definiție | Tip | Voidability
linkingTime | Perioada de timp a legăturii. | TM_Object | voidable
7.2.3. Instalația rețelei (NetworkFacility)
Legătura dintre «EnvironmentalMonitoringNetwork» și «EnvironmentalMonitoringFacility».
Acest tip este o clasă de asociere.
Atribute ale tipului de date «NetworkFacility»
Atribut | Definiție | Tip | Voidability
linkingTime | Perioada de timp a legăturii. | TM_Object | voidable
7.2.4. Informare referitoare la actul juridic (ReportToLegalAct)
Informare privind implicarea unei «AbstractMonitoringFeature» în raportare. Informațiile sunt specifice în funcție de raportul transmis și nu în funcție de obligație/acord.
Atribute ale tipului de date «ReportToLegalAct»
Atribut | Definiție | Tip | Voidability
legalAct | «LegalAct» căruia i se raportează. | LegislationCitation |
reportDate | Momentul raportării. | DateTime | voidable
reportedEnvelope | Legătură la datele raportate stabilite în funcție de data indicată în atributul «reportDate». | URI | voidable
observationRequired | Indică dacă o observație este necesară pentru «AbstractMonitoringFeature». | Boolean | voidable
observingCapabilityRequired | Indică dacă «observingCapability» este necesară pentru «AbstractMonitoringFeature». | Boolean | voidable
description | Informații suplimentare privind datele efective raportate. | CharacterString | voidable
7.3. Liste de coduri
7.3.1. Regim de măsurare (MeasurementRegimeValue)
Categorii pentru diferite tipuri de «MeasurementRegime».
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind instalațiile de monitorizare a mediului.
7.3.2. Medii (MediaValue)
Categorii pentru diferite tipuri de medii.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind instalațiile de monitorizare a mediului.
7.3.3. Tip de proces (ProcessTypeValue)
Categorii pentru diferite tipuri de procese.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind instalațiile de monitorizare a mediului.
7.3.4. Scopul colectării (PurposeOfCollectionValue)
Categorii pentru diferite scopuri ale colecției.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
7.3.5. Sursa colectării de rezultate (ResultAcquisitionSourceValue)
Categorii pentru diferite tipuri de «ResultAcquisitionSource».
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind instalațiile de monitorizare a mediului.
7.3.6. Natura rezultatelor (ResultNatureValue)
Starea rezultatului unei observări.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind instalațiile de monitorizare a mediului.
7.3.7. Tipul de specializare a instalației de monitorizare a mediului (SpecialisedEMFTypeValue)
Categorii pentru diferite tipuri de «EnvironmentalMonitoringFacilities».
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
7.4. Straturi
Straturi pentru categoria de date spațiale «Environmental Monitoring Facilities»
Numele stratului | Titlul stratului | Tip de obiect spațial
EF.EnvironmentalMonitoringFacilities | Instalații de monitorizare a mediului | EnvironmentalMonitoringFacility
EF.EnvironmentalMonitoringNetworks | Rețele de monitorizare a mediului | EnvironmentalMonitoringNetwork
EF.EnvironmentalMonitoringProgrammes | Programe de monitorizare a mediului | EnvironmentalMonitoringProgramme
8. UNITĂȚI DE PRODUCȚIE ȘI INDUSTRIALE (PRODUCTION AND INDUSTRIAL FACILITIES)
8.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «emisie» (emission) înseamnă eliberarea directă sau indirectă, în aer, apă sau sol, de substanțe, vibrații, căldură sau zgomot din surse individuale sau difuze dintr-o instalație.
(2) «producție» (production) înseamnă o activitate care implică o serie de acțiuni sau operațiuni într-un context productiv.
8.2. Tipuri de obiecte spațiale
Pentru categoria de date spațiale «Unități de producție și industriale» sunt specificate următoarele tipuri de obiecte spațiale:
— Unitate de producție
— Instalație de producție
— Parte a instalației de producție
— Amplasament de producție
— Zonă de producție
— Clădire unde se desfășoară producția
8.2.1. Unitate de producție (ProductionFacility)
Una sau mai multe instalații de pe același amplasament, exploatate de aceeași persoană fizică sau juridică, proiectate, construite sau instalate în scopuri de producție sau în scopuri industriale, incluzând totalitatea infrastructurilor, echipamentelor și materialelor.
Acest tip este un subtip al «ActivityComplex».
Atribute ale tipului de obiect spațial «ProductionFacility»
Atribut | Definiție | Tip | Voidability
surfaceGeometry | Proprietate spațială a obiectului spațial. | GM_Surface | voidable
riverBasinDistrict | Identificator și/sau nume de cod atribuit bazinului hidrografic al unui curs de apă. | RiverBasinDistrictValue |
status | Statutul sau starea unității de producție, din punctul de vedere al ordinii funcționale sau operaționale în care aceasta este organizată pentru o perioadă de timp limitată. | StatusType | voidable
Roluri de asociere ale tipului de obiect spațial «ProductionFacility»
Rol de asociere | Definiție | Tip | Voidability
groupedBuilding | Clădiri administrate de unitatea de producție. | ProductionBuilding | voidable
groupedPlot | Zone administrate de unitatea de producție. | ProductionPlot | voidable
hostingSite | Amplasamente aflate în zona geografică unde este localizată unitatea de producție. | ProductionSite | voidable
groupedInstallation | Instalații care fac parte, atât din punct de vedere tehnic cât și juridic din instalația de producție. | ProductionInstallation | voidable
8.2.2. Instalație de producție (ProductionInstallation)
O unitate tehnică, cum ar fi utilaje, aparate, dispozitive sau echipamente, instalată sau conectat spre a fi utilizată.
Atribute ale tipului de obiect spațial «ProductionInstallation»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
thematicId | Identificator de obiect tematic. | ThematicIdentifier |
pointGeometry | Proprietate spațială a obiectului spațial. | GM_Point |
surfaceGeometry | Proprietate spațială a obiectului spațial. | GM_Surface | voidable
name | Denumirea oficială sau denumirea proprie sau convențională a instalației. | CharacterString | voidable
description | Declarație descriptivă referitoare la instalație. | CharacterString | voidable
status | Statutul sau starea instalației de producție, din punctul de vedere al ordinii funcționale sau operaționale în care aceasta este organizată pentru o perioadă de timp limitată. | StatusType | voidable
type | Tip special de instalație, menționând funcția operativă care trebuie îndeplinită. | InstallationType | voidable
Roluri de asociere ale tipului de obiect spațial «ProductionInstallation»
Rol de asociere | Definiție | Tip | Voidability
groupedInstallationPart | Instalații mai mici, care fac parte, din punct de vedere tehnic sau juridic, dintr-o instalație mare. | ProductionInstallationPart | voidable
8.2.3. Parte a instalației de producție (ProductionInstallationPart)
O singură unitate tehnică care îndeplinește funcționalități specifice legate de o activitate de producție.
Acest nivel de descriere cuprinde părți specifice ale instalației de producție, care trebuie să fie înregistrate prin mandatul legal al autorităților competente, inclusiv punctele de emisie înregistrate ca și coșuri industriale (pentru poluanți) sau rezervoare (pentru produse speciale).
Atribute ale tipului de obiect spațial «ProductionInstallationPart»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
thematicId | Identificator de obiect tematic. | ThematicIdentifier |
pointGeometry | Proprietate spațială a obiectului spațial. | GM_Point |
surfaceGeometry | Proprietate spațială a obiectului spațial. | GM_Surface | voidable
name | Denumirea oficială sau denumirea proprie sau convențională a părții instalației. | CharacterString | voidable
description | Declarație descriptivă referitoare la partea instalației. | CharacterString | voidable
status | Starea părții instalației, din punctul de vedere al ordinii funcționale sau operaționale în care aceasta este organizată pentru o perioadă de timp limitată. | StatusType | voidable
type | Tip special de parte a instalației, menționând funcția operativă care trebuie îndeplinită. | InstallationPartType | voidable
technique | Metodă de reducere a concentrației de poluanți provenind din emisiile unei componente tehnice, de regulă un coș industrial. | PollutionAbatementTechniqueValue | voidable
8.2.4. Amplasament de producție (ProductionSite)
Tot terenul dintr-o zona geografică dată unde a fost, este sau se intenționează a fi localizată producția. Este inclusă totalitatea infrastructurilor, echipamentelor și materialelor.
Atribute ale tipului de obiect spațial «ProductionSite»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
thematicId | Identificator de obiect tematic. | ThematicIdentifier |
geometry | Proprietate spațială a obiectului spațial. | GM_MultiSurface |
sitePlan | Declarație descriptivă cu privire la proiectul privind configurația și organizarea amplasamentului de producție. | DocumentCitation | voidable
name | Denumirea oficială sau denumirea proprie sau convențională a amplasamentului. | CharacterString | voidable
description | Declarație descriptivă referitoare la amplasament. | CharacterString | voidable
status | Starea amplasamentului de producție, din punctul de vedere al ordinii funcționale sau operaționale în care acesta este organizat pentru o perioadă de timp limitată. | StatusType | voidable
8.2.5. Zonă de producție (ProductionPlot)
O porțiune de teren sau de apă ale unei unități de producție menită să servească unor scopuri funcționale.
Atribute ale tipului de obiect spațial «ProductionPlot»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
thematicId | Identificator de obiect tematic. | ThematicIdentifier |
geometry | Proprietate spațială a obiectului spațial. | GM_Surface |
status | Starea zonei de producție, din punctul de vedere al ordinii funcționale sau operaționale în care acesta este organizat pentru o perioadă de timp limitată. | StatusType | voidable
8.2.6. Clădire unde se desfășoară producția (ProductionBuilding)
Construcție artificială, constituind parte a unei unități de producție, care este utilizată pentru a găzdui sau a adăposti desfășurarea de activități.
Atribute ale tipului de obiect spațial «ProductionBuilding»
Atribut | Definiție | Tip | Voidability
thematicId | Identificator de obiect tematic. | ThematicIdentifier |
typeOfBuilding | Descrieree clasificată a clădirii unde se desfășoară activități de producție și industriale. | TypeOfProductionBuildingValue | voidable
status | Starea clădirii unde se desfășoară activități de producție și industriale, din punctul de vedere al ordinii funcționale sau operaționale în care aceasta este aranjată pentru o perioadă de timp limitată. | StatusType | voidable
geometry | Proprietate spațială a obiectului spațial. | GM_Object | voidable
Roluri de asociere ale tipului de obiect spațial «ProductionBuilding»
Rol de asociere | Definiție | Tip | Voidability
building | Reprezentare a clădirii unde se desfășoară producția în cadrul unui set de date referitoare la «Clădiri». | AbstractBuilding | voidable
Constrângeri ale tipului de obiect spațial «Building» în care se desfășoară producția
Geometria trebuie să fie furnizată în cazul în care proprietatea clădirii este goală.
8.3. Tipuri de date
8.3.1. Tipul statutului (StatusType)
Starea unei componente tehnice, din punctul de vedere al ordinii funcționale sau operaționale în care aceasta este organizată pentru o perioadă de timp limitată sau extinsă.
Atribute ale tipului de date «StatusType»
Atribut | Definiție | Tip | Voidability
statusType | Starea unei componente tehnice în funcție de o listă de valori potențiale predefinite. | ConditionOfFacilityValue |
description | Declarație descriptivă referitoare la statutul declarat. | CharacterString | voidable
validFrom | Momentul de începere a valabilității unui tip de statut. | Date | voidable
validTo | Momentul de încheiere a valabilității unui tip de statut. | Date | voidable
8.4. Liste de coduri
8.4.1. Tehnică de reducere a poluării (PollutionAbatementTechniqueValue)
Metode de reducere a concentrației de poluanți provenind din emisiile unei componente tehnice, de regulă un coș industrial.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «PollutionAbatementTechniqueValue»
Valoare | Nume | Definiție
gravitation | gravitație | Reducere a poluanților ca urmare a gravitației
dustScrubbers | scrubere cu apă | Reducerea poluanților cu ajutorul scruberelor cu apă
filtration | filtrare | Reducerea poluanților prin filtrare
condensation | condensare | Reducerea poluanților prin condensare
adsorption | adsorbție | Reducerea poluanților prin adsorbție
8.4.2. Tipul instalației (InstallationTypeValue)
Valori care indică funcția operativă care trebuie îndeplinită de o instalație. Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
8.4.3. Tipul părții instalației (InstallationPartTypeValue)
Valori care indică funcția operativă care trebuie îndeplinită de o parte a instalației. Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
8.4.4. District hidrografic (RiverBasinDistrictValue)
Identificatori și/sau nume de cod atribuite bazinelor hidrografice. Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
8.4.5. Tipul clădirii în care se desfășoară producția (TypeOfProductionBuildingValue)
Clasificarea clădirilor de producție și industriale.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
8.5. Straturi
Straturi pentru categoria de date spațiale «Unități de producție și industriale»
Numele stratului | Titlul stratului | Tip de obiect spațial
PF.ProductionSite | Amplasament industrial și de producție | ProductionSite
PF. <ValoaredinListadeCoduri>(5) | <nume lizibil de către om> | ProductionFacility
Exemplu: PF.Manufacturing | Exemplu: Fabricare | (activity: EconomicActivityValue)
PF.ProductionPlot | Zonă de producție și industrială | ProductionPlot
PF.ProductionInstallation | Instalație de producție și industrială | ProductionInstallation
PF.ProductionInstallationPart | Parte a unei instalații de producție și industriale | ProductionInstallationPart
PF.ProductionBuilding | Clădire în care se desfășoară activități industriale și de producție | ProductionBuilding
9. UNITĂȚI AGRICOLE ȘI DE ACVACULTURĂ (AGRICULTURAL AND AQUACULTURE FACILITIES)
9.1. Definiții
Pe lângă definițiile stabilite în articolul 2, se aplică următoarele definiții:
(1) «agricultură» (agriculture) înseamnă setul de procese și activități care constau în cultivarea solurilor, producția de culturi și creșterea animalelor; printre alte activități se numără recoltarea, mulsul, creșterea animalelor și deținerea de animale în scopuri agricole. În conformitate cu Regulamentul (CE) nr. 73/2009 al Consiliului, menținerea terenurilor în bune condiții agricole și de mediu este considerată ca fiind o activitate agricolă.
(2) «animale de crescătorie» (livestock) înseamnă animalele reproduse și/sau crescute în vederea utilizării lor și a realizării de profit (vizate de activitățile definite în codurile CAEN A.1.4. și A.1.5).
(3) «acvacultură» (aquaculture) înseamnă setul de activități și tehnici aferente producției, reproducerii și tratării peștilor, moluștelor, algelor de mare și a altor specii de resurse acvatice (vegetale sau animale).
9.2. Tipuri de obiecte spațiale
Pentru categoria de date spațiale «Unități agricole și de acvacultura» sunt specificate următoarele tipuri de obiecte spațiale:
— Exploatație
— Site
9.2.1. Exploatație (Holding)
Întreaga zonă și toate infrastructurile conexe, care acoperă aceleași «amplasamente» (sau altele), aflate sub controlul unui exploatator responsabil cu desfășurarea de activități agricole sau de acvacultură.
Acest tip este un subtip al «ActivityComplex».
Roluri de asociere ale tipului de obiect spațial «Holding»
Atribut | Definiție | Tip | Voidability
contains | Siturile care fac parte din «Exploatația» specificată. | Site |
Constrângeri ale tipului de obiect spațial «Holding»
Cel puțin unul dintre atributele referitoare la funcție ale obiectului spațial «Exploatație» trebuie să fie furnizat cu ajutorul listei de coduri «EconomicActivityNACEValue» (pentru atributul referitor la activitate al tipului de date «Funcție»).
9.2.1.1. Amplasament (Site)
Totalitatea terenului din aceeași zonă geografică distinctă (sau o alta), aflată sub controlul managerial al unei exploatații acoperind activități, produse și servicii. Este inclusă totalitatea infrastructurilor, echipamentelor și materialelor.
Atribute ale tipului de obiect spațial «Site»
Atribut | Definiție | Tip | Voidability
geometry | Geometrie care definește extinderea sau poziția sitului. | GM_Object |
activity | Clasificarea activității economice desfășurată în cadrul sitului, în conformitate cu codificarea CAEN rev. 2.0. | EconomicActivityNACEValue |
includesAnimal | Prezența animalelor în cadrul sitului. | FarmAnimalSpecies | voidable
9.3. Tipuri de date
9.3.1. Specii de animale de fermă (FarmAnimalSpecies)
Identifică un animal sau un grup de animale («Animale de crescătorie» sau «Acvacultură») din aceeași specie, crescute pe un anumit sit.
Atribute ale tipului de date «FarmAnimalSpecies»
Atribut | Definiție | Tip | Voidability
livestock | Prezența de specii de animale de crescătorie în cadrul sitului. | LivestockSpeciesValue | voidable
aquaculture | Prezența de specii de acvacultură în cadrul sitului. | AquacultureSpeciesValue | voidable
9.4. Liste de coduri
9.4.1. Specii de animale de crescătorie (LivestockSpeciesValue)
Clasificarea speciilor de animale de crescătorie.
Valorile permise pentru această listă de coduri cuprind valorile specificate în anexa II la Regulamentul (CE) nr. 1165/2008 (6) și valori suplimentare la orice nivel definit de furnizorii de date.
9.4.2. Specii de acvacultură (AquacultureSpeciesValue)
Clasificarea speciilor de acvacultură.
Valorile permise pentru această listă de coduri cuprind numai valorile specificate în versiunea din februarie 2012 a ASFIS (Aquatic Sciences and Fisheries Information System) List of Species for Fishery Statistics Purposes published by the Food and Agriculture Organization of the United Nations.
9.5. Straturi
Straturi pentru categoria de date spațiale «Unități agricole și de acvacultură»
Numele stratului | Titlul stratului | Tip de obiect spațial
AF. AgriculturalHolding | Exploatație agricolă | Exploatație (obiecte spațiale al căror atribut privind activitatea are valoarea = «A1 - Crop and animal production, hunting and related service activities» [din lista de coduri «EconomicActivityNACEValue») sau o valoare mai restrânsă]
AF. AquacultureHolding | Exploatație de acvacultură | Exploatație (obiect spațial al cărui atribut privind activitatea are valoarea «A3 - Fishing and aquaculture activities» [din lista de coduri «EconomicActivityNACEValue») sau o valoare mai restrânsă]
AF.Site | Situri agricole și de acvacultură | Site
10. DISTRIBUȚIA POPULAȚIEI – DEMOGRAFIA (POPULATION DISTRIBUTION – DEMOGRAPHY)
10.1. Tipuri de obiecte spațiale
Pentru categoria de date spațiale «Distribuția populației - demografie» este specificat următorul tip de obiect spațial: distribuție statistică.
10.1.1. Distribuție statistică (StatisticalDistribution)
Set de măsuri care descriu modul în care un fenomen este răspândit într-o anumită parte a lumii în 2D.
Atribute ale tipului de obiect spațial «StatisticalDistribution»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
areaOfDissemination | Parte a lumii în 2D pe care o descrie «StatisticalDataDistribution». | GM_Surface |
universe | Atunci când distribuția este legată de un subansamblu al populației și nu de populație în întregul său, descrierea literală a modului în care a fost definit acest subansamblu. | PT_FreeText |
domain | Parte a informațiilor statistice la care se referă datele. | PT_FreeText |
measure | Măsura care face obiectul distribuției. | VariableValue |
measurementMethod | Descrierea metodei statistice de măsurare. | StatisticsMeasurementMethodValue |
measurementUnit | Unitatea de măsurare. | UnitOfMeasure |
notCountedProportion | Parte a populației din zona de interes care nu este luată în considerare în niciuna dintre componentele sale spațiale. | Number |
periodOfMeasurement | Data sau perioada în care au fost făcute observațiile sau au fost colectate datele. | TM_Period |
periodOfReference | Perioada în care datele ar trebui să ofere o imagine a zonei de interes. | TM_Period |
periodOfValidity | Perioada în care datele continuă să rămână relevante. | TM_Period |
beginLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
generalStatus | Statutul distribuției de date statistice. | StatisticalDataStatusValue |
Roluri de asociere ale tipului de obiect spațial «StatisticalDistribution»
Rol de asociere | Definiție | Tip | Voidability
value | Valorile statistice care alcătuiesc distribuția. | StatisticalValue |
classification | Clasificări suplimentare utilizate pentru a diviza o valoare totală a fenomenului descris. Obiectul «StatisticalDistribution» va furniza de fapt mai multe distribuții, una pentru fiecare element al clasificării utilizate. În cazul în care nu se oferă nicio clasificare, valoarea statistică este populația totală. | Classification |
10.2. Tipuri de date
10.2.1. Clasificare (Classification)
O clasificare utilizată pentru o distribuție statistică.
Atribute ale tipului de date «Classification»
Atribut | Definiție | Tip | Voidability
type | Tipul de clasificare. | ClassificationTypeValue |
Roluri de asociere ale tipului de date «Classification»
Rol de asociere | Definiție | Tip | Voidability
item | Elementele care alcătuiesc clasificarea. | ClassificationItem |
10.2.2. Element al clasificării (ClassificationItem)
Un element care alcătuiește o clasificare.
Atribute ale tipului de date «ClassificationItem»
Atribut | Definiție | Tip | Voidability
type | Tipul de element al clasificării. | ClassificationItemTypeValue |
10.2.3. Valoare statistică (StatisticalValue)
Datele elementare ale distribuției.
Atribute ale tipului de date «StatisticalValue»
Atribut | Definiție | Tip | Voidability
value | Valoarea datei elementare. | Number |
specialValue | Un șir convențional atunci când valoarea datei elementare nu poate fi furnizată: Valoare lipsă, valoare ascunsă din motive de confidențialitate. | SpecialValue |
conventionallyLocatedProportion | Parte a populației luată în considerare în data elementară, dar care nu poate fi localizată fizic în zona de interes. | Number |
approximatelyLocatedPopulationProportion | Parte a numărării populației care nu respectă regulile comune de localizare. Prin «populație» se pot înțelege persoane, dacă obiectul numărării sunt persoanele, locuințe dacă «StatisticalDatadistribution» are drept obiect locuințele etc. | Number |
comment | Comentariu în stil liber privind valoarea. | PT_FreeText |
flags | Un set de observații codificate formate dintr-un singur caracter referitoare la date. | PT_FreeText |
periodOfMeasurement | Perioada de colectare a valorii statistice. Această perioadă are prioritate asupra perioadei specificate în distribuția statistică asociată. | TM_Period | voidable
status | Statutul datelor statistice. | StatisticalDataStatusValue |
Roluri de asociere ale tipului de date «StatisticalValue»
Rol de asociere | Definiție | Tip | Voidability
dimensions | Parte a lumii la care data elementară face trimitere. Dimensiunile conțin o descriere a localizării geografice (dimensiune 2D), împreună cu posibilele dimensiuni suplimentare atunci când au loc numărări ale populației simultane pentru caracteristici individuale diferite. | Dimensions |
Constrângeri ale tipului de date «StatisticalValue»
Trebuie să se furnizeze fie valoarea, fie atributul «specialValue».
10.2.4. Dimensiuni (Dimensions)
Identificarea obiectivului la care se referă data elementară, din punctul de vedere al localizării geografice sau al caracteristicilor individuale.
Roluri de asociere ale tipului de date «Dimensions»
Rol de asociere | Definiție | Tip | Voidability
spatial | Dimensiunea spațială a valorii statistice. | StatisticalUnit |
thematic | Dimensiunile tematice ale valorii statistice. | ClassificationItem |
10.3. Liste de coduri
10.3.1. Tipul clasificării (ClassificationTypeValue)
Valorile codurilor pentru tipurile de clasificare.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind distribuția populației.
10.3.2. Tipul elementelor de clasificare (ClassificationItemTypeValue)
Valorile codurilor pentru elementele de clasificare.
Valorile permise pentru această listă de coduri cuprind valorile următoarelor liste de coduri sau alte liste de coduri indicate de furnizorii de date:
— Vârsta de până la 5 ani (AgeBy5YearsValue): Valorile codurilor pentru elementele de clasificare aferente vârstei de până la 5 ani, astfel cum se specifică în tabelul de mai jos.
Valori pentru lista de coduri «AgeBy5Years»
Valoare | Nume | Definiție
0-5 | 0-5 | 0 la mai puțin de 5
5-10 | 5-10 | 5 la mai puțin de 10
10-15 | 10-15 | 10 la mai puțin de 15
15-20 | 15-20 | 15 la mai puțin de 20
20-25 | 20-25 | 20 la mai puțin de 25
25-30 | 25-30 | 25 la mai puțin de 30
30-35 | 30-35 | 30 la mai puțin de 35
35-40 | 35-40 | 35 la mai puțin de 40
40-45 | 40-45 | 40 la mai puțin de 45
45-50 | 45-50 | 45 la mai puțin de 50
50-55 | 50-55 | 50 la mai puțin de 55
55-60 | 55-60 | 55 la mai puțin de 60
60-65 | 60-65 | 60 la mai puțin de 65
65-70 | 65-70 | 65 la mai puțin de 70
70-75 | 70-75 | 70 la mai puțin de 75
75-80 | 75-80 | 75 la mai puțin de 80
80-85 | 80-85 | 80 la mai puțin de 85
85-90 | 85-90 | 85 la mai puțin de 90
90+ | 90 | 90 de ani și peste
90-95 | 90-95 | 90 la mai puțin de 95
95+ | 95 | 95 de ani și peste
95-100 | 95-100 | 95 la mai puțin de 100
100+ | 100 | 100 de ani și peste
— Vârsta în funcție de ani (AgeByYearValue): Valorile codurilor pentru elementele de clasificare aferente vârstei în funcție de ani, inclusiv o valoare pentru fiecare interval de un an. Prima valoare trebuie să fie «0-1» cu eticheta «0-1» și definiția «0 la mai puțin de 1 an», iar ultima valoare trebuie să fie «100+» cu eticheta «100+» și definiția «100 de ani sau mai mult».
— Codul CAEN (NACECodeValue): Clasificarea activităților economice, în conformitate cu CAEN al Eurostat, astfel cum se precizează în Regulamentul (CE) nr. 1893/2006 al Parlamentului European și al Consiliului și valori mai restrânse definite de furnizorii de date.
— Sex (GenderValue): Sexul unei persoane sau al unui grup de persoane, după cum se precizează în secțiunea 4.6 din anexa I.
10.3.3. Variabilă (VariableValue)
Valorile codurilor pentru numele variabilelor.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind Distribuția populației - demografie.
10.3.4. Metoda de măsurare statistică (StatisticsMeasurementMethodValue)
Valorile codurilor pentru metoda de măsurare statistică.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «StatisticsMeasurementMethodValue»
Valoare | Nume | Definiție
count | numărare | O simplă numărare.
relativeCount | numărare relativă | Un raport care combină două tipuri de populație statistică.
percentage | procentaj | O proporție exprimată ca raport cu numitorul 100.
median | mediană | Mediana.
10.3.5. Statutul datelor statistice (StatisticalDataStatusValue)
Valorile codurilor pentru statut.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valorile pentru lista de coduri «StatisticalDataStatusValue»
Valoare | Nume | Definiție
definitive | definitivă | O valoare definitivă a datelor statistice.
final | finală | O valoare finală a datelor statistice.
preliminary | preliminară | O valoare preliminară a datelor statistice.
provisional | provizorie | O valoare provizorie a datelor statistice.
semiDefinitive | semi-definitivă | O valoare semi-definitivă a datelor statistice.
10.3.6. Valoare specială (SpecialValue)
Valorile codurilor pentru valori speciale.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «SpecialValue»
Valoare | Nume | Definiție
confidential | confidențială | Valoarea nu este făcută cunoscută din motive de confidențialitate.
unknown | necunoscută | Valoarea ar fi putut fi măsurată, dar acest lucru nu s-a întâmplat.
notApplicable | nu se aplică | Valoarea nu ar avea niciun sens.
10.4. Straturi
Pentru categoria de date spațiale «Distribuția populației și demografia» nu sunt definite straturi.
11. ZONE DE GESTIONARE/DE RESTRICȚIONARE/DE REGLEMENTARE ȘI UNITĂȚI DE RAPORTARE (AREA MANAGEMENT/RESTRICTION/REGULATION ZONES AND REPORTING UNITS)
11.1. Definiții
Pe lângă definițiile stabilite în articolul 2, se aplică următoarele definiții:
(1) «a gestiona» (manage) înseamnă a planifica, a desfășura, a monitoriza și a controla activități cu scopul de a atinge obiective de mediu specifice definite de lege.
(2) «a restricționa» (restrict) înseamnă a interzice sau a limita anumite activități, care să fie întreprinse numai în limite și/sau pe perioade de timp specifice, pentru a atinge un anumit obiectiv în conformitate cu responsabilități sau obligații bine definite de lege.
(3) «a reglementa» (regulate) înseamnă a monitoriza și a controla anumite activități (de autorizare, promovare, interzicere sau restricționare), pentru a atinge obiective de mediu definite de lege. O activitate reglementată poate necesita ca, în cazul în care calitatea mediului se degradează, să fie luate o serie de măsuri specifice pentru a reveni la starea ecologică bună.
(4) «a raporta» (report) înseamnă a evalua eficacitatea politicilor de mediu și a publica date și informații (și anume, date spațiale, observații, statistici, indicatori) care ar putea fi utilizate pentru a evalua progresele înregistrate în privința menținerii sau îmbunătățirii calității mediului și atingerea obiectivelor de politică.
(5) «unitate de raportare» (reporting unit) înseamnă un obiect spațial care furnizează referința spațială pentru orice date nespațiale schimbate în temeiul obligațiilor de raportare de mediu.
(6) «instrument juridic» (legal instrument) înseamnă un document care precizează obligațiile legale, inclusiv, dar fără a se limita la, convențiile internaționale, legislația și actele juridice sau regulamentele de punere în aplicare la orice nivel administrativ.
(7) «gestionarea integrată a zonelor costiere» (integrated coastal zone management) înseamnă un proces dinamic de gestionare și utilizare a zonelor costiere, ținând seama, în același timp, de fragilitatea ecosistemelor și peisajelor costiere, de diversitatea activităților și utilizărilor, de interacțiunile acestora, de orientarea maritimă a anumitor activități și de utilizări și impactul acestora atât pe mare, cât și pe uscat.
(8) «climă» (climate) înseamnă descrierea statistică în ceea ce privește media și variabilitatea cantităților relevante pe o perioadă de timp, variind de la luni la câteva mii sau milioane de ani. Aceste cantități sunt, de cele mai multe ori, variabile de suprafață, cum ar fi temperatura, precipitațiile și vântul.
11.2. Tipuri de obiecte spațiale
Pentru categoria de date spațiale «Zone de gestionare/de restricționare/de reglementare și unități de raportare», trebuie să se specifice următorul tip de obiect spațial: «Zonă de gestionare, de restricție sau de reglementare».
11.2.1. Zonă de gestionare, de restricționare sau de reglementare (ManagementRestrictionOrRegulationZone)
Zonă gestionată, restricționată sau reglementată în conformitate cu o cerință legală referitoare la o politică de mediu sau la o politică sau activitate care ar putea avea un impact asupra mediului la orice nivel administrativ (internațional, european, național, regional și local).
Atribute ale tipului de obiect spațial «ManagementRestrictionOrRegulationZone»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
thematicId | Identificator descriptiv de obiect unic aplicat obiectelor spațiale într-o categorie informațională definită. | ThematicIdentifier | voidable
name | O denumire geografică utilizată pentru a identifica zona de gestionare, restricționare sau reglementare din realitate. Acesta furnizează cheia de asociere în mod implicit a diferitelor reprezentări ale obiectului. | GeographicalName | voidable
geometry | Geometria reprezentând extinderea spațială a obiectului spațial. | GM_Object |
zoneType | Clasificare de nivel înalt care definește tipul de zonă de gestionare, de restricționare sau de reglementare. | ZoneTypeCode |
specialisedZoneType | Valoare a clasificării suplimentare care conferă caracterul special al tipului de zonă de gestionare, de restricționare sau de reglementare relevantă pentru domeniul respectiv. | SpecialisedZoneTypeCode | voidable
environmentalDomain | Clasificarea domeniului (domeniilor) de mediu în cazul cărora, prin instituirea zonei, anumite obiective de mediu urmează să fie atinse. | EnvironmentalDomain |
designationPeriod | Perioada de timp în care zona de gestionare, de restricționare sau de reglementare a fost desemnată legal sau a devenit efectivă în realitate. | TM_Period | voidable
competentAuthority | Descrierea organizației (organizațiilor), responsabile cu măsurile sau activitățile de gestionare, restricționare sau reglementare din zona respectivă. | RelatedParty | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «ManagementRestrictionOrRegulationZone»
Rol de asociere | Definiție | Tip | Voidability
legalBasis | Trimitere la, sau citare din, instrumentul juridic sau documentul care a necesitat instituirea zonei. | LegislationCitation | voidable
relatedZone | Trimitere la o zonă conexă de gestionare, reglementare sau restricționare. | ManagementRestrictionOrRegulationZone | voidable
plan | Trimitere la, sau citare dintr-un plan (plan de gestionare sau de acțiune) care descrie obiectivele și măsurile de mediu care urmează să fie întreprinse în zonă pentru a asigura protecția mediului. | DocumentCitation | voidable
Constrângeri ale tipului de obiect spațial «ManagementRestrictionOrRegulationZone»
Trebuie să se furnizeze cel puțin instrumentul juridic cel mai specific care a prevăzut instituirea zonei, utilizându-se rolul de asociere «legalBasis».
Atributul «role» al «competentAuthority» ia valoarea «authority».
11.3. Liste de coduri
11.3.1. Codul tipului de zonă (ZoneTypeCode)
Clasificare de nivel înalt care definește tipul de zonă de gestionare, de restricționare sau de reglementare.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «ZoneTypeCode»
Valoare | Nume | Definiție
airQualityManagementZone | zonă de gestionare a calității aerului | Parte a teritoriului unui stat membru, astfel cum este delimitată de acesta în scopul evaluării și gestionării calității aerului.
noiseRestrictionZone | zonă de restricție în materie de zgomot | O zonă delimitată de autoritatea competentă pentru a gestiona și reduce poluarea sonoră. Aceasta include aglomerările și zonele liniștite (din cadrul aglomerărilor și din spațiu deschis), astfel cum sunt definite în Directiva 2002/49/CE a Parlamentului European și a Consiliului.
animalHealthRestrictionZone | zonă de restricție în materie de sănătate animală | Zone de restricție stabilite pentru controlul și eradicarea bolilor animalelor cu notificare obligatorie
prospectingAndMiningPermitArea | zonă de autorizare a prospectării și a mineritului | zona în care a fost autorizată prospectarea sau extracția oricărui mineral și pentru care se acordă acest drept sau autorizație.
regulatedFairwayAtSeaOrLargeInlandWater | șenal navigabil reglementat pe mare sau pe căi navigabile interioare mari | Zone maritime de navigație interportuară stabilite pentru a organiza traficul, a preveni accidentele și poluarea, precum și pentru a sprijini gestionarea și planificarea.
restrictedZonesAroundContaminatedSites | zone de restricție în jurul siturilor contaminate | Zone stabilite pentru a proteja sănătatea umană, a plantelor și a animalelor, precum și pentru a controla circulația și dezvoltarea în cadrul unui sit contaminat.
areaForDisposalOfWaste | zonă de eliminare a deșeurilor | Zonă afectată de eliminarea deșeurilor, astfel cum se definește la articolul 3 alineatul (19) din Directiva 2008/98/CE(7).
coastalZoneManagementArea | zonă de gestionare a regiunilor costiere | Zonă în care are loc gestionarea integrată a regiunilor costiere.
drinkingWaterProtectionArea | zonă de protecție a surselor de apă potabilă | Zonă în care scurgerile de ape uzate, utilizarea îngrășămintelor artificiale sau a pesticidelor sau instituirea de situri de depozitare a deșeurilor sunt interzise.
nitrateVulnerableZone | zonă vulnerabilă la nitrați | Suprafețe de teren care drenează în ape poluate sau în pericol și care contribuie la poluarea cu nitrați.
marineRegion | regiune marină | Regiunile marine și subregiunile acestora sunt regiuni desemnate în temeiul legislației internaționale, a Uniunii, naționale sau regionale în scopul evaluării, gestionării și reglementării.
riverBasinDistrict | district hidrografic | Zonă de uscat și mare, formată din una sau mai multe bazine hidrografice învecinate, precum și din apele subterane și apele costiere conexe, identificate în temeiul articolului 3 alineatul (1) din Directiva 2000/60/CE(8) ca fiind principala unitate de gestionare a bazinelor hidrografice.
bathingWaters | ape pentru scăldat | Ape costiere sau ape interioare (râuri, lacuri) autorizate în mod explicit pentru scăldatul recreativ de către un mare număr de persoane sau care nu fac obiectul unei interdicții în acest sens.
floodUnitOfManagement | unitate de gestionare a inundațiilor | Zonă de uscat și mare, identificată în temeiul Directivei 2007/60/CE a Parlamentului European și Consiliului(9), ca fiind principala unitate de gestionare atunci când se alege o alternativă la districtele sau sub-districtele hidrografice.
waterBodyForWFD | corp de apă în temeiul Directivei-cadru privind apa (2000/60/CE) | «Corpul de apă» reprezintă o subunitate a bazinului (districtului) hidrografic căreia i se aplică obiectivele de mediu ale Directivei 2000/60/CE. Identificarea corpurilor de apă se bazează pe factori determinanți geografice și hidrologici. Printre acestea se numără include corpuri de apă de suprafață (râuri, lacuri, ape de tranziție și costiere) și corpuri de apă subterane.
sensitiveArea | zonă sensibilă | Corpuri de apă identificate ca zone sensibile, astfel cum sunt definite în anexa II la Directiva 91/271/CEE(10).
designatedWaters | ape desemnate | Ape maritime, costiere sau de suprafață desemnate de către statele membre ca necesitând protecție sau îmbunătățiri pentru a întreține resursele piscicole.
plantHealthProtectionZone | zonă de protecție a plantelor | Zona de protecție în care sunt stabilite măsuri de protecție împotriva introducerii de organisme dăunătoare plantelor sau produselor din plante și împotriva răspândirii lor.
forestManagementArea | zonă de gestionare a pădurilor | Zonă desemnată pentru gestionarea durabilă a resurselor și funcțiilor forestiere.
11.3.2. Codul tipului de zonă specializată (SpecialisedZoneTypeCode)
Valoarea clasificării suplimentare care definește tipul specializat de zonă.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
11.3.3. Domeniu al mediului (EnvironmentalDomain)
Domeniul al mediului, în cazul căruia pot fi definite obiective de mediu.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «EnvironmentalDomain»
Valoare | Nume | Definiție
soil | sol | Stratul superior al suprafeței terestre care este alcătuit din particule de rocă dezintegrată, humus, apă și aer.
noise | zgomot | Sunet nedorit, fie ca urmare a efectelor sale asupra oamenilor, asupra oboselii sau funcționării necorespunzătoare a echipamentelor fizice, fie ca urmare a interferenței sale cu perceperea sau detectarea altor sunete.
naturalResources | resurse naturale | O caracteristică sau o componentă a mediului natural, valoroasă în ceea ce privește deservirea nevoilor umane, de exemplu, sol, apă, floră, faună etc. Unele resurse naturale au o valoare economică (de exemplu lemnul), în timp ce altele au o valoare de natură «neeconomică» (de exemplu frumusețea peisajelor).
climateAndClimateChange | climă și schimbări climatice | Starea climei și/sau a schimbărilor climatice care poate fi identificată (de exemplu prin utilizarea încercărilor statistice) prin urmărirea schimbărilor în ceea ce privește valorile medii și/sau variabilitatea proprietăților, și care persistă pentru o perioadă lungă, de regulă, decenii sau mai mult.
healthProtection | protecția sănătății | Măsuri sau dispozitive concepute pentru a reduce riscurile pentru sănătatea umană cauzate de poluanți sau de alte condiții nefavorabile din cadrul ecosistemului.
air | aer | Un amestec predominant mecanic dintr-o varietate de gaze individuale care formează atmosfera terestră înconjurătoare.
water | apă | Lichid comun (H2O) care dă naștere la ploaie, râuri, mare etc., și care reprezintă o parte importantă din corpurile organismelor.
waste | deșeuri | Material, adesea inutilizabil, rămas nefolosit în urma unor procese de fabricare, industriale, agricole sau umane; material deteriorat sau modificat pe parcursul unui proces de fabricație și neutilizat ulterior.
natureAndBiodiversity | natură și biodiversitate | Gestionarea activă a resursele terestre naturale și a mediului pentru a asigura menținerea calității acestora și utilizarea lor în mod rațional.
sustainableDevelopment | dezvoltare durabilă | Dezvoltare care oferă beneficii economice, sociale și de mediu pe termen lung, având în vedere nevoile generațiilor actuale și ale celor viitoare.
landUse | utilizarea terenului | Termenul de utilizare a terenului se referă la aspectele spațiale ale tuturor activităților umane de pe uscat și la modul în care suprafața solului suferă sau ar putea suferi modificări pentru a servi nevoilor umane.
11.4. Cerințe specifice categoriei
11.4.1. Zone de gestionare, de restricționare sau de reglementare
| (1) | În cazul în care geometria obiectului spațial este derivată dintr-un alt obiect spațial, geometriile celor două obiecte trebuie să fie în concordanță.
| (2) | În cazul în care geometriile obiectelor spațiale dintr-un set de date «ManagementRestrictionOrRegulationZone» sunt derivate din geometriile obiectelor spațiale dintr-un alt set de date, atunci acest set de date sursă (inclusiv versiunea sa) este descris ca parte din elementul de metadate aferent filiației.
| (3) | Furnizorii de date trebuie să includă următoarele cuvinte-cheie în plus față de cuvintele-cheie obligatorii definite în Regulamentul (CE) nr. 1205/2008/CE: (a) Unul sau mai multe cuvinte-cheie care să descrie clasificarea la nivel înalt a tipului (tipurilor) de zone incluse în setul de date, astfel cum sunt definite în lista de coduri «ZoneTypeCode». (b) Se stabilește unul sau mai multe cuvinte-cheie care să descrie numărul (numerele) documentului oficial al instrumentului (instrumentelor) juridic(e) inclus(e) în setul de date. Pentru legislația Uniunii, se utilizează numărul CELEX.
11.4.2. Unități de raportare
| (1) | Obiectele spațiale care acționează ca unități de raportare sunt definite și puse la dispoziție în conformitate cu cerințele din categoria (categoriile) respective de date spațiale INSPIRE.
| (2) | În cazul în care, pentru a stabili o referință spațială, datele de raportare privind mediul se referă la entități reale care sunt puse la dispoziție ca obiecte spațiale în conformitate cu acest regulament, datele de raportare trebuie să includă o trimitere explicită la obiectele spațiale în cauză.
11.4.3. Cerințe valabile pentru toate categoriile
| (1) | În cazul în care o zonă a fost desemnată în scopul exclusiv de a gestiona, reglementa și restricționa activități pentru a conserva natura, biodiversitatea și patrimoniul cultural, aceasta este pusă la dispoziție ca obiect spațial «ProtectedSite». În cazul în care o zonă a fost desemnată pentru a îndeplini obiective multiple, inclusiv conservarea naturii, a biodiversității și a patrimoniului cultural, aceasta trebuie pusă la dispoziție ca obiect spațial «ManagementRestrictionOrRegulationZone».
| (2) | În cazul în care o zonă a fost desemnată pentru a reglementa utilizarea planificată a terenului și definită în cadrul unui plan spațial obligatoriu din punct de vedere juridic, aceasta intră în sfera de aplicare a categoriei «Utilizarea terenului» și trebuie codificată ca o «SupplementaryRegulation». Cu toate acestea, în cazul în care zona a fost desemnată prin cerință legislativă însă ea nu a fost definită în cadrul unui plan spațial obligatoriu din punct de vedere juridic, aceasta trebuie codificată ca o «ManagementRestrictionOrRegulationZone».
11.5. Straturi
Straturi pentru categoria de date spațiale «Zone de gestionare /de restricționare/de reglementare și unități de raportare»
Numele stratului | Titlul stratului | Tip de obiect spațial
AU.<ValoaredinListadeCoduri>(11) | <nume lizibil de către om> | ManagementRestrictionOrRegulationZone (zoneType: ZoneTypeCode)
Exemplu: AM.AirQualityManagementZone | Exemplu: Zonă de gestionare a calității aerului |
12. ZONE DE RISC NATURAL (NATURAL RISK ZONES)
12.1. Definiții
Pe lângă definițiile stabilite în articolul 2, se aplică următoarele definiții:
(1) «risc» (risk) înseamnă combinația dintre consecințele unui eveniment (hazard) și posibilitatea/probabilitatea producerii acestuia, în conformitate cu ISO/IEC 31010:2009.
(2) «hazard» (hazard) înseamnă un fenomen, o substanță, o activitate umană sau o stare de lucruri periculoasă care poate avea ca efect pierderi de vieți, răniri sau alte efecte asupra sănătății, pagube materiale, pierderea de mijloace de subzistență și pierderea de servicii, perturbări sociale și economice sau daune de mediu.
(3) «expunere» (exposure) înseamnă persoane, bunuri, sisteme sau alte elemente care sunt prezente în zonele de hazard și care, prin urmare, pot fi afectate de eventuale pierderi.
(4) «vulnerabilitate» (vulnerability) înseamnă caracteristicile și circumstanțele unei comunități, ale unui sistem sau ale unui bun care le fac susceptibile la efectele nocive ale unui hazard.
12.2. Tipuri de obiecte spațiale
Pentru categoria de date spațiale «Zone de risc natural» sunt specificate următoarele tipuri de obicte spațiale:
— Element expus abstract
— Zonă de hazard abstractă
— Eveniment abstract observat
— Zonă de risc abstractă
— Acoperirea elementului expus
— Element expus
— Zonă de hazard
— Acoperire de hazard
— Acoperirea evenimentului observat
— Eveniment observat
— Acoperire de risc
— Zonă de risc
12.2.1. Element expus abstract (AbstractExposedElement)
Persoane, bunuri, sisteme sau alte elemente prezente în zonele de hazard care, prin urmare, pot fi afectate de eventuale pierderi.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractExposedElement»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | identifier |
beginLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
validFrom | Momentul în care elementul expus a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care elementul expus nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «AbstractExposedElement»
Rol de asociere | Definiție | Tip | Voidability
sourceOfSpatialRepresentation | Obiectul sursă utilizat pentru a reprezenta elementul expus. | AbstractFeature | voidable
Constrângeri ale tipului de obiect spațial «AbstractExposedElement»
Dacă rolul de asociere «sourceOfSpatialRepresentation» este gol, trebuie să se furnizeze geometria obiectului spațial «AbstractExposedElement».
12.2.2. Zonă de hazard abstractă (AbstractHazardArea)
O zonă afectată de un hazard natural.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractHazardArea»
Atribut | Definiție | Tip | Voidability
beginLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
determinationMethod | Precizează dacă rezultatul zonei de hazard este delimitat după modelare sau determinat după interpretare. | DeterminationMethodValue |
endLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | identifier |
typeOfHazard | O clasificare generică și o clasificare specifică a tipului de hazard natural. | NaturalHazardClassification |
validityPeriod | Durata de timp în care se aplică modelul. | TM_Period | voidable
Roluri de asociere ale tipului de obiect spațial «AbstractHazardArea»
Rol de asociere | Definiție | Tip | Voidability
source | Evenimentul observat care a declanșat modelarea zonei de hazard. | AbstractObservedEvent | voidable
12.2.3. Eveniment abstract observat (AbstractObservedEvent)
Un fenomen natural relevant pentru studiul hazardelor naturale, care s-a produs sau care se produce în prezent și care a fost observat.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractObservedEvent»
Atribut | Definiție | Tip | Voidability
beginLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
nameOfEvent | Denumirea comună a evenimentului observat. | CharacterString | voidable
typeOfHazard | O clasificare generică și o clasificare specifică a tipului de hazard. | NaturalHazardClassification |
validFrom | Momentul în care evenimentul observat a început să existe în realitate. | DateTime | voidable
validTo | Momentul începând cu care evenimentul observat nu mai există în realitate. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «AbstractObservedEvent»
Rol de asociere | Definiție | Tip | Voidability
isMonitoredBy | Programul de mediu care monitorizează evenimentul observat | EnvironmentalMonitoringActivity | voidable
12.2.4. Zonă de risc abstractă (AbstractRiskZone)
O zonă de risc înseamnă extinderea spațială a unei combinații de consecințe ale unui eveniment (hazard) și posibilitatea/probabilitatea producerii acestuia.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «AbstractRiskZone»
Atribut | Definiție | Tip | Voidability
beginLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifeSpanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | identifier |
sourceOfRisk | O clasificare generică și o clasificare specifică a tipului de hazard care este o sursă de risc. | NaturalHazardClassification |
validityPeriod | Durata de timp finită în care se aplică modelul. | TM_Period | voidable
Roluri de asociere ale tipului de obiect spațial «AbstractRiskZone»
Rol de asociere | Definiție | Tip | Voidability
exposedElement | Elementul care se află într-o zonă periculoasă | AbstractExposedElement | voidable
source | Hazardul care este luat în considerare pentru crearea obiectului zonei de risc. | AbstractHazardArea | voidable
12.2.5. Acoperirea elementului expus (ExposedElementCoverage)
O acoperire care reprezintă un set de informații continue despre elementele expuse.
Acest tip este un subtip al «AbstractExposedElement».
Acest tip este un subtip al «CoverageByDomainAndRange».
Atribute ale tipului de obiect spațial «ExposedElementCoverage»
Atribut | Definiție | Tip | Voidability
typeOfElement | O clasificare a elementului expus. | ExposedElementClassification | voidable
Constrângeri ale tipului de obiect spațial «ExposedElementCoverage»
Intervalul este compus din nivelul sau intensitatea evaluării vulnerabilității.
Domeniul este un caroiaj rectificat sau un caroiaj referențiabil.
12.2.6. Element expus (ExposedElement)
Obiecte spațiale discrete reprezentând un element expus.
Acest tip este un subtip al «AbstractExposedElement».
Atribute ale tipului de obiect spațial «ExposedElement»
Atribut | Definiție | Tip | Voidability
geometry | Reprezentare geometrică a elementului expus. | GM_Object |
assessmentOfVulnerability | Evaluarea vulnerabilității elementului expus. | VulnerabilityAssessment | voidable
12.2.7. Zonă de hazard (HazardArea)
Obiecte spațiale discrete reprezentând un hazard natural.
Acest tip este un subtip al «AbstractHazardArea».
Atribute ale tipului de obiect spațial «HazardArea»
Atribut | Definiție | Tip | Voidability
geometry | Reprezentare geometrică a extinderii spațiale acoperite de zona de hazard. | GM_Surface |
likelihoodOfOccurrence | Un concept general care se referă la posibilitatea producerii unui eveniment. | LikelihoodOfOccurrence | voidable
magnitudeOrIntensity | O expresie a magnitudinii sau intensității unui fenomen. | LevelOrIntensity | voidable
12.2.8. Acoperire de hazard (HazardCoverage)
O acoperire reprezentând un set de informații continue despre un tip de hazard natural.
Acest tip este un subtip al «AbstractHazardArea».
Acest tip este un subtip al «CoverageByDomainAndRange».
Constrângeri ale tipului de obiect spațial «HazardCoverage»
Intervalul este descris în funcție de magnitudine sau intensitate sau de probabilitatea producerii.
Domeniul este un caroiaj rectificat sau un caroiaj referențiabil.
12.2.9. Acoperirea evenimentului observat (ObservedEventCoverage)
O acoperire reprezentând un set de informații continue despre evenimentele observate.
Acest tip este un subtip al «AbstractObservedEvent».
Acest tip este un subtip al «CoverageByDomainAndRange».
Constrângeri ale tipului de obiect spațial «ObservedEventCoverage»
Intervalul este descris în funcție de magnitudine sau intensitate sau de probabilitatea producerii.
Domeniul este un caroiaj rectificat sau un caroiaj referențiabil.
12.2.10. Eveniment observat (ObservedEvent)
Obiecte spațiale discrete reprezentând un fenomen natural relevant pentru studiul hazardelor naturale, care s-a produs sau care se produce în prezent și care a fost observat.
Acest tip este un subtip al «AbstractObservedEvent».
Atribute ale tipului de obiect spațial «ObservedEvent»
Atribut | Definiție | Tip | Voidability
geometry | Reprezentare geometrică a extinderii spațiale acoperite de evenimentul observat. | GM_Object |
magnitudeOrIntensity | O expresie a magnitudinii sau intensității unui fenomen. | LevelOrIntensity | voidable
12.2.11. Acoperire de risc (RiskCoverage)
O acoperire reprezentând un set de informații continue despre intensitate sau nivelul de risc.
Acest tip este un subtip al «AbstractRiskZone».
Acest tip este un subtip al «CoverageByDomainAndRange».
Constrângeri ale tipului de obiect spațial «RiskCoverage»
Intervalul este descris în funcție de nivel sau intensitate.
Domeniul este un caroiaj rectificat sau un caroiaj referențiabil.
12.2.12. Zonă de risc (RiskCoverage)
Obiecte spațiale discrete reprezentând extinderea spațială a unei combinații de consecințe ale unui eveniment (hazard) și posibilitatea/probabilitatea producerii acestuia.
Acest tip este un subtip al «AbstractRiskZone».
Atribute ale tipului de obiect spațial «RiskZone»
Atribut | Definiție | Tip | Voidability
geometry | Reprezentare geometrică a extinderii spațiale acoperite de această zonă de risc. | GM_Surface |
levelOfRisk | Nivelul de risc este o evaluare a combinației dintre consecințele unui eveniment (hazard) și posibilitatea/probabilitatea producerii evenimentului. | LevelOrIntensity | voidable
12.3. Tipuri de date
12.3.1. Clasificare a elementului expus (ExposedElementClassification)
Această categorie se referă la informații cu privire la natura elementului expus care este relevant pentru analiza riscurilor.
Atribute ale tipului de date «ExposedElementClassification»
Atribut | Definiție | Tip | Voidability
exposedElementCategory | O clasificare generică a tipurilor de elemente care sunt expuse riscului. | ExposedElementCategoryValue |
specificExposedElementType | O denumire suplimentară a elementului expus în conformitate cu un nomenclator specific setului de date. | SpecificExposedElementTypeValue | voidable
12.3.2. Nivel sau intensitate (LevelOrIntensity)
Evaluarea cantitativă sau calitativă a riscului, a hazardului sau a vulnerabilității.
Atribute ale tipului de date «LevelOrIntensity»
Atribut | Definiție | Tip | Voidability
qualitativeValue | O evaluare calitativă a nivelului sau a intensității. | CharacterString | voidable
quantitativeValue | O evaluare cantitativă a nivelului sau a intensității. | Measure | voidable
assessmentMethod | O citare a metodei utilizate pentru a exprima nivelul sau intensitatea. | DocumentCitation | voidable
Constrângeri ale tipului de date «LevelOrIntensity»
Trebuie să se furnizeze fie valoare calitativă, fie valoarea cantitativă.
12.3.3. Probabilitatea producerii (LikelihoodOfOccurrence)
Probabilitatea reprezintă un concept general care se referă la posibilitatea producerii unui eveniment.
Atribute ale tipului de date «LikelihoodOfOccurrence»
Atribut | Definiție | Tip | Voidability
qualitativeLikelihood | O evaluare calitativă a probabilității de producere a unui hazard. | CharacterString | voidable
quantitativeLikelihood | Frecvența cu care se produce sau perioada de revenire a unui fenomen care reprezintă un hazard. | QuantitativeLikelihood | voidable
assessmentMethod | O citare a metodei utilizate pentru a exprima probabilitatea. | DocumentCitation | voidable
Constrângeri ale tipului de date «LikelihoodOfOccurrence»
Trebuie să se furnizeze fie probabilitatea calitativă, fie probabilitatea cantitativă.
12.3.4. Clasificarea hazardelor naturale (NaturalHazardClassification)
Această categorie se referă la informații cu privire la natura hazardului natural, precum și la tipul de hazard care reprezintă sursa de risc.
Atribute ale tipului de date «NaturalHazardClassification»
Atribut | Definiție | Tip | Voidability
hazardCategory | O clasificare generică a tipurilor de hazarde naturale. | HazardCategoryValue |
specificHazardType | Clasificare suplimentară a hazardelor naturale care precizează în plus tipul de hazard în conformitate cu un nomenclator specific acestui set de date. | SpecificHazardTypeValue | voidable
12.3.5. Probabilitate cantitativă (QuantitativeLikelihood)
Frecvența cu care se produce sau perioada de revenire a unui fenomen care reprezintă un hazard.
Atribute ale tipului de date «QuantitativeLikelihood»
Atribut | Definiție | Tip | Voidability
probabilityOfOccurrence | Probabilitatea producerii unui eveniment care reprezintă un hazard, exprimată ca o valoare cuprinsă între 0 și 1. | Probability | voidable
returnPeriod | Interval mediu de timp pe termen lung sau numărul de ani în care un eveniment va fi egalat sau depășit. | Number | voidable
12.3.6. Evaluarea vulnerabilității (VulnerabilityAssessment)
Evaluarea vulnerabilității.
Atribute ale tipului de date «VulnerabilityAssessment»
Atribut | Definiție | Tip | Voidability
sourceOfVulnerability | Tipul de hazard a cărui vulnerabilitate este evaluată. | NaturalHazardClassification |
levelOfVulnerability | Nivel de vulnerabilitate. | LevelOrIntensity | voidable
magnitudeOrIntensityOfHazard | O expresie a magnitudinii sau intensității unui fenomen. | LevelOrIntensity | voidable
typeOfElement | O clasificare a elementului expus. | ExposedElementClassification | voidable
12.4. Enumerări
12.4.1. Metoda de determinare (DeterminationMethodValue)
O enumerare care să descrie metoda utilizată pentru a defini zona de hazard sau de risc.
Valori pentru enumerarea «DeterminationMethodValue»
Valoare | Definiție
modelling | Suprafața a fost calculată conform unui model.
indirectDetermination | Suprafața a fost determinată prin interpretarea de date și/sau informații disponibile.
12.5. Liste de coduri
12.5.1. Categoria elementului expus (ExposedElementCategoryValue)
O clasificare a elementului expus.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «ExposedElementCategoryValue»
Valoare | Nume | Definiție | Parent value
social | social | Orice aspect referitor la persoane sau grupuri de persoane. |
people | persoane | Prezența ființelor umane. | social
community | comunitate | O relație complexă între ființe umane care acționează ca un întreg sau ca o unitate. | social
political | politic | Orice obiect relevant pentru domeniul politicii. | social
socialService | serviciu social | Orice serviciu furnizat persoanelor. | social
economic | economic | Orice obiect legat de proprietate, economie sau aspecte monetare. |
property | proprietate | Orice obiect care este supus dreptului de proprietate, cum ar fi o casă. | economic
infrastructure | infrastructură | Orice obiect considerat ca fiind o structură ce furnizează un serviciu, cum ar fi un drum, un pod, o unitate militară etc. | economic
economicActivity | activitate economică | Orice obiect care reprezintă o activitate economică, cum ar fi o industrie. | economic
ruralLandUse | utilizarea terenului rural | Orice obiect neurban destinat oricărei utilizări date. | economic
environmental | mediu | O zonă supusă unui anumit nivel de protecție, cum ar fi un parc natural. |
waterBody | corp de apă | Orice acumulare semnificativă de apă. | environmental
protectedArea | zonă protejată | O zonă care este protejată | environmental
pollutionSource | sursă de poluare | Un obiect care conține poluanți. | environmental
heritage | patrimoniu | Orice aspect legat de obiecte relevante dintr-o perspectivă culturală sau de patrimoniu. |
culturalAsset | bun cultural | Orice obiect considerat relevant din punct de vedere cultural, cum ar fi un stadion, un teatru, un muzeu etc. | heritage
historicalAsset | bun istoric | Orice obiect cu o importanță istorică. | heritage
worldHeritageSite | sit al patrimoniului mondial | Un loc (cum ar fi o pădure, un munte, un lac, un deșert, un monument, o clădire, un complex sau un oraș), care este înscris pe lista UNESCO ca având o importanță culturală sau fizică deosebită. | heritage
12.5.2. Categoria de hazard natural (NaturalHazardCategoryValue)
O clasificare generică a tipurilor de hazarde naturale.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «NaturalHazardCategoryValue»
Valoare | Nume | Definiție | Parent value
geologicalHydrological | geologic/hidrologic | Procese care au o natură (sau o origine) geologică (geosferă) sau hidrologică (hidrosferă). |
tsunami | tsunami | Dislocare a unui val lung într-un volum mare de apă și care atinge uscatul de emersiune. | geologicalHydrological
volcanic | vulcanic | O deschidere sau o ruptură a scoarței terestre care permite eliberarea de magmă fierbinte, cenușă și gaze. | geologicalHydrological
earthquake | cutremur | Pericolele de cutremur implică propagarea de unde elastice la sau aproape de suprafață, după eliberarea stresului tectonic sau a altor surse naturale, cum ar fi exploziile vulcanice sau impacturile meteorice. | geologicalHydrological
subsidenceAndCollapse | subsidență și prăbușire | Fenomenele de subsidență și prăbușire implică, în principal, o deplasare verticală în jos a suprafaței terestre, datorată diverselor procese de dezagregare sau compactare a rocilor, până când structura rocii nu își mai poate suporta propria sarcină (colaps) sau poate provoca deplasări lente în jos (subsidențe). | geologicalHydrological
landslide | alunecare de teren | Procese de coborâre pe o pantă a solului, rocilor și materialelor organice, asociate cu diferite tipuri de defecte ale solului. | geologicalHydrological
snowAvalanche | avalanșă | O masă de zăpadă având, de regulă, un volum mai mare de 100 m3 și o lungime minimă de 50 metri care coboară cu repeziciune pe o pantă. | geologicalHydrological
flood | inundație | Procesele de inundare, de obicei, a unui teren uscat (emersat) sau acoperirea temporară cu apă a unui teren care nu este de obicei acoperit cu apă. | geologicalHydrological
toxicOrRadioactive | toxic sau radioactiv | Procese legate de natura substanțelor care ar putea constitui o amenințare pentru sănătatea umană. | geologicalHydrological
meteorologicalClimatological | meteorologic/climatologic | Procese care au un caracter (sau o origine) meteorologic(ă) [(atmosferic(ă)] sau climatic(ă) (schimbări pe termen lung ale variabilelor de mediu). |
drought | secetă | Existența unei disponibilități sub medie, susținute și extensive, a apei, cauzată de variații climatice. | meteorologicalClimatological
extremeTemperature | temperaturi extreme | O creștere sau o scădere anormală de temperatură, care durează mai mult decât o scădere sau o creștere obișnuită de temperatură. | meteorologicalClimatological
tornadosAndHurricanesStrongWinds | tornade, uragane și vânturi puternice | Vânturi violente (de mare viteză). | meteorologicalClimatological
descărcare electrică | descărcare electrică | Descărcarea de energie electrică în atmosferă. | meteorologicalClimatological
stormSurge | undă de furtună | Apă împinsă dinspre mare pe uscat, cauzată de o perturbare atmosferică, precum un uragan sau o schimbare rapidă a presiunii atmosferice. | meteorologicalClimatological
fires | incendii | Această categorie include toate tipurile de procese care implică izbucnirea și răspândirea incendiilor. |
forestFireWildfire | incendii forestiere sau incendii necontrolate | Izbucnirea incendiilor și răspândirea lor pe terenurile cu vegetație. | fires
undergroundFires | incendii subterane | Răspândirea incendiilor în subsol, de regulă, în cazul solurilor bogate în turbă. | fires
biological | biologic | Procese direct legate de organisme vii sau de produse ale organismelor vii. |
infestation | infestare | Creșterea anormală a populației de organisme vii. | biological
epidemic | epidemie | Apariție a unei boli care se răspândește rapid printre indivizii dintr-o zonă sau printre indivizii unei populații. |
allergens | alergeni | Produse sau substanțe biologice (precum polenul), care ar putea provoca alergii în cazul unui număr mare de persoane. | biological
cosmic | cosmic | Procese din spațiul cosmic. |
meteoriteImpact | impact meteoric | Materiale solide din spațiul cosmic care ajung pe Pământ. | cosmic
magneticDisruption | perturbare magnetică | Perturbarea câmpului magnetic al Pământului. | cosmic
solarAndCosmicRadiation | radiații cosmice și solare | Radiații provenite din spațiul cosmic (UV, gamma etc.). | cosmic
12.5.3. Tipul specific de element expus (SpecificExposedElementTypeValue)
O denumire suplimentară a elementelor expuse.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
12.5.4. Tip specific de hazard (SpecificHazardTypeValue)
O clasificare suplimentară a hazardelor naturale.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
12.6. Cerințe specifice categoriei
| (1) | În cazul în care o «RiskZone» este asociată cu o «HazardArea», «RiskZone» și «HazardArea» trebuie să se suprapună.
| (2) | În cazul în care o «RiskZone» este asociată cu un «ExposedElement», «ExposedElement» și «RiskZone» trebuie să se suprapună.
12.7. Straturi
Straturi pentru categoria de date spațiale «Zone de risc natural»
Numele stratului | Titlul stratului | Tip de obiect spațial
NZ.RiskZone | Zone de risc | RiskZone
NZ.RiskZoneCoverage | Acoperirea zonelor de risc | RiskZoneCoverage
NZ. <ValoaredinListadeCoduri>(12) | <nume lizibil de către om> | HazardArea, HazardAreaCoverage (typeOfHazard: NaturalHazardCategoryValue)
Exemplu: NZ.Landslide | Exemplu: Alunecări de teren |
NZ. <ValoaredinListadeCoduri>(13) | <nume lizibil de către om> | ObservedEvent, ObservedEventCoverage (typeOfHazard: NaturalHazardCategoryValue)
Exemplu: NZ.Flood | Exemplu: Inundații |
NZ.ExposedElement | Elemente expuse | ExposedElement
NZ.ExposedElementCoverage | Acoperirea elementului expus | ExposedElementCoverage
13. CONDIȚII ATMOSFERICE ȘI CARACTERISTICI GEOGRAFICE METEOROLOGICE (ATMOSPHERIC CONDITIONS AND METEOROLOGICAL GEOGRAPHICAL FEATURES)
13.1. Structura categoriilor de date spațiale «Condiții atmosferice și caracteristici geografice meteorologice»
Tipurile specificate pentru categoria de date spațiale «Condiții atmosferice și caracteristici geografice meteorologice» sunt structurate în următoarele pachete:
— Condiții atmosferice și caracteristici geografice meteorologice
— Observații specializate (Specialised Observations) (specificate în secțiunea 7.4 din anexa I)
— Procese (Processes) (specificate în secțiunea 7.2 din anexa I)
— Proprietăți observabile (Observable Properties) (specificate în secțiunea 7.3 din anexa I)
13.2. Condiții atmosferice și caracteristici geografice meteorologice
13.2.1. Liste de coduri
13.2.1.1. Componentă de referință a UE privind calitatea aerului (EU_AirQualityReferenceComponentValue)
Definiții ale fenomenelor în ceea ce privește calitatea aerului, în contextul raportării în temeiul legislației Uniunii.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind condițiile atmosferice și caracteristicile geografice meteorologice.
13.2.1.2. Tabelul 4.2 GRIB Code și Flags al OMM (GRIB_CodeTable4_2Value)
Definiții ale fenomenelor observate în domeniul meteorologiei.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind condițiile atmosferice și caracteristicile geografice meteorologice.
13.3. Cerințe specifice categoriei
| (1) | Prin derogare de la cerințele secțiunii 2.2 din anexa II, datele în format caroiaj referitoare la categoriile «Condiții atmosferice» și «Caracteristici geografice meteorologice» pot fi puse la dispoziție utilizându-se un caroiaj corespunzător.
| (2) | Datele referitoare la categoriile «Condiții atmosferice» sau «Caracteristici geografice meteorologice» trebuie puse la dispoziție utilizându-se tipurile definite în pachetul «Observații specializate» din anexa I, tipul de obiect spațial «OM_Observation» sau subtipurile aferente.
| (3) | Proprietatea observată a unei «OM_Observation» trebuie identificată printr-un identificator din cadrul vocabularelor Componentei de referință a UE privind calitatea aerului, ale Tabelului 4.2 GRIB Code și Flags al OMM, ale Numelor standard în materie de climă și previziuni meteorologice sau din alte vocabulare corespunzătoare.
13.4. Straturi
Pentru categoriile «Condiții atmosferice» și «Caracteristici geografice meteorologice», nu sunt specificate straturi.
14. CARACTERISTICI GEOGRAFICE OCEANOGRAFICE (OCEANOGRAPHIC GEOGRAPHICAL FEATURES)
14.1. Structura categoriei de date spațiale «Caracteristici geografice oceanografice»
Tipurile specificate pentru categoria de date spațiale «Caracteristici geografice oceanografice» sunt structurate în următoarele pachete:
— Caracteristici geografice oceanografice
— Observații specializate (Specialised Observations) (specificate în secțiunea 7.4 din anexa I)
— Procese (Processes) (specificate în secțiunea 7.2 din anexa I)
— Proprietăți observabile (Observable Properties) (specificate în secțiunea 7.3 din anexa I)
— Trimiteri la observații (Observation References) (specificate în secțiunea 7.4 din anexa I)
14.2. Caracteristici geografice oceanografice
14.2.1. Liste de coduri
14.2.1.1. Utilizarea parametrului BODC P01 (BODC_P01ParameterUsageValue)
Definiții ale fenomenelor observate în domeniul oceanografiei.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile privind elevația specificate în Ghidul tehnic INSPIRE privind Caracteristicile geografice oceanografice.
14.3. Cerințe specifice categoriei
| (1) | Prin derogare de la cerințele secțiunii 2.2 din anexa II, datele în format caroiaj referitoare la categoria «Caracteristici geografice oceanografice» trebuie puse la dispoziție utilizându-se un caroiaj corespunzător.
| (2) | Datele referitoare la categoria «Caracteristici geografice oceanografice» trebuie puse la dispoziție utilizându-se următoarele tipuri definite în pachetul «Observații specializate» din anexa I: «PointObservation», «PointTimeSeriesObservation», «MultiPointObservation», «GridObservation», «GridSeriesObservation», «PointObservationCollection».
| (3) | Proprietatea observată a unei «OM_Observation» trebuie identificată printr-un identificator din cadrul vocabularelor «Utilizarea parametrului BODC P01» sau «Nume standard în domeniul climei și al prognozei».
14.4. Straturi
Straturi pentru categoria de date spațiale «Caracteristici geografice oceanografice»
Numele stratului | Titlul stratului | Tip de obiect spațial
OF.PointObservation | Observare oceanografică punctuală | PointObservation
OF.PointTimeSeriesObservation | Observație oceanografică de serie temporală într-un punct | PointTimeSeriesObservation
OF.MultiPointObservation | Observare oceanografică punctuală multiplă | MultiPointObservation
OF.GridObservation | Observare oceanografică în caroiaj | GridObservation
OF.GridSeriesObservation | Observație oceanografică în serii de caroiaje | GridSeriesObservation
15. REGIUNILE MARINE (SEA REGIONS)
15.1. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt specificate pentru categoria de date spațiale «Regiuni marine»:
— Zonă marină
— Mare
— Zonă de circulație marină
— Zonă inter-maree
— Linie de țărm
— Segment de țărm
— Linie de coastă
— Contur marin
— Strat marin
— Zonă a fundului mării
— Zonă a suprafeței mării
15.1.1. Zonă marină (SeaArea)
O zonă a mării definită în funcție de caracteristicile sale fizice și chimice. Aceasta poate avea multiple geometrii (extindere) pentru a reprezenta diferite faze ale mareei.
Acest tip este un sub-tip al «HydroObject».
Atribute ale tipului de obiect spațial «SeaArea»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
seaAreaType | Tip de zonă marină în conformitate cu clasificările din lista de coduri «SeaAreaTypeClassificationValue», de exemplu estuar. | SeaAreaTypeClassificationValue |
extent | Extinderea zonei marine într-o anumită fază a mareei. | MarineExtent |
parameterValue | O valoare a unui parametru alocat zonei marine. De exemplu Temperatura medie anuală a suprafeței mării = 12 grade Celsius. | ParameterValuePair |
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «SeaArea»
Rol de asociere | Definiție | Tip | Voidability
subArea | Zonele marine pot consta din subzone, de exemplu, o zonă marină care definește toate mările europene ar putea fi rezultatul agregării mai multor zone marine (Marea Nordului, Marea Mediterană etc.). | SeaArea |
15.1.2. Mare (Sea)
Întinderea mării în cazul mareei înalte (meanHighWater).
Acest tip este un subtip al «SeaArea».
Atribute ale tipului de obiect spațial «Sea»
Atribut | Definiție | Tip | Voidability
extent | Extinderea mării în cazul mareei înalte medii. | MarineExtent |
Constrângeri ale tipului de obiect spațial «Sea»
Marea este definită la Mean High Water. Această constrângere poate fi atenuată dacă nu există o variație semnificativă a nivelului apei în caz de maree.
15.1.3. Zonă de circulație marină (MarineCirculationZone)
O zonă marină este definită de modelele sale fizice și chimice de circulație. Această zonă este utilizată, de regulă, pentru gestionarea și raportarea mediului marin sau clasificarea mediului marin.
Acest tip este un subtip al «SeaArea».
Atribute ale tipului de obiect spațial «MarineCirculationZone»
Atribut | Definiție | Tip | Voidability
zoneType | Tipul de zonă de circulație marină, de exemplu «sedimentCell». | ZoneTypeValue |
extent | Extinderea zonei de circulație marină într-o anumită fază a mareei. | MarineExtent |
15.1.4. Zonă inter-maree (InterTidalArea)
Parte a mediului marin care este expusă (cu alte cuvinte nu este acoperită de apă) pe durata unui ciclu normal al mareei; este definită ca diferența dintre un nivel al mareei înalte și un nivel al mareei joase.
Acest tip este un subtip al «Shore».
Atribute ale tipului de obiect spațial «InterTidalArea»
Atribut | Definiție | Tip | Voidability
lowWaterLevel | Nivelul mareei joase utilizat pentru a defini limita inferioară a zonei inter-maree, de exemplu «meanLowWater». | WaterLevelValue |
highWaterLevel | Nivelul mareei înalte utilizat pentru a defini limita superioară a zonei inter-maree, de exemplu «meanHighWater». | WaterLevelValue |
15.1.5. Linie de țărm (Shoreline)
Orice graniță între o zonă marină și uscat.
Acest tip este un sub-tip al «HydroObject».
Atribute ale tipului de obiect spațial «Shoreline»
Atribut | Definiție | Tip | Voidability
segment | O secțiune a liniei de țărm. | ShoreSegment |
waterLevel | Nivelul apei utilizat pentru definirea acestei linii de țărm (de exemplu «meanHighWater»). | WaterLevelValue | voidable
15.1.6. Segment de țărm (ShoreSegment)
Un segment de țărm este o secțiune a liniei de țărm.
Atribute ale tipului de obiect spațial «ShoreSegment»
Atribut | Definiție | Tip | Voidability
geometry | Geometria «ShoreSegment». | GM_Curve |
shoreClassification | Tipul principal de segment de țărm, preluat din lista de coduri «ShoreTypeClassificationValue». | ShoreTypeClassificationValue | voidable
shoreStability | Tipul principal de stabilitate al segmentului de țărm, preluat din lista de coduri «ShoreTypeClassificationValue». | ShoreStabilityValue | voidable
15.1.7. Linie de coastă (Coastline)
Un caz special de linie a țărmului definită ca linie a țărmului în caz de maree înaltă medie (Mean High Water - MHW). În cazul în care nu există variații importante ale nivelului apei, nivelul mediu al mării (Mean Sea Level - MSL) poate fi utilizat ca substitut pentru MHW.
Acest tip este un subtip al «Shoreline».
Constrângeri ale tipului de obiect spațial «Coastline»
Linia de coastă este un caz special de linie de țărm în caz de nivel mediu al mareei înalte (Mean High Water Level - MHW). Linia de coastă reprezintă granița dintre uscat și pe mare, care poate fi utilizată pentru aplicații de vizualizare, descoperire și aplicații vizând obiective generale în cazul în care este necesară o demarcație uscat/mare. În cazul în care nu există variații importante ale nivelului apei, nivelul mediu al mării (MSL) poate fi utilizat ca substitut pentru MHW.
15.1.8. Contur marin (MarineContour)
Un set de izolinii reprezentând valoarea anumitor fenomene la un moment dat.
Atribute ale tipului de obiect spațial «MarineContour»
Atribut | Definiție | Tip | Voidability
isoline | Izolinie utilizată pentru a genera conturul. | MarineIsoline |
phenomenon | Proprietatea reprezentată de izolinii (de exemplu înălțimea valurilor). | AbstractObservableProperty |
validTime | Momentul în care acest contur este reprezentativ. | TM_Instant |
Roluri de asociere ale tipului de obiect spațial «MarineContour»
Rol de asociere | Definiție | Tip | Voidability
sourceObservations | Utilizat pentru stabili legătura la un set de observații de bază care au fost utilizate pentru a defini un contur marin. | ObservationSet |
15.1.9. Strat marin (MarineLayer)
Un strat marin descrie orice strat care poate acoperi orice parte a suprafeței marine sau a fundului mării.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «MarineLayer»
Atribut | Definiție | Tip | Voidability
geometry | Geometria stratului marin. | GM_Object |
validTime | Perioada de timp în care stratul marin este valabil. | TM_Period |
Roluri de asociere ale tipului de obiect spațial «MarineLayer»
Rol de asociere | Definiție | Tip | Voidability
subLayer | Un strat marin poate avea un substrat, de exemplu o pată de petrol poate fi alcătuită dintr-o parte principală și o serie de pete mai mici. | MarineLayer |
Constrângeri ale tipului de obiect spațial «MarineLayer»
Un strat marin pot fi reprezentat fie sub forma unei suprafețe, fie sub forma unui punct. Tipul de geometrie de tip punct reflectă realitatea conform căreia straturile marine sunt identificate cu ajutorul observațiilor punctuale.
15.1.10. Zonă a fundului mării (SeaBedArea)
O zonă a fundului mării caracterizată de un tip identificat de acoperire, de exemplu o porțiune de vegetație sau un tip de sediment.
Acest tip este un subtip al «MarineLayer».
Atribute ale tipului de obiect spațial «SeaBedArea»
Atribut | Definiție | Tip | Voidability
surfaceType | Tipul de suprafață al fundului mării. | SeaBedCoverValue |
15.1.11. Zonă a suprafeței mării (SeaSurfaceArea)
O zonă a suprafeței mării caracterizată de un anumit tip de acoperire, de exemplu o porțiune de gheață marină.
Acest tip este un subtip al «MarineLayer».
Atribute ale tipului de obiect spațial «SeaSurfaceArea»
Atribut | Definiție | Tip | Voidability
surfaceType | Tipul de suprafață al zonei marine. | SeaSurfaceClassificationValue |
15.2. Tipuri de date
15.2.1. Întindere marină (MarineExtent)
Întinderea zonei marine în cazul unei faze a mareei date.
Atribute ale tipului de date «MarineExtent»
Atribut | Definiție | Tip | Voidability
geometry | Geometria întinderii marine. | GM_MultiSurface |
waterLevel | Nivelul apei la care este valabilă întinderea. | WaterLevelValue |
15.2.2. Izolinie marină (MarineIsoline)
O izolinie reprezentând o anumită valoare a unui anumit fenomen marin fizic sau chimic, cum ar fi temperatura, salinitatea sau înălțimea valurilor.
Atribute ale tipului de date «MarineIsoline»
Atribut | Definiție | Tip | Voidability
geometry | Geometria izoliniilor. | GM_MultiCurve |
value | Valori atribuite izoliniilor. | Measure |
15.2.3. Cuplu parametru-valoare (ParameterValuePair)
O pereche de valori ale parametrilor conține o valoare a unei anumite proprietăți observate, de exemplu temperatura medie anuală a suprafeței mării.
Atribute ale tipului de date «ParameterValuePair»
Atribut | Definiție | Tip | Voidability
parameter | O definiție a parametrului observat (de exemplu temperatura medie). | AbstractObservableProperty |
value | Valoarea parametrului observat, de exemplu 12 grade Celsius. | Measure |
validTime | Perioada de timp în care valoarea atribuită este valabilă. Poate fi vorba de un moment în timp sau de o durată. | TM_Object | Voidable
15.3. Liste de coduri
15.3.1. Clasificarea tipului de zonă marină (SeaAreaTypeClassificationValue)
Tipul de clasificare a «SeaArea», de exemplu «estuary», «openOcean».
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind regiunile marine.
15.3.2. Acoperirea fundului mării (SeaBedCoverValue)
Tipuri de acoperire a fundului mării.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind regiunile marine.
15.3.3. Clasificarea suprafeței marine (SeaSurfaceClassificationValue)
Tipuri de straturi ale suprafeței marine existente la suprafața mărilor.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind regiunile marine.
15.3.4. Stabilitatea țărmului (ShoreStabilityValue)
Tipuri de stabilitate a segmenetelor de țărm.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind regiunile marine.
15.3.5. Clasificarea tipurilor de țărm (ShoreTypeClassificationValue)
Tipuri de segmente de țărm.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind regiunile marine.
15.3.6. Tipul zonei (ZoneTypeValue)
Tipuri de zone de circulație marină.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind regiunile marine.
15.4. Cerințe specifice categoriei
| (1) | Tipul de obiect spațial «Mare» trebuie utilizat pentru a descrie zone ale mărilor (sau oceanelor) identificate și denumite. Unitățile artificiale de raportare sunt excluse de la această cerință.
| (2) | «MarineExtent» al unui obiect spațial «Mare» trebuie să aibă o valoare a nivelului mării egală cu «MeanHighWater», cu condiția să nu existe o modificare apreciabilă a întinderii mării ca urmare a mareei, caz în care poate fi utilizată o valoare a «MeanSeaLevel».
| (3) | Nivelul mareei joase utilizat pentru a defini o «IntertidalArea» trebuie furnizată ca o valoare a atributului «lowWaterLevel». Nivelul ar trebui să fie unul al mareei joase.
| (4) | Listele de coduri definite în cadrul categoriei de date spațiale «Caracteristici geografice oceanografice» trebuie să fie utilizate pentru identificarea fenomenelor reprezentate de tipurile de obiecte spațiale «MarineContour».
| (5) | «SeaAreas» este reprezentată ca geometrii bidimensionale.
15.5. Straturi
Straturi pentru categoria de date spațiale «regiuni marine»
Numele stratului | Titlul stratului | Tip de obiect spațial
SR.SeaArea | Zonă marină | SeaArea
SR.Sea | Mare | Sea
SR.MarineCirculationZone | Zonă de circulație marină | MarineCirculationZone
SR.InterTidalArea | Zonă inter-maree | InterTidalArea
SR.MarineContour | Contur marin | MarineContour
SR.Shoreline | Linie de țărm | Shoreline
SR.Coastline | Linie de coastă | CoastLine
SR.SeaSurfaceArea | Zonă a suprafeței mării | SeaSurfaceArea
SR.SeaBedArea | Zonă a fundului mării | SeaBedArea
16. REGIUNI BIOGEOGRAFICE (BIO-GEOGRAPHICAL REGIONS)
16.1. Tipuri de obiecte spațiale
Pentru categoria de date spațiale «regiuni biogeografice» este specificat următorul tip de obiect spațial: «Bio-geographical region».
16.1.1. Regiune biogeografică (Bio-geographicalRegion)
O zonă în care există condiții ecologice relativ omogene, având caracteristici comune.
Atribute ale tipului de obiect spațial «Bio-geographicalRegion»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Geometria care definește regiunea ecologică. | GM_MultiSurface |
regionClassification | Codul de clasă al regiunii, în conformitate cu un sistem de clasificare. | RegionClassificationValue |
regionClassificationScheme | Sistemul de clasificare utilizat pentru clasificarea regiunilor. | RegionClassificationSchemeValue |
regionClassificationLevel | Nivelul de clasificare a clasei de regiuni. | RegionClassificationLevelValue | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
16.2. Liste de coduri
16.2.1. Nivel de clasificare a regiunii (RegionClassificationLevelValue)
Coduri care definesc nivelul de clasificare al clasei de regiuni.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «RegionClassificationLevelValue»
Valoare | Nume | Definiție
international | Internațional | Aceasta este o clasificare a regiunilor la nivel internațional.
local | Local | Aceasta este o clasificare a regiunilor la nivel local.
national | Național | Aceasta este o clasificare a regiunilor la nivel național.
regional | Regional | Aceasta este o clasificare a regiunilor la nivel regional.
16.2.2. Sistem de clasificare a regiunilor (RegionClassificationSchemeValue)
Coduri care definesc diferitele regiuni biogeografice.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind regiunile biogeografice.
16.2.3. Clasificarea regiunilor (RegionClassificationValue)
Coduri utilizate pentru a defini diferitele regiuni biogeografice.
Valorile permise pentru această listă de coduri cuprind valorile următoarelor liste de coduri sau alte liste de coduri indicate de furnizorii de date:
— Clasificare a stratificării de mediu (EnvironmentalStratificationClassificationValue): Coduri pentru stratificare climatică a mediului în Uniune, astfel cum se specifică în Metzger, M.J., Shkaruba, A.D., Jongman, R.H.G. & Bunce, R.G.H., Descriptions of the European Environmental Zones and Strata. Alterra, Wageningen, 2012.
— Clasificare în conformitate cu Directiva-cadru privind strategia pentru mediul marin (MarineStrategyFrameworkDirectiveClassificationValue): Coduri pentru clasificarea în conformitate cu Directiva-cadru privind strategiile marine, astfel cum este prezentată la articolul 4 din Directiva 2008/56/CE (14).
— Clasificarea regiunilor biogeografice conform Natura 2000 și Emerald (Natura2000AndEmeraldBio-geographicalRegionClassificationValue): Codes for the classification of bio-geographical regions, as specified in the Code List for Bio-geographical Regions, Europe 2011, publicată pe site-ul web al Agenției Europene de Mediu.
— Clasificarea vegetației naturale (NaturalVegetationClassificationValue): Coduri pentru clasificarea vegetației naturale, în conformitate cu principalele categorii desemnate în Bohn, U., Gollub, G., and Hettwer, C., Map of the natural vegetation of Europe: scale 1:2,500,000, Part 2: Legend, Bundesamt für Naturschutz (German Federal Agency for Nature conservation), Bonn, 2000.
16.3. Straturi
Strat pentru categoria de date spațiale «Bio-Geographical Regions»
Numele stratului | Titlul stratului | Tip de obiect spațial
BR.Bio-geographicalRegion | Regiuni biogeografice | Bio-geographicalRegion
17. HABITATE ȘI BIOTOPURI (HABITATS AND BIOTOPES)
17.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «biotop» (biotope) înseamnă o regiune caracterizată de condiții de mediu relativ uniforme, ocupată de o anumită comunitate vegetală și de comunitatea animală conexă.
(2) «habitat» (habitat) înseamnă locul în care o plantă sau un animal se dezvoltă sau trăiește în mod natural. Aceasta poate fi fie aria geografică în care aceasta (acesta) se întinde, fie un anumit loc în care se regăsește un specimen. Un habitat este caracterizat de o uniformitate relativă a mediului fizic și de o interacțiune relativ mare a tuturor speciilor biologice implicate.
(3) «tip de habitat» (sau tip de biotop)» [habitat type (or biotope type)] înseamnă un tip abstract clasificat pentru a descrie habitate și biotopuri care sunt comune în ceea ce privește anumite caracteristici la un anumit nivel de detaliu. Criteriile de clasificare utilizate în mod obișnuit pot face referire la structura vegetației (precum terenuri împădurite, pășuni, lande) sau la caracteristici abiotice, precum ape curgătoare, roci de calcar sau dune de nisip, dar și la fazele sau etapele pertinente ale ciclului de viață al unui anumite specii sau al unei ghilde ecologice, precum zone de hibernare, zone de cuibărit sau coridoare de migrație etc.
(4) «distribuție (a tipurilor de habitate)» [distribution (of habitat types)] înseamnă un set de obiecte spațiale în care apare tipul de habitat, care oferă informații în timp și spațiu referitoare la un tip anume de habitat, împărțite în unități analitice. Distribuția este de obicei descrisă sau modelată pe baza altor obiecte spațiale utilizate ca unități analitice, de exemplu pentru celulele de caroiaj (foarte frecvent), regiuni biogeografice, situri de conservare a habitatelor naturale sau unități administrative.
(5) «caracteristică a habitatului» (habitat feature) înseamnă un habitat din punctukl de vedere al localizării sale exacte, al dimensiunii (suprafața sau volumul) și al informațiile biologice (de exemplu tipurile de habitate în cauză, caracteristicile structurale, listele de specii, tipurile de vegetație).
(6) «specie» (species) înseamnă o categorie taxonomică situată imediat sub un gen și care include indivizi strâns înrudiți și similari din punct de vedere morfologic, care se înmulțesc între ei în mod real sau potențial. În contextul categoriei «Habitate și biotopuri», «specie» înseamnă toate speciile de animale, de plante sau de ciuperci relevante pentru a descrie un habitat.
(7) «vegetație» (vegetation) înseamnă plantele dintr-o zonă, considerată în general sau ca și comunitate, însă nu din punct de vedere taxonomic. Vegetația poate, de asemenea, să fie definită ca fiind totalul acoperișului vegetal dintr-o anumită zonă sau de pe suprafața terestră, în ansamblul său.
(8) «tip de vegetație» (vegetation type) înseamnă plante (sau masa totală a plantelor) dintr-o anumită zonă, considerate în general sau ca și comunități vegetale, dar nu din punct de vedere taxonomic.
17.2. Tipuri de obiecte spațiale
Pentru categoria de date spațiale «Habitate și biotopuri», este specificat următorul tip de obiect spațial: Habitat.
17.2.1. Habitat (Habitat)
Zone geografice caracterizate de condiții ecologice, procese, structură și funcții specifice, care sprijină fizic organismele care trăiesc în zonele respective.
Atribute ale tipului de obiect spațial «Habitat»
Atribut | Definiție | Tip | Voidability
geometry | Întinderea habitatului pe baza granițelor naturale. | GM_Object |
habitat | Identificatorul unei clase de habitate, definite și descrise în cadrul unui sistem internațional, național sau local de clasificare a habitatelor. | HabitatTypeCoverType |
habitatSpecies | Lista speciilor care trăiesc într-un habitat sau care constituie un anumit habitat la momentul cartografierii. | HabitatSpeciesType | voidable
habitatVegetation | Lista tipurilor de vegetație (în conformitate cu un sistem local de clasificare a vegetației) care constituie un anumit habitat. | HabitatVegetationType | voidable
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
17.3. Tipuri de date
17.3.1. Tipul de specii ale unui habitat (HabitatSpeciesType)
Specii care trăiesc într-un anumit habitat la momentul cartografierii.
Atribute ale tipului de date «HabitatSpeciesType»
Atribut | Definiție | Tip | Voidability
localSpeciesName | Denumirea științifică și numele autorului utilizate în nomenclatorul național, împreună cu conceptul său taxonomic național. | LocalNameType | voidable
referenceSpeciesScheme | Listă de referință care definește un standard taxonomic și nomenclatural în funcție de care trebuie cartografiate toate denumirile locale de specii și toate conceptele taxonomice. | ReferenceSpeciesSchemeValue |
referenceSpeciesId | Identificator al uneia dintre listele de referință furnizate de «referenceSpeciesScheme». | ReferenceSpeciesCodeValue |
17.3.2. Tipul de acoperire a habitatului (HabitatTypeCoverType)
Tip de habitat în conformitate cu un sistem internațional, național sau local de clasificare a habitatelor.
Atribute ale tipului de date «HabitatTypeCoverType»
Atribut | Definiție | Tip | Voidability
areaCovered | Zona acoperită de un anumit tip de habitat în cadrul geometriei date a obiectului spațial «habitat». | Area | voidable
lengthCovered | Lungimea acoperită de un anumit tip de habitat în cadrul geometriei date a obiectului spațial «habitat». | Length | voidable
volumeCovered | Volumul unui anumit tip de habitat în cadrul geometriei date a obiectului spațial «habitat». | Volume | voidable
referenceHabitatTypeId | Tip de identificator unic al habitatului, în conformitate cu un sistem de clasificare paneuropean. | ReferenceHabitatTypeCodeValue |
referenceHabitatTypeScheme | Unul dintre sistemele paneuropene de clasificare care sunt utilizate la scară largă în Europa. | ReferenceHabitatTypeSchemeValue |
localHabitatName | Tip de habitat în conformitate cu un sistem local de clasificare a habitatelor. | LocalNameType | voidable
referenceHabitatTypeName | Denumirea unui tip de habitat în conformitate cu un sistem paneuropean de clasificare. | CharacterString | voidable
17.3.3. Tipul de vegetație al habitatului (HabitatVegetationType)
Tipul de vegetație care trăiește într-un anumit habitat.
Atribute ale tipului de date «HabitatVegetationType»
Atribut | Definiție | Tip | Voidability
localVegetationName | Clasa de vegetație (tipul de vegetație), în conformitate cu un sistem local de clasificare. Denumirea în limbaj colocvial în conformitate cu un sistem local de clasificare a vegetației. | LocalNameType |
17.3.4. Tipul de denumire locală (LocalNameType)
Denumire în conformitate cu un sistem local de clasificare.
Atribute ale tipului de date «LocalNameType»
Atribut | Definiție | Tip | Voidability
localScheme | Identificator uniform de resurse al unui sistem local de clasificare. | CharacterString |
localNameCode | Denumire în limbaj colocvial în conformitate cu un sistem local de clasificare. | LocalNameCodeValue |
qualifierLocalName | Relația dintre denumirea locală și denumirea omoloagă din sistemul paneuropean. | QualifierLocalNameValue | voidable
localName | Denumire în conformitate cu un sistem local de clasificare. | CharacterString | voidable
17.4. Liste de coduri
17.4.1. Nume local al calificatorului (QualifierLocalNameValue)
Listă de valori care caracterizează relația dintre o denumire utilizată la nivel local și o denumire utilizată la nivel paneuropean.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «QualifierLocalNameValue»
Valoare | Nume | Definiție
congruent | congruent | Tipul local este, din punct de vedere conceptual, identic cu tipul paneuropean asociat.
excludes | exclude | Tipul paneuropean de habitat nu este, din punct de vedere conceptual, un subtip al tipului local asociat.
includedIn | inclus în | Tipul local este, din punct de vedere conceptual, un subtip al tipului paneuropean asociat.
includes | include | Tipul paneuropean de habitat este, din punct de vedere conceptual, un subtip al tipului local asociat.
overlaps | se suprapune | Există o anumită suprapunere între tipul local și cel paneuropean asociat, în conformitate cu definițiile lor respective, însă niciuna dintre celelalte relații specifice (congruent, exclude, inclus în, include) nu este valabilă.
17.4.2. Codul tipurilor de habitate de referință (ReferenceHabitatTypeCodeValue)
Valori utilizate în cadrul sistemelor paneuropene de clasificare a habitatelor.
Valorile permise pentru această listă de coduri cuprind valorile din următoarele liste de coduri:
— Codul tipului de habitat conform EUNIS (EunisHabitatTypeCodeValue): Clasificarea tipurilor de habitat în conformitate cu Baza de date EUNIS privind biodiversitatea, astfel cum sunt menționate în clasificarea EUNIS a tipurilor de habitate publicată pe site-ul web al Agenției Europene de Mediu.
— Cod în temeiul Directivei «Habitate» (HabitatsDirectiveCodeValue): Clasificarea tipurilor de habitate în conformitate cu anexa I la Directiva 92/43/CEE.
— Cod în conformitate cu Directiva-cadru privind strategia pentru mediul marin (MarineStrategyFrameworkDirectiveCodeValue): Clasificarea tipurilor de habitate în conformitate cu tabelul 1 din anexa III la Directiva 2008/56/CE.
17.4.3. Sistemul de referință al tipului de habitat (ReferenceHabitatTypeSchemeValue)
Această valoare definește tipul de sistem paneuropean de clasificare a habitatelor utilizat.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «ReferenceHabitatTypeSchemeValue»
Valoare | Nume | Definiție
eunis | Eunis | Clasificare EUNIS a habitatelor.
habitatsDirective | Directiva «Habitate» | Clasificarea habitatelor în conformitate cu anexa I la Directiva 92/43/CEE.
marineStrategyFrameworkDirective | Directiva-cadru privind strategia pentru mediul marin | Clasificarea habitatelor în conformitate cu tabelul 1 din anexa III la Directiva 2008/56/CE.
17.4.4. Codul denumirii locale (LocalNameCodeValue)
Identificator preluat din orice sistem local de clasificare.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
17.5. Cerințe specifice categoriei
| (1) | Este obligatoriu să se pună la dispoziție cel puțin un tip de habitat în conformitate cu un «referenceHabitatTypeScheme» (paneuropean) inclus în lista de coduri «ReferenceHabitatTypeSchemeValue». Această codificare este menită să permită întrebări privitoare la tipurile de habitate la nivel paneuropean armonizat.
17.6. Straturi
Strat pentru categoria de date spațiale «Habitate și biotopuri»
Numele stratului | Titlul stratului | Tip de obiect spațial
HB.Habitat | Habitat | Habitat
18. DISTRIBUȚIA SPECIILOR (SPECIES DISTRIBUTION)
18.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «agregare» (aggregation) înseamnă gruparea mai multor obiecte într-o clasă sau într-un grup.
(2) «comasare» (amalgamation) înseamnă combinația mai multor obiecte într-o structură unică.
18.2. Tipuri de obiecte spațiale
Următoarele tipuri de obiecte spațiale sunt specificate pentru categoria de date spațiale «Species Distribution»:
— Set de date referitoare la distribuția speciilor
— Unitate de distribuție a speciilor
18.2.1. Set de date referitoare la distribuția speciilor (SpeciesDistributionDataSet)
Acest set de date este o colecție de obiecte spațiale individuale (unități) dintr-o distribuție a speciilor.
Atribute ale tipului de obiect spațial «SpeciesDistributionDataSet»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
domainExtent | Extinderea geografică a domeniului colecției de caracteristici. | GM_MultiSurface | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
name | Numele unui anumit set de date furnizat pentru distribuția speciilor. | CharacterString | voidable
Roluri de asociere ale tipului de obiect spațial «SpeciesDistributionDataSet»
Rol de asociere | Definiție | Tip | Voidability
member | Obiect spațial individual dintr-o colecție de obiecte spațiale. | SpeciesDistributionUnit |
documentBasis | Trimitere la sau citare dintr-un document care descrie o campanie sau un act juridic care stă la baza setului de date. | DocumentCitation | voidable
18.2.2. Unitate de distribuție a speciilor (SpeciesDistributionUnit)
Ocurență a unor specii de animale și plante agregate în funcție de caroiaj, regiune, unitate administrativă sau altă unitate analitică.
Atribute ale tipului de obiect spațial «SpeciesDistributionUnit»
Atribut | Definiție | Tip | Voidability
geometry | Geometria fiecărei unități dintr-o colecție. | GM_Object |
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
distributionInfo | Descrierea obiectului distribuției (ocurențe sau populație), indicarea numărului de observații sau a dimensiunii populației dintr-o anumită specie, a grupului de specii sau a gradului taxonului și a distribuției sau izolării acestuia sau izolarea în cadrul unității de distribuție a speciilor. | DistributionInfoType | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
speciesName | Identificator și denumire științifică, inclusiv autorul, preluate dintr-o listă internațională de referință, suplimentată, în mod opțional, cu o denumire utilizată la nivel local și relația sa taxonomică conceptuală cu denumirea de referință. | SpeciesNameType |
Roluri de asociere ale tipului de obiect spațial «SpeciesDistributionUnit»
Rol de asociere | Definiție | Tip | Voidability
spatialObject | O trimitere la un alt obiect spațial care definește întinderea spațială a unei unități de distribuție. | AbstractFeature | voidable
Constrângeri ale tipului de obiect spațial «SpeciesDistributionUnit»
În cazul în care geometria nu prezintă nicio valoare, trebuie să se furnizeze o trimitere la un obiect spațial.
18.3. Tipuri de date
18.3.1. Tipul de informații referitoare la distribuție (DistributionInfoType)
Descrierea statutului obiectul distribuției în cadrul unității de distribuție a speciilor, inclusiv indicarea abundenței prin numărare, estimarea sau calcularea numărului de ocurențe sau a dimensiunii populației din anumite specii.
Atribute ale tipului de date «DistributionInfoType»
Atribut | Definiție | Tip | Voidability
occurrenceCategory | Densitatea populației speciei în cadrul unității de distribuție a speciilor. | OccurrenceCategoryValue |
residencyStatus | Informații privind statutul prezenței unei specii, din punctul de vedere al caracterului nativ al acesteia comparativ cu introducerea și stabilirea permanentă. | ResidencyStatusValue | voidable
populationSize | Interval de valori care indică ocurențele numărate, estimate sau calculate ale dimensiunilor populațiilor, prin utilizarea unei limite superioare și inferioare. | PopulationSizeType |
sensitiveInfo | Valoare booleană care indică dacă locul unde se află o anumitî specie are un caracter sensibil. | Boolean | voidable
populationType | Permanența populațiilor, în special în ceea ce privește speciile migratoare, în cadrul unei unități date de distribuție a speciilor. | PopulationTypeValue | voidable
collectedFrom | Data la care a început colectarea inițială a datelor privind ocurența speciilor. | Date | voidable
collectedTo | Data la care s-a încheiat colectarea inițială a datelor privind ocurența speciilor. | Date | voidable
18.3.2. Tipul de dimensiune a populației (PopulationSizeType)
O valoare din interval care indică ocurențele numărate, estimate sau calculate ale dimensiunilor populațiilor, definite prin utilizarea unei limite superioare și inferioare.
Atribute ale tipului de date «PopulationSizeType»
Atribut | Definiție | Tip | Voidability
countingMethod | Modalitatea de furnizare a unui număr pentru indicarea abundenței unei specii în cadrul unei anumite unități de distribuție a speciilor. | CountingMethodValue |
countingUnit | Ceea ce a fost numărat, estimat sau calculat atunci când s-a realizat compilarea informațiilor privind abundența unei specii în cadrul unității de distribuție a speciei. | CountingUnitValue |
populationSize | O valoare din interval care indică ocurențele sau dimensiunile populațiilor numărate, estimate sau calculate cu ajutorul unor limite superioare și inferioare. | RangeType |
18.3.3. Tip de interval (RangeType)
Valoare care indică limitele superioară și inferioară a activității de numărare, estimare sau calculare a ocurențelor.
Atribute ale tipului de date «RangeType»
Atribut | Definiție | Tip | Voidability
upperBound | Limita superioară a intervalului. În cazul în care valoarea acestui atribut este nulă și «lowerBound» (Limitainferioară) este populată, acest lucru presupune că valoarea se situează între «lowerBound» și infinit. | Integer |
lowerBound | Limita inferioară a intervalului. În cazul în care valoarea acestui atribut este nulă și «upperBound» (Limitasuperioară) este populată, acest lucru presupune că valoarea se situează între «upperBound» și zero. | Integer |
18.3.4. Tip de denumire a speciilor (SpeciesNameType)
Identificator și denumire științifică, inclusiv autorul, preluate dintr-o listă internațională de referință, suplimentată, în mod opțional, cu o denumire utilizată la nivel local și relația sa taxonomică conceptuală cu denumirea de referință.
Atribute ale tipului de date «SpeciesNameType»
Atribut | Definiție | Tip | Voidability
referenceSpeciesId | Identificator al uneia dintre listele de referință furnizate de «referenceSpeciesScheme». | ReferenceSpeciesCodeValue |
referenceSpeciesScheme | Listă de referință care definește un standard taxonomic și nomenclatural în funcție de care trebuie cartografiate toate denumirile de specii și toate conceptele taxonomice locale. | ReferenceSpeciesSchemeValue |
referenceSpeciesName | Denumirea științifică utilizată în «ReferenceSpeciesScheme» autorizată. | CharacterString | voidable
localSpeciesId | Identificator utilizat în nomenclatorul național. | LocalSpeciesNameCodeValue | voidable
localSpeciesScheme | Denumirea sistemului local de clasificare a speciilor (trimitere bibliografică). | CharacterString | voidable
localSpeciesName | Denumirea științifică utilizată în nomenclatorul național împreună cu conceptul său taxonomic național. | CharacterString | voidable
qualifier | Precizează relația taxonomică conceptuală dintre identificatorul local și identificatorul de referință al speciei. | QualifierValue | voidable
18.4. Liste de coduri
18.4.1. Metodă de numărare (CountingMethodValue)
Metoda de calculare a cifrelor care indică abundența unei specii în cadrul unei unități de agregare.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «CountingMethodValue»
Valoare | Nume | Definiție
counted | numărate | Unitățile definite de «countUnitValues» au fost numărate.
estimated | estimate | Unitățile definite de «countUnitValues» au fost estimate.
calculated | calculate | Unitățile definite de «countUnitValues» au fost calculate cu ajutorul unei tehnici de modelare.
18.4.2. Unitatea de numărare (CountingUnitValue)
Unitate definită utilizată pentru a exprima o cifră numărată sau estimată care indică abundența unei specii în cadrul unei «SpeciesDistributionUnit».
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate pentru una dintre următoarele liste de coduri din Ghidul tehnic INSPIRE privind distribuția speciilor:
— Unitate generală de numărare (GeneralCountingUnitValue): Unitatea utilizată pentru a exprima o cifră numărată sau estimată care indică abundența în cadrul unei «SpeciesAggregationUnit» (de exemplu ocurențe sau dimensiunea populației).
— Unitate de numărare conformă articolului 17 (Article17CountingUnitValue): Unitatea utilizată în scopuri de raportare în conformitate cu articolul 17 din Directiva 92/43/CEE. Această unitate exprimă o cifră numărată sau estimată care indică abundența în cadrul unei unități de distribuție a speciilor (de exemplu ocurențe sau dimensiunea populației).
18.4.3. Codul denumirilor locale ale speciilor (LocalSpeciesNameCodeValue)
Identificator al speciilor preluat din orice sistem local de clasificare.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
18.4.4. Categoria de ocurențe (OccurrenceCategoryValue)
Densitatea populației speciei în cadrul «SpeciesDistributionUnit».
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «OccurrenceCategoryValue»
Valoare | Nume | Definiție
common | comună | Specia este considerată ca fiind comună în cadrul «SpeciesDistributionUnit», de către furnizorul datelor.
rare | rară | Specia este considerată ca fiind rară în cadrul «SpeciesDistributionUnit», de către furnizorul datelor.
veryRare | foarte rară | Specia este considerată ca fiind foarte rară în cadrul «SpeciesDistributionUnit», de către furnizorul datelor.
present | prezentă | Specia este prezentă în cadrul «SpeciesDistributionUnit».
absent | absentă | Specia a fost căutată, dar care nu a fost găsită în «SpeciesDistributionUnit».
18.4.5. Tipul populației (PopulationTypeValue)
Permanența populațiilor, în special în ceea ce privește speciile migratoare, în cadrul unei unități date de distribuție a speciilor.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind distribuția populației.
18.4.6. Calificator (QualifierValue)
Această valoare definește relația dintre conceptele taxonomice ale denumirii locale a unei specii și denumirea de referință a speciei dată de identificatorul de referință al speciei sau de un sistem de referință al speciei.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «QualifierValue»
Valoare | Nume | Definiție
congruent | congruente | Conceptele taxonomice sunt identice.
includedIn | inclus în | Conceptul taxonomic al «localSpeciesName» este inclus în conceptul de «referenceSpeciesName».
includes | include | Conceptul taxonomic al «localSpeciesName» include conceptul de «referenceSpeciesName».
overlaps | se suprapun | Conceptele taxonomice se suprapun parțial, dar fiecare dintre acestea deține o parte care nu este inclusă în cealaltă.
excludes | exclude | Conceptele taxonomice se exclud reciproc.
18.4.7. Codul de referință al speciilor (ReferenceSpeciesCodeValue)
Liste de referință care conțin identificatorii speciilor.
Valorile permise pentru această listă de coduri cuprind valorile din următoarele liste de coduri:
— Codul EU-Nomen (EuNomenCodeValue): Liste de referință care conțin identificatori de specii EU-Nomen, astfel cum se menționează în infrastructura paneuropeană a registrelor speciilor, disponibilă prin intermediul portalului EU-Nomen.
— Codul speciei conform EUNIS (EunisSpeciesCodeValue): Liste de referință care conțin identificatori de specii EUNIS, astfel cum se menționează în baza de date EUNIS privind biodiversitatea, publicată pe site-ul web al Agenției Europene de Mediu.
— Codul în temeiul Directivelor «Natura» (NatureDirectivesCodeValue): Liste de referință care conțin identificatori de specii în temeiul Directivelor «Natura», astfel cum se menționează în cadrul portalului de referință pentru Natura 2000, definit în Decizia de punere în aplicare 2011/484/UE a Comisiei.
18.4.8. Sistemul de referință al speciilor (ReferenceSpeciesSchemeValue)
Liste de referință care definesc un standard taxonomic și nomenclatural în funcție de care pot fi cartografiate denumirile de specii și conceptele taxonomice locale.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «ReferenceSpeciesSchemeValue»
Valoare | Nume | Definiție
eunomen | Eunomen | Denumiri și concepte taxonomice, astfel cum sunt definite de Inventarul paneuropean al speciilor, publicat de portalul EU-Nomen.
eunis | Eunis | Denumiri și concepte taxonomice, astfel cum sunt definite de lista EUNIS a speciilor.
natureDirectives | Directivele «Natura» | Denumiri și concepte taxonomice, astfel cum sunt definite de către listele de specii din Directiva 2009/147/CE (Directiva «Păsări») și Directiva 92/43/CEE (Directiva «Habitate»).
18.4.9. Statutul prezenței (ResidencyStatusValue)
Categoria de prezență a ocurențelor sau a populației estimate într-o unitate de agregare dată.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind distribuția speciilor.
18.5. Cerințe specifice categoriei
| (1) | În cazul în care sunt necesare reprezentări de tip rețea ale distribuțiilor speciilor, trebuie să se utilizeze Grid_ETRS89-LAEA, astfel cum este definit în secțiunea 2.2.1 din anexa II.
| (2) | Pentru obiectele spațiale «SpeciesDistributionUnit», (a) în cazul în care o specie nu a fost căutată în mod activ, atributul «distributionInfo» trebuie să fie nul (void), cu motivul «necunoscut», (b) iar în cazul în care o specie a fost căutată în mod activ, dar nu a fost găsită, valoarea atributului «occurenceCategory» al «DistributionInfoType» trebuie să fie «absent».
| (3) | În cazul în care geometriile obiectelor spațiale dintr-un set de date «aSpeciesDistributionUnit» sunt derivate din geometriile obiectelor spațiale dintr-un alt set de date, atunci acest set de date sursă (inclusiv versiunea sa) este descris ca parte din elementul de metadate aferent filiației.
18.6. Strat
Strat pentru categoria de date spațiale «Distribuția speciilor»
Numele stratului | Titlul stratului | Tip de obiect spațial
SD.<ValoaredinListadeCoduri>(15) | Distribuția speciilor (de <nume lizibil de către om>) | SpeciesDistributionUnit (speciesName / referenceSpeciesId: ReferenceSpeciesCodeValue)
Exemplu: SD.SulaBassana | Exemplu: Distribuția speciilor (de Sula bassana) |
19. RESURSE ENERGETICE (ENERGY RESOURCES)
19.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(4) «resursă de energie» (energy resource) înseamnă o concentrație sau o ocurență a unei surse de energie care ar fi putut fi, este sau poate fi prezentă în viitor.
(5) «combustibili fosili» (fossil fuels) înseamnă o formă de energie primară neregenerabilă formată prin procese naturale cum ar fi descompunerea anaerobă a organismelor moarte îngropate, care conține procentaje ridicate de carbon; printre aceștia se numără cărbunele, țițeiul și gazele naturale.
(6) «energie primară» (primary energy) înseamnă energie care nu a fost supusă niciunui proces de conversie sau de transformare.
(7) «energie neregenerabilă» (non-renewable energy) înseamnă resurse naturale care, datorită formării pe termen lung, nu pot fi produse, cultivate, generate sau utilizate la o scară care să poată susține consumul acesteia.
(8) «energie din surse regenerabile» (energy from renewable sources) înseamnă energie din surse regenerabile nefosile, respectiv eoliană, solară, aerotermală, geotermală, hidrotermală și energia oceanelor, hidroelectrică, biomasă, gaze de fermentare a deșeurilor, gaze provenite din stațiile de epurare a apelor uzate și din biogaze, în conformitate cu articolul 2 din Directiva 2009/28/CE a Parlamentului European și a Consiliului (16).
(9) «deșeuri ca resurse energetice» (waste as energy resources) înseamnă un combustibil care poate consta din mai multe materiale diferite provenite din deșeuri combustibile industriale, instituționale, spitalicești și deșeuri de uz casnic, cum ar fi materialele plastice, cauciucul, deșeurile de uleiuri fosile și alte substanțe similare. Acestea sunt solide sau lichide, regenerabile sau neregenerabile, biodegradabile sau nebiodegradabile.
19.2. Structura categoriei de date spațiale «Resurse energetice»
Tipurile specificate pentru categoria de date spațiale «Resurse energetice» sunt organizate în următoarele pachete:
— Baza resurselor energetice
— Resurse energetice – mod vector
— Acoperirea resurselor energetice
19.3. Baza resurselor energetice
19.3.1. Tipuri de date
19.3.1.1. Tip de interval al extinderii verticale (VerticalExtentRangeType)
Valoare care indică limitele superioare și inferioare ale intervalului de înălțime/de adâncime.
Atribute ale tipului de date «VerticalExtentRangeType»
Atribut | Definiție | Tip | Voidability
lowerBound | Valoare care indică limita inferioară a intervalului de înălțime/de adâncime. | Length | voidable
upperBound | Valoare care indică limita superioară a intervalului de înălțime/de adâncime. | Length |
Constrângeri ale tipului de date «VerticalExtentRangeType»
Valoarea «lowerBound» trebuie exprimată în metri.
Valoarea «upperBound» trebuie exprimată în metri.
19.3.1.2. Tip de extindere verticală (VerticalExtentType)
Proprietate a dimensiunilor verticale care constă dintr-o măsură absolută sau dintr-o serie de măsuri absolute referențiate la un nivel de referință vertical bine definit care este considerat în mod normal ca fiind originea (nivelul solului, nivelul mediu al mării etc.).
Atribute ale tipului de date «VerticalExtentType»
Atribut | Definiție | Tip | Voidability
verticalExtent | Extindere a dimensiunii verticale, reprezentată de o mărime scalară sau de o serie de valori. | VerticalExtentValue |
verticalReference | Nivel de referință care a fost ales pentru a determina adâncimea/înălțimea verticală. | VerticalReferenceValue |
19.3.1.3. Valoare a extinderii verticale (VerticalExtentValue)
Fie un număr unic sau o serie de valori ale înălțimii/adâncimii pentru a descrie poziția din punctul de vedere al înălțimii/adâncimii unei resurse energetice.
Acest tip este o uniune.
Atribute ale tipului de uniune «VerticalExtentValue»
Atribut | Definiție | Tip | Voidability
range | Seria de numere care reprezintă intervalul de înălțime sau adâncime al unei resurse energetice | VerticalReferenceRangeType |
scalar | Număr care reprezintă înălțimea sau adâncimea unei resurse energetice. | Length |
Constrângeri ale tipului de uniune «VerticalExtentValue»
Valoarea măsurii scalare trebuie măsurată în metri.
19.3.2. Liste de coduri
19.3.2.1. Cadru de clasificare și cuantificare (ClassificationAndQuantificationFrameworkValue)
Valorile pentru sistemele de clasificare cel mai des utilizate pentru a clasifica și a cuantifica resursele energetice.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind resursele energetice.
19.3.2.2. Clasa combustibililor fosili (FossilFuelClassValue)
Valori care indică diferitele niveluri de resurse de combustibili fosili.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind resursele energetice.
19.3.2.3. Resurse regenerabile și deșeuri (RenewableAndWasteValue)
Tipuri de resurse regenerabile și provenite din deșeuri.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «RenewableAndWasteValue»
Valoare | Nume | Definiție
biogas | biogaz | Un gaz compus în principal din metan și dioxid de carbon produs prin digestia anaerobă a biomasei.
geothermal | energie geotermală | Energie disponibilă sub formă de căldură eliebrată din scoarța terestră, de obicei sub formă de apă sau aburi fierbinți. Această producție de energie reprezintă diferența dintre entalpia fluidului extras din gaura de sondă și cea a fluidului eliminat. Este exploatată în situri adecvate pentru producerea de electricitate sau direct sub formă de căldură.
hydro | energie hidroelectrică | Energie potențială și cinetică a apei transformată în electricitate în centralele hidroelectrice.
industrialWaste | deșeuri industriale | Deșeuri de origine industrială neregenerabile (solide sau lichide) arse în mod direct pentru a produce electricitate și/sau căldură.
liquidBiofuels | biocombustibili lichizi | Biocombustibilii lichizi sunt biobenzina, biodieselul sau alți biocombustibili direct utilizați drept combustibil.
municipalSolidWaste | deșeuri urbane solide | Deșeuri produse de gospodării, industrie, spitale și de sectorul terțiar, ce conțin materiale biodegradabile care sunt incinerate în instalații speciale.
solarPhotovoltaic | energie solară fotovoltaică | Lumina solară transformată în energie electrică prin intermediul celulelor solare alcătuite în general din materiale semi-conductoare care, expuse la lumină, produc electricitate.
solarThermal | energie termică solară | Căldură provenită din radiațiile solare produsă cu ajutorul centralelor termoelectrice solare sau al echipamentelor de producere a căldurii.
solidBiomass | biomasă solidă | Materiale organice, nefosile, de origine biologică, care pot fi utilizate drept combustibil pentru producerea de căldură sau de electricitate.
tideWaveOcean | maree, val, ocean | Energia mecanică provenită din mișcarea mareelor, a valurilor sau din curenții marini și exploatată pentru a produce electricitate.
wind | energie eoliană | Energie cinetică a vântului exploatată pentru a produce electricitate cu ajutorul turbinelor eoliene.
19.3.2.4. Combustibili fosili (FossilFuelValue)
Tipuri de combustibili fosili.
Valorile permise pentru această listă de coduri cuprind numai valorile indicate în tabelul de mai jos.
Valori pentru lista de coduri «FossilFuelValue»
Valoare | Nume | Definiție
hardCoal | cărbune sărac în gaze | Sedimente de culoare neagră, combustibile, solide și organice, adesea cunoscute drept cărbune de calitate superioară, datorită puterii lor calorice ridicate, sau drept cărbune negru, având în vedere caracteristicile lor fizice. Această categorie include antracitul, cărbunele cocsificabil și alți cărbuni bituminoși.
lowRankCoal | cărbune de calitate inferioară | Sedimente combustibile, de culoare brună până la neagră, organice, fosile, care sunt neaglutinanți, sunt adesea cunoscute drept cărbune de calitate inferioară, din cauza puterii lor calorice scăzute, sau drept cărbune brun, având în vedere caracteristicile lor fizice. Această categorie include cărbuni subbituminoși și lignitul.
peat | turbă | Un depozit sedimentar moale, poros sau comprimat, de origine vegetală, cu un conținut mare de apă (până la 90 % în stare brută), ușor de tăiat, de culoare brun deschis până la închis.
crudeOil | țiței | Țițeiul este un tip de ulei mineral de origine naturală, care conține un amestec de hidrocarburi și impurități asociate, precum sulful. Se găsește în stare lichidă în condiții normale de temperatură și presiune de suprafață, iar caracteristicile sale fizice (densitate, vâscozitate etc.) sunt foarte variabile.
naturalGas | gaze naturale | Gaze aflate în zăcăminte subterane, lichefiate sau gazoase, și care constau în principal din metan.
naturalGasLiquids | lichide din gaze naturale | Hidrocarburi lichide sau lichefiate obținute din gaze naturale în instalații de separare sau de prelucrare a gazului.
oilSands | nisipuri petrolifere | Nisipurile petrolifere, nisipurile asfaltice sau, mai tehnic, nisipurile bituminoase, sunt nisipuri neconsolidate sau o gresie parțial consolidată, saturată cu o formă densă și extrem de vâscoasă de țiței, cunoscută din punct de vedere tehnic ca și bitum.
oilShales | șisturi bituminoase | Șist bituminos, cunoscut, de asemenea, drept șist cu formațiuni de kerogen, este o rocă sedimentară bogată în substanțe organice, cu aspect granular fin, care conține kerogen (hidrocarburi imature).
19.3.2.5. Referință verticală (VerticalReferenceValue)
Valori care indică nivelul de referință al întinderii verticale.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind resursele energetice.
19.4. Resurse energetice – mod vector
19.4.1. Tipuri de obiecte spațiale
Pachetul «Resurse energetice – mod vector» conține următoarele tipuri de obiecte spațiale:
— Resurse energetice – mod vector
— Resurse de combustibili fosili
— Resurse regenerabile și provenite din deșeuri
19.4.1.1. Resurse energetice – mod vector (VectorEnergyResource)
Un obiect spațial vectorial care definește o întindere spațială dedusă sau observabilă a unei resurse care poate fi sau care a fost utilizată ca sursă de energie.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «VectorEnergyResource»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
geometry | Reprezentare geometrică a întinderii spațiale acoperite de această resursă energetică. | GM_Object |
classificationAndQuantificationFramework | Un sistem de clasificare de referință pentru a clasifica și a cuantifica resursele energetice. | ClassificationAndQuantificationFrameworkValue |
verticalExtent | Proprietate a dimensiunilor verticale care constă dintr-o măsură absolută sau dintr-o serie de măsuri absolute referențiate la un nivel de referință vertical bine definit care este considerat în mod normal ca fiind originea (nivelul solului, nivelul mediu al mării etc.). | VerticalExtentType | voidable
exploitationPeriod | «exploitationPeriod» definește data de început și, dacă este aplicabil, data de încheiere a exploatării aplicației. | ExploitationPeriodType | voidable
reportingAuthority | Organizație responsabilă cu raportarea cu privire la resursele energetice produse și estimate. | RelatedParty | voidable
resourceName | Numele resursă energetice. | GeographicalName | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
19.4.1.2. Resurse de combustibili fosili (FossilFuelResource)
Un obiect spațial care definește o întindere spațială dedusă sau observabilă a unei resurse care poate fi sau care a fost utilizată ca sursă de energie provenită din combustibili fosili. Cele mai frecvene tipuri de combustibili fosili sunt cărbunele, gazele naturale și țițeiul.
Acest tip este un subtip al «VectorEnergyResource».
Atribute ale tipului de obiect spațial «FossilFuelResource»
Atribut | Definiție | Tip | Voidability
resource | Tipul și cantitatea de resurse de combustibili fosili într-un singur obiect spațial. | FossilFuelResourceType |
dateOfDiscovery | Data la care a fost descoperită sursa de energie. | TM_Position | voidable
19.4.1.3. Resurse regenerabile și provenite din deșeuri (RenewableAndWasteResource)
Un obiect spațial care definește o întindere spațială dedusă sau observabilă a unei resurse care poate fi sau care a fost utilizată ca sursă de energie regenerabilă sau ca sursă de deșeuri.
Acest tip este un subtip al «VectorEnergyResource».
Atribute ale tipului de obiect spațial «RenewableAndWasteResource»
Atribut | Definiție | Tip | Voidability
capacity | Capacitatea energetică a unei resurse de energie regenerabilă în cadru întinderii spațiale. | Measure | voidable
dateOfDetermination | Data la care a fost determinată capacitatea resursei. | TM_Position | voidable
typeOfResource | Tipul de resursă de energie regenerabilă sau de deșeuri. | RenewableAndWasteValue |
19.4.2. Tipuri de date
19.4.2.1. Tipul intervalului caloric (CalorificRangeType)
Valoare care indică limitele superioare și inferioare ale intervalului caloric al resursei energetice.
Atribute ale tipului de date «CalorificRangeType»
Atribut | Definiție | Tip | Voidability
lowerBound | Valoare care indică limita inferioară a intervalului caloric. | Measure |
upperBound | Valoare care indică limita superioară a intervalului caloric. | Measure |
19.4.2.2. Tipul valorii calorice (CalorificValueType)
Valoare sau serie de valori care descriu valoarea calorică a unei resurse energetice.
Acest tip este o uniune.
Atribute ale tipului de uniune «CalorificValueType»
Atribut | Definiție | Tip | Voidability
calorificRange | O serie de valori calorice care descriu valoarea calorică a unei resurse energetice. | CalorificRangeType |
calorificScalar | Măsură care cuantifică proprietatea calorică a unei resurse energetice. | Measure |
19.4.2.3. Tipul perioadei de exploatare (ExploitationPeriodType)
«exploitationPeriod» (Perioadadeexploatare) definește data de început și, dacă este aplicabil, data de încheiere a exploatării aplicației.
Atribute ale tipului de date «ExploitationPeriodType»
Atribut | Definiție | Tip | Voidability
beginTime | Momentul în care a început exploatarea. | TM_Position |
endTime | Momentul în care s-a încheiat exploatarea. | TM_Position |
19.4.2.4. Măsura combustibililor fosili (FossilFuelMeasure)
Cantitatea de resurse în funcție de clasificarea în categorii specifice.
Atribute ale tipului de date «FossilFuelMeasure»
Atribut | Definiție | Tip | Voidability
amount | Cantitatea de resurse prezente în obiectul spațial. | Measure |
dateOfDetermination | Data cuantificării resursei. | TM_Position |
resourceClass | Categorie care indică nivelurile diferite de încredere în ceea ce privește o resursele de combustibili fosili, cum ar fi existența inițială, zăcăminte demonstrate sau eventuale. | FossilFuelClassValue |
19.4.2.5. Tip resurselor de combustibili fosili (FossilFuelResourceType)
Tipul și cantitatea resurselor în conformitate cu clasificarea în categorii specifice.
Atribute ale tipului de date «FossilFuelResourceType»
Atribut | Definiție | Tip | Voidability
calorificValue | Fiecare resursă de combustibili fosili este caracterizată de propria sa valoare calorică, și anume de cantitatea de energie disponibilă într-o unitate de masă. | CalorificValueType | voidable
quantity | Cantitatea de resurse în funcție de clasificarea în categorii specifice. | HydrocarbonMeasure | voidable
typeOfResource | Tipul de combustibil fosil. | FossilFuelValue |
19.5. Acoperirea resurselor energetice
19.5.1. Tipuri de obiecte spațiale
Pachetul «Acoperirea resurselor energetice» conține tipul de obiect spațial «Acoperirea potențialului de energii regenerabile și de deșeuri».
19.5.1.1. Acoperirea potențialului de energii regenerabile și de deșeuri (RenewableAndWastePotentialCoverage)
Funcție care returnează o valoare energetică potențială din intervalul său pentru orice poziție directă în cadrul domeniului său spațial, temporal sau spațio-temporal.
Acest tip este un subtip al «RectifiedGridCoverage».
Atribute ale tipului de obiect spațial «RenewableAndWastePotentialCoverage»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
potentialType | Există diverse tipuri de energie potențială, fiecare fiind asociată cu un anumit tip de putere. | PotentialTypeValue |
typeOfResource | Tipul resurselor regenerabile și provenite din deșeuri căruia i se aplică fenomentul măsurat. | RenewableAndWasteValue |
domainExtent | Atributul «domainExtent» conține extinderea domeniului spațio-temporal al acoperirii. Extinderea poate fi indicată atât în spațiu, cât și în timp. | EX_Extent |
assessmentMethod | O trimitere la metoda utilizată pentru evaluarea potențialului resursei energetice. | DocumentCitation | voidable
name | Numele acoperirii. | CharacterString | voidable
validTime | Perioada de timp pentru care această acoperire este reprezentativă. | TM_Period | voidable
verticalExtent | Un număr sau o serie de valori ale înălțimii/adâncimii pentru a descrie înălțimea/adâncimea pentru care este valabil intervalul valorilor de referință. | VerticalExtentType | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Constrângeri ale tipului de obiect spațial «RenewableAndWastePotentialCoverage»
Valorile «rangeSet» trebuie să fie de tipul «Measure».
19.5.2. Liste de coduri
19.5.2.1. Tipul de potențial (PotentialTypeValue)
Tipuri de energii potențiale obținute din resurse regenerabile și resurse provenite din deșeuri.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate pentru una dintre următoarele liste de coduri din Ghidul tehnic INSPIRE privind resursele energetice:
— Potențial geotermal (GeothermalPotentialValue): Tipuri de energie geotermală potențială.
— Potențial hidroenergetic (HydroPotentialValue): Tipuri de hidroenergii potențiale.
— Potențial solar (SolarPotentialValue): Tipuri de energii solare potențiale.
— Potențial maremotric (TidalPotentialValue): Tipuri de energii maremotrice potențiale.
— Potențial eolian (WindPotentialValue): Tipuri de energii eoliene potențiale.
19.6. Cerințe specifice categoriei
În cazul în care de geometria obiectului spațial este derivată dintr-un alt obiect spațial, geometriile celor două obiecte trebuie să fie consecvente.
19.7. Straturi
Straturi pentru categoria de date spațiale «Resurse energetice»
Numele stratului | Titlul stratului | Tip de obiect spațial
ER. FossilFuelResource | Resurse de combustibili fosili | FossilFuelResource
ER.RenewableAndWasteResource | Resurse regenerabile și provenite din deșeuri | RenewableAndWasteResource
ER.RenewableAndWastePotentialCoverage | Acoperirea potențialului de energii regenerabile și de deșeuri | RenewableAndWastePotentialCoverage
20. RESURSE MINERALE
20.1. Definiții
Pe lângă definițiile stabilite la articolul 2, se aplică următoarele definiții:
(1) «substanță» (commodity) înseamnă un material de interes economic într-o resursă terestră.
(2) «mină» (mine) înseamnă o activitate de excavare pentru extracția zăcămintelor de minerale, inclusiv exploatări în subteran și exploatări în carieră (denumite, de asemenea, exploatări la zi) pentru extracția de substanțe metalice, precum și exploatări în carieră pentru extracția mineralelor industriale (cunoscute în limbajul comun drept cariere).
(3) «activitate de minerit» (mining activity) înseamnă procesul de extracție a zăcămintelor de minerale metalice sau nemetalice din pământ.
20.2. Structura categoriei de date spațiale «Resurse minerale»
Tipurile specificate pentru categoria de date spațiale «Resurse minerale» sunt organizate în următoarele pachete:
— Resurse minerale
— Geologie (Geology) (pentru tipul de obiect spațial «MappedFeature», specificat în secțiunea 4.2.1.10 din anexa III)
20.3. Resurse minerale
Pachetul «Resurse minerale» conține următoarele tipuri de obiecte spațiale:
— Resurse terestre
— Ocurență minerală
— Substanță
— Activitate de prospectare
— Caracteristică a mineritului
— Ocurența caracteristicii mineritului
— Mină
— Activitate minieră
20.3.1. Tipuri de obiecte spațiale
20.3.1.1. Resurse terestre (EarthResource)
Tipurile de fenomene observabile sau deduse necesare pentru a clasifica resursele terestre economice și neeconomice.
Acest tip este un subtip al «GeologicFeature».
Acest tip este abstract.
Atribute ale tipului de obiect spațial «EarthResource»
Atribut | Definiție | Tip | Voidability
dimension | Dimensiunea/volumul resurselor terestre. | EarthResourceDimension | voidable
expression | Un indicator menit să arate dacă o «EarthResource» apare la suprafață sau dacă a fost detectată sub straturile de roci. | Category | voidable
form | Relația fizică și structurală tipică a zăcământului de minereuri cu rocile de fundament sau cu rocile asociate. | Category | voidable
linearOrientation | Orientarea liniară a «Earth Resource». | CGI_LinearOrientation | voidable
planarOrientation | Orientarea plană a «Earth Resource». | CGI_PlanarOrientation | voidable
shape | Forma geometrică tipică a «Earth Resource». | Category | voidable
sourceReference | Referința sursei pentru «Resursa terestră». | DocumentCitation | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanversion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «EarthResource»
Rol de asociere | Definiție | Tip | Voidability
oreAmount | Cantitatea estimată sau calculată a zăcămintelor de minereu, cu identificarea substanțelor conținute și a concentrației lor. | OreMeasure | voidable
explorationHistory | Lista cronologică a prospectărilor efectuate, pentru a defini mai bine potențialul unei ocurențe minerale. | ExplorationActivity | voidable
classification | Clasificarea «EarthResource». | MineralDepositModel | voidable
resourceExtraction | Una sau mai multe perioade de activitate minieră vizând resursele terestre. | MiningActivity | voidable
commodityDescription | Substanțele prezente în cadrul resursei, clasificate în ordinea importanței | Commodity |
20.3.1.2. Ocurență minerală (MineralOccurrence)
O acumulare de minerale în litosferă.
Acest tip este un subtip al «EarthResource».
Atribute ale tipului de obiect spațial «MineralOccurrence»
Atribut | Definiție | Tip | Voidability
type | Tipul de ocurență minerală. | MineralOccurrenceTypeValue |
endusePotential | Potențial de utilizare finală al mineralului. | EndusePotentialValue | voidable
20.3.1.3. Substanță (Commodity)
Materialul de interes economic aparținând «EarthResource».
Atribute ale tipului de obiect spațial «Commodity»
Atribut | Definiție | Tip | Voidability
commodityImportance | Importanța zăcământului pentru substanța respectivă. | ImportanceValue | voidable
commodity | Substanță provenind din resursele terestre. | CommodityCodeValue |
commodityRank | Poziția ocupată de substanță. | Integer | voidable
Roluri de asociere ale tipului de obiect spațial «Commodity»
Rol de asociere | Definiție | Tip | Voidability
source | Zăcământul/resursa din care provine substanța. | EarthResource |
20.3.1.4. Activitate de prospectare (ExplorationActivity)
O perioadă de activitate de prospectare.
Atribute ale tipului de obiect spațial «ExplorationActivity»
Atribut | Definiție | Tip | Voidability
activityDuration | Perioadă, sau întinderea în timp, a activității de prospectare. | TM_Period |
activityType | Tipul de activitate de prospectare. | ExplorationActivityTypeValue |
explorationResult | Rezultatul activității de prospectare. | ExplorationResultValue |
20.3.1.5. Caracteristică a mineritului (MiningFeature)
Tipul de obiect spațial care grupează proprietățile comune ale minelor și activităților miniere.
Acest tip este abstract.
Atribute ale tipului de obiect spațial «MiningFeature»
Atribut | Definiție | Tip | Voidability
inspireId | Identificator de obiect extern al obiectului spațial. | Identifier |
20.3.1.6. Ocurență a caracteristicii mineritului (MiningFeatureOccurrence)
O reprezentare spațială a unei «MiningFeature».
Atribute ale tipului de obiect spațial «MiningFeatureOccurrence»
Atribut | Definiție | Tip | Voidability
shape | Geometria «MiningFeature». | GM_Object |
Roluri de asociere ale tipului de obiect spațial «MiningFeatureOccurrence»
Rol de asociere | Definiție | Tip | Voidability
specification | Indică «MiningFeature» pe care o specifică «MiningFeatureOccurrence». | MiningFeature |
20.3.1.7. Mină (Mine)
Lucrări de excavare efectuate pentru extracția de zăcăminte de minerale.
Acest tip este un subtip al «MiningFeature».
Atribute ale tipului de obiect spațial «Mine»
Atribut | Definiție | Tip | Voidability
mineName | Tip de date care indică denumirea minei și dacă aceasta este denumirea preferată. | MineName |
status | Valoarea statutului operațional al minei. | MineStatusValue |
sourceReference | Referința sursei pentru mină. | DocumentCitation | voidable
startDate | Data la care a început exploatarea minei. | TM_Instant | voidable
endDate | Data la care s-a încheiat exploatarea minei. | TM_Instant | voidable
beginLifespanVersion | Data și ora la care versiunea obiectului spațial a fost inserată sau modificată în cadrul setului de date spațiale. | DateTime | voidable
endLifespanVersion | Data și ora la care versiunea obiectului spațial a fost înlocuită sau retrasă din setul de date spațiale. | DateTime | voidable
Roluri de asociere ale tipului de obiect spațial «Mine»
Rol de asociere | Definiție | Tip | Voidability
relatedMine | O mină asociată. | Mine | voidable
relatedActivity | «MiningActivity» asociată cu mina. | MiningActivity |
20.3.1.8. Activitate minieră (MiningActivity)
Procesul de extracție a zăcămintelor de roci metalice, nemetalice sau industriale din Pământ.
Acest tip este un subtip al «MiningFeature».
Atribute ale tipului de obiect spațial «MiningActivity»
Atribut | Definiție | Tip | Voidability
activityDuration | Perioadă, sau întinderea în timp, a activității miniere. | TM_Period |
activityType | Tipul de activitate minieră. | MiningActivityTypeValue |
oreProcessed | Cantitatea de minereu prelucrate în urma activității. | Quantity | voidable
processingType | Tipul de prelucrare efectuată în timpul activității miniere. | ProcessingActivityTypeValue |
Roluri de asociere ale tipului de obiect spațial «MiningActivity»
Rol de asociere | Definiție | Tip | Voidability
associatedMine | Mina în care a avut sau are loc activitatea minieră. | Mine | voidable
deposit | Zăcământul cu care activitatea minieră este asociată. | EarthResource | voidable
20.3.2. Tipuri de date
20.3.2.1. Cantitatea substanței (CommodityMeasure)
O măsură a cantității substanței pe baza calculării rezervelor, a resurselor sau a potențialului.
Atribute ale tipului de date «CommodityMeasure»
Atribut | Definiție | Tip | Voidability
commodityAmount | Cantitatea de substanță. | QuantityRange | voidable
cutOffGrade | Concentrația fragmentului (cut-off grade) utilizată pentru calcularea cantității substanței. | QuantityRange | voidable
grade | Concentrația substanței. | QuantityRange | voidable
Roluri de asociere ale tipului de date «CommodityMeasure»
Rol de asociere | Definiție | Tip | Voidability
commodityOfInterest | Substanța la care se referă «CommodityMeasure». | Commodity |
20.3.2.2. Dimensiunea resurselor terestre (EarthResourceDimension)
Mărimea și volumul resurselor terestre.
Atribute ale tipului de date «EarthResourceDimension»
Atribut | Definiție | Tip | Voidability
area | Suprafața resursei terestre. | QuantityRange | voidable
depth | Adâncimea resursei terestre. | QuantityRange | voidable
length | Lungimea resursei terestre. | QuantityRange | voidable
width | Lățimea resursei terestre. | QuantityRange | voidable
20.3.2.3. Potențial (Endowment)
Cantitatea dintr-un mineral (sau dintr-un grup de minerale pentru roci industriale) prezent în stocuri (zăcăminte) care îndeplinește caracteristici fizice specifice, cum ar fi calitatea, dimensiunea și adâncimea.
Acest tip este un subtip al «OreMeasure».
Atribute ale tipului de date «Endowment»
Atribut | Definiție | Tip | Voidability
includesReserves | Simbol care indică dacă estimarea include valoarea rezervelor. | Boolean | voidable
includesResources | Simbol care indică dacă estimarea include valoarea resurselor. | Boolean | voidable
20.3.2.4. Denumirea minei (MineName)
Un tip de date care indică denumirea minei și dacă aceasta este denumirea preferată.
Atribute ale tipului de date «MineName»
Atribut | Definiție | Tip | Voidability
isPreferred | Un operator boolean care indică dacă valoarea din «mineName» este denumirea preferată a minei. | Boolean |
mineName | Denumirea minei. | CharacterString |
20.3.2.5. Modelul zăcământului de minerale (MineralDepositModel)
Informații aranjate în mod sistematic care descriu atributele esențiale ale unei categorii de zăcăminte de minerale. Acestea pot fi empirice (descriptive) sau teoretice (genetice).
Atribute ale «MineralDepositModel»
Atribut | Definiție | Tip | Voidability
mineralDepositGroup | O grupare de zăcăminte de minerale definite de caracteristici generice. | MineralDepositGroupValue |
mineralDepositType | Stilul ocurenței sau al zăcământului. | MineralDepositTypeValue | voidable
20.3.2.6. Măsura minereurilor (OreMeasure)
Estimarea rezervelor, a resurselor sau a potențialului de minereuri.
Acest tip este abstract.
Atribute ale tipului de date «OreMeasure»
Atribut | Definiție | Tip | Voidability
classificationMethodUsed | Modalitatea de calculare a măsurării. | ClassificationMethodUsedValue |
date | Data valorii calculate sau estimate. | TM_GeometricPrimitive |
dimension | Mărimea corpului utilizat la calcul. | EarthResourceDimension | voidable
ore | Cantitatea de minereu. | QuantityRange |
proposedExtractionMethod | Metoda propusă pentru extracția substanței. | Category | voidable
sourceReference | Referința pentru valorile «OreMeasure». | DocumentCitation |
Roluri de asociere ale tipului de date «OreMeasure»
Rol de asociere | Definiție | Tip | Voidability
measureDetails | O măsură a cantității din fiecare substanță, bazată pe o calculare a rezervelor, resurselor sau a potențialului. | CommodityMeasure |
20.3.2.7. Rezervă (Reserve)
Parte exploatabilă din punct de vedere economic a unei resurse minerale măsurate și/sau a unei resurse minerale indicate.
Acest tip este un subtip al «OreMeasure».
Atribute ale tipului de date «Reserve»
Atribut | Definiție | Tip | Voidability
category | Nivelul de încredere al estimării. | ReserveCategoryValue |
20.3.2.8. Resurse (Resource)
O acumulare de interese economice materiale intrinseci în sau pe scoarța Pământului într-o formă, de o calitate și într-o cantitate astfel încât că există perspective rezonabile pentru e extracție economică.
Acest tip este un subtip al «OreMeasure».
Atribute ale tipului de date «Resource»
Atribut | Definiție | Tip | Voidability
category | Indiciu conform căruia resursa este măsurată, indicată sau dedusă. | ResourceCategoryValue |
includesReserves | Un steag care indică dacă estimarea resurselor include valorile rezervelor. | Boolean | voidable
20.3.3. Liste de coduri
20.3.3.1. Metoda de clasificare utilizată (ClassificationMethodUsedValue)
Coduri care indică metodologia utilizată pentru a calcula măsurarea minereurilor.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «ClassificationMethodUsedValue»
Valoare | Nume | Definiție
JORCcode | JORC code | Codul australasiatic pentru comunicarea rezultatelor prospectării și resursele și rezervele minerale.
NI43-101 | NI 43-101 | National Instrument 43-101 (the «NI 43-101» or the «NI») este un sistem de clasificare a resurselor minerale utilizat pentru punerea la dispoziția publicului a informațiilor referitoare la proprietățile minerale din Canada.
CIMstandards | CIM standards | Standardele CIM de definire a resurselor și rezervelor minerale (CIM Definition Standards) stabilesc definiții și orientări pentru raportarea informațiilor referitoare la prospectări, la resursele și rezervele minerale din Canada.
SAMRECcode | SAMREC code | Codul sud-african pentru comunicarea rezultatelor prospectărilor și resursele și rezervele minerale.
IMMReportingCode | IMM Reporting Code | Codul pentru raportarea resurselor și rezervelor minerale, stabilește standarde minime, recomandări și orientări pentru o raportare publică a rezultatelor prospectărilor, a resurselor și a rezervelor minerale din Regatul Unit, Irlanda și Europa.
SMEGuide | SME Guide | Un ghid pentru raportarea informațiilor referitoare la prospectare, a resurselor și rezervelor minerale – SUA
IIMChCode | IIMCh Code | Codul de certificare pentru perspective de prospectare, resurse minerale și rezerve de minereuri. Acest cod este rezultatul unui acord de colaborare între Institution of Mining Engineers of Chile (Institutul de ingineri în minerit din Chile - IIMCh) și ministerul mineritului.
peruvianCode | Peruvian Code | Acest cod a fost elaborat de un comitet mixt format din membri ai bursei de valori de la Lima și din profesioniști în materie de prospectare și evaluare a resurselor minerale.
CRIRSCOCode | CRIRSCO Code | Modelul internațional pentru raportarea rezultatelor prospectării, a resurselor și rezervelor minerale al Comitetului pentru Standardele internaționale de raportare a rezervelor minerale (CRIRSCO) integrează normele minime adoptate în codurile de raportare naționale de la nivel mondial, precum și recomandările și orientările pentru raportarea publică a rezultatelor prospectării, a resurselor și rezervelor minerale.
UNFCCode | UNFC Code | The United Nations Framework Classification for Fossil Energy and Mineral Reserves and Resources 2009 (Clasificarea-cadru a Națiunilor Unite în ceea ce privește energia fosilă și rezervele și resursele minerale 2009) (UNFC-2009) este un sistem aplicabil la nivel global pentru clasificarea/evaluarea rezervelor și resurselor energetice și minerale – este succesorul UNFC-2004.
SECGuide | SEC Guide | Descrierea proprietății de către emitenții implicați sau care urmează să fie implicați în operațiuni de minerit semnificative. Dezvoltat de United States Securities and Exchange Commission.
PERCCode | PERC Code | Codul comitetului paneuropean responsabil cu raportarea rezervelor și resurselor (PERC) pentru raportarea rezultatelor prospectărilor, a resurselor și rezervelor minerale (denumit în continuare «the Code») stabilește standarde minime, recomandări și orientări pentru Raportarea publică a rezultatelor prospectărilor, a resurselor și rezervelor minerale din Regatul Unit, Irlanda și Europa.
russianCode | Russian Code | În prezent, în Rusia este în vigoare Codul aprobat prin Decretul ministerului reurselor naturale, RF RF Nr. 278 din 11 decembrie 2006. Titlul complet al documentului: Classification of resources/reserves and prognostic resources of solid minerals.
historicResourceEstimate | estimarea istorică a resurselor | Termen pentru estimare înainte de «coduri standard» (de exemplu JORC etc.)
20.3.3.2. Codul substanței (CommodityCodeValue)
Valori care indică tipul substanței.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind resursele minerale.
20.3.3.3. Potențial de utilizare finală (EndusePotentialValue)
Valori care indică potențialul de utilizare finală a mineralului.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «EndusePotentialValue»
Valoare | Nume | Definiție | Parent
metallicMinerals | minerale metalice | Ocurențe minerale, inclusiv orice tip de mineral metalic. |
preciousMetals | metale prețioase | Ocurențe minerale, inclusiv argint; aur; platinoide în general. | metallicMinerals
baseMetals | metale comune | Ocurențe minerale, inclusiv aluminiu; cupru; plumb; plumb + zinc; staniu; zinc | metallicMinerals
ironFerroalloyMetals | fier și metale pentru aliaje feroase | Ocurențe minerale, inclusiv cobalt; crom; fier; mangan; molibden; niobiu; nichel; vanadiu; tungsten. | metallicMinerals
specialityAndRareMetals | metale de specialitate și metale rare | Ocurențe minerale, inclusiv beriliu; bismut; cadmiu; germaniu, galiu; hafniu; mercur; indiu; litiu; rubidiu, cesiu; reniu; pământuri rare (nediferențiate); antimoniu; seleniu; tantal; telur; titan (ilmenit, rutil); zirconiu (zircon, baddeleyit). | metallicMinerals
nonMetallicMinerals | minerale nemetalice | Ocurențe minerale, inclusiv orice tip de mineral nemetalic. |
buildingRawMaterial | materii prime pentru construcții | Ocurențe minerale, inclusiv piatră concasată; pietre de mari dimensiuni și pietre ornamentale (granit, gabro, travertin etc.); gips, anhidrit; ciment de var; calcar utilizat pentru var; marmură. | nonMetallicMinerals
ceramicAndRefractory | pietre ceramice și refractare | Ocurențe minerale, inclusiv argile comune (cărămizi, tigle); argile albe (argile refractare și ceramice); dolomită; feldspat, nefelin; caolin; grupul andaluzit (andaluzit, cianit, silimanit). | nonMetallicMinerals
chemicalMinerals | minerale chimice | Ocurențe minerale, inclusiv borați; barită; fluorită; magneziu (magnezită); sulfat de sodiu; carbonat de sodiu (trona); pirită; sulf; sare gemă; stronțiu; zeoliți. | nonMetallicMinerals
energyCoverMinerals | minerale care acoperă necesarul energetic | Ocurențe minerale inclusiv gresie bituminoasă/calcal bituminos, ist bituminos; cărbune; lignit; turbă; toriu; uraniu. | nonMetallicMinerals
fertilizer | îngrășământ | Ocurențe minerale, inclusiv fosfat; potasa (silvinit, carnalit). | nonMetallicMinerals
preciousAndSemiPreciousStones | pietre prețioase și semiprețioase | Ocurențe minerale (inclusiv diamant (industrial și ca piatră gemă); smarald; rubin, safir, corindon (piatră gemă); beriluri, cuarț, tourmaline, granate, topaz, peridot, zirconiu etc. (pietre geme). | nonMetallicMinerals
specialityAndOtherIndustrialMinerals | roci și minerale de specialitate și alte roci și minerale | Ocurențe minerale inclusiv abrazive: granat, staurolit, corindon; azbest (antofillit, crisotil, crocidolit); attapulgit, sepiolit (argilă); bentonită (argilă); calcar, calcit (agent de umplere); diatomit (kieselgur); grafit; mică; perlit; cuarț (masiv / bloc pentru ferosiliciu); cuarț, utilizare optică și piezoelectrică; nisip de siliciu; talc, pirofilit; vermiculit; wollastonit. | nonMetallicMinerals
recycledWaste | deșeuri reciclate | Ocurențe minerale, inclusiv metale sau minerale provenite din tratarea deșeurilor miniere. |
20.3.3.4. Tipul activităților de explorare (ExplorationActivityTypeValue)
Tipuri de activități de prospectare efectuate.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Această listă de coduri este ierarhică.
Valori pentru lista de coduri «ExplorationActivityTypeValue»
Valoare | Nume | Definiție | Parent
regionalReconnaissance | recunoaștere regională | Investigare regională pentru identificarea de anomalii (geochimice, geofizice, mineralogice) și pentru a descoperi ocurențe. |
hammerProspectingAndGeologicalReconnaissance | prospectare cu ajutorul ciocanului și recunoaștere geologică | Elaborarea unei hărți geologice preliminare conținând principalele formațiuni și structuri, inclusiv privind amplasamentul dovezilor minerale descoperite. | regionalReconnaissance
regionalGeochemistry | geochimie regională | Detectarea concentrațiilor anormale de elemente chimice în apele de suprafață, soluri sau organisme, de obicei realizată cu ajutorul unor instrumente, analize punctuale sau tehnici rapide aplicabile pe teren. | regionalReconnaissance
airborneGeophysics | aerogeofizică | Tehnica de prospectare bazată pe detectarea caracteristicilor fizice anormale ale unui sol. | regionalReconnaissance
regionalHeavyMineralSampling | eșantionare regională de minerale grele | Prospectare cu un instrument manual de spălat, de obicei de forma unei plăci sau a unui con plat, în a cărui parte inferioară sunt colectate cele mai dense fragmente ale unui sol sau ale unui sediment aluvial. | regionalReconnaissance
detailedSurfaceExploration | prospectare detaliată de suprafață | Prospectare detaliată de suprafață pentru a delimita anomaliile și a descrie ocurențele în contextul lor geologic rafinat. |
geologicalMappingAndSampling | cartografiere și eșantionare geologică | Cartografiere geologică detaliată a zonei (zonelor) de interes. | detailedSurfaceExploration
detailedGeochemistry | geochemie detaliată | Anchete detaliate (deseori pe un caroiaj) utilizând metoda cea mai adecvată, cu scopul de a confirma, de a delimita și de a caracteriza mai precis anomaliile geochimice identificate în faza anterioară. | detailedSurfaceExploration
detailedGeophysics | geofizică detaliată | Anchete detaliate (în general pe un caroiaj), utilizând metoda cea mai adecvată, cu scopul de a confirma, de a delimita și de a caracteriza mai precis anomaliile geofizice identificate în faza anterioară. | detailedSurfaceExploration
detailedHeavyMineralSampling | eșantionare detaliată a de minerale grele | Prospectare detaliată la scară locală, cu ajutorul unui instrument manual de spălat, de obicei de forma unei plăci sau a unui con plat, în a cărui parte inferioară sunt colectate cele mai dense fracțiuni ale unui sol sau ale unui sediment aluvial. | detailedSurfaceExploration
subsurfaceExploration | prospectare subterană | Prospectare subterană utilizând tehnici necostisitoare (săparea de șanturi, practici de foraj distructive etc.) a evaluării resurselor. |
trenchingChannelSampling | îndepărtarea materialului de copertă, săparea de șanțuri, eșantionare cu ajutorul canalelor | Șanț de mică adâncime din care se poate preleva un eșantion pe baza căruia se poate face o observație geologică. | subsurfaceExploration
augerDrilling | foraj cu burghiu de mină | Forarea unei găuri cilindrice cu un instrument ad hoc pentru a colecta un eșantion de rocă sau pentru a efectua o măsurare fizică sau o observație geologică. Prin extensie, acesta desemnează, de asemenea, gaura forată, indiferent de scopul acesteia din urmă. În acest caz, forajul este efectuat cu ajutorul unui burghiu de mină. | subsurfaceExploration
percussionDrilling | foraj percutant | Forarea unei găuri cilindrice cu un instrument ad hoc pentru a colecta un eșantion de rocă sau pentru a efectua o măsurare fizică sau o observație geologică. Prin extensie, acesta desemnează, de asemenea, gaura forată, indiferent de scopul acesteia din urmă. În acest caz, forarea se efectuează cu o sculă percutantă. | subsurfaceExploration
assesmentOfResource | evaluarea resursei | Obiectivul acestei faze delimitarea (încă estimativă) a delimitării anvelopei unui zăcământ de minereu. Logging al carotelor, eșantionarea secțiunilor mineralizate pentru a înțelege mai bine caracteristicile distincte ale zăcământului, proprietățile fizice ale minereului, și, în fine, pentru a contribui la o primă calculare (încă aproximativă) a resursei. |
reconnaissancePercussionDrilling | foraj percutant de recunoaștere | Evaluarea resursei utilizând forajul percutant, uneori pe o plasă cu ochiuri mari. Obiectivul acestei faze delimitarea (încă estimativă) a delimitării anvelopei unui zăcământ de minereu. Logging de foraj, eșantionarea secțiunilor mineralizate pentru a înțelege mai bine caracteristicile distincte ale zăcământului, proprietățile fizice ale minereului, și, în fine, pentru a contribui la o primă calculare (încă aproximativă) a resursei. | assesmentOfResource
reconnaissanceCoreDrilling | foraj cu carotaj de recunoaștere | Forarea unei găuri cilindrice cu un instrument ad hoc pentru a colecta un eșantion de rocă sau pentru a efectua o măsurare fizică sau o observație geologică. Prin extensie, acesta desemnează, de asemenea, gaura forată, indiferent de scopul acesteia din urmă. Găurile de sondă sunt forate prin carotaj. Această tehnică este utilizat pentru a colecta cilindrii de rocă neafectați și permite confirmarea/indicarea rezultatelor forajului percutant. | assesmentOfResource
geologicalInterpretation | interpretare geologică | Compilarea și sintetizarea tuturor informațiilor geologice disponibile pentru a obține un model cât mai precis al resursei minerale. | assesmentOfResource
oreBeneficiationTest | teste de îmbogățire a minereurilor | Tehnică menită să trateze minereul brut. | assesmentOfResource
approximateResourceCalculation | calcul aproximativ al resursei | Evaluare aproximativă a tonajului și a concentrației în principal pe baza informațiilor despre găurile de sondă, prin corelare și interpolare a secțiunilor mineralizate intersectate. | assesmentOfResource
evaluationOfOreDeposit | evaluare depozitului de minereuri | Aceasta este faza finală a evaluării, care duce la decizia finală afirmativă/negativă referitoare la minerit. |
systematicReconnaissanceCoreDrilling | foraj cu carotaj de recunoaștere sistematică | Evaluarea zăcământului de minereuri cu scopul de a obține informații foarte detaliate privind întregul depozit și eșantioanele de cea mai bună calitate. Aceasta este faza finală a evaluării, care duce la decizia finală afirmativă/negativă referitoare la minerit. | evaluationOfOreDeposit
miningWorkings | exploatări miniere | Activități de recunoaștere care vizează o mai bună înțelegere a zăcământului și care permit obținerea unor eșantioane mari de minereuri pentru testele detaliate de îmbogățire. | evaluationOfOreDeposit
geostatisticalEstimates | estimările geostatistice | Tehnică bazată pe teoria probabilităților care este utilizată pentru a calcula variabilele regionalizate, ale căror valori depind de poziția lor în spațiu, cum ar fi conținutul sau concentrația metalelor dintr-un zăcământ. | evaluationOfOreDeposit
feasibilityStudyReport | studiu de fezabilitate și raport | Studiu tehnico-economic vizând evaluarea posibilității de a demara o afacere în sectorul minier. | evaluationOfOreDeposit
miningPilot | pilot minier | Etapă intermediară între testele de laborator și instalația efectivă. | evaluationOfOreDeposit
20.3.3.5. Rezultatul prospectării (ExplorationResultValue)
Valori care indică rezultatul activității de prospectare.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «ExplorationResultValue»
Valoare | Nume | Definiție
isolatedMineralizedStones | pietre mineralizate izolate, urme de mineralizare, ocurențe, zone alterate | Identificarea posibililor markei ai unei zone mineralizate.
anomalies | anomalii | Zonă cu anomalii ale cărei proprietăți geofizice sau geochimice sunt diferite de zonele din împrejurimi și care ar putea indica prezența unui proces de mineralizare în apropiere.
keyMineralsIdentification | identificarea principalelor minerale | Identificarea anumitor minerale care pot indica o eventuală zonă mineralizată sau care pot însoți un proces de mineralizare.
detailedProspectMap | hartă prospectivă detaliată cu localizarea zonelor mineralizate | O hartă detaliată cu localizarea tuturor ocurențelor mineralizate, indiferent de mărimea lor, și cu reprezentarea relațiilor acestora cu litologia, structurile în cauză, zonele de alterare, zonele anormale, rezultatele analizei eșantionării.
structuredAnomalies | anomalii structurate | Reducerea zonei care face obiectul prospectării minerale și o structură internă mai detaliată
prospectBoundariesRefinement | rafinarea limitelor prospectării | Reducerea progresivă a suprafaței până la descoperirea unui zăcământ de minerale.
primaryReconnaissanceMineralization | recunoaștere primară a mineralizării | Primele încercări de a vedea (îndepărtarea stratului de copertă, săparea de șanturi) sau de a intercepta (burghiu de mină, foraj percutant) și de a eșantiona mineralizarea primară.
indicatedMineralization | mineralizare indicată | Primele încercări de a delimita aproximativ zăcământul de minereu, cu utilizarea forajului de recunoaștere (foraj percutant și, apoi, foraj cu carotaj), cu scopul de a-l eșantiona în detaliu, precum și de a evalua aproximativ resursa, cu ajutorul interpretării geologice și a testelor de îmbogățire.
indicatedOreDeposit | zăcământ de minereu indicat | Prezența unui zăcământ de minereu a fost demonstrată cu ajutorul unui foraj de carotaj sistematic și, uneori, a unor activități miniere preliminare. Geometria externă a zăcământului de minereu și structura sa internă (inclusiv distribuția concentrației minereului) începe să fie cunoscută.
indicatedAndEstimatedOreDeposit | zăcământ de minereu indicat și estimat | Perfecționarea cunoștințelor anterioare, utilizând instrumente statistice care permit, de exemplu, interpolări între găuri de foraj, și definirea zonelor îmbogățite.
feasibilityStudyForMiningDecision | raport privind studiul de fezabilitate disponibil în vederea luării deciziei de minerit | Studiu tehnico-economic vizând evaluarea posibilității de a demara o afacere în sectorul minier.
industrialTest | încercare industrială | Etapă intermediară între testele de laborator și instalația efectivă.
20.3.3.6. Importanță (ImportanceValue)
Valori care indică importanța substanței pentru resursa terestră.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind resursele minerale.
20.3.3.7. Statutul minei (MineStatusValue)
Valori care indică statutul operațional ale minei.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «MineStatusValue»
Valoare | Nume | Definiție | Parent
operating | operating | O mină este în regim de funcționare. |
operatingContinuously | în regim de funcționare continuu | O mină este în regim de funcționare continuu. | operating
operatingIntermittently | în regim de funcționare intermitent | O mină este în regim de funcționare intermitent. | operating
notOperating | nu este în regim de funcționare | O mină nu este în regim de funcționare. |
closed | închisă | O mină poate fi închisă din motive tehnice, economice sau tehnico-economice. | notOperating
abandoned | abandonată | O mină este abandonată. | notOperating
careAndMaintenance | aflată în regim de îngrijire și întreținere | O mină este în regim de îngrijire și întreținere. | notOperating
retention | retenție | O mină poate fi păstrată neexploatată până când prețul substanței (substanțelor) o face rentabilă. | notOperating
historic | istoric | O mină «veche» care a fost exploatată înainte de 1900. | notOperating
underDevelopment | în curs de dezvoltare | În curs de dezvoltare. |
construction | în construcție | În construcție. | underDevelopment
pendingApproval | în așteptarea aprobării | O mină care așteaptă să primească autorizația de exploatare, dată, în general, de Departamentul de inginerie în domeniul mineritului al unui stat. | underDevelopment
feasibility | fezabilitate | Studiu tehnico-economic vizând evaluarea posibilității de a demara o afacere în sectorul minier. | underDevelopment
20.3.3.8. Grupul zăcămintelor de minerale (MineralDepositGroupValue)
Valori care indică grupul de zăcăminte de minerale pe baza caracteristicilor lor generale.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «MineralDepositGroupValue»
Valoare | Nume | Definiție
organic | organic | Zăcăminte organice rezultate din concentrația de materie organică la suprafață, sau aproape de aceasta, prin sedimentare și diageneză timpurie.
residualOrSurficial | rezidual/de suprafață | Procesele de suprafață sunt fenomenele fizice și chimice care produc concentrarea de minereuri în regolit, în general prin îndepărtarea compușilor chimici ca urmare a unei lixivieri apoase. Aceasta include zăcăminte de laterit și zăcăminte reziduale sau eluviale.
placer | zăcământ | Concentrări de minerale grele de anumite elemente, în special de Au, U și PGE, prin procese de sedimentare.
continentalSedimentAndVolcanics | sedimente continentale și materiale vulcanice | Zăcăminte de minerale asociate cu sedimente sau materiale vulcanice pe scoarță continentală. Acestea se formează atunci când rocile vulcanice și straturile de cenușă reacționează cu ape subterane alcaline, și pot, de asemenea, să cristalizeze în medii post-depoziționale pe perioade care variază între mii și milioane de ani în bazine marine de adâncime mică.
sedimentHosted | îngropate în roci sedimentare | Zăcăminte îngropate în roci sedimentare pot fi împărțite în două mari subtipuri. Primul subtip este format din minereuri de plumb-zinc dominate de clastic, care sunt găzduite în șisturi, gresie, aleurit sau în roci clastice mixte, sau care apar ca și înlocuitoare de carbonat, într-o secvență de rocă sedimentară dominată de clastic. Acest subtip include zăcămintele cunoscute în mod tradițional ca depozite sedimentare exhalative. Al doilea subtip de zăcăminte Pb-Zn îngropate în roci sedimentare este de tip «Mississippi Valley» și apare în secvențele carbonate de platformă, de obicei în medii tectonice de margine pasivă.
chemicalSediment | sedimente chimice | Zăcăminte de minerale, în principal Fe sau Mn, de origine sedimentară care au debutat ca precipitate chimice din apa oceanelor străvechi. Procesul de acumulare a acestor zăcăminte sedimentare este controlat de proprietățile fizico-chimice inerente fierului și manganului.
marineVolcanicAssociation | asociere între mediu marin și vulcanic | Zăcăminte de minerale, formate într-un mediu marin vulcanic. Fluidele magmatice și hidrotermice reacționează cu apa de mare pentru a da naștere la sulfuri masive volcanogene (VMS), care la origine au fost zăcăminte stratiforme de Cu, Zn, Pb, Ag, Au.
epithermal | epitermal | Zăcămintele epitermale apar, în mare parte, în arcuri vulcano-plutonice asociate cu zonele de subducție, cu vârste similare cu cele ale vulcanismului. Zăcămintele se formează la adâncime mică, la mai puțin de 1 km, în intervalul de temperatură 50°-200°C, și sunt găzduite în principal de roci vulcanice, apărând în principal ca filoane.
veinBrecciaStockwork | filoane, brecie și ștockwerk | Este un grup sistematic, cu o ocurență specială a zăcămintelor de minerale într-un volum finit de rocă. Filon: Zăcăminte de umplere a fracturilor cu o suprafață laterală și/sau o adâncime mare, dar care sunt de obicei foarte înguste. Brecie: O fisură care conține fragmente de roci de fundament, cu zăcăminte de minerale în interstiții. Ștockwerk: un sistem complex de filoane controlate structural și orientate aleatoriu.
manto | manto | Zăcăminte de minereuri de tip manto sunt definite printr-un control stratigrafic strict al distribuției lor, în general în cadrul unei formațiuni poroase în interiorul unui sit cu rol de capcană structurală. Se consideră că sursa de minereu din zăcămintele de manto este una interformațională, că ea provine dintr-o sursă sedimentară din cadrul unui bazin sedimentar adiacent sau din fluide mineralizatoare provenite din roci intruzive.
skarn | skarn | Zăcăminte de minerale formate prin înlocuirea calcarului cu resurse minerale și silicați calcici, de obicei adiacente unei roci intruzive felsice sau granitice.
porphyry | porfir | Zăcămintele de porfir sunt zăcăminte de minerale legate de intruziune, de mare tonaj și de concentrație mică cu acumulări de metale care pot include toate sau unele dintre următoarele metale: cupru, molibden, aur și argint. Geneza acestor zăcăminte este legată de amplasarea de intruziuni de la intermediare la felsice, hipabisale și în general porfirice, formate în mod obișnuit la limitele convergente ale plăcilor litosferice.
ultramaficOrMafic | ultrabazic/bazic | Zăcăminte de minerale legate de plutonism bazic și ultrabazic și care provin în urma unor procese magmatice precum cristalizarea fracțională. Principalele tipuri de zăcăminte sunt cromita și platinoidele în peridotite ofiolitice, titan în anortozite, nichel, cupru și platinoide în complexe ultrabazice.
carbonatite | carbonatite | Carbonatitele sunt roci eruptive intruzive în mineral carbonat, multe dintre ele conținând abundențe distincte de apatit, magnetit, barită și fluorit, care pot conține concentrații economice sau anormale de elemente rare, fosfor, niobiu, uraniu, toriu, cupru, fier, titan, bariu, fluorină, zirconiu și alte elemente rare sau incompatibile. Acestea pot, de asemenea, constitui surse din mică sau de vermiculit. Carbonatitele pot forma coloane centrale în cadrul unor complexe intruzive alcaline zonate sau pot apărea sub formă de dyke-uri, filoane-strat, brecie și filoane.
pegmatite | pegmatit | Pegmatitele tind să apară, în majoritatea cazurilor, în aureole de granituri și au, de obicei, un caracter granitic, adesea în concordanță cu compozițiile graniturile învecinate. Pegmatitele ar trebui, prin urmare, să reprezinte material granitic de exsoluție care cristalizează în rocile de fundament. Cu toate acestea, se are în vedere și o origine a fluidelor de pegmatite prin devolatilizarea (deshidratarea) rocilor metamorfice. Pegmatitele sunt roci cu granulație mare, compuse în principal din cuarț, feldspat și mică și sunt importante, deoarece ele conțin adesea minerale rare și pietre prețioase cum ar fi acvamarin, tourmalină, topaz, fluorină și corindon și adesea sunt însoțite, printre altele, de minerale de cositor și wolfram.
metamorphicHosted | îngropate în roci metamorfice | Zăcăminte de minerale asociate cu un metamorfism de adâncime (de peste 10 km), într-un context în care fluidele carbonice și apoase dau naștere la filoane aurifere.
gemsOrSemipreciousStones | pietre prețioase și semiprețioase | O bucată de mineral, care, după șlefuire și polizare, este utilizată pentru a fabrica bijuterii sau alte ornamente.
industrialRocks | roci industriale | Mineralele industriale sunt materiale geologice care sunt exploatate pentru valoarea lor comercială, sunt diferite de mineralele pentru combustibil și nu sunt surse de minereuri metalice. Acestea sunt utilizate în stare naturală sau după îmbogățire, fie ca materii prime, fie ca aditivi într-o gamă largă de aplicații.
20.3.3.9. Tipul de zăcământ de minerale (MineralDepositTypeValue)
Valori care indică stilul ocurenței sau al zăcământului.
Valorile permise pentru această listă de coduri cuprind orice valori definite de furnizorii de date.
Furnizorii de date pot utiliza valorile specificate în Ghidul tehnic INSPIRE privind resursele minerale.
20.3.3.10. Tipul de ocurență minerală (MineralOccurrenceTypeValue)
Tipul de ocurență minerală.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «MineralOccurrenceTypeValue»
Valoare | Nume | Definiție
mineralDeposit | zăcământ de minerale | O masă de materiale minerale prezente în stare naturală, de exemplu, minereuri metalice sau minerale nemetalice, de obicei cu valoare economică, fără a ține seama de tipul de origine. Acumulările de cărbune și petrol pot sau nu să fie incluse.
oreDeposit | zăcământ de minereuri | Material prezent în stare naturală din care se poate extrage un mineral sau mai multe minerale cu valoare economică, la un profit rezonabil.
occurrence | ocurență | Orice minereu sau mineral cu valoare economică, prezent în orice rocă de bază sau ca aluviuni.
prospect | zonă de prospectare | O zonă care reprezintă un sit potențial de zăcăminte minerale, bazată pe prospectări preliminare, prospectări anterioare. O anomalie geologică sau de geofizică, în special una recomandată pentru prospectare suplimentară.
province | provincie | Provincii geologice clasificate în funcție de resursele minerale.
district | district | Districte geologice clasificate în funcție de resursele minerale.
field | câmp | O regiune sau o zonă care deține sau este caracterizată de o anumită resursă minerală.
lode | filon | Un zăcământ de minerale constând dintr-o zonă de filoane, filoane subțiri deviate din altele mai groase, diseminări sau brecii plane.
20.3.3.11. Tipul de activitate minieră (MiningActivityTypeValue)
Tipul de activitate minieră, de activitate de prelucrare sau de producție.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «MiningActivityTypeValue»
Valoare | Nume | Definiție
adit | galerie de acces | O trecere orizontală de la suprafață în mină.
alluvial | aluvial | Termen aplicabil unui placer format prin acțiunea apelor curgătoare, precum este cazul într-un canal de izvor sau într-un con aluvial; de asemenea, termenul se aplică și mineralului prețios, de exemplu aur sau diamant, asociate cu un placer aluvial.
decline | galerie înclinată | Pasaj sau galerie de acces înclinată, pentru a accesa o mină pornind de la suprafață.
diggings | săpături | Un termen utilizat în vestul SUA pentru a desemna excavările pentru exploatarea aurului sau a altor minerale prețioase situate pe o bară de roci sau în apele de mică adâncime ale unui curs de apă, și efectuate atunci când nivelul apei este scăzut.
dredging | dragaj | O formă de exploatare la suprafață în care utilajele de forat și instalația de prelucrare sunt situate pe o barjă sau pe un corp de navă.
multiple | multiplu | O activitate multiplă.
openPit | exploatare la suprafață | O exploatare sub cerul liber (cunoscută și sub denumirea de exploatare în carieră) pentru extracția de minereuri și/sau de substanțe metalice.
openPitAndUnderground | exploatare la suprafață și exploatare în subteran | Acoperă atât activitatea minieră desfășurată la suprafață, cât și cea desfășurată în subteran.
quarry | carieră | Exploatări la suprafață, de obicei pentru extracția de piatră.
reworking | prelucrare | Noi activități de minierit desfășurate în mine deja prospectate.
shaft | puț de mină | O lucrare de excavare verticală sau înclinată prin care se exploatează o mină.
sluicing | spălare a minereului | Concentrarea de minerale grele, de exemplu aur sau casiterit, prin spălarea materialului neconsolidat cu ajutorul unor jgheaburi (scoc) echipate cu lațuri care rețin mineralele mai grele pe fundul jgheabului.
solutionMining | extracție prin dizolvare | (a) Dizolvarea la fața locului a componentelor minerale solubile în apă ale unui zăcământ de minereuri, prin permiterea ca o soluție de lixiviere, de obicei apoasă, să se scurgă prin minereul fracturat în galeriile de colectare de adâncime; (b) extracția de material de rocă solubil, de obicei sare, din zăcăminte subterane, prin pomparea de apă în puțuri conectate la zăcământ și îndepărtarea saramurii artificiale astfel create.
surfaceMining | minerit de suprafață | Categorie largă de minerit în care de solul și roca de deasupra zăcământului de minerale (strat de copertă) sunt eliminate.
surfaceMiningAndUnderground | minerit de suprafață și minerit subteran | Vizează atât exploatarea minieră de suprafață, cât și cea subterană.
underground | subteran | O excavare subterană pentru extracția de zăcăminte de minerale, deosebită de excavațiile de suprafață.
20.3.3.12. Tipul activității de prelucrare (ProcessingActivityTypeValue)
Valori care indică tipul de prelucrare efectuat în timpul unei activități miniere.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Furnizorii de date pot, de asemenea, să utilizeze valorile mai restrânse specificate pentru această listă de coduri în Ghidul tehnic INSPIRE privind resursele minerale.
Valori pentru lista de coduri «ProcessingActivityTypeValue»
Valoare | Nume | Definiție
physicalTreatment | tratare fizică | Proces de sortare care utilizează metodele de separare fizică.
physicalChemicalTreatment | tratare fizico-chimică | Proces de sortare care combină metode de separare fizice și chimice.
chemicalTreatment | tratare chimică | Proces de sortare care utilizează metode de separare chimică.
unknownTreatment | tratare necunoscută | Proces de sortare – tipul de tratare este necunoscut.
20.3.3.13. Categoria rezervei (ReserveCategoryValue)
Nivelul de încredere al estimării rezervei.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «ReserveCategoryValue»
Valoare | Nume | Definiție
provedOreReserves | rezerve de minereu dovedite | O «rezervă de minereu dovedită» reprezintă partea exploatabilă din punct de vedere economic a unei resurse minerale măsurate. Aceasta include materialele de diluare și garanțiile pentru pierderi, care pot apărea odată cu exploatarea materialului.
probableOreReserves | rezerve de minereu de probabile | O «rezervă de minereu probabilă» reprezintă partea exploatabilă din punct de vedere economic a unei rezerve indicate și, în anumite cazuri, o resursă minerală măsurată. Aceasta include materialele de diluare și garanțiile pentru pierderi, care pot apărea odată cu exploatarea materialului.
provedAndProbableOreReserves | rezerve de minereu dovedite și probabile | Vizează atât rezervele de minereu dovedite, cât și rezervele de minereu probabile.
inaccessibleDocumentation | documentație inaccesibilă | Rezerve de minereu fără o documentație accesibilă.
20.3.3.14. Categoria resursei (ResourceCategoryValue)
Indiciu conform căruia resursa este măsurată, indicată sau dedusă.
Valorile permise pentru această listă de coduri cuprind valorile din tabelul de mai jos și valorile suplimentare de la orice nivel definite de furnizorii de date.
Valori pentru lista de coduri «ResourceCategoryValue»
Valoare | Nume | Definiție
measuredMineralResource | resursă minerală măsurată | Parte a unei resurse minerale ale cărei tonaj, densități, formă, caracteristici fizice, concentrație și conținut mineral pot fi estimate cu un nivel ridicat de încredere.
indicatedMineralResource | resursă minerală indicată | Parte a unei resurse minerale ale cărei tonaj, densități, formă, caracteristici fizice, concentrație și conținut mineral pot fi estimate cu un nivel de încredere rezonabil.
inferredMineralResource | resursă minerală dedusă | Parte a unei resurse minerale al cărei tonaj, concentrație și conținut mineral pot fi estimate cu un nivel scăzut de încredere. Resursa minerală este dedusă din indicații geologice și dintr-o continuitate a geologiei și/sau a concentrației presupuse, dar neverificate.
measuredAndIndicatedMineralResource | resursă minerală măsurată și indicată | O combinație de resurse minerale măsurate și de resurse minerale indicate.
measuredIndicatedAndInferredMineralResource | resursă minerală măsurată, indicată și dedusă | O combinație resurse minerale măsurate, resurse minerale indicate și resurse minerale deduse.
indicatedAndInferredMineralResource | resursă minerală indicată și dedusă | O combinație de resurse minerale indicate și de resurse minerale deduse.
poorlyDocumented | slab documentată | Resursă minerală slab estimată și documentată.
20.4. Cerințe specifice categoriei
Tipul «MappedFeature» specificat în secțiunea 4.2.1.10 din anexa III trebuie utilizat pentru a descrie proprietățile geometrice ale obiectelor spațiale «MineralOccurrence».
20.5. Straturi
Straturi pentru categoria de date spațiale «Resurse minerale»
Numele stratului | Titlul stratului | Tip de obiect spațial
MR.Mine | Mine | MiningFeatureOccurrence
MR.MineralOccurrence | Ocurențe minerale | «MappedFeature» (obiecte spațiale ale căror proprietate de specificare este de tipul «MineralOccurrence»)”
(1) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(2) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(3) JO L 154, 21.06.2003, p. 1.
(4) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(5) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(6) JO L 321, 1.12.2008, p. 1.
(7) JO L 312, 22.11.2008, p. 3.
(8) JO L 327, 22.12.2000, p. 1.
(9) JO L 288, 6.11.2007, p. 27.
(10) JO L 135, 30.5.1991, p. 40.
(11) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(12) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(13) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(14) JO L 164, 25.6.2008, p. 19.
(15) Un strat va fi pus la dispoziție pentru fiecare valoare din lista de coduri, în conformitate cu articolul 14 alineatul (3).
(16) JO L 140, 5.6.2009, p. 16.
