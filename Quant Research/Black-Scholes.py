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

from datetime import datetime, timedelta

def cotacoes(ticker, dias):
    # formata o nome do ticker
    start = (datetime.today()-timedelta(dias)).strftime('%Y-%m-%d')
    ticker=ticker+'.SA' if ticker[-3:] != '.SA' else ticker
    
    # busca o ticker no yahoo finance
    df = yf.download(ticker, start)
    return df

cotacoes ("EMBR3",10)


def selic():
    # busca o histórico diário da selic
    r=requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json').json()
    df = pd.DataFrame(r).set_index('data')
    df['valor'] = df['valor'].astype(float)
    
    # anualiza as taxas, considerando 252 dias úteis no ano
    df['valor'] = df['valor'].apply(lambda x: 1+x/100)**252-1
    
    # obtem o valor atual
    selic=df['valor'].iloc[-1]
    return selic

selic()


def d1(S, K, r, sigma, T):
    return (np.log(S/K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))

def d2(S, K, r, sigma, T):
    return (np.log(S/K) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))

def bsm_call(S, K, r, sigma, T):
    return (S * norm.cdf(d1(S, K, r, sigma, T)) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, sigma, T))))

def bsm_put(S, K, r, sigma, T):
    return  - (S * norm.cdf(-d1(S, K, r, sigma, T))) + (K * np.exp(-r * T) * norm.cdf(-d2(S, K, r, sigma, T)))

#Usando duas opções de BBAS3 como exemplo, obtidas no site opcoes.net.br. 
# O campo Último mostra o preço de mercado

ativo = 'BBAS3'
vencimento = '2022-12-16'
K = 45.05

# A data que está sendo executado é 17/09/2022
# em outro dia os parâmetros serão diferentes, portanto os resultados serão diferentes

# Série histórica, usaremos os últimos 365 dias. O parâmetro dias irá afetar diretamente a volatildiade (sigma)
df = cotacoes(ativo, 365)

# Preço atual da ação
S = df['Adj Close'][-1]

# Gera a coluna de retorno os retornos logaritmicos
df['Returns'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))

# volatilidade: usaremos o desvio padarão dos retornos anualizado.
# Obs: Existem outros modelos de volatildiade, como o EWMA. O modelo pode ser escolhido dependendo da sua estratégia.
sigma = df['Returns'].std() * 252 ** 0.5

# taxa livre de risco
r = selic()

# tempo em anos até o vencimento
T = (datetime.strptime(vencimento, '%Y-%m-%d') - datetime.now()).days/365

print(S) # 39.400001525878906
print(K) # 45.05
print(r) # 0.13649989315282562
print(sigma) # 0.2941359350202654
print(T) # 0.24383561643835616

bsm_put(S, K, r, sigma, T) # 5.043368866048489


#O modelo precificou a BBASX45 em aproximadamente R$ 5,04 enquanto o mercado está precificando a R$ 6,26. Já a opção BBASL373 foi precificada pelo modelo em aproximadamente R$ 4,76 enquanto o mercado está precificando a R$ 5,85.

#Importante lembrar que o preço gerado pelo modelo varia dependendo principalmente do intervalo de tempo escolhido do histórico de preços do ativo objeto e do modelo de volatilidade usado. O valor de mercado da opção pode ser afetado por outros fatores de mercado não previstos no modelo BSM. Se o valor de mercado estiver abaixo do valor dado pelo modelo, isso não significa que a opção esteja necessariamente barata. Não use apenas esse modelo para tomar decisões de investimentos.

#Bonus
#Como obter os dados do site opcoes.net.br diretamente pelo python
#A função listar_opcoes retorna um dataframe com as informações sobre todas as opções listadas do ativo indicado.

#Obs: o campo MOD indica o modelo da opção, Americana ou Europeia

# Obtem os vencimentos
def vencimentos(ticker):
    url = f'https://opcoes.net.br/listaopcoes/completa?au=False&uinhc=0&idLista=ML&idAcao={ticker}&listarVencimentos=true&cotacoes=true'
    response = requests.get(url, verify=False).json()
    vctos = [[i['value'], i['text']] for i in response['data']['vencimentos']]
    return vctos

# Obtem as opções
def listar_opcoes(ticker):
    # Busca os vencimentos
    vctos = vencimentos(ticker)
    opcs=[]
    
    # Busca as opções para cada data de vencimento
    for vcto in vctos:
        url=f'https://opcoes.net.br/listaopcoes/completa?au=False&uinhc=0&idLista=ML&idAcao={ticker}&listarVencimentos=false&cotacoes=true&vencimentos={vcto[0]}'
        response = requests.get(url).json()
        
        # Busca apenas os campos necessários
        opcs += ([[ticker]+[i[0][:i[0].find('_')]] + i[2:4] + [vcto[1]] + [i[5]] + [i[8]] for i in response['data']['cotacoesOpcoes']])
    
    # Gera o dataframe
    colunas = ['ATIVO_OBJ','ATIVO', 'TIPO', 'MOD', 'DT_VCTO', 'STRIKE', 'PRECO']
    opcs = pd.DataFrame(opcs, columns=colunas)
    
    # transforma o campo vencimento e datetime
    opcs['DT_VCTO'] = pd.to_datetime(opcs['DT_VCTO'])
    
    return opcs