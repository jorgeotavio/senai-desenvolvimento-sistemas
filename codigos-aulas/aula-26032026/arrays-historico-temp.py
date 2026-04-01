temperaturas = [28.5, 30.2, 29.8, 31.0, 27.9]

print("Temperaturas coletadas:")
for t in temperaturas:
    print(t)

soma = 0
for t in temperaturas:
    soma += t

media = soma / len(temperaturas)
print("Média:", media)

maior = max(temperaturas)
menor = min(temperaturas)

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)

for t in temperaturas:
    if t > 30:
        print("Ativar resfriamento")
        break

for t in temperaturas:
    if t < 28:
        print("Ativar aquecimento")
        break
