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
"yfinance", "scikit-learn", "panel", "datashader", "param", "colorcet", "transformers","einops","accelerate", 
"bitsandbytes"]

install_packages(packages_list)

#####################
### Load Packages ###
#####################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import numpy as np
import joblib
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from IPython.display import display

data = "https://raw.githubusercontent.com/HenrySchall/Databases/main/AI/GenAI/projects_data.csv"
df = pd.read_csv(data)

Q1 = dados.quantile(0.25)
Q3 = dados.quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
print(f"Limite Inferior:\n{limite_inferior}")
print(f"Limite Superior:\n{limite_superior}")
dados = dados[~((dados < limite_inferior) | (dados > limite_superior)).any(axis=1)]
dados.shape

X = dados[['FrqAnual']]
y = dados['CusInic']

modelo = LinearRegression()
modelo.fit(X, y)

plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, modelo.predict(X), color='red', label='Regressão Linear')
plt.xlabel("Taxa Anual")
plt.ylabel("Custo Inicial")
plt.title("Gráfico de Dispersão com Regressão Linear")
plt.legend()
plt.show()

################
### Previsão ###
################

novo_valor = float(input("Taxa Anual da Franquia: "))

dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
prev = modelo.predict(dados_novo_valor)

print(f"Previsão de Custo Inicial R$: {prev[0]:.2f}")