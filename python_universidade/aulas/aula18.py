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
urlCidade = 'https://raw.githubusercontent.com/chandez/Estados-Cidades-IBGE/master/csv/municipios.csv'


# PERGUNTA:
# Qual a quantidade municipios por estado?

dfEstado = pd.read_csv(urlEstado)
dfCidade = pd.read_csv(urlCidade)

# Deletando colunas desnecessárias
del dfEstado['CodigoUf']
del dfCidade['Codigo']
# print(dfEstado,'\n'+'-'*40+'\n', dfCidade,'\n'+'-'*40)

dfEstado.rename(columns={
    'Id': 'IdEstado', 
    'Nome': 'Estado', 
    'Uf': 'UF', 
    'Regiao': 'IdRegiao'
    }, inplace=True
)
# print(dfEstado, '\n'+'-'*40)

dfCidade.rename(columns={
    'Id': 'IdCidade',
    'Nome': 'Cidade',
    'Uf': 'UF'
    }, inplace=True
)
# print(dfCidade, '\n'+'-'*40)

# Realizando a junção dos dataframes.
df_innerEstadoCidade = pd.merge(dfEstado, dfCidade, on='UF', how='inner')
# print(df_innerEstadoCidade)

# Método 1
# Contando a quantidade de municípios por estado
df_municipios_por_estado = df_innerEstadoCidade['UF'].value_counts()
print(df_municipios_por_estado)

# Método 2
# Contando o número de municípios por estado
municipios_por_estado = df_innerEstadoCidade.groupby('UF')['Cidade'].count()
# Exibindo o resultado
print(municipios_por_estado)

# Criando um gráfico de barras
municipios_por_estado.plot(kind='bar', figsize=(12, 6))
plt.title('Número de Municípios por Estado')
plt.xlabel('Estado (UF)')
plt.ylabel('Número de Municípios')
plt.xticks(rotation=0)  # Rotação dos rótulos do eixo x
plt.show()


# Atenção
'''
Os dois métodos apresentam resultados semelhantes, mas eles têm significados diferentes.

O primeiro método, utilizando value_counts(), conta a quantidade de ocorrências de cada 
código de estado (UF) na coluna 'UF'. O resultado será a quantidade de cidades
(ou registros no DataFrame) que possuem o mesmo código de estado. Isso não é o mesmo que 
contar o número de municípios por estado, pois uma cidade pode aparecer mais de uma vez 
se houver registros duplicados ou se ela estiver em diferentes regiões dentro do mesmo 
estado.

O segundo método, utilizando groupby() e count(), agrupa os dados pelo código de 
estado (UF) e, em seguida, conta quantas cidades (ou registros) existem em cada grupo. 
Isso representa de forma mais precisa o número de municípios por estado, porque ele 
considera cada cidade apenas uma vez, independentemente de quantas vezes ela esteja 
presente no DataFrame.

Portanto, a abordagem corrigida com groupby() e count() é a mais apropriada para contar 
número de municípios por estado, pois evita distorções devido a registros duplicados e 
fornece um resultado mais preciso.

'''