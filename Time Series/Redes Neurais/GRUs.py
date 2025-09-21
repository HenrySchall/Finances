import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sm
import math
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU, Dropout
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('all-stocks-5yr.csv')

df.head()

companies = df.Name.unique()
companies

#Zoetis Inc
z = df.loc[df['Name'] == 'ZTS']
z.info()

z.head()

trainingd = z.iloc[:, 4:5].values

trainingd

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
training_set_scaled = sc.fit_transform(trainingd)

#array de 3 dimensões esparado pelo lstm
#linhas
#sequencia: 45
#features: 1
x_train = []
y_train = []
timestamp = 45
length = len(trainingd)
for i in range(timestamp, length):
    x_train.append(training_set_scaled[i-timestamp:i, 0])
    y_train.append(training_set_scaled[i, 0])

x_train = np.array(x_train)
y_train = np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape

model = Sequential()
model.add(GRU(units = 120, return_sequences = True, input_shape = (x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(GRU(units = 120, return_sequences = True))
model.add(Dropout(0.2))
model.add(GRU(units = 120, return_sequences = True))
model.add(Dropout(0.2))
model.add(GRU(units = 120, return_sequences = False))
model.add(Dropout(0.2))
model.add(Dense(units = 1))
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(x_train, y_train, epochs = 25, batch_size = 32)

#vamos testar com outra empresa Boeing
test_set = df.loc[df['Name'] == 'BA']
test_set = test_set.loc[:, test_set.columns=='close']

y_test = test_set.iloc[timestamp:,0:].values

closing_price = test_set.iloc[:,0:].values
closing_price_scaled = sc.transform(closing_price)

x_test = []
length = len(test_set)

for i in range(timestamp, length):
    x_test.append(closing_price_scaled[i-timestamp:i,0])

x_test = np.array(x_test)
x_test.shape

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))
x_test.shape

y_pred = model.predict(x_test)
predicted_price = sc.inverse_transform(y_pred)

plt.plot(y_test, color='blue', label='Preço Atual das Ações')
plt.plot(predicted_price, color='red', label='Preço Previsto das Ações')
plt.title('Previsão de Preço de Ações')
plt.xlabel('Tempo')
plt.ylabel('Preço das Ações')
plt.legend()
plt.show()