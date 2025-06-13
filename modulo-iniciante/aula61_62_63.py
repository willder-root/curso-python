"""
CPF: 710.460.024-81
Colete a soma dos 9 primeiros dígitos do CPF
mutiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex. 710.460.024-81 (71046002481)
10  9  8  7  6  5  4  3  2
7   1  0  4  6  0  0  2  4
70  9  0  28 36 0  0  6  8

Somar todos os resultados:
70 + 9 + 0 + 28 + 36 + 0 + 0 + 6 + 8 = 157
mutiplicar o resultado por 10
157 * 10 = 1570
obter o reto da divisão da conta anterior por 11
1570 % 11 = 8
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    o resultado é o valor da conta

"""

#print('Informe o número do cpf (Apenas Números)')
# input()
cpf = '710.460.024-80'\
    .replace('.','') \
    .replace(' ','') \
    .replace('-','')

iguais = True
if (cpf[0] == cpf[1]) and \
    (cpf[0] == cpf[2]) and \
    (cpf[0] == cpf[3]) and \
    (cpf[0] == cpf[4]) and \
    (cpf[0] == cpf[5]) and \
    (cpf[0] == cpf[6]) and \
    (cpf[0] == cpf[7]) and \
    (cpf[0] == cpf[8]) and \
    (cpf[0] == cpf[9]) and \
    (cpf[0] == cpf[10]):
    print("O CPF não pode ter todos os digitos iguais!")

digito_1 = cpf[9]
digito_2 = cpf[10]
cpf_1 = cpf[:9]
print(cpf_1)

if len(cpf) != 11:
    print("O CPF deve ter 11 dígitos!")

if not cpf.isdigit:
    print("CPF inválido!")

count = 10
resultado_1 = 0
for digito in cpf_1:
    resultado_1 = resultado_1 + (int(digito) * count)
    count -= 1

resultado_1 = (resultado_1 * 10) % 11

if resultado_1 > 9:
    resultado_1 = 0

if f"{resultado_1}" == digito_1:
    cpf_2 = f"{cpf_1}{resultado_1}"
    count2 = 11
    resultado_2 = 0
    for digito in cpf_2:
        resultado_2 = resultado_2 + (int(digito) * count2)
        count2 -= 1

    resultado_2 = (resultado_2 * 10) % 11

    if resultado_2 > 9:
        resultado_2 = 0
    
    if f"{resultado_2}" == digito_2:
        print(f"O CPF {cpf} é válido")
    else:
        print(f'O CPF {cpf} inválido')
else:
    print(f'O CPF {cpf} inválido')