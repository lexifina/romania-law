# Anexa nr. 1
CORELAREA informațiilor din mesajul SWIFT (pacs. 008), necesare a fi comunicate de către participanți, pentru a se asigura decontarea automată și reconcilierea finală în relație cu Ministerul Finanțelor -
Trezoreria Statului în sistemul ReGIS
1.
ID01 = număr ordin de plată - obligatoriu conform schemei; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/PmtId/EndToEndId
2.
ID02 = data decontării/data mesajului - obligatoriu conform schemei; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/IntrBkSttlmDt
3.
ID03 = data debitării ordinului de plată - obligatoriu pentru TREZ (În situația în care informația lipsește sau este invalidă, va fi completată automat de Ministerul Finanțelor - Trezoreria Statului cu data decontării în sistemul ReGIS.); /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/AccptncDtTm
4.
ID04 = cod identificare fiscală plătitor - CIF (CF - cod înregistrare fiscală, CUI - cod unic de înregistrare, CNP - cod numeric personal, NIF - număr de identificare fiscală) - Identificatorul poate fi preluat din oricare din cele 2 elemente: -
Organisation - pentru persoane juridice; sau
-
Private - pentru persoane fizice.
Se va completa un singur identificator fiscal - obligatoriu pentru TREZ; /Document/FIToFICstmrCdtTrf/ CdtTrfTxInf/Dbtr/Id/OrgId/Othr/Id sau /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Id/PrvtId/Othr/Id
5.
ID05 = cont/IBAN plătitor (contul poate fi preluat indiferent de elementul prin care va fi transmis; se va completa doar una din variante, în funcție de tipul contului IBAN/non-IBAN), obligatoriu pentru TREZ; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAcct/Id/IBAN (pentru coduri IBAN) /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/ DbtrAcct/Id/Othr/Id (pentru coduri non-IBAN)
6.
ID06 = BIC banca plătitoare/expeditoare din România - obligatoriu conform schemei și/sau pentru TREZ; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/InstgAgt/FinInstnId/BICFI
7.
ID07 = BIC banca beneficiară/destinatară = TREZROBU - obligatoriu conform schemei și/sau pentru TREZ; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/InstdAgt/FinInstnId/BICFI
8.
ID08 = cod identificare fiscală beneficiar - CIF (CF - cod înregistrare fiscală, CUI - cod unic de înregistrare, CNP - cod numeric personal, NIF - număr de identificare fiscală) - Identificatorul poate fi preluat din oricare din cele 2 elemente: -
Organisation - pentru persoane juridice; sau
-
Private - pentru persoane fizice.
Se va completa un singur identificator fiscal - obligatoriu pentru TREZ, se va completa cu o valoare validă, conform algoritmului specific de validare; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Id/OrgId/Othr/Id /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Id/PrvtId/Othr/Id
9.
ID09 = IBAN beneficiar (TREZROBU are doar conturi în format IBAN.) - obligatoriu pentru TREZ, se va completa cu un IBAN valid, conform algoritmului specific de validare; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAcct/Id/IBAN
10.
ID10 = număr de evidență a plății (cod ANAF) - opțional pentru TREZ; atunci când se completează trebuie să fie codul de maximum 23 de caractere numerice alocat/generat de Agenția Națională de Administrare Fiscală/ANAF; dacă numărul de evidență a plății lipsește, câmpul nu se va completa/va rămâne gol; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/RmtInf/Strd/TaxRmt/RefNb
11.
ID11 = data emiterii ordinului de plată = data documentului - obligatoriu pentru TREZ; /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/RmtInf/Strd/TaxRmt/Dt
12.
ID 12 = explicații privind conținutul economic al operațiunii - opțional pentru TREZ; atunci când se completează, trebuie transmis conținutul introdus de client. /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/RmtInf/Strd/AddtlRmtInf
13.
ID13 = câmpul de explicații pentru retururile realizate peste 3 zile; se va completa astfel: /RETN/cod eroare potrivit standardelor SWIFT/MREF/referința mesajului inițial refuzat/valoarea UETR din mesajul inițial /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/RmtInf/Ustrd
