import json


# pegar os dados de array.json e salvar em array para usar em outros códigos
with open("array.json", "r") as a:
    array = json.load(a)

# pegar os dados de matriz.json e salvar em matriz para usar em outros códigos
with open("matriz.json", "r") as m:
    matriz = json.load(m)