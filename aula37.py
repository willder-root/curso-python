"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1
   

    if contador % 2 != 0:
        continue

    if contador == 40:
        break

    print(contador)

print("Acabou")