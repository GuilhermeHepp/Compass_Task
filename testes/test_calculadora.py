from calculadorafun.calculadora import *
import pytest

def test_soma_valido():
    calc = Calculadora(10, 5)
    assert calc.somar() == 15

def test_subtrair_valido():
    calc = Calculadora(10, 5)
    assert calc.subtrair() == 5

def test_multiplicar_valido():
    calc = Calculadora(10, 5)
    assert calc.multiplicar() == 50

def test_dividir_valido():
    calc = Calculadora(10, 5)
    assert calc.dividir() == 2

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        calc = Calculadora(10, 0)
        calc.dividir()

def test_potencia_valido():
    calc = Calculadora(2, 3)
    assert calc.potencia() == 8

def test_raiz_quadrada_valido():
    calc = Calculadora(16, 25)
    assert calc.raiz_quadrada() == (4.0, 5.0)

def test_raiz_quadrada_negativo():
    with pytest.raises(ValueError):
        calc = Calculadora(-16, 25)
        calc.raiz_quadrada()
    with pytest.raises(ValueError):
        calc = Calculadora(16, -25)
        calc.raiz_quadrada()
    with pytest.raises(ValueError):
        calc = Calculadora(-16, -25)
        calc.raiz_quadrada()
