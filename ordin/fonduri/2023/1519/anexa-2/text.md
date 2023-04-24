# Anexa nr. 2
Activități de suport tehnic, acceptanță și timpi de răspuns așteptați
I.
Detalierea responsabililor de activități de suport a) suport bug-fixing: (i)
Ministerul Investițiilor și Proiectelor Europene (MIPE): înregistrează incidentele în JIRA;
(ii)
Serviciul de Telecomunicații Speciale (STS);
b) suport incidente aplicații, baze de date, platformă, networking: (i)
MIPE;
(ii)
STS.
II.
Canale de comunicare a) e-mail - mediu de comunicare oficial - pentru documente ce necesită validare formală;
b)
JIRA;
c)
Mattermost.
III.
Procedura de acceptanță Tipuri de acceptanță și conținutul fiecărei acceptanțe (documente care se semnează, cine semnează, momentul semnării); a) acceptanță instalare și configurare platformă MySMIS2021 (pentru fiecare mediu: test&preprod&prod) 1. arhitectura detaliată a fiecărui mediu - STS, după finalizarea instalării și configurării fiecărui mediu;
2. nume mașini & credențiale - STS, după finalizarea instalării și configurării fiecărui mediu;
3. manuale & instrucțiuni de administrare și utilizare - STS, după finalizarea instalării și configurării fiecărui mediu;
4. raport testare platformă funcțională - MIPE, după testarea fiecărui mediu;
b) acceptanță dezvoltare aplicație MySMIS2021 (pentru fiecare modul): 1. documentație cerințe și specificații funcționale - export taskuri din JIRA - STS, verificat de MIPE, semnat de echipele de analiză ale STS & MIPE după finalizarea ședințelor de grooming ale fiecărui modul;
2. acceptanță funcțională - plan de testare & raport de testare & document UAT - echipa de testare a MIPE - după finalizarea testării funcționale;
3. acceptanță de performanță - plan de testare & raport de testare - STS, după finalizarea testelor de performanță;
4. acceptanță de securitate - plan de testare & raport de testare - echipa de testare - STS, după finalizarea testelor de securitate;
c) modul de lucru
1. documentare cerințe funcționale: MIPE documentează cerințele funcționale în aplicația OpenProject;
2. design evenimente: -
STS, cu suport MIPE, realizează designul evenimentelor în Colaboard;
- echipele de analiză ale MIPE & STS semnează un document de analiză cu evenimentele modelate în Colaboard;
- după această etapă, STS poate estima efortul necesar dezvoltării; 3. documentare taskuri JIRA:
-
STS creează în JIRA taskurile de tip Epic & MIPE le completează;
-
STS creează în JIRA taskurile de tip Story & MIPE le completează; 4. grooming: DEV STS & analiști STS & analiști MIPE
- vor fi mai multe ședințe de grooming deoarece în fiecare ședință de grooming sunt discutate numai câteva taskuri;
- pentru fiecare modul, echipele de analiză ale MIPE & STS semnează un document unde sunt enumerate epic-urile și story-urile discutate la grooming și care intră în respectivul modul (doar enumerare taskuri de tip Epic și Story - descrierea rezultând pentru fiecare task din history JIRA); 5. review zilnic cerințe:
-
DEV solicită clarificări pentru cerințe neclare sau incomplete;
-
MIPE răspunde la solicitări;
-
MIPE definește UAC;
d) în implementarea proiectului folosim metodologia Agile Scrum 1. pentru o monitorizare a progresului se vor folosi sprinturi de maximum 2 săptămâni cu backlog active;
2. taskurile documentate în JIRA ar trebui să intre în sprinturi separate (să nu se mai aștepte 2-3-4 săptămâni până se finalizează groomingul pentru întregul modul);
3. taskurile și subtaskurile asociate story-urilor să fie asignate persoanelor care lucrează pe ele pentru a putea oricând identifica persoana responsabilă pe task pentru o comunicare directă (Mattermost, videoconferințe) și numai cu ele să se întâmple groomingul;
4. urmărire în timp real cât s-a implementat din estimatul de la 2 săptămâni, pentru a analiza dacă ne încadrăm în termenele stabilite prin Memorandum;
e) evenimente 1.
Planning confom Kanban;
2.
Backlog Refiniment;
3.
Retrospective.
IV.
Timpii de răspuns așteptați sunt următorii: a) pentru dezvoltare inițială - Tdev = 2-4 săptămâni;
b) pentru testare/QA - Tdev/4= 5-7 zile;
V.
Principalele activități desfășurate în cadrul configurării, administrării și operării rețelei de comunicații de tip VPN sunt următoarele: a) asigurarea conexiunilor securizate de tip IPSec VPN între entitățile care au nevoie de acces la resursele MySMIS și HUB MIPE;
b) configurarea politicilor de securitate pe echipamentele tip firewall pentru rețeaua VPN;
c) asigurarea rutării pentru accesul la resursele MySMIS;
d) actualizarea și optimizarea soluției în funcție de nevoile survenite;
e) suport tehnic pentru modificarea locațiilor de acces la rețeaua MySMIS;
f) monitorizarea echipamentelor instalate în rețeaua VPN MySMIS și remedierea incidentelor.
VI.
Activitățile desfășurate pentru asigurarea expunerii în rețeaua internet a serviciilor de interes prin configurarea echipamentelor centrale, de tip firewall/UTM și a switch-urilor de datacenter, se realizează astfel: a) configurarea vlan-urilor și porturilor de pe echipamentele de tip switch datacenter;
b) asigurarea posturii de securitate a rețelei prin configurarea echipamentelor de tip UTM;
c) configurarea politicilor de securitate pe echipamentele tip firewall pentru accesul la internet;
d) expunerea în rețeaua internet a serviciilor de interes;
e) monitorizarea echipamentelor în vederea identificării și remedierii prompte a incidentelor.
VII.
Pentru asigurarea atribuțiilor menționate la art. 3 lit. k) din ordin, STS desfășoară următoarele activități: a) asigurarea conexiunilor securizate între echipamentele din cadrul rețelei extranet;
b) asigurarea disponibilității accesului la serviciile expuse în rețeaua extranet printr-o infrastructură redundantă;
c) configurarea regulilor de acces în funcție de solicitări;
d) implementarea protocoalelor de rutare în vederea asigurării accesului la resursele expuse în rețeaua extranet.
VIII.
Pentru configurarea și administrarea tehnică a centrului de suport operat de către MIPE, STS desfășoară următoarele activități: a) instalează și configurează aplicația de call center;
b) configurează aplicația de call center pentru accesul utilizatorilor la cozi, în funcție de fluxurile de lucru;
c) instalează și configurează SIP Trunk pentru accesul la serviciul de tip call center;
d) realizează mesaje de tip IVR pentru serviciul de tip call center;
e) realizează și configurează programe de lucru pentru serviciul de tip call center;
f) configurează aplicația prin care se pot extrage date statistice privind activitatea din call center;
g) administrează și monitorizează echipamentele și aplicația care oferă serviciul de tip call center.
