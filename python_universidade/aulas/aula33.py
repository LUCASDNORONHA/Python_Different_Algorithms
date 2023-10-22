# Importando módulo 'json'.
import json

# Criando um dicionário.
meu_dicionario = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "profissão": "Engenheiro",
    "interesses": ["Programação", "Música", "Esportes"],
    "contato": {
        "email": "joao@email.com",
        "telefone": "123-456-7890"
    },
    "experiencia_profissional": [
        {
            "cargo": "Desenvolvedor Python",
            "empresa": "ABC Tech",
            "ano_inicio": 2015,
            "ano_fim": 2020
        },
        {
            "cargo": "Engenheiro de Software",
            "empresa": "XYZ Software",
            "ano_inicio": 2020,
            "ano_fim": 2023
        }
    ]
}

# Salvando meu dicionário como arquivo .json
with open ('C:\\Users\\lucas\\diretorio_python\\python_universidade\\arquivos_gerados\\aula33_salvando_dic.json', 'w') as arquivo:
    json.dump(meu_dicionario, arquivo)

# Criando uma lista.
minha_lista = [' Maçã', 'Laranja', 'Goiaba', 'Uva', 'Limão', 'Abacaxi', 'Melancia']

# Salvando minha lista como arquivo .json
with open ('C:\\Users\\lucas\\diretorio_python\\python_universidade\\arquivos_gerados\\aula33_salvando_lis.json', 'w') as arquivo:
    json.dump(minha_lista, arquivo)



# Info
"""
    Arquivos JSON (JavaScript Object Notation) são um formato de intercâmbio de dados 
    leves e legíveis por humanos. Eles são amplamente utilizados para representar 
    estruturas de dados simples e complexas em formato de texto. Em Python, o módulo 
    json é usado para trabalhar com arquivos JSON. Aqui estão algumas informações sobre 
    arquivos JSON e sua utilização em Python:

    Estrutura do JSON: O JSON é uma coleção de pares chave-valor, semelhante aos 
    dicionários em Python. Ele pode conter tipos de dados primitivos, como números, 
    strings, booleanos, arrays e objetos (que se mapeiam diretamente para dicionários em 
    Python).

    Leitura de Arquivos JSON em Python: O módulo json em Python permite que você leia 
    dados de um arquivo JSON e converta-os em estruturas de dados Python. Isso é feito 
    com a função json.load().

    Escrita de Arquivos JSON em Python: Você pode criar um arquivo JSON a partir de uma 
    estrutura de dados Python usando a função json.dump().

    Manipulação de Dados: Após carregar um arquivo JSON, você pode manipular os dados da 
    mesma forma que faria com dicionários Python. O JSON é uma representação independente 
    da linguagem, então você pode facilmente compartilhar dados entre diferentes linguagens.

    Validação de JSON: O módulo json também permite validar JSON para garantir que ele 
    esteja bem formado. Use json.loads() para validar e carregar JSON em uma estrutura de 
    dados Python. Se houver erros no JSON, ele lançará uma exceção json.JSONDecodeError.

    Formatação: O módulo json em Python permite definir a formatação dos arquivos JSON, 
    incluindo a possibilidade de indentação para melhor legibilidade. Você pode usar o 
    argumento indent ao salvar arquivos JSON.

    Uso Comum: Os arquivos JSON são frequentemente usados para configurar aplicativos, 
    compartilhar dados na web, trocar informações entre sistemas e armazenar dados 
    estruturados de maneira simples e eficaz.

    Limitações do JSON: O JSON tem algumas limitações, como a falta de suporte para 
    tipos de dados personalizados, data e hora, comentários e referências circulares. 
    Para casos mais complexos, outros formatos, como o YAML ou o XML, podem ser mais 
    adequados.

    O JSON é amplamente utilizado na programação Python e é uma parte essencial da 
    interoperabilidade de dados, especialmente em aplicações web, onde muitas APIs 
    retornam dados em formato JSON.

"""