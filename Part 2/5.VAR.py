import yfinance as yf
# Essa função retorna em um DataFrame os preços de fechamento ajustados 
# das 4 ações no período
df = yf.download(['PETR4.SA', 'ABEV3.SA', 'MGLU3.SA', 'AMER3.SA'], 
              start = '2022-02-01', end = '2023-02-01')['Adj Close']


# Função do pandas para calcular os retornos diários
# dropna é para remover a primeira linha que vai ser nula
df = df.pct_change().dropna()

df.std()

# Para o calculo da volatilidade EWMA, vamos criar a função da seguinte forma 
#(lembrando que o lambda por padrão vai ser 0.94 que é o mais usado pelo mercado):

import numpy as np

# função para calcular a volatildiade ewma
def vol_ewma(serie, lbda = 0.94):
    # gera uma lista decrescente do número total de elementos menos um até 0
    i = np.arange(len(serie)-1, -1, -1)
    
    # aplicação da formula para gerar a variância
    variancia = ((1 - lbda) * lbda ** i * serie ** 2).sum()
    
    # calcula a raiz da variância 
    vol = np.sqrt(variancia)
    return vol

    df.apply(vol_ewma)