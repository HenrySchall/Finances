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