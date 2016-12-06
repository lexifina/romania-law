# Anexa 1
Raport de instalare și punere în funcțiune AIS - interior Attestation relative au montage et au fonctionnement de l'appareil AIS Interieur
```
┌────────────────────────────────────────────────────────────────────────────┐
│ 1. Detalii navă/Details du bateau                                          │
├──────────────────────────────────────┬─────────────────────────────────────┤
│ 1.1. NUMELE NAVEI:                   │ 1.2. ENI:                           │
│ Nom du bateau                        │                                     │
├──────────────────────────────────────┼─────────────────────────────────────┤
│ 1.3. Număr ANR:                      │ 1.4. Tipul navei:                   │
│ Numero officiel                      │ Type de bateau                      │
├──────────────────────────────────────┼─────────────────────────────────────┤
│ 1.5. Număr identificare radio (MMSI):│ 1.6. Armator:                       │
│ N° d'appel du service mobile maritime│ Proprietaire du bateau              │
├──────────────────────────────────────┼─────────────────────────────────────┤
│ 1.7. Persoană de contact:            │ 1.8. Email:                         │
│ Contact                              │                                     │
├──────────────────────────────────────┴─────────────────────────────────────┤
│ 1.9. Adresa:                                                               │
│ Adresse                                                                    │
├──────────────────────────────────────┬─────────────────────────────────────┤
│ 1.10. Telefon:                       │ 1.11. Fax:                          │
│ Telephone                            │                                     │
├──────────────────────────────────────┴─────────────────────────────────────┤
│ 2. Societatea autorizată pentru instalare și verificare AIS/Societe        │
│ specialisee agreee pour le montage et fonctionnement                       │
├──────────────────────────────────────┬─────────────────────────────────────┤
│ 2.1. Societatea:                     │ 2.2. Email                          │
│ Nom de societe                       │                                     │
├──────────────────────────────────────┴─────────────────────────────────────┤
│ 2.3. Adresa:                                                               │
│ Adresse                                                                    │
├──────────────────────────────────────┬─────────────────────────────────────┤
│ 2.4. Telefon:                        │ 2.5. Fax:                           │
│ Telephone                            │                                     │
├──────────────────────────────────────┼─────────────────────────────────────┤
│ 2.6. Locul, data:                    │ 2.7. Ștampila/Semnătura             │
│ Lieu, date                           │ Cachet de la societe/signature      │
├──────────────────────────────────────┴─────────────────────────────────────┤
│ 3. Detalii Stație AIS/Details appareil AIS Interieur                       │
├─────────────────┬────────────────────────┬─────────────────────────────────┤
│ Tip:            │ Producător:            │ Număr certificat:               │
│ Type            │ Fabricant              │ N° d'agrement                   │
├─────────────────┴────────────────────────┴─────────────────────────────────┤
│ 4. Configurația echipamentului AIS/Corfguration d'equipement AIS interieur │
├────────────────────────────────────────────────────────────────────────────┤
│ 4.1. Informații generale/Informations generales                            │
├─────────────────────┬─────────────────┬─────────────────────┬──────────────┤
│ Producător:         │                 │ Seria:              │              │
│ Fabricant           │                 │ Numero de serie     │              │
├─────────────────────┼─────────────────┼─────────────────────┼──────────────┤
│ Versiune:           │                 │ MMSI                │              │
│ Version du logiciel │                 │                     │              │
├─────────────────────┼─────────────────┼─────────────────────┼──────────────┤
│ Numele navei:       │ ATIS            │ ENI                 │              │
│ Nom du bateau       │                 │                     │              │
├─────────────────────┼─────────────────┼─────────────────────┼──────────────┤
│Calitatea semnalului:│ Vieza:          │ Cursul:             │ Direcția:    │
│Qualite de l'entree  │ Vitesse:        │ Route: haut bas     │ Direction:   │
│du capteur           │ haut bas        │                     │ haut bas     │
├─────────────────────┴─────────────────┴─────────────────────┴──────────────┤
│ 4.2. Informații particularizate pentru navă/convoi/Donnees semi-statiques  │
│ (statiques element pour un batiment, semi statiques pour un convoi)        │
├─────────────────────────┬────┬────┬────┬────┬──────────────────────────────┤
│Poziționarea antenei la  │ A: │ B: │ C: │ D: │  ─ ┌─────────────── .        │
│bordul navei propulsoare │    │    │    │    │  ↑ │                 .       │
│/Position de l'antenne   │    │    │    │    │ C↓ │                  .      │
│GNSS interne (m) par     │    │    │    │    │  ──┼────o              .     │
│rapport a la dimension   │    │    │    │    │  ↑ │    │               .    │
│totale                   │    │    │    │    │ D│ │    │              .│    │
├─────────────────────────┼────┼────┼────┼────┤  │ │    │             . │    │
│Poziționarea antenei în  │ A: │ B: │ C: │ D: │  ↓ │    │            .  │    │
│convoi/Position de       │    │    │    │    │  ─ └────┼───────────.   │    │
│l'antenne GNSS externe   │    │    │    │    │    │←B─→│←────A────────→│    │
│(m) par rapport a la     │    │    │    │    │                              │
│dimension totale         │    │    │    │    │                              │
├───────────────────────┬─┴────┴───┬┴────┴────┴────────────┬─────────────────┤
│Lungime convoi/        │Cod ERI / │Lățime convoi /        │Cod OMI/         │
│Longueur du convoi (dm)│Code ERI  │Largeur du convoi (dm) │Cod OMI          │
├───────────────────────┴──────────┴───────────────────────┴─────────────────┤
│ 4.3. Informații voiaj/Donnees relatives au voyage                          │
├───────────────────────┬──────────────────┬─────────────┬───────────────────┤
│Starea navei/convoiului│Acostat/terre     │Ancorat/ancre│Marș/en mouvement  │
│/Statut de navigation  │                  │             │                   │
├───────────────────────┼────────┬─────────┼─────────────┼──────┬────────────┤
│Încărcare/descărcare   │Încărcat│Descărcat│Mărfuri      │Clasa/│Cantitatea/ │
│Chargement/dechargement│/Charge │/Lege    │periculoase/ │classe│quantite    │
│                       │        │         │Bleu Cones   │      │            │
├───────────────────────┼──────┬─┴─────────┼─────────────┼──────┼────────────┤
│Înălțimea antenei AIS/ │      │Destinația │             │ETA:  │            │
│Inland AIS Tirant d'eau│      │navei/     │             │      │            │
│cm                     │      │Destination│             │      │            │
├───────────────────────┼──────┼───────────┼─────────────┼──────┴────────────┤
│Număr total de persoane│      │Echipaj/   │Alte persoane│Pasageri/Passagers:│
│la bord/Personnes a    │      │Equipage:  │/Autre       │                   │
│bord                   │      │           │personnel de │                   │
│                       │      │           │bord         │                   │
├───────────────────────┴──────┴───────────┴─────────────┴───────────────────┤
│Utilizatorul a fost informat cum să introducă datele privind configurația   │
│statică și de voiaj precum și alte informații privind echipamentul AIS/     │
│L'usager a ete informe de la maniere de saisir et de mettre a jour les      │
│donnees semi-statiques et de voyage ci-dessus ainsi que d'autres            │
│informations optionnelles supportees par l'appareil AIS Interieur           │
├────────────────────────────────────────────────────────────────────────────┤
│ 5. Instalarea AIS-interior/Montage de l'appareil AIS interieur             │
├────────────────────────────────────────────────────────────────────────────┤
│Descrierea echipamentelor perifierice - funcționare, specificații/          │
│Veuillez indiquer les appareils peripheriques relies - Fabricant de         │
│l'appareil et la specification du type                                      │
├──────────────────────────────────────┬─────────────────────────────────────┤
│Modul de alimentare a AIS/            │                                     │
│Alimentation electrique de l'appareil │                                     │
│AIS interieur                         │                                     │
├──────────────────────────────────────┼─────────────────────────────────────┤
│Lungimea estimativă a cablului de     │                                     │
│antenă GNSS/ Longueur estimee du cable│                                     │
│vers l'antenne GNSS en m              │                                     │
├──────────────────────────────────────┼─────────────────────────────────────┤
│Lungimea estimativă a cablului de     │                                     │
│antenă VHF/Longueur estimee du cable  │                                     │
│vers l'antenne VHF en m               │                                     │
├──────────────────────────────────────┼─────────────────────────────────────┤
│Se va atașa o schiță cu poziționarea  │                                     │
│antenei VHF și GNSS/Veuillez decrire  │                                     │
│l'emplacement de l'antenne VHF et GNSS│                                     │
│(interne, externe) ci-dessous ou      │                                     │
│joignez un croquis au present document│                                     │
├──────────────────────────────────────┴─────────────────────────────────────┤
│ 6. Verificarea instalației de către:/Le controle final du montage a ete    │
│effectue par.                                                               │
├──────────────────────────────┬───────┬────────────────────────────┬────────┤
│Verificarea vizuală a datelor │       │Verificarea vizuală a       │        │
│afișate de echipament pentru  │       │datelor afișate de          │        │
│nava proprie/Controle visuel  │       │echipament pentru altă navă.│        │
│du clavier et de l'affichage  │       │/Controle visuel du clavier │        │
│des donnees relatives au      │       │et de l'affichage des       │        │
│bateau                        │       │donnees relatives a d'autres│        │
│                              │       │bateaux                     │        │
├──────────────────────────────┼───────┼────────────────────────────┼────────┤
│Verificarea datelor navei     │       │Verificarea datelor navei   │        │
│proprii afișate pe ECDIS/     │       │proprii afișate pe un       │        │
│Verification des donnees      │       │echipament AIS de la o altă │        │
│relatives au bateau via un    │       │navă/Verification des       │        │
│appareil ECDIS                │       │donnees relatives au bateau │        │
│                              │       │via un autre appareil de    │        │
│                              │       │reception AIS               │        │
├──────────────────────────────┴───────┴────────────────────────────┴────────┤
│ 7. Configurația AIS/Configuration du capteur                               │
├───────────────────┬────────────────────┬───────────────┬───────────────────┤
│Senzori conectați/ │Tipul echipamentului│Tipul NMEA/NMEA│Viteza de          │
│Capteur connecte   │/Type d'equipement  │Talker/peines  │actualizare/Vitesse│
│                   │connecte            │               │de l'information de│
│                   │                    │               │mise a jour        │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH1 │                    │               │                   │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH2 │                    │               │                   │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH3 │                    │               │                   │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH4 │                    │               │                   │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH5 │                    │               │                   │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH8 │                    │               │                   │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH9 │                    │               │                   │
├───────────────────┼────────────────────┼───────────────┼───────────────────┤
│Senzor/Capteur CH10│                    │               │                   │
├───────────────────┴────────────────────┴───────────────┴───────────────────┤
│ 8. Specificațiile alarmelor/Indication des alarmes actives SI presente     │
├───────────────────┬─────────┬──────────┬────────────────┬─────────┬────────┤
│Tipul alamei/      │Da/Oui   │Nu/Non    │Tipul alarmei/  │Da/Oui   │Nu/Non  │
│Type d'alarme      │         │          │Type d'alarme   │         │        │
├───────────────────┼─────────┼──────────┼────────────────┼─────────┼────────┤
│                   │         │          │                │         │        │
├───────────────────┼─────────┼──────────┼────────────────┼─────────┼────────┤
│                   │         │          │                │         │        │
├───────────────────┼─────────┼──────────┼────────────────┼─────────┼────────┤
│                   │         │          │                │         │        │
├───────────────────┼─────────┼──────────┼────────────────┼─────────┼────────┤
│                   │         │          │                │         │        │
├───────────────────┼─────────┼──────────┼────────────────┼─────────┼────────┤
│                   │         │          │                │         │        │
├───────────────────┼─────────┼──────────┼────────────────┼─────────┼────────┤
│                   │         │          │                │         │        │
├───────────────────┼─────────┼──────────┼────────────────┼─────────┼────────┤
│                   │         │          │                │         │        │
├───────────────────┴─────────┴──────────┴────────────────┴─────────┴────────┤
│ 9. Confirmare instalare și instruire/Confirmation de montage et une        │
│ qualifie adequate                                                          │
├──────────────────────────────────────┬─────────────────────────────────────┤
│        Societatea autorizată         │      Coducatorul navei/armator      │
│        Societe de montage            │      Conducteur/proprietaire        │
├──────────────────────────────────────┼─────────────────────────────────────┤
│ Nume:                                │                                     │
│ Nom                                  │                                     │
├──────────────────────────────────────┼─────────────────────────────────────┤
│ Semnatura                            │                                     │
│ Signature:                           │                                     │
├──────────────────────────────────────┼─────────────────────────────────────┤
│ Locul                                │ Data:                               │
│ Lieu:                                │ Date                                │
└──────────────────────────────────────┴─────────────────────────────────────┘
```
