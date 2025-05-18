"""
    Iterável -> str, range, etc
    Iterador -> quem sabe entregar um valor por vez
    netx -> me entregue o próximo valor
    iter -> me entrgue seu iterador
"""

# numeros = range(0,100,8)

# for numero in numeros:
#     print(numero)

texto = "Willder Araujo"
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break