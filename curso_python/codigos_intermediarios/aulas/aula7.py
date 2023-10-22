def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicar)

def par_impar(n):
    multiplo_de_dois = n % 2 == 0

    if multiplo_de_dois:
        return '{n} é par'

    return '{m} é impar'
    

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(34))

