# operadores lógicos
# and (e), or (ou), not (não)
# or - Qualquer condição verdadeira avalia toda expressão como verdadeira.
# Se qualquer valor for considerado verdadiro, a expressão inteira será avaliada naquele valor.
# São considerados falso:
# 0, 0.0, '', False
# Também existe o operador None que é usado para representar um não valor.

# Exemplo 1
# entrada =  input("[E]ntrar [S]air: ")
# senha_digitada = input("Senha: ")
# senha_permitida = '123456'

# if ((entrada == 'e') or (entrada == 'E')) and senha_digitada == senha_permitida:
#     print('Entrou')
# else:
#     print("Saiu")

# Exemplo 2
senha = input('Senha: ') or 'sem senha'
print(senha)