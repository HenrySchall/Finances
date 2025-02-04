import string as string
import random as random
import radian as rd
import pandas as pd
import numpy as np
import seaborn as sns
import yfinance as yf
import matplotlib.pyplot as plt
import requests
import math

##################
### Dividendos ###
##################

dados_yf = yf.Ticker("CMIG4.SA").history(period="max")

dados_yf

ticker = "CMIG4"

url = "https://www.fundamentus.com.br/proventos.php?papel=" + ticker + "tipo=2

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.365 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36", 
           "X-Requested-With": "XMLHttpRequest"}
r = requests.get(url, headers)

dados_fundamentus = pd.read_html(r.text, decimal = ",", thousands="."[0])
dados_fundamentus

import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL do site Suno com a tabela de dividendos
url = "https://www.suno.com.br/acoes/VALE3/#dividendos/"  # Exemplo com VALE3

# Faz a requisição e obtém o conteúdo da página
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar a tabela de dividendos
tabela_dividendos = soup.find("table", {"class": "table"})

# Criar lista para armazenar os dados
dividendos = []

# Percorrer as linhas da tabela (exceto a linha de cabeçalho)
for linha in tabela_dividendos.find_all("tr")[1:]:
    colunas = linha.find_all("td")
    if len(colunas) > 1:
        Data com = colunas[0].text.strip()
        Pagamento = colunas[1].text.strip()
        Cotação = colunas[2].text.strip()
        Valor (R$) = colunas[3].text.strip()
        Yield (%) = colunas[4].text.strip()
        
        # Armazenar dados na lista
        dividendos.append([Data com, Pagamento,  Cotação,  Valor (R$),  Yield (%)])

# Converter em DataFrame
df_dividendos = pd.DataFrame(dividendos, columns=["Data com", "Pagamento", "Cotação", "Valor (R$)", "Yield (%)"])

# Exibir a tabela de dividendos
print(df_dividendos)

