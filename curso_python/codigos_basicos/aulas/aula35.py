'''Calculadora com while'''

while True:

    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (+ - / *): ")

    numeros_validos = None

    try:
        numero1_float = float(numero_1)
        numero2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Número(s) inválidos.")
        continue

    operadores_permitidos = "+ - / *"

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print ("Digite apenas um operador.")
        continue

    print('Realizando operação.')
    
    if operador == '+':
        print(f'{numero1_float} + {numero2_float} = ', numero1_float + numero2_float)
    
    elif operador == '-':
        print(f'{numero1_float} - {numero2_float} = ', numero1_float - numero2_float)
    
    elif operador == '/':
        print(f'{numero1_float} / {numero2_float} = ', numero1_float / numero2_float)
    
    elif operador == '*':
        print(f'{numero1_float} * {numero2_float} = ', numero1_float * numero2_float)

    else:
        print("Algo deu errado.")


    sair = input("Quer sair? Digite [S]im ou [N]ão: ").lower().startswith('s')

    if sair is True:
        break