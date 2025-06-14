"""
args - argumentos não nomeados
*- *argas (empacotamento e desepacotamento)
"""

x, y, *resto = 1,2,3,4
print(x,y,resto)

def soma(x,y):
    return x + y

print(1)

def somar(*args):
    valor = 0
    for arg in args:
        valor += arg
    return valor

resultado = somar(1,2,3,4,5,6,7,8,9,0)
print(resultado)
