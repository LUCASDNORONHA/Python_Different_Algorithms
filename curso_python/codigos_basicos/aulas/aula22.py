entrada = input("[E] entrar [S] sair")

senha = input('Senha: ')

senhapermitida = '12345'


if (entrada == 'E' or entrada == 'e') and senha == senhapermitida:
    print('Entrar')

else:
    print("Sair")

print(False or False or True)
print(bool(0.0))

