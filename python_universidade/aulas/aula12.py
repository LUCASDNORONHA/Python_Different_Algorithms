'''

    Descritores Estatísticos

    O campo da estatística coleta, apresenta, analisa e utiliza os dados para tomar
    decisões, resolver problemas e planejar e otimizar processos. Os modelos estatísticos 
    são utilizados para estudar a variedade, porque sucessivas observações de um sistema
    ou fenômeno não produzem o mesmo resultado.
'''

# Importar a bibliteca Pandas.
import pandas as pd

Notas = r"C:\Users\lucas\VScode\Python\Python_university\Notas.xlsx" # caminho do arquivo

df = pd.read_excel(Notas) # Ler o arquivo e cria um objeto dataframe chamado df.

print(df.head(15)) # Retorna as primeiras 15 linhas.
print('- '*30) # Multiplica o sinal 30 vezes para fazer uma linha tracejada.

print(df.describe()) # Retorna uma descrição estatística.


'''
Após a geração do DataFrame por meio de criação manual ou importação dos dados, para 
exibir todos os nomes das colunas e o tipo de dados é utilizada a instrução em Python:

dataframe.info()

Para obter o cálculo de determinada coluna do DataFrame, pode-se fazer uso das seguintes 
sintaxes para:

Soma: dataframe[‘coluna’].sum();

Média: dataframe[‘coluna’].mean();

Desvio-padrão: dataframe[‘coluna’].std();

Variância: dataframe[‘coluna’].var();

Mínimo: dataframe[‘coluna’].min();

Máximo: dataframe[‘coluna’].max();

Estatísticas descritivas: dataframe[‘coluna’].describe() para obter as estatísticas 
descritivas de uma coluna específica do DataFrame.

Para resumir os dados presentes no quadro de dados de todo o DataFrame, pode ser 
utilizado o método describe(). Esse método é usado para visualizar alguns resultados 
estatísticos – como percentil, média, padrão, mínimo, máximo, soma e contagem etc. – do 
quadro de dados junto com os tipos de dados dessa coluna específica, gerando uma 
estatística descritiva dos dados.
'''

