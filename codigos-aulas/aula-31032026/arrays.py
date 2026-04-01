# C R U D
temperaturas_dia_1 = [
    28.3,
    31.2
]

# Create: insert, append
temperaturas_dia_1.insert(0, 30)
temperaturas_dia_1.append(40)

# Read: acessar os dados
# print(temperaturas_dia_1)
# print(temperaturas_dia_1[2])

# Update: Atualizar um dado do array
temperaturas_dia_1[2] = 24

# Delete: Remover um dado do array
temperaturas_dia_1.pop()
temperaturas_dia_1.pop(0)
temperaturas_dia_1.remove(28.3)

# print(temperaturas_dia_1)
tupla_temperaturas = (32, 34, 50, 80)

tupla_temperaturas[1]

print(tupla_temperaturas[1])