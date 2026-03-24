temperatura_ideal = 30
margem = 2

temperatura = float(input("Informe a temperatura da piscina: "))

if temperatura < temperatura_ideal - margem:
    print("Temperatura baixa. Ligar aquecedor.")
elif temperatura > temperatura_ideal + margem:
    print("Temperatura alta. Desligar aquecedor ou resfriar.")
else:
    print("Temperatura ideal.")