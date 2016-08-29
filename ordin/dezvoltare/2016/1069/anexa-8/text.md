# Anexa nr. 5 la protocol
Condiții tehnice și de securitate privind suportul de comunicații
Canalul de comunicație asigurat de către STS este de tipul VPN securizat (tehnologie IPSEC) și se închide pe un echipament de routare instalat la beneficiar.
STS pune la dispoziția beneficiarului infrastructură de transport formată din nucleul rețelei proprii și rețeaua periferică proprie sau contractată de la terți furnizori de buclă locală.
Elementele de comunicații necesar a fi achiziționate de către UAT/SAT sau agențiile subordonate sunt următoarele: ● router VPN, conform specificațiilor din prezenta anexă; ● serviciu de date de buclă locală de tip VPN nivel 2 închiriat de la terți operatori (în cazul în care STS nu dispune de soluție tehnică de interconectare în locația beneficiarului).
După achiziționare și instalare, echipamentele vor fi preluate în sistemul de management de către STS și vor fi monitorizate 24x7.
Responsabilitatea STS pentru remedierea deranjamentelor se extinde numai asupra serviciului de comunicații, sistemele informatice și aplicațiile fiind în responsabilitatea reprezentanților DRPCÎV.
Punctul de contact STS pentru conectarea UAT/SAT și a agențiilor subordonate este Centrul de Management Rețele (NOC) STS București (tel. 021/2022648, e-mail hqdti@stsnet.ro).
După punerea în funcțiune a serviciului, eventualele deranjamente vor fi anunțate către NOC OJTS, urmând ca, în funcție de domeniul în care se încadrează deranjamentul sesizat, acesta să se escaladeze către NOC STS București, respectiv MAI DGCTI.
Specificații tehnice pentru subsistemul de comunicații
1.
Bucla locală închiriată de la operatori publici I.
Suportul fizic pe care este asigurată legătura de date: - conexiune permanentă instalată la sediul beneficiarului, pentru serviciul de buclă locală;
- se vor asigura echipamentele de media conversie pentru suportul fizic oferit, acestea asigurând cel puțin o interfață Ethernet/FastEthernet;
- serviciul de comunicații de buclă locală trebuie să permită dirijarea traficului între locația beneficiarului și sediul STS județean (OJTS).
II.
Caracteristicile tehnice ale legăturilor de date (obligatorii): - conexiuni permanente nivel 2 dedicate, VLAN Ethernet, EoMPLS, VPWS, VPLS, end-to-end (denumite generic conexiuni de nivel 2);
- serviciile vor fi agregate la OJTS pe o interfață de tip Ethernet/FastEthernet;
- furnizorul are obligația să asigure separarea traficului asigurat pentru acest proiect de restul traficului transportat prin rețelele sale (VLAN dedicat).
III.
Caracteristici generale de performanță: - disponibilitatea accesului = 99,90%;
- latența pachetelor/1000 pachete < 30 ms;
- procent de pachete pierdute < 1%;
- bandă garantată: 100%.
Observație: Achiziția de servicii de comunicații de buclă locală de la un alt operator decât principalii operatori de pe piață și cu care Serviciul de Telecomunicații Speciale colaborează presupune obținerea unui aviz de securitate eliberat de către STS și încheierea unui acord de confidențialitate între STS și operatorul respectiv.
2.
Router
Configurație și performanțe hardware
Carcasă ● Router rack-mount 19 inch de 1U sau kit de montare în rack (tavă, șuruburi, piulițe, alte accesorii, de la același producător)
Interfețe ● 2 interfețe WAN Ethernet: minimum 1GE și 1FE ● 8 interfețe LAN 10/100 Ethernet: în configurație de switch administrat cu un suport minim de 14 VLAN-uri 802.1q ● 2 interfețe USB 2.0 ● 1 port consolă (pentru acces direct la interfața de configurare a echipamentului)
Memorie ● Memorie Flash minimum 256 MB ● Memorie DRAM minimum 512 MB ● Memoria instalată va trebui să asigure simultan toate funcționalitățile solicitate.
Performanțe ● Performanțe de routare: minimum 90.000 pps (pachete de 64 bytes/secundă) ● Performanțe de trafic cu servicii simultane de Firewall,
PBR, QoS, IPSec, NAT: minimum 10 Mbps. ● Trafic IPSec VPN multi-tunel: minimum 50 Mbps ● Număr de tunele IPSec VPN concurente: minimum 50 ● Funcționalitățile de criptare VPN IPSec ale sistemului trebuie să fie accelerate hardware.
Condiții alimentare ● Alimentare curent alternativ 100-240V, 50-60 Hz, cu sursă externă
Mediu de funcționare ● Temperatura: 0 to 40°C ● Umiditate: 10 to 85% (umiditate relativă)
Certificare ISO ● Certificat ISO 9001 sau echivalent pentru producător
Accesorii ● 1 X cablu consolă ● 1 X cablu de alimentare energie electrică tip schuko conform standardelor românești ● Documentație cu manual de utilizare și configurare tipărit ● Documentație cu manual de utilizare și configurare în format electronic pe mediu optic (CD) ● 1 X kit de instalare cu toate cablurile de protecție (împământare), șuruburile, precum și alte accesorii necesare instalării și punerii în funcțiune incluse
Funcționalități sistem de operare
Funcționalități firewall ● Suport NAT, PAT, NAT traversal ● Statefull Firewall (routing/transparent) ● URL filtering
Funcționalități
VPN ● Suport IPSec, L2TP + IPSec, SSL VPN ● Criptare DES, 3DES, AES128, AES192, AES256;
Autentificare SHA-1/SHA-256, SHA2/SHA-384/SHA-512, MD5, 802.1x Authenticator
Funcționalități rețelistică și routare ● Suport pentru legături WAN (Internet) multiple ● Suport DHCP Client/Relay/Server, DHCPv6 ● Routare bazată pe politici ● Routare dinamică IPv4: RIPv1 RIPv2, OSPF, BGP v4,
Multicast (PIM), IS-IS ● Routare dinamică IPv6: RIPng, OSPFv3, multiprotocol BGP ● Suport VRRP, balansare cu împărțire de încărcare automată între două echipamente și Link Failure Control ● Suport VLAN Tagging (802.1Q) și IPv6 Data Link: VLAN-uri ce folosesc IEEE 802.1Q ● Routare între VLAN-uri ● Suport pentru servicii IPv6, QoS, FTP, AAA, SSHv2, DNS proxy multicast ● Multi-Link Aggregation - 802.3ad ● Posibilitate mapare (Binding) adrese IP - adrese MAC ● Posibilitatea de a exporta statistici despre trafic care să includă și informații despre aplicații, într-un format general acceptat (Netflow sau similar)
Funcționalități
QoS ● Limitare/garantare/prioritizare a benzii de trafic prin politici ● Traffic Shaping per aplicație și adresă IP cu posibilitatea de rezervare de bandă exclusivă pentru un tip de trafic marcat prioritar; Traffic shaping bazat pe clase ● Posibilitatea de a marca/prioritiza/limita banda în funcție de aplicație ● Suport pentru marcare și prioritizare trafic după DSCP și
ToS ● Limitarea cotei de trafic ● Funcție de clasificare a traficului înainte de criptare în tunele IPSec ● QoS class-based WFQ, Hierarchical queuing-QoS
Funcționalități de administrare ● Administrare prin interfața WEB (HTTP/HTTPS), Telnet,
Secure Command Shell (SSH) pentru IPv4 și IPv6, Linie de comandă (CLI) ● Utilizatori/Administratori cu drepturi configurabile ● Funcționalitate de descărcare/încărcare a configurației prin FTP, SCP, TFTP, USB Flash ● Politică de control al parolelor
Funcționalități de logare și monitorizare ● Interfața grafică pentru monitorizare în timp real ● Opțiune de păstrare/stocare a logurilor pe suportul local ● Suport SNMPv3 ● Monitorizarea tunelelor VPN
Funcționalități de autentificare a utilizatorilor ● Definire locală a utilizatorilor ● Integrare cu RADIUS/TACACS+ ● Suport Xauth prin RADIUS pentru IPSec VPN
Garanție ● Furnizorul va oferi garanție și suport pentru echipamentele sale timp de un an de zile, cu posibilitatea de a escalada problemele de funcționalitate hardware/software la producătorul echipamentelor.
-----
