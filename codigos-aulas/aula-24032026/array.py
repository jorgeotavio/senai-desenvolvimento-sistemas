import time

temperatura_ideal = 30
margem = 2

historico = []
contador = 0

while contador < 5:
    temperatura = float(input("Informe a temperatura da piscina: "))
    historico.append(temperatura)

    if temperatura < temperatura_ideal - margem:
        print("Temperatura baixa. Ligar aquecedor.")
    elif temperatura > temperatura_ideal + margem:
        print("Temperatura alta. Desligar aquecedor ou resfriar.")
    else:
        print("Temperatura ideal.")

    contador += 1
    time.sleep(1)

print("Histórico:", historico)

soma = 0
for t in historico:
    soma += t

media = soma / len(historico)
print("Média:", media)