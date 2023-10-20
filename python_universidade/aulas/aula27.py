# Importa a função groupby do módulo itertools
from itertools import groupby

# Define uma lista de dicionários onde cada dicionário representa um aluno com nome e nota
alunos = [
    {'nome': 'Lucas', 'nota': 'A'},
    {'nome': 'Fernando', 'nota': 'D'},
    {'nome': 'Matilda', 'nota': 'A'},
    {'nome': 'Einstein', 'nota': 'B'},
    {'nome': 'Newton', 'nota': 'A'},
    {'nome': 'Da Vinci', 'nota': 'B'},
    {'nome': 'Galileu', 'nota': 'C'},
    {'nome': 'Darwin', 'nota': 'D'},
    {'nome': 'Carl', 'nota': 'A'},
    {'nome': 'Socrates', 'nota': 'C'},
    {'nome': 'Platão', 'nota': 'D'},
    {'nome': 'Aristoteles', 'nota': 'E'},
    {'nome': 'Confucio', 'nota': 'B'},
    {'nome': 'Salomão', 'nota': 'B'},
    {'nome': 'Tesla', 'nota': 'A'},
    {'nome': 'Napoleão', 'nota': 'E'},
    {'nome': 'Alexandre', 'nota': 'C'},
]

# Ordena a lista de alunos com base na nota de cada aluno
alunos_agrupados = sorted(alunos, key=lambda aluno: aluno['nota'])

# Usa a função groupby para agrupar os alunos com base na nota
grupos = groupby(alunos_agrupados, key=lambda aluno: aluno['nota'])

# Itera sobre os grupos formados pela função groupby
for chave, grupo in grupos:
    # Imprime a nota atual e indica que está listando os alunos com essa nota
    print(f'Alunos com nota {chave}:')
    
    # Itera sobre os alunos no grupo
    for aluno in grupo:
        # Imprime o nome do aluno
        print(aluno['nome'])
    
    # Adiciona uma linha em branco para separar os grupos de diferentes notas
    print()

# Info
"""
    O método groupby faz parte do módulo itertools em Python e é usado para agrupar 
    elementos de um iterável (por exemplo, uma lista) com base em um critério 
    especificado. Ele retorna um objeto de agrupamento que pode ser percorrido para 
    acessar os grupos de elementos com base no critério de agrupamento. 
"""
