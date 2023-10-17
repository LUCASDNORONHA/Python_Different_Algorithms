'''

EXERCICIO 2

Faça um programa que pergunte a hora ao usuário e, baseando-se no horario
descrito. exiba a saudação apropriada. 

Ex:

Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

'''

horario = float(input('Informe o horário atual em formato de 0 a 24: '))

if horario >= 0 and horario <= 11:
    print('Boa dia!')
elif horario >= 12 and horario <= 17:
    print('Boa tarde!')
else:
    print("Boa noite!")

