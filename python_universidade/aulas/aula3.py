'''
CÁLCULO DO FATORIAL COM FUNÇÃO RECURSIVA
'''

def Fatorial(n):
    if n == 1:
        return 1
    else:
        return n * Fatorial(n-1) # acumalador n
    
while True:
    num = int(input('Digite um valor inteiro e positivo para calcular o fatorial: '))
    if(num > 0):
        print('Fatorial: ', Fatorial(num))
    else:
        print('Número inválido')
        break

'''
Estrutura Condicional ou de Decisão (if...elif...else)

A linguagem Python apresenta uma solução interessante ao problema de múltiplos if aninhados,
a cláusula elif, a qual substitui um par else...if, sem criar outro nível de estrutura, evitando
problemas de deslocamento desnecessário à direita (MENEZES, 2019).

Em Python não há uma construção como selecione caso ou switch...CA “se”; em vez disso, a
forma preferida e mais simples de se substituir esse comando, que existe nas linguagens que
derivaram da sintaxe de C, tais como Java, Java script, C++, C#, entre outras, é usar o if do Python,
que além do else tem a expressão elif, tal como apresentado na Figura 13:
'''

s = input (input('\nDigite o sementre que você está cursando: \n'))

if s == 1:
    print (f'O semestre que você está cursando é {s}!')
elif s == 2:
    print(f'O sementre que você está cursando é {s}!')
elif s == 3:
    print(f'O semestre que você está cursando é {s}!')
elif s == 4:
    print(f'O semestre que você está cursando é {s}!')
elif s == 5:
    print(f'O semestre que você está cursando é {s}!')
elif s == 6:
    print(f'O semestre que você está cursando é {s}!')
elif s == 7:
    print(f'O semestre que você está cursando é {s}!')
elif s == 8:
    print(f'O semestre que você está cursando é {s}!')
elif s == 9:
    print(f'O semestre que você está cursando é {s}!')
elif s == 10:
    print(f'O semestre que você está cursando é {s}!')
else:
    print(f'O semestre que você digitou {s} é inválido!')