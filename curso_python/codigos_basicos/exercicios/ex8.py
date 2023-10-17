# Algoritmo simples para validação de CPF.

# Autor: Lucas Dias Noronha



# O seguinte processo tem como objetivo validar o primeiro digito verificador do CPF.

# Recenbendo o CPF digitado pelo usuário.
CPF_usuario = input('Digite seu CPF sem pontos ou traços: ')
# Adicionados os nove primeiros digito do CPF em uma nova variável.
nove_digitos = CPF_usuario[0:9:1]

# Uma variavél global para armazenar o resultado dos calculos de validação do primeiros digito verificador no seguinte laço for.
resultado1 = 0

# Estrutura de repetição "laço for".
for digito in nove_digitos:
    
    # Uma variável local para armazernar o valor dos multiplos.
    multiplo_digito_1 = 10

    # Uma variável para armazenar o resultador da multiplicação de cada indice pelo multiplo (definido anteriormente).
    resultado1 += int(digito) * multiplo_digito_1

    # Em cada iteração, o valor do multiplo será subtraido por 1. 
    multiplo_digito_1 -= 1

# Uma variável para armazenar o resto.
digito_1 = (resultado1 * 10) % 11

# Atualizando a variável (anterior) com o valor do primeiro digito verificador.
digito_1 = digito_1 if digito_1 <= 9 else 0


############################################


# O seguinte processo tem como objetivo validar o segundo digito verificador do CPF.

# Adicionados os 10 primeiros digito do CPF em uma nova variável.
dez_digitos = CPF_usuario[0:10:1]

# Uma variavél global para armazenar o resultado dos calculos de validação do segundo digito verificador no seguinte laço for.
resultado2 = 0

# Estrutura de repetição "laço for".
for digito in dez_digitos:

    # Uma variável local para armazernar o valor dos multiplos.
    multiplo_digito_2 = 11
    
    # Uma variável para armazenar o resultador da multiplicação de cada indice pelo multiplo (definido anteriormente).
    resultado2 += int(digito) * multiplo_digito_2

    # Em cada iteração, o multiplo terá um valor subtraido.
    multiplo_digito_2 -= 1

# Uma variável para armazenar o resto.
digito_2 = (resultado2 * 10) % 11

# Atualizando a variável (anterior) com o valor do segundo digito verificador.
digito_2 = digito_2 if digito_2 <= 9 else 0


############################################

# O seguide processo tem como objetivo válidar o CPF.

# Uma variável para armazenar o CPF válidado.
CPF_validado = f'{nove_digitos}{digito_1}{digito_2}'

# Se o CPF digitado for igual CPF válidado, então o CPF é válido.
if int(CPF_usuario) == int(CPF_validado):
    print(f'O CPF {CPF_usuario} é válido.')

# Caso Contrario, o CPF é inválido.
else:
    print('CPF inválido.')

# Fim