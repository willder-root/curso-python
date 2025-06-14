"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado rece apenas o argumento (valor)
"""

def somar(x,y):
    print(f"{x=}  {y=}",'|','x + y = ', x + y)

somar(1,2)
somar(y=2,x=1)