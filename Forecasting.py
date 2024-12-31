import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.statespace.tools import diff
import statsmodels.api as sm
from statsmodels.tsa.stattools import acovf, acf, pacf, pacf_yw, pacf_ols
from pandas.plotting import lag_plot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# # Carregar o dataset
# df = pd.read_csv('C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\UDEMY_TSA_FINAL\\Data\\airline_passengers.csv',
#                  index_col='Month', parse_dates=True)
# df.index.freq = 'MS'
#
# # Convertendo a coluna 'Thousands of Passengers' para float64, pois estava dando erro na hora de prever por resultar em valores maiores que o int suporta
# # não adiantou, parece que mesmo assim estoura a quantidade de valores que o float suporta, mas ele rodou corretamente
#
# df['Thousands of Passengers'] = df['Thousands of Passengers'].astype('float64')
#
# #Se você quer prever 1 ano você deve ter pelo menos 10 ano de dados para usar no treinamento ou 80% usa para treino e 20% para teste
# #e assim obter resultados mais precisos
# #print(df.info())
#
# # Separar dados de treino e teste
# # Peguei 109 dias para treino
# train_data = df.iloc[:109]  #.loc[:'1940-0101'] se quisesse selecionar por data e não por index
# test_data = df.iloc[108:]   # Dados de 108 em diante para teste
#
# # Ajustar o modelo Exponential Smoothing
# fitted_model = ExponentialSmoothing(train_data['Thousands of Passengers'],
#                                     trend='mul',
#                                     seasonal='mul',
#                                     seasonal_periods=12).fit()
#
# # O método forecast() é utilizado para prever os dados de teste, cada linha nesses dados tem 1 mês
# # então se quiser prever 1 mês a frente você deve passar 12 como argumento
# test_predictions = fitted_model.forecast(36)
# print(test_predictions)
#
# train_data['Thousands of Passengers'].plot(legend=True, label ='TRAIN DATA', figsize=(12,8))
# test_data['Thousands of Passengers'].plot(legend=True, label='TEST DATA')
# test_predictions.plot(legend=True, label = 'PREDICTIONS', xlim=['1958-01-01','1961-01-01'])
# plt.show()
#
#
#
# # Algumas formas de avaliar o modelo são:
# # Quando nós permormamos com forecast para valores continuos no conjunto d eteste nós temos 2 valores
# # y - o valor real do daddo
# # ŷ - o valor previsto
#
# # Mean Absolute Error (MAE) - o problema com MAE é que ele é simplesmente a média dos residuos,
# # ele não vai nos alertar se nosso forecast estiver fora em alguns pontos, e nós queremos ser alertados
# # sobre qualquer erro que seja muito grande, ainda que forem poucos
# # exemplo: nós não queremos errar 500% em um mês e não ser alertado só pq acertamos os outros meses
#
# # Mean Squared Error (MSE) - é possível notar erros grandes agora, mas temos um problema, agora todos
# # os nossos valores estão ao quadrado
# #ex: se nosso resultado é em dolar o resultado seria em dolar ao quadrado, então não é muito intuitivo
#
# # Root Mean Squared Error (RMSE) - então por isso criaram a raiz quadrada do MSE, para voltar ao valor original
# # mas a resposta se temos um bom RMSE é subjetiva, depende do problema, pois há casos que esse valor é aceitável
# # e outros que é ináceitavel
#
# mean_squared_error_ = mean_squared_error(test_data, test_predictions)
# mean_absolute_error_ = mean_absolute_error(test_data, test_predictions)
#
# print(test_data.describe())
# # Tem uma média de 428,5 e um desvio padrão de 79,3
# # Já que o MAE deu 63,03 é possível dizer que o modelo está indo bem, pois o erro é menor que o desvio padrão
# print(f'Mean Squared Error: {mean_squared_error_}')
# print(f'Mean Absolute Error: {mean_absolute_error_}')
# # O RMSE deu 74,9 que é menor que o desvio padrão, então o modelo está indo bem
# print(f'raiz do MSE : {np.sqrt(mean_squared_error_)}')
#
# # Nosso modelo até agora está se ajustando bem aos dado já que teve valores de MAE e RMSE menor que o desvio padrão, então agora vamos prever para o futuro
#
# # Agora vamos prever para o futuro
# # O modelo já foi treinado com os dados de treino, então agora vamos prever para o futuro
# # seasonal_periods define o ciclo de sazonalidade dos dados e nesse caso são 12 meses, ou seja, a cada 12 meses os dados se repetem
# final_model = ExponentialSmoothing(df['Thousands of Passengers'],
#                                  trend='mul',
#                                  seasonal='mul',
#                                  seasonal_periods=12).fit()
# forecast_predictions = final_model.forecast((36))
#
# df['Thousands of Passengers'].plot(figsize=(12,8))
# forecast_predictions.plot()
# plt.show()
#
# # Dizemos que um dataset é estacionário quando ele não tem tendência e nem sazonalidade
# # ou seja, as flutuações nos dados são inteiramente devido a forças externas e ruídos
#
#
# # Vamos ver um dataset com isso
# # parse_dates=True é para transformar a coluna de data em datetime
# df2 = pd.read_csv('C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\UDEMY_TSA_FINAL\\Data\\samples.csv', index_col=0, parse_dates=True)
# #print(df2.head())
#
# # A coluna "a" não apresenta tendência e nem sazonalidade, então ela é estacionária
# df2["a"].plot()
# #plt.show()
# # Apesar dos dados não seguirem uma sazonalidade, eles ainda são previsíveis, pois eles seguem uma tendência
# df2['b'].plot()
# #plt.show()
#
# # para prever os dados como da coluna b podemos olhar o estácionário e ver o que é conhecido
# # como diferença e é um método simples que calcula a diferença entre pontos consecutivos
#
# #shift é um método que move os dados para cima ou para baixo, no caso de 1, move 1 para baixo
# # Assim é uma forma de fazer na mão
# #print(df2["b"] - df2["b"].shift(1))
#
# # O bom dessa função no lugar de fazer a mãe é que a primeira linha não fica com o valor nulo
# #diff(df2["b"],k_diff=1).plot()
# #plt.show()
# # após usar essa função o gráfico se transformou em um gráfico estaionário, ou seja, sem tendência e sem sazonalidade



# ACF e PACF
# ACF - AutoCorrelation Function - é uma medida de correlação entre um ponto e outro ponto em um intervalo de tempo
# PACF - Partial AutoCorrelation Function - é uma medida de correlação entre um ponto e outro ponto em um intervalo de tempo, mas
# Correlação é basicamente a relação entre 2 variáveis, então se uma variável aumenta a outra também aumenta e se uma diminui a outra diminui também


# NON STATIONARY
df1 = pd.read_csv('C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\UDEMY_TSA_FINAL\\Data\\airline_passengers.csv', index_col = 'Month', parse_dates=True)
df1.index.freq = 'MS'

# STATIONARY
df2 = pd.read_csv('C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\UDEMY_TSA_FINAL\\Data\\DailyTotalFemaleBirths.csv', index_col = 'Date', parse_dates = True)
df2.index.freq = 'D'


import warnings
warnings.filterwarnings('ignore')

df = pd.DataFrame({'a':[13,5,11,12,9]})
#print(df)

# Para ver a autocorrelação
#print(acf(df['a']))

# A conta é feita de quantas linhas tem menos 1 para o nlags
# mle é para maximum likelihood estimation
# bom quando tem muitos dados, assume que a série original é estacionário (sem tendência ou sazonalidade) e foi tratada antes de colocar no modelo
#print(pacf_yw(df['a'],nlags=4, method='mle'))
# ou pode usar para ter o mesmo resultado
#print(pacf_yw(df['a'], nlags=4, method='unbiased'))
# unbiased não roda

# O nlags deve ser pelo menos 2
nobs = len(df['a'])
# Ensure nlags is smaller than nobs // 2
nlags = nobs // 2 - 1

# utiliza regresões sucessivas no cálculo, ajusta o modelo aos dados, lento para calcular séries mais longas, mas é bom para calcular séries com
# propriedades não estácionárias
print(pacf_ols(df['a'], nlags=nlags))

lag_plot(df1['Thousands of Passengers']).plot()
#plt.show()
lag_plot(df2['Births']).plot()
#plt.show()

df1.plot()

# quanto mais lags mais pontos aparecem no gráfico
# gráfico de dados não estácionários
plot_acf(df1, lags=40)
#plt.show()

# gráfico estácionário
plot_acf(df2, lags=40)
#plt.show()

plot_acf(df2, lags = 40, title = "Daily Female Births")