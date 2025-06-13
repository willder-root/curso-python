"""
Exercício 
Exiba os índices da lista
"""

lista =  ['Willder', 'Joaquim', 'Maria']

indices = range(len(lista))

for indice in indices:
    print(f"Índice: {indice}, Item: {lista[indice]}, Tipo: {type(lista[indice])}" )