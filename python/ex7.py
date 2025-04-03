# 7. Remova duplicatas
# Dado um array com números repetidos, retorne um novo array apenas com
# valores únicos.

from utils import array

array_unico = []
array_unico.append(array[0])

for num in array:
    if num not in array_unico:
        array_unico.append(num)

print(array_unico)