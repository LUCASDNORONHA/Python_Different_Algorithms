import pandas as pd

df = pd.DataFrame({
    'Coluna A' : ['a', 'b', 'c', 'd','a'],
    'Coluna B' : ['Um', 'Dois', 'Três', 'Quatro', 'Cinco']
})

print(df)

'''
Para a leitura de arquivos, a biblioteca Pandas oferece vários métodos de leitura
de dados com diferentes formatos: .xlsx, .json, .csv, .txt, entre outros. 
Os métodos geralmente iniciam com a palavra “read”, seguida da extensão do arquivo,
exemplos:

read_excel();

read_csv();

read_xml();

read_json();

read_sql();

entre outros
'''