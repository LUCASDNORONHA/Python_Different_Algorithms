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


# PERGUNTA:
# Qual é a quantidade de municípios por região e a sua porcentagem?

'''
O data frame região e cidade não possuem colunas em comum para fazer a mesclagem das
colunas. Para resolver isso, irei usar o data frame estado, que possui colunas em comum
com os dois data frame, para que assim eu possa resolvar a pergunta.
'''

# Lendo os datas frames.
dfRegiao = pd.read_csv(urlRegião)
dfEstado = pd.read_csv(urlEstado)
dfCidade = pd.read_csv(urlCidade)

# Imprimindo os datas frames.
# print(dfRegiao,'\n'+'-'*20+'\n', dfEstado, '\n'+'-'*20+'\n', dfCidade, '\n'+'-'*20+'\n')

# Deletando colunas desnecessárias para nossa análise.
del dfEstado['CodigoUf']
del dfCidade['Codigo']

# Renomeando as colunas para uma melhor análise e mesclagem.
dfRegiao.rename(columns={'Id': 'IdRegiao', 'Nome': 'Regiao'}, inplace=True)
dfEstado.rename(columns={'Id': 'IdEstado', 'Nome': 'Estado', 'Uf': 'UF', 'Regiao': 'IdRegiao'}, inplace=True)
dfCidade.rename(columns={'Id': 'IdCidade', 'Nome': 'Cidade', 'Uf': 'UF'}, inplace=True)

# Criando um dicionário que relaciona UF a Região
uf_regiao_dict = dfEstado.set_index('UF')['Regiao'].to_dict()

# Adicionando a coluna 'Regiao' ao DataFrame dfCidade com base no dicionário
dfCidade['Regiao'] = dfCidade['UF'].map(uf_regiao_dict)

# Contando a quantidade de municípios por região
municipios_por_regiao = dfCidade['Regiao'].value_counts().reset_index()
municipios_por_regiao.columns = ['Regiao', 'Qtde']

# Cálculo da porcentagem
total_municipios = municipios_por_regiao['Qtde'].sum()
municipios_por_regiao['Porcentagem'] = (municipios_por_regiao['Qtde'] / total_municipios) * 100

# Exibindo o resultado
print(municipios_por_regiao)