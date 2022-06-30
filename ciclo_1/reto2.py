def cliente(informacion: dict) -> dict:
    id_cliente = informacion["id_cliente"]
    nombre = informacion["nombre"]
    edad = informacion["edad"]
    primer_ingreso = informacion["primer_ingreso"]
    apto = True
    global descuento

    if edad > 18:
        valor_boleta = 20000
        atraccion = "X-Treme"
    elif edad >= 15 and edad <= 18:
        valor_boleta = 5000
        atraccion = "Carros chocones"
    elif edad >= 7 and edad < 15:
        valor_boleta = 10000
        atraccion = "Sillas voladoras"
    elif edad < 7:
        apto = False
        atraccion = "N/A"
        valor_boleta = "N/A"
    total_boleta = valor_boleta

    if primer_ingreso == True or primer_ingreso == True:
        if edad > 18:
            descuento = 0.05
        elif edad >= 15 and edad <= 18:
            descuento = 0.07
        elif edad >= 7 and edad < 15:
            descuento = 0.05
        if edad > 7:
            total_boleta = valor_boleta - (valor_boleta * descuento)

    nuevoDic = {
        "nombre": nombre,
        "edad": edad,
        "atraccion": atraccion,
        "apto": apto,
        "primer_ingreso": primer_ingreso,
        "total_boleta": total_boleta,
    }
    return nuevoDic
