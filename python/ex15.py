# 15. Transposta de uma matriz
# Dada uma matriz N x M, gere sua transposta (troque linhas por colunas).

from utils import matriz

rows = len(matriz)
cols = len(matriz[0])

novaMatriz = []

for j in range(cols):
    newR = []
    for i in range(rows):
        newR.append(matriz[i][j])
    novaMatriz.append(newR)
    
print(novaMatriz)