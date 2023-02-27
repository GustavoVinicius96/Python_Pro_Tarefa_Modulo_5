from funcoes_multiplo import verificar_multiplo

def main():
    """
    Solicita ao usuário que digite um número natural e
    exibe na tela o resultado da verificação de múltiplos.
    """
    numero = int(input('Digite um número natural: '))
    resultado = verificar_multiplo(numero)
    print(resultado)

if __name__ == '__main__':
    main()
