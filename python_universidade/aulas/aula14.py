# Importando o Pandas
import pandas as pd

# Criando o dataframe
df = pd.DataFrame(
    {
        'A':[9, 5, 6, 7],
        'B':[6, 7, 1, 4],
        'C':[3, 6, 0, 2],
    }, dtype = 'category' # Definindo um dataframe com variáveis do tipo categóricas.
)

# Imprimi o estado inicial do dataframe.
print('\nEstado inicial','*'*20,'\n',df,'\n')
# Imprimi a dimensionalidade do dataframe em linhas colunas.
print('Dimensionalidade do DataFrame Linhas e Colunas', '*'*20, '\n',df.shape,'\n')
# Imprimi as informações do dataframe.
print('\nInformações do DataFrane','*'*20, '\n'), print(df.info(),'\n')


'''
Variáveis Categóricas

As variáveis categóricas são os tipos de dados disponíveis na biblioteca Pandas do Python.
Uma variável categórica recebe apenas uma categoria fixa (geralmente um número fixo) de 
valores. Alguns exemplos de variáveis categóricas são sexo, grupo sanguíneo, idioma etc. 
Um contraste principal com essas variáveis é que nenhuma operação matemática pode ser 
realizada com elas.

Um DataFrame pode ser criado em Pandas, consistindo em valores categóricos usando o 
construtor DataFrame e especificando dtype=“category”. Na Figura 6 é apresentado o 
script para a criação manual de um DataFrame do tipo categórico.
'''