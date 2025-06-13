"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis: 
        append - Adiciona um item ao final
        insert -  Adiciona um item no índice escolhido
        pop - remove do final ou do índice escolhido
        del - apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
Cuidados com dados mutáveis
    = - copiando o valor (imutáveis)
    = - aponta para o mesmo valor na memória (mutável)

"""

#            +01234
#           -54321
string = 'ABCDE' # 5 caracteres (len)
lista1 = [123, True, 'Willder Araujo', 1.2]
lista2 = ['novo', False, 1, 45, 8.900, 'Calor']
lista = lista1 + lista2
lista[1] = 'novo'
lista.append(False)
valor = lista.pop(0)
lista3 =  lista2.copy()
valor2 = lista3.pop()
print(f"lista 1: {lista1}")
print(f"lista 2: {lista2}")
print(f"lista 3: {lista3}")
print(valor)
print(valor2)
print(lista, type(lista))