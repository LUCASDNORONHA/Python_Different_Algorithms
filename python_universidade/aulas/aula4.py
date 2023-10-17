'''LISTAS

A estrutura de dados mais simples
'''

L = ['A', 'B', 'C', 'D', 'E', 'F']

for elem in L:
    print(elem) 


L1 = list(range(7))
print(L1) # 0, 1, 2, 3, 4, 5, 6

L2 = list(range(1,9))
print(L2) # 1, 2, 3, 4, 5, 6, 7, 8, 9

L3 = list(range(1,12,2))
print(L3) # 1, 3, 5, 7, 9, 11

'''
TUPLA

Podem ser visto como uma lista, por ser muito semelhante, porém utilizam parenteses,
porém são imutaveis. O elementos também são ordenados.
'''

tupla = ('Maçã', 'Pera', 'Goiaba', 'Laranja', 'Manga')

print(tupla[1])
print(tupla[3])
print(tupla[3:])
print(tupla * 2)
print(len(tupla))
del tupla


'''
DICIONÁRIO

Dicionario é um objeto que contém mais que um valor.

O acesso a informação acontece por meio de chave a um valor especifíco.

Em Python criamos um utilizando chaves {}.

Cada elemento do dicionário é uma combinação de chave e valor.
'''

produto = {
           'Maçã': 0.90,
           'Pera': 4.99,
           'Goiaba': 3.78,
           'Laranja': 0.99,
           'Manga': 4.30,
}

print(produto) # Retorna tudo os elementos do dicionário
produto['Arroz'] = 17.99 # Adiciona
del produto['Manga'] # Deleta
print(produto.keys()) # Retorna as chaves
print(produto.values()) # Retorna os valores
print('Arroz' in produto) # True or False


'''
Estrutura de Repetição

For - Estrutura de bloco
'''

for elemento in produto:
    print(elemento)

for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)


'''
MÉTODO DE BOLHA (BUBBLE MEHOD)

Ordenação da lista
'''

import random # Módulo random

L = list(range(10)) # Sorteando 10 elementos de 0 a 9

L = random.sample(L, len(L)) # Colocando a sequência de valores em modo aleatório

print(L)

fim = len(L) # Número de elementos da lista

while fim > 1:
    trocou = False
    x = 0
    while x <(fim-1):
        if L[x] >  L[x+1]:
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] + temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)

'''
Numpy (Numeric Python)

'''

import numpy as np

l = [1, 2, 3, 4]

vetor = np.array(l)

va = np.arange(1, 5)

vetor2 = np.array([1, 2, 3, 4])

print(vetor)
print(va)
print(vetor2)

