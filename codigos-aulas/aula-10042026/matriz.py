arquivo = open('matriz.txt', '+a')

matriz = [
    [1,2,1,24,5,12,3],
    [1,2,1,24,5,12,2],
    [1,34,10,23,9,13,7],
    [1,2,1,24,5,12,3],
    [1,2,6,24,5,12,6],
]

for line in matriz:
    for idx, item in enumerate(line):
        arquivo.write(str(item)+",")

        if idx == len(line) - 1:
            arquivo.write("\n")
            