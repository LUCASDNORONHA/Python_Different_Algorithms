import pandas as pd

# Fonte dos dados
urlRegiao = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/regioes.csv'
urlEstado = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/estados.csv'
urlCidade = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/municipios.csv'

# Lendo os DataFrames
dfRegiao = pd.read_csv(urlRegiao)
dfEstado = pd.read_csv(urlEstado)
dfCidade = pd.read_csv(urlCidade)

# Renomeando colunas para facilitar a análise
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
