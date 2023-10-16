# Jogo de Adivinhação de Profissão

# Autor: Lucas Dias Noronha

# O objetivo deste algoritmo é fazer o usuario tentar advinha o nome de uma certa profissão.



# Mensagem de iniciação do jogo de advinhação.
print ('Jogo de adivinhação!\n'\
       'Você deve tentar advinhar uma palavra.\n'\
        'A palavra é o nome de "Uma profissão".\n'\
        'Vamos começar!')

# Definindo a variável que irá armazenar a palavra secreta.
palavra_secreta = 'Enfermeira'.upper()
# Definindo a lista que irá armazenar as letras acertadas pelo usuario.
palavra_digitada = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
# Definindo a variável que armazenará a quantidade de letras acertada.
contador_acertos = 0
# Definindo a variável que armazenará a quantidade geral de tentativas, exceto quando o caractere digitador for inválido.
contador_geral = 0

# Estrutura de repetição "While" que cuidará de todo o processo.
while True:

    # Variável que armazenará os valores digitados pelo usuario.
    palavra = input('Digite uma letra: ').upper()

    # Verificando se o valor digitado é um digito.
    if palavra.isdigit():

        # Mensagem de erro.
        print('Caractere digitado não é um letra. Tente novamente.')
        # Comando para continuar do inicio a partir daqui.
        continue

    # Verificando se o valor digitado é mais de um caractere.
    elif len(palavra) > 1:

        # Mensagem de erro.
        print('Mais de um letra foi digitada. Tente novamente.')
        # Comando para continuar do inicio a partir daqui.
        continue

    # Verificando se a letra digitada não está na palavra secreta.
    elif palavra not in palavra_secreta:

        # Mensagem de erro.
        print('Letra digitado não faz parte da palavra. Tente novamente.')
        # Comando para continuar do inicio a partir daqui.
        continue

    # Verificando se a letra digitada está na palavra secreta.
    elif palavra in palavra_secreta:

        # Verificando se a letra digitada é igual "E" e se já não consta como contabilizada.
        if palavra == 'E' and palavra not in palavra_digitada:

            # Mensagem de acerto.
            print('Parabéns, você acertou três letras!')
            # Armazenando a letra na lista que armazenará as letras acertadas, de acordo com seu índice (para que as letras possam ser ordenadas em sua devida posição na palavra).
            palavra_digitada[0] = palavra
            # Como a letra se repete mais de uma vez na palavra, é preciso armazená-la em vários índice diferentes, de acordo com sua posição.
            palavra_digitada[3] = palavra
            # Como a letra se repete mais de uma vez...
            palavra_digitada[6] = palavra

            # Contabilizando os números de letras acertadas. 
            contador_acertos += 3
            # Contabilizando o número de tentativa.
            contador_geral += 1

        # Verificando se a letra digitada é igual "N" e se já não consta como contabilizada.
        elif palavra == 'N' and palavra not in palavra_digitada:

            print('Parabéns, você acertou uma letra!')
            # Armazenando a letra na lista que armazenará...
            palavra_digitada[1] = palavra

            # Contabilizando o número de letras acertadas. 
            contador_acertos += 1
            # Contabilizando o número de tentativa.
            contador_geral += 1
        
        # Verificando se a letra digitada é igual "F" e se já não consta como contabilizada.
        elif palavra == 'F' and palavra not in palavra_digitada:

            print('Parabéns, você acertou uma letra!')
            # Armazenando a letra na lista que armazenará...
            palavra_digitada[2] = palavra

            # Contabilizando o número de letras acertadas.
            contador_acertos += 1
            # Contabilizando o número de tentativa.
            contador_geral += 1

        # Verificando se a letra digitada é igual "R" e se já não consta como contabilizada.
        elif palavra == 'R' and palavra not in palavra_digitada:

            print('Parabéns, você acertou duas letras!')
            # Armazenando a letra na lista...
            palavra_digitada[4] = palavra
            # Armazenando a letra na lista...
            palavra_digitada[8] = palavra

            # Contabilizando os números de letras acertadas.
            contador_acertos += 2
            # Contabilizando o número de tentativa.
            contador_geral += 1

        # Verificando se a letra digitada é igual "M" e se já não consta como contabilizada.
        elif palavra == 'M' and palavra not in palavra_digitada:

            print('Parabéns, você acertou uma letra!')
            # Armazenando a letra na lista...
            palavra_digitada[5] = palavra

            # Contabilizando o número de letras acertadas.
            contador_acertos += 1
            # Contabilizando o número de tentativa.
            contador_geral += 1

        # Verificando se a letra digitada é igual "I" e se já não consta como contabilizada.
        elif palavra == 'I' and palavra not in palavra_digitada:

            print('Parabéns, você acertou uma letra!')
            # Armazenando a letra na lista...
            palavra_digitada[7] = palavra

            # Contabilizando o número de letras acertadas.
            contador_acertos += 1
            # Contabilizando o número de tentativa.
            contador_geral += 1

        # Verificando se a letra digitada é igual "A" e se já não consta como contabilizada.
        elif palavra == 'A' and palavra not in palavra_digitada:

            print('Parabéns, você acertou uma letra!')
            # Armazenando a letra na lista...
            palavra_digitada[9] = palavra

            # Contabilizando o número de letras acertadas.
            contador_acertos += 1
            # Contabilizando o número de tentativa.
            contador_geral += 1

        # Se a letra já foi contabilizada, será mostrada uma mensagem que já foi contabilizada.
        else:
            print('Letra digitada já foi contabilizada. Não digite letras repetidas.')

            # Contabilizando o número de tentativa.
            contador_geral += 1
        
        # A cada tentativa será mostrada a lista atualizada com ou sem acertos.
        print (palavra_digitada)

    # Definindo a condição para o laço "while" parar. Se o número de acerto for igual a quantidade de letras da palavra secreta.
    if contador_acertos == len(palavra_secreta):
        # Mensagem parabenizando o sucesso em descobrir a palavra secreta.
        print(f'Parabéns, após {contador_geral} tentativas, você descobriu a palavra!\n'\
              f'A palavra que representa uma profissão é "{palavra_secreta}".')
        
        # Comando parar o laço "while".
        break

# Fim