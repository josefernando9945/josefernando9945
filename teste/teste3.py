"""
criar lista de afazeres
criar input de entrada de afazeres
criar input de alteração de afazeres
criar input de esclusão de afazeres

"""

def ListaDeTarefas():
    lista = ['correr', 'nadar', 'saltar',  'pular', 'comprar']
    menu = 0
    while not menu == 4:
        print('*****Lista de Tarefas*****')

        print('1 - Inserir')
        print('2 - Alterar')
        print('3 - Excluir')
        print('4 - sair')
        print('Escolha a opção')

        menu = int(input().strip())




        if menu == 1:
            print('Insira a tarefa')
            entratarefa = input().strip()
            lista.append(entratarefa)
            print(lista)


        elif menu == 2:
            print('Altere a tarefa')
            for tar in lista:
                print(lista.index(tar), tar)
            print('Digite o numero da sua alteração:')
            alteratarefa = int(input().strip())
            print(lista[alteratarefa])
            modeificatarefa = (input().strip())
            lista[alteratarefa] = modeificatarefa
            print(lista)

        elif menu == 3:
            print('Excluir a tarefa')
            for tar in lista:
                print(lista.index(tar), tar)
            print('Digite o numero a excluir:')
            excluirtarefa = int(input().strip())
            print(lista[excluirtarefa])
            del(lista[excluirtarefa])
            print(lista)

        elif menu == 4:
            print('Você saiu da lista')






if __name__ == '__main__':

    ListaDeTarefas()
