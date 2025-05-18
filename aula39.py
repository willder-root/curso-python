"""
    Iterando strings com while
"""

nome = "Willder Araujo"
tamanho_nome = len(nome)
indice_inicial = 0
nova_string = ""

while indice_inicial < tamanho_nome:
    nova_string += f"*{nome[indice_inicial]}"
    indice_inicial += 1

print(nova_string)