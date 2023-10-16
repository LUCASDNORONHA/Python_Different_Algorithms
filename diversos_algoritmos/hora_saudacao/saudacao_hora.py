# Algoritmo simples para verificar a saudação apropriada de acordo com a hora.

# Autor: Lucas Dias Noronha

'''
Programa que pergunta a hora ao usuário e, baseando-se no horario
descrito. exiba a saudação adequada. 
'''

# Armazenado a hora.
horario = float(input('Informe o horário atual em formato de 0 a 24: '))

# Verificando se é manhã.
if horario >= 0 and horario <= 11:
    print('Bom dia!')

# Verificando se é tarde.
elif horario >= 12 and horario <= 17:
    print('Boa tarde!')

# Caso não seja nenhumas das outras, então é noite.
else:
    print("Boa noite!")

