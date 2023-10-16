import pandas as pd

lst = [4, 8, -7, 6, 5,]

obj = pd.Series(lst)

print(obj)

lst = [4, 8, -7, 6, 5,]
obj = pd.Series(lst, index=['a', 'b', 'c', 'd', 'e',])

print(obj)
print(obj['b'])
print(obj[['c', 'd', 'e']])

df = pd.DataFrame({
    'Coluna A': ['a', 'b', 'c', 'd'],
    'Coluna B': [1, 2, 3, 4]
    })

print(df) # Apresenta o DataFrame
print(df.columns) # Nome dos índices de coluna (axis = 1)
print(df.index) # Nome dos índices de linha (axis = 0)
print(df.shape) # Número de linhas e colunas
print(df.size) # Número de cédulas