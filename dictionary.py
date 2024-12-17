# um dicionário não é ordenado e possui uma chave e valor

people = { "name": "João", "age": 30, "city": "São Paulo" }

print("Valores do dicionário pessoa:", people)

print("Nome salvo no dicionário:", people["name"])
print("Idade salvo no dicionário:", people["age"])
print("Cidade salvo no dicionário:", people["city"])

#  forma para criar um novo valor
people["isActive"] = True

print("A pessoal está ativa?", people["isActive"])

# forma de excluir um valor
del people["city"]

print("Chaves do dicionário no formato dict:", people.keys())
print("Chaves do dicionário no formato lista:", list(people.keys()))

print("Valores do dicionário no formato dict:", people.values())
print("Valores do dicionário no formato lista:", list(people.values()))

print("Transforma o dicionário em tupla dict:", people.items())
print("Transforma o dicionário em tupla lista:", list(people.items()))
print("Exibe o o segundo valor da primeira tupla:", list(people.items())[0][1])
