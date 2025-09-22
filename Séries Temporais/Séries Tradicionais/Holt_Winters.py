import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from pandas.plotting import register_matplotlib_converters
from matplotlib.pylab import rcParams
from datetime import datetime
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

# Configuração do padrão de medidas do plot dos gráficos
rcParams['figure.figsize'] = 15, 6

df = pd.read_csv(
    r'C:/Users/HenriqueSchall/OneDrive - Neo Digital Industries/nPlan-Data-Science/Projetos/nPlan Forecast/Dados/PremieRPet/Tratados/PremieRPet_Tratados.csv',
    parse_dates=['Datetime'],
    index_col='Datetime',
    date_format='%Y-%m-%d'
)

df.head()

# Seleciona o item desejado
item = 4003
df_item = df[df['Item'] == item]
df_item = df_item.asfreq("MS") # MS or AS

df_item['Quantidade'].plot(title=f'Quantidade Mensal - Item {item}')
plt.show()

item_id = 4001
serie = df.loc[df['Item'] == item_id, 'Quantidade'] 
serie = (serie.sort_index().asfreq('MS').astype('float'))

# Ajusta o modelo
fit1 = ExponentialSmoothing(
    serie,
    seasonal_periods=12,
    trend='additive',
    seasonal='additive',
).fit()

forecast = fit1.forecast(12)
print(forecast)

fit1.fittedvalues.plot(style='--', color='red')
plt.show()

fit1.forecast(24).plot(style='--', marker='o', color='black', legend=True)
plt.show()

fit1.fittedvalues.plot(style='--', color='red')
fit1.forecast(24).plot(style='--', marker='o', color='black', legend=True)
plt.show()