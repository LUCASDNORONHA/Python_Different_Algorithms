string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [

    ['Maria', 'Helena'], #0

    ['Lucas' ],#1
    
    ['Fernado', 'Rodolfo', 'Eduarda', (0, 10, 20, 30, 40)]#2

]

a, b, *_, u = lista
print(a, u)


for nome in lista:
    print(nome, end=' ')


print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)
print(*string)
print(tupla)

print(*salas, sep='\n')
