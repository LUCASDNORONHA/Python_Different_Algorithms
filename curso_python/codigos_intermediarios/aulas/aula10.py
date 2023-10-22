def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadruplicar(numero):
    return numero * 4

def criar_multplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multplicador(2)
triplicar = criar_multplicador(3)
quadruplicar = criar_multplicador(4)

print(duplicar(3))
print(triplicar(5))
print(quadruplicar(6))