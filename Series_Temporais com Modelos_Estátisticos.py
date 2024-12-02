# Há trends que indicam uma tendência de crescimento ou decrescimento ao longo do tempo.
# Sasonalidade é a repetição de padrões ao longo do tempo (repetrição de trends).
# Ciclico são padrões que não se repetem em intervalos fixos.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing


# Usa isso para definir um tamanho padrão para os gráficos
rcParams["figure.figsize"] = 12,5

df =  pd.read_csv("C:/Users/KaiquedeJesusPessoaS/Desktop/UDEMY_TSA_FINAL/Data/macrodata.csv", index_col = 0, parse_dates = True)
#print(df.head())


df["realgdp"].plot()
plt.show()

# é um valor padrão para o filtro HP
lamb = 1600 
gdp_cycle, gdp_trend = hpfilter(df['realgdp'], lamb = 1600)

print(type(gdp_trend))

gdp_trend.plot()
plt.show()

df["trend"] = gdp_trend
print(df.head())

df[['trend', 'realgdp']]["2005-01-01":].plot()
plt.show()


# ETS Models (Error-Trend-Seasonality)
# Uma abordagem para modelar séries temporais que consiste em três componentes: erro, tendência e sazonalidade.
# Utiliza alguens pontos como o Erro = Ruído/Incerteza da série, Tendência = Crescimento, Decrescimento ou estável, Sazonalidade = Padrões de repetição em períodos fixos.


# Modelo Aditivo = y(t) = Tendência + Sazonalidade + Erro
# Quando a trend é mais linear, a sazonalidade e os componentes da trend são mais constantes no decorrer do tempo.
# Ex: a cada ano a quantidade de passageiros aumenta em 1000

# Modelo Multiplicativo = y(t) = Tendência * Sazonalidade * Erro
# Quando está aumentando ou diminuindo de forma não linear
# Ex: todo ano dobra a quantidade de passageiros

airline = pd.read_csv("C:/Users/KaiquedeJesusPessoaS/Desktop/UDEMY_TSA_FINAL/Data/airline_passengers.csv", index_col = "Month")
#print(airline.head())
# Não pode ter valores nulos quando performa com ETS
airline = airline.dropna()

airline.plot()
plt.show()

# Já que todo ano aumenta de forma não linear, vamos usar o modelo multiplicativo nesse dataframe
result = seasonal_decompose(airline["Thousands of Passengers"], model = "multiplicative")
print(result.trend)

result.plot()
plt.show()


#EWMA Models
# SMA - Simple Moving Averages - Média simples dos últimos N períodos
# EWMA - Exponential Weighted Moving Averages - Média ponderada dos últimos N períodos (basicamente é a expansão da idéia de SMA)

airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)
print(airline.head())


airline["6-month-SMA"] = airline["Thousands of Passengers"].rolling(window=6).mean()
airline["12-month-SMA"] = airline["Thousands of Passengers"].rolling(window=12).mean()
airline.plot(figsize=(12,5))
plt.show()

# O problema do SMA é que ele não é muito responsivo a mudanças, então vamos usar o EWMA, pois ele dá mais peso aos valores mais recentes
airline["EWMA-12"] = airline["Thousands of Passengers"].ewm(span=12).mean()

airline[["Thousands of Passengers", "EWMA-12"]].plot()
plt.show()


# HOLY - Winters Methods Theory
# Modelo aditivo tem um alfa e ele melhor se utilizado quando os dados tem um padrão de crescimento constante
# Modelo multiplicativo tem um beta e um alfa e ele é melhor se utilizado quando os dados tem um padrão de crescimento não constante
# o alfa e beta são arbitrários e podem ser ajustados para melhorar a previsão, se você quer que o modelo seja mais reativo a dados recente, aumente o alfa e beta
# se quiser que o modelo de mais ênfase a dados antigos, diminua o alfa e beta
# está separando em dois valores basicamente o valor verdadedeiro/real e o valor trend

# Esse modelo tem TREND, SEASONAL e LEVEL (em quantas partes vai dividir a sazonalidade))


df = pd.read_csv("C:/Users/KaiquedeJesusPessoaS/Desktop/UDEMY_TSA_FINAL/Data/airline_passengers.csv", index_col = "Month", parse_dates = True)
#print(df.head())

df = df.dropna()

#print(df.index)

# O modelo estatístico vai analisar o freq e ele precisa ser diferente de None
# MS pois nesse caso a série segue um padrão de começar todo início de mês
df.index.freq = 'MS'

#print(df.index)

# span = 2 pq vamos dividir em 12 meses
span = 12
alpha = 2/(span+1)

# alpha = alpha pois vamos deixar para o algoritmo encontrar o alpha
df['EWMA12'] = df['Thousands of Passengers'].ewm(alpha=alpha,adjust = False).mean()
# EWMA12 tem basicamente uma média exponencial
#print(df.head())

model = SimpleExpSmoothing(df['Thousands of Passengers'])
fitted_model = model.fit(smoothing_level=alpha, optimized=False)
#print(fitted_model.fittedvalues.shift(-1))

df['SES12'] = fitted_model.fittedvalues.shift(-1)

# Isso faz com que o SES12 seja a média exponencial do valor anterior
df['SES12'] = SimpleExpSmoothing(df['Thousands of Passengers']).fit(smoothing_level= alpha, optimized = False).fittedvalues.shift(-1)
#print(df.head())
df.plot()
plt.show()

df['DES_add_12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend = 'add').fit().fittedvalues.shift(-1)
#print(df.head())

# iloc[:24] é utilizado para pegar os 24 primeiros meses ou primeiros 2 anos
#df[['Thousands of Passengers', 'SES12', 'DES_add_12']].iloc[:24].plot(figsize = (20,5))

# Se quisermos os últimos 2 anos, basta mudar o iloc para [-24:]



# Se ficar difícil saber se usa o modelo aditivo ou multiplicativo, teste com os dois e veja o que se adapta melhor ao problema

df['DES_mult_12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend = 'mul').fit().fittedvalues.shift(-1)
df[['Thousands of Passengers', 'SES12', 'DES_add_12','DES_mult_12']].iloc[-24:].plot(figsize = (20,5))
df[['Thousands of Passengers', 'SES12', 'DES_add_12','DES_mult_12']].iloc[:24].plot(figsize = (20,5))
plt.show()


# Triplo Modelo Exponencial

# Se adicional o seasonal_periods = 12, ele vai dividir a sazonalidade em 12 partes e não precisa adicionar o fittedvalues com shift
df['TES_mul_12'] = ExponentialSmoothing(df['Thousands of Passengers'], trend = 'mul', seasonal = 'mul', seasonal_periods=12).fit().fittedvalues
df.plot()

df[['Thousands of Passengers', 'DES_add_12','TES_mul_12']].iloc[-24:].plot(figsize = (12,6))
df[['Thousands of Passengers', 'DES_add_12','TES_mul_12']].iloc[:24].plot(figsize = (12,6))

plt.show()

