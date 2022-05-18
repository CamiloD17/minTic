def CDT(usuario: str, capital: int, tiempo: int):
    if tiempo > 2:
        porcentajeIntereses = 0.03
        valorIntereses = (capital * porcentajeIntereses * tiempo) / 12
        valorTotal = valorIntereses + capital
    else:
        porcentajePerder = 0.02
        valorPerder = capital * porcentajePerder
        valorTotal = capital - valorPerder

    mensaje = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}"

    return mensaje
