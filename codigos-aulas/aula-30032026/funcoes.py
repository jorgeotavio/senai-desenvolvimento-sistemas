def get_temperatura(t, y, x):
    print(t, y, x)
    match t:
        case t if t > 30:
            return "Quente"
        case t if t < 30:
            return "Frio"
        case _:
            return "Temperatura ideal"

temperatura = get_temperatura(10, 56, 70)

print(temperatura)

def get_temperatura(t):
    return t > 30

temperatura = get_temperatura(31)

if temperatura == True:
    print("Quente")
else:
    print("Frio")

        