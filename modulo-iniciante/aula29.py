"""
    Introdução ao try/except
    rty -> tenta executar o código
    except -> ocorreu algum erro ao tentar executar
"""

try:
    numero = input('Vou deobrar o número que você digitar: ')
    numero_float = float(numero)
    print(f"O dobro de {numero} é {numero_float * 2:.2f}")
except:
    print(f'O valor "{numero}" não é um número')