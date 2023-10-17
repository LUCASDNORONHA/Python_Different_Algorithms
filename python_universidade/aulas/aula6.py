def funcao():
    x = 2 # Variável local
    print(x)

x = 7 # Variável global

funcao() # Retorna 2

print(x) # Retorna 7

def somar(*args):
    soma = sum(args)
    return soma

print(somar(33, 45, 65, 34))

somar2 = lambda *args: sum(args)

print(somar2(33, 45, 65, 34))

imprimir = lambda str: print(str)

print(imprimir('Hello World!')) # Retorna o texto mas também retorna None

imprimir('Hello World!')
