"""
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1

print("------------------------------")
while linha <= qtd_linhas:
    coluna = 1
    # print(f"Linha: {linha}")
    while coluna <= qtd_colunas:
        print(f"Linha: {linha} | Coluna: {coluna}")
        coluna += 1
    print("------------------------------")
    linha += 1

print("Acabou")