# Séries Temporais
Modelos de séries temporais

    ARIMA, GARCH, EGARCH, TGARCH – previsões de retornos ou volatilidade.
    VAR / SVAR / Bayesian VAR – analisar interações entre vários ativos ou variáveis macroeconômicas.
    Modelos de alta frequência (ex.: modelos de ponto de ocorrência) – para dados intradiários.


> Uma série temporal é um conjunto de observações ordenadas em ordem cronológica no tempo ou um processo estocástico desconhecido. Matematicamente: Y = Tdt + Szt + et.

covariacia x corrrelação

* Tendência (Tdt): Mudanças graduais no longo prazo (crescimento populacional).
* Sazonalidade (Szt): oscilações para cima e para baixo que sempre ocorrem em um determinado período (contas de luz mais altas no inverno).
* Resíduos (et): mostram os movimentos para cima e para baixo na série após a remoção da tendência ou do efeito sazonal (sequência de variáveis aleatórias).

(IMAGEM)

> As Séries temporais podem ser usadas para fazer previsões futuras, descrever o comportamento serial de um variável, analisar periodicidade, tendências ou até mesmo definir o processo gerador de uma série. Elas podem ser divididas em dois tipos:-
- Variáveis
- Univariadas = apenas uma variável muda ao longo do tempo
- Multivariadas = mais de uma variável muda ao longo do tempo

- Tempo
- Unidimensuiioaonsi somente a vria´vel tempom envolvio
- Multidimensioanis -> outras vria´vesi asspociadas ao tempo

### Conceitos Básicos 
> Processo Estocástico -> É uma coleção de variáveis aleatórias definidas no mesmo espaço de probabilidade (processo que gera uma série de variáveis). A descrição de um processo estocástico é feita por meio de uma distribuição de probabilidade conjunta (o que é muito complexo de fazer), então geralmente o descrevemos por meio das funções:
- $𝜇(𝑡)=𝐸{𝑍(𝑡)}$ -> Média
- $𝜎^2(𝑡)=𝑉𝑎𝑟{𝑍(𝑡)}$ -> Variância
- $𝛾(𝑡1,𝑡2)=𝐶𝑜𝑣{𝑍(𝑡1),𝑍(𝑡2)}$ -> Autocovariância

![Img1](https://github.com/user-attachments/assets/4f5af5b4-917b-4c5a-97ac-45166549dcbe)

> Ruído Branco -> é quando o erro de uma série temporal segue uma distribuição normal, ou seja, um processo puramente aleatório.
- E(Xt)=0
- Var(Xt)=𝜎2

> Passeio Aleatória (Random Walk) -> é a soma de pequenas flutuações estocásticas (tendência estocástica). Matematicamente: 𝑍𝑡 = 𝑍(𝑡−1) + et

(IMAGEM)

> Autocorrelação -> é a correlação de determinados períodos anteriores com o período atual, ou seja, o grau de dependência serial. Cada período desse tipo de correlação é chamado de defasagem e sua representação é feita pela Função de Autocorrelação (ACF) e pela Função de Autocorrelação Parcial (PAF), ambas comparando o valor presente com os valores passados da série. A diferença entre elas é que a CAF analisa tanto a correlação direta quanto a indireta, enquanto a PAF analisa apenas a correlação direta. Então, podemos dizer que a CAF vê a correlação direta do mês de janeiro com o de março e também a correlação indireta que o mês de janeiro teve com o de fevereiro, que também teve com o de março, enquanto a PAF apenas a correlação de janeiro com o de março. Essa análise é feita por ser a premissa essencial para a criação de previsões eficientes de uma série.

> Estacionariedade -> É quando uma série temporal apresenta todas as suas características estatísticas constantes ao longo do tempo, ou seja, não mudam de comportamento (inclinação e mudança de nível)

(IMAGEM)
 
 Tipos 
 - Estacionariedade Forte = também chamada de estacionariedade estrita, ocorre quando as distribuições unidimensionais são invariantes ao longo do tempo, ou seja, as distribuições individuais são as mesmas para todos os "ts". Portanto, a covariância depende apenas da distância entre as observações e não do momento específico em que ocorreram.
 - Estacionariedade Fraca = É quando as propriedades estatísticas são estáveis apenas na Média E(x) = U, Variância Var(x) = 𝜎² e na Covariância COV(X,X-n) = k, ou seja, estabilidade de segunda ordem. Na prática estacionariedade geralmente significa estacionariedade fraca porque muitos métodos dependem apenas de momentos de ordem 1 e 2.


















![plot](https://github.com/user-attachments/assets/6cde76a5-8419-4d3c-b32b-1630c27b36a5)

> Time series studies can be used for future predictions, description of serial behavior, and analysis of periodicity, trends, or even the process that generates the series. They are divided into two types:

- Univariate = only one variable changes over time
- Multivariate = more than one variable changes over time****

### Initial Concepts

> Stochastic Process -> is a collection of random variables defined in the same probability space (process generating a series of variables). The description of a stochastic process is done through a joint probability distribution (which is very complex to do), so we usually describe it through the functions:
- $𝜇(𝑡)=𝐸{𝑍(𝑡)}$ -> Average
- $𝜎^2(𝑡)=𝑉𝑎𝑟{𝑍(𝑡)}$ -> Variance 
- $𝛾(𝑡1,𝑡2)=𝐶𝑜𝑣{𝑍(𝑡1),𝑍(𝑡2)}$ -> Autocovariance

![estocastico](https://github.com/user-attachments/assets/d1a7faa1-0cad-46f2-bf2c-b369e13209c2)

> Stationarity -> is when a time series presents all its statistical characteristics constant over time

- Weak Stationarity = when the statistical properties are constant over time, E(x) = U, Var(x) = 𝜎², COV(X,X-n) = k (covariance between observations at different points in time depends on the specific time at which they occurred). In the literature, stationarity generally means weak stationarity.
- Strong Stationarity = also called strict stationarity, is when the joint probability function is invariant over time, that is, the individual distributions are the same for all "ts". Therefore, the covariance depends only on the distance between the observations and not on the specific time at which they occurred.

> Autocorrelation -> is the correlation of certain previous periods with the current period, that is, the degree of serial dependence. Each period of this type of correlation is called lag and its representation is made by the Autocorrelation Function (ACF) and the Partial Autocorrelation Function (PAF), both of which compare the present value with the past values ​​of the series. The difference between them is that the CAF analyzes both direct and indirect correlation, while the PAF only analyzes direct correlation. So we can say that the CAF sees the direct correlation of the month of January in March and also the indirect correlation that the month of January had in February, which also had in March, while the PAF only the correlation of January in March. This analysis is done because it is the essential assumption for creating efficient forecasts of a series.

![FAC](https://github.com/user-attachments/assets/4623a946-6427-4bc2-aadc-d8219df93db9)

![FACP](https://github.com/user-attachments/assets/9d577631-0da2-4101-b695-cfa4f35d2fc5)

> White Noise -> is when the error of a time series follows a normal distribution, that is, a purely random process.
- E(Xt)=0
- Var(Xt)=𝜎2

![Captura de tela 2025-01-30 132421](https://github.com/user-attachments/assets/0fbabff6-f692-48ad-bc84-bea27f7f30ae)

> Random Walk -> is the sum of small stochastic fluctuations (stochastic trend). Mathematically: 𝑍𝑡=𝑍(𝑡−1)+et

![Captura de tela 2025-01-30 132324](https://github.com/user-attachments/assets/bf7ce3a1-560b-45ad-9d1c-459cea90fe26)

> Transformation and Smoothing -> These are techniques that seek to make the series as close as possible to a normal distribution. Transforming the value of the variables or smoothing the trend and/or seasonality of the series. Among all the existing techniques we can mention:

1) Log Transformation
2) Exponential Transformation
3) Box-Cox Transformation
4) Exponential Moving Average Smoothing (EMA) - Short-term
5) Simple Moving Average Smoothing (SMA) - Long-term

> Differentiation -> Differentiation seeks to transform a non-stationary series into a stationary one, by means of the difference of two consecutive periods

![Sem Título-1](https://github.com/user-attachments/assets/390abc00-d4aa-41bf-be96-6ec3eeaf7684)

#### Univariate time series models:
Linear models:
- Autoregressive models (AR)
- Moving average models (MA)
- Autoregressive and moving average models (ARMA)
- Autoregressive integrated and moving average models (ARIMA)
- Long time dependency or long memory models (ARFIMA)
- Autoregressive integrated and moving average models with seasonality (SARIMA)

Nonlinear models:
- Autoregressive with threshold (TAR)
- Autoregressive with smooth transition (STAR)
- Markov regime switching (MSM)
- Autoregressive artificial neural networks (AR-ANN)

Structure:
- Autoregressive (AR): indicates that the variable is regressed on its previous values.
- Integrated (I): indicates that the data values ​​were replaced with the difference between their values ​​and the previous values ​​(differencing).
- Moving average (MA): Indicates that the regression error is a linear combination of the error terms of the past values.
- 
Coding: (p, d, q) Parameter d can only be an integer, if we were working with an ARFIMA Model, the parameter d can be fractional
- p = order of autoregression.
- d = degree of differentiation.
- q = order of the moving average.

> When we add seasonality, in addition to the Arima coding (p, d, q), we include the coding for Seasonality (P, D, Q). Then a SARIMA model is defined by: (p, d, q)(P, D, Q)
Examples:

- ARFIMA model: (1, 0.25, 1)
- ARIMA model: (2, 1, 1)
- AR model: (1, 0, 0)
- MA model (0, 0, 3)
- I model: (0, 2, 0)
- ARMA model: (4, 0, 1)
- SARIMA model: (1, 1, 2)(2, 0, 1)

Akaike's Information Criterion (AIC) and the Bayesian Information Criterion (BIC)
> In more advanced models, the autocorrelation and partial autocorrelation functions are not informative for defining the order of the models, so an information criterion is used. An information criterion is a way of finding the ideal number of parameters for a model. To understand it, keep in mind that, with each additional regressor, the sum of the residuals will not increase; it will often decrease. The reduction occurs at the cost of more regressors. To balance the reduction in errors and the increase in the number of regressors, the information criterion associates a penalty with this increase. Therefore, its equation has two parts: the first measures the quality of the model's fit to the data, while the second part is called the penalty function since it penalizes models with many parameters. Therefore, given all the combinations of models, we look for the one with the lowest AIC.







#### Testes Estatísticos

##### Teste de Kolmogorov-Smirnov
> Qualifica a máxima diferença absoluta entre a função de distribuição da amostra e a função de distribuição acumulada da distribuição de referência (geramente distribuição normal), ou seja, ele qualifica distância entre duas amostras (comparação entre elas).

- *H0: A amostra segue a distribuição de referência*
- *H1: A amostra não segue a distribuição de referência*

##### Teste de Anderson-Darling 
> Testa se uma função de distribuição acumulada f(x), pode ser candidata a ser um função de distribuição acumulada de uma amostra aleatória;

- *H0: A amostra tem distribuição de f(x)*
- *H1: A amostra não tem distribuição f(x)*

##### Teste de Shapiro Wilk 
> O teste Shapiro Wilk segue a seguinte equação descrita abaixo. Sendo que xi são os valores da amostra ordenados, no qual valores menores que W são evidências de que os dados são normais.

![Captura de tela 2024-07-04 191812](https://github.com/HenrySchall/Time-Series/assets/96027335/c9789639-2602-44bb-a9f3-491b92b65310)

> Já o termo b é determinado pela seguinte equação:

![Captura de tela 2024-07-04 192115](https://github.com/HenrySchall/Time-Series/assets/96027335/c2594f21-082f-4f6d-9293-66b45b0125fb)

> onde ai são constantes geradas pelas médias, variâncias e covariâncias das estatísticas de ordem de uma amostra de tamanho n de uma distribuição normal (tabela da normal).

Estatística de teste:
- *H0: A amostra segue uma distribuição normal (W-obtido < W-crítico)*
- *H1: A amostra não segue uma distribuição normal (W-obtido > W-crítico)*

![img46](https://github.com/HenrySchall/Time-Series/assets/96027335/64ca5aa1-d601-44b1-8d21-16ec79400211)

##### Teste de Jarque-Bera
> Verifica se os erros são um Ruído Branco, ou seja, seguem uma distribuição normal. O teste se baseia nos resíduos do método dos mínimos quadrados. Para sua realização o teste necessita dos cálculos da assimetria (skewness) e da curtose (kurtosis) da amostra, dado pela seguinte fórmula:
 
![Captura de tela 2024-07-04 193133](https://github.com/HenrySchall/Time-Series/assets/96027335/fe76cc80-fa40-46c8-8357-7e19e49339a5)

> onde n e o número de observações (ou graus de liberdade geral); S é aassimetria da amostra; e K é a curtose da amostra

![Captura de tela 2024-07-04 193243](https://github.com/HenrySchall/Time-Series/assets/96027335/b24d6ca3-6e20-44ed-a3d6-5004c3646bd6)

$\widehat{u3}$ e $\widehat{u4}$ são as estimativas do terceiro e quarto momentos, respectivamente; $\bar{x}$ a média da amostra, e $𝜎^2$ é a estimativa do segundo momento, a variância.

- *H0: resíduos são normalmente distribuídos*
- *H1: resíduos não são normalmente distribuídos*

#### Resumo:

|Teste|Quando usar|Prós|Contras|Cenários não indicados|
|---|---|---|---|---|
|Shapiro-Wilk|Pequenas amostras (sensível a pequenas desvios da normalidade)|Sensível a pequenas desvios da normalidade (adequado para amostras pequenas|Pode ser menos potente em amostras maiores|Dados com distribuição fortemente bimodal ou multimodal|
|Kolmogorov-Smirov|Amostras grandes (teste não paramétrico)|Não requer suposições sobre os parâmetros da distribuição (adequado para amostras grandes)|Menos sensível a pequenos desvios (menos potente em amostras pequenas)|Sensível a desvios nas caudas da distribuição|
|Anderson Darling|Verificação geral de normalidade|Sensibilidade a desvios em caudas e simetria (fornece estatística de teste e valores críticos)|Menos sensível a desvios pequenos|Não é recomendado para amostras muito pequenas|
|Jaque-Bera|Verificação geral de normalidade em amostras grandes|Combina informações sobre simetria e curtose (adequado para amostras grandes)|Menos sensível a desvios pequenos|Sensível a desvios nas caudas da distribuição| 
  
##### Teste de Aderência
> Este teste é utilizado quando deseja-se validar a hipótese que um conjunto de dados é gerado por uma determinada distribuição de probabilidade.

- *H0: segue o modelo proposto*
- *H1: não segue o modelo proposto*
  
##### Teste de Indepedência
> Este teste é utilizado quando deseja-se validar a hipótese de independência entre duas variáveis aleatórias. Se por exemplo, existe a funlçao de probabilidade conjunta das duas variáveis aleatórias, pode-se verificar se para todos os possíveis valores das variávies, o produto das probabilidades margianis é igual à probabilidade conjunto.

- *H0: as variáveis aleatórias são independentes*
- *H1: as variáveis aleatórias não são independentes*

##### Teste de Homogeneidade
> Esse teste é utilizado quando deseja-se validar a hipótese de que uma variável aleatória apresenta comportamento similar, ou homogêneo, em relação às suas várias subpopulações. Este teste apresenta a mesma mecânica do Teste de Independência, mas uma distinção importante se refere à forma como as amostras são coletadas. No Teste de homogeneidade fixa-se o tamanho da amostra em cada uma das subpopulações e, então, seleciona-se uma amostra de cada uma delas.

- *H0: As subpopulações das variáveis aleatórias são homogêneas*
- *H1: As subpopulações das variáveis aleatórias não são homogêneas*

#### Coeficientes de Correlação
> Os coeficientes de correlação verificam a existência e o grau de associação entre dois conjuntos de dados.

##### Coeficiente Pearson 
> Estabelecer o nível de relação linear entre duas variáveis. Em outras palavras, mede em grau e o sentido (crescente/decrescente) da associação linear entre duas variáveis. Ele sempre estará entre −1,00 e +1,00, tendo o sinal a função de indicar a direção do movimento, ou seja, positivo (relação direta) e negativa (relação inversa) e o valor do coeficiente, a função de indicar a força da correlação, onde nos intervalos:
> - (+0,90; +1,00) ou (−1,00; −0,90) = correlação muito forte
> - (+0,60; +0,90) ou (−0,90; −0,60) = correlação forte
> - (+0,30; +0,60) ou (−0,60; −0,30) = correlação moderada
> - (0,00; +0,30) ou (−0,30; 0,00) = correlação fraca
>
> Graficamente:

![3](https://github.com/HenrySchall/Time-Series/assets/96027335/5391579e-90f0-4ed2-92a0-b95c6068591f)

> Sua equação é definida pela seguinte fórmula:

![1](https://github.com/HenrySchall/Time-Series/assets/96027335/8f4dd7f6-e82b-4bf0-a06d-58400ede1060)

> Lembrando que o coeficiente de correlação populacional é dado por:

![2](https://github.com/HenrySchall/Time-Series/assets/96027335/6e39a2b7-4bfd-4d30-987e-bca3e8c5c8d8)

> Exemplo: A tabela abaixo apresenta 15 observações, com o tempo de entrega (em minutos) e a distância de entrega de um TelePizza.

|Tempo|Distância|
|---|---|
|40|688|
|21|215|
|14|255|
|20|462|
|24|448|
|29|776|
|15|200|
|19|132|
|10|36|
|35|770|
|18|140|
|52|810|
|19|450|
|20|635|
|11|150|

> Calculando os valores obtemos o seguinte resultado:

![4](https://github.com/HenrySchall/Time-Series/assets/96027335/a224016f-5d0a-4b84-ac79-6b8f5dae6ae1)

> Conclui-se que existe uma relação linear forte e positiva entre as variáveis. Todavia o coeficiente de correlação de Pearson é apenas uma estimativa do coeficiente de correlação populacional, pois é calculado com base em uma amostra aleatória de 𝑛 pares de dados. Sendo assim a amostra observada pode apresentar correlação, mas a população não, neste caso, tem-se um problema de inferência, pois o fato de r≠0 não é garantia de 𝜌≠0. Para resolver esse problema, utiliza-se da estatística de teste T-student, definido pela equação abaixo, para verificar se realmente existe correlação linear entre as variáveis:

![5](https://github.com/HenrySchall/Time-Series/assets/96027335/84310f44-b3d8-477d-9e71-1ec81dcbb21a)

> Onde 𝑡 segue uma distribuição 𝑡−𝑆𝑡𝑢𝑑𝑒𝑛𝑡 com 𝑛−2 graus de liberdade e regido pelas seguintes hipóteses:

- *H0: A correlação entre as variáveis é zero (𝜌 = 0)*
- *H1: A correlação entre as variáveis não é zero (𝜌 ≠ 0)*

![6](https://github.com/HenrySchall/Time-Series/assets/96027335/ccc5a428-cea3-4a8f-a773-c6b454b87f28)

> A partir da estatística 𝑡 com 13 graus de liberdade, os pontos críticos são ±2,1604. Portanto, rejeita-se 𝐻𝑜 ao nível de significância de 5%. Sendo assim a correlação entre o tempo de entrega e a distância percorrida é diferente de zero, então, existe uma relação linear e positiva entre as variáveis da ordem de 𝑟 = 0,8216.

##### Coeficiente Spearman
> O coeficiente de correlação de Spearman, ou rho de Spearman, é uma medida não paramétrica da correlação (associação) entre duas variáveis ordinais. Ao contrário do coeficiente de correlação de Pearson, que mede a força e a direção da relação linear entre duas variáveis, o coeficiente de Spearman avalia a intensidade (o quão bem) é a relação entre duas variáveis. O coeficiente de correlação de Spearman (𝜌) é calculado utilizando a seguinte fórmula:

![20](https://github.com/HenrySchall/Time-Series/assets/96027335/65f56f8e-31b3-4d4f-a4d0-b7e692b2fd44)

#### Interpretação:
- ρ=1 indica uma perfeita correlação positiva.
- ρ=−1 indica uma perfeita correlação negativa.
- ρ=0 indica ausência de correlação.

> Exemplo: Dados os valores da tabela abaixo:

![9](https://github.com/HenrySchall/Time-Series/assets/96027335/68db17b8-2b31-41c9-b1d1-cf241b30ee55)

> Calculando os valores obtemos o seguinte resultado:

![12](https://github.com/HenrySchall/Time-Series/assets/96027335/1c332788-5570-48e1-8d17-2b3b36c61aff)
 
> Utilizando-se da mesma equação estatística do teste T-student. Teremos as seguintes hipóteses:

- *H0: A correlação entre as variáveis é zero*
- *H1: A correlação entre as variáveis não é zero*

> A partir da estatística 𝑡−𝑆𝑡𝑢𝑑𝑒𝑛𝑡 com 11 graus de liberdade, os pontos críticos são ±2,2010. Portanto, rejeita-se 𝐻𝑜 ao nível de significância de 5%. Sendo assim a correlação entre as variáveis 𝑋 e 𝑌 é diferente 
de zero, então, existe uma relação não-linear e negativa de ordem 𝑟= −0,9698. 

##### Coeficiente Kendall 
> O coeficiente de correlação de Kendall é uma medida estatística utilizada para avaliar a associação entre duas variáveis ordinais, exatamente igual ao coeficiente de correlação de Spearman, a difenreça é que ele mede a correlação de concordância, enquanto Spearman, mede a correlação de postos. Sendo particularmente útil quando as variáveis em questão não assumem necessariamente distribuições normais. O coeficiente de correlação de Kendall (τ) é definido pela seguinte fórmula:

![124](https://github.com/HenrySchall/Time-Series/assets/96027335/ac68ba9a-1c0d-4cab-a892-7d9ab87cc400)

> No qual, 𝑛 é o número de elementos aos quais atribui-se postos, 𝑆 é a soma da variável 𝑌 à direita que são superiores menos o número de postos à direita que são inferiores.

#### Interpretação:
- τ=1 indica uma perfeita concordância.
- τ=−1 indica uma perfeita discordância.
- τ=0 indica ausência de associação entre as variáveis.

> Para o cálculo do coeficiente de correlação por postos de Kendall ordena-se inicialmente uma das variáveis em ordem crescente de postos e o S correspondente a cada elemento será obtido fazendo o número de elementos 
cujo posto é superior ao que se está calculando menos o número de elementos cujo posto é inferior ao mesmo. Para verificar a significância do valor observado do coeficiente 𝜏 de Kendall, para 𝑛≤10 deve-se consultar a tabela abaixo.

![125](https://github.com/HenrySchall/Time-Series/assets/96027335/9a2f16b5-e667-4d3c-a8dd-01d3ed678409)

> Para 𝑛>10, pode utilizar a estatística de teste:

![128](https://github.com/HenrySchall/Time-Series/assets/96027335/275d3eda-ef7e-453a-86d1-a4918ef935ff)

> Exemplo: Dados os valores da tabela abaixo:



> Calculando os valores obtemos o seguinte resultado:



> Tendo as seguintes hipóteses:

- *H0: A correlação entre as variáveis é zero (𝜏=0)*
- *H1: A correlação entre as variáveis não é zero (𝜏≠0)*

>  A partir da estatística 𝑁𝑜𝑟𝑚𝑎𝑙 𝑝𝑎𝑑𝑟ã𝑜, os pontos críticos são ±1,96. Portanto, rejeita-se 𝐻𝑜 ao nível de significância de 5%. Sendo assim a correlação entre as variáveis 𝑋 e 𝑌 é diferente de zero, então, existe uma 
relação não-linear e negativa de ordem 𝜏=−0,7692.

*Observação: Pode-se fazer uma comparação entre coeficiente de correlação de Spearman e o coeficiente de correlação por postos de Kendall. Os valores numéricos não são iguais, quando calculados para os mesmos pares de postos, e não são comparáveis numericamente. Contudo, pelo fato de utilizarem a mesma quantidade de informação contida nos dados, ambos têm o mesmo poder de detectar a existência de associação na população, e rejeitarão a hipótese nula para um mesmo nível de significância.*


############################
### Holt-Winters Aditivo ###
############################

from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

# PremierPet
Produto = 4002
serie = df[df['Produto'] == Produto][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

# Ajusta o modelo
fit1 = ExponentialSmoothing(
    serie,
    trend='additive',
    damped_trend = False,
    seasonal='additive',
    seasonal_periods=12,
).fit()

forecast = fit1.forecast(12)
print(forecast)

# Valores Passados
fit1.fittedvalues.plot(style='--', color='red')
plt.show()

# Valores Futuros
fit = 12 # meses futuros
fit1.forecast(fit).plot(style='--', marker='o', color='black', legend=True)
plt.show()

# Agrupando tudo em um gráfico
forecast_h = 12  # meses futuros
forecast = fit1.forecast(forecast_h)

plt.plot(serie, label='Observado', color='blue')
plt.plot(fit1.fittedvalues, '--', label='Ajustado', color='red')
plt.plot(forecast, '--o', label='Previsão', color='black')
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.title(f'Previsão Holt-Winters - Produto {Produto}')
plt.legend()
plt.grid(True)
plt.show()

###################################
### Holt-Winters Multiplicativo ###
###################################

from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

# PremierPet
Produto = 4002
serie = df[df['Produto'] == Produto][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

# Ajusta o modelo
fit2 = ExponentialSmoothing(
    serie,
    trend='multiplicative',
    damped_trend = False
    seasonal='multiplicative',
    seasonal_periods=12,
).fit()

forecast = fit2.forecast(12)
print(forecast)

# Valores Passados
fit2.fittedvalues.plot(style='--', color='red')
plt.show()

# Valores Futuros
fit = 12 # meses futuros
fit2.forecast(fit).plot(style='--', marker='o', color='black', legend=True)
plt.show()

# Agrupando tudo em um gráfico
forecast_h = 12  # meses futuros
forecast = fit2.forecast(forecast_h)

plt.plot(serie, label='Observado', color='blue')
plt.plot(fit2.fittedvalues, '--', label='Ajustado', color='red')
plt.plot(forecast, '--o', label='Previsão', color='black')
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.title(f'Previsão Holt-Winters - Produto {Produto}')
plt.legend()
plt.grid(True)
plt.show()

##############################
### Média Móvel Simples 3M ###
##############################

import numpy as np

# PremierPet
Produto = 4001
serie = df[df['Produto'] == Produto][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

serie_MMS = serie['Quantidade'].rolling(3).mean()
print(serie_MMS)

# Plotando os resultados
plt.plot(serie['Quantidade'], label='Original', color='blue')
plt.plot(serie_MMS, label='Média Móvel Simples 3M', color='red')
plt.xlabel("Ano", fontsize=14)
plt.ylabel("Quantidade")
plt.title(f"Média Móvel Simples 3 Meses - Produto {Produto}")
plt.legend()
plt.grid(True)
plt.show()

################################
### Média Móvel Ponderada 3M ###
################################

import numpy as np

# PremierPet
Produto = 4001
serie = df[df['Produto'] == Produto][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

weights = np.array([0.1, 0.3, 0.6])
serie_MMP = serie['Quantidade'].rolling(window=3).apply(lambda x: np.dot(x, weights), raw=True)
print(serie_MMP)

# Plotando os resultados
plt.plot(serie['Quantidade'], label='Original', color='blue')
plt.plot(serie_MMP, label='Média Móvel Ponderada 3M', color='red')
plt.xlabel("Ano", fontsize=14)
plt.ylabel("Quantidade")
plt.title(f"Média Móvel Ponderada 3 Meses - Produto {Produto}")
plt.legend()
plt.grid(True)
plt.show()

################
### LightGBM ###
################

import lightgbm as lgb
from mlforecast import MLForecast
from mlforecast.lag_transforms import ExpandingMean, RollingMean
from mlforecast.target_transforms import Differences

# PremierPet
Produto = 4002
series = df[df['Produto'] == Produto][['Datetime', 'Quantidade']].copy()
series.set_index('Datetime', inplace=True)

series = series.reset_index().rename(columns={
    'Datetime': 'ds',
    'Quantidade': 'y'
})
series['unique_id'] = Produto

models = [lgb.LGBMRegressor(random_state=0, verbosity=-1)]

# Previsão com MLForecast
fcst = MLForecast(
    models=models,
    freq='D',
    lags=[7, 14],
    lag_transforms={
    1: [ExpandingMean()],
    7: [RollingMean(window_size=28)]
    },
    date_features=['dayofweek'],
    target_transforms=[Differences([1])],
)

# Ajuste do modelo
fcst.fit(series)

# Valores Observado
plt.plot(series['ds'], series['y'], label='Observado', color='blue')
plt.show()

# Previsão Valores Futuros
n = 12 # meses futuros
forecast = fcst.predict(n)
plt.plot(forecast['ds'], forecast['LGBMRegressor'], '--', label='Previsto', color='red')
plt.show()

# Previsão In-sample
train = series.iloc[:-12]  # últimos 12 meses como treino
test = series.iloc[-12:] # últimos 12 meses como teste

fcst.fit(train)
n = 36
predictions = fcst.predict(n) 
plt.plot(test['ds'], test['y'], label='Teste Observado', color='Green') # 12 meses à frente
plt.show()

# Plot
plt.figure(figsize=(12,6))
plt.plot(series['ds'], series['y'], label='Treino', color='blue')
plt.plot(test['ds'], test['y'], label='Teste', color='White', linestyle='--')
plt.plot(forecast['ds'], forecast['LGBMRegressor'], '--', label='Previsto', color='red')
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

####################
### AutoLightGBM ###
####################

import lightgbm as lgb
from mlforecast import MLForecast
from mlforecast.auto import AutoLightGBM, AutoXGBoost, AutoMLForecast
from mlforecast.target_transforms import Differences

###################
### AutoXGBoost ###
###################

import xgboost as xgb
from mlforecast import MLForecast
from mlforecast.auto import AutoLightGBM, AutoXGBoost, AutoMLForecast
from mlforecast.target_transforms import Differences

# PremierPet
url = "C:/Users/HenriqueSchall/OneDrive - Neo Digital Industries/nPlan-Data-Science/nPlan Forecast/Arquivos/Dados/PremieRPet/Dados_Tratados_pet.xlsx"
df = pd.read_excel(url, sheet_name="Faturamento_Historico")
print(df)

df = df.drop(columns=["Ano", "Mês_num", "Mês"])
df.info()
print(df)

Produto = 4002
series = df[df['Produto'] == Produto][['Datetime', 'Quantidade']].copy()
series.set_index('Datetime', inplace=True)

series = series.reset_index().rename(columns={
    'Datetime': 'ds',
    'Quantidade': 'y'
})
series['unique_id'] = Produto

fcst = MLForecast(
    models=AutoXGBoost(),
    freq='D',  # ajuste para a frequência da série ('D' = diária)
    lags=[24 * (i + 1) for i in range(7)],  # defasagens
    target_transforms=[Differences([24])]  # transforma a série, se necessário
)

# Treinamento do modelo
fcst.fit(series)

# Exemplo de previsão para 48 passos à frente
forecast = fcst.predict(48)

print(forecast.head())

#############################
### RandomForestRegressor ###
#############################

from sklearn.ensemble import RandomForestRegressor





