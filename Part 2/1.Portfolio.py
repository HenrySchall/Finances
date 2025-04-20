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

# Preparando Dados
dataset_df = ['VALE3.SA', 'WEGE3.SA', 'ITUB4.SA', 'GOLL4.SA', 'BOVA11.SA']

dataset_vector = pd.DataFrame()
for acao in dataset_df:
  dataset_vector[acao] = yf.download(acao, start='2015-01-02', end='2023-12-31')['Close']
dataset_vector

dataset = dataset_vector.rename(columns={'VALE3.SA': 'VALE', 'WEGE3.SA': 'WEGE','ITUB4.SA': 'ITAU', 'GOLL4.SA': 'GOL', 'BOVA11.SA': 'BOVA'})

dataset.isnull().sum()
dataset.dropna(inplace=True)
dataset.isnull().sum()

dataset

dataset.to_csv('dataset_df.csv')
dataset = pd.read_csv('dataset_df.csv')
dataset

####################
### Carteira MVP ###
####################

################
### Alocação ###
################

valor_total_investido = 5000
num_pesos = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

alocacao_ativos = (pd.read_csv('dataset_df.csv'), valor_total_investido)
alocacao_ativos

def alocacao_ativos(dataset, valor_total_investido):
  dataset = dataset.copy()








def alocacao_ativos(dataset, dinheiro_total, seed = 0, melhores_pesos = []):
  dataset = dataset.copy()

  if seed != 0:
    np.random.seed(seed)

  if len(melhores_pesos) > 0:
    pesos = melhores_pesos
  else:
    pesos = np.random.random(len(dataset.columns) - 1)
    #print(pesos, pesos.sum())
    pesos = pesos / pesos.sum()
    #print(pesos, pesos.sum())

  colunas = dataset.columns[1:]
  #print(colunas)
  for i in colunas:
    dataset[i] = (dataset[i] / dataset[i][0])

  for i, acao in enumerate(dataset.columns[1:]):
    #print(i, acao)
    dataset[acao] = dataset[acao] * pesos[i] * dinheiro_total

  # ATUALIZAÇÃO ABR-2024
  # dataset['soma valor'] = dataset.sum(axis = 1)
  dataset['soma valor'] = dataset.iloc[:, 1:].sum(axis = 1)

  datas = dataset['Date']
  #print(datas)

  dataset.drop(labels = ['Date'], axis = 1, inplace = True)
  dataset['taxa retorno'] = 0.0

  for i in range(1, len(dataset)):
    dataset['taxa retorno'][i] = ((dataset['soma valor'][i] / dataset['soma valor'][i - 1]) - 1) * 100

  acoes_pesos = pd.DataFrame(data = {'Ações': colunas, 'Pesos': pesos * 100})

  return dataset, datas, acoes_pesos, dataset.loc[len(dataset) - 1]['soma valor']
