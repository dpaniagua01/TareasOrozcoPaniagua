def separa_letras(cadena):
    """
    Separa una cadena en letras mayúsculas y minúsculas.

    Parámetros:
        cadena (str): Cadena de entrada que debe contener solo
        letras del abecedario.

    Retorna:
        tuple: (Código de estado, string con mayúsculas,
        string con minúsculas)
            - (-100, None, None) si la entrada no es un string.
            - (-300, None, None) si la entrada es una cadena vacía.
            - (-200, None, None) si la entrada contiene caracteres
            fuera del abecedario.
            - (0, mayúsculas, minúsculas) si la separación es exitosa.
    """
    if not isinstance(cadena, str):
        return -100, None, None  # Error por no ser string
    if cadena == "":
        return -300, None, None  # Error por cadena vacía
    if not cadena.isalpha():
        return -200, None, None  # Error por contener caracteres
        # fuera del abecedario

    # Separar caracteres en dos grupos: mayúsculas y minúsculas
    mayusculas = "".join(
        [c for c in cadena if c.isupper()]
    )
    minusculas = "".join(
        [c for c in cadena if c.islower()]
    )

    return 0, mayusculas, minusculas  # Éxito


def potencia_manual(base, potencia):
    """
    Calcula la potencia de un número sin usar el operador de
    multiplicación ni potencias.

    Parámetros:
        base (int): Base de la potencia.
        potencia (int): Exponente de la potencia.

    Retorna:
        tuple: (Código de estado, resultado de la operación)
            - (-400, None) si algún parámetro es un string.
            - (0, resultado) con el cálculo exitoso.
    """
    if isinstance(base, str) or isinstance(potencia, str):
        return -400, None  # Error por recibir un string

    if potencia == 0:
        return 0, 1  # Cualquier número elevado a 0 es 1

    resultado = 1
    for _ in range(abs(potencia)):
        temp = 0
        for _ in range(abs(base)):
            temp += resultado  # Simulación de multiplicación con sumas
        resultado = temp

    if potencia < 0:
        resultado = 1 / resultado  # Invertir si el exponente es negativo

    return 0, resultado  # Éxito
