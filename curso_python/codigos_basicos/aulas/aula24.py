nome = 'Otávio'

print(nome[1])
print(nome[4])
print(nome[-1])
print(nome[-4])

print('a' in nome)
print('vio' in nome)
print("0" in nome)
print('vio' not in nome)
print('0' not in nome)

nome = input('Digite seu nome: ')
encontrar = input("Digite o que deseja encontrar: ")


if encontrar in nome:
    print (f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')
