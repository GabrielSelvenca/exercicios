# 5. Conte os números pares e ímpares
# Dado um array de números inteiros, conte quantos são pares e quantos são
# ímpares.

from utils import array

impares = 0
pares = 0

for num in array:
    if num%2 == 0:
        pares+=1
    else:
        impares+=1
    
print(f"Total de números impares: {impares}\nTotal de números pares: {pares}")