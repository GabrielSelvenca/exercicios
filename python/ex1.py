# Encontre o maior número
# Dado um array, retorne o maior número presente nele.

# Função de gerar arrays

from utils import array

maior = 0

for number in array:
    if number > maior:
        maior = number

print(f"Maior número: {maior}")