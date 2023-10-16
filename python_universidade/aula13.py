# Importando o pandas
import pandas as pd

# Criando nosso dataframe com duas colunas.
df = pd.DataFrame({'Chave':['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
                   'Dados':[9, 5, 3, 5, 7, 6, 6, 1, 0, 7, 4, 2]
})

print(df) # Retorna nosso dataframe

print('Grupos pela coluna Chave' + '*'*20)  # Titulo

groups = df.groupby(df.Chave) # Atribui os grupos

A_df = groups.get_group('A') # Pega o grupo A
B_df = groups.get_group('B') # Pega o grupo B
C_df = groups.get_group('C') # Pega o grupo C

print('Grupo A', '*'*20) # Titulo
print(A_df, '\n') # Retorna o grupo A
print('A soma do grupo A = ' + str(A_df['Dados'].sum())) # Retorna o somatório dos valores do grupo A
print(groups.get_group('A')['Dados'].sum()) # Retorna o somatorio do grupo A
print('Grupo B', '*'*20) # Titulo
print(B_df,'\n') # Retorna grupo B
print('A soma do grupo B = '+ str(B_df['Dados'].sum())) # Retorna o somatório dos valores do grupo B.
print('Grupo C'+'*'*20) # Titulo
print(C_df, '\n') # Retorna grupo C
print('A soma do grupo C = '+ str(C_df['Dados'].sum())) # Retorna o somatório dos valores do grupo C.


'''
O agrupamento é usado para agrupar uma ou mais colunas em um DataFrame usando o método 
Groupby(). O Groupby refere-se, principalmente, a um processo que envolve uma ou mais 
das seguintes etapas:

Divisão: é um processo no qual os dados são divididos em grupos, aplicando algumas 
condições nos conjuntos de dados;

Aplicação: é um processo no qual é aplicada uma função a cada grupo, de forma 
independente;

Combinação: é um processo no qual são combinados diferentes conjuntos de dados após 
a aplicação de Groupby, resultando em uma estrutura de dados.

Agrupar e manipular dados com Pandas é muito comum em Análise ou Ciência de Dados 
para responder a perguntas do tipo “Qual é a soma dos valores da categoria A?” ou 
questões similares. Para responder a essas questões, é necessário agrupar os dados 
de acordo com a sua categoria.
'''