# criando uma lista (array)
myList = [5, 1, 4, 2, 1, "rocketseat", True, False]

# formas de exibir a lista
print("Minha lista, completa:", myList)
print("Minha lista, 6º elemento:", myList[5])
print("Minha lista, 2º ao 5º elemento:", myList[1:5])
print("Minha lista, a partir do 2º elemento:", myList[1:])

# adicionar o último elemento
myList.append(6)

# retorna o index do elemento
myList.index(6)

# adicionar um elemento no index informado
myList.insert(2, 10)

# remove um elemento no index informado
myList.pop(3)

# remove o elemento informado
myList.pop(True)

# organiza os elementos da lista do mesmo tipo de dado
myList[0:4].sort()
