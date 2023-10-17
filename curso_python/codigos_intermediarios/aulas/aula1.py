def imprimir (a, b, c, d):
    print(a, b, c, d)

imprimir(1, 2, 3, 4)


def saudacao( nome = 'Sem Nome' ):
    print( 'Olá, {}!'.format( nome ) )

saudacao('Lucas')
saudacao('Maria')
saudacao('Fernando')
saudacao()

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print('{} é multiplo de {}?'.format(numero, multiplo), end = ' ')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

