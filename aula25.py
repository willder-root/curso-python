"""
    Interpolação básica de strings
    s - string
    d e i - int
    f - float
    x e X - Hexadecimal (0123456789ABCDEF)
"""

nome = 'Willder'
salario = 3000.1234850
mensagem = ' %s tem o salario de R$%.2f' % (nome, salario)
print(mensagem)
