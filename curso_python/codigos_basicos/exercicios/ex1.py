nome = input('Digite seu nome: ')

idade = input('Digite sua idade: ')

if nome and idade != None:

    print (f'Seu nome é {nome}')
    print (f'Seu nome invetido é {nome[::-1]} ')
    
    if " " in nome:
        print (f'Seu nome contém espaço')

    else:
        print ('Seu nome não contém espaço')

    print (f'Seu nome tem {len(nome)} letras')
    print (f'A primeira letra do seu nome é {(nome[0])}')
    print (f'A ultima letra do seu nome é {(nome[-1])}')

else:

    print('Desculpe, você deixou o campo vazio')