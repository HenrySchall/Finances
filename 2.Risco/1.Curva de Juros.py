# pip install xlrd
# pip install bizdays

import pandas as pd
import requests
import numpy as np
import calendar
import xlrd
from bizdays import Calendar
from datetime import datetime
from bs4 import BeautifulSoup as bs

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
df.columns = ['Ativo', 'Cod_Vencimento', 'ValorAjuste'] #Rename Columns

df['ValorAjuste'] = df['ValorAjuste'].str.replace('.', '').str.replace(',', '.').astype(float) #Replace , for .

df = df.iloc[223:263] #Select DI value lines

df['Ativo'] = np.nan
df['Ativo'] = df['Ativo'].fillna('DI1')
df['CodVcto'] = df['CodVcto'].str.strip() # Remove the empty spaces from the expiration code column
df = df[df['Ativo'].str.startswith('DI1')] #