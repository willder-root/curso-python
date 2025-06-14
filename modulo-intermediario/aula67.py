"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valroes padrão. Caso o valor não seja 
enviado para o paâmetro, o valor padrão será usado.
"""

def soma(x,y,z=0):
    print(x+y+z)


soma(1,5)