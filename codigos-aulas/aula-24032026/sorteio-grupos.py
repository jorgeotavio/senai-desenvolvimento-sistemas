import random
import time

def sortear_grupos(nomes, tamanho_grupo=3):
    nomes_disponiveis = nomes.copy()
    selecionados = []
    grupos = []

    while len(nomes_disponiveis) > 0:
        if len(nomes_disponiveis) < tamanho_grupo:
            grupo = nomes_disponiveis.copy()
        else:
            grupo = random.sample(nomes_disponiveis, tamanho_grupo)

        for pessoa in grupo:
            nomes_disponiveis.remove(pessoa)
            selecionados.append(pessoa)

        grupos.append(grupo)

    return grupos, selecionados


nomes = [
    "Sid",
    "Higor",
    "Juliana",
    "Cibely",
    "Geovana",
    "Graziela",
    "Pedro",
    "Francinelma",
    "Neilma",
    "Joel",
    "Emily",
]

# len função do python que quantifica o total de elementos em uma string ou array

nomes.append("Alexandre")

# nomes[0] = "Leonardo"

grupos, selecionados = sortear_grupos(nomes, 3)

sorteado = 1
for i, grupo in enumerate(grupos, 1):
    print(f"Sorteando grupo {i}")
    time.sleep(5)
    print(f"Grupo {i} sorteado: {grupo}")

print("\nPessoas já selecionadas:")
print(selecionados)


# https://youtu.be/888vbCs9wLY?si=U8mUGgfLLi-eF-rb

# https://youtu.be/FVFMQjuLXd4?si=gMVrJMzeA_OICk2D

# https://youtu.be/05bjf7Y1mQo?si=hZ2naE4miOg4HPIk