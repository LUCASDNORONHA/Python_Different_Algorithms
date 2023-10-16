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
df_gp = df_innerRegiaoEstado.drop(['IdEstado', 'Estado', 'UF'], axis=1)
df_gp = pd.DataFrame(df_gp.groupby('Regiao').count().reset_index())
df_gp.sort_values(by=['IdRegiao'], inplace=True, ascending=True)
df_gp.rename(columns={'IdRegiao': 'Qtde'}, inplace=True)
print(df_gp.head(20))


df_gp.set_index(['Regiao'], inplace=True)

# Cria um dicionário com as cores para as colunas.
my_dic_color = {'Qtde':['red', 'purple', 'blue', 'gray', 'black']}

# Configura o tipo de gráfico, tamanho da fonte e rótulos.
ax = df_gp.plot(kind='bar', rot=50, color = my_dic_color,
                figsize=(13, 6), fontsize=16, xlabel='Regiao', ylabel='Qtde', legend=False)

# Define as margins internas do gráfico e seus rotulos externos.
ax.margins(y=0.2, x=0.2)
ax.set_title('\n Quantidade de Estados por Região \n ', fontsize=16)
ax.set_xlabel('Reguião', fontsize=16)
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