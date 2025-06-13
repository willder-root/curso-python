# operadores lógicos
# and (e), or (ou), not (não)
# and - TOdas as condições precisam ser verdadeiras.
# Se qualquer valor for considereado falso, a expressão inteira será avaliada naquele valor
# São considerados falso
# 0, 0.0, '', false
# Também existe o tipo None que é usado para representar um não valor


# Exemplo 1
# valor_1 = 'a'
# valor_2 = 't'
# valor_3 = 1
# valor_4 = 4

# if (valor_1 != valor_2) and (valor_3 < valor_4):
#     print("Condição verdadeira")
# else:
#     print('Condição não atendida')


# Exemplo 2
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E') and senha_digitada == senha_permitida:
    print("Entrou")
else:
    print("Saiu")