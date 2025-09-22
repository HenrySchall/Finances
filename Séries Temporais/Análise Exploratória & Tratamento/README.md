# Séries Suavizadas
> Uma série temporal é um conjunto de observações ordenadas em ordem cronológica no tempo ou um processo estocástico desconhecido. Matematicamente: Y = Tdt + Szt + et.

* Tendência (Tdt): Mudanças graduais no longo prazo (crescimento populacional).
* Sazonalidade (Szt): oscilações para cima e para baixo que sempre ocorrem em um determinado período (contas de luz mais altas no inverno).
* Resíduos (et): mostram os movimentos para cima e para baixo na série após a remoção da tendência ou do efeito sazonal (sequência de variáveis aleatórias).

> As Séries temporais podem ser usadas para fazer previsões futuras, descrever o comportamento serial de um variável, analisar periodicidade, tendências ou até mesmo definir o processo gerador de uma série. Elas podem ser divididas em dois tipos:

- Univariadas = apenas uma variável muda ao longo do tempo
- Multivariadas = mais de uma variável muda ao longo do tempo

### Conceitos Básicos 

> Processo Estocástico -> é uma coleção de variáveis aleatórias definidas no mesmo espaço de probabilidade (processo que gera uma série de variáveis). A descrição de um processo estocástico é feita por meio de uma distribuição de probabilidade conjunta (o que é muito complexo de fazer), então geralmente o descrevemos por meio das funções:
- $𝜇(𝑡)=𝐸{𝑍(𝑡)}$ -> Average
- $𝜎^2(𝑡)=𝑉𝑎𝑟{𝑍(𝑡)}$ -> Variance 
- $𝛾(𝑡1,𝑡2)=𝐶𝑜𝑣{𝑍(𝑡1),𝑍(𝑡2)}$ -> Autocovariance

![Img1](https://github.com/user-attachments/assets/4f5af5b4-917b-4c5a-97ac-45166549dcbe)

> Estacionariedade -> é quando uma série temporal apresenta todas as suas características estatísticas constantes ao longo do tempo

- Estacionariedade Fraca = quando as propriedades estatísticas são constantes ao longo do tempo, E(x) = U, Var(x) = 𝜎², COV(X,X-n) = k (a covariância entre observações em diferentes pontos no tempo depende do momento específico em que ocorreram). Na literatura, estacionariedade geralmente significa estacionariedade fraca.
- Estacionariedade Forte = também chamada de estacionariedade estrita, ocorre quando a função de probabilidade conjunta é invariante ao longo do tempo, ou seja, as distribuições individuais são as mesmas para todos os "ts". Portanto, a covariância depende apenas da distância entre as observações e não do momento específico em que ocorreram.

> Autocorrelação -> é a correlação de determinados períodos anteriores com o período atual, ou seja, o grau de dependência serial. Cada período desse tipo de correlação é chamado de defasagem e sua representação é feita pela Função de Autocorrelação (ACF) e pela Função de Autocorrelação Parcial (PAF), ambas comparando o valor presente com os valores passados da série. A diferença entre elas é que a CAF analisa tanto a correlação direta quanto a indireta, enquanto a PAF analisa apenas a correlação direta. Então, podemos dizer que a CAF vê a correlação direta do mês de janeiro com o de março e também a correlação indireta que o mês de janeiro teve com o de fevereiro, que também teve com o de março, enquanto a PAF apenas a correlação de janeiro com o de março. Essa análise é feita por ser a premissa essencial para a criação de previsões eficientes de uma série.

> Ruído Branco -> é quando o erro de uma série temporal segue uma distribuição normal, ou seja, um processo puramente aleatório.
- E(Xt)=0
- Var(Xt)=𝜎2

> Passeio Aleatória (Random Walk) -> é a soma de pequenas flutuações estocásticas (tendência estocástica). Matematicamente: 𝑍𝑡 = 𝑍(𝑡−1) + et

> Transformação e Suavização -> São técnicas que buscam tornar a série o mais próxima possível de uma distribuição normal. Transformando o valor das variáveis ou suavizando a tendência e/ou sazonalidade da série. Dentre todas as técnicas existentes, podemos citar:

1) Transformação Logarítmica
2) Transformação Exponencial
3) Transformação Box-Cox
4) Suavização Exponencial de Médias Móveis (MME) - Curto Prazo
5) Suavização Simples de Médias Móveis (MMS) - Longo Prazo

> Diferenciação -> A diferenciação busca transformar uma série não estacionária em estacionária, por meio da diferença de dois períodos consecutivos
### Métricas de desempenho
> São indicadores quantitativos ou qualitativos usados para medir, monitorar e avaliar a eficiência e a eficácia de um processo. Em Séries Temporais, podemos dizer que existem quatro tipos:

  1) Avalição após a ocorrência -> Ex: Faço uma previsão para 12 meses, daqui a 12 meses eu comparo o previsto com o valor real
  2) Comparação histórica -> Ex: Faz uma previsão em cima dos dados históricos passados e comparo os dados históricos com o previsto.
  3) Separação entre Treino e Teste (Técnica Hold-out)-> Ex: Você pega um parte dos dados históricos para treinar o modelo e um parte (teste) para medir a performace do modelo
  4) Separação entre Treino e Teste (Técnica Cross Validation) -> Nesse caso divide-se a base de dados em várias partes de treino e se preve o teste para cada uma delas, depois tira-se a soma dos erros médios de cada previsão e a média dos valores previstos. Ex: Divide dados mensais de Abril, Maio e Junho, para prever Julho, tendo a seguinte combinação: 

- Abril + Maio -> Junho (Mês 1 e 2, testo no mês 3)
- Maio + Junho -> Julho (Mês 2 e 3, testo no mês 4)

Cada etapa fornece um erro de previsão, então calcula-se a soma da média dos erros de todos os passos e a soma da média dos valores previstos. Não é muito utilizada em Séries Temporais, devido a autocorrelação serial (lags) que um período carrega para o outro, gerando possívelmente viés de estimação.

> Na maioria dos casos, opta-se pela técnica de separação entre Treino e Teste, como é esperado o modelo não vai acertar todasas previsões da série temporal, por isso para verificar a qualidade do modelo usa-se os Testes de Acurácia. Eles são responsáveis por fazerem a comparação entre os valores previstos e os valores reais observados, são métodos estatísticos usados para avaliar quão boas são as previsões feitas por um modelo. 

#### Tipos:
- ME = Erro Médio (Mean Error)
- R² = Coeficiente de Determinação (Coefficient of Determination)
- MAE = Erro Absoluto Médio (Mean Absolute Error)
- MSE = Erro Quadrático Médio (Mean Squared Error)
- RMSE = Raiz do Erro Quadrático Médio (Root Mean-Square Error)
- MAPE = Erro Percentual Absoluto Médio (Mean Absolute Percentual Error)
- WMAPE = Erro Percentual Absoluto Médio Ponderado (Weighted Mean Absolute Percentage Error)
- BIAS = Viés de Previsão (Forecast Bias)
