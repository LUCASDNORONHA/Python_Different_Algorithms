from itertools import combinations, permutations, product

# Combinations

# Gera todas as combinações de 2 elementos de uma lista
lista = [1, 2, 3, 4]
combs = combinations(lista, 2)

for comb in combs:
    print(comb)
# Saída:
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)

# Permutations

# Gera todas as permutações de 3 elementos de uma string
string = "abc"
perms = permutations(string, 3)

for perm in perms:
    print("".join(perm))

# Saída: 
# abc
# acb
# bac
# bca
# cab
# cba

# Product

# Gera o produto cartesiano de duas listas
lista1 = [1, 2]
lista2 = ['a', 'b']
prod = product(lista1, lista2)

for p in prod:
    print(p)

# Saída:
# (1, 'a')
# (1, 'b')
# (2, 'a')
# (2, 'b')

# Info
"""
    O módulo itertools em Python fornece funções para trabalhar com combinações, 
    permutações e produtos de elementos. 

    Essas funções do módulo itertools são muito úteis quando você precisa trabalhar 
    com combinações, permutações e produtos de elementos em Python. Elas podem ser 
    aplicadas em várias situações, como geração de subconjuntos, permutações de 
    caracteres, cálculos de coordenadas, entre outros.
"""