# Medir o Espaço Ocupado na Memória

# Importa o módulo sys para acessar funções relacionadas ao sistema
import sys

# Definindo as primeiras três tuplas
Tuple1 = ('A', 1, 'B', 2, 'C', 3)
Tuple2 = ('Geek1', 'Raju', 'Geek2', 'Nikhil', 'Geek3', 'Deepanshu')
Tuple3 = ((1, 'Lion'), (2, 'Tiger'), (3, 'Fox'), (4, 'Wolf'))

# Calculando e imprimindo o tamanho em bytes das primeiras três tuplas usando o método __sizeof__()
print('Size of Tuple1: ' + str(Tuple1.__sizeof__()) + ' bytes')
print('Size of Tuple2: ' + str(Tuple2.__sizeof__()) + ' bytes')
print('Size of Tuple3: ' + str(Tuple3.__sizeof__()) + ' bytes')

# Definindo as segundas três tuplas
Tuple4 = ('A', 1, 'b', 2, 'c', 3)
Tuple5 = ('Geek', 'Baju', 'Geek2', 'Nikhil', 'Geek3', 'Deepanshu')
Tuple6 = ((1, 'Lion'), (2, 'Tiger'), (3, 'Fox'), (4, 'Wplf'))

# Calculando e imprimindo o tamanho em bytes das segundas três tuplas usando a função sys.getsizeof()
print('Size of Tuple4: ' + str(sys.getsizeof(Tuple4)) + ' bytes')
print('Size of Tuple5: ' + str(sys.getsizeof(Tuple5)) + ' bytes')
print('Size of Tuple6: ' + str(sys.getsizeof(Tuple6)) + ' bytes')
