from funcoes_multiplo import verificar_multiplo


def test_multiplo_de_5():
    """Testa se um número múltiplo de 5 retorna 'fizz'."""
    resultado = verificar_multiplo(10)
    assert resultado == 'fizz'


def test_multiplo_de_7():
    """Testa se um número múltiplo de 7 retorna 'buzz'."""
    resultado = verificar_multiplo(14)
    assert resultado == 'buzz'


def test_multiplo_de_5_e_7():
    """Testa se um número múltiplo de 5 e 7 retorna 'fizzbuzz'."""
    resultado = verificar_multiplo(35)
    assert resultado == 'fizzbuzz'


def test_nao_multiplo_de_5_nem_7():
    """Testa se um número que não é múltiplo de 5 nem de 7 retorna 'miss'."""
    resultado = verificar_multiplo(11)
    assert resultado == 'miss'
