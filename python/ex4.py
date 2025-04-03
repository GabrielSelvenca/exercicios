# 4. Calcule a média dos elementos
# Dado um array de números, retorne a média dos valores.

from utils import array

soma = 0

for num in array:
    soma+=num
    
media = soma/len(array)

print(f"Média da array: {media}")