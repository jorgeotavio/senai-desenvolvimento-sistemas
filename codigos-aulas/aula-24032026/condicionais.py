def  get_temperatura_da_piscina():
    return 45

temperatura_da_piscina = get_temperatura_da_piscina()

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

