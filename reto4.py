from functools import reduce


def ordenes(rutinaContable):
    print(
        "------------------------ Inicio Registro diario ---------------------------------"
    )
    suma = []
    sumaEnVector = 0
    for i in range(len(rutinaContable)):
        for j in range(len(rutinaContable[i]) - 1):
            numero = int(rutinaContable[i][0])
            sin_string = list(
                filter(
                    lambda x: isinstance(x, int) == True
                    or isinstance(x, float) == True,
                    rutinaContable[i][j + 1],
                )
            )

            multiplica = reduce(lambda x, y: x * y, sin_string)
            sumaEnVector += multiplica
        suma.append(sumaEnVector)

        if i > 0:
            cantidad = suma[i] - suma[i - 1]
        else:
            cantidad = suma[i]
        if cantidad < 600000:
            cantidad += 25000
        print(f"La factura {numero} tiene un total en pesos de {cantidad:,.2f}")

    print(
        "-------------------------- Fin Registro diario ----------------------------------"
    )


ordenes(
    [
        [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
        [6590, ("5236", 8, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)],
        [6591, ("7812", 2, 11.99), ("9652", 11, 18.99)],
    ]
)
