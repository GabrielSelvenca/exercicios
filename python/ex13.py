# 13.Diagonal principal
# Dada uma matriz quadrada N x N, retorne os elementos da sua diagonal principal.

from utils import matriz

matriz = matriz[:25]

for i, row in enumerate(matriz):
    print(row[i])