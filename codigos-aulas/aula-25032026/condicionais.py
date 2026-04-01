# Implementem o histórico de temperaturas que foram obtidas durante 3 execuções

import random

def  get_temperatura_da_piscina():
    return random.sample([10, 20, 40, 8, 60], 1)[0]

historico = []

while len(historico) < 3:
    temperatura_da_piscina = get_temperatura_da_piscina()
    
    historico.append(temperatura_da_piscina)

    temperatura_ideal = 30
    margem_de_erro = 2

    esta_fria = temperatura_da_piscina < (temperatura_ideal - margem_de_erro)
    esta_quente = temperatura_da_piscina > (temperatura_ideal + margem_de_erro)

    temperatura_esta_ideal = not esta_fria and not esta_quente

    if temperatura_esta_ideal:
        print('Nao faz nada')
    elif esta_fria:
        print('Esquento')
    else:
        print('Esfria')

print(historico)

for t in historico:
    print(t)