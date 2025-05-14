# usando f-string

nome = 'Willder Araujo'
altura = 1.80 
peso = 85
imc = peso / (altura * altura)
linha_1 = f'{nome}  tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'

print(linha_1)
print(linha_2)
print(f"{imc:.2f}")