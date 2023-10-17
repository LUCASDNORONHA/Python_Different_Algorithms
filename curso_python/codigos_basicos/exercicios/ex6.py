estoque = ('Pacote  de Arroz', 'Pacote de Feijão', 'Pacote de Macarrão',\
            'Pacote de Trigo','Maçã', 'Goiaba', 'Laranja')

carrinho = []
quantidade_levar = 0

while True:
    comprar = input('Desejar comprar algum item do nosso estoque? Sim ou Não? ').lower()

    if comprar == 'sim':

        while True:
            print('Produtos em estoque:\n', estoque)

            item = input('Qual item do nosso estoque você vai querer levar? Digite o nome corretamente: ')
            quantidade = int(input('Quantidade: '))

            if item.isdigit():
                print('Valor digitado é inválido.')
                continue
            elif item not in estoque:
                print('Valor digitado não consta no nosso estoque.')
                continue
            elif item in estoque:
                carrinho.append(item)
                quantidade_levar += quantidade
                print('Produto adicionado ao carrinho.')

            
            comprar = ('Deseja adicionar mais itens ao carrinho? Sim ou Não: ').lower()

            if comprar == 'não':
                print('Você escolheu sair.')
                break
        
        print('Seus inten(s) são ', carrinho)
        
        remover = input('Deseja finalizar a compra ou remover algum do seu carrinho? Digite Remover ou Finalizar: ').lower()
        
        if remover == 'remover' or remover == 'finalizar':

            if remover == 'remover':

                while True:

                    print(carrinho)

                    apagar = input('Digite sem erros o nome do item que deseja remover: ')
            
                    if apagar in carrinho:
                        carrinho.pop(apagar)
                        print('Item removido com sucesso.')  
                    else:
                        print('Item digitado não consta na lista. Digite novamente.')
                        continue
                
                    continuar = input('Deseja remover mais algum item do seu carrinho? Sim ou Não: ').lower()

                    if continuar == 'sim':
                        continue
                    elif continuar == 'não':
                        break


            elif remover == 'finalizar':
                print('Finalizando a comprar.')


    elif comprar == 'não':
        print('Vocês escolheu sair. Finalizando programa.')
        break

    else:
        print('Valor digitado é invalido, tente novamente.')

