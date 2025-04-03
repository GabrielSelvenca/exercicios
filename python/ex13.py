# 13.Diagonal principal
# Dada uma matriz quadrada N x N, retorne os elementos da sua diagonal principal.

from utils import matriz

matriz = matriz[:25]
i=0

for row in matriz:
    print(row[i])
    i+=1