import pytest
from calculadora import soma, subtracao, multiplicacao, divisao

def teste_soma():
    assert soma(2, 3) == 5

def teste_subtracao():
    assert subtracao(10, 6) == 4

def teste_multiplicacao():
    assert multiplicacao(6, 5) == 30

def teste_divisao():
    with pytest.raises(ValueError):
        divisao(100, 0)

