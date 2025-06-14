"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg):
    return msg

def executa(funcao, msg):
    return funcao(msg)

v = saudacao('Bom dia')
print(v)

saudacao_2 = saudacao



print(saudacao_2('Olá'))

execucao = executa(saudacao,'Tudo certo?')
print(execucao)