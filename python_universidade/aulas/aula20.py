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