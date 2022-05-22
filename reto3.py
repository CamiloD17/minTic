def AutoPartes(ventas: list):
    dic = {}
    for (
        IdProducto,
        dProducto,
        pnProducto,
        cvProducto,
        sProducto,
        nComprador,
        cComprador,
        fVenta,
    ) in ventas:
        if dic.get(IdProducto) == None:
            dic[IdProducto] = []
        dic[IdProducto].append(
            (
                dProducto,
                pnProducto,
                cvProducto,
                sProducto,
                nComprador,
                cComprador,
                fVenta,
            )
        )
    return dic


def consultaRegistro(ventas, IdProducto):
    nuevodic = ventas
    if IdProducto in nuevodic.keys():
        for i in range(len(nuevodic[IdProducto])):
            dProducto = nuevodic.get(IdProducto)[i][0]
            pnProducto = nuevodic.get(IdProducto)[i][1]
            cvProducto = nuevodic.get(IdProducto)[i][2]
            sProducto = nuevodic.get(IdProducto)[i][3]
            nComprador = nuevodic.get(IdProducto)[i][4]
            cComprador = nuevodic.get(IdProducto)[i][5]
            fVenta = nuevodic.get(IdProducto)[i][6]

            print(
                f"Producto consultado : {IdProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}"
            )
    else:
        print(f"No hay registro de venta de ese producto")


consultaRegistro(
    AutoPartes(
        [
            (9852, "Culata", "XC9875", 2, 165, "Luis Molero", 3455846, "14/06/2020"),
            (9852, "Culata", "XC9875", 2, 165, "Jose Mejia", 1355846, "14/06/2020"),
            (2564, "Cárter", "PT29872", 2, 32, "Peter Cerezo", 8545436, "14/06/2020"),
            (5412, "válvula", "AZ8798", 2, 11, "Juan Peña", 568975, "14/06/2020"),
        ]
    ),
    9852,
)
