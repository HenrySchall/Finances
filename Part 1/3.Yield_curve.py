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

################################
## Creating National Holidays ##
################################

def brazil_calendar():
    # Extrai a lista de feriados direto do site da anbima
    holidays = pd.read_excel('http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls', skipfooter=9)["Data"]
    weekends = ["Saturday", "Sunday"]
    # Cria o calendário
    calendar = Calendar(holidays, weekends)
    return calendar

####################################
## Obtaining DI Futures Contracts ##
####################################

cal = brazil_calendar()

r = requests.get('https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-ajustes-do-pregao-ptBR.asp')
s = bs(r.content, 'html.parser')

dataref = s.find('input', id = 'dData1').get('value')
dataref = datetime.strptime(dataref, '%d/%m/%Y').strftime('%Y-%m-%d')

tb = s.find('table', id = 'tblDadosAjustes')

lines = [l.find_all('td') for l in tb.findAll('tr')[1:]]

df = pd.DataFrame([[i.text for i in l] for l in lines])

print(df)

df = df[[0, 1, 3]] #Select Columns
df.columns = ['Ativo', 'CodVcto', 'ValorAjuste'] #Rename Columns

df['ValorAjuste'] = df['ValorAjuste'].str.replace('.', '').str.replace(',', '.').astype(float) #Replace , for .

df = df.iloc[223:263] #Select DI value lines

df['Ativo'] = np.nan
df['Ativo'] = df['Ativo'].fillna('DI1')
df['CodVcto'] = df['CodVcto'].str.strip() # Remove the empty spaces from the expiration code column

print(df)

MESES_VCTO = {
    'F': 1,  # Janeiro
    'G': 2,  # Fevereiro
    'H': 3,  # Março
    'J': 4,  # Abril
    'K': 5,  # Maio
    'M': 6,  # Junho
    'N': 7,  # Julho
    'Q': 8,  # Agosto
    'U': 9,  # Setembro
    'V': 10, # Outubro
    'X': 11, # Novembro
    'Z': 12  # Dezembro
    }

# Transform the code in date
def cod_to_vcto(cod):
    # Encontra o mês e ano
    mes = MESES_VCTO[cod[0]]
    ano = 2000 + int(cod[-2:])

    # Define a data e retorna em formato de texto
    # O método following retorna o primeiro dia a partir da data indicada
    data = cal.following(datetime(ano, mes, 1))
    return data.strftime("%Y-%m-%d")

# Gerar os vencimentos e os dias úteis
# A data de referência é a data de fechamento ods preços
df['Vcto'] = df['CodVcto'].apply(cod_to_vcto)
df['DU'] = df['Vcto'].apply(lambda x: cal.bizdays(dataref, x))

df['Taxa'] = (100000 / df['ValorAjuste']) ** (252 / df['DU']) - 1

print(df)

###################
## Interpolation ##
###################

# Cria uma coluna com a taxa do dia vigente e do dia seguinte
df['r0'] = df['Taxa']
df['r1'] = df['Taxa'].shift(-1)

# Cria uma coluna com o tempo do dia vigente e do dia seguinte
df['du0'] = df['DU']
df['du1'] = df['DU'].shift(-1).fillna(9999)

# gera uma lista com todos os dias úteis entre o primeiro e o último vértice
list_dus = [i for i in range(df['DU'].min(), df['DU'].max()) if i not in df['DU'].values]

# concatena os dias úteis com o dataframe dos vértices
df_dus = pd.DataFrame(list_dus, columns = ['DU'])
df = pd.concat([df, df_dus]).sort_values(by = 'DU').reset_index(drop = True)

# Cria a coluna de anos úteis (a quantidade de dias úteis sobre a quantidade total do ano)
df['AU'] = df['DU'] / 252

# Encontra a data referente a cada dia
df['Vcto'] = df['DU'].apply(lambda x: cal.offset(dataref, x))

# preenche as datas e taxas anterior e próxima nas novas linhas que criadas
df['r0'] = df['r0'].fillna(method = 'ffill')
df['r1'] = df['r1'].fillna(method = 'ffill')
df['du0'] = df['du0'].fillna(method = 'ffill')
df['du1'] = df['du1'].fillna(method = 'ffill')