from funcoes_multiplo import verificar_multiplo

def main():
    numero = int(input('Digite um número natural: '))
    resultado = verificar_multiplo(numero)
    print(resultado)

if __name__ == '__main__':
    main()
