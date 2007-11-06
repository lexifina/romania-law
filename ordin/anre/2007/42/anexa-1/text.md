# Anexa 1
Anexa 1
PROCEDURA OPERAȚIONALĂ "Mecanismul de compensare a efectelor utilizării rețelelor electrice de transport pentru tranzite de energie electrică între operatorii de transport și de sistem" 1. Introducere Pe baza acordurilor încheiate la întâlnirea Comitetului director de la Viena la 15 decembrie 2006 și de la Ljubjiana la 16 martie 2007, ETSO*1 a propus mecanismul descris mai jos pentru compensarea efectelor utilizării rețelelor electrice de transport pentru tranzite de energie electrică între operatorii de transport și de sistem, denumit în continuare Mecanismul interimar ITC*2. Acest nou mecanism este o îmbunătățire a actualului mecanism CBT*3, ca o etapă către viitorul mecanism ITC. ___________ *1 ETSO - European Transmission System Operators (TSO). *2 ITC - Inter TSO Compensation. *3 CBT - Cross Border Trade. Lista țărilor care au semnat Contractul ITC interimar de decontare și clearing (Contract ITC) este prezentată la pct. 4. 2. Principiile Mecanismului interimar ITC Pentru definirea mecanismului interimar ITC, s-au urmărit 4 componente: 2.1. compensarea costurilor cu infrastructura; 2.2. compensarea costurilor cu consumul propriu tehnologic în rețeaua electrică de transport; 2.3. finanțarea fondului de compensare; 2.4. decontarea diferențelor dintre obligațiile de plată și drepturile de încasat. 2.1. Compensarea costurilor cu infrastructura Sistemul de compensare pentru costurile cu infrastructura urmărește: * măsura în care rețeaua electrică de transport a unei țări (parte ITC) semnatare a Contractului ITC este folosită de către terțe părți care fac schimburi transfrontaliere de energie electrică între ele; * repartizarea corespunzătoare a costurilor rețelei unei părți ITC, datorate de celelalte părți. În cadrul sistemului de compensare pentru costurile de infrastructură se calculează: * compensările pe clase de active; * factorii de senzitivitate și schimburile de referință pe baza unui set de regimuri care descriu funcționarea reală a rețelei electrice în orele stabilite. Definirea claselor de active Conform Mecanismului interimar ITC, se consideră 6 clase de active pentru descrierea rețelei electrice de transport a fiecărei țări (parte ITC) semnatare a Contractului ITC: * clasa A: linii de curent alternativ de peste 300 kV; * clasa B: linii de curent alternativ de la 220 kV la 300 kV; * clasa C: alte linii de curent alternativ; * clasa D: linii de curent continuu pentru orice tensiune; * clasa E: transformatoare de putere între activele din clasa B și clasa A; * clasa F: transformatoare de putere între activele din clasa C și clasa B și transformatoare de putere între activele din clasa A și clasa C. Fiecare parte ITC furnizează o repartizare a costurilor reglementate pentru infrastructura de rețea pe clasele de active definite mai sus. Alocarea costurilor stațiilor între linii și transformatoare poate să difere de la o parte ITC la alta. Această discrepanță este atenuată prin reducerea numărului de clase de active atunci când se efectuează calculul compensărilor. Ca urmare, costurile transformatoarelor (clasele de active E și F) sunt adunate la costurile clasei de active ce reprezintă nivelul lor secundar de tensiune (B și C) astfel încât calculul compensărilor să fie realizat luându-se în considerare numai 4 clase de active, astfel:
A* = A; B* = B+E; C*= C+F și D* = D.
Modelarea rețelei Regimurile de funcționare reală privind topologia rețelei, caracteristicile tehnice, distribuția consumurilor și a producției se consideră pentru un număr limitat de ore predefinite, deoarece colectarea unui set de informații complet care să descrie situațiile de funcționare reală în toate cele 8.760 de ore din an nu este posibilă. Fiecare oră h din an este simulată printr-un model similar unuia dintre regimurile de funcționare reală predefinite T. Pentru fiecare lună se utilizează 6 regimuri de funcționare reală la orele CET*4: 3,30 h, 11,30 h și 19,30 h din cea de-a treia miercuri și din duminica precedentă. _________ *4 CET - Central European Time. Formatul convenit pentru transmiterea regimurilor de funcționare reală este: * formatul UCTE pentru rețelele din țările UCTE; * formatul PSS/E 29 pentru rețelele din țările nordice (Nordel) și țările baltice. Calculul factorilor de senzitivitate absoluți Pentru fiecare regim de funcționare predefinit T, se calculează factorii de senzitivitate absoluți Tau^k(abs,ij)[T,k]: pentru fiecare clasă de active a oricărei părți ITC k prin simularea unui schimb de 100 MW între țara i și țara j, astfel: * în țara i se distribuie o putere generată de 100 MW în toate nodurile producătoare; * în țara j se distribuie un consum de 100 MW în toate nodurile consumatoare. Factorii de senzitivitate absoluți reprezintă produsul dintre: * lungimea elementului de rețea l; și * diferența, în valoare absolută, dintre fluxurile de putere P în regimul inițial și fluxurile de putere rezultate după simularea schimbului de 100 MW între țara i și țara j, corespunzătoare fiecărui element de rețea l.
│
│ Tau^k(abs,ij)[T,K] = │
f2Σ (│DeltaP(b)│ x l(b)) │/100MW
(1) │bȘțării k∩clasa active K
b │ └─
─┘
Factorii de senzitivitate absoluți se numesc și distanțe electrice. Distanța electrică d(ij)[T]/d(ij)[h] dintre țările i și j pentru regimul de funcționare predefinit T/ pentru fiecare oră pentru care s-a definit regimul de funcționare T este determinată prin însumarea factorilor de senzitivitate absoluți Tau^k(abs,ij)[T] corespunzători elementelor de rețea din toate țările k.
Tau^k(abs,ij)[T] = f2Σ Tau^k(abs,ij)[T,K]
(2) K
d(ij)[T] =
Σ Tau^k(abs,ij)[T]
(3)
și kȘPartiITC
d(ij)[h] = d(ij)[T]
(4)
unde: h = o oră în perioada similară regimului de funcționare predefinit T. Factorii de senzitivitate absoluți Tau^k(abs,ij)[T,] sunt considerați în calculul cheilor de tranzit reprezentând utilizarea relativă a clasei de active K (A, B, C, D) din țara k, respectiv a compensării datorate țării k de toate celelalte părți ITC. Calculul factorilor de senzitivitate neți Pentru fiecare regim de funcționare predefinit T se calculează factorii de senzitivitate neți pentru fiecare clasă de active k (A, B, C, D) a oricărei părți ITC k prin simularea unui schimb de 100 MW între țara i și țara j, în mod similar cu simularea considerată în determinarea factorilor de senzitivitate absoluți. Factorii de senzitivitate neți reprezintă produsul dintre: * lungimea elementului de rețea l; și * diferența dintre fluxurile de putere P în regimul inițial și fluxurile de putere rezultate după simularea schimbului de 100 MW între țara i și țara j.
│
│ Tau^k(net,ij)[T,K] = │
f2Σ (│DeltaP(b)│ x l(b)) │/100MW
(5) │bȘțării k∩clasa active K
b │ └─
─┘
Factorii de senzitivitate neți Tau^k(net,ij)[T,K] sunt considerați în calculul compensărilor datorate fiecărei părți ITC pentru fiecare clasă de active. Calculul schimburilor de referință Schimburile de referință se calculează între fiecare pereche de țări net exportatoare și net importatoare și constituie baza pentru calculul drepturilor de încasat (al compensărilor) pentru părțile ITC. Schimburile de referință X(ij)[h] pentru fiecare pereche constituită dintr-o țară net exportatoare i și o țară net importatoare j pentru orice oră h vor fi definite astfel încât: 1. pentru o țară net exportatoare i, suma schimburilor de referință dintre această țară i și toate țările net importatoare j este egală cu exportul său net la ora h:
f2Σ X(ij)[h] = export net al țării i (h)
(6)
2. pentru o țară net importatoare j, suma schimburilor de referință dintre toate țările net exportatoare i și această țară este egală cu importul său net la ora h:
f2Σ X(ij)[h] = import net al țării i (h)
(7)
3. schimburile de referință X(ij)[h] respectând ecuațiile (5) și (6) se determină astfel încât utilizarea rețelelor tranzitate să fie minimă, reprezentată prin minimizarea următoarei funcții-obiectiv:
min f2Σ(d(ij)[h])X(ij)[h]
(8)
unde d(ij)[h] este distanța electrică pentru un schimb de 100 MW între țările i și j pentru ora h. Calculul compensărilor Compensarea cuvenită fiecărei părți ITC k va reflecta utilizarea rețelei sale de către terțe părți, care fac schimburi de putere între ele în comparație cu utilizarea totală a acestei rețele. Calculul compensărilor ține seama de clasele de active definite. Calculul utilizării totale a rețelei fiecărei părți ITC Utilizarea totală a oricărei clase de active din țara K(A, B, C, D) din țara k este cantitatea cumulată lunar (Q)[MWh.km] pe toate elementele de rețea dintr-o clasă de active k. Cantitatea (Q) corespunzătoare unui element de rețea reprezintă produsul dintre: * lungimea acestui element de rețea l; și * fluxul de putere P prin elementul de rețea rezultat dintr-un calcul de regim permanent efectuat pe o bază de date (T) rezultată din agregarea regimurilor de funcționare predefinite T din toate țările. Cantitatea cumulată lunar (Q) pentru o țară k și o clasă de active k (A, B, C, D) este definită cu formula:
Q(k,K) - f2Σ n(h)[T] x Σ (│DeltaP(b)│ x l(b))
(9) T
bȘK
unde: nh(T) - este numărul de ore în perioada similară regimului de funcționare predefinit T. Calculul cheilor de tranzit Cheia de tranzit reprezintă utilizarea relativă a clasei de active k (A, B, C, D) din țara k de toate perechile de terțe părți care fac schimburi de energie între ele și este definită după cum urmează:
│ f2Σ
Σ X(ij)[h] x Tau^k(net,ij)[T(h),K] │ │ h i#k,j#k
│ cheie tranzit(k,K) = min │────────────────────────────────────── ;1│/100MW (10) │
Q(k,K)
│ └─
─┘
Calculul compensărilor Compensarea datorată țării k pentru fiecare clasă de active K* (A*, B*, C*, D*) este dată de formula următoare:
compensare(k,K*) = max[cheie tranzit(k,K) x ACC(k,K*);0] x 0,45
(11)
unde ACC(k,K*) este costul asociat clasei de active K*. Prin aplicarea funcției "max" rezultă că pentru nicio parte ITC nu va rezultă compensare negativă pentru infrastructură. Procentul de 45% reprezintă limitarea ce s-a convenit pentru fondul de compensare. Această procedură de limitare își propune să aducă nivelul fondului de compensare pentru costurile cu infrastructura la o sumă apropiată de nivelul convenit. Calculul fondului de compensare pentru infrastructură Fondul total de compensare pentru infrastructură este suma tuturor compensărilor pentru infrastructură corespunzătoare părților ITC și claselor de active definite. 2.2. Compensarea costurilor cu consumul propriu tehnologic în rețeaua electrică de transport (CPT) Metoda "cu și fără tranzite" (WWT - With and Without Transits) ia în considerare impactul tranzitelor asupra fiecărei părți ITC participante. Ea se bazează pe o comparație între fluxurile de rețea pentru două situații: situația înregistrată (conținând fluxurile reale) și situația de după înlăturarea tranzitelor. În metoda WWT, compensările și contribuțiile pentru CPT sunt calculate pe baza: "situațiilor înregistrate" descrise prin regimuri de funcționare, a costurilor ex-ante pentru pierderi și a fluxurilor programate dintre țările participante și țările perimetrice. Acestor rezultate nu li se va aplica nicio limitare. _ Compensarea lunară pentru pierderi datorată fiecărei părți ITC k pentru luna m este:
compensare(k,m) = DeltaP(pierdere_k)[k,m] x C(pierderi)[k]
(12)
Delta P(pierdere_k) = diferența între pierderile din rețea în situația reală din regimul de funcționare și în situația în care s-au eliminat tranzitele de putere prin țara k. C(pierderi) = costul energiei electrice achiziționate pentru acoperirea pierderilor din rețeaua electrică de transport (RET); Fondul de compensare lunară global pentru pierderi este egal cu suma compensărilor tuturor părților ITC k:
Fond(pierdere)[k,m] = f2Σ compensare(k,m)
(13) kȘpartiITC
2.3. Finanțarea fondului de compensare Contribuțiile operatorului de transport și de sistem la fondul de compensare sunt formate din două părți, în mod similar cu Mecanismul din 2006: * prima parte a fondului ia în considerare contribuția din partea țărilor perimetrice. Tariful de tranzit (euro/MWh) este determinat ex-ante, aplicat exporturilor (EPC) și importurilor (IPC) programate din țările perimetrice în/din țările participante la mecanismul de compensare; * a doua parte a fondului denumită partea de "flux net de energie electrică în direcția export/import" bazată pe un "tarif pentru fluxul net", care se aplică exporturilor și importurilor nete. Tariful pentru fluxurile nete se calculează lunar, astfel încât să fie asigurată acoperirea fondului de compensare. Fluxurile nete în direcția export (NEF) și fluxurile nete în direcția import (NIF) se calculează în mod similar celor din contractele CBT anterioare, incluzând regulile pentru țările "de margine". Tariful reglementat de tranzit, aplicat importurilor și exporturilor programate din țările perimetrice, reprezintă suma dintre tariful aplicat fluxului net pentru compensarea costurilor cu infrastructura [NFP(ea)I] și tariful aplicat fluxului net pentru compensarea costurilor cu pierderile [NFP(ea)L], determinate ex-ante (ea). Tariful aplicat fluxului net pentru compensarea costurilor cu infrastructura, determinat ex-ante, este dat de raportul dintre fondul total de compensare pentru infrastructură și suma fluxurilor considerate în calculul contribuției la fond:
Fond(ea)I NFP(ea)I = ──────────────────────────────────────────────────────
(14) _
_
_
_ f2Σ
_ Σ [NEF(k,m) + NIF(k,m) + EPC(k,m) + IPC(k,m)] kȘITC mȘ2005
Tariful aplicat fluxului net pentru compensarea costurilor cu pierderile, determinat ex-ante este dat de următorul raport:
Fond(ea)L NFP(ea)L = ──────────────────────────────────────────────────────
(15) _
_
_
_ f2Σ _ Σ [NEF(k,m) + NIF(k,m) + EPC(k,m) + IPC(k,m)] kȘIT mȘ2005
Pentru a asigura permanenta egalitate dintre contribuțiile la fond și compensările _ pentru infrastructură sau pierderi, lunar (m) se calculează tariful aplicat fluxului net _ pentru compensarea costurilor cu infrastructura NFP(ep)I(m) și compensarea costurilor cu _ pierderile NFP(ep)L(m), astfel:
Fond(ep)I(m) - f2Σ Ct^(I,PC)(ep)[k,m] _
kȘITC NFP(ep)I(m) = ─────────────────────────────────────── (16) f2Σ
Σ
_[NEF(k,m) + NIF(k,m)] kȘITC m=1..m
_
_ Fond(ep)L(m) - f2Σ Ct^(L,PC)(ep)[k,m] _
kȘITC NFP(ep)L(m) = ─────────────────────────────────────── (17) f2Σ
Σ
_[NEF(k,m) + NIF(k,m)] kȘITC m=1..m
_ Ct^(I,PC)(ep)[k,m] - contribuția la fond pentru compensarea costurilor cu infrastructura pentru importurile și exporturile programate din țările perimetrice; _ Ct^(I,PC)(ep)[k,m]- contribuția la fond pentru compensarea costurilor cu consumul propriu tehnologic în RET pentru importurile și exporturile programate din țările perimetrice. _ NOTĂ: La finele fiecărei luni (m) se recalculează tariful pentru fluxul net, cumulat _ într-un "interval extins" (m) care începe din luna (1) până în luna (m). 2.4. Decontarea diferențelor dintre obligațiile de plată și drepturile de încasat Procedura de decontare lunară _ În fiecare lună m sumele destinate obligațiilor de plată pentru orice parte ITC sunt determinate după calculul ex-post (ep) al compensărilor pentru infrastructură și pentru pierderi. _ Rezultatele finale nete [NR^0(ep)] datorate în luna m fiecărei părți ITC k sunt calculate ca diferența dintre suma drepturilor de încasat (a compensărilor costurilor) pentru infrastructură [CC(ep)I] și pierderi [CC(ep)L] și suma obligațiilor de plată (a contribuțiilor) pentru infrastructură [Ct(ep)I] și pierderi [Ct(ep)L].
NR^0(ep)(k,m)=(CC(ep)I[k,m] + CC(ep)L[k,m]) - (Ct(ep)I[k,m] + Ct(ep)L[k,m])(18)
Rezultatele finale nete lunare se vor calcula luându-se în considerare diferența dintre _ _ rezultatele finale ale lunii (m) și rezultatele finale ale lunii precedente (m - 1). Procedura de decontare finală Avându-se în vedere că tariful aplicat fluxului net se recalculează lunar pentru asigurarea egalității dintre contribuțiile la fond și compensațiile pentru infrastructură și pierderi, nu mai este necesară nicio altă procedură de decontare finală după încheierea decontărilor lunare. 3. Administratorul de date pentru mecanismul interimar ITC RWE Transportnetz Strom și Swissgrid AG (denumite împreună administrator de date) îndeplinesc sarcinile de administrare a datelor prevăzute în Contractul ITC. 4. Parametri geografici 4.1 Lista țărilor/blocurilor de control (codurile ISO din două litere) Albania (AL) Austria (AT) Bosnia și Herțegovina (BA) Belgia (BE) Bulgaria (BG) Elveția (CH) Germania (DE) Danemarca de Est (DKE) Danemarca de Vest (DKW) Estonia (EE) Spania (ES) Finlanda (FI) Franța (FR) Grecia (GR) Croația (HR) Ungaria (HU) Italia (IT) Muntenegru (ME) Fosta Republică Iugoslavă Macedonia (MK) Olanda (NL) Norvegia (NO) Polonia (PL) Portugalia (PT) România (RO) Serbia (RS) Suedia (SE) Slovenia (ȘI) 4.2 Lista țărilor perimetrice (codurile ISO din două litere) Bielorusia (BY) Republica Cehă (CZ) Marea Britanie (GB) Maroc (MA) Federația Rusă (RU) Ucraina (UA) Slovacia (SK) Letonia (LV) Irlanda (IR)
Anexa 2
RAPORTARE LUNARĂ a Companiei Naționale de Transport al Energiei Electrice "Transelectrica"- S.A. privind tranzitul de energie electrică prin Sistemul electroenergetic național
[MWh]
┌────┬────────────────────────────────┬──────────────────────────────────────┐ │
│
│
Ora
│ │Data│
├──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┤ │
│
│ 1│ 2│ 3│ 4│ .│ .│ .│ .│ .│21│22│23│24│ ├────┼────────────────────────────────┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤ │
│Fluxul de energie electrică
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │
│înregistrată în direcția import │ │ │ │ │ │ │ │ │ │ │ │ │ │ ├────┼────────────────────────────────┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤ │
│Fluxul de energie electrică
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │
│înregistrată în direcția export │ │ │ │ │ │ │ │ │ │ │ │ │ │ ├────┼────────────────────────────────┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤ │
│Energia electrică din/spre
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │
│țările perimetrice prin Sistemul│ │ │ │ │ │ │ │ │ │ │ │ │ │ │
│electroenergetic național
│ │ │ │ │ │ │ │ │ │ │ │ │ │ └────┴────────────────────────────────┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
----
