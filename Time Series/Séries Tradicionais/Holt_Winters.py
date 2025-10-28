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

url = "C:/Users/HenriqueSchall/Desktop/Dados_Tratados.xlsx"
df = pd.read_excel(url, sheet_name="Faturamento_Historico")
print(df)

df = df.drop(columns=["Ano", "Mês_num", "Mês"])
df.info()
print(df)

Produto = 4002
df_Produto = df[df['Produto'] == Produto].copy()  
df_Produto.set_index('Datetime', inplace=True)
df_Produto = df_Produto.asfreq('MS')

df_Produto['Quantidade'].plot(title=f'Quantidade Mensal - Produto {Produto}')
plt.show()

############################
### Holt-Winters Aditivo ###
############################

item_id = 4002
serie = df[df['Produto'] == item_id][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

# Ajusta o modelo
fit1 = ExponentialSmoothing(
    serie,
    seasonal_periods=12,
    trend='additive',
    seasonal='additive',
).fit()

forecast = fit1.forecast(12)
print(forecast)

# Valores Passados
fit1.fittedvalues.plot(style='--', color='red')
plt.show()

# Valores Futuros
fit = 12 # meses futuros
fit1.forecast(fit).plot(style='--', marker='o', color='black', legend=True)
plt.show()

# Agrupando tudo em um gráfico
forecast_h = 12  # meses futuros
forecast = fit1.forecast(forecast_h)

plt.plot(serie, label='Observado', color='blue')
plt.plot(fit1.fittedvalues, '--', label='Ajustado', color='red')
plt.plot(forecast, '--o', label='Previsão', color='black')
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.title(f'Previsão Holt-Winters - Produto {item_id}')
plt.legend()
plt.grid(True)
plt.show()

###################################
### Holt-Winters Multiplicativo ###
###################################

item_id = 4002
serie = df[df['Produto'] == item_id][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

# Ajusta o modelo
fit2 = ExponentialSmoothing(
    serie,
    seasonal_periods=12,
    trend='multiplicative',
    seasonal='multiplicative',
).fit()

forecast = fit2.forecast(12)
print(forecast)

# Valores Passados
fit2.fittedvalues.plot(style='--', color='red')
plt.show()

# Valores Futuros
fit = 12 # meses futuros
fit2.forecast(fit).plot(style='--', marker='o', color='black', legend=True)
plt.show()

# Agrupando tudo em um gráfico
forecast_h = 12  # meses futuros
forecast = fit2.forecast(forecast_h)

plt.plot(serie, label='Observado', color='blue')
plt.plot(fit2.fittedvalues, '--', label='Ajustado', color='red')
plt.plot(forecast, '--o', label='Previsão', color='black')
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.title(f'Previsão Holt-Winters - Produto {item_id}')
plt.legend()
plt.grid(True)
plt.show()

##############################
### Média Móvel Simples 3M ###
##############################

Produto = 4001
serie = df[df['Produto'] == item_id][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

serie_MMS = serie['Quantidade'].rolling(3).mean()

# Plotando os resultados
plt.plot(serie['Quantidade'], label='Original', color='blue')
plt.plot(serie_MMS, label='Média Móvel Simples 3M', color='red')
plt.xlabel("Ano", fontsize=14)
plt.ylabel("Quantidade")
plt.title(f"Média Móvel Simples 3 Meses - Produto {item_id}")
plt.legend()
plt.grid(True)
plt.show()

################################
### Média Móvel Ponderada 3M ###
################################

Produto = 4001
serie = df[df['Produto'] == item_id][['Datetime', 'Quantidade']].copy()
serie.set_index('Datetime', inplace=True)

weights = np.array([0.1, 0.3, 0.6])
serie_MMP = serie['Quantidade'].rolling(window=3).apply(lambda x: np.dot(x, weights), raw=True)

# Plotando os resultados
plt.plot(serie['Quantidade'], label='Original', color='blue')
plt.plot(serie_MMP, label='Média Móvel Ponderada 3M', color='red')
plt.xlabel("Ano", fontsize=14)
plt.ylabel("Quantidade")
plt.title(f"Média Móvel Ponderada 3 Meses - Produto {item_id}")
plt.legend()
plt.grid(True)
plt.show()
