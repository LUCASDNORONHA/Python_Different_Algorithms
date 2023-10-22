dados_pessoa =  {} 

chave = 'Nome'
valor = 'Lucas'
dados_pessoa[chave] = valor

print(dados_pessoa)
print(dados_pessoa[chave])

del dados_pessoa[chave]

chave2 = 'Sobrenome'
valor2 = 'Dias Noronha'

dados_pessoa[chave2] = valor2

if dados_pessoa.get(chave2) is None:
    print('Chave não existe')
else:
    print(dados_pessoa[chave2])