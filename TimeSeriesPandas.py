from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.pyplot import autoscale

# my_year = 2005
# my_month = 2
# my_day = 10
# my_hour = 10
# my_minute = 30
# my_second = 15

# my_date  = datetime(my_year, my_month, my_day)
# print(my_date)

# my_date_time = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)
# print(my_date_time)

# np.array(["2005-02-10", "2024-11-05", "2013-03-15"],dtype = 'datetime64 [h] ')
#antes do dtype está de quanto em quanto tempo vai pular e o datetime64[] é em que quantidade de tempo que vai pular, semanas, dias, anos, meses...
# pt = np.arange("2005-02-10", "2024-11-05",3, dtype = 'datetime64 [Y]')
# np.arange(0,10,2)

# pt = np.arange("2005-02-10", "2024-11-05",3, dtype = 'datetime64 [Y]')
# print(pt)

# df = pd.date_range("2020-01-01", periods = 7, freq = 'D')
# print(df)

# A coluna Date deixa de ser uma coluna e se torna um index
# parse_dates = True, transforma a coluna Date em um objeto datetime

# print(df.head())
#
# print(df.info())
# print(df.index)

# usado transformar uma data diária em anual daily -> yearly
# print(df.resample(rule='A').mean())


# def first_day(entry):
#
#     # checar se a entrada é vazia
#     if len(entry) != 0:
#         return entry[0]
#
#
# print(df.resample(rule="A").apply(first_day))

# df["Close"].resample("A").mean().plot.bar()
# plt.show()

# Exibe de forma anual
# df["Close"].resample("A").mean().plot.bar(title = "Yearly Mean Closing Price for Starbucks", color = ["red", "blue", "green", "yellow", "orange", "black", "purple"])
# plt.show()

# Exibe de forma mensal
# df["Close"].resample("M").max().plot.bar(title = "Yearly Mean Closing Price for Starbucks", color = ["red", "blue", "green", "yellow", "orange", "black", "purple"])
# plt.show()

##################################################################################################################################################################################################################


#print(df.head())

# Mostra as últimas linhas
#print(df.tail())

# Mostra a linha de cima copiada sobre a linha de baixo, teoricamente a primeira linha recebe valor null
# Se quiser que a primeira linha receba um valor específico no lugar do null, basta colocar o valor no fill_value
# print(df.shift(1, fill_value = 0))
# Mostra a linha de baixo copiada sobre a linha de cima, teoricamente a última linha recebe valor null
# print(df.shift(-1))


# Mostra por mês
#print(df.shift(periods = 1, freq = "ME").head())


df = pd.read_csv("C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\UDEMY_TSA_FINAL\\Data\\starbucks.csv", index_col= 'Date', parse_dates = True)
#print(df.head())
#print(df.index)

# se não estivesse com index em formato de data, poderia fazer isso
# df.index = pd.to_datetime(df.index)


# df["Close"].plot(figsize = (12,5))
# plt.show()

# Os primeiros 7 dias não tem média, pois não tem 7 dias para calcular a média, então recebem NULL
#print(df.rolling(window = 7).mean())
# Esse window é o tamanho da janela que vai ser calculado a média, nesse caso 30 dias
# df.rolling(window = 60).mean()["Close"].plot()
#plt.show()


# Adiciona uma nova coluna com a média dos últimos 30 dias
# df["Close: 30 Day Mean"] = df["Close"].rolling(window=30).mean()

# Criando um gráfico com a coluna Close e Close: 30 Day Mean para comparar a média mensal em relação ao fechamento real
# assim com os dados de pelo menos metade do mês é possível observar um padrão
# df[["Close", "Close: 30 Day Mean"]].plot(figsize=(12, 5))
#plt.show()

# Se quisesse expandir isso para um período maior e contar com dados que ainda não temos, podemos usar o método expanding
#df["Close"].expanding().mean().plot(figsize=(12, 5))
#plt.show()


# df.plot()
# plt.show()
#
# df["Close"].plot()
# plt.show()
#
# df["Volume"].plot()
# plt.show()



# Se quiser adicionar nome nos eixos é possível fazer assim e adicionar a variável na hora da chamada
# ou pode adicionar uma string diretamente na chamada do método
title = "Starbucks Closing Stock Prices"
ylabel = "Closing Price (USD)"
xlabel = "Closing Date"

#ax = df["Close"].plot(figsize = (12,6), title = title)
#ax.set(xlabel = xlabel, ylabel = ylabel)
#plt.show()

# se quiser escalar automaticamente o gráfico é só usar
#ax.autoscale(axis = "both", tight = "True")
# pode passar ambos os eixos ou só um deles

# Caso queira selecionar específicos períodos de tempo
#df["Close"]["2017-01-01":"2017-12-31"].plot(figsize = (12,4))
#plt.show()

# ou se quiser pode usar o perído de tempo no final, mas a forma que plota o gráfico muda, pois ele abstrai depois que plotou o gráfico
# alterando a forma que o dado é exibido, pois ele reescala o gráfico no final
#df["Close"].plot(figsize = (12,4), xlim = ["2017-01-01", "2017-12-31"])
plt.show()

# Se quiser colocar limites no eixo y pode fazer assim
#df["Close"].plot(figsize = (12,4), xlim = ["2017-01-01", "2017-12-31"], ylim = [0,70])
#plt.show()

# Se quiser estilizar a linha pode
# ls para mudar o traço e c para mudar a cor
# Tem que ser aspas simples
#df["Close"].plot(figsize = (12,4), xlim = ["2017-01-01", "2017-12-31"], ylim = [40,70], ls = '--', c = 'green')
#plt.show()


ax = df["Close"].plot(xlim = ["2017-01-01", "2017-03-01"], ylim = [50,60], figsize = (12,4))
ax.set(xlabel = " " )

# byweekday = 0 é para começar a semana na segunda-feira
# usar locator quando quer controlar o eixo x
ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday = 0))

# usar formatter quando quer controlar o formato do eixo x
#ax.xaxis.set_major_formatter(dates.DateFormatter('%a-%B-%d'))

ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_locator(dates.MonthLocator())

# Se quiser adicionar espaço pode digitar apenas \n\n
ax.xaxis.set_minor_formatter(dates.DateFormatter("\n\n%b"))

# Se quiser adicionar grade no gráfico
#LINHAS NA HORIZONTAL
ax.yaxis.grid(True)
#LINHAS NA VERTICAL
ax.xaxis.grid(True)
plt.show()


# Para conseguir ver o tipo dos dados das colunas utilizar
df.dtypes

# Para converter uma coluna para o tipo datetime
df["Date"] = pd.to_datetime(df["Date"])

#Converter coluna para index
df = df.set_index('Date')

# don't work because Date is a index
#df["Month"] = df["Date"].dt.month

# this work when Date is a index
df['Month']=df.index.month
df.head()