# Estruturas de dados Lineares

# Vetores: Uma estrutura de dados básicas
"""
    O vetor (ou array) é um conjunto finito e ordenado de elementos homogêneos. Nesse sentido, essa 
    estrutura apresenta um tamanho pré-definido, onde seus elementos estão em posições específicas e 
    são todos do mesmo tipo. Outra característica importante é que o vetor ocupa uma porção contígua 
    de memória física e pode ser acessado de maneira aleatória.
"""

# Vetor
"""
    Nesse sentido, considere o seguinte código, no qual há declaração de um vetor de 
    inteiros denominado vetor, a criação de um objeto (instanciação) com 10 posições e a inserção 
    de valores de 1 a 10 em cada uma das posiç
"""
# Criando um vetor de inteiros com 10 posições
vetor = [0] * 10

# Inserindo valores de 1 a 10 nas posições do vetor
for i in range(10):
    vetor[i] = i + 1

# Imprimindo o vetor
print(vetor)


# Função de busca em um vetor.
"""
    A manipulação de dados, organizados em uma estrutura específica, caracteriza as operações sobre 
    a estrutura. Para o caso do vetor, definiremos três operações; busca, remoção e inserção. A 
    operação de busca consiste de dado um vetor v e um valor x , ambos inteiros, encontrar um 
    índice k , tal que v[k] = x . A função que implementa a busca em um vetor retorna k caso o 
    valor buscado esteja presente no vetor e -1 caso contrário. 
"""
def busca_em_vetor(v, x):
    """
    A função busca percorre as posições do vetor, a partir da posição k = 0 , comparando o valor 
    a ser encontrado com os valores armazenados no vetor. Caso esse dois valores sejam iguais, a 
    função retorna o índice k que indica a posição do valor no vetor. Caso a função percorra o 
    vetor até sua última posição e não encontre correspondência com o valor buscado, a função 
    retorna -1.
    """
    for k in range(len(v)):
        if v[k] == x:
            return k  # Valor encontrado, retorna o índice
    return -1  # Valor não encontrado, retorna -1

# Valor de busca.
valor_procurado = 5

# Armazrnando resultado
indice_encontrado = busca_em_vetor(vetor, valor_procurado)

# Imprimindo
if indice_encontrado != -1:
    print(f"O valor {valor_procurado} foi encontrado na posição {indice_encontrado}.")
else:
    print(f"O valor {valor_procurado} não foi encontrado no vetor.")


# Função de remoção de valor em vetor.
"""
    Uma função remove, recebe o índice do valor a ser removido( k ), um valor inteiro que 
    representa o tamanho do vetor ( n ) e o próprio vetor ( v ). O valor a ser removido é 
    armazenado na variável x , a qual será retornada, posteriormente, pela função. Um laço 
    for percorre o vetor a partir do índice consecutivo àquele removido e desloca todos os 
    valores uma posição à esquerda, de modo a não deixar uma lacuna na posição do valor removido.
"""
def remove_do_vetor(indice, tamanho, vetor):
    """
    A função remove_do_vetor recebe o índice, o tamanho e o vetor como argumentos. Ela verifica se 
    o índice está dentro dos limites do vetor e, se estiver, remove o elemento no índice, deslocando 
    todos os elementos à esquerda. A função retorna o valor removido.
    """
    if indice < 0 or indice >= tamanho:
        # Verifica se o índice está dentro dos limites do vetor
        return None  # Retorna None para indicar um erro
    
    valor_removido = vetor[indice]  # Armazena o valor que será removido

    for i in range(indice, tamanho - 1):
        # Desloca os elementos à esquerda para preencher o espaço
        vetor[i] = vetor[i + 1]

    # Reduz o tamanho do vetor após a remoção
    tamanho -= 1

    return valor_removido

# Exemplo de uso:
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tamanho = len(vetor)
indice_a_remover = 3

valor_removido = remove_do_vetor(indice_a_remover, tamanho, vetor)

# Imprimindo
if valor_removido is not None:
    print(f"Valor removido: {valor_removido}")
    print(f"Vetor após a remoção: {vetor[:tamanho - 1]}")  # Exclui o último elemento do vetor
else:
    print("Índice fora dos limites do vetor")

# Atenção!
"""
    Em Python, a posição no vetor não é preenchida automaticamente após a remoção de um elemento. 
    Em vez disso, os elementos subsequentes são deslocados para a esquerda para preencher o espaço 
    deixado pelo elemento removido.

    Em Java, por exemplo, a manipulação de vetores (ou arrays) é um pouco diferente em relação a 
    listas dinâmicas, como as listas em Python. Em Java, quando você remove um elemento de um array, 
    a posição desse elemento não fica automaticamente vazia, e você precisará ajustar manualmente o 
    tamanho do array para refletir a remoção. Este é motivo pelo qual Java é uma linguagem muito utilizada
    para explicar as estruturas de dados e seus compotamentos.

    Em Python, quando você remove um elemento de uma lista, o espaço que estava ocupado por esse 
    elemento não é deixado vazio; ele é, na verdade, preenchido com uma referência nula ou "None". 
    Os elementos subsequentes são deslocados para a esquerda, e o último elemento, que agora é 
    redundante, é descartado. O tamanho da lista permanece o mesmo, e os elementos subsequentes 
    são deslocados para preencher o espaço vago.

    É importante notar que a presença de elementos None pode ser um indício de que um elemento 
    foi removido, mas esse espaço não é automaticamente liberado da memória. Se você deseja remover 
    elementos e compactar a lista para liberar espaço, é possível criar uma nova lista sem os 
    elementos indesejados e atribuí-la à variável original, ou você pode usar estruturas de dados 
    específicas para esse propósito, como um deque da biblioteca collections.

"""

# Função para inserir valores em um índice especifico do vetor
"""
    Suponha que queremos inserir um novo valor inteiro x em um vetor v [0...n-1] entre os 
    índices k −1 e k . A operação de inserção deve ser precedida de uma verificação sobre a 
    quantidade de elementos armazenados no vetor, ou seja, se o vetor estiver cheio não é 
    possível inserir nenhum elemento, caso contrário teremos um transbordamento (overflow). 
    Por exemplo, inseriremos o valor x = -8 no vetor v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,  ,  ], 
    entre as posições k = 5 e k = 6 , nesse sentido, o vetor resultante será 
    v = [1, 2, 3, 4, 5, 6, -8, 7, 8, 9, 10,  ]. Note que o vetor apresenta 12 posições, sendo 
    que as duas últimas posições estão vazias, esta condição é imprescindível para a inserção 
    de um novo elemento no vetor.
"""
def inserir_no_vetor(vetor, tamanho, valor, k):
    if tamanho >= len(vetor):
        print("Transbordamento (overflow): o vetor está cheio e não é possível inserir mais elementos.")
        return

    if k < 0 or k > tamanho:
        print("Índice inválido para a inserção.")
        return

    for i in range(tamanho, k, -1):
        vetor[i] = vetor[i - 1]

    vetor[k] = valor

    return tamanho + 1

# Exemplo de uso:
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None]  # Duas últimas posições vazias
tamanho_atual = 10  # Tamanho atual do vetor
valor_a_inserir = -8
indice_a_inserir = 6

novo_tamanho = inserir_no_vetor(vetor, tamanho_atual, valor_a_inserir, indice_a_inserir)

# Imprindo
if novo_tamanho is not None:
    print(f"Vetor após a inserção: {vetor}")
    print(f"Novo tamanho do vetor: {novo_tamanho}")
else:
    print("Não foi possível realizar a inserção.")
# Saída:
# [1, 2, 3, 4, 5, 6, -8, 7, 8, 9, 10, None]

