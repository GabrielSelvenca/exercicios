# 8. Rotacione um array para a direita
# Dado um array e um número k, rotacione os elementos k vezes para a direita.

from utils import array

while True:
    try:
        k = int(input("Digite o valor de K (número)"))
        break
    except:
        print("Digite um NÚMERO")
        continue
    
n = len(array)
k %= n

print(f"Array invertido: {array[-k:] + array[:-k]}")