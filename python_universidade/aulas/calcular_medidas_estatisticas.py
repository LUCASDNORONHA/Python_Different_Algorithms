# Calculando Médidas Estatísticas

# Definindo uma amostra de idades
amostra_idade = (21, 32, 18, 27, 34, 64, 45, 49, 34, 86, 22, 23)

# Calculando a média das idades
media = sum(amostra_idade) / len(amostra_idade)
print("Média das idades:", media)

# Encontrando o maior e o menor valor na amostra
maior_valor = max(amostra_idade)
menor_valor = min(amostra_idade)

# Calculando a amplitude (diferença entre o maior e o menor valor)
amplitude = maior_valor - menor_valor
print("Amplitude:", amplitude)

# Inicializando a variável para a soma dos quadrados das diferenças
soma_quadrado_da_diferença = 0

# Calculando a variância da amostra
for valor in amostra_idade:
    diferenca = valor - media
    soma_quadrado_da_diferença += diferenca ** 2

variancia_amostra = soma_quadrado_da_diferença / (len(amostra_idade) - 1)  # Usando n-1 para amostra
print("Variância da amostra:", variancia_amostra)

# Calculando o desvio padrão da amostra
desvio_padrao_amostra = variancia_amostra ** 0.5
print("Desvio padrão da amostra:", desvio_padrao_amostra)
