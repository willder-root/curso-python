"""
    Calculadora com while
"""

sair = True
continuar = ''
valor_1 = None
valor_2 = None
resultado = None
while sair:
    valor_1 = None
    valor_2 = None
    resultado = None
    operacao = input("""
                Qual operação deseja realizar?
                
                Adição: +
                Subtração: -
                Mutiplicação *
                Divisão: /
                    """)

    if operacao in ['+', '-','*','/']:
        if operacao == '+':
            valor_1 = input("Informe um número: ")
            valor_2 = input("Informe um número: ")

            if valor_1.isnumeric() and valor_2.isnumeric:
                resultado = float(valor_1) + float(valor_2)
                print(f"Resultado: {resultado:.2f}")
            else:
                print("Valores não são números")
        elif operacao == '-':
            valor_1 = input("Informe um número: ")
            valor_2 = input("Informe um número: ")

            if valor_1.isnumeric() and valor_2.isnumeric:
                resultado = float(valor_1) - float(valor_2)
                print(f"Resultado: {resultado:.2f}")
            else:
                print("Valores não são números")
        elif operacao == '*':
            valor_1 = input("Informe um número: ")
            valor_2 = input("Informe um número: ")

            if valor_1.isnumeric() and valor_2.isnumeric:
                resultado = float(valor_1) * float(valor_2)
                print(f"Resultado: {resultado:.2f}")
            else:
                print("Valores não são números")
        else:
            valor_1 = input("Informe um número: ")
            valor_2 = input("Informe um número: ")

            if valor_1.isnumeric() and valor_2.isnumeric:
                if float(valor_2) and float(valor_1):
                    resultado = float(valor_1) / float(valor_2)
                    print(f"Resultado: {resultado:.2f}")
                else:
                    print("Erro: divisão por zero")
            else:
                print("Valores não são números")
    else:
        print("Operação selecionada é inválida")

    continuar = input("""
                        Deseja sair? 
                        [S]im ou [N]ao 
                    """)
    
    sair = continuar.lower().startswith('n')


