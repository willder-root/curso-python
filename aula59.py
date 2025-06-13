# Desempacontamento em chamadas
# de métodos e funções


string = 'ABCD'
lista = ['Willder', 'Joaquim', 'Maria', 'Eduarda']
tupla = 'Python', 'é', 'legal!'

a, b, c, *_ = lista
print(a, c)
lista_nova = lista.copy()
lista_nova.append(1)
lista_nova.append(2)
lista_nova.append(3)
*__, d = lista_nova
print(d)
for item in tupla:
    print(item,end= " ")

print(*tupla)