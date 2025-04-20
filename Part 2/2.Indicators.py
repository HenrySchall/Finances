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