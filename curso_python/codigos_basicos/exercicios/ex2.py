# Algoritmo que verifica se um número é par ou impar.

# Auto: Lucas Dias Noronha

'''
Programa que pede ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite o
número inteiro, será informado que não é um número.
'''

# Recebendo o valor digitado pelo usuário.
numero = input("Digite um número: ")

# Verificando se o valor digitado é um digito.
if numero.isdigit():

    # Convertendo o valor digitado para número inteiro.
    numero = int(numero)

    # Verificando se o valor digitado divido por 2 tem resto 0.
    if numero % 2 == 0:
        print("%i é um número par." % numero)

    # Caso o resto não seja 0, então o seguinte bloco será executado.
    else: 
        print("%i é um número impar." % numero)

# Caso não seja um digito, o seguinte bloco será executado.
else:
    print('O valor digitado não é um número, portanto não pode ser convertido para número inteiro.')

# FIM