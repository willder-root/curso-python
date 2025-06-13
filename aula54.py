"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os
try:
    lista_compras = []
    while True:
        print("============================================")
        print('Lista de compras!')
        print()
        print('Ações:')
        print(" 1 - Adicionar item")
        print(" 2 - Remover item")
        print(" 3 - Listar itens" )
        print(" 4 - Limpar lista")
        print(" 5 - Sair")
        print()
        print("============================================")
        opcao = input()

        os.system('cls')

        if opcao not in ['1','2','3','4','5']:
            print("Opção inválida!")
            input("Pressione Enter e tente novamente!")
            os.system('cls')
            continue
        
        if opcao == '1':
            item = input("Informe o item para compra: ")
            lista_compras.append(item)
            print(f'o item "{item}" foi adicionado com sucesso a lista de compras')
        elif opcao == '2':
            if len(lista_compras) == 0:
                print("Não há itens para remover")
                input("Pressione Enter e tente novamente!")
            else:
                try:

                    print("Qual item deseja remover?") 
                    print("============================================")
                    for indice, item in enumerate(lista_compras):
                        print(indice, item )
                    print("============================================")
                    print()
                    item_selecionado = input()
                    item_removido = lista_compras.pop(int(item_selecionado))
                    print(f"O item {item_removido} foi removido com sucesso")
                    input("Pressione Enter para voltar ao menu principal")
                except IndexError:
                    print("O item escolhido não existe na lista!")
                    input("Pressione Enter e tente novamente!")        
        elif opcao == '3':
            print("Itens da lista de compras: ")
            print("============================================")
            for item in lista_compras:
                print(item)
            print("============================================")
            print()
            input("Pressione Enter para voltar ao menu principal")        
        elif opcao == '4':
            lista_compras.clear
            print("Lista limpa com sucesso!")        
            input("Pressione Enter para voltar ao menu principal")
        elif opcao == '5':
            break
            
        os.system('cls')
        continue
except KeyboardInterrupt:
    pass
