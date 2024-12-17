# forma de tratar as mensagens de erros

print("Exemplo de captura de exceções")

try:
  number = int(input("Digite um número inteiro: "))

  result = 10 / number

except ValueError as error:
  print(f"Error value: {error}")
  raise ValueError("Tipo de valor deve ser um número inteiro")

except Exception as error:
  print(f"Error: {error}")

else:
  print(f"O resultado foi de {result}")

finally:
  print("Operação finalizada")
