"""
aplit e join com list e string
split - divide uma string
join - une uma string
"""

frase = '    olha só que, coisa interessante '
lista_palavras = frase.split(',')
print(lista_palavras)
for indice, frase in enumerate(lista_palavras):
    lista_palavras[indice] = lista_palavras[indice].strip()


print(lista_palavras)