# Comparando valores digitados pelo usuário.

valor1 = int(input("Digite um valor: "))

valor2 = int(input("Digite outro valor: "))


if valor1 > valor2:
    print(f'O valor {valor1} é maior que o valor valor {valor2}')

elif valor1 == valor2:
    print(f'O valor {valor1} é igual o valor {valor2}')

else:
    print(f'O valor {valor2} é maior que o valor {valor1}')