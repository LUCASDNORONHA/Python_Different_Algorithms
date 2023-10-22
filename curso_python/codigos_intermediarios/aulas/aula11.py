pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Dias Noronha',
    'idade': 23,
    'altura': 1.8,
    'endereço': {
        'rua': 'tal',
        'numero': 2345,
        'bairro': 'tal',
        'cidade': 'tal',
        'estado': 'tal',
        'país': 'tal',
    }
}
#pessoa = dict(nome= 'Lucas', sobrenome= 'Dias Noronha')

print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])

