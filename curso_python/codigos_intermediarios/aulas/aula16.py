# Exercícios - sistema de perguntas e repostas

print('Jogo de perguntas e reposta. Você deve selecionar uma das 4 opções de três perguntas. Boa sorte!')

perguntas = [
    {
        'Pergunta': 'Quanto é 2+3? ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
qtd_erros = 0

for pergunta in perguntas:

    print('Pergunta:', pergunta['Pergunta'])
    
    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)

    continuar = False

    while not continuar:
        escolha = input('Escolha uma opção: ')
    
        resposta_correta = pergunta['Resposta']

        acertou = False

        escolha_int =  None

        qtd_opcoes = len(opcoes)

        if escolha.isdigit():
            escolha_int = int(escolha)

        if escolha_int is not None:
            if escolha == resposta_correta and escolha in opcoes:
                acertou = True
                continuar = True
        else:
            print('Caractere digitado é inválido por não ser um digito.')
            continue
    

    if acertou is True:
        qtd_acertos += 1
        print('Acertou a resposta 👍')
    else:
        qtd_erros += 1
        print('Errou a resposta 👎')


print(f'Você acertou {qtd_acertos} de {len(perguntas)}.')