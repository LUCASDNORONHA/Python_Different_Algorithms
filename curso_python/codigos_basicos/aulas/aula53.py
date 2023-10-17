# .strip() r ou l

frase = 'Olha só que , coisa interessante.'

lista_palavras_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_palavras_cruas):
    lista_frases.append(lista_palavras_cruas[i].strip())

print(lista_palavras_cruas)
print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)