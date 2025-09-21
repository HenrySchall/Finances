# Machine Learning

##### Multi-Level Perceptron (MLP)

Onde:
- Camada de entrada (Imput Layer): Recebe os dados brutos
- Camadas ocultas (Hidden Layer): Faz as transformações intermediárias, combinando pesos e aplicando funções espécificas (não lineares).
- Camada de saída (Output Layer): Gera o resultado final

> A grande diferença entre a Regressão Linear Multipla, está na camada oculta (Hidden Layer), que é responsável por permitir a não linearidade, já que por meio da função de ativação, decide como a entrada de um neurônio será transformado na sua saída. Outra diferença é a combinação de entradas, gerando uma dinâmica entre elas, transformando em variáveis dinâmicas. Sem esses fatores, uma rede neural seria apenas uma combinação linear de entrada, sendo assim, mesmo com várias camadas ela faria uma simples regressão linear.

#### Equação Geral
$$\mathrm{Zj} = BJ + \sum_{i=1}^{n} Wi,j * Xi$$

Onde:
- W = Pesos
- B = Parâmetros
- X = Entradas
- Z = Função de Ativação ou Saídas das Camadas Ocultas, dada por y = $f(z)$
- j = Número de camadas ocultas
- i = Número de entradas

Tipos de funções de ativação: Lineares, Sigmoid, Tanh, ReLU, Leaky ReLU, Softmax.

#### Processo de retrocesso 

Deep Learning é uma subárea do aprendizado de máquina (Machine Learning), que utiliza-se de Redes Neurais Artificiais Profundas para aprender padrões complexos em dados. Todavia antes de aprofundar o conceito de Deep Learning, deve-se entender dois conceitos básicos: Regressão Linear Múltipla e Redes Neurais Artificiais.
