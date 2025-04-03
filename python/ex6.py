# 6. Inverta um array
# Dado um array, retorne um novo array com os elementos invertidos.

from utils import array

array_invertido = []

for i, _ in enumerate(array):
    array_invertido.append(array[(len(array) - 1) - i])

print(array_invertido)