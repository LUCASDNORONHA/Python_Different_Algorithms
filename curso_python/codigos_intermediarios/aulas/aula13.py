pessoa = {
    'Nome': 'Lucas',
    'Sobrenome': 'Dias Noronha',
    'Idade': 25,
}

pessoa.setdefault('Idade', 0)
print(pessoa['Idade'])

# print(pessoa.__len__())
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for chave in pessoa.keys():
#    print(chave)

# for chave in pessoa:
#    print(chave)

# for chave, valor in pessoa.items():
#    print(chave, valor)

