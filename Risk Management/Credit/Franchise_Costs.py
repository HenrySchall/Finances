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

data = "https://raw.githubusercontent.com/HenrySchall/Databases/main/AI/GenAI/projects_data.csv"
df = pd.read_csv(data)

def train_or_predict(new_projects):
    # Testa se o modelo existe
    model_path = 'logistic_model.joblib'
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        scaler = joblib.load(model_path.replace(".joblib", "_scaler.joblib"))
    else:
        df_projects = pd.read_csv("projects_data.csv")

        # Separa variáveis
        X = df_projects[["investment", "expected_return", "impact_score"]]
        y = df_projects["viability"]

        # Normaliza
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Divide em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.3, random_state=42
        )

        # Treina
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Avalia
        y_pred = model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        # Salva modelo, scaler e métricas em disco
        joblib.dump(model, model_path)
        joblib.dump(scaler, model_path.replace(".joblib", "_scaler.joblib"))
        joblib.dump(report, model_path.replace(".joblib", "_metrics.joblib"))

    # Previsão
    if new_projects:
        df_new_projects = pd.DataFrame(new_projects)

        X_new_scaled = scaler.transform(df_new_projects)

        predictions = model.predict(X_new_scaled)
        # Probabildiade de 1
        probabilities = model.predict_proba(X_new_scaled)[:, 1]
        df_new_projects["probability"] = probabilities
        df_new_projects["viability"] = predictions

        return df_new_projects, joblib.load(model_path.replace(".joblib", "_metrics.joblib"))

    return None, joblib.load(model_path.replace(".joblib", "_metrics.joblib"))

#######################
### Teste do Modelo ###
#######################

# Novos projetos
new_projects = [
    #{"investment": 13000, "expected_return": 69000, "impact_score": 7}
    {"investment": 40000, "expected_return": 60000, "impact_score": 6}
]

predictions, metrics = train_or_predict(new_projects)

if predictions is not None:
    print("\nNovos Projetos e Viabilidade:")
    print(predictions)

print("\nMétricas do Modelo:")
print(metrics)