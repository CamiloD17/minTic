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
    i = 0
    if IdProducto in nuevodic.keys():
        while i in range(len(nuevodic[IdProducto])):
            dProducto = nuevodic.get(IdProducto)[i][0]
            pnProducto = nuevodic.get(IdProducto)[i][1]
            cvProducto = nuevodic.get(IdProducto)[i][2]
            sProducto = nuevodic.get(IdProducto)[i][3]
            nComprador = nuevodic.get(IdProducto)[i][4]
            cComprador = nuevodic.get(IdProducto)[i][5]
            fVenta = nuevodic.get(IdProducto)[i][6]
            i += 1
            print(
                f"Producto consultado : {IdProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}"
            )
    else:
        print(f"No hay registro de venta de ese producto")