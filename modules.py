# exemplo de importação de um módulo padrão
import math
raiz = math.sqrt(25)
print(f"A raiz quadrada de 25 é {raiz}")

# exemplo de importação de um módulo específico
from math import sqrt
raiz = sqrt(196)
print(f"A raiz quadrada de 196 é {raiz}")

# utilizando um módulo próprio
from myModule import greeting, doubleSum
greeting("Gustavo Antonio")
doubleSum()
