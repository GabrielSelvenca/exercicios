# 10. Encontre o maior elemento de uma matriz
# Dada uma matriz N x M, encontre o maior número presente nela.

from utils import matriz

maior = 0

for rows in matriz:
    for num in rows:
        if num > maior:
            maior = num
            
print(f"O maior número é: {maior}")