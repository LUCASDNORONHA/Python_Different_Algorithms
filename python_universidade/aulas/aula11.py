# Importando Pandas.
import pandas as pd

lst = [4, 7, -5, 3] # Criando uma lista.

obj = pd.Series(lst) # Criando um objeto Series do Pandas a partir da lista.

print(obj) # Retorna o objeto.

# Criando um segundo objeto a partir da lista, porém com indices nomeados de a, b, c, d.
obj2 = pd.Series(lst, index=['a', 'b', 'c', 'd'])

print(obj2) # Retorna o segundo objeto.

print(obj2['b']) # Retorna o índice b do objeto.

print(obj2[['c', 'a', 'd']]) # Retorna os índices mencionados.

# Dicionário
dir_tab = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.45,
}

obj3 = pd.Series(dir_tab) # Criando um terceiro objeto a partir do dicionário.

print(obj3) # Retorna o objeto.

print(pd.Series(dir_tab, index=['Alface', 'Tomate'])) # Retornado pelo índice.
