'''

EXERCICIO 3

Faça um program que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; e maior que 5 e 6 letras, escreva "Seu nome é grande".

'''

nome = input ('Digite seu nome: ')

letras = len(nome)

if letras >= 0 and letras <= 4:
    print('Seu nome tem {} letras, então ele é pequeno'.format(letras))
elif letras >= 5 and letras <= 6:
    print('Seu nome tem {} letras, então ele é médio'.format(letras))
else:
    print('Seu nome tem {} letras, então ele é grande'.format(letras))