frase = 'o Python é uma línguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais <= qtd_atual:

        qtd_apareceu_mais = qtd_atual

        letra_apareceu_mais = letra_atual

    i += 1

print('A letra que apareceu mais foi a letra '
      f'"{letra_apareceu_mais}" que apareceu, '
     f'{qtd_apareceu_mais} vezes.' )




