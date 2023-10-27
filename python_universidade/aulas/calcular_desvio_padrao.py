# 1. CALCULANDO A MÉDIA

# Tomamos como exemplo de amostra uma distribuição com a idade de diversos individuos amarzenado na seguinte lista.
amostra_idades = [
    36, 25, 38, 46, 55, 68, 72, 55, 36, 38, 67, 40, 22, 48, 91, 46, 52, 61, 58, 55
    ]
# Calculo da média da amostra
media = sum(amostra_idades) / len(amostra_idades)
# Retornando a média
print (f'Média = {media}')

# 2. CALCULANDO AMPLITUDE

# Descobrindo o maior valor
maior_valor = max(amostra_idades)
# Descobrindo o menor valor
menor_valor = min(amostra_idades)

# Calculo da amplitude
A = maior_valor - menor_valor
# Retornando a amplintude
print(f'Amplitude = {A}')


# 3. CALCULANDO A VARIÂNCIA DA AMOSTRA

# Inicializndo uma variável para armazenar a soma dos quadrados das diferenças
soma_quadrados_diferencas = 0

# Calcule a soma dos quadrados das diferenças
for valor in amostra_idades:
    diferenca = valor - media
    soma_quadrados_diferencas += diferenca ** 2

# Calculo da variância da amostra
variancia_amostra = soma_quadrados_diferencas / (len(amostra_idades) - 1)
# Retorndo a variãncia
print(f"Variância da amostra = {variancia_amostra}")

# 4. CALCULANDO O DEVIO PADRÃO

# Calcule o desvio padrão da amostra manualmente
desvio_padrao_amostra = variancia_amostra ** 0.5
# Retornando o desvio padrão
print(f"Desvio padrão da amostra = {desvio_padrao_amostra}")