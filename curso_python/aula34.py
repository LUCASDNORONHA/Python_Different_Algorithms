nome = 'Lucas Dias Noronha'


tamanho = len(nome)

contador = 0

novo_nome = ""

while contador < tamanho:
    
    letra = f'{nome[contador]}*'
    novo_nome += letra

    contador += 1

print(novo_nome)