import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import os
from pandas.plotting import register_matplotlib_converters
from matplotlib.pylab import rcParams
from datetime import datetime

########################
### Tratando Dataset ###
########################

# Configuração do padrão de medidas do plot dos gráficos
rcParams['figure.figsize'] = 15, 6

# Restaura todos os rcParams para o padrão
plt.rcdefaults()

arquivo = "C:/Users/HenriqueSchall/OneDrive - Neo Digital Industries/nPlan-Data-Science/Projetos/nPlan Forecast/Dados/PremieRPet/Dados_PremieRPet.xlsx"
df = pd.read_excel(arquivo, sheet_name="Faturamento Historico")
df.head()

df['AnoMes'] = df['Ano'].astype(str) + '-' + df['Mês'].astype(str).str.zfill(2)
df['Datetime'] = pd.to_datetime(df['AnoMes'] + '-01', format='%Y-%m-%d').dt.date
df.drop(columns=['Ano', 'Mês', 'AnoMes'], inplace=True)
df.head(50)

df.to_excel('PremieRPet_Tratados.xlsx', index=False)
df.to_csv('PremieRPet_Tratados.csv', index=False, sep=',')
print("Diretório atual:", os.getcwd())