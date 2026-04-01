historico_temperaturas = [
    [28.5, 30.2, 29.8, 31.0, 27.9],
    [27.0, 28.5, 29.0, 30.1, 28.0],
    [29.5, 31.2, 30.8, 32.0, 29.9]
]

medias = []
alertas = []

for i in range(len(historico_temperaturas)):
    leituras = historico_temperaturas[i]
    
    soma = 0
    for t in leituras:
        soma += t
    
    media = soma / len(leituras)
    medias.append(media)
    
    acima = False
    abaixo = False
    
    for t in leituras:
        if t > 30:
            acima = True
        if t < 28:
            abaixo = True
    
    if acima:
        alertas.append("Resfriamento no dia " + str(i))
    if abaixo:
        alertas.append("Aquecimento no dia " + str(i))

print("Médias por dia:")
for i in range(len(medias)):
    print("Dia", i, ":", medias[i])

print("Alertas:")
for alerta in alertas:
    print(alerta)

maior_media = max(medias)
indice_critico = medias.index(maior_media)

print("Dia mais crítico:", indice_critico)