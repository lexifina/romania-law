# Anexa 1
Anexa nr. 1
la Metodologia privind evaluarea riscurilor pentru domeniul feroviar, transportului cu metroul, metroul ușor, monorai și transportului urban, suburban și regional pe șine, pe linii ferate industriale și pe căile ferate cu caracter de patrimoniu, de muzeu sau turistic.
Modalități posibile de calcul privind metodele cantitative
1.
Principiul de bază al Analizei probabilistice a riscurilor, denumită în continuare APR: a)
APR presupune evaluarea probabilității de apariție a unui pericol și a impactului acestuia asupra sistemului studiat.
b)
APR utilizează date istorice, modelele statistice și tehnici de simulare pentru a estima aceste probabilități și pentru a cuantifica riscurile.
c)
în general, APR include evaluarea probabilității de apariție a riscurilor și calcularea severității acestora, astfel încât să se poată estima risc global.
2.
Pașii de bază în APR: a)
identificarea evenimentelor de risc: primul pas este identificarea tuturor pericolelor care ar putea duce la un accident sau la o defecțiune în sistemul de transport sau în procesul analizat și aceste pericole pot fi directe sau indirecte.
b)
colectarea datelor statistice: se adună date istorice și statistice relevante despre frecvența și severitatea acestor pericole, astfel încât să se poată construi distribuții de probabilitate pentru fiecare tip de pericol.
c)
calcularea probabilităților: se calculează probabilitatea de apariție a fiecărui pericol și a combinațiilor de pericole care ar putea duce la un incident major.
d)
estimarea impactului: după estimarea probabilităților, se calculează și impactul fiecărui pericol, fie în termeni de daune materiale, numărul de victime sau alte efecte.
e)
calculul riscului: produsul dintre probabilități și consecințe, pentru a evalua riscul global se folosesc formule de calcul adecvate.
3.
Formule matematice în ARP: 3.1.
Pentru a evalua riscurile într-un domeniu complex, sunt folosite mai multe formule și concepte matematice.
3.2.
Cele mai importante sunt probabilitatea de apariție a unui pericol, severitatea impactului și riscul combinat.
3.3.
Probabilitatea unui pericol 3.3.1.
Probabilitatea unui pericol P reprezintă șansa ca un pericol să aibă loc, iar formula de bază este:
P(pericol) = Numărul de pericole / Numărul de pericole posibile
3.3.2.
În ARP, se colectează date istorice pentru a estima această probabilitate, iar pentru pericole complexe sau necunoscute, se pot utiliza distribuții de probabilitate.
3.4.
Probabilitatea unui sistem de pericole, cum ar fi evenimentele dependente și independente Pentru un sistem care implică mai multe evenimente, trebuie să se ia în considerare relația dintre ele, dacă sunt dependente sau independente, cum ar fi: a)
evenimente independente: i.
dacă evenimentele sunt independente, probabilitatea ca toate evenimentele să aibă loc este produsul probabilităților individuale.
ii.
de exemplu, pentru două evenimente independente E_1 și E_2:
P(E_1 ∩ E_2) = P (E_1) * P(E_2)
b)
evenimente dependente: i.
dacă evenimentele sunt dependente, trebuie să se țină cont de condiționarea între ele.
ii.
probabilitatea evenimentului E_1 dat că E_2 s-a produs este:
3.5.
Severitatea unui pericol 3.5.1.
Severitatea unui pericol S este o măsură a consecințelor acestuia.
3.5.2.
De exemplu, pentru un accident feroviar, severitatea poate fi măsurată în termeni de daune materiale sau număr de victime.
3.5.3.
Severitatea se poate exprima matematic ca o funcție a impactului și poate fi ajustată pe baza unui factor de risc.
3.6.
Calculul riscului global: Risc = Probabilitate x Impact 3.6.1.
Riscul global R este dat de produsul dintre probabilitatea pericolului și severitatea impactului acestuia, iar formula generală este:
R = P(E) * S
unde:
● P(E) este probabilitatea ca pericolului să se întâmple,
● S este severitatea sau impactul pericolului.
3.7.
Riscul combinat pentru mai multe pericole 3.7.1.
În practică, sistemele sunt adesea complexe, iar riscurile se pot combina.
3.7.2.
De exemplu, pentru două pericole independente care contribuie la un risc comun, riscul combinat R_c poate fi dat de suma riscurilor individuale:
R_c = R_1 + R_2 - P(E_1 ∩ E_2) * S_c
unde:
● R_1 și R_2 sunt riscurile individuale ale evenimentelor 1 și 2;
● P(E_1 ∩ E_2) este probabilitatea ca ambele evenimente să se întâmple simultan;
● S_c este severitatea combinată a evenimentelor.
3.8.
Analiza pericolelor rare (Pericolele cu probabilitate mică) 3.8.1.
Pentru pericole rare, se utilizează adesea distribuții de probabilitate cum ar fi distribuțiile Poisson sau Weibull pentru a estima probabilitatea acestor pericole.
3.8.2.
Distribuția Poisson pentru pericole rare are formula:
4.
Exemplu de aplicație ARP 4.1.
Să presupunem că vrem să evaluăm riscul unui accident pe o linie feroviară care implică două evenimente majore: a)
eveniment 1: Defecțiunea semnalizării, cu o probabilitate de 0.02 (2%) și o severitate de 10 milioane RON (costuri de reparare).
b)
eveniment 2: Condiții meteo extreme, cu o probabilitate de 0.05 (5%) și o severitate de 50 milioane RON.
4.2.
Riscul combinat poate fi calculat astfel: a)
riscul pentru fiecare eveniment:
● R_1 = P(E_1) * S_1 = 0.02 * 10,000,000 = 200,000 RON
● R_2 = P(E_2) * S_2 = 0.05 * 50,000,000 = 2,500,000 RON
b)
riscul combinat (presupunând că evenimentele sunt independente):
● R_c = R_1 + R_2 = 200,000 + 2,500,000 = 2,700,000 RON
5.
Evaluarea riscului pe baza analizei Monte Carlo: Metodă care folosește simulări statistice pentru a evalua riscurile și a estima variațiile. 5.1.
Definirea modelului de risc: În primul rând, trebuie să se definească un model matematic al procesului sau al sistemului de interes.
5.2.
De exemplu, dacă se analizează riscul unui accident feroviar, trebuie să se definească parametrii care pot influența acest risc, cum ar fi viteza trenului, condițiile meteo, întreținerea echipamentelor și altele.
5.3.
Definirea distribuțiilor de probabilitate pentru variabilele de intrare: Fiecare parametru din model este considerat o variabilă aleatorie. Aceste variabile sunt asociate cu o distribuție de probabilitate, care reprezintă incertitudinea legată de fiecare factor. De exemplu: a)
viteza trenului ar putea avea o distribuție Gauss, cu o valoare medie și o deviație standard;
b)
condițiile meteo ar putea fi modelate cu o distribuție uniformă sau o distribuție Beta.
5.4.
Simularea scenariilor multiple: se generează un număr mare de scenarii de risc, fiecare având valori aleatorii extrase din distribuțiile de probabilitate stabilite pentru fiecare variabilă de intrare.
5.5.
Evaluarea rezultatelor pentru fiecare simulare: după generarea scenariilor, se calculează rezultatele, de exemplu probabilitatea unui accident feroviar, pentru fiecare simulare.
5.6.
Analiza rezultatelor: după ce au fost obținute un număr mare de simulări, rezultatele sunt analizate statistic pentru a înțelege variabilitatea și incertitudinea, de exemplu, se poate calcula media și dispersia rezultatelor, se pot determina intervalele de încredere pentru estimarea riscurilor și se pot identifica cele mai probabile scenarii.
6.
În analiza Monte Carlo, utilizarea unor formule matematice de bază este esențială pentru simularea scenariilor și evaluarea rezultatelor. 6.1.
În continuare se prezintă posibile elemente matematice: 6.1.1.
Simularea variabilelor aleatorii 6.1.1.1.
Fiecare variabilă aleatorie X_i poate fi modelată cu o distribuție de probabilitate specifică. De exemplu, dacă X_i urmează o distribuție normală cu medie σ și deviație standard o formula de simulare este:
X_i aproximativ N(μ, σ^2)
6.1.1.2.
Aceasta înseamnă că variabila aleatorie X_i are o valoare extrasă dintr-o distribuție normală cu medie μ și varianță σ^2.
6.2.
Calculul riscurilor pe baza simulărilor 6.2.1.
După ce au fost generate simulările pentru fiecare variabilă aleatorie, trebuie calculat rezultatul riscului.
6.2.2.
Să presupunem că rezultatul R depinde de o combinație liniară a variabilelor X_1,X_2,...,X_n, iar relația este dată de formula:
R = f(X_1, X_2,...,X_n)
6.2.3.
Aici, f() este o funcție care poate reprezenta un model de risc, cum ar fi riscul de accident feroviar în funcție de viteză, condiții meteo și întreținere.
6.3.
Calculul mediei și dispersiei
După generarea unui număr mare de simulări, trebuie să calculăm media și dispersia pentru a obține o estimare a riscurilor și incertitudinilor. a)
media rezultatelor:
unde R_i este rezultatul simulării pentru scenariul i, iar N este numărul total de simulări realizate.
b)
dispersia (sau varianța):
unde μ_R este media rezultatelor obținute, iar R_i sunt rezultatele individuale ale simulărilor.
6.4.
Estimarea intervalelor de încredere 6.4.1.
Pentru a evalua incertitudinea asociată cu rezultatul riscului, putem utiliza intervale de încredere.
6.4.2.
De exemplu, pentru un interval de încredere de 95%, formula pentru intervalul de încredere este:
6.5.
Exemplu de aplicație în domeniul feroviar
Să presupunem că vrem să estimăm probabilitatea unui accident feroviar într-un anumit interval de timp, având în vedere variabile precum: a)
viteza trenurilor, care urmează o distribuție normală cu o medie de 100 km/h și o deviație standard de 10 km/h;
b)
condițiile meteo, care urmează o distribuție uniformă între 0 și 1, reprezentând diverse condiții de siguranță;
c)
starea infrastructurii, care urmează o distribuție Beta, reflectând probabilitatea de defecțiuni.
7.
Analiza de Fiabilitate: măsoară probabilitatea ca sistemul să funcționeze fără defecțiuni într-un anumit interval de timp. 7.1.
Definiția Fiabilității
Fiabilitatea R(t) este definită ca probabilitatea ca un sistem sau o componentă să funcționeze fără defecțiuni într-un interval de timp t, având în vedere condițiile de operare.
R(t) = P(T &gt; t)
unde:
● R(t)) este fiabilitatea la timpul t,
● P(T&gt;t) este probabilitatea ca timpul până la defecțiune T să fie mai mare decât t, adică sistemul să funcționeze corect până la timpul t.
7.2.
Funcția de Distribuție a timpului până la defecțiune 7.2.1.
Pentru a evalua fiabilitatea, este important să înțelegem distribuția timpului până la defecțiune al unui sistem sau echipament. Timpul până la defecțiune, notat cu T, poate fi modelat prin diferite distribuții de probabilitate, cum ar fi distribuția Exponențială, Weibull, Log-Normal, etc.
7.2.2.
Funcția de Distribuție Cumulativă (CDF) - Funcția de distribuție cumulativă F(t) exprimă probabilitatea ca un sistem să se defecteze până la momentul t:
F(t) = P(T ≤ t)
7.2.3.
Prin urmare, fiabilitatea R(t) este complementul funcției de distribuție cumulativă:
R(t) = 1 - F(t)
7.2.4.
Exemplu: distribuția exponențială - o distribuție foarte utilizată în analiza fiabilității este distribuția exponențială, care este folosită pentru a modela timpul până la defecțiune în condiții de rata constantă de defecțiune.
7.2.5.
Funcția de densitate de probabilitate f(t) a distribuției exponențiale este dată de:
unde:
● lamda este rata de defecțiune, numărul de defecțiuni pe unitatea de timp,
● t este timpul.
7.2.6.
Funcția de distribuție cumulativă F(t) pentru distribuția exponențială este:
F(t) = 1 - e^(-lambda t)
și fiabilitatea este:
R(t) = 1 - F(t) = e^(-lambda t)
7.2.7.
Aceasta înseamnă că probabilitatea ca un sistem să funcționeze fără defecțiuni până la timpul t este dată de e^(lambda t).
7.3.
Funcția de fiabilitate pentru distribuția Weibull 7.3.1.
Distribuția Weibull este frecvent folosită în analiza fiabilității pentru a modela timpul până la defecțiune, deoarece poate descrie atât sisteme cu defecte care apar rapid, fail-fast, cât și sisteme care funcționează mult timp fără probleme.
7.3.2.
Funcția de fiabilitate pentru distribuția Weibull este dată de:
unde:
● eta este scalarea sau parametru de viață caracteristic al sistemului;
● β este forma distribuției Weibull, care determină comportamentul sistemului, pentru β = 1, distribuția devine exponențială, iar pentru β &gt; 1, rata de defecțiune crește în timp.
7.3.3.
Exemple de interpretare a valorii lui β:
● β = 1: Rata de defecțiune este constantă în timp, comportament exponențial;
● β &gt; 1: Rata de defecțiune crește în timp, defecțiuni pe măsură ce echipamentele se uzează;
● β &lt; 1: Rata de defecțiune scade în timp, defecțiuni rare în faza inițială de utilizare.
7.4.
Calculul fiabilității într-un sistem complex 7.4.1.
Pentru sisteme mai complexe, care sunt formate din mai multe componente, fiabilitatea totală R_tot a sistemului depinde de modul în care sunt conectate aceste componente, în serie sau în paralel.
7.4.2.
Sistem în serie - pentru un sistem în serie, fiabilitatea totală este produsul fiabilităților componentelor individuale.
7.4.3.
Dacă un sistem are n componente, iar fiabilitatea fiecărei componente i este Ri(t), atunci fiabilitatea totală a sistemului este:
7.4.4.
Acesta este cazul în care defectarea oricărei componente duce la defectarea întregului sistem.
7.4.5.
Sistem în paralel - pentru un sistem în paralel, fiabilitatea totală este mai mare, deoarece sistemul continuă să funcționeze atâta timp cât cel puțin o componentă este în stare de funcționare.
7.4.6.
Fiabilitatea unui sistem în paralel este dată de:
8.
Funcția de timp mediu între defecțiuni 8.1.
Un alt concept important în analiza fiabilității este timpul mediu între defecțiuni - MTBF.
8.2.
Aceasta este o măsură a fiabilității pentru un sistem sau echipament și reprezintă media timpului dintre defecțiuni.
8.3.
Dacă sistemul urmează o distribuție exponențială, MTBF este dat de:
MTBF = 1/lambda
unde lambda este rata de defecțiune.
