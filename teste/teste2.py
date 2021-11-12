# criar dois imput para numero
# se não for numero informar mensagen
# se for numero imprimir a soma

import os

print('*****Trabalhe com as quatro operações matematicas*****')


def SomaDeNumeros(numero1,numero2):


    if numero1.isdigit() and numero2.isdigit():
        resultado1 = (int(numero1) * int(numero2))
        resultado2 = (int(numero1) / int(numero2))
        resultado3 = (int(numero1) + int(numero2))
        resultado4 = (int(numero1) - int(numero2))

        if menu == 1:
            print('O resultado da multiplicação é:')
            print(resultado1)
        elif menu == 2:
            print('O resultado da divisão é:')
            print(resultado2)
        elif menu == 3:
            print('O resultado da adição é:')
            print(resultado3)
        elif menu == 4:
            print('O resultado da subtração é:')
            print(resultado4)

    else:
        print('Você deve digitar somente numeros')


if __name__ == '__main__':
    print('informe o primeiro numero:')


    numero1 = input().strip()
    os.system('clear')

    print('Qual oreração voce quer realisar?')
    print('Multiplicação digite: 1')
    print('Divisão digite: 2')
    print('Adição digite: 3')
    print('Subitração digite: 4')

    menu = int(input().strip())
    os.system('clear')

    print('informe o segundo numero:')

    numero2 = input().strip()
    os.system('clear')

    result = SomaDeNumeros(numero1,numero2)
