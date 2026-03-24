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
    "Ana", "Bruno", "Carlos", "Daniela",
    "Eduardo", "Fernanda", "Gabriel",
    "Helena", "Igor", "Juliana"
]

grupos, selecionados = sortear_grupos(nomes, 3)

sorteado = 1
for i, grupo in enumerate(grupos, 1):
    print(f"Sorteando grupo {sorteado}")
    time.sleep(5)
    print(f"Grupo {i} sorteado: {grupo}")

print("\nPessoas já selecionadas:")
print(selecionados)