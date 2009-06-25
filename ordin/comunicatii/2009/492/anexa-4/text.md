# Anexa 4
CONȚINUTUL ȘI STRUCTURA MĂRCII TEMPORALE
Nume Explicație detaliată Structura ASN1 Observații
A. Informații despre marca temporală propriu-zisă (TSTInfo)
Versiune
INTEGER
Politica
OID
Amprenta de marcat Hash-ul + algoritmul de hash messagelmprint
Număr serial unic
INTEGER
Momentul exact de timp al emiterii UTC, notație "zulu" GeneralizedTime
Precizie Secunde, milisecunde, microsecunde Accuracy opțional
Număr aleatoriu (Nonce)
INTEGER opțional
Numele furnizorului
GeneralName opțional
Extensii
Extensions opțional
B. Semnătura furnizorului (ContentInfo ce încapsulează o structură signedData)
Info semnătură Semnătura propriu-zisă (SignatureValue), însoțită de datele de identificare ale semnatarului (Signerldentifier) signerlnfo
Certificatul furnizorului
certs opțional
C. Statutul PKI (PKIStatusInfo)
Codul de status PKI
PKIStatus
Mesajul text PKI
PKIFreeText opțional
Informații despre eroarea PKI
PKIFailurelnfo opțional
