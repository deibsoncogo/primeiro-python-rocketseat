# o for é utilizado para criar loops

people = { "name": "João", "age": 30, "city": "São Paulo" }
list = [1, 2, 3, 4, 5]

for element in list:
  print(element)

print("\nUsando o keys")
for key in people.keys():
  print(key)

print("\nUsando o values")
for value in people.values():
  print(value)

print("\nUsando o items")
for key, value in people.items():
  print(f"{key}, {value}")

print("\nUsando o range")
for number in range(5):
  print("Número:", {number})

print("\nUsando o range com o len")
for index in range(0, len(list)):
  print(f"index {index}, list {list[index]}")

print("\nUsando o enumerate")
for index, value in enumerate(list):
  print(f"index {index}, list {value}")
