"""
    Faça um jogo par o usuário adivinhar qual a palavra secreta.
    - Você  vai propor uma palavra secreta qualuer e vai dar a 
    possibilidade par o usuário digitar apenas uma letra.
    - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está 
    na palavra secreta.
        - Se a letra digitada estiver na palavra secreta; exiba a letra;
        - Se a letra digitada não estiver na palavra secreta; exiba *.
    Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_secreta = "medico"
palavra_formatada = len(palavra_secreta) * '*'
letra_informada = ''
temp_palavra_formatada = ''
tentativas = 0
while True:
    if palavra_formatada == palavra_secreta:
        print("Parabéns! Você acertou a palavra secreta.")
        print(f"Palavra secreta: {palavra_formatada}")
        print(f"Tentativas: {tentativas}")
        input()
        os.system('cls')
        palavra_formatada = len(palavra_secreta) * '*'
        letra_informada = ''
        temp_palavra_formatada = ''
        tentativas = 0

    
    letra_informada = input("Digite uma letra: ")
    tentativas += 1
    if len(letra_informada) > 1:
        print("Digite apenas uma letra")
        continue
    
    
    
    if (letra_informada) and (letra_informada in palavra_secreta):    
        for i in range(len(palavra_secreta)):
            if letra_informada == palavra_secreta[i]:
                temp_palavra_formatada += f"{letra_informada}"
            else:
                temp_palavra_formatada += palavra_formatada[i]
        palavra_formatada = temp_palavra_formatada
        temp_palavra_formatada = ''
    print(f"Palavra formatada: {palavra_formatada}")