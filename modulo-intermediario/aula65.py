"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def saudacao(nome='Sem nome'):
    print(f"Olá, {nome}")

def imprimirTresValores(a,b,c):
    print(a)
    print(b)
    print(c)

imprimirTresValores('willder','joaquim','maria')

saudacao('Willder')
saudacao('Joaquim')
saudacao()