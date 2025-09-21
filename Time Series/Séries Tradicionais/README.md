# Séries Suavizadas
> As Séries Suavizadas são séries temporais que recebem métodos de suavização, para reduzir ruído (variações aleatórias e irregulares) e identificar padrões subjacentes, como tendência e sazonalidade, em dados temporais.

#### Tipos
- Médias Estáticas
  - Simples
  - Ponderada
- Médias Móveis Simples (MMS) 
  - Aditiva
  - Multiplicativa 
- Suavizações Exponenciais Simples (SES) ou Médias Móveis Exponenciais (MME)
  - Aditiva
  - Multiplicativa
  - Holt-Winters 
    - Aditivo
    - Multiplicativo
    - Amortecido (ETS)

### Regressão Linear Múltipla
> A Regressão Linear Múltipla ou Multilinear é usada para modelar a relação entre uma variável dependente (y) e duas ou mais variáveis independentes (X1, X2, Xn, ...).

#### Equação Geral
$Y = β0 + βX1 + β2X2 + βXn ... + e$

Onde: 
- Y = Variável prevista (dependente).
- $X1$, $X2$, $Xn$ = Variáveis explicativas (independentes)
- $β0$ = intercepto, valor de Y quando todos os X são zero
- $β0$, $βX1$, $β2X2$, $βXn$ = coeficientes que mostram o efeito de cada variável X sobre Y, mantendo as outras constantes.
- e = erro, parte que o modelo não explica.
