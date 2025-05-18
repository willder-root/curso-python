"""
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se esté número é par ou ímpar. Caso o usuário não digite um número
    inteiro, informe que não é um número inteiro.
"""

# numero = input('Informe um número: ')
# if str.isdigit(numero):
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f"O número {numero} é par")
#     else:
#         print(f"O número {numero} é ímpar")
# else:
#     print(f'O valor "{numero}" não é um número inteiro')

""""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
    descrito, exiba a saudação apropriada. Ex.:
    Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""

# hora_atual = input("Hora: ")
# if str.isdigit(hora_atual):
#     hora_atual_int = int(hora_atual)
#     if (hora_atual_int == 0) or (hora_atual_int == 24) or (hora_atual_int < 12):
#         print('bom dia')
#     elif (hora_atual_int == 12) or (hora_atual_int < 18):
#         print("Boa tarde")
#     elif (hora_atual_int == 18) or (hora_atual_int < 24):
#         print('Boa noite')    
#     else:
#         print("Hora inválida")
# else:
#     print("Hora inválida")

"""
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
    menos  escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, ecreva
    "seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

primeiro_nome = input('Informe o seu primeiro nome: ')
if primeiro_nome:
    if len(primeiro_nome) <= 4:
        print("Seu nome é curto")
    elif len(primeiro_nome) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("É necessário informar o nome")