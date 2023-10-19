# Importando Pandas
import pandas as pd
# Inportando Matplolib
import matplotlib.pyplot as plt

# URLs dos arquivos CSV
urlRegiao = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/regioes.csv'
urlEstado = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/estados.csv'
urlCidade = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/municipios.csv'

# PERGUNTAS:
# Qual a quantidade de municípios por região?
# Qual a porcentagem de municípios por região?

# Carregando os DataFrames
dfRegiao = pd.read_csv(urlRegiao)
dfEstado = pd.read_csv(urlEstado)
dfCidade = pd.read_csv(urlCidade)

# Deletando colunas desnecessárias
del dfEstado['CodigoUf']
del dfCidade['Codigo']

# Renomeando colunas
dfRegiao.rename(columns={
    'Id': 'IdRegiao', 
    'Nome': 'Regiao'
    }, inplace=True
)
dfEstado.rename(columns={
    'Id': 'IdEstado',
    'Nome': 'Estado',
    'Uf': 'UF',
    'Regiao': 'IdRegiao'
}, inplace=True
)
dfCidade.rename(columns={
    'Id': 'IdCidade',
    'Nome': 'Cidade',
    'Uf': 'UF'
}, inplace=True
)

# Realizando junções
df_innerEstadoCidade = pd.merge(dfEstado, dfCidade, on='UF', how='inner')
df_innerRegiaoEstadoCidade = pd.merge(df_innerEstadoCidade, dfRegiao, on='IdRegiao', how='inner')
# print(df_innerRegiaoEstadoCidade)

# Contando a quantidade de municípios por região
municipios_por_regiao = df_innerRegiaoEstadoCidade['Regiao'].value_counts()
# print(municipios_por_regiao)

# Criando um gráfico de barras
municipios_por_regiao.plot(kind='bar', figsize=(12, 6))
plt.title('Número de Municípios por Região')
plt.xlabel('Região')
plt.ylabel('Número de Municípios')
plt.xticks(rotation=0)
plt.show()

# Criando um gráfico de setores (pizza) com as porcentagens
plt.figure(figsize=(8, 8))
plt.pie(municipios_por_regiao, labels=municipios_por_regiao.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Para garantir que o gráfico seja um círculo.
plt.title('Porcentagem de Municípios por Região')
plt.show()

