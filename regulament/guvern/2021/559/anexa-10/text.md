# Anexa 10
Anexa nr. 9
la regulament
CERINȚELE SPECIFICE
activităților de audit de securitate
Generalități
1.
Pe timpul desfășurării activităților de audit, desfășurate în baza contractului de audit, operatorul economic și auditorii de securitate cibernetică trebuie să respecte cerințele specifice stabilite în această anexă, respectiv de la [CAS1] la [CAS6].
2.
Activitățile tehnice descrise la [CAS1] până la [CAS4] nu exclud evaluarea securității organizației, respectiv securitatea logică și fizică a domeniului auditat. Această evaluare constă în verificarea faptului că politicile și procedurile de securitate definite pentru asigurarea cerințelor minime de securitate a rețelelor și sistemelor informatice auditate sunt conforme cu nivelul tehnicii.
3.
Activitățile tehnice de la [CAS6], auditul sistemelor de control industrial, presupun atingerea cerințelor specifice prin cerințele stabilite la [CAS1] până la [CAS5].
4.
Cerințele enunțate de la [CAS1] la [CAS5] sunt date cu titlu informativ și nu sunt exhaustive. În plus, acestea trebuie efectuate numai atunci când sunt aplicabile rețelelor și sistemelor informatice auditate.
[CAS1]. Cerințe specifice auditului arhitecturii
1.
Acțiuni ale OE Operatorul economic trebuie să furnizeze auditorului de securitate cibernetică elementele de arhitectură și configurare a rețelelor și sistemelor informatice auditate.
2.
Acțiuni tehnice ale ASI Auditorul de securitate cibernetică trebuie să revizuiască/ auditeze următoarele documente atunci când acestea există: – diagramele arhitecturale de nivel 2 și 3 corespunzătoare Modelului OSI (interconectarea sistemelor deschise/Open Systems Interconnection);
– matricea fluxurilor;
– regulile de filtrare;
– configurarea echipamentelor de rețea (routere și comutatoare);
– interconectări cu rețele terțe sau internet;
– analizele de risc ale rețelelor și sistemelor informatice;
– documentele de arhitectură tehnică legate de ținta auditului.
3.
Comunicarea dintre ASI și OE Auditorul de securitate cibernetică trebuie să poată organiza interviuri cu personalul implicat în stabilirea și administrarea rețelelor și sistemelor informatice auditate, în special în ceea ce privește procedurile de administrare.
[CAS2]. Cerințe specifice auditului de configurare
1.
Acțiuni ale OE Operatorul economic trebuie să furnizeze auditorului de securitate cibernetică elementele de configurare ale rețelelor și sistemelor informatice auditate. Elementele de configurare pot fi identificate manual sau automat, folosind „acces privilegiat“, sub formă de fișiere de configurare sau capturi de ecran.
Această acțiune poate fi întreprinsă direct de auditorul de securitate cibernetică după aprobarea operatorului economic supus auditului.
2.
Acțiuni tehnice ale ASI Auditorul de securitate cibernetică trebuie să verifice securitatea configurațiilor, în conformitate cu stadiul tehnicii, cerințele minime de asigurare a securității rețelelor și sistemelor informatice și regulile specifice ale OE, respectiv a: – echipamentelor de rețea cu fir sau fără fir (cum ar fi switchuri sau routere);
– echipamentelor de securitate (tip firewall sau releu invers, filtrare sau nu, și regulile lor de filtrare, criptare etc.);
– sistemelor de operare;
– sistemelor de gestionare a bazelor de date;
– serviciilor de infrastructură;
– serverelor de aplicații;
– stațiilor de lucru;
– echipamentelor de telefonie;
– mediilor de virtualizare.
3.
Comunicarea dintre ASI și OE Auditorul de securitate cibernetică trebuie să poată organiza interviuri cu personalul implicat în stabilirea și administrarea rețelelor și sistemelor informatice auditate, în special în ceea ce privește standardele de configurare.
[CAS3]. Cerințe specifice auditului codului sursă
1.
Acțiuni ale OE Operatorul economic trebuie să furnizeze auditorului de securitate cibernetică: codul sursă, documentația referitoare la implementare, metodele și rapoartele de testare și arhitectura rețelelor și sistemelor informatice auditate, precum și configurația elementelor de compilare și de execuție, în limitele drepturilor operatorului economic.
2.
Acțiuni tehnice ale ASI Auditorul de securitate cibernetică trebuie: – să verifice securitatea părților din codul sursă referitoare la: • mecanisme de autentificare;
• mecanisme criptografice;
• gestionarea utilizatorilor;
• controlul accesului la resurse;
• interacțiuni cu alte aplicații;
• relații cu sistemele de gestionare a bazelor de date;
• respectarea cerințelor de securitate referitoare la mediul în care este implementată aplicația;
– să verifice cele mai frecvente vulnerabilități în următoarele domenii: • scripturi între site-uri;
• injecții SQL;
• falsificare a cererilor între site-uri;
• erori logice ale aplicației;
• depășirea bufferului;
• executarea comenzilor arbitrare;
• includerea fișierelor (local sau la distanță);
– să respecte regulile specifice de audit, respectiv trebuie: • să efectueze o analiză de securitate a aplicației auditate pentru a limita auditul la părțile critice ale codului său;
• să prevină scurgerile de informații și modificări în funcționarea rețelelor și sistemelor informatice;
• să efectueze activitate manual sau automat folosind instrumente specializate. Fazele automatizate, precum și instrumentele utilizate trebuie identificate în livrabile și, în special, în raportul de audit.
3.
Comunicarea dintre ASI și OE Auditorul de securitate cibernetică va efectua interviuri cu unul dintre dezvoltatori/programatori sau persoana responsabilă de implementarea codului sursă auditat pentru a avea informații referitoare la contextul aplicației, nevoile de securitate și practicile de dezvoltare.
[CAS4]. Cerințe specifice auditului de penetrare (testarea de penetrare)
1.
Acțiuni ale OE Operatorul economic trebuie să aprobe activitatea.
2.
Acțiuni tehnice ale ASI Auditorul de securitate cibernetică trebuie: – să efectueze una sau mai multe dintre următoarele faze: • faza 1 - „Black box“ (cutie neagră). Auditorul nu are alte informații decât adresele IP și adresele URL asociate țintei auditate. Această fază este în general precedată de descoperirea informațiilor și identificarea țintei prin interogarea serviciilor DNS, scanarea porturilor deschise, descoperirea prezenței echipamentelor de filtrare etc.;
• faza 2 - „Gray box“ (cutie gri). Auditorul are cunoștință despre un utilizator standard al rețelelor și sistemelor informatice (autentificare legitimă, stație de lucru „standard“ etc.). Identificatorii pot aparține diferitelor profiluri de utilizator pentru a testa diferite niveluri de privilegii;
• faza 3 - „White box“ (cutie albă). Auditorul dispune de cât mai multe informații tehnice (arhitectură, cod sursă, contacte telefonice, identificatori etc.) înainte de a începe analiza. De asemenea, are acces la contacte tehnice legate de rețelele și sistemele informatice țintă.
În cazul în care sunt efectuate mai multe dintre faze, se recomandă păstrarea ordinii de execuție descrise mai sus;
– să definească un profil de atacator simulat;
– să exploateze vulnerabilitățile descoperite numai cu acordul operatorului economic, atunci când știe că rețelele și sistemele informatice auditate vor fi instabile sau chiar va fi provocat un refuz de serviciu;
– să indice și să justifice în raportul de audit absența oricărei încercări de exploatare a vulnerabilităților;
– să comunice ANSRSI vulnerabilitățile nonpublice descoperite în timpul auditului.
3.
Comunicarea dintre ASI și OE Auditorul de securitate cibernetică trebuie să aibă un contact permanent cu operatorul economic și să avertizeze/să informeze operatorul economic înainte de orice acțiune care ar putea duce la o defecțiune sau chiar la o refuzare a serviciului rețelelor și sistemelor informatice auditate.
[CAS5]. Cerințe specifice auditului securității organizației
1.
Acțiuni ale OE Operatorul economic trebuie să pună la dispoziția auditorului de securitate cibernetică toate documentele și înscrisurile necesare desfășurării activității de audit.
2.
Acțiuni tehnice ale ASI Auditorul de securitate cibernetică trebuie: – să analizeze organizarea securității rețelelor și sistemelor informatice pe baza standardelor tehnice și de reglementare stabilite în Lista standardelor și specificațiilor europene și internaționale (LSSEINIS), în conformitate cu cerințele minime de securitate aplicabile operatorilor de servicii esențiale, respectiv furnizorilor de servicii digitale;
– să respecte regulile specifice de audit, respectiv trebuie: • să permită măsurarea conformității rețelelor și sistemelor informatice auditate cu privire la parametrii de referință și identificarea abaterilor care prezintă vulnerabilități majore ale acestora;
• să integreze analiza elementelor legate de securitatea aspectelor fizice ale rețelelor și sistemelor informatice, în special protecția spațiilor care găzduiesc componente ale rețelelor și sistemelor informatice și a datelor/informațiilor auditate sau controlul acces la aceste componente.
3.
Comunicarea dintre ASI și OE Auditorul de securitate cibernetică trebuie să aibă un contact permanent cu operatorul economic, să poată avea discuții/ interviuri cu managerii de proces și responsabilii cu securitatea, inclusiv responsabilii NIS.
[CAS6]. Cerințe specifice auditului sistemelor de control industrial
1.
Acțiuni ale OE Operatorul economic trebuie să pună la dispoziția auditorului de securitate cibernetică documente și înscrisuri, precum și accesul la elementele/componentele care urmează a fi supuse auditului tehnic.
2.
Acțiuni tehnice ale ASI Auditorul de securitate cibernetică trebuie să desfășoare următoarele activități în cadrul sistemului de control industrial (ISC) și, după caz, al centrului său de control (SCADA): – audit arhitectură;
– audit de configurare;
– audit securitate logică și fizică.
3.
Comunicarea dintre ASI și OE Auditorul de securitate cibernetică trebuie: – să poată organiza interviuri cu personalul implicat în securitatea sistemului de control industrial, managerul operațional al sistemului și, după caz, administratorii tehnici;
– să informeze operatorul economic cu privire la riscurile efectuării testărilor de penetrare într-un mediu care cuprinde sisteme de control industrial.
