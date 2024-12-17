# principais função para as variáveis de tipo string

name = "Gabriel Grande"

print("Codifica para bit:", name.encode())
print("Decodifica de bit:", name.encode().decode())

print("Texto em maiúsculo:", name.upper())
print("Texto em minúsculo:", name.lower())

print("Conta quantos a existem:", name.count("a"))
print("Retornar a posição do primeiro a:", name.find("a"))

print("Substitui o texto:", name.replace("Grande", "G."))
print("Cria um array ao encontra o elemento:", name.split(" "))
print("Insere o elemento dentro do texto:", "-".join(name))

print("Se o texto tem x no começo e fim:", name.strip("x"))
print("Se o texto tem x no fim:", name.rstrip("x"))

print("Se o texto começa com Ga:", name.startswith("Ga"))

print("Se o texto tem el:", "el" in name)
print("Se o texto não tem el:", "el" not in name)
