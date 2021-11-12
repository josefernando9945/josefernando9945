import os

"""
Ojetivo:
Mostrar sim se a string tiver duas ou mais consoantes
Se tiver mais de duas substituir por duas consoantes
g = h
r= v 

"""
def possibleChanges(usernames):

    listavogais = ['a', 'e', 'i', 'o', 'u']


    contador = 0


    for letra in list(usernames):
        if letra not in listavogais:
            contador += 1

    if contador >= 2:
        new_string = usernames.replace('g', 'h')
        new_string = new_string.replace('r', 'v')
        print(f"String pode ser alterada: {new_string}")
    else:
        print("não pode ser alterada")

if __name__ == '__main__':
    print("Informe seu username:")


    usernames = input().strip()


    result = possibleChanges(usernames)

