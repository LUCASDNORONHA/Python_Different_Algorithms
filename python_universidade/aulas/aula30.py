from functools import reduce

# Exemplo 1:

# Lista de produtos;
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 12', 'preco': 50.04},
    {'nome': 'Produto 1', 'preco': 18.99},
    {'nome': 'Produto 3', 'preco': 2.25},
    {'nome': 'Produto 2', 'preco': 23.99},
    {'nome': 'Produto 6', 'preco': 89.30},
    {'nome': 'Produto 4', 'preco': 20.00},
    {'nome': 'Produto 8', 'preco': 65.75},
    {'nome': 'Produto 9', 'preco': 44.50},
    {'nome': 'Produto 10', 'preco': 0.99},
    {'nome': 'Produto 7', 'preco': 140.00},
    {'nome': 'Produto 13', 'preco': 24.00},
    {'nome': 'Produto 11', 'preco': 34.00},
]

# Função para reduzir e calcular o total dos preços dos produtos.
def funcition_reduce(acumulador, elemento):
    return acumulador + elemento['preco']

total = reduce(funcition_reduce, produtos, 0)

print('-' * 40)
print(f'Total: {total:.2f}')
print('-' * 40)

# Exemplo 2:

# Lista com letras do alfabeto.
alfabeto = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z'
]

# Função para reduzir e concatenar as letras do alfabeto.
def concatenar_letras(acumulador, letra):
    return acumulador + (' - ' + letra)

# Usando método reduce para listar o alfabeto ordenado em um elemento.
alfabeto_ordenado = reduce(concatenar_letras, alfabeto, "")

print()
print(f'Alfabeto ordernado :\n {alfabeto_ordenado}')
print('-' * 40)

# Info
"""
    O método reduce não é uma função integrada em Python 3. Ele estava presente na 
    biblioteca padrão do Python 2 e no módulo functools, mas a partir do Python 3, 
    foi movido para um pacote separado chamado functools.reduce.

    O método reduce é usado para aplicar uma função cumulativa a elementos de um 
    iterável, de forma que ela reduza os elementos a um único valor agregado. A função 
    cumulativa recebe dois argumentos e acumula o resultado ao longo de todo o iterável. 
    No entanto, devido à sua complexidade e potencial de erro, o uso de reduce é 
    desencorajado em favor de soluções mais legíveis, como loops for ou compreensões 
    de lista.
"""

