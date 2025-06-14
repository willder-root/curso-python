"""
Exercícios com funções

Crie uma função que mutiplica todos os argumentos
não nomeados recebidos. 
Retorne o total para uma variável e mostre o valor
da variável.

Crie uma função fala se um número é par ou é ímpar.
Retorno se o número é par ou ímpar.
"""


def mutiplicaValores(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def IsPar(numero):
    return numero % 2 == 0

resultado_1 = mutiplicaValores(1,8,7,6,55,90,7)
resultado_2 = mutiplicaValores(1,55,440,7)

resultado_3 = IsPar(2)
resultado_4 = IsPar(5)

print(resultado_1, resultado_2, resultado_3, resultado_4)