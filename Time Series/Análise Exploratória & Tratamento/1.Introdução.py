import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import statsmodels.tsa.stattools
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from matplotlib.pylab import rcParams
from random import sample, random
from statsmodels.tsa.seasonal import seasonal_decompose as decompose

# Configuração do padrão de medidas do plot dos gráficos para ficar visivelmente mais agradáveis
rcParams['figure.figsize'] = 15, 6

###################
### Série Anual ###
###################

# Criando array de dados aleatórios para a Série (Periodo: 1980 a 2020 = 41 anos)
np.random.seed(10) # definir ponto inicial para sempre gerar mesmos valores aleatórios
df = np.random.normal(
    0, # média
    1, # desvio padrão
    41) # quantidade de valores
df.shape
df

# Criando índice temporal
index = pd.date_range(
    start="1980",
    periods = len(df),    
    freq="AS") #A ou AS
index

# Verificando valores
len(index)
len(df)

# Criando DataFrame Conjunto
df_anual = pd.DataFrame({
    "Anual": index,
    "Valores": df
})

# Definindo Ano como índice temporal
df_anual.set_index("Anual", inplace=True)

df_anual.describe()
# count = Número de observações no conjunto de dados
# mean = Número de observações no conjunto de dados
# std = O desvio padrão. Mede a dispersão dos dados em relação à média. Quanto maior, mais espalhados os valores estão
# min = O menor valor do conjunto de dados
# 25% = O primeiro quartil. 25% dos dados estão abaixo deste valor
# 50% = A mediana. 50% dos dados estão abaixo deste valor
# 75% = O terceiro quartil. 75% dos dados estão abaixo deste valor
# max = O maior valor do conjunto de dados

# Plotando a série temporal
serie_index = pd.Series(df_anual["Valores"].values)

# Customizando o gráfico 
ax = serie_index.plot(color="cyan") # Título
ax.set_title("Série Temporal Anual", color="white", fontsize=14) # Fundo da área do gráfico
ax.set_facecolor("black") # Fundo da figura
ax.figure.set_facecolor("black") # Cor da linha
ax.tick_params(colors="white") # Valores
ax.xaxis.label.set_color("white") # Eixo x
ax.yaxis.label.set_color("white") # Eixo y
for spine in ax.spines.values(): # Bordas
    spine.set_color("white")

plt.show()

####################
### Série Mensal ###
####################

# Período: 1995-01 a 2000-12 = 72 meses)
np.random.seed(6) # definir ponto inicial para sempre gerar mesmos valores aleatórios
df_mensal = np.random.normal(
    0, # média
    1, # desvio padrão
    72) # quantidade de valores
df_mensal.shape
df_mensal

index_mensal = pd.date_range(
    start="2015-01",
    periods=72, 
    freq="M")
index_mensal

len(index_mensal)
len(df_mensal)

df_mensal_concat = pd.DataFrame({
    "Mensal": index_mensal,
    "Valores": df_mensal
})

df_mensal_concat.set_index("Mensal", inplace=True)
serie_index_mensal = pd.Series(df_mensal_concat["Valores"].values)

ax = serie_index_mensal.plot(color="cyan") # Título
ax.set_title("Série Temporal Mensal", color="white", fontsize=14) # Fundo da área do gráfico
ax.set_facecolor("black") # Fundo da figura            
ax.figure.set_facecolor("black") # Cor da linha     
ax.tick_params(colors="white") # Valores       
ax.xaxis.label.set_color("white") # Eixo x    
ax.yaxis.label.set_color("white") # Eixo y    
for spine in ax.spines.values(): # Bordas
    spine.set_color("white")

plt.show()

########################
### Série Trimestral ###
########################

# Período: 2020-01-01 a 2020-12-31 = 366 dias (ano bissexto)
np.random.seed(29) # definir ponto inicial para sempre gerar mesmos valores aleatórios
df_trimestral = np.random.normal(
    0, # média
    1, # desvio padrão
    164) # quantidade de valores
df_trimestral.shape
df_trimestral

index_trimestral = pd.date_range(
    start="1980-01",
    periods=731, 
    freq="3M")
index_trimestral

len(index_trimestral)
len(df_trimestral)

df_trimestral_concat = pd.DataFrame({
    "Trimestral": index_trimestral,
    "Valores": df_trimestral
})

df_trimestral_concat.set_index("Trimestral", inplace=True)
serie_index_trimestral = pd.Series(df_trimestral_concat["Valores"].values)
serie_index_trimestral.plot()
plt.show()

####################
### Série Diária ###
####################

# Período: 2020-01-01 a 2020-12-31 = 366 dias (ano bissexto)
np.random.seed(12) # definir ponto inicial para sempre gerar mesmos valores aleatórios
df_diario = np.random.normal(
    1, # média
    2, # desvio padrão
    731) # quantidade de valores
df_diario.shape
df_diario

index_diario = pd.date_range(
    start="2020-01-01",
    periods=731, 
    freq="D")
index_diario

len(index_diario)
len(df_diario)

df_diario_concat = pd.DataFrame({
    "Diário": index_diario,
    "Valores": df_diario
})

df_diario_concat.set_index("Diário", inplace=True)
serie_index_diario = pd.Series(df_diario_concat["Valores"].values)
serie_index_diario.plot()
plt.show()

######################
### Autocorrelação ###
######################

np.random.seed(6)
dados1 = np.random.normal(0,1,72)
dados1

serie = pd.Series(dados1)
serie.plot()
plt.show()

## FAC ###
plot_acf(serie, lags=15)
plt.show()

## FACP ###
plot_pacf(serie, lags=30)
plt.show()









#########################
### Passeio Aleatório ###
#########################

# Série Passeio aleatório 1
# Criando dados
dados_alet = sample(range(100), k=41) # k -> valores retirados de 100
dados_alet

# Criando período
periodo = list(range(1980, 2021))
periodo

serie_passeio_1 = pd.Series(dados_alet, index = periodo)
serie_passeio_1
serie_passeio_1.plot()
plt.show()

## Série Passeio aleatório 2
# Criando dados
serie_passeio_2 = list()
serie_passeio_2.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movimento = -1 if random() < 0.5 else 1
    valor = serie_passeio_2[i-1] + movimento
    serie_passeio_2.append(valor)

serie_passeio_2 = pd.Series(serie_passeio_2)
serie_passeio_2.plot()
plt.show()

##############
### Testes ###
##############

### Testes de Normalidade (Shapiro-Wilk) ###
# - H0: resíduos normalmente distribuídos (p > 0.05)
# - H1: resíduos não são normalmente distribuídos (p <= 0.05)
teste_1 = stats.shapiro(serie_index)
print('p-valor: {}'.format(teste_1.pvalue))

teste_2 = stats.shapiro(serie_passeio_1)
print('p-valor: {}'.format(teste_2.pvalue))

teste_3 = stats.shapiro(serie_passeio_2)
print('p-valor: {}'.format(teste_3.pvalue))

### Testes de Estacionaridade ###
# Teste pp (Philips-Perron)
# - H0 = é estacionária: p > 0.05
# - H1 = não é estacionária: p <= 0.05
pp_test = sm.phillips_perron(serie1)

# Renomendando saídas 
pp_test_output = {'Estatítica do teste': pp_test[0], 'p-value': pp_test[1], 'Número de lags': pp_test[2], 'Número de Observações': pp_test[3], 'Valores Críticos': pp_test[4]}
pp_test_output

### Teste Kwiatkowski-Phillips-Schmidt-Shin ###
# - H0 = é estacionária: teste estatístico < valor crítico
# - H1 = não é estacionária: teste estatístico >= valor crítico
kpss_test = sm.kpss(serie1)

kpss = statsmodels.tsa.stattools.kpss(serie1)
print('Estatítica do teste: {:.4f}'.format(kpss[0]))
print('p_valor: {:.4f}'.format(kpss[1]))
print('número de lags: {}'.format(kpss[2]))
print('Valores Críticos:')
for chave, valor in kpss[3].items():
   print('{}: {:.4f}'.format(chave, valor))



kpss_test_output = {'Estatítica do teste': kpss_test[0], 'p-value': kpss_test[1], 'Número de lags': kpss_test[2], 'Valores Críticos': kpss_test[3]}
kpss_test_output

### Teste Dickey Fuller ###
# - H0 = é estacionária:  teste estatístico < valor crítico
# - H1 = não é estacionária: teste estatístico > valor crítico
df_test = sm.adfuller(serie1)

df_test_output = {'Estatítica do teste': df_test[0], 'p-value': df_test[1], 'Número de lags': df_test[2], 'Número de Observações': df_test[3], 'Valores Críticos': df_test[4]}
df_test_output

### Testes de Autocorrelação (Ljung-Box ) ###
# - H0: não autocorrelacionados (p > 0.05)
# - H1: são autocorrelacionados (p <= 0.05)
ljung_box_test = sm.stats.acorr_ljungbox(serie1, lags=[10], return_df=True)
ljung_box_test


#**AirPassengers: dados clássicos da companhia aérea Box & Jenkins. Totais mensais de passageiros de companhias aéreas internacionais, 1949 a 1960.**

serie2 = pd.read_csv('/content/drive/MyDrive/Cursos_Udemy/series_temporais_PYTHON/AirPassengers.csv')

serie2 = pd.Series(serie2['#Passengers'].values, index = serie2['Month'])
serie2

serie2.plot()
plt.show()




# Selecionando o Período 
# data = np.array('2015-01', dtype = np.datetime64())
# data = data + np.arange(72)
# data = pd.DataFrame(data)
# data.columns = ['data']
# data

# Combinando valores
# serie2 = pd.concat([data, dados], axis=1)
# serie2

# serie2 = pd.Series(serie2['valores'].values, index = serie2['data'])
# serie2
# serie2.plot()
# plt.show()

# Criando dados aleatórios (Série Diária)
# np.random.seed(12)
# dados = np.random.normal(0,1,731)
# dados = pd.DataFrame(dados)
# dados.columns = ['valores']
# dados

# Selecionando o Período 
# data = pd.date_range('2019 Jan 1', periods = len(dados3), freq = 'D'
# data

# serie3 = pd.Series(dados['valores'].values, index = data)
# serie3.plot()
# plt.show()

# Tabela 
dados = pd.DataFrame(dados)
dados.columns = ['valores']
dados
dados.shape # verificando valores

# Gráfico 
serie = pd.Series(dados)
serie.plot()
plt.show()

# Selecionando o Período 
periodo = pd.date_range('2000', periods = len(dados), freq = 'Y')
periodo

serie1 = pd.Series(dados['valores'].values, index = periodo)
serie1.plot()
plt.show()

### Case Manchas Solares ###

manchas_solares = sm.datasets.sunspots.load_pandas().data
manchas_solares

serie_m = pd.Series(manchas_solares['SUNACTIVITY'].values, index = manchas_solares['YEAR'])
serie_m

serie_m.plot()

plot_acf(serie_m, lags=45)
plt.show()

plot_pacf(serie_m, lags=30)
plt.show()

####################
### Decomposição ###
####################

concentracao = sm.datasets.co2.load_pandas().data
concentracao

serie = pd.Series(concentracao['co2'].values, index = concentracao.index)
serie

serie.plot()
plt.show()

# Valores missing
concentracao.isnull().sum()
concentracao.dropna(inplace=True)

serie2 = pd.Series(concentracao['co2'].values, index = concentracao.index)
serie2.plot()
plt.show()

decomposicao = decompose(serie2, period=15)
decomposicao = decompose(serie2)

decomposicao.plot()
plt.show()

# Renomeando Labels
plt.subplot(411)
plt.plot(serie, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(decomposicao.trend, label='Tendência')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(decomposicao.seasonal,label='Sazonalidade')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(decomposicao.resid, label='Resíduos')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Decomposição multiplicativa
decomp_mult = decompose(serie2,period=7,model='multiplicative')
decomp_mult.plot()

decomp_mult.plot()
plt.show()

####################################
### Tranformação e Diferenciação ###
####################################

##################
### Suavização ###
##################
