# Anexa 9
STRUCTURA ȘI CODIFICAREA conturilor de evidență a titlurilor de stat Structura și codificarea conturilor de evidență a titlurilor de stat, în conformitate cu prevederile Regulilor Sistemului de depozitare și decontare a instrumentelor financiare - SaFIR, denumit în continuare Sistemul SaFIR, sunt următoarele:
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ A │ A │ A │ B │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
```
AAAA - reprezintă cod deținător cont și este identificat prin primele 4 caractere ale codului BIC.
B - reprezintă cod categorie cont: 0 pentru dețineri proprii; 1 pentru dețineri clienți cu cont individual și clienți cu cont global, alții decât cei menționați la categoria "2"; 2 pentru dețineri în contul intermediarilor secundari și al instituțiilor de credit cu cont în sistemul SaFIR care tranzacționează exclusiv în nume și pe cont propriu;
CCCCCCCCCCCCC - reprezintă cod client și identifică clientul în Registrul secundar al dealerului primar, format din 13 caractere alfanumerice alocate de dealerul primar.
Pentru clienții intermediari secundari și instituții de credit cu cont în Sistemul SaFIR care tranzacționează exclusiv în nume și pe cont propriu, primele 4 caractere din codul de client reprezintă în mod obligatoriu primele 4 caractere ale codului BIC al deținătorului respectiv.
Exemple:
- cont dealer primar nume propriu:
```
┌───┬───┬───┬───┬───┐
│ A │ A │ A │ A │ 0 │
└─┬─┴───┴───┴─┬─┴───┘
```
│ │ └─────┬─────┘ │ └──────────────────> primele 4 caractere din codul BIC al dealerului primar
- cont client individual al unui dealer primar, alții decât cei menționați la categoria "2":
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ A │ A │ A │ 1 │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │
└─┬─┴───┴───┴─┬─┴───┴─┬─┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴─┬─┘
```
│ │ │ │ └─────┬─────┘ └───┬───────────────────────────────────────────┘ │: └─────────────────:──────────> primele 4 caractere din codul:
BIC al dealerului primar:::──────────> 13 caractere alfanumerice alocate de dealerul primar
- cont global de clienți deschis la dealerul primar de un alt intermediar:
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ A │ A │ A │ 1 │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │ C │
└─┬─┴───┴───┴─┬─┴───┴─┬─┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴─┬─┘
```
│ │ │ │ └─────┬─────┘ └───┬───────────────────────────────────────────┘ │: └─────────────────:──────────> primele 4 caractere din codul:
BIC al dealerului primar:::──────────> 13 caractere alfanumerice alocate de dealerul primar
- cont client individual al unui dealer primar, intermediar secundar și/sau instituție de credit cu cont în Sistemul SaFIR care tranzacționează exclusiv în nume și pe cont propriu:
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ A │ A │ A │ 2 │ C │ C │ C │ C │
└─┬─┴───┴───┴─┬─┴───┴─┬─┴───┴───┴─┬─┘
```
│ │ │ │ └─────┬─────┘ └───┬───────┘ │: └────────────────────────────> primele 4 caractere din codul:
BIC al dealerului primar:::──────────> primele 4 caractere din codul BIC al clientului intermediar secundar și/sau instituție de credit care tranzacționează exclusiv în nume și pe cont propriu
