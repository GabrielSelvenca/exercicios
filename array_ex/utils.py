import random

def generate_array(n,min_val=0,max_val=1):
  numeros = [random.randint(min_val, max_val) for _ in range(n)]
  random.shuffle(numeros)
  return numeros

def gerar():
    numeros = generate_array(1000,0,11500)
    return numeros

def mostrar_array(array):
    try:
        resposta = int(input("Deseja mostrar o array ou apenas pular para a lógica?\n\n[1] Mostrar\n[2] Pular\n"))
        if resposta == 2:
            print("Pulando...")
            return
        print(f"{array}\n\n\n")
    except:
        print("Valor incorreto, pulando...")
        return