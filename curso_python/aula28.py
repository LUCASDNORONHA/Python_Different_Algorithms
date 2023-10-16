print("Vamos coverter um número para o dobro dele!")

numero = input("Digite um número: ")

try:
    print('Valor {} ainda está no tipo string, vamos tentar converter para o tipo float'.format(numero))
    numero = float(numero)
    print('Valor {} foi convertido para númerico do tipo float'.format(numero))
    print('O dobro de {} é igual {}'.format(numero, (numero * 2)))
except:
    print("O caractere {} não é do tipo númerico, portanto não pode ser convertidade para o tipo float".format(numero))


'''

#Outra forma para fazer essa questão, seria:

numero = input('Digite um número:')

if numero.isdigit:
    numero = float(numero)
    print('O dobro de {} é igual {}'.format(numero, numero*2))

else:
    print('O caractere digitado não é um digito')
    
    '''