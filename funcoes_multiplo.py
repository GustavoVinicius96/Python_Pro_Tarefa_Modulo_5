"""
Módulo para verificação de múltiplos de 5 e 7.
"""
def verificar_multiplo(numero):
    """
    Verifica se um número é múltiplo de 5 e/ou 7.
    Retorna:
        - 'fizz' se o número for múltiplo de 5.
        - 'buzz' se o número for múltiplo de 7.
        - 'fizzbuzz' se o número for múltiplo de 5 e de 7.
        - 'miss' se o número não for múltiplo de 5 nem de 7.
    """
    if numero % 5 == 0 and numero % 7 == 0:
        return 'fizzbuzz'
    elif numero % 5 == 0:
        return 'fizz'
    elif numero % 7 == 0:
        return 'buzz'
    else:
        return 'miss'
