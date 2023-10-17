'''
lista de listas e seus indices
'''

salas = [

    ['Maria', 'Helena'], #0

    ['Lucas' ],#1
    
    ['Fernado', 'Rodolfo', 'Eduarda', (0, 10, 20, 30, 40)]#2

]

print(salas[1])
print(salas[0][1])
print(salas[2][3][2])

    
for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)