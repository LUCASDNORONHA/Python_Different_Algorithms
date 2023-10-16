'''
ESTRUTURA DE REPETIÇÃO: while
'''

# While simples

# x será a variável de controle.
x = 0

# Tabuada de multiplicação de 2.
while x <= 10:
    print(f'2x {x} = ' + str(2*x))
    x = x + 1

# While composto

tab = 1
# Tabuada de 1 a 10.
while tab <= 10:
    indice = 0
    while indice <= 10:
        print(f'{tab} x {indice} = {tab*indice}')
        indice += 1
    print('\n')
    tab += 1


'''
Estrutura de Repetição: for
'''
# For simples
for indice in range(0, 11, 1):
    print(f'2x {indice} = ' + str(2*indice))

# While composto/aninhado
for tab in range (1, 11, 1):
    for indice in range(0, 11, 1):
        print(f'{tab} x {indice} = ' + str(tab*indice))
    print('\n')


'''
CÁLCULO DO FATORIAL: WHILE
'''

# ESTRUTURA WHILE
num = int(input('Digite um valor inteiro e positivo para calcular o fatorial: '))

result = 1 # Acumulador
count = 1 # Contador

while count <= num:
    result *= count
    count += 1

print(result)

# ESTRUTURA FOR
num = int(input('Digite um valor inteiro e positivo para calcular o fatorial: '))

fat = 1

for n in range(1 , num+1, 1):
    fat *= n

print(fat)


'''
CÁLCULO DO FATORIAL COM FUNÇÃO RECURSIVA
'''

def Fatorial(n):
    if n == 1:
        return 1
    else:
        return n * Fatorial(n-1) # acumalador n
    
while True:
    num - int(input('Digite um valor inteiro e positivo para calcular o fatorial: '))
    if(num > 0):
        print('Fatorial: ', Fatorial(num))
    else:
        print('Número inválido')
        break
