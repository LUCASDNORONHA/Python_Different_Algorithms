# Diferença entre método count() e range().

# Método range
iterator_range = range(1, 50, 5)

# Método count
from itertools import count
iterator_count = count(start=1, step=5)

# Iteração com método range.
for i in range(2, 10, 2):
    print(i)

# Usando o método range() para definir um fim para o iterator_count.
for i in range(5):
    print(next(iterator_count))

# Info
"""
    range() e count() são duas funções/métodos em Python que têm finalidades diferentes:

    
    range():

    range() é uma função que cria uma sequência de números inteiros, geralmente usada 
    em laços de repetição como for.
    Ela recebe até três argumentos: start, stop e step (início, parada e passo).
    start é o valor inicial da sequência (por padrão, é 0).
    stop é o valor em que a sequência para (o valor máximo não está incluso).
    step é a diferença entre os valores da sequência (por padrão, é 1).
    range() retorna um objeto iterável que gera os valores da sequência sob demanda.

    
    count():

    count() é um método de um objeto do tipo "iterador" da biblioteca padrão Python, 
    como é o caso do iterador infinito itertools.count().
    Ele gera uma sequência infinita de números inteiros a partir de um valor inicial e 
    com um passo definido.
    count() não tem um valor de parada, o que significa que ele continuará gerando números 
    indefinidamente, a menos que seja interrompido manualmente.
"""