# Anexa 4
Anexa nr. 4
la Metodologia privind evaluarea riscurilor pentru domeniul feroviar, transportului cu metroul, metroul ușor, monorai și transportului urban, suburban și regional pe șine, pe linii ferate industriale și pe căile ferate cu caracter de patrimoniu, de muzeu sau turistic.
Metodele bazate pe simulare
1.
Simularea Monte Carlo 1.1.
Simularea Monte Carlo este o tehnică probabilistică utilizată pentru a modela incertitudinea în procese și pentru a estima probabilitatea unor rezultate variate.
1.2.
Aceasta simulare implică generarea unui număr mare de scenarii, folosind valori aleatorii pentru variabilele de intrare.
1.3.
Pași în simularea Monte Carlo: a)
identificarea variabilelor de risc presupune selectarea variabilelor cheie care pot influența rezultatele;
b)
atribuirea distribuțiilor de probabilitate presupune că fiecare variabilă este modelată cu o distribuție statistică normală, uniformă, triangulară sau altă variantă, în funcție de comportamentul analizat;
c)
generarea scenariilor presupunerea generarea unor valori aleatorii pentru fiecare variabilă în baza distribuțiilor lor și se rulează simularea de mai multe ori;
d)
calcularea rezultatelor presupune determinarea valorilor de ieșire pentru fiecare scenariu.
1.4.
Rezultatul final R într-o simulare Monte Carlo este adesea calculat ca medie a tuturor scenariilor simulate, iar formula de baza este:
unde:
● N este numărul de simulări (iterații),
● Ri este rezultatul obținut la fiecare simulare individuală.
2.
Modelarea Stochastică 2.1.
Modelarea Stochastică este folosită pentru a simula procese aleatorii și variabile care variază în timp.
2.2.
Aceasta permite evaluarea probabilistică a performanței și riscurilor în procese complexe, cum ar fi defecțiunile sistemelor sau comportamentul utilizatorilor.
2.3.
Exemple și formule comune a)
Procesul Poisson: Utilizat pentru a modela evenimente rare, cum ar fi defecțiunile unui sistem, pe o perioadă de timp.
P(X = k) = (lambda^k e^-lambda)/k!
unde:
● P(X=k) este probabilitatea de apariție a k evenimente într-un interval de timp,
● lambda este rata medie de apariție a evenimentelor.
b)
Distribuția exponențială: utilizată pentru a modela timpul între evenimente în procese Poisson.
f(t) = lambda e^(-lambda t)
unde:
● f(t) este funcția de densitate de probabilitate pentru timpul t între evenimente,
● lambda este rata de apariție a evenimentelor.
3.
Discrete Event Simulation - DES 3.1.
DES modelează sistemele printr-o serie de evenimente care se desfășoară în ordine cronologică.
3.2.
Fiecare eveniment reprezintă o schimbare în starea sistemului și este utilizat pentru a analiza fluxul de trafic, întreținerea echipamentelor și alte procese complexe în sectorul feroviar și de transport.
3.3.
Pași principali: a)
definirea evenimentelor presupune identificarea schimbărilor de stare relevante, de ex. sosirea unui tren sau o defecțiune a echipamentului;
b)
stabilirea regulilor de tranziție presupune definirea condițiilor în care fiecare eveniment are loc;
c)
calculul rezultatelor presupune determinarea timpilor și resurselor implicate la fiecare tranziție.
4.
Analiza de scenarii 4.1.
Această metodă implică construirea mai multor scenarii ipotetice, de ex. scenariu optimist, pesimist sau realist și evaluarea riscurilor asociate fiecăruia.
4.2.
Formulă de bază pentru calculul rezultatului mediu al scenariilor
R_mediu = (R_optimist + R_pesimist + R_realist)/3
unde:
● R_optimist, R_pesimist, R_realist sunt rezultatele calculate pentru fiecare scenariu.
4.3.
Prin aceste metode, simulările oferă o perspectivă probabilistică asupra riscurilor și performanței sistemului, ajutând la fundamentarea deciziilor de management în funcție de variabilele și condițiile schimbătoare ale sistemului.
