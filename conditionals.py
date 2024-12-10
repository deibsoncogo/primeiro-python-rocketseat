idade = 18

if idade != 10:
  print("Você não tem 10 anos")

if idade == 17:
  print("Você tem 17 anos")


if idade >= 18:
  print("Você é maior de idade")
elif idade >= 12:
  print("Você é um adolescente")
else:
  print("Você é menor de idade")


message = "Emissão da CNH liberada" if idade >= 18 else "Você não pode ter uma CNH"
print(message)
