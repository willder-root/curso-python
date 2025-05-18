frase = 'o python é uma linguagem de programação '\
        'multiparadigma.'\
        'Python foi criado por Guido van Rossum.'

i = 0
maior_quantidade = 0
letra_usada_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    elif frase.count(letra_atual) > maior_quantidade:
        maior_quantidade = frase.count(letra_atual) 
        letra_usada_mais_vezes = letra_atual
    
    print(f"{letra_atual}: {frase.count(letra_atual)}")
    i += 1

print(f'A letra "{letra_usada_mais_vezes}" foi usada mais vezes, '\
      f'com um total de {maior_quantidade} vezes')    