import numpy as np

#
# # mylist = [1,2,3]
# # #
# # # type(mylist)
# # #
# # # np.array(mylist)
# # #
# # # print(mylist)
# #
# # #print(type(mylist))
# #
# # arr = np.array(mylist)
# #
# # #print(arr)
# #
# # mylist = [[1,2,3,],[4,5,6],[7,8,9]]
# #
# # #print(mylist)
# #
# # my_matrix = np.array(mylist)
# # my_matrix.shape
# #
# # #tamanho da matriz
# # #print(my_matrix.shape)
# #
# # mynematrix = np.array(mylist)
# #
# # #não inclui 10
# #
# #
# # #uma matriz com 4 linhas e 10 colunas
# # print(np.zeros((4,10)))
# #
# # correto = np.linspace(0,10,20)
# #
# # print(correto)
# #
# # print(np.eye(4))
# # print(np.random.rand(5,5))
# #print(np.random.rand(3,3))
# #print(np.random.normal(1))
# #print(np.random.randint(1,100,10))
# # print(np.random.seed(555))
# # print(np.random.rand(5))
#
#
# # arr = np.arange(25)
# # print(arr)
# #
# # ranarr = np.random.randint(0,50,10)
# # print(ranarr)
# # #print(arr.shape)
# # arr = arr.reshape(5,5)
# # print(arr)
# #
# # print(ranarr.max())
# # print(ranarr.argmax())
#
# # arr = np.arange(0,11)
# # slice_array = arr[0:6]
# #
# # #Tudo dentro do array vai ser 99
# # #como slice pegou apenas um pedaço, aquela fatia vai ser 99 e o resto mantém
# # slice_array[:] = 99
# #
# # print(arr)
# #
# # #copy para copiar um array
# # array_copy = arr.copy()
# # array_copy[:] = 100
# # print(array_copy)
# #
# # arr2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
# # print(arr2d)
# # print(arr2d[1])
# # print(arr2d[2][2])
# # arr2d[2,2] = 10
# # print(arr2d)
# #
# # # Vai exibir as duas primeiras linhas
# # #arr2d = arr2d[:2]
# #
# # # Vai exibir as duas últimas colunas
# # arr2d = arr2d[:,2:]
# #
# # print("new", arr2d)
#
#
# array = np.arange(1,11)
# print(array)
# bool_array = array > 5
# array = array[bool_array]
# # igual array = array[array>5]
# print(array)


arr = np.arange(1,11)
arr = arr + 10
print("soma", arr.sum())
print("média", arr.mean())
print("máximo", arr.max())
print("mínimo", arr.min())

arr_2d = np.array(([1,2,3,4],[5,6,7,8],[9,10,11,12]))
print(arr_2d)
# print("soma", arr_2d.sum())
#Soma por coluna
print("soma das colunas", arr_2d.sum(axis=0))
#Soma por linha
print("soma das linhas", arr_2d.sum(axis=1))

# print("média", arr_2d.mean())
# print("máximo", arr_2d.max())
# print("mínimo", arr_2d.min())
# print("raiz quadrada", np.sqrt(arr_2d))
# print("exponencial", np.exp(arr_2d))
# print("seno", np.sin(arr_2d))
# print("logaritmo", np.log(arr_2d))

