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
"sklearn.preprocessing.LabelEncoder":"LabelEncoder", "sklearn.preprocessing.OneHotEncoder":"OneHotEncoder", "sklearn.naive_bayes.GaussianNB":"GNB", "xlrd": ">xlrd", "bizdays": "bd"
"sklearn.preprocessing.MinMaxScaler":"MinMaxScaler", "sklearn.preprocessing.MinMaxScaler":"MinMaxScaler", "sklearn.model_selection.train_test_split":"train_test_split"})

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