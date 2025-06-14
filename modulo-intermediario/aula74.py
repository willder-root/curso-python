"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudaco, nome):
    def saudar():
        return f"{saudaco} {nome}!"
    return saudar

s1 = criar_saudacao('Bom dia', 'Willder')
print(s1())
print(s1())