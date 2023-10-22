'''

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

EX.: 746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
resultado é 0

contrario disso:
resultado é o valor da conta

O primeiro digito do CPF é 7
'''

CPF = input( 'Digite o seu CPF, sem pontos ou traços: ' )

nove_digitos =  CPF[0:9:1]

Validar = True if nove_digitos == 9 else False

somar_todos_valores = 0


for indice in range( len( nove_digitos ) ):

    multiplo = 10

    multiplicar_resultado = int( nove_digitos[ indice ] ) * multiplo

    somar_todos_valores += multiplicar_resultado

    multiplo -= 1


multiplicar_resultado_por_10 = somar_todos_valores * 10

resto = multiplicar_resultado_por_10 % 11

primeiro_digito_verificador_CPF = resto if resto <= 9 else 0

print('O primeiro digito verificador do seu CPF é: ', primeiro_digito_verificador_CPF)
