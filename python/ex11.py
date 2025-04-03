# 11. Soma de cada linha
# Dada uma matriz, calcule a soma dos elementos de cada linha e exiba os
# resultados.

from utils import matriz

soma = 0

for i, rows in enumerate(matriz):
    for num in rows:
        soma+=num
    print(f"Soma linha {i + 1}: {soma}")
    soma = 0