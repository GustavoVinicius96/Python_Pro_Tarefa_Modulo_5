from funcoes_multiplo import verificar_multiplo

def test_multiplo_de_5():
    resultado = verificar_multiplo(10)
    assert resultado == 'fizz'

def test_multiplo_de_7():
    resultado = verificar_multiplo(14)
    assert resultado == 'buzz'

def test_multiplo_de_5_e_7():
    resultado = verificar_multiplo(35)
    assert resultado == 'fizzbuzz'

def test_nao_multiplo_de_5_nem_7():
    resultado = verificar_multiplo(11)
    assert resultado == 'miss'
