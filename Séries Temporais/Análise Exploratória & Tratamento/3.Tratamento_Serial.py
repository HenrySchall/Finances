import pandas as pd
import numpy as np
import seaborn as sns
import sklearn
import statsmodels.tsa.stattools as sm
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE
from matplotlib import pyplot
from pandas import Series

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

arquivo = ""
df = pd.read_excel(arquivo, sheet_name="Faturamento Historico")
df.head()

df['AnoMes'] = df['Ano'].astype(str) + '-' + df['Mês'].astype(str).str.zfill(2)
df['Datetime'] = pd.to_datetime(df['AnoMes'] + '-01', format='%Y-%m-%d').dt.date
df.drop(columns=['Ano', 'Mês', 'AnoMes'], inplace=True)
df.head(50)

df.to_excel('.xlsx', index=False)
df.to_csv('.csv', index=False, sep=',')
print("Diretório atual:", os.getcwd())


Média_Móveis

Suavização_Exponencial

---

d = pd.read_csv("AirPassengers.csv", header=0, parse_dates=[0], index_col=0).squeeze("columns")
d = d.astype("float32")
d

differenced = d.diff(12)
differenced.head(n=13)

differenced.plot()
pyplot.show()

differenced = differenced[12:]

differenced.head(n=13)

differenced.plot()
pyplot.show()

dataframe = pd.DataFrame()
for i in range(12, 0, -1):
    dataframe['t-'+str(i)] = differenced.shift(i)
dataframe['t'] = differenced.values

dataframe = dataframe[12:]

dataframe

array = dataframe.values
X = array[:,0:-1]
y = array[:,-1]

model = RandomForestRegressor(n_estimators=500, random_state=1)
model.fit(X, y)

print(model.feature_importances_)

rankings = len(model.feature_importances_) - np.argsort(model.feature_importances_).argsort()
print("Rankings:", rankings)

names = dataframe.columns.values[0:-1]
ticks = [i for i in range(len(names))]
pyplot.bar(ticks, model.feature_importances_)
pyplot.xticks(ticks, names)
pyplot.show()

rfe = RFE(RandomForestRegressor(n_estimators=500, random_state=1))
fit = rfe.fit(X, y)

names = dataframe.columns.values[0:-1]
for i in range(len(fit.support_)):
    if fit.support_[i]:
        print(names[i])