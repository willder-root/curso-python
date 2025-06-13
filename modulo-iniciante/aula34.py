"""
Repetições
while(enquanto)
Executa uma ação enquanto uma codição for verdadeira
"""

condicao = True

while condicao:
    nome = input("Qual o seu nome? ")
    print(f"Seu nome é {nome}")
    if nome.lower() == "sair":
        break