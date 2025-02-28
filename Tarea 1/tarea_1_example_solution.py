def separa_letras(cadena):
    
    if not isinstance(cadena, str):
        return -100, None, None  # Error por no ser string
    if not cadena.isalpha():
        return -200, None, None  # Error por contener caracteres fuera del abecedario
    if cadena == "":
        return -300, None, None  # Error por cadena vacía

    mayusculas = "".join([c for c in cadena if c.isupper()])
    minusculas = "".join([c for c in cadena if c.islower()])
    
    return 0, mayusculas, minusculas  # Éxito


def potencia_manual(base, potencia):
    
    if isinstance(base, str) or isinstance(potencia, str):
        return -400, None  # Error por recibir un string

    if potencia == 0:
        return 0, 1  # Cualquier número elevado a 0 es 1

    resultado = 1
    for _ in range(abs(potencia)):
        temp = 0
        for _ in range(abs(base)):  # Simulación de multiplicación con sumas
            temp += resultado
        resultado = temp

    if potencia < 0:
        resultado = 1 / resultado  # Invertir si el exponente es negativo

    return 0, resultado  # Éxito
