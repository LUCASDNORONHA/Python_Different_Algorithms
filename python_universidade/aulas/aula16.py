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

# PERGUNTA:
# Qual a porcentagem de estados por região?
# Qual a quantidade de estados por região?

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


# Ajusta os labels para a geração do Gráfico em formato pizza (Gráfico de Setores).
labels = [str(df_gp['Qtde'][i]) + ' ' + str(df_gp['Regiao'][i]) for i in df_gp.index]

# Espaçamento da divisão entre as partes do gráfico.
parts = (0.1, 0.1, 0.1, 0.2, 0.3)

# Cria o Gráfico. O método shadow=True é reponsável pelo sombreamento dando um aspecto de 3D.
plt.pie(df_gp['Qtde'], labels=labels, autopct='%1.2f%%', shadow=True, explode=parts)
plt.title('Estados por região', loc = 'center', fontdict = {'fontsize':15, 'fontweight':13}, color='White')

# Define que o gráfico será plotado em circulo
plt.axis('equal')

# Apresenta o gráfico de setores (pizza).
# Os rótulos internos apresentam a porcentagem de estados por região.
# os externos apresentam o nome da região e a quantidade de estados por região.
plt.show()



# Info
"""
    Data Visualization

    Ao trabalhar com dados, visualizá-los em modo tabular pode ser difícil de entender. 
    Para compreender exatamente o que os dados transmitem, é necessário limpá-los e 
    selecionar modelos adequados para visualizá-los ou representá-los em forma pictórica. 
    A visualização por imagem ajuda a expor padrões, correlações e tendências que não 
    podem ser obtidos quando os dados estão em uma tabela ou arquivo.

    A visualização de dados é um campo da Análise de Dados que lida com a representação 
    visual deles, plotando de forma gráfica e eficaz a comunicação da inferência dos dados.

    A visualização de dados é o processo de encontrar tendências e correlações entre os 
    dados. Desempenha um papel significativo na representação de pequenos, médios ou 
    grandes conjuntos de dados, representando-os por meio de imagens, sendo especialmente 
    útil em grandes conjuntos, nos quais é impossível visualizar todos os dados de forma 
    única, muito menos processá-los e compreendê-los manualmente.

    Em Python, para realizar a visualização de dados, podem ser usados vários pacotes, 
    como Matplotlib, Seaborn, Plotly etc. Cada biblioteca em Python oferece diferentes 
    recursos para criar gráficos informativos, personalizados e atraentes para apresentar 
    os dados de forma simples e eficaz.

    As principais bibliotecas usadas para visualização de dados são Matplotlib e Seaborn. 
    Essas bibliotecas têm módulos embutidos para traçar gráficos diferentes. Enquanto o 
    Matplotlib é usado para incorporar gráficos em aplicativos, o Seaborn é usado 
    principalmente para gráficos estatísticos.
"""

# Importante
'''
    É gerado o gráfico em formato de pizza com as suas configurações.
    Os rótulos externos apresentam o nome da região e a quantidade de estados por região. 
    Os rótulos internos apresentam a porcentagem de estados por região com suas cores 
    aleatórias e o espaçamento entre as divisões.
'''