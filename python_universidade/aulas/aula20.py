# RECURSIVIDADE

# Calculo do fatorial

# Função comum sem recursividade.
def fatorial(n):

    resultado = 1          
    for i in range(1, n + 1):
        resultado *= i
        # print(resultado)

    return f'O fatorial de {n} é {resultado}'

# Função com recursividade.
def fatorial_recursiva(n):
    # Caso base
    if n == 1:
        return 1
    return n * fatorial_recursiva(n - 1)

# Váriavel que recebe valor
n = int(input('Digite um número inteiro para calcularmos o fatorial : '))

# print(fatorial(n))
print(fatorial_recursiva(n)) 

"""
    A recursividade é um conceito em programação no qual uma função chama a si mesma 
    para resolver um problema. É comumente usado em situações em que um problema pode 
    ser decomposto em subproblemas semelhantes. Aqui está um exemplo clássico de 
    cálculo do fatorial de um número.

    O fatorial de um número inteiro não negativo n, denotado por n!, é o produto de 
    todos os números inteiros de 1 a n. Ele é definido da seguinte forma:

    n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
"""