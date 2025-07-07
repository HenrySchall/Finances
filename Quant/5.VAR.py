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

import pyomo.environ as pyo
import gurobipy as gp
import pandas as pd 
import seaborn as sns
import plotly.express as px
import numpy as np
import panel as pn 
import seaborn.objects as so
import matplotlib as mpl
import colorcet as cc
import matplotlib.pyplot as plt
import math
import datetime
import param
import sklearn
import scipy
import string
import random
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.naive_bayes import GaussianNB as GNB

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