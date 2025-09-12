from calculadora import *
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
