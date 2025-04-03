# 12. Soma de cada coluna
# Dada uma matriz, calcule a soma dos elementos de cada coluna e exiba os
# resultados.

from utils import matriz

soma = 0
i = 0

while i < len(matriz[0]):
    for row in matriz:
        soma+=row[i]
    print(f"Soma da coluna [{i+1}]: {soma}")
    soma = 0
    i+=1