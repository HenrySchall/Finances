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
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

data = "https://raw.githubusercontent.com/HenrySchall/Databases/main/AI/GenAI/projects_data.csv"
df = pd.read_csv(data)

#########################
### Pré-Processamento ###
#########################

# Remove colunas sem valor semântico
df = df.drop(columns=['transaction_id', 'customer_id'])

# Pré-processa Variáveis Categóricas
df_encoded = pd.get_dummies(df, columns=['location'], drop_first=True)

# Separa
X = df_encoded.drop(columns=['is_fraud'])
y = df_encoded['is_fraud']

# Normaliza
scaler = StandardScaler()
X[['amount', 'time']] = scaler.fit_transform(X[['amount', 'time']])

# Dividi em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train)

###################
### Treinamento ###
###################

model = MLPClassifier(hidden_layer_sizes=(10, 8, 10), max_iter=500,
                      random_state=42, learning_rate_init=0.01, activation='relu')
model.fit(X_train, y_train)

#################
### Avaliação ###
#################

y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred, output_dict=True)
print(report)

###################
### Novos Dados ###
###################

# Lista de novas transações
new_transactions = [
    {"amount": 3871.09, "time": 10, "location": "Loja Física"},
    {"amount": 12.56, "time": 12, "location": "Online"},
    {"amount": 4451.62, "time": 20, "location": "Online"},
    {"amount": 38.09, "time": 20, "location": "Loja Física"}
]


# Cria DataFrame
df_new = pd.DataFrame(new_transactions)

# Transforma variavel categórica
df_new_encoded = pd.get_dummies(df_new, columns=['location'], drop_first=True)

# Normaliza
df_new_encoded[['amount', 'time']] = scaler.transform(df_new_encoded[['amount', 'time']])

# Previsão
predictions = model.predict(df_new_encoded)
probabilities = model.predict_proba(df_new_encoded)[:, 1]

# Adiciona os resultados ao DataFrame original
df_new["fraud_probability"] = probabilities
df_new["is_fraud_predicted"] = predictions

# Exibr previsões
print(df_new[["amount", "time", "location", "fraud_probability", "is_fraud_predicted"]])
