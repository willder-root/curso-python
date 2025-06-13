"""
enumerate - enumera iteráveis(índices)
"""

lista = ['Willder', 'Joaquim', 'Maria']
lista_enumerada = enumerate(lista)

for indice,item in enumerate(lista):
    print(indice,item)