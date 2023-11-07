# Algoritmo para geração de 100 CPF válidos.

# Autor: Lucas Dias Noronha



# Importando módulo 'random' para utilizar funções geradoras de números aleatórios.
import random

# Através deste laço "for", será feito 100 repetições onde em cada repetição (iteração) será gerado 1 CPF.
for _ in range ( 100 ):

    # Variável para armazenar os noves caracteres do CPF.
    nove_digitos = ''

    # Atráves deste laço "for", será gerado nove digitos aleatórios.
    for i in range( 9 ):
        
        # Em cada iteração, será gerado um número entre 0 a 9 (utilizando a função '.randint' do moduludo random) que será concatenado a variável 'nove digito'.
        nove_digitos += str( random.randint(0, 9) )


    ##################################################


    # Todo os bloco de código abaixo é para fazer os calculos de validação que irão gerar os dois digitos verificadores do CPF atráves dos noves digitos gerados acima.
    


    # Gerando e válidando primeiro digito verificador do CPF.
    
    Multiplo_primeiro_digito = 10

    resultado_digito_1 = 0


    for digito in nove_digitos:

        resultado_digito_1 += int( digito ) * Multiplo_primeiro_digito
        Multiplo_primeiro_digito -= 1

    
    primeiro_digito_verificador = ( resultado_digito_1 * 10 ) % 11

    primeiro_digito_verificador = primeiro_digito_verificador if primeiro_digito_verificador <= 9 else 0




    # Gerando e válidando o segundo digito verificador do CPF.


    dez_digitos = nove_digitos + str( primeiro_digito_verificador )

    Multiplo_segundo_digito = 11

    resultado_digito_2 = 0


    for digito in dez_digitos:

        resultado_digito_2 += int( digito ) * Multiplo_segundo_digito

        Multiplo_segundo_digito -= 1


    segundo_digito_verificador = ( resultado_digito_2 * 10 ) % 11

    segundo_digito_verificador = segundo_digito_verificador if segundo_digito_verificador <= 9 else 0



    # Gerando CPF completo.

    cpf_gerado_pelo_calculo = f'{ nove_digitos }{ primeiro_digito_verificador }{ segundo_digito_verificador }'

    print( cpf_gerado_pelo_calculo )


# FIM