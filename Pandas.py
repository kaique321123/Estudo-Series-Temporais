import pandas as pd
import numpy as np
from numpy.random import randn

# np.random.seed(101)
#
# labels = ["a","b","c"]
# mylist = [10,20,30]
#
# arr = np.array(mylist)
#
# #print(arr)
#
#
# d = {"a":10,"b":20,"c":30}
#
# # print(pd.Series(data = mylist))
# #
# # print(pd.Series(data = arr,index = labels))
#
# # basicamente é um array com index
# #print(pd.Series(data=[10,"a",4.4]))
#
# ser1 = pd.Series([1,2,3,4], index = ["USA", "Germany", "URSS"," Japan"])
# #print(ser1)
#
# # print(ser1["Germany"])
#
# ser2 = pd.Series([1,2,5,4], index = ["USA", "Germany", "Italy"," Japan"])
#
# print(ser1 + ser2)


# Um "df" com 5 linhas e 4 colunas de valores aleatórios
# rand_mat = randn(5,4)

#print(rand_mat)

# Com esse split adiciona "virgula" automaticamente entre os espaços
# df = pd.DataFrame(data = rand_mat, index = "A B C D E".split(), columns = " W X Y Z".split())
# #print(df)
#
# #se quiser pegar mais de uma coluna
# mylist = ["W","Y"]
# # print(df[["W","Y"]])
# # print(df[mylist])
#
# df["NEW"] = df["W"] + df["Y"]
# #print(df)
#
# Contar os itens que aparecem na coluna de forma unica
# df["Col2"].nunique()
#
# # Apagar as colunas
# df.drop("NEW",axis=1, inplace = True)
#
# # Apagar as linhas
# df.drop("A", axis = 0)

#Selecionar linha
# print(df.loc["A"])
# print(df.iloc[0])

#Selecionar múltiplas linhas
#Usa braços duplos quando for mais de uma linha (uma lista)
# print(df.loc[["A","E"]])
# print(df.iloc[[0,3]])

#Primeiro passa a linha e depois a coluna
#print(df.loc[["A","B"]][["Y","Z"]])

# RETORNA UM DATAFRAME COM BOOLEANOS
#print(df > 0 )
# df_bool = df > 0

# Retorna uma série com booleanos que satisfazem a condição em uma coluna
#print(df["W"]> 0 )

#Retorna uma série com os valores que satisfazem a condição para o df inteiro
#print(df[df["W"]> 0 ])

#print(df[df["W"]> 0]["Y"].loc["A"] )

# cond1 = df["W"] > 0
# cond2 = df['Y'] > 1
# and = &, or = |
# print(df[(cond1) & (cond2)])

# new_ind = "CA NY WY OR CO".split()
#print(new_ind)

# df["States"] = new_ind
#print(df)

# df.set_index("States")
#print(df)

# Informações sobre o dataframe
#print(df.info())

# Estatísticas sobre o dataframe
#print(df.describe())


# ser_w = df["W"] > 0
# print(ser_w)
#
# print(sum(ser_w))

#df = pd.DataFrame({"A":[1,2,np.nan],"B":[5,np.nan, np.nan],"C":[1,2,3]})
#print(df)

# Remove qualuqer linha que tenha valores nulos
#df.dropna()
#print(df)

# Remove qualquer coluna que tenha valores nulos
#print(df.dropna(axis = 1))

#Remove linhas que tenham no mínimo 2 valores nulos
#print(df.dropna(thresh = 2))

#Preencher valores nullos com alguma coisa
#print(df.fillna(value = "FILL VALUE"))
#print(df.fillna(value = 0))
#print(df.fillna(value = df.mean()))
#print(df["A"].fillna(value = df["A"].mean()))

# data = {"Company": ["GOOG","GOOG","MSFT","MSFT","FB","FB"],
#         "Person": ["Sam","Charlie","Amy","Vanessa","Carl","Sarah"],
#         "Sales": [200,120,340,124,243,350]
#       }
# #Colunas Primeiro e depois linha dentro das chaves
#
# df = pd.DataFrame(data)
#
# #print(df)
#
# # transpose transforma as linhas em colunas e as colunas em linhas
# print(df.groupby("Company")["Sales"].describe().transpose())

# Primeiro é o nome da coluna, dois ponto ":", e o valor que queremos nas linhas
df = pd.DataFrame({"col1":[1,2,3,4],"col2":[444,555,666,444],"col3":["abc","def","ghi","xyz"]})
#print(df.head())

# Retorna os valores únicos
#df["col2"].unique()

# Retorna a quantidade de valores únicos
#df["col1"].nunique()

# Retorna a quantidade de vezes que cada valor aparece
#df["col2"].value_counts()

# Col1 é maior que 2
# Col2 é igual a 444
# newdf = df[(df["col1"] > 2) & (df["col2"] == 444)]
# #print(newdf)
#
#
# def times_two(number):
#     return number * 2
#
# print(times_two(4))
#
#
# #Usar função em uma coluna
# df["new"] = df["col1"].apply(times_two)
# #print(df, "\n")
#
# #Deletar coluna
# #del df["new"]
#
# #Outra forma, mas da mais trabalho
# df.drop("new", axis=1, inplace = True)
# #print(df)
#
# #Retorna o nome das colunas
# df.columns
#
# #Retorna o index
# df.index
#
# #Retorna os tipos, nome de colunas, se há valores nulos, tamanho da memória, etc
# df.info()
#
# Exibir em ordem dados de alguma coluna
# df = df.sort_values(by = "col2", ascending = False)
# print(df)


excel = pd.read_csv("example.csv")
# excel_dois = pd.read_csv("C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\Estudo-Series-Temporais\\example.csv")
# print(excel_dois)

new_df = excel[['a','b']]
#print(new_df)

# Só deixar o index = True se quiser aquelas números que identificam a linha
# Comando para salvar o arquivo
new_df.to_csv("my_file.csv", index = False)

df = pd.read_excel("C:\\Users\\KaiquedeJesusPessoaS\\Desktop\\Estudo-Series-Temporais\\Excel_Sample.xlsx", sheet_name = "Sheet1")
print(df)