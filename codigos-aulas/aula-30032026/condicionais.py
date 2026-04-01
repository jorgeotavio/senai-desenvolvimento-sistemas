temperatura = 20

match temperatura:
    case temperatura if temperatura > 30:
        print("Quente")
    case temperatura if temperatura < 30:
        print("Frio")
    case temperatura if temperatura < 30:
        print("Frio")
    case temperatura if temperatura < 30:
        print("Frio")
    case _:
        print("Temperatura ideal")

