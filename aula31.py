"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is nor é ou não é (tipo, valor, identidade)
id = identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça algo")
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

v1 = 'A'
v2 = 'A'
print(id(v1))
print(id(v2))