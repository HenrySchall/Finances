# Teoria do Portolio 
> Levando em conta a Hipótese dos Mercados Eficientes (HME), ou seja, aquela em que os preços refletem as informações disponíveis e apresentam grande sensibilidade a novas informações relevantes. O valor de um ativo é reflexo do consenso dos participantes com relação ao seu desempenho esperado, sendo assim, nenhum investidor é capaz de identificar ativos com preço em desequilíbrio e todos os investidores são racionais e, portanto,
têm aversão ao risco, optando sempre por investir em carteiras, e não em ativos individuais (diversificando parte do risco inerente à situação em que se coloca todo o dinheiro em um único ativo).
>  A teoria do Portfolio trata da composição de uma carteira ótimade ativos, tendo por objetivo maximizar a utilidade do investidor pela relação risco/retorno. Um único ativo, sofrerá todas as consequências de um mau
desempenho.Isso não ocorrerá com um investidor que aplicar em uma carteira diversificada de ativos

O objetivo do gestor financeiro é criar uma carteira eficiente,
que maximize o retorno para certo nível de risco ou minimize o
risco para determinado nível de retorno

![image](https://github.com/HenrySchall/Finance/assets/96027335/3af52f76-c600-46f1-9489-544b30fbfa77)

#### Value at Risk
O Value at Risk (VaR) é um modelo amplamente utilizado para avaliar o risco financeiro de uma carteira de investimentos, estimando a perda máxima esperada de um portfólio, para um período de tempo específico, para um nível de confiança específico. Existem três abordagens principais para calcular o VaR:

1) VaR Paramétrico (Delta-Normal) = Assume que os retornos dos ativos seguem uma distribuição normal, sendo assim utliza-se da média e do desvio-padrão dos retornos históricos para calcular o VaR.
   
3) VaR Histórico (Backtesting) = Baseia-se nos retornos históricos do portfólio, ou seja, ordena os retornos e encontra o percentil correspondente ao nível de confiança escolhido. Se o nível de confiança for 95%, o VaR será o retorno no 5º percentil dos dados históricos.

6) VaR de Simulação de Monte Carlo = Gera múltiplas simulações de retornos futuros usando processos estocásticos (ex: Modelo de Black-Scholes, GARCH), ou seja, calcula o VaR a partir da distribuição simulada de retornos.

#### CAPM (Capital Asset Pricing Model)
> É um modelo que determina uma taxa de retorno esperada, para um ativo ou de um portfólio de ativos, considerando um mercado em equilíbrio (perfeito), com o risco não diversificável (de mercado), via coeficiente beta ($\beta1$).

$Rn = Rf + \beta1 * (Rm - Rf)$

- Rn = Retorno esperado
- Rf = Risk Free (Ativo Livre de Risco)
- $\beta1$ = beta da empresa
- Rm = Risco de Mercado

> $\beta1$ É uma medida do risco sistemático de um ativo, isto é, a reação do retorno do ativo às reações na carteira de mercado. Determinado pela seguinte fórmula: 

$\beta = (Cov (Rn,Rm)/(σ^2 Rm)$

- $(Cov (Rn,Rm)$ -> Covariância dos retornos da ação com os retornos do mercado
- $(σ^2 Rm)$ -> Variância do mercado
  
Interpretação do Beta 
- B > 1 -> Agressivo
- B < 1 -> Defensivo
- B = 1 -> Neutro ou Beta do Mercado
- B < 0 -> Contrário ao Mercado
- B = 0 -> Ativo Livre de Risco
  
![foto_page-0001](https://github.com/HenrySchall/Finance/assets/96027335/6f11e3dd-7199-4cb8-902e-77f3fb7d54fc)

##### Índice de Sharpe (IT)
> Indica o prêmio de risco esperado ou observado por unidade de risco sistemático (medido pelo $\beta1$). Sendo assim quanto maior, maior o prêmio de risco, ou seja, melhor é.

$IS = Rn - Rf / \beta$ 

- Rn = Retorno esperado do Ativo n
- Rf = Retorno esperado do Ativo Livre de Risco)
- &\beta& =  Beta do ativo n
