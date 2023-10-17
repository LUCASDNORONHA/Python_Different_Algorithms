def exibir(lista):
    for item in lista:
        print(item)

lista = [
    {'Nome': 'Lucas', 'Sobrenome': 'Dias'},
    {'Nome': 'Fernando', 'Sobrenome': 'Rodriguez'},
    {'Nome': 'Leonardo', 'Sobrenome': 'Silva'},
    {'Nome': 'Maria', 'Sobrenome': 'Pereira'},
    {'Nome': 'Daniel', 'Sobrenome': 'Galeleu'}
]

print("Lista original:")
exibir(lista)
print()

lista_ordenada_por_nome = sorted(lista, key=lambda item: item['Nome'])
lista_ordenada_por_sobrenome = sorted(lista, key=lambda item: item['Sobrenome'])

print("Ordenada pelo nome:")
exibir(lista_ordenada_por_nome)

print("Ordenada pelo sobrenome:")
exibir(lista_ordenada_por_sobrenome)


