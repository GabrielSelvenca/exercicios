# 14.Diagonal secundária
# Dada uma matriz quadrada N x N, retorne os elementos da sua diagonal
# secundária.

from utils import matriz

matriz = matriz[:25]

n = len(matriz)

for i in range(n):
    print(matriz[i][n - 1 - n])