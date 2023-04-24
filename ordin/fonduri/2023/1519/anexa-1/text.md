# Anexa nr. 1
PROCEDURĂ DE LUCRU privind acordarea suportului de nivel 1, 2 și 3 către utilizatorii sistemului informatic MySMIS2021/SMIS2021+
Prezentarea generală a scopului procedurii
Scopul procedurii este acela de a stabili modul de acțiune al personalului desemnat să își desfășoare activitatea în centrul de suport beneficiari pentru preluarea solicitărilor transmise de către reprezentanții Ministerului Investițiilor și Proiectelor Europene (MIPE) privind disfuncționalități ale sistemului informatic MySMIS2021/SMIS2021+, dar și al personalului dedicat din cadrul MIPE care oferă suport utilizatorilor aplicației.
Suportul operațional implică preluarea petițiilor și întrebărilor de la aplicanți; suportul operațional se realizează prin serviciul helpdesk de către personalul MIPE dedicat gestionării acestora și responsabil cu asigurarea suportului operațional de nivel 1 și 2.
În cazul în care personalul MIPE care gestionează helpdeskul și asigură suportul operațional de nivel 1 și 2, în urma informațiilor de la solicitant și a consultării manualelor de utilizare, constată că este o problemă de natură tehnică, va solicita datele de identificare ale solicitantului și ale organizației care a întâmpinat probleme în utilizarea aplicației, precum și toate detaliile legate de situația expusă, în vederea realizării tichetului corespunzător în aplicația JIRA.
Obiectiv
Această procedură urmărește: a) stabilirea unor norme interne privind primirea și soluționarea solicitărilor, pe linia suportului de operare în cadrul aplicației;
b) stabilirea modului în care solicitările vor fi soluționate.
Documente de referință
Manual de utilizare
1.
Definiții și abrevieri ale termenilor utilizați în procedură
Nr. crt.
Abrevierea Termenul abreviat
1. JIRA
Aplicație pentru înregistrarea, vizualizarea și gestionarea solicitărilor primite în helpdesk MIPE
2. Status
Starea în care se află o solicitare la un anumit moment
3. Apelant Reprezentantul MIPE/helpdesk MIPE
4. Task (sarcină) Solicitare care trebuie soluționată
5. Subtask (sarcină în legătură cu taskul din care face parte) Solicitare care trebuie soluționată, având legătură cu taskul din care face parte
6. Solicitant Utilizator care anunță centrul helpdesk MIPE că a întâmpinat o problemă în aplicație
7. Bug Defect, disfuncționalitate raportată a sistemului informatic
2.
Înregistrarea solicitărilor (1)
Pentru înregistrarea solicitării apelantului, reprezentantul MIPE cu acces în JIRA trebuie să primească un minimum de informații: a) numele și prenumele persoanei;
b) centrul din care face parte apelantul (centru helpdesk MIPE);
c) numele și prenumele solicitantului (eventual, entitatea pe care o reprezintă);
d) o descriere a problemei întâmpinate, necesară completării tichetului din JIRA, conform indicațiilor de mai jos.
(2)
Reprezentantul MIPE cu acces în JIRA are următoarele obligații: a) să solicite toate datele necesare creării taskului în JIRA;
b) să revină la apelant cu un apel telefonic în situația în care dezvoltatorul sau analistul de business solicită date suplimentare;
c) să înregistreze solicitarea în JIRA, menționând toate datele necesare pentru identificarea problemei sesizate.
(3)
Dacă se constată existența unei cazuistici recurente pe care se identifică mai multe spețe, se va înregistra un task specific în JIRA, iar toate spețele similare se vor înregistra ca subtaskuri individualizate în cadrul taskului cu respectiva specificitate.
(4)
Pașii pentru crearea tichetului în JIRA sunt: a) se va accesa butonul „Create”, după care se va deschide automat tabul „Create Issue”;
b) se va selecta proiectul;
c) la „Issue Type” se va selecta, conform specificului problemei, opțiunea: „Bug” (bug = o problemă care afectează sau împiedică funcționarea produsului);
d) la „Summary” se va descrie pe scurt problema în cauză. La „Component/s” se va completa componenta, dacă este cazul;
e) la „Description” se vor completa toate detaliile aferente „bugului” semnalat. Se vor completa: - contul de pe care s-a semnalat bugul;
- linkul aplicației din momentul semnalării bugului;
- screenshoturi cât mai clare (fullscreen, inclusiv data și ora de pe ecran), care să cuprindă cât mai multe detalii aferente bugului;
- fluxul parcurs în situația specifică, precizând pasul la care a apărut comportamentul nedorit, precum și descrierea cât mai precisă a acestui comportament (de exemplu, mesajul exact returnat, timpul de așteptare etc.);
f)
„Priority” se referă la nivelul de prioritate care indică importanța problemei. Prioritățile definite în prezent sunt enumerate mai jos: -
„Highest” - Această problemă va bloca progresul. Este vorba despre o eroare blocantă;
-
„High” - există o probabilitate mare ca această problemă să blocheze progresul;
-
„Medium” - problema detectată are potențialul de a bloca progresul;
-
„Low” - problemă minoră sau ușor de rezolvat;
-
„Lowest” - problemă banală cu impact redus sau fără impact asupra progresului;
-
„None” - nici n grad de prioritate.
g) la „Assignee” se va putea completa numele celui care va prelua acea solicitare, însă se recomandă completarea cu opțiunea default „Automatic”;
h) statusurile solicitărilor în JIRA se clasifică în următoarele categorii: -
„Done” - solicitarea a fost rezolvată;
-
„In progress” - solicitarea se află în lucru;
-
„No category” - încă nu a fost selectat un status pentru solicitare;
-
„To do” - de rezolvat solicitarea;
-
„Review” - tichetul a fost rezolvat și trebuie testat.
3.
Suport tehnic de nivel 3 Suportul tehnic de nivel 3 (disfuncționalități ale aplicației, rezolvarea problemelor tehnice apărute la echipamentele hardware, infrastructura de comunicații, sisteme de operare sau aplicații-suport - servere de aplicații, baze de date) va fi asigurat de către Serviciul de Telecomunicații Speciale (STS).
4.
Rezolvarea solicitărilor După ce echipa MIPE/STS dedicată proiectului rezolvă solicitarea, taskul din JIRA se va găsi în starea „de aprobat” (review/in review), iar echipele de testare ale STS și MIPE vor verifica rezolvarea sarcinii, urmând ca, în baza feedbackului rezultat, reprezentantul MIPE cu acces în JIRA să valideze soluționarea solicitării prin închiderea taskului sau retrimiterea acestuia în lucru dacă rezultatul nu este cel așteptat. Răspunsurile la solicitări și finalizarea bugurilor semnalate nu vor fi operaționalizate pe mediul de producție fără ca taskul din JIRA să fie închis de către reprezentanții MIPE.
