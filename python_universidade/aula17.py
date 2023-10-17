# Importando Pandas
import pandas as pd
# Importando Matplotlib
import matplotlib.pylab as plt

# Fonte dos dados
'''
    Vamos utilizar a base de dados do Instituto Brasileiro de Geografia e Estatística (IBGE)
    sobre regiões, estados e cidades brasileiros que estão disponíveis em arquivo .csv no 
    repositório do GitHub a seguir.
'''

# Endereço web dos arquivos, mas poderia ser local.
urlRegião = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/regioes.csv'
urlEstado = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/estados.csv'

# Importa a tabela de dados.
dfRegiao = pd.read_csv(urlRegião)
dfEstado = pd.read_csv(urlEstado)

# Remove colunas do dataframe que não são relevantes para nossa análise.
del dfEstado['CodigoUf']

# Renomeia as colunas no dataframe.
dfRegiao.rename(columns={'Id': 'IdRegiao', 'Nome': 'Regiao'}, inplace=True)
dfEstado.rename(columns={'Id': 'IdEstado', 'Regiao': 'IdRegiao', 'Nome': 'Estado', 'Uf': 'UF'}, inplace=True)

# merge Região com Estado pela coluna IdRegiao.
df_innerRegiaoEstado = pd.merge(dfRegiao, dfEstado, on='IdRegiao', how='inner')
print('Grupos por Região '+'*'*20)

# Remove as colunas do DataFrane df_innerRegiaoEstado.
# .drop() é usado para remover colunas específicas do DataFrame. 
# No caso, estamos removendo as colunas 'IdEstado', 'Estado' e 'UF'.
# axis=1 é um argumento que especifica que as colunas devem ser removidas.
# O valor 1 representa colunas. Se fosse 0, indicaria a remoção de linhas.
df_gp = df_innerRegiaoEstado.drop(['IdEstado', 'Estado', 'UF'], axis=1)

# Criando um dataframe com: 
# .groupby() realiza uma operação de agrupamento (groupby) no DataFrame.
# .count() é um método para contar o número de ocorrências em cada grupo (nesse caso, o número de estados em cada região).
# .reset_index() é método usado para redefinir o índice do DataFrame resultante, para que o índice seja numérico em ordem crescente.
df_gp = pd.DataFrame(df_gp.groupby('Regiao').count().reset_index())

# .sort_values() é um método que classifica o DataFrame df_gp com base na coluna 'IdRegiao'. 
# by=[] especifica qual coluna deve ser usada para classificar o DataFrame.
# inplace=True faz a classificação no próprio DataFrame, em vez de retornar um novo DataFrame classificado.
# ascending=True indica que a classificação deve ser feita em ordem ascendente, ou seja, do menor número de estados para o maior número de estados.
df_gp.sort_values(by=['IdRegiao'], inplace=True, ascending=True)

# .rename() é um método usado para renomear colunas em um DataFrame. 
# Aqui, estamos renomeando a coluna 'IdRegiao' para 'Qtde', indicando o número de estados em cada região.
df_gp.rename(columns={'IdRegiao': 'Qtde'}, inplace=True)

# Imprimi as 20 primeiras linhas.
print(df_gp.head(20))

# .set_index() é um método do DataFrame que é usado para definir uma nova coluna como o índice do DataFrame. 
# Nesse caso, estamos definindo a coluna 'Regiao' como o índice do DataFrame. 
# Isso significa que a coluna 'Regiao' será usada como rótulo para identificar as linhas do DataFrame.
df_gp.set_index(['Regiao'], inplace=True)

# Cria um dicionário com as cores para as colunas.
my_dic_color = {'Qtde':['red', 'purple', 'blue', 'gray', 'black']}

# Configura o tipo de gráfico, tamanho da fonte e rótulos.
ax = df_gp.plot(kind='bar', rot=50, color = my_dic_color,
                figsize=(13, 6), fontsize=16, xlabel='Regiao', ylabel='Qtde', legend=False)

# Define as margins internas do gráfico e seus rotulos externos.
ax.margins(y=0.2, x=0.2)
ax.set_title('\n Quantidade de Estados por Região \n ', fontsize=16)
ax.set_xlabel('Região', fontsize=16)
ax.set_ylabel('Quantidade', fontsize=16)

# Configura o valores das colunas e sua localização na barra.
ax.bar_label(ax.containers[0], label_type='center', fontsize=16, color='white')

# Mostrar o gráfico de barras.
plt.show()


# Info
"""
    O gráfico vertical tem os valores referentes à quantidade de estados por região, 
    como apresentado no centro de cada barra vertical, configurado pela propriedade 
    label_type='center' na linha 37.
"""

# Importante
'''
    Mudar o formato do gráfico de barras verticais para horizontais em Python, fazendo 
    uso da biblioteca Matplolib, é simples, sendo necessário alterar o parâmetro 
    kind='bar' para kind='barh', com o h.

    As propriedades e os parâmetros para realizar essa alteração são:

    label_type='center' para label_type='edge'; e

    color='white' para color='black'.
'''