########################
### Install Packages ###
########################

import subprocess
import sys

def install_packages(pacotes):
    for pacote in pacotes:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

# List of packages
packages_list = ["numpy", "pandas", "matplotlib", "scipy", "seaborn","statsmodels", "plotly", "gurobipy",
"yfinance", "scikit-learn", "pyomo", "panel", "hvplot", "holoviews", "datashader", "param", "colorcet"]

install_packages(packages_list)

#####################
### Load Packages ###
#####################

def load_packages(pack):
    import importlib
    import sys

    for packages_list, load in pack.items():
        try:
            modulo = importlib.import_module(packages_list)
            sys.modules[load] = modulo
            globals()[load] = modulo
        except ImportError:
            print(f"Erro ao importar o pacote: {packages_list}")

load_packages({"radian":"rd", "pyomo.environ":"pyo", "gurobipy":"gp", "pandas":"pd", "string":"string", "random":"random", "seaborn":"sns", "numpy":"np", "pandas":"pd",
"matplotlib.pyplot":"plt", "scipy":"stats", "matplotlib":"mpl", "seaborn.objects":"so", "plotly.express":"px", "matplotlib.pyplot":"plt", "math":"math","yfinance":"yf",
"datetime":"datetime", "panel":"pn", "hvplot":"hvplot", "holoviews":"hv", "datashader":"ds", "colorcet":"cc", "param":"param", "sklearn.preprocessing.StandardScaler":"Scaler",
"sklearn.preprocessing.LabelEncoder":"LabelEncoder", "sklearn.preprocessing.OneHotEncoder":"OneHotEncoder", "sklearn.naive_bayes.GaussianNB":"GNB", 
"sklearn.preprocessing.MinMaxScaler":"MinMaxScaler", "sklearn.preprocessing.MinMaxScaler":"MinMaxScaler", "sklearn.model_selection.train_test_split":"train_test_split"})

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

