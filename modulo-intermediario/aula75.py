"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parametro
"""
def mutiplicarValor(mutiplicador):
    def callback(numero):
        return numero  * mutiplicador
    return callback

duplicar = mutiplicarValor(2)

triplicar = mutiplicarValor(3)

quadruplicar = mutiplicarValor(3)



