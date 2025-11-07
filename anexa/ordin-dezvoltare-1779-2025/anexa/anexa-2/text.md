# Anexa 2
Anexa nr. 2
la ghid
SPECIFICAȚIILE TEHNICE
pentru elaborarea seturilor de date asociate
planului de mobilitate urbană durabilă (PMUD)
Articolul 1
(1)
Seturile de date asociate PMUD sunt organizate și prezentate într-o bază de date format deschis Geopackage (.gpkg).
(2)
Seturile de date asociate PMUD care au asociate geometrii sunt denumite în continuare seturi de date spațiale.
Articolul 2
Seturile de date spațiale pentru PMUD se corelează cu temele de date spațiale prevăzute în anexa nr. 3 - Teme de date spațiale III, pct. III.4. „Utilizarea terenului“ la Ordonanța Guvernului nr. 4/2010 privind instituirea Infrastructurii naționale pentru informații spațiale în România, republicată.
Articolul 3
(1)
Seturile de date spațiale pentru PMUD se realizează în Sistemul național de proiecție stereografic 1970, cunoscut ca Stereo 70, având codul SRID (identificatorul sistemului de referință spațială) 3844 în cadrul registrului EPSG (European Petroleum Survey Group).
(2)
Scara la care se digitizează PMUD este 1:5000.
Articolul 4
(1)
MDLPA, prin Observatorul teritorial, pune la dispoziția elaboratorilor de PMUD un fișier model cu baza de date în formatul solicitat la art. 1 alin. (1) , însoțit de detalii tehnice și instrucțiuni de utilizare, completare și comunicare în Registrul național al planurilor de mobilitate urbană durabilă.
(2)
Modelul de bază de date format Geopackage conține minim seturile de date prezentate în tabelul nr. 1, acestea putând fi extinse în funcție de necesitățile identificate la nivelul platformei Observatorului teritorial.
(3)
Prin Observatorul teritorial sunt puse la dispoziția elaboratorilor instrumente de validare a conținutului seturilor de date prin care se vor implementa cele mai bune practici din domeniu și se vor asigura mecanismele de agregare, raportare și interoperabilitate a seturilor de date.
(4)
Tabelul nr. 1 - Setul minim de date spațiale PMUD - obiecte spațiale
Nr. crt.
Denumire obiect spatial
Geometrie
Descriere
Atribute minime
Detalii
1
Limita_UAT
Poligon
Limita UAT conform ANCPI
denumire
Text liber 255 de caractere
siruta
Conform nomenclatorului national SIRUTA
sursa
Text liber 255 de caractere
2
Intravilan
Poligon
Limita intravilanului localitatilor
denumire
Text liber 255 de caractere
siruta
Conform nomenclatorului national SIRUTA
sursa
Text liber 255 de caractere
3
Cai_rutiere
Linie
Reteaua de cai rutiere
indicativ
Text liber 255 de caractere
categorie
Autostrada, drum expres, drum national, drum judetean, drum comunal sau alta categorie de drum
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
4
Cai_feroviare*
Linie
Reteaua de cai ferate
indicativ
Text liber 255 de caractere
electrificare
Da sau nu
ecartament
Normal sau îngust
latime
Simpla sau dubla
transport_persoane
Da sau nu
transport_marfa
Da sau nu
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
5
Statii_CF
Punct
Statii de cale ferata
denumire
Text liber 255 de caractere
categorie
Principal sau secundar
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
6
TP
Linie
Transport de persoane
denumire
Text liber 255 de caractere
categorie
Public sau privat
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
7
Benzi_TP
Linie
Benzi dedicate pentru transport public
latime
Numar intreg
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
8
Statii_TP
Punct
Statii de transport public
denumire
Text liber 255 de caractere
categorie
tramvai, autobuz/troleibuz, microbuz, mixt
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
9
Noduri_intermodale
Punct
Noduri intermodale
denumire
Text liber 255 de caractere
acces_cf
Da sau nu
acces_tramvai
Da sau nu
acces_bus
Da sau nu
acces_parcare
Da sau nu
acces_velo
Da sau nu
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
10
MA
Linie
Mijloace alternative de mobilitate
denumire
Text liber 255 de caractere
categorie
Public sau privat
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
11
Piste
Linie
Piste de biciclete
denumire
Text liber 255 de caractere
latime
Numar întreg
sursa
Text liber 255 de caractere
situatie
Existent sau propus
proiect_id
ID din tabela proiecte_pmud
12
Generatori
Punct
Generatori de trafic
denumire
Text liber 255 de caractere
categorie
Lista de valori predefinita
mza
Intreg
max
Intreg
13
ZNRC
Poligon
Zone cu nivel ridicat de complexitate (de exemplu, zone care genereaza trafic/zone care au servituti ce afecteaza mobilitatea - zone cu emisii scazute sau zone linistite stabilite conform prevederilor Legii nr. 121/2019 privind evaluarea si gestionarea zgomotului ambiant, cu modificarile si completarile ulterioare)
denumire
Text liber 255 de caractere
descriere
Text liber 4.000 de caractere
tip_znrc
Lista de valori predefinita
14
Puncte_masurare
Punct
Puncte de masurare trafic
identificator
Text liber 255 de caractere
denumire
Text liber 255 de caractere
siruta
Conform nomenclatorului national SIRUTA
x_coord
Numar
y_coord
Numar
15
Po_obiective
Fara
Obiective plan operational
obiectiv_national
Lista de valori predefinita
directie_actiune
Lista de valori predefinita
obiectiv_propus
Text liber 4.000 de caractere
16
Po_masuri
Fara
Masuri plan operational
obiectiv_national
Lista de valori predefinita
directie_actiune
Lista de valori predefinita
obiectiv_propus_id
ID din tabela PO_obiective
proiect_id
ID din tabela proiecte_pmud
masura
Text liber 4.000 de caractere
17
Proiecte_pmud
Punct
Lista de proiecte din PMUD
denumire
Text liber 255 de caractere
valoarea_totala_euro
Numar
surse_proprii_euro
Numar
surse_europene_euro
Numar
surse_altele_euro
Numar
18
Po_indicatori
Fara
Indicatori PMUD la nivel de masura
masura_id
ID din tabela po_masuri
tip indicator
Lista de valori predefinita
valoare_existenta
Numar
valoare_propusa
Numar
19
Indicatori_pmud
Fara
Indicatori PMUD existenti si propusi la final de implementare PMUD
tip indicator
Lista de valori predefinita
valoare_existenta
Numar
valoare_propusa
Numar
