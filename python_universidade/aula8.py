import numpy as np

'''Dimensões'''

a = np.array(23) # OD ou Zero dimensões
b = np.array([1, 2, 3, 4]) # 1D ou Uma dimensão
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) # 2D ou Duas dimensões
d = np.array([
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
    [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
]) # 3D ou três dimensões

print(
    f'{a}\n Número de dimensões : {a.ndim}\n {b}\n Número de dimensões : {b.ndim}\n {c}\n Número de dimensões : {c.ndim}\n {d}\n Número de dimensões : {d.ndim}\n'
)

arr = np.array([1, 2, 3, 4], ndmin=5) # 5D ou Cinco dimensões

print(arr)
print('Numero de dimensões : ', arr.ndim)


'''
Métodos:

.ndim retorna as dimensões de um ndarray
.ndmin é uma parâmetro que define o número de dimensões durante a criação de um ndarray

'''