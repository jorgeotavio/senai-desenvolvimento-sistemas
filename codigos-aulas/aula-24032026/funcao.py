import time

temperatura_ideal = 30
margem = 2

def ler_temperatura():
    return float(input("Informe a temperatura da piscina: "))

def verificar_temperatura(temperatura):
    if temperatura < temperatura_ideal - margem:
        return "baixa"
    elif temperatura > temperatura_ideal + margem:
        return "alta"
    else:
        return "ideal"

def agir(status):
    if status == "baixa":
        print("Ligar aquecedor.")
    elif status == "alta":
        print("Desligar aquecedor ou resfriar.")
    else:
        print("Temperatura ideal.")

def calcular_media(lista):
    soma = 0
    for t in lista:
        soma += t
    return soma / len(lista)

historico = []
contador = 0

while contador < 5:
    temperatura = ler_temperatura()
    historico.append(temperatura)

    status = verificar_temperatura(temperatura)
    agir(status)

    contador += 1
    time.sleep(1)

print("Histórico:", historico)
print("Média:", calcular_media(historico))