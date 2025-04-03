# 16. Verifique se uma matriz é simétrica
# Uma matriz quadrada é simétrica se for igual à sua transposta.

from utils import matriz

matriz = matriz[:25]

def simetrica():
    size = len(matriz)
    
    for i in range(size):
        for j in range(size):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

print("A matriz é simétrica" if simetrica() else "Não é simétrica")