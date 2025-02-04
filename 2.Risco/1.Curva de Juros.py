# pip install xlrd
# pip install bizdays
# pip install polars

import pandas as pd
import polars as pl
import requests
import xlrd
from bizdays import Calendar
from datetime import datetime
from bs4 import BeautifulSoup as bs
import calendar

#########################################
## Creating national holidays calendar ##
#########################################

def brazil_calendar():
    # Extrai a lista de feriados direto do site da anbima
    holidays = pd.read_excel('http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls', skipfooter=9)["Data"]
    weekends = ["Saturday", "Sunday"]
    # Cria o calendário
    calendar = Calendar(holidays, weekends)
    return calendar

#########################################
## Obtaining DI Futures Contracts data ##
#########################################

cal = brazil_calendar()

r = requests.get('https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-ajustes-do-pregao-ptBR.asp')
s = bs(r.content, 'html.parser')

dataref = s.find('input', id = 'dData1').get('value')
dataref = datetime.strptime(dataref, '%d/%m/%Y').strftime('%Y-%m-%d')

tb = s.find('table', id = 'tblDadosAjustes')

lines = [l.find_all('td') for l in tb.findAll('tr')[1:]]

df = pl.DataFrame([[i.text for i in l] for l in lines])

print(df)

#########################
## Formatting the data ##
#########################

df = df[[0, 1, 3]]
df.columns = ['Ativo', 'Cod-Vencimento', 'ValorAjuste']

df['ValorAjuste'] = df['ValorAjuste'].str.replace('.', '').str.replace(',', '.').astype(float)

# preenche os valores vazios na coluna com o nome da mercadoria
df['Ativo'] = df['Ativo'].replace('', None)

# tira os espaços vazios da coluna código de vencimento
df['CodVcto'] = df['CodVcto'].str.strip()

# mantem apenas os futuros de DI
df = df[df['Ativo'].str.startswith('DI1')]