# 9. Soma de todos os elementos da matriz
# Dada uma matriz N x M, retorne a soma de todos os seus elementos.

from utils import matriz

soma = 0

for rows in matriz:
    for num in rows:
        soma+=num

print(f"Soma é: {soma}")