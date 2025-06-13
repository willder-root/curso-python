"""
    CONSTANTE = "Variáveis" que não vão mudar
    Muitas condições no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde está o radar 1
RADAR_RANGE = 1 # Adistância onder o radar pegaa

carro_acima_velcidade = velocidade > RADAR_1
carro_multado = (local_carro >= (LOCAL_1 - RADAR_RANGE)) and \
    (local_carro <= (LOCAL_1 + RADAR_RANGE)) and \
    carro_acima_velcidade

if carro_acima_velcidade:
    print('velocidade carro passou do radar 1')

if  carro_multado:
    print("Carro multado em rada 1")