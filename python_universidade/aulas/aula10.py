# Para ler arquivo Excel no formato XLSX é preciso instalar a biblioteca 'openpyxl' pelo terminal
# Comando pip install openpyxl

# Importando o Pacote Pandas
import pandas as pd

# Endereços local do arquivo, nome do arquivo e extensão.
Notas = r"C:\Users\lucas\VScode\Python\Python_university\Notas.xlsx" #

df = pd.read_excel(Notas) # Criando um objeto que contém o dataframe

# Apresentando o conteúdo contido no DataFrame
# print(df) # Retorna o DataFrame
# print(df.head(3)) # Retorna as 3 primeira linhas do DataFrame
# print(df.tail(3)) # Retorna as 3 últimas linhas do DataFrame
# print(df.info()) # Retorna um resumo das informações contida no DataFrame
# print(df.isnull().sum()) # Retorna o somatório dos valores nulos.

df.fillna({'P1':0, 'P3':0}, inplace = True) # Substituindo os valores NaN por 0. 

df['Média'] = 0 # Criando nova coluna chamada Média com valor padrão 0.

'''

    Observação:

    Uma função lambda para calcular a média das notas das colunas P1, P2 e P3 do DataFrame df.
    Esta função lambda, chamada de md, aceita um único argumento n. 
    No contexto do Pandas, n representa uma linha (uma única entrada de dados) do DataFrame df.

    Criando uma nova coluna no DataFrame chamada 'Média' e atribuindo a essa coluna o resultado 
    da função lambda md aplicada a cada linha do DataFrame df. Isso efetivamente calcula a média 
    das notas para cada linha e a atribui à nova coluna 'Média' do DataFrame.

    Depois de calcular a média, arredonda os valores para 2 casas decimais usando df.Média.round(decimals=2).

    O resultado é que o DataFrame agora tem uma coluna adicional chamada 'Média' que contém a média das notas calculadas
    com base nas colunas P1, P2 e P3. Isso é como a função lambda está sendo aplicada ao DataFrame para calcular as médias.

'''
# Adiciona a coluna com a média de cada aluno.
md = lambda n: (n.P1 + n.P2 + n.P3)/3 # Função para calcular a média utilizando a função lambda.

df['Média'] = md(df)
df['Média'] = df.Média.round(decimals = 2)

# print(df)

'''
    Após adicionar a coluna de médias, pode-se responder quais alunos estão aprovados, quais precisarão de exames e quais 
    reprovados. Nesse contexto, é necessário adicionar uma nova coluna para verificar qual é o status de cada aluno.
'''

# Método para calcular Status.
def df_StatusFinal():
    return lambda n: 'R p Falta' if n.Faltas > 7 \
    else ('Reprovado' if n.Média < 4 else ('Aprovado' if n.Média >= 7 else 'Exame'))

# Adiciona a coluna com o Status.
df['Status'] = df.apply(func = df_StatusFinal(), axis = 1)

# print(df)

'''
Fatiamento

O DataFrame do Pandas é uma estrutura de dados rotulada bidimensional, que contém as funções “loc” e “iloc”. 
Essas funções são utilizadas para acessar linhas e/ou colunas, onde:

“loc” é para acessar por rótulos;

“iloc” é para acessar por posição, ou seja, índices numéricos.

'''
# Usando o método .loc para acessar as linhas a partir de 3 a 5.
# Das colunas mencionadas dentro dos colchete.
# print(df.loc[3:5, ['Alunos', 'Cursos', 'P1', 'P2', 'P3', 'Faltas', 'Média', 'Status']])

# Acessando informações pelo valor "R p Falta" da coluna 'Status'.
# Também posso mencionar os nomes das outras colunas que quero que apareça as informações.
# print(df.loc[
#    (df['Status'] == 'R p Falta'),
#   ['Alunos', 'Cursos', 'P1', 'P2', 'P3', 'Faltas', 'Média', 'Status']
# ])

# del df['Cursos'] # Para excluir uma coluna do DataFrame

# Renomeando a coluna Status por Status_Final
df.rename(
    columns={
        "Status": "Status_Final"
        }, inplace=True
)

# Renomenado as colunas P1, P2 e P3.
df.rename(
    columns={
        'P1': 'Prova_1',
        'P2': 'Prova_2',
        'P3': 'Prova_3',
    }, inplace=True
)

# Print(df)

# Convertendo os nomes das colunas por letras maísculas.
df.rename(columns=str.upper, inplace=True) 

# print(df)

# Salvando o arquivo depois da manipulação do dados.
df.to_excel('output_notasfinais1.xlsx', sheet_name='Notas')