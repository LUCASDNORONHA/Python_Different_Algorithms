# Algoritmo simples para detecção de infração por um radar de transito

# Autor: Lucas Dias Noronha

'''
A função deste algoritmo é dectar se um carro passou acima da velocidade permitida numa
rodovia com limite de velocidade de 60km.

'''

# Declaração da variável que armazenará a velocidade do carro.
velocidade_carro = 64

# Declaração da variavel que armazenará  a localização do carro na rodovia.
local_carro = 100

# Declaração da variável que armazenará a velocidade permitida da rodovia.
radar_velocidade_permitida = 60

# Declaração da variável que armazenará a posição do radar na rodovia.
local_radar = 100

# Declaração da variável que armazenará o alcancer do radar na rodovia.
radar_alcance = 1

# Declaração da variável que armazenará se é verdadeiro ou falso que a velocidade do carro ultrapassou a velocidade permitida.
velocidade_ultrapassada = (velocidade_carro > radar_velocidade_permitida)

# Declaração da variável que armazenará se verdadeiro ou falso que a localização do carro está na localização do radar e no alcance do radar.
carro_area_do_radar = (((local_carro == local_radar+radar_alcance)and(local_carro == local_radar-radar_alcance)) or local_carro == local_radar)

# Declaração de variável que armazenará se é verdadeiro ou falso que o carro infligiu o limite de velocidade.
infracao_detectada = (velocidade_ultrapassada and carro_area_do_radar)

# Declaração da variável que armazenará a notificação de multa aplicada.
multar_carro = ('Você foi multado por estar acima da velocidade permitida na rodovia.')

# Declaração da variável que armazenará a notifição de nenhuma regra infligida.
nao_multar_carro = "Você está dentro da velocidade permitida na rodovia."


# Com a estrutura de decisão o algoritmo irá conferir se é verdadeiro ou falso
# a infração. Se houver infração ele exibirá o comando para exibir a
# notificação de multa aplica, caso o contrario ele exibirá a notificação de 
# nenhuma regra infliginda.
if infracao_detectada:
    print(multar_carro)

else:
    print(nao_multar_carro)


