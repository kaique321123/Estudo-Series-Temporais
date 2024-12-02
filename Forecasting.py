import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Carregar o dataset
df = pd.read_csv('C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\UDEMY_TSA_FINAL\\Data\\airline_passengers.csv',
                 index_col='Month', parse_dates=True)
df.index.freq = 'MS'

# Convertendo a coluna 'Thousands of Passengers' para float64, pois estava dando erro na hora de prever por resultar em valores maiores que o int suporta
# não adiantou, parece que mesmo assim estoura a quantidade de valores que o float suporta, mas ele rodou corretamente

df['Thousands of Passengers'] = df['Thousands of Passengers'].astype('float64')

# Se você quer prever 1 ano você deve ter pelo menos 10 ano de dados para usar no treinamento ou 80% usa para treino e 20% para teste
# e assim obter resultados mais precisos
#print(df.info())

# Separar dados de treino e teste
# Peguei 109 dias para treino
train_data = df.iloc[:109]  #.loc[:'1940-0101'] se quisesse selecionar por data e não por index
test_data = df.iloc[108:]   # Dados de 108 em diante para teste

# Ajustar o modelo Exponential Smoothing
fitted_model = ExponentialSmoothing(train_data['Thousands of Passengers'],
                                    trend='mul',
                                    seasonal='mul',
                                    seasonal_periods=12).fit()

# O método forecast() é utilizado para prever os dados de teste, cada linha nesses dados tem 1 mês
# então se quiser prever 1 mês a frente você deve passar 12 como argumento
test_predictions = fitted_model.forecast(36)
#print(test_predictions)

train_data['Thousands of Passengers'].plot(legend=True, label ='TRAIN DATA', figsize=(12,8))
test_data['Thousands of Passengers'].plot(legend=True, label='TEST DATA')
test_predictions.plot(legend=True, label = 'PREDICTIONS', xlim=['1958-01-01','1961-01-01'])
#plt.show()



# Algumas formas de avaliar o modelo são:
# Quando nós permormamos com forecast para valores continuos no conjunto d eteste nós temos 2 valores
# y - o valor real do daddo
# ŷ - o valor previsto

# Mean Absolute Error (MAE) - o problema com MAE é que ele é simplesmente a média dos residuos,
# ele não vai nos alertar se nosso forecast estiver fora em alguns pontos, e nós queremos ser alertados
# sobre qualquer erro que seja muito grande, ainda que forem poucos
# exemplo: nós não queremos errar 500% em um mês e não ser alertado só pq acertamos os outros meses

# Mean Squared Error (MSE) - é possível notar erros grandes agora, mas temos um problema, agora todos
# os nossos valores estão ao quadrado
#ex: se nosso resultado é em dolar o resultado seria em dolar ao quadrado, então não é muito intuitivo

# Root Mean Squared Error (RMSE) - então por isso criaram a raiz quadrada do MSE, para voltar ao valor original
# mas a resposta se temos um bom RMSE é subjetiva, depende do problema, pois há casos que esse valor é aceitável
# e outros que é ináceitavel






