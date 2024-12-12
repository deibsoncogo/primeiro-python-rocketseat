def greeting(name):
  print(f"Olá, {name}")

def square(number):
  result = number ** 2
  return result

def sum(number1, number2):
  result = number1 + number2
  return result

print("Chamando a função de saudação:")
greeting("Gustavo")

resultSquare = square(4)
print(f"O resultado da função quadrado é de {resultSquare}")

resultSum = sum(5, 8)
print(f"O resultado da função soma é de {resultSum}")
