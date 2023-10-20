# Recursividade

# Funções recursvas.

# Definindo um método chamada fibonacci(n):
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(0)) # Saída: 0
print(fibonacci(1)) # Saída: 1
print(fibonacci(7)) # Sáida: 13 (o sétimo número na sequência.)

# Info
"""
    Um exemplo clássico de uma função recursiva que calcula a sequência de Fibonacci. 
    A sequência de Fibonacci é uma sequência de números em que cada número é a soma dos 
    dois números anteriores na sequência, começando com 0 e 1. Portanto, a sequência 
    começa assim: 0, 1, 1, 2, 3, 5, 8, 13, ...

    Tenha em mente que, embora a recursão seja uma maneira elegante de calcular a 
    sequência de Fibonacci, ela pode ser ineficiente para valores grandes de n, pois a 
    função realiza muitos cálculos repetidos. Em tais casos, técnicas de memoização 
    (armazenamento em cache dos resultados) ou uma abordagem iterativa podem ser mais 
    eficientes.
"""