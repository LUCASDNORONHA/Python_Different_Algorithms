# MÉTODO FILTER

# Exemplo:

# Definindo uma função chamada 'filtro'.
def filtro(numero):
    # Retorna verdade se o número tiver resto igual a 0.
    return numero % 2 == 0

# Criando uma lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Aplicado a função o método 'filter' para e passo como parâmentros 
# a função 'filtro' (função filtro) e a lista 'numeros' (iteravel).
resultado = filter(filtro, numeros)

# Converte o objeto de filtro em uma lista.
lista_resultado = list(resultado)

# Imprime o resultado.
print(lista_resultado)
# Saída:
# [2, 4, 6, 8, 10]


# Info
"""
    O método filter é uma função integrada (built-in) em Python que é usada para 
    filtrar elementos de um iterável (por exemplo, uma lista, tupla ou sequência) 
    com base em uma função de teste, chamada de função de filtro. Ele cria um novo 
    iterável contendo apenas os elementos para os quais a função de filtro retorna True.

    função_de_filtro: A função que determina o critério de filtragem. Ela recebe um 
    elemento do iterável como argumento e deve retornar True para manter o elemento 
    no resultado ou False para excluí-lo.

    iterável: O iterável contendo os elementos que você deseja filtrar.

    O filter retorna um objeto de filtro (filter object), que é um iterável. Para obter 
    os resultados como uma lista ou outro tipo de sequência, você normalmente converte o 
    objeto de filtro em um tipo de sequência usando list(), tuple(), ou similiar.

    O filter é uma ferramenta útil para selecionar elementos com base em critérios 
    específicos de uma lista ou sequência, sem a necessidade de escrever loops explícitos. 
    Isso pode tornar seu código mais conciso e legível.

    Lembre-se de que a função de filtro deve retornar True para os elementos que você 
    deseja manter e False para os elementos que deseja descartar.
"""
