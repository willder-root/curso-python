"""
    Formatação básica de strings
    s - string 
    d - int
    f - float
    .<Número de dígitos>
    x ou X - hexadecimal
    (Caractere)(><^)(Quantidade)
    > - Esquerda
    < - Direita
    ^ - Centro
    Sinal -, + ou -
    Ex.: 0>-100,.1f
    Flags de conversão - !r, !s, !a
"""

variavel = 'ABC'
print(f'{variavel:2>10}')
print(f'{variavel:1<10}')
print(f'{variavel:4^10}')
print(f'{1234.9879869869786:0=+10,.2f}')
