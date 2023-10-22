# Python | Contar ocorrências de um elemento em uma lista

lista_numeros = [2, 3, 5, 1, 5, 6, 8, 5, 10, 0]

print(lista_numeros)

elemento = input('Digite um elemento para verificar quantas vezes ele aparece na lista: ')

ocorrencias =  lista_numeros.count(int(elemento))

print('O elemento {} aparecer {} vez(es) na lista.'.format(elemento, ocorrencias))
