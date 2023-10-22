lista = ['Maria', 'Lucas', 'João']
lista.append('Fernando')

lista_enumerada = enumerate(lista)

print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)
