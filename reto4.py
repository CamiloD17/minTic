from functools import reduce


def ordenes(rutinaContable):
    print("----------------- Inicio Registro diario --------------------------")
    suma = []
    suma2 = 0
    for i in range(len(rutinaContable)):
        for j in range(len(rutinaContable) + 1):
            for k in range(len(rutinaContable) + 1):
                numero = rutinaContable[i][0]
                codigo = rutinaContable[i][j + 1][k]
                productos = rutinaContable[i][j + 1][k]
                cantidad = rutinaContable[i][j + 1][k]
                sin_string = list(
                    filter(
                        lambda x: isinstance(x, int) == True
                        or isinstance(x, float) == True,
                        rutinaContable[i][j + 1],
                    )
                )

            multiplica = reduce(lambda x, y: x * y, sin_string)
            suma2 += multiplica
        suma.append(suma2)
        # print(suma)

        if i > 0:
            total = suma[i] - suma[i - 1]
        else:
            total = suma[i]
        if total < 600000:
            total += 25000
        print(f"La factura {numero} tiene un total en pesos de {total:.2f}")
    print(
        "-------------------------- Fin Registro diario ----------------------------------"
    )


ordenes(
    [
        [1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
        [1202, ("8756", 3, 115362.58), ("1112", 18, 2354.99)],
        # [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20)],
    ]
)

# rutinaContable = [ [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
#                    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
#                    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
#                    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
# ]
# ordenes(rutinaContable)
