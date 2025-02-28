import tarea_1_example_solution
import random
import string
import pytest

# Codigos de retorno esperados
# Caso de éxito => 0

# Errores esperados metodo de separar letras
# Error en caso de un número entero de entrada => -100
# Error en caso de un caracter fuera del abecedario => -200
# Error en caso de un string vacio => -300

# Errores esparados metodo de potencia
# Error en caso de que se pase un string => -400


# Prueba 1
# Verifica todos los casos de error de la solución
def test_casos_error_separador():
    # Error por número
    estado, res1, res2 = tarea_1_example_solution.separa_letras(7)
    assert estado == -100
    assert res1 is None
    assert res2 is None

    # Error por caracter fuera del abecedario
    random_punctuation = random.choice(string.punctuation)
    estado, res1, res2 = tarea_1_example_solution.separa_letras(random_punctuation)
    assert estado == -200
    assert res1 is None
    assert res2 is None

    # Error por string vacio
    estado, res1, res2 = tarea_1_example_solution.separa_letras("")
    assert estado == -300
    assert res1 is None
    assert res2 is None


# Prueba 2
# Verifica casos de exito de la funcion
def test_casos_exito_separador():
    estado, res1, res2 = tarea_1_example_solution.separa_letras("AWprolQTyMNTTTZFghk")
    assert estado == 0
    assert res1 == "AWQTMNTTTZF"
    assert res2 == "prolyghk"

    estado, res1, res2 = tarea_1_example_solution.separa_letras("P")
    assert estado == 0
    assert res1 == "P"
    assert res2 == ""

    estado, res1, res2 = tarea_1_example_solution.separa_letras("y")
    assert estado == 0
    assert res1 == ""
    assert res2 == "y"


# Prueba 3
# Verifica los casos de error de la funcion de potencia
def test_casos_error_potencia():
    estado, result = tarea_1_example_solution.potencia_manual("Cafe", 10)
    assert estado == -400
    assert result is None

    estado, result = tarea_1_example_solution.potencia_manual(4, "10")
    assert estado == -400
    assert result is None

    estado, result = tarea_1_example_solution.potencia_manual("", 3)
    assert estado == -400
    assert result is None

    estado, result = tarea_1_example_solution.potencia_manual("s", "s")
    assert estado == -400
    assert result is None


# Prueba 4
# Verifica los casos de exito de la funcion de potencia
def test_casos_exito_potencia():
    param1 = random.randint(0, 10)
    param2 = random.randint(0, 10)
    expected_result = param1**param2

    print(param1, "---", param2)
    estado, result = tarea_1_example_solution.potencia_manual(param1, param2)
    assert estado == 0
    assert result == expected_result
