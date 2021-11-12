# criar dois imput para numero
# se não for numero informar mensagen
# se for numero imprimir a soma

import os

print('*****Trabalhe com as quatro operações matematicas*****')


def multiplicao(n1, n2):
    return int(n1) * int(n2)


def divisao(n1, n2):
    return int(n1) / int(n2)


def adicao(n1, n2):
    return int(n1) + int(n2)


def subtracao(n1, n2):
    return int(n1) - int(n2)


def calculo(numero1, numero2):

    if numero1.isdigit() and numero2.isdigit():

        if menu == 1:
            resultado = multiplicao(numero1, numero2)

        elif menu == 2:
            resultado = divisao(numero1, numero2)

        elif menu == 3:
            resultado = adicao(numero1, numero2)

        elif menu == 4:
            resultado = subtracao(numero1, numero2)

        print("#################################")
        print('O resultado é:')
        print(resultado)
        print("#################################")

    else:
        print('Você deve digitar somente numeros')





if __name__ == '__main__':
    print('informe o primeiro numero:')


    numero1 = input().strip()
    os.system('clear')

    print("###########################################")
    print('Selecione a opção desejada')
    print("----------------------------")
    print('1 - Multiplicação')
    print('2 - Divisão')
    print('3 - Adição')
    print('4 - Subitração')
    print("###########################################")

    menu = int(input().strip())
    os.system('clear')

    print('informe o segundo numero:')

    numero2 = input().strip()
    os.system('clear')


    result = calculo(numero1, numero2)