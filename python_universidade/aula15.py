# Importando Pandas
import pandas as pd

'''
    Vamos utilizar a base de dados do Instituto Brasileiro de Geografia e Estatística (IBGE)
    sobre regiões, estados e cidades brasileiros que estão disponíveis em arquivo .csv no 
    repositório do GitHub a seguir.
'''

# Endereço web dos arquivos, mas poderia ser local.
urlRegião = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/regioes.csv'
urlEstado = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/estados.csv'
urlCidade = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/municipios.csv'

# Importa a tabela de dados.
dfRegiao = pd.read_csv(urlRegião)
dfEstado = pd.read_csv(urlEstado)
dfCidade = pd.read_csv(urlCidade)

# Remove colunas do dataframe que não são relevantes para nossa análise.
del dfEstado['CodigoUf']
del dfCidade['Codigo']

# Renomeia as colunas no dataframe.
dfRegiao.rename(columns={'Id': 'IdRegiao', 'Nome': 'Regiao'}, inplace=True)
dfEstado.rename(columns={'Id': 'IdEstado', 'Regiao': 'IdRegiao', 'Nome': 'Estado', 'Uf': 'UF'}, inplace=True)
dfCidade.rename(columns={'Id': 'IdCidade', 'Nome': 'Cidade', 'Uf': 'UF'}, inplace=True)

# merge Região com Estado pela coluna IdRegiao.
df_innerRegiaoEstado = pd.merge(dfRegiao, dfEstado, on='IdRegiao', how='inner')
print('-'*40)
print(df_innerRegiaoEstado[['Estado', 'UF', 'Regiao']].head(5))

# merge Estado com Cidade pela coluna UF
df_innerEstadoCidade = pd.merge(dfCidade, dfEstado, on='UF', how='inner')
print('-'*40)
print(df_innerEstadoCidade[['Cidade', 'Estado', 'UF']].head(5))
print('-'*40)

# merge Estado com Cidade pela coluna UF - visualizar Cidade, Estado e Região.
df_innerEstadoCidade = df_innerEstadoCidade.drop(['Estado', 'IdRegiao', 'IdEstado'], axis=1)
df_innerRegiaoEstadoCidade = pd.merge(df_innerRegiaoEstado, df_innerEstadoCidade, on='UF', how='inner')
print(df_innerRegiaoEstadoCidade[['Cidade','Estado', 'UF', 'Regiao']].head(5))
print('-'*40)

# Retorna a dimensões do dataframe.
print('Dimensionalidade do DataFrame :\n',df_innerRegiaoEstadoCidade.shape)
print('-'*40)



# Info
"""
    Merge e Joins de DataFrames

    Os objetos Series e DataFrame da biblioteca Pandas são ferramentas poderosas 
    para explorar e analisar dados. Parte de seu poder vem de uma abordagem 
    multifacetada para combinar conjuntos de dados separados. Com o pacote Pandas, 
    pode-se mesclar, unir e concatenar os conjuntos de dados, permitindo unificar e 
    entender melhor os dados à medida que a análise é realizada.

    Para mesclar os dados com Pandas, é necessário fazer uso dos métodos:

    .merge(): para combinar dados em colunas ou índices comuns;

    .join(): para combinar dados em uma coluna de chave ou um índice;

    .concat(): para combinar DataFrames em linhas ou colunas (STRATIS, 2022).

    Quanto ao Merge(), o método é utilizado sempre que for necessário fazer uma 
    funcionalidade semelhante às operações de junção de um banco de dados relacional. 
    O método Merge() é útil quando é necessário combinar objetos de dados com base em 
    uma ou mais chaves, semelhantemente ao que seria necessário em um banco de dados 
    relacional (SIMPLILEARN, 2022). O Merge() é benéfico quando existe a necessidade de 
    combinar linhas que compartilham dados, sendo um método flexível por possuir muitos 
    parâmetros que podem ser utilizados para definir o comportamento na mesclagem, sendo 
    dois argumentos obrigatórios: o left DataFrame e o right DataFrame.

    Após esses parâmetros obrigatórios, ficam disponíveis vários argumentos opcionais para 
    definir os conjuntos de dados que serão mesclados.

    Alguns dos parâmetros mais importantes para passar para o método Merge() são:

    how: define qual tipo de mesclagem fazer. O padrão é inner, mas outras opções 
    possíveis incluem outer, left e right;

    on: informa em Merge() quais colunas ou índices, também chamados de colunas-chave 
    ou índices-chave, que se almeja ingressar, sendo opcional;

    left_on e right_on: especifica uma coluna ou índice que esteja presente apenas no 
    objeto left ou right que está mesclando. Ambos por padrão são None;

    left_index e right_index: ambos são padronizados para False, mas podem ser modificados 
    para usar o índice do objeto esquerdo ou direito a ser mesclado, definindo o argumento 
    como True;
    
    suffixes: é uma tupla de strings para anexar a nomes de colunas idênticos que não são 
    chaves de mesclagem. Isso permite o acompanhamento das origens das colunas com o mesmo 
    nome.

    Esses são alguns dos parâmetros mais importantes para usar com o Merge()
"""

# Importante
'''
Sobre a mesclagem: inner, outer, left e right são conhecidas também como operações de 
junções. Nesse contexto, pode-se considerar os termos merge e join como equivalentes.
'''