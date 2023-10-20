# MÉTODO MAP

# Exemplo 1:

# Definindor uma função chamada 'dobrar'.
def dobrar(numero):
    return numero * 2

# Criando uma lista.
numeros = [1, 2, 3, 4, 5]

# Usando o método map para a função 'dobrar' iterar e aplicar sobre cada elemento do
# interador 'numeros'.
resultado = map(dobrar, numeros)

# Converte o objeto de mapa em uma lista.
lista_resultado = list(resultado)

# Imprime o resultado.
print(lista_resultado)
# Saída:
# [2, 4, 6, 8, 10]

# Exemplo 2:

# Função para calcular a média de três números
def calcular_media(a, b, c):
    return (a + b + c) / 3

# Listas de números
lista1 = [10, 20, 30]
lista2 = [15, 25, 35]
lista3 = [5, 15, 25]

# Usando o map para calcular a média de cada conjunto de números
medias = map(calcular_media, lista1, lista2, lista3)

# Converte o objeto de map em uma lista de médias
lista_de_medias = list(medias)

print(lista_de_medias)
# Saída:
# [10.0, 20.0, 30.0]



# Info
"""
    O método map é uma função integrada (built-in) em Python que é usada para aplicar 
    uma função a cada elemento de um ou mais iteráveis, como listas, tuplas ou sequências, 
    e criar um novo iterável contendo os resultados das aplicações da função.

    O map retorna um objeto de mapa (map object), que é um iterável. Para obter os 
    resultados como uma lista ou outro tipo de sequência, você normalmente converte o 
    objeto de mapa em um tipo de sequência usando list(), tuple(), ou similar.
"""