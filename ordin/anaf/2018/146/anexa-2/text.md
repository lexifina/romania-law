# Anexa nr. 2
Structura XML a fișierelor prevăzute la art. 22 pct. J lit. b) din Normele metodologice pentru aplicarea
Ordonanței de urgență a Guvernului nr. 28/1999 privind obligația operatorilor economici de a utiliza aparate de marcat electronice fiscale, aprobate prin Hotărârea Guvernului nr. 479/2003, republicată, cu modificările și completările ulterioare, precum și structura XML a mesajelor de activare a profilurilor
Secțiunea I
1.
Structura XML a datelor prevăzute la art. 3 alin. (2) lit. a) din anexa nr. 11 la normele metodologice se regăsește la secțiunea II.1.
2.
Structura XML a datelor prevăzute la art. 3 alin. (2) lit. b) din anexa nr. 11 la normele metodologice se regăsește la secțiunea II.2.
3.
Structura XML a datelor prevăzute la art. 3 alin. (1) lit. a) din anexa nr. 11 la normele metodologice se regăsește la secțiunea II.3
4.
Structura XML a datelor prevăzute la art. 3 alin. (2) lit. c) din anexa nr. 11 la normele metodologice se regăsește la secțiunea II.4
5.
Structura XML a datelor prevăzute la art. 3 alin. (1) lit. b) din anexa nr. 11 la normele metodologice pentru: a) aparate de marcat electronice fiscale utilizate în activitatea de schimb valutar se regăsește la secțiunea II.5;
b) aparate de marcat electronice fiscale utilizate în activitatea de taximetrie se regăsește la secțiunea II.6;
c) aparate de marcat electronice fiscale, altele decât cele de la lit. a) și b), se regăsește la secțiunea II.7.
6.
Structura XML a informațiilor referitoare la pornirea/oprirea aparatului de marcat electronic fiscal, încetarea funcționării acestuia în urma unor evenimente de tipul lipsă curent electric sau întrerupere conexiune la internet, precum și cu privire la repunerea în funcțiune/reconectarea aparatului se regăsește la secțiunea II.8.
7.
Structura XML a datelor prevăzute la art. 3 alin. (1) lit. d) din anexa nr. 11 la normele metodologice se regăsește la secțiunea II.9.
8.
Structura XML a mesajului de activare a profilurilor conform art. 3 alin. (3) din anexa nr. 11 la normele metodologice se regăsește la secțiunea II.10.
9.
Structura XML a mesajului de trecere din profilul 1 în profilul 0 se regăsește la secțiunea II.11.
10.
Structura XML a mesajului registru ce conține numerele de ordine ale rapoartelor de închidere zilnică emise în perioada de raportare se regăsește la secțiunea II.12.
11.
Transmiterea fișierelor XML se face conform celor prevăzute în secțiunea II.13.
12.
Nomenclatoarele folosite în cadrul fișierelor XML se regăsesc în secțiunea II.14
Secțiunea II.1
Nr. crt.
Denumire secțiune/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj c(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: data și ora generării mesajului
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică <bonSV>
Secțiune repetitivă
Secțiunea va avea un număr de apariții egal cu numărul de bonuri tipărite. idB
Numărul de identificare al bonului fiscal
C(32)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRRBBBB
Primele 10 caractere = număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: data și ora emitere bonuri
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică din care face parte bonul fiscal
Următoarele 4 caractere: număr de ordine bon fiscal la nivelul zilei de lucru
Trebuie să fie unic pe aparatul de marcat electronic fiscal. moneda_i
Moneda în care a fost încasată suma de la client
C(3)
DA
Nomenclator monede suma_i
Suma încasată de la client
N(20.2)
DA moneda_p
Moneda în care a fost plătită suma clientului
C(3)
DA
Nomenclator monede suma_p
Suma plătită clientului
N(20.2)
DA com
Comision practicat aferent sumei tranzacționate
N(20.2)
DA totTva
Valoarea totală a taxei pe valoare adăugată
N(20.2)
DA
Valoarea totTva este egală cu însumarea valorilor tva din secțiunea cote. <cote>
Secțiune repetitivă
Cel puțin o apariție dacă totTva>0 cota_com
Nivel cotă TVA
N(2)
DA tva
Valoarea taxei pe valoare adăugată
N(20.2)
DA </cote> </bonSV> </msj>
Secțiunea II.2
Nr. crt.
Denumire secțiune/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj c(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră emitere mesaj
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică <bonT>
Secțiune repetitivă
Secțiunea va avea un număr de apariții egal cu numărul de bonuri tipărite. idB
Numărul de identificare al bonului fiscal
C(32)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRRBBBB
Primele 10 caractere = număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră emitere bonuri fiscale
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică din care face parte bonul fiscal
Următoarele 4 caractere: număr de ordine bon fiscal la nivelul zilei de lucru
Trebuie să fie unic pe aparatul de marcat electronic fiscal. nrC
Numărul cursei
N(3)
DA totB
Valoarea totală a serviciului
N(20.2)
DA totTva
Valoarea totală a taxei pe valoare adăugată
N(20.2)
DA
Valoarea totTva este egală cu însumarea valorilor tva din secțiunea cote. <cote>
Secțiune repetitivă
Se completează câte o secțiune pentru fiecare cotă existentă pe bon. cota
Nivel cotă TVA
N(2)
DA tva
Valoarea taxei pe valoare adaugată
N(20.2)
DA </cote> </bonT> </msj>
Secțiunea II.3
Nr. crt.
Denumire secțiune/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj c(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră emitere mesaj
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică. <bon>
Secțiune repetitivă
Secțiunea va avea un număr de apariții egal cu numărul de bonuri tipărite. idB
Numărul de identificare al bonului fiscal
C(32)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRRBBBB
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: data și ora emiterii bonului fiscal
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică din care face parte bonul fiscal
Următoarele 4 caractere: număr de ordine bon fiscal la nivelul zilei de lucru
Trebuie să fie unic pe aparatul de marcat electronic fiscal. totB
Valoarea totală a bonului fiscal
N(20.2)
DA totTva
Valoarea totală a taxei pe valoarea adăugată
N(20.2)
DA
Valoarea totTva este egală cu însumarea valorilor TVA din secțiunea cote. <cote>
Secțiune repetitivă
Se completează câte o secțiune pentru fiecare cotă existentă pe bon. cota
Nivel cotă TVA
N(2)
DA tva
Valoarea taxei pe valoarea adăugată
N(20.2)
DA </cote> </bon> </msj>
Secțiunea II.4
Nr. crt.
Denumire secțiune/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj c(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră emitere mesaj
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică <bon>
Secțiune repetitivă
Secțiunea va avea un număr de apariții egal cu numărul de bonuri tipărite. idB
Numărul de identificare al bonului fiscal
C(32)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRRBBBB
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: data și ora emiterii bonului fiscal
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică din care face parte bonul fiscal
Următoarele 4 caractere: număr de ordine bon fiscal la nivelul zilei de lucru
Trebuie să fie unic pe aparatul de marcat electronic fiscal. nrC
Numărul cursei aeriene
C(10)
DA totB
Valoarea totală a bonului fiscal
N(20.2)
DA totTva
Valoarea totală a taxei pe valoare adăugată
N(20.2)
DA
Valoarea totTva este egală cu însumarea valorilor TVA din secțiunea cote. <cote>
Secțiune repetitivă
Se completează câte o secțiune pentru fiecare cotă existentă pe bon. cota
Nivel cotă TVA
N(2)
DA tva
Valoarea taxei pe valoare adăugată
N(20.2)
DA </cote> </bon> </msj>
Secțiunea II.5
Nr. crt.
Denumire secțiune/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj c(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră generare mesaj
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică <rSV>
O apariție idR
Numărul de identificare al raportului fiscal de închidere zilnică
C(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere = număr unic de identificare aparat de marcat electronic fiscal
Următoarele 14 caractere: dată și oră emitere raport fiscal de închidere zilnică
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică generat
Trebuie să fie unic pe aparatul de marcat electronic fiscal. nrA
Număr avarii (reset RAM)
N(3)
DA
Numărul de secțiuni av = nrA nrB
Număr bonuri emise aferente raportului fiscal de închidere zilnică
N(10)
DA totB
Valoarea totală a operațiunilor aferente raportului fiscal de închidere zilnică
N(20.2)
DA nrBC
Număr bonuri emise aferente raportului fiscal de închidere zilnică având înscris codul de înregistrare fiscală în scopuri de TVA
N(10) nrAn
Numărul operațiunilor de anulare efectuate în timpul tipăririi bonurilor fiscale aferente raportului fiscal de închidere zilnică
N(10)
DA totA
Suma totală aferentă operațiunilor de anulare efectuate în timpul tipăririi bonurilor fiscale
N(20.2)
DA nrR
Numărul operațiunilor de reducere efectuate în timpul tipăririi bonurilor fiscale aferente raportului fiscal de închidere zilnică
N(10)
DA totR
Suma totală aferentă operațiunilor de reducere efectuate în timpul tipăririi bonurilor fiscale
N(20.2)
DA nrM
Numărul operațiunilor de majorare efectuate în timpul tipăririi bonurilor fiscale aferente raportului fiscal de închidere zilnică
N(10)
DA totM
Suma totală aferentă operațiunilor de majorare efectuate în timpul tipăririi bonurilor fiscale
N(20.2)
DA totTva
Totalul taxei pe valoare adăugată
N(20.2)
DA sume_serv_in
Sume de serviciu declarate la începerea zilei de lucru
N(20.2)
DA sume_serv_out
Sume de serviciu declarate la sfârșitul zilei de lucru
N(20.2)
DA totC
Totalul comisionului încasat din cumpărare și vânzare de valută
N(20.2)
DA <act>
Secțiune repetitivă
Cel puțin o secțiune dacă nrB-nrBA> 0
Gruparea (tipAct, mon, cota_act) trebuie să fie unică. tipAct
Tipul operațiunii
N(1)
DA 1= vânzare 2 = cumpărare totAct
Totalul sumelor încasate din cumpărarea/ vânzarea de valută, inclusiv comision
N(20.2)
DA totCom
Total comision încasat din cumpărarea/ vânzarea de valută
N(20,2)
DA mon
Moneda
C(3)
DA
Nomenclator cota_act
Nivel cotă de TVA
N(2)
Dacă totCom>0 atunci cota_act este diferit de nul. </act> <av>
Secțiune repetitivă data
Oră avarie
C(19)
DA zz.ll.aaaa HH24:mi:ss </av> <pl>
Secțiune repetitivă tipP
Modalitate de plată
N(2)
DA
Nomenclator valPl
Totalul sumei plătite de client
N(20.2)
DA monPl
Moneda în care s-a făcut plata
C(3)
DA
Nomenclator </pl> </rSV> </msj>
Secțiunea II.6
Nr. crt.
Denumire secțiune/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj c(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare aparat de marcat electronic fiscal
Următoarele 14 caractere: dată și oră generare mesaj
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică <rT>
O apariție idR
Numărul de identificare al raportului fiscal de închidere zilnică
C(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere = număr de identificare aparat de marcat electronic fiscal
Următoarele 14 caractere: dată și oră emitere raport fiscal de închidere zilnică
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică generat
Trebuie să fie unic pe aparatul de marcat electronic fiscal. nrAv
Număr avarii (reset RAM)
N(3)
DA nrAv este egal cu numărul de secțiuni av. nrB
Număr bonuri emise aferente raportului fiscal de închidere zilnică
N(10)
DA valB
Valoarea totală a operațiunilor aferente raportului fiscal de închidere zilnică
N(20.2)
DA totTva
Totalul taxei pe valoarea adăugată rezultat din totalul bonurilor fiscale emise
N(20.2)
DA nrBC
Număr bonuri emise având înscris codul de înregistrare fiscală în scopuri de TVA
N(10)
DA valBC
Valoare totală a operațiunilor din totalul bonurilor fiscale emise având înscris codul de înregistrare fiscală în scopuri de TVA
N(20.2)
DA totTVA_cui
Totalul taxei pe valoarea adăugată rezultat din totalul bonurilor fiscale ce au înscris codul de înregistrare fiscală în scopuri de TVA
N(20.2)
DA totD
Totalul distanței parcurse (în km)
N(10.2)
DA totDC
Totalul distanței parcurse având călători (în km)
N(10.2)
DA <coteZ>
Secțiune repetitivă cota
Nivel cotă TVA
N(2)
DA tva
Totalul taxei pe valoarea adăugată rezultat din totalul bonurilor fiscale emise defalcată pe cotă de TVA
N(20.2)
DA tva_cui
Totalul taxei pe valoarea adăugată rezultat din totalul bonurilor fiscale ce au înscris codul de înregistrare fiscală în scopuri de TVA, defalcată pe cotă de TVA
N(20.2)
DA </coteZ> <av>
Secțiune repetitivă ora_avarie
Oră avarie
C(19)
DA zz.ll.aaaa HH24:mi:ss </av> <ut>
Secțiune repetitivă
Cel puțin o apariție idU
Identificator persoană care utilizează taximetrul
C(5)
DA totDU
Totalul distanței parcurse (în km) de către taximetrist
N(10.2)
DA totDCU
Totalul distanței parcurse având călători de către taximetrist
N(10.2)
DA totalBU
Valoarea totală încasată de către taximetrist
N(20.2)
DA <curse>
Secțiune repetitivă nr_cursa
Numărul cursei
C(20)
DA </curse> </ut> <set>
Secțiune repetitivă nrSet
Număr aferent setului de tarif
N(1)
DA 1 - Zi 2 - Noapte tarif
Valoarea tarifului aplicat
N(3.2)
DA totSet
Totalul sumei plătite de client aferente tarifului
N(20.2)
DA totDS
Total distanță parcursă având călători aferentă tarifului
N(10.2)
DA </set> </rT> </msj>
Secțiunea II.7
Nr. crt.
Denumire element/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj c(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare aparat de marcat electronic fiscal
Următoarele 14 caractere: dată și oră generare mesaj
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică <rB>
O apariție idR
Numărul de identificare al raportului fiscal de închidere zilnică
C(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere = număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră emitere raport fiscal de închidere zilnică
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică generat
Trebuie să fie unic pe aparatul de marcat electronic fiscal. nrAv
Număr avarii (reset RAM)
N(3)
DA nrA este egal cu numărul de secțiuni av. nrB
Număr bonuri emise aferente raportului fiscal de închidere zilnică
N(10)
DA totB
Valoarea totală a operațiunilor aferente raportului fiscal de închidere zilnică
N(20.2)
DA nrBC
Număr bonuri emise aferente raportului fiscal de închidere zilnică având înscris codul de înregistrare fiscală în scopuri de TVA
N(10)
DA totBC
Valoare totală operațiuni rezultată din totalul bonurilor fiscale ce au înscris codul de înregistrare fiscală în scopuri de TVA
N(20.2)
DA nrA
Numărul operațiunilor de anulare efectuate în timpul tipăririi bonurilor fiscale aferente raportului fiscal de închidere zilnică
N(10)
DA totA
Suma totală aferentă operațiunilor de anulare efectuate în timpul tipăririi bonurilor fiscale
N(20.2)
DA nrR
Numărul operațiunilor de reducere efectuate în timpul tipăririi bonurilor fiscale aferente raportului fiscal de închidere zilnică
N(10)
DA totR
Suma totală aferentă operațiunilor de reducere efectuate în timpul tipăririi bonurilor fiscale
N(20.2)
DA nrM
Numărul operațiunilor de majorare efectuate în timpul tipăririi bonurilor fiscale aferente raportului fiscal de închidere zilnică
N(10)
DA totM
Suma totală aferentă operațiunilor de majorare efectuate în timpul tipăririi bonurilor fiscale
N(20.2)
DA totTva
Totalul taxei pe valoarea adăugată
N(20.2)
DA totTvaC
Totalul taxei pe valoarea adăugată rezultat din bonurile ce au înscris codul de înregistrare fiscală în scopuri de TVA
N(20.2)
DA totTaxe
Valoare alte taxe ce nu se cuprind în baza de impozitare a taxei pe valoarea adăugată
N(20.2)
DA totNet
Valoare operațiuni scutite
N(20.2)
DA sume_serv_in
Sume de serviciu declarate la începerea zilei de lucru
N(20.2)
DA sume_serv_out
Sume de serviciu declarate la sfârșitul zilei de lucru
N(20.2)
DA monRef
Moneda de referință a aparatului de marcat electronic fiscal
C(3)
DA
Nomenclator monede <pl>
Secțiune repetitivă
Secțiunea are cel puțin o apariție pentru totB> 0.
Altfel lipsește. tipP
Modalitate de plată
N(2)
DA
Nomenclator valPl
Totalul sumei plătite de client
N(20.2)
DA monPl
Moneda în care s-a făcut plata
C(3)
DA
Nomenclator </pl> <coteZ>
Secțiune repetitivă
Secțiunea apare pentru fiecare cotă existentă. cota
Nivel cotă de TVA
N(2)
DA valOp
Valoarea totală a operațiunilor cărora li se aplică nivelul de cotă
N(20.2)
DA tva
Total tva/cotă
N(20.2)
DA </coteZ> <av>
Secțiune repetitivă data
Dată avarie
C(19)
DA zz.ll.aaaa HH24:mi:ss </av> </rB> </msj>
Secțiunea II.8
Nr. crt.
Denumire element/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj
C(28)
DA
NNNNNNNNNNAAAALLZZHHMMSSRRRR
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră generare mesaj
Următoarele 4 caractere: numărul raportului fiscal de închidere zilnică <mE>
Maximum o apariție nrB
Număr bonuri emise în perioada în care are loc evenimentul
N(10)
DA <ev>
Secțiune repetitivă
Cel puțin o apariție dataI
Dată început eveniment
C(19)
DA zz.ll.aaaa HH24:mi:ss dataF
Dată sfârșit eveniment
C(19)
DA zz.ll.aaaa HH24:mi:ss tipE
Tipul evenimentului
N(1)
DA 1 - lipsă curent 2 - lipsă conexiune internet </ev> </mE> </msj>
Secțiunea II.9
Nr. crt.
Denumire element/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <msj> idM
Identificator unic mesaj
C(24)
DA
NNNNNNNNNNAAAALLZZHHMMSS
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră generare mesaj </msj>
Secțiunea II.10
Nr. crt.
Denumire element/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <mP> idM
Identificator unic mesaj
C(24)
DA
NNNNNNNNNNAAAALLZZHHMMSS
Identificator unic de identificare al aparatului de marcat electronic fiscal, an lună zi oră minut secundă tipP
Tipul profilului
N(1)
DA
Tipul profilului pe care trebuie să îl execute aparatul de marcat electronic fiscal: 0 - aparatul de marcat electronic fiscal nu are obligația conectării la sistemul informatic național. 1 - aparatul de marcat electronic fiscal are obligația conectării și transmiterii datelor către sistemul informatic național. data
Data de la care aparatul de marcat electronic fiscal funcționează în profilul stabilit
C(10) zz.ll.aaaa afisM
În urma analizei datelor transmise de aparatul de marcat electronic fiscal se constată că aparatul nu funcționează în parametri normali. Utilizatorul este atenționat asupra necesității prezentării la unitatea de service.
N(1) 1 - prezentare unitate de service.
Altfel lipsește. rapZ
Aparatul de marcat este obligat să încerce stabilirea conexiunii cu sistemul informatic național și să transmită date imediat după generarea raportului fiscal de închidere zilnică.
N(1) 1 - DA 2 - NU, Aparatul de marcat este obligat să încerce stabilirea conexiunii cu sistemul informatic național și să transmită date la intervalul nrT. nrZ
Număr zile după care activitatea aparatului de marcat electronic fiscal se blochează
N(4) nrM
Număr minute la care se încearcă stabilirea conexiunii cu sistemul informatic
N(6) nrT
Număr minute la care se încearcă stabilirea conexiunii cu sistemul informatic în vederea transmiterii datelor de la art. 5 alin. (1) și (2) din anexa nr. 11
N(6) codD
Cod deblocare
C(1024)
Ultimul id mesaj din mesajul registru transmis către sistemul informatic național certANAF
Certificatul digital al Agenției Naționale de Administrare Fiscală
C(4000)
Câmpul conține certificatul digital al Agenției Naționale de Administrare Fiscală în format PKCS7 cert only codificat base 64. certA
Schimbă certificatul digital al aparatului de marcat electronic fiscal.
N(1) 1 - DA <url>
Secțiune repetitivă
Secțiunea este permisă numai pentru tip_profil = 1. tip
Tip url
N(1)
DA
Categorii URL-uri din anexa nr. 3 la ordin url
Adrese folosite în comunicarea aparatului de marcat electronic fiscal cu sistemul informatic național al Agenției Naționale de Administrare Fiscală
C(50)
DA </url> </mP>
Secțiunea II.11
Nr. crt.
Denumire element/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <mReset> idM
Identificator unic mesaj
C(14)
DA
AAAALLZZHHMMSS an lună zi oră minut secundă tipP
Tipul profilului
N(1)
DA tipP = 0 dataP
Data până la care aparatul de marcat electronic fiscal funcționează în profilul 0
C(10)
DA zz.ll.aaaa
După această dată aparatul de marcat electronic fiscal trece în profilul 1. </mReset>
Secțiunea II.12
Nr. crt.
Denumire element/atribut
Semnificație atribut
Tip și lungime
Obligatoriu
Validări/Formule
Observații <mReg> idM
Identificator unic mesaj
C(24)
DA
NNNNNNNNNNAAAALLZZHHMMSS
Primele 10 caractere: număr unic de identificare al aparatului de marcat electronic fiscal
Următoarele 14 caractere: dată și oră generare mesaj cif
Cod de identificare fiscală utilizator aparat de marcat electronic fiscal
N(13)
DA nrRapI
Număr raport fiscal de închidere zilnică inițial generat în perioada de raportare
N(4)
DA nrRapF
Număr raport fiscal de închidere zilnică final generat în perioada de raportare
N(4)
DA tip_amef
Destinația aparatului de marcat electronic fiscal
C(1)
DA
S - schimb valutar
T - taximetrie
U - uzual
A - Magazin aeroporturi </mReg
Secțiunea II.13
Transmiterea fișierelor XML
Aparatul de marcat electronic fiscal vine presetat cu funcționarea în profilul 0. Trecerea la profilul 1 se face prin importul unui fișier XML prevăzut la secțiunea II.10 și care conține în mod obligatoriu următoarele categorii de informații: - tipul profilului: 1;
- data de la care se trece în profilul 1;
- numărul de zile după care activitatea aparatului de marcat electronic fiscal se blochează;
- intervalul în minute la care aparatul de marcat electronic fiscal încearcă conectarea la sistemul informatic național de supraveghere și monitorizare a datelor fiscale;
- intervalul în minute la care aparatul de marcat electronic fiscal încearcă conectarea la sistemul informatic național de supraveghere și monitorizare a datelor fiscale în vederea transmiterii datelor prevăzute la art. 3 alin. (1) sau (2) din anexa nr. 11 la normele metodologice;
-
URL-urile utilizate în comunicarea aparatului de marcat electronic fiscal cu sistemul informatic național de supraveghere și monitorizare a datelor fiscale;
- certificatul digital al Agenției Naționale de Administrare Fiscală în format PKCS#7 cert only codificat base 64.
Operațiunea de trecere de la profilul 0 la profilul 1 se efectuează exclusiv de către tehnicianul de service al distribuitorului autorizat sau al unității de service acreditate.
Trecerea de la profilul 1 la profilul 0 se face prin importul unui fișier XML semnat folosind certificatul digital al Agenției Naționale de Administrare Fiscală prevăzut la secțiunea II.11 și care conține în mod obligatoriu următoarele categorii de informații: - tipul profilului: 0;
- data până la care aparatul de marcat electronic fiscal funcționează în profilul 0.
Operațiunea de trecere de la profilul 1 la profilul 0 se efectuează exclusiv de către tehnicianul de service al distribuitorului autorizat sau al unității de service acreditate.
Aparatul de marcat electronic fiscal care lucrează în profilul 1 își blochează activitatea de emitere și tipărire de bonuri fiscale ca urmare a atingerii/depășirii termenului stabilit potrivit art. 8 din anexa nr. 11 la normele metodologice. Deblocarea aparatului de marcat electronic fiscal se face ulterior transmiterii datelor prevăzute la art. 3 alin. (1) sau alin. (2) din anexa nr. 11 la normele metodologice prin importul unui fișier XML prevăzut la secțiunea II.10.
Fișierul conține în mod obligatoriu următoarele categorii de informații: - tipul profilului;
- cod deblocare activitate aparat de marcat electronic fiscal, reprezentat de valoarea id mesaj al ultimului mesaj registru transmis.
În cazul aparatelor de marcat electronice fiscale care transmit online către sistemul informatic național datele prevăzute la art. 3 alin. (1) sau (2) din anexa nr. 11 la normele metodologice, se transmit unul sau mai multe fișiere XML conform secțiunilor II.1-II. 9, după caz.
În cazul aparatelor de marcat electronice fiscale care transmit offline către sistemul informatic datele prevăzute la art. 3 alin. (1) sau (2) din anexa nr. 11 la normele metodologice, se exportă pe un mediu de stocare extern unul sau mai multe fișiere XML semnate cu certificatul digital al acestora, care conțin datele aferente fiecărei zile fiscale încheiate conform secțiunilor II.1-II.7, precum și un fișier XML registru conform secțiunii II.12. Fișierele se validează și se atașează la un PDF folosind aplicația pusă la dispoziție pe portalul Agenției Naționale de Administrare Fiscală și se depune la organul fiscal folosind mijloace de transmitere la distanță.
Fișierul de la secțiunea II.10 conține valorile indicatorilor pe baza cărora aparatul de marcat electronic fiscal funcționează, este semnat folosind certificatul digital al Agenției Naționale de Administrare Fiscală și se transmite ca răspuns la îndeplinirea obligației aparatului de marcat electronic fiscal prevăzută la art. 3 alin. (1) sau (2) din anexa nr. 11 la normele metodologice.
În cazul aparatelor de marcat electronice fiscale care funcționează în modul de lucru offline, mesajul de la secțiunea II.10 ce conține atât codul de deblocare, respectiv continuare a activității, și/sau valorile modificate ale indicatorilor profilului se recepționează după transmiterea datelor prevăzute la art. 3 alin. (1) sau (2) din anexa nr. 11 la normele metodologice.
Comunicarea dintre aparatele de marcat electronice fiscale și sistemul informatic național de supraveghere și monitorizare a datelor fiscale se face prin transmiterea, respectiv recepționarea fișierelor prevăzute în secțiunile II.1-II.12. Fișierele XML trebuie să conțină elementele, respectiv atributele marcate ca fiind obligatorii. Succesiunea elementelor este în mod obligatoriu cea prevăzută în cadrul fiecărei secțiuni. Atributele care în dreptul coloanei „Câmp obligatoriu” nu au prevăzută mențiunea „DA” se vor transmite numai în cazul în care informația respectivă există. Fișierele XML care se transmit offline sunt semnate, aplicându-se o semnătură inclusă conformă cu standardul PKCS#7 folosind algoritmul de calcul al rezumatului SHA-256 și algoritmul de semnătură bazat pe RSA 2048. Structura certificatului digital X.509v3 conform cu RFC 5280 are minimum următoarele caracteristici:
ISSUER
NUMELE DISTINCTIV AL AUTORITĂȚII DE CERTIFICARE EMITENTE (DN)
SerialNumber
Numărul de serie al certificatului. Acest număr este unic și va conține minimum 4 octeți cu date generate aleatoriu.
Subject
Numele distinctiv al entității pentru care se emite certificatul. Acesta va include informații de identificare a aparatului de marcat electronic fiscal (numărul de serie al aparatului).
SignatureAlgorithm
Tipul de semnătură cu care autoritatea de certificare a emis certificatul
NotBefore
Data începând cu care certificatul este valid
NotAfter
Data la care expiră certificatul digital
Subject Key Identifier
Identificatorul cheii subiectului
Authority Info Access [1]Authority Info Access
Access Method=On-line Certificate Status Protocol (1.3.6.1.5.5.7.48.1)
Alternative Name:
URL=url-ul la care autoritatea de certificare pune la dispoziție mecanismul de validare al certificatelor digitale OCSP conform RFC 6960
Certificate Policies [1]Certificate Policy:
Policy Identifier=OID-ul politicii sub care sunt emise certificatele de către autoritatea de certificare [2,1]Policy Qualifier Info:
Policy Qualifier Id=CPS
Qualifier: url-ul unde se găsește documentul descriptiv privind emiterea certificatelor digitale de către autoritatea de certificare
CRL Distribution Points url-ul unde sunt publicate CRL-urile emise de autoritatea de certificare
Operațiunea de reînnoire se face prin generarea perechii de chei publică-privată pentru care se emite certificatul de către modulul criptografic al aparatului de marcat electronic fiscal folosind protocolul simplu de înrolare a certificatelor pe baza protocolului de comunicații IETF-CMC, respectând standardul RFC 5280 care guvernează bunele practici și specificațiile tehnice pentru acest tip de informații electronice.
Operațiunea de reînnoire a certificatului digital al aparatului de marcat electronic fiscal se face: - la cererea sistemului informatic național de supraveghere și monitorizare a datelor fiscale al Agenției Naționale de Administrare Fiscală sau
- de către producător sau, după caz, de către distribuitorul autorizat, ca urmare a atingerii/depășirii perioadei de valabilitate de 10 ani a certificatului digital instalat inițial.
Secțiunea II.14
Nomenclatorul pentru tipul de plată:
Semnificație
Valoare
Card 1
Numerar 3
Tichete masă 4
Bonuri/tichete valorice 5
Voucher 6
Credit 7
Metode moderne de plată 8
Alte metode 9
Nomenclatorul pentru valută:
Valoare
Semnificație
AED
DIRHAM UAE
AFA
AFGANI AFGANISTAN
ALL
LEKA ALBANEZ
AMD
DRAM ARMENIAN
ANG
GULDEN ANTILE OLAND.
AON
KWANZA (NOU) ANGOLA
ARS
PESO ARGENTINIAN
AUD
DOLAR AUSTRALIAN
AWG
FLORIN ARUBAN
AZM
MANAT AZERBAIDJAN
BAM
MARCA CONV. BOSNIACĂ
BBD
DOLAR BARBADOS
BDT
TAKA BANGLADESH
BGN
LEVA BULGĂREASCĂ
BHD
DINAR BAHRAINI
BIF
FRANC BURUNDI
BMD
DOLAR BERMUDIAN
BND
DOLAR BRUNEI
BOB
BOLIVIAN BOLIVIAN
BRL
REAL BRAZILIAN
BSD
DOLAR BAHAMAS
BTN
NGULTRUM BHUTAN
BWP
PULL BOTSWANA
BYR
RUBLĂ BIELORUSĂ
BZD
DOLAR BELIZE
CAD
DOLAR CANADIAN
CDF
FRANC CONGOLEZ
CHF
FRANC ELVEȚIAN
CLP
PESO CILIAN
CNY
YUAN RENMINBI CHINA
COP
PESO COLUMBIAN
CRC
COLON COSTA RICA
CSD
DINAR SERBIA&MUNTEN.
CUP
PESO CUBANEZ
CVE
ESCUDO CABOVERDIANO
CYP
LIRA CIPRIOTĂ
CZK
COROANA CEHĂ
DJF
FRANC DJIBOUTI
DKK
COROANA DANEZĂ
DOP
PESO REP. DOMINICANĂ
DZD
DINAR ALGERIAN
ECS
SUCRE ECUADOR
EEK
CORONA ESTONIANĂ
EGP
LIRA EGIPTEANĂ
ERN
NAKFA ERITREA
ETB
BIRR ETIOPIA
EUR
EURO
FJD
DOLAR FIJI
FKP
LIRA FALKLAND
GBP
LIRA STERLINĂ
GEL
LARI GEORGIA
GHC
CEDI GHANA
GIP
LIRA GIBRALTAR
GMD
DALASI GAMBIA
GTQ
QUETZAL GUATEMALA
GYD
DOLAR GUYANA
HKD
DOLAR HONG KONG
HNL
LEMPIRA HONDURAS
HRK
KUNA CROATĂ
HTG
GOURDE HAITI
HUF
FORINT MAGHIAR
IDR
RUPIA INDONEZIANĂ
ILS
SECHEL ISRAELIAN
INR
RUPIA INDIANĂ
IQD
DINAR IRAQ
IRR
RIAL IRANIAN
ISK
COROANA ISLANDEZĂ
JMD
DOLAR JAMAICA
JOD
DINAR IORDANIA
JPY
YEN JAPONEZ
KES
SILING KENYA
KGS
SOM KIRGHIZSTAN
KHR
RIEL CAMBODGIA
KMF
FRANC COMORIAN
KPW
WON NORD-COREEAN
KRW
WON SUD-COREEAN
KWD
DINAR KUWEIT
KYD
DOLAR INSULE CAYMAN
KZT
TENGE KAZAKHSTAN
LAK
KIP LAOS
LBP
LIRA LIBAN
LKR
RUPIA SRI LANKA
LRD
DOLAR LIBERIA
LSL
MALOTI LESOTHO
LTL
LITU LITUANIAN
LVL
LATS LETONIA
LYD
DINAR LIBIA
MAD
DIRHAM MAROCAN
MDL
LEU MOLDOVENESC
MGF
FRANC MADAGASCAR
MKD
DENAR MACEDONIA
MMK
KYAT MYANMAR
MNT
TUGRIK MONGOLIA
MOP
PATACA MACAO
MRO
OUGUIYA MAURITANIA
MTL
LIRA MALTEZĂ
MUR
RUPIA MAURITIUS
MVR
RUFIYAA MALDIVE
MWK
KWACHA MALAWI
MXN
PESO MEXICAN
MYR
RINGGIT MALAIEZIA
MZM
METICAL MOZAMBIC
NAD
DOLAR NAMIBIAN
NGN
NAIRA NIGERIA
NIO
CORDOBA NICARAGUA
NOK
COROANA NORVEGIANĂ
NPR
RUPIA NEPALEZĂ
NZD
DOLAR NEOZEELANDEZ
OMR
RIYAL OMANI
PAB
BALBOA PANAMEZĂ
PEN
SOL NOU PERU
PGK
KINA PAPUA&NOUA GUI.
PHP
PESO FILIPINE
PKR
RUPIA PAKISTAN
PLN
ZLOT NOU POLONEZ
PYG
GUARANI PARAGUAY
QAR
RIYAL QATARI
RON
LEU ROMÂNIA
RUB
RUBLA RUSEASCĂ NOUĂ
RUR
RUBLA RUSEASCĂ
RWF
FRANC RWANDA
SAC
RAND COM.SUD AFRICAN
SAR
RIYAL ARABIA SAUDITĂ
SBD
DOLAR INSULE SOLOMON
SCR
RUPIE SEYCHELLES
SDP
LIRA SUDANEZĂ
SEK
COROANA SUEDEZĂ
SGD
DOLAR SINGAPORE
SHP
LIRA ST HELENA
SIT
TOLAR SLOVENIAN
SKK
COROANA SLOVACĂ
SLL
LEU SIERRA LEONE
SOS
SILING SOMALIA
SRG
GULDEN SURINAM
STD
DOBRA SAO TOME&PRINC
SVC
COLON EL SALVADOR
SYP
LIRA SIRIANĂ
SZL
LILANGENI SWAZILAND
THB
BAHT THAILANDEZ
TJR
RUBLA TADJIKISTAN
TMM
MANAT TURKMENISTAN
TND
DINAR TUNISIAN
TOP
TONGAN PA'ANGA
TRL
LIRE TURCEȘTI
TRY
LIRA TURCEASCĂ NOUĂ
TTD
DOLAR TRINIDAD&TOBAG
TWD
DOLAR NOU TAIWAN
TZS
SILING TANZANIAN
UAH
HRYVNA UCRAINEANĂ
UGX
SILING UGANDA
USD
DOLAR SUA
UYU
PESO NOU URUGUAI
UZS
SUM UZBEKISTAN
VEB
BOLIVAR VENEZUELA
VND
DONG VIETNAM
VUV
VATU VANUATU
WST
TALA SAMOA DE VEST
XAF
FRANC COM. FINANCIARĂ
XAU
AUR
XCD
DOLAR CARAIBELE DE EST
XDR
DST
XPF
FRANC CFP
YER
RIYAL YEMEN
YUM
DINAR IUGOSLAV
ZAR
RAND SUD-AFRICAN
ZMK
KWACHA ZAMBIA
ZRN
ZAIR NOU
ZWD
DOLAR ZIMBABWE
