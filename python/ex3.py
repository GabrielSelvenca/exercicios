# 3. Calcule a soma dos elementos
# Dado um array, calcule a soma de todos os seus elementos.

from utils import array

soma = 0

for i in array:
    soma+=i

print(f"Soma total: {soma}")