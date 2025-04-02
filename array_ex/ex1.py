# Encontre o maior número
# Dado um array, retorne o maior número presente nele.

# Função de gerar arrays

from utils import gerar, mostrar_array

array = gerar()

mostrar_array(array)

maior = 0

for number in array:
    if number > maior:
        maior = number

print(f"Maior número: {maior}")