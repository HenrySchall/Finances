# Redes Neurais
> Redes neurais são um conjunto de neurônios interligados por um processo de sinapse, responsáveis por transmitir informações ao longo de toda cadeia cerebral humana. Já as Redes Neurais Artificiais são modelos inspirados no funcionamento do cérebro humano, inventados na década de 1950, mas que foram deixadas de lado durante décadas porque a baixa capacidade computacional existente, fazia com que suas aplicações fossem muito limitadas. Isso mudou no início da década de 1990, quando o avanço tecnológico finalmente alcançou o ponto em que as Redes Neurais Artificiais passaram a ter valor prático. Basicamente uma Rede Neural Artificial é composta de um neurônio que recebe entradas (valores) e transmite eles ao longo de uma cadeia de neurônios, produzindo saídas com os valores fornecidos.

<img width="1450" height="650" alt="userlmn_0157c514bb2bdb1351c7356e0380af4c" src="https://github.com/user-attachments/assets/fb6210d6-6e31-4045-9c28-646d698d4347" />
Fonte: Asimov Institute

> Uma Rede Neural Artificial é defnida pela sua topologia (Estrutra de nós e camadas) e pela sua arquitetura, que é o modo como a rede funciona

### Tipos de Arquiteturas
- Redes Feedforward (FNN) = Fluxo unidirecional da informação (entrada → camadas ocultas → saída).
- Redes Recorrentes (RNN) = Possuem conexões que “retornam” para camadas anteriores (processo de backpropagation), permitindo memória temporal
- Redes Convolucionais (CNN)
- Redes Autoencoders
- Redes Generativas
- Redes de Atenção e Transformers
- Redes Neurais Gráficas (GNN)
- Redes Híbridas e Avançadas

### Tipos de Redes Neurais Artificiais

#### Legenda 

<img width="1324" height="848" alt="userlmn_04acb6fd5de4492f72726877bdb072de" src="https://github.com/user-attachments/assets/ba354710-0118-4c1d-953b-23834024420c" />
Fonte: Asimov Institute

#### 1) Redes Feedforward

- Perceptron (P)
- Feed Forward Network (FFN)
- Radial Basis Network (RBF)

##### Perceptron (P)

##### Feed Forward Network (FFN)

##### Radial Basis Network (RBF)

> São o tipo mais básico, onde a informação de entrada flui em sequência linear até a saída. Em cada neurônio ocorre uma operação matemática linear do tipo Wx + b, onde x é o valor do dado de entrada, e W e b são os parâmetros peso e bias do neurônio. O resultado dessas operações pode passar por uma função de ativação antes de passar para a camada adiante; no caso específico de funções de ativação com base radial (aquelas que determinam a distância do resultado a um ponto de origem), por questão meramente histórica, a rede correspondente é chamada de rede de base radial. As conexões entre os neurônios representam a passagem de informação de um neurônio para o próximo. Um neurônio que recebe mais de uma conexão de entrada soma estes valores antes de aplicar a equação linear pela qual é responsável. Esta rede neural pode ter várias camadas escondidas entre a camada de entrada e a de saída, por isso também costuma ser chamada de rede neural profunda. FFNs são capazes de modelar vários problemas onde os dados de entrada têm um impacto atemporal nos dados de saída. Um exemplo é usar informações de um exame de sangue para determinar a presença de uma doença.

<p align="center">
  <img width="375" height="110" alt="userlmn_79d5da35c78f64872a041aaef54e014a" src="https://github.com/user-attachments/assets/cb7b8b0b-7596-4a1e-a1ec-49a0e9490e1f"/>
</p>
Fonte: Asimov Institute

#### 2) Redes Recorrentes
- RNN (Recurrent Neural Network)
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)

##### Recurrent Neural Network (RNN)
> São projetadas para lidar com dados sequenciais ou temporais. Diferente de redes neurais tradicionais (Feed Forward), que processam cada entrada de forma independente, as RNNs possuem uma memória interna, permitindo que informações sejam passadas de um período para outro ao processar uma nova entrada (dependência temporal). O grande problema dessa arquitetura está na dependência de longo prazo, causada pelo desaparecimento ou exploção dos gradientes, ou seja, a saída em um certo ponto depende de informações que ocorreram muito tempo antes na sequência (esquecimento neural).

<p align="center">
  <img width="230" height="179" alt="userlmn_79d5da35c78f64872a041aaef54e014a" src="https://github.com/user-attachments/assets/1dc5077b-a66e-470f-8c71-3422da7ae5bc"/>
</p>
Fonte: Asimov Institute

##### Long short-term memory (LSTM)

> As redes long short-term memory (memória de curto-prazo longa), foram desenvolvidas para resolver o problema de dependência de longo prazo das redes neurais recorrentes. Em redes de arquitetura RNNs, existe um vetor das derivadas parciais, chamado gradiente, que tem o objetivo de mostra como a função de perda muda em relação aos parâmetros da rede (pesos), dizendo qual a direção e intensidade em que devemos ajustar os pesos para reduzir o erro, em resumo ele nos diz como os pesos da rede devem ser ajustados (medida de ajuste). Acontece que como as RNNs são redes bidirecionais, ou seja, possuem conexões que “retornam” para camadas anteriores, quando se realiza o processo de backpropagation (retropropagação do erro), que é o processo fundamental para treinar redes neurais, ajustando os pesos de forma iterativa para minimizar o erro entre as previsões da rede e os valores desejados, as camadas mais próximas da entradas (profundas), terão seus pesos não atualizados ou serão atualizados lentamente, causando esquecimento neural ou desaparecimento do gradiente. Por isso as LSTM utilizam-se da chamada camada oculta.

<p align="center">
  <img width="226" height="177" alt="userlmn_a9c1677509e9265d5e2b7819c007cb3f" src="https://github.com/user-attachments/assets/4e4ce37d-4ee7-47d8-a7dc-64c249e76254"/>
</p>
Fonte: Asimov Institute

#### 4) Gated recurrent network (GRU)

> As redes neurais com unidades recorrentes com portão são uma variação das LSTMs. O portão de entrada e saída é substituído por um portão de atualização, que é responsável por controlar quanto de informação reter e quanto atualizar. No lugar do portão de esquecimento temos um portão de reset, que funciona de forma análoga mas cuja localização na estrutura é diferente. As GRUs costumam ter aplicação similar às das LSTMs, mas são mais rápidas e fáceis de treinar. Entretanto, seu desempenho pode ser um pouco menos expressivo.

<p align="center">
  <img width="239" height="182" alt="userlmn_a5ce4924f6fb1aea43673692ed1fba42" src="https://github.com/user-attachments/assets/d59faae4-f0ed-453a-bb35-49ad9a5bf114"/>
</p>
Fonte: Asimov Institute

#### 5) Auto-encoder (AE)

> Os auto-encoders são projetados para representar a informação de entrada em um espaço dimensional menor. Por isso, a camada escondida central dessa rede, que representa esse espaço, deve ter menos neurônios que a camada de entrada. A camada de saída é uma cópia da informação de entrada, de forma que, durante o treinamento, os auto-encoders aprendem a representar a informação original em menos espaço, mas com informação suficiente para reconstruir os dados originais. A primeira metade da rede, que comprime a informação, é chamada de encoder, e a segunda de decoder. Os auto-encoders podem ser usados tanto para compactar dados para armazenamento e/ou transmissão, quanto para que representar os dados em forma reduzida para que, por exemplo, outra rede neural especializada em uma tarefa específica possa utilizá-los.

<p align="center">
  <img width="173" height="234" alt="userlmn_d72e5126078fda173c524d1980839a06" src="https://github.com/user-attachments/assets/3940cb46-1a53-48ab-bdad-827a8e553f6d"/>
</p>
Fonte: Asimov Institute

#### 6) Variational auto-encoder (VAE)
> O auto-encoder variacional é similar ao auto-encoder apresentado acima, com a diferença de que sua tarefa não é representar os dados originais em um espaço dimensional compactado, mas sim como distribuições probabilísticas. Como essa rede também é treinada para reconstruir os dados originais, essas distribuições costumam ser boas formas de representar a natureza das variáveis de entrada. Por essas características, os VAEs são utilizados para realizar o treinamento e a inferência em problemas de natureza probabilística.

<p align="center">
  <img width="170" height="225" alt="userlmn_b4e11101910da85eda70baf097d459c2" src="https://github.com/user-attachments/assets/c8b7bd49-b2c3-4947-b432-06f02aeb2656" />
</p>
Fonte: Asimov Institute

#### 7) Denoising auto-encoder (DAE)

> São auto-encoders cujos dados de entrada são os dados originais adicionados de um ruído. Dessa forma, a rede aprende a capturar informações de uma perspectiva mais ampla, já que em uma escala menor, os dados vão sempre apresentar um ruído de natureza inconstante. Uma aplicação óbvia dos DAE é limpar dados que contêm ruído por natureza, como por exemplo aumentar a resolução de vídeos antigos.

<p align="center">
  <img width="168" height="231" alt="userlmn_c0b260318ff0f4d70df418c026f3d5d8" src="https://github.com/user-attachments/assets/489aa00c-c9ff-4a99-abf7-e687a4d24f9a" />
</p>
Fonte: Asimov Institute

#### 8) Sparse auto-encoder (SAE)

> O auto-encoder esparso faz o oposto que o auto-encoder tradicional. Ao invés de representar os dados originais em um espaço dimensional menor, ele o faz em um espaço dimensional maior. O objetivo de SAEs é descobrir novos features menores eventualmente contidos no dataset original mas escondidos nas inter-relações entre os features presentes.

<p align="center">
  <img width="168" height="229" alt="userlmn_d0d39c8859daf3d805d132f0ddcc4d06" src="https://github.com/user-attachments/assets/774dab4d-f364-4438-9a6b-925024ed5323" />
</p>
Fonte: Asimov Institute

#### 9) Markov chain (MC)

> Apesar de nem sempre serem consideradas redes neurais, as cadeias de Markov podem ser representadas de forma similar, e são precursoras de outras redes. O objetivo das cadeias de Markov é responder a uma pergunta do tipo: dada a presença de um dado em determinado nodo, qual a probabilidade de este dado passar para outro nodo? As cadeias de Markov não contêm memória, de forma que o estado seguinte depende exclusivamente do estado atual, e não de seus antecessores. Cadeias de Markov são utilizadas, por exemplo, para representar a probabilidade de mutação de um aminoácido durante a evolução, o que é muito importante na área de biologia evolutiva para determinar o grau de parentesco entre as espécies.

<p align="center">
  <img width="228" height="236" alt="userlmn_28d1f3575b3f72be664fce07822d9d3d" src="https://github.com/user-attachments/assets/40053cd1-02d0-4552-a9c4-d2604a0b8c45" />
</p>
Fonte: Asimov Institute

#### 10) Hopfield network (HN)

> A rede de Hopfield tem estrutura similar às cadeias de Markov, mas seu funcionamento é diferente. Primeiro, todos os neurônios são conectados entre si, o que não é requisito na estrutura anterior. Segundo, os neurônios têm todas as funções das camadas de uma rede neural, funcionando como entrada no início, camada escondida durante o treinamento, e saída ao final. A rede é treinada para que seu estado convirja para um estado estável de interesse. Devido à sua característica prática, ela também é chamada de memória associativa, já que é capaz de se “lembrar” do estado de interesse recebendo como entrada um estado similar. Assim, ela pode ser usada para reconstruir informações completas quando, por exemplo, apenas metade da informação está disponível.

<p align="center">
  <img width="231" height="234" alt="userlmn_f813e172d1728b56b239c4aadda5f1fb" src="https://github.com/user-attachments/assets/ee5bdb68-8193-4a75-b7cc-a8ed32fd4d2b" />
</p>
Fonte: Asimov Institute

#### 11) Boltzmann machine (BM)

> A máquina de Boltzmann é similar às HNs, com a diferença de que alguns neurônios são explicitamente designados como de entrada (se tornando de saída ao final do treinamento), e outros como escondidos, o que lhe permite usar mais informação que aquela de entrada para atingir um estado estável. BMs podem ser usadas por exemplo para regular o piloto automático de um avião, onde os dados de entrada são os sinais de vários sensores. Perturbações ambientais são captadas por esses sensores, o que deve provocar ajustes nas partes mecânicas da aeronave para que ela atinja um novo estado de equilíbrio.

<p align="center">
  <img width="227" height="239" alt="userlmn_71dc532cc40c8fda201394a2b5cb6553" src="https://github.com/user-attachments/assets/6cd85f03-89dc-4407-9324-de7563af421d" />
</p>
Fonte: Asimov Institute

#### 12) Restricted Boltzmann machine (RBM)

> A máquina de Boltzman restrita é uma forma não-circular da BM, onde não há inter-conexões entre os neurônios de entrada ou entre os neurônios escondidos. A principal vantagem vem no treinamento, já que elas podem ser treinadas de forma similar a uma FFN.As aplicações são as mesmas que aquelas das BMs, mas as RBMs costumam ser mais usadas por essa natureza restrita.

<p align="center">
  <img width="117" height="229" alt="userlmn_64ee0fe96a660d60f04ab43d93b97e5e" src="https://github.com/user-attachments/assets/192b3636-17a8-486d-9077-9e78b02dff29" />
</p>
Fonte: Asimov Institute

#### 13) Deep belief network (DBN)

> A rede de crença profunda é uma forma empilhada das RBMs ou de VAEs, onde cada camada tem a tarefa de codificar somente a camada imediatamente anterior. Esta rede treina de forma “gulosa” (greedy), ou seja, ela encontra a melhor solução local, que é considerada suficiente para a aplicação em questão, mas que não necessariamente representa a melhor solução global. Como parte da estrutura envolve representações probabilísticas dos dados, a rede pode ser usadas para gerar novos dados de saída, ou seja, novos estados de equilíbrio de um sistema.

<p align="center">
  <img width="410" height="232" alt="userlmn_e36a352b41c2b9a7a6afd0f474f77c1f" src="https://github.com/user-attachments/assets/d7c2c2ba-542a-482b-92cb-83974bd45ba2" />
</p>
Fonte: Asimov Institute

#### 14) Convolutional neural network (CNN) ou Deep convolutional network (DCN)

> A rede neural convolucional tem uma estrutura bem diferente daquelas apresentadas até aqui. Nas camadas de convolução, a informação passa por vários filtros (que na prática são matrizes numéricas) com a função de acentuar padrões regulares locais, ao mesmo tempo em que vão reduzindo a dimensão dos dados originais. Os resultados de vários filtros são sumarizados por operações de pooling. Na parte mais profunda das convoluções, espera-se que os dados num espaço dimensional reduzido contenham informação suficiente sobre esses padrões locais para atribuir um valor semântico ao dado original. Esses dados passam então por uma estrutura de FFN clássica para a tarefa de classificação. Por essas características, a aplicação mais comum das CNNs é na classificação de imagens; os filtros acentuam atributos dos objetos necessários à sua correta classificação. Uma CNN especializada em classificar rostos, por exemplo, nas primeiras camadas reconhece contornos, curvas e bordas; mais adiante, usa essa informação para reconhecer boca, olhos, orelha e nariz; e no final, reconhece o rosto inteiro. Além de imagens, qualquer informação com regularidade local pode se beneficiar do uso de CNNs, como áudio por exemplo.

<p align="center">
  <img width="468" height="288" alt="userlmn_308b154576a39321779c8cbf2237b707" src="https://github.com/user-attachments/assets/d188aedb-010f-4659-9d5b-71d0516b0736" />
</p>
Fonte: Asimov Institute

#### 15) Deconvolutional networks (DN)

> A rede deconvolucional é, como o nome sugere, uma rede convolucional invertida. A partir de dados em um espaço dimensional reduzido, elas são capazes de “inflar” a informação para o espaço dimensional original. Uma aplicação possível de DNs é, por exemplo, a geração de novas imagens. Imagine alimentar a rede com dados convolucionados para que ela gere novos rostos.

<p align="center">
  <img width="286" height="289" alt="userlmn_789cc324a82b7bdcb16061f935b64fb4" src="https://github.com/user-attachments/assets/8f047f3c-ee6e-4722-b285-680c41f50fe0"/>
</p>
Fonte: Asimov Institute

#### 16) Deep convolutional inverse graphics network (DCIGN)

> A rede profunda de gráfico inverso convolucional nada mais é que uma VAE que possui uma CNN como encoder e uma DN como decoder. Como ela aprende a representar a informação no espaço dimensional reduzido como uma distribuição probabilística, ela é capaz de gerar um dado “misto”, formado por dois dados que ela recebeu separadamente. Imagine, por exemplo, uma rede convolucional especializada em classificar rostos de duas etnias diferentes. A DCIGN poderia gerar um rosto de uma etnia mista. Em outras palavras, ela poderia responder à pergunta: como seria o filho de duas pessoas dessas etnias?

<p align="center">
  <img width="525" height="289" alt="userlmn_54dd07f58a2304242e68d78778f5e289" src="https://github.com/user-attachments/assets/81df65ce-cbd6-4862-9232-40f5e15fc969" />
</p>
Fonte: Asimov Institute

#### 17) Generative adversarial network (GAN)

> A rede adversarial generativa pode ser descrita como contendo internamente duas redes que funcionam em conjunto, de forma competitiva. A primeira rede – a parte generativa – é responsável por gerar conteúdo, sendo treinada na tarefa de recriar a informação original. A segunda rede – a parte adversarial – é responsável por julgar o conteúdo, comparando a criação da rede generativa com a informação original. Quando a rede adversarial julga que a informação gerada não pode se passar pela original, a rede generativa é forçada a melhorar seu desempenho, até conseguir enganar a outra. Isso faz com que as GANs tenham a capacidade de criar conteúdo inédito, já que a saída da rede foi produzida pela parte generativa e julgada aceitável pela parte adversarial. Isso pode ser considerada uma forma primitiva de criatividade, e por isso as GANs costumam ser citadas como artistas da inteligência artificial.

<p align="center">
  <img width="406" height="166" alt="userlmn_93ce3f6bd4dd9f2190abdf87c0c8cc28" src="https://github.com/user-attachments/assets/2fb24710-4f95-4aa4-86cc-9ce9a67985d8" />
</p>
Fonte: Asimov Institute

#### 18) Liquid state machine (LSM)

> A máquina em estado líquido é um tipo de rede neural com disparo. As funções de ativação são substituídas por uma função de limite, e cada neurônio tem também a função de memória. Dessa forma, quando o valor que o neurônio processa é atualizado, ele soma os valores que recebe como entrada ao valor que já possuía do processamento anterior, e “dispara” (ou seja, passa informação adiante) quando o referido limite é alcançado. Além disso, as conexões entre os neurônios são aleatórias. De certo modo, essa representação é mais parecida com o que acontece em alguns processos no cérebro do que a rede neural clássica. Por isso, as LSMs costumam ter aplicação nas áreas de reconhecimento de fala e visão computacional, por exemplo.

<p align="center">
  <img width="289" height="233" alt="userlmn_b61151de838f3ce6d03bf0fe39b79b1d" src="https://github.com/user-attachments/assets/ea16733b-bf43-48d4-b77d-60ff31bd58a3" />
</p>
Fonte: Asimov Institute

#### 19) Extreme learning machine (ELM)

> A máquina de aprendizagem extrema é nada mais que uma rede neural profunda com conexões aleatórias entre as camadas. Ela também pode ser pensada como uma LSM sem memória e sem ativação por disparo. A principal diferença, entretanto, é que essa rede não é treinada pelo mecanismo de backpropagation, mas sim em uma etapa única, usando o ajuste do menor quadrado. Isso faz com que ela seja menos expressiva, mas seu treinamento é muito mais rápido. ELMs podem ser aplicadas nos mesmos casos que as FFNs.

<p align="center">
  <img width="293" height="234" alt="userlmn_792b9f65ad36fdd7d1d06367ade8fa8f" src="https://github.com/user-attachments/assets/7075b742-6c64-4a3c-b1d8-d217871fa17e" />
</p>
Fonte: Asimov Institute

#### 20) Echo state network (ESN)

> A rede de estado de eco é uma rede neural recorrente com conexões aleatórias entre as camadas. A principal diferença, entretanto, também é relacionada ao método de treinamento, que não depende do mecanismo de backpropagation. Isso acabou, no momento de seu advento, aumentando a aplicabilidade da estrutura recorrente, já que, antes, as RNNs dificilmente eram usadas na prática, pois o treinamento costumava ser lento e nem sempre a convergência era garantida. Atualmente, os problemas práticos das RNNs são considerados resolvidos, mas as ESNs ainda encontram aplicação nas áreas que dependem de dados computacionais não-digitais, como microchips óticos, nano-osciladores mecânicos ou próteses maleáveis, os quais não têm a mesma precisão numérica que dados digitais.

<p align="center">
  <img width="289" height="231" alt="userlmn_5f35117b68c09516af1a06269367073e" src="https://github.com/user-attachments/assets/e70d311e-b449-470f-938e-7dc3e4e3e5ed" />
</p>
Fonte: Asimov Institute

#### 21 ) Deep residual network (DRN)

> A rede residual profunda é uma FFN com muitas camadas, e que possui conexões extras ligando camadas não subsequentes. Dessa forma, as camadas mais profundas não recebem somente a informação da camada imediatamente anterior, mas também de outras camadas anteriores. Por causa dessa estrutura, as DRNs podem aprender padrões tendo até 150 camadas de profundidade – FFNs costumam ser limitadas a 5. Mas alguns trabalhos comparam o desempenho dessa estrutura com aquele de RNNs, sendo portanto as DRNs chamadas de RNNs sem a construção explícita de tempo, ou ainda LSTMs sem portão. A aplicação é derivada das estruturas recorrentes que a DRN acaba emulando.

<p align="center">
  <img width="530" height="135" alt="userlmn_48eadaf11705b157ec00c0828b8da893" src="https://github.com/user-attachments/assets/08fa7bf7-31dd-40a4-b615-e8f37ccfbbf2" />
</p>
Fonte: Asimov Institute

#### 22) Neural Turing machine (NTM)

> A máquina neural de Turing é uma abstração da LSTM, que tenta explicar o que a LSTM faz separando o neurônio que atualiza os dados que passam pela rede de seu componente de memória. As células de memória agem como um banco de memória que a rede neural consegue ler e sobrescrever, característica responsável pelo nome dessa arquitetura: ela pode representar qualquer coisa que uma Máquina de Turing Universal pode representar. Em termos práticos, a NTM também pode ser pensada como uma LSTM, com a vantagem de que seu funcionamento é mais transparente.

<p align="center">
  <img width="322" height="232" alt="userlmn_c8728e5276fbf1e562cde5d2342cdf9d" src="https://github.com/user-attachments/assets/63607ebe-1f91-4a22-afdc-5065783b9c6f"  />
</p>
Fonte: Asimov Institute

#### 23) Differentiable neural computers (DNC)

> O computador neural diferenciável é uma NTM melhorada, com memória escalonável, inspirada pela forma com que o hipocampo armazena memória em humanos. Fazendo um paralelo com computadores, essa rede age como se a CPU fosse substituída por uma RNN, que aprende o que e quando ler da memória RAM. A memória pode ser redimensionada sem que a parte recorrente precise ser retreinada. A RNN pode determinar a similaridade dos dados de entrada aos valores contidos na memória, a relação temporal entre dois dados na memória, e se uma informação na memória foi atualizada recentemente. Os autores do trabalho que introduziu essa arquitetura demonstraram seu potencial em responder perguntas sobre dados estruturados complexos, como histórias geradas artificialmente, árvores familiares, e até um mapa de metrô.

<p align="center">
  <img width="400" height="300" alt="userlmn_8b330907a35e94af972efdcc4294ff3f" src="https://github.com/user-attachments/assets/6e57894c-5e51-4e74-9055-1d6e87485fd9" />
</p>
Fonte: Asimov Institute

#### 24) Capsule network (CapsNet)

> A rede cápsula contém conexões entre os neurônios que são representadas por pesos múltiplos. Assim, cada neurônio consegue passar mais informação adiante, como, por exemplo, não somente a informação relacionada a um feature, mas também a posição, cor ou orientação do feature. Essa característica multi-informacional faz com que a rede cápsula tenha comportamento similar às camadas de pooling geralmente usadas para resumir as informações geradas nas camadas de convolução. Essa arquitetura foi desenvolvida recentemente, buscando resolver algumas das deficiências das CNNs tradicionais, o que devem aumentar seu desempenho ou campo de aplicação original.

<p align="center">
  <img width="400" height="300" alt="userlmn_7b77df1b91a87f026b660b89787e9e5b" src="https://github.com/user-attachments/assets/56242db7-db4b-4c77-9b65-50bba6f4a8f4" />
</p>
Fonte: Asimov Institute

#### 25) Kohonen network (KN)

> A rede Kohonen também é chamada de mapa auto-organizável (self organizing map, SOM). Ela usa aprendizado competitivo para classificar os dados sem supervisão. Os dados de entrada são comparados com os valores dos neurônios (inicializados aleatoriamente) através de uma métrica de similaridade, e as conexões que representam maior similaridade são fortalecidas. Os neurônios então se ajustam para representar os dados originais de forma ainda mais similar, “arrastando” junto os neurônios em sua proximidade. Assim, ao final do treinamento, os dados originais podem ser classificados em clusters de similaridade na forma de um mapa definido pelos neurônios da rede. Os SOMs são capazes de organizar dados para que os clusters formados possam ser explorados posteriormente. Por exemplo, eles podem indicar se um equipamento complexo está funcionando corretamente a partir das medições de sensores embutidos.

<p align="center">
  <img width="250" height="200" alt="userlmn_5f698b7d91083a4496b1585170e597cf" src="https://github.com/user-attachments/assets/18a8a190-2af0-4a6c-82d9-b91ffa540cc0" />
</p>
Fonte: Asimov Institute

#### 26) Attention networks (AN)

> A rede de atenção é uma rede que usa a arquitetura chamada de transformer. A estrutura é bastante complexa, mas basicamente, o que essa rede faz é manter uma memória, cujo acesso é mediado pelo mecanismo de atenção, que define o grau de importância que cada informação da memória vai receber a cada passo. As ANs podem ser usadas em substituição às RNNs e redes derivadas, com a principal vantagem de que elas conseguem eliminar o componente temporal do processamento, o que permite paralelização e assim, treinamento mais rápido. As ANs têm encontrado ampla aplicação na área de processamento de linguagem natural. Um dos modelos recentes mais bem-sucedidos, o BERT, faz uso dessa estrutura para produzir codificações dos dados com valor semântico suficiente para realizar tarefas complexas como classificar documentos, responder perguntas, identificar parafraseamento e até sarcasmo.

<p align="center">
  <img width="400" height="300" alt="userlmn_3bb7111163681644902d0f0914c4f67a" src="https://github.com/user-attachments/assets/ff1e447e-1913-4855-9c85-a30a633d5b5d" />
</p>
Fonte: Asimov Institute

### Referências Biográficas:
- Neural Networks and Deep Learning: A Textbook, by Charu C Aggarwal
- Deep Learning (Adaptive Computation and Machine Learning series),by Ian Goodfellow (Author), Yoshua Bengio (Author), Aaron Courville
- https://www.asimovinstitute.org/neural-network-zoo/
