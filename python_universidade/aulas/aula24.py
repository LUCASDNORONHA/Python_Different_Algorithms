# DECORATOR

# Função decorator.
def my_decorator(function):
    # Função interna que encapsula a função dentro dos parâmetro.
    def wrapper():
        # criar um novo escopo de código.
        print('Antes da função ser chamada')
        # Posso retornar a função antiga, se eu quiser.
        function()
        # Posso criar um novo escopo após chamar a função antiga.
        print('Após a função ser chamada')
    # Retornando a função wrapper (função interna)
    return wrapper

# Chamando a função decorator.
# Ou seja, quando eu chamar a my_function, não será ela que irá roda, e sim my_decorator.
@my_decorator
def my_function():
    print('Minha função original')

# Chamando a função
my_function()

# Info
"""

    Funções decoradas, também conhecidas como decorators em Python, são uma 
    característica poderosa da linguagem que permite modificar o comportamento 
    de funções ou métodos de uma maneira limpa e reutilizável. Elas são usadas 
    principalmente em Python para adicionar funcionalidades a funções existentes 
    sem modificar seu código subjacente. Decorators são amplamente utilizados em 
    frameworks e bibliotecas populares, como o Flask e o Django, para tarefas como 
    autenticação, registro de log, validação de entrada, entre outras.

    Uma explicação de como os decorators funcionam em Python:

    Funções como objetos: Em Python, as funções são tratadas como objetos de primeira 
    classe. Isso significa que você pode atribuí-las a variáveis, passá-las como 
    argumentos para outras funções e até mesmo retorná-las de outras funções.

    Definição de um decorator: Um decorator é, em si, uma função que toma outra função 
    como argumento e retorna uma nova função que geralmente estende ou modifica o 
    comportamento da função original. Um decorator é definido usando a função "@" 
    antes da função que você deseja decorar.
"""

