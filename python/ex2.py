# 2. Encontre o menor número
# Dado um array, retorne o menor número presente nele.

from utils import array

menor = 9999

for numero in array:
    if numero < menor:
        menor = numero
        
print(f"Menor número: {menor}")