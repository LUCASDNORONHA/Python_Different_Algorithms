# Estruturas de Dados Lineares

# Listas Ligadas ou Listas Encadeadas: uma estrutura de dados
"""
    Uma lista ligada, ou encadeada, é uma estrutura de dados na qual os elementos são
    organizados linearmente. Nesse sentido, a linearidade dessa estrutura não é definida
    pela localização dos elementos na memória, como é o caso do vetor, mas sim por um
    ponteiro associado a cada um dos elementos, o qual define a posição do próximo.
"""
# Criando uma classe No
class No:
    """
    A classe No representa um nó individual na lista encadeada. Cada nó possui um valor e 
    uma referência para o próximo nó na lista.
    """
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# Criando uma classe ListaEncadeada.
class ListaEncadeada:
    """
    A classe ListaEncadeada é a estrutura principal que gerencia a lista. Ela mantém uma 
    referência para o primeiro nó na lista (ou None se estiver vazia).
    """
    def __init__(self):
        self.primeiro = None
    # Método que verifica se a lista está vazia.
    def esta_vazia(self):
        return self.primeiro is None
    # Método para adicionar elementos a lista.
    """
    Este método adiciona um novo nó com o valor fornecido ao final da lista. Se a lista estiver 
    vazia, o novo nó se torna o primeiro nó. Caso contrário, ele percorre a lista até o último nó 
    e o liga ao novo nó.
    """
    def adicionar(self, valor):
        novo_no = No(valor)
        if self.esta_vazia():
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
    # Método que remove elementos da lista.
    """
    Este método remove o nó com o valor fornecido da lista. Ele verifica se a lista está vazia e se 
    o primeiro nó contém o valor a ser removido. Caso contrário, ele percorre a lista até encontrar 
    o nó com o valor e o remove, ajustando as referências apropriadamente.
    """
    def remover(self, valor):
        if self.esta_vazia():
            return

        if self.primeiro.valor == valor:
            self.primeiro = self.primeiro.proximo
            return

        atual = self.primeiro
        while atual.proximo is not None:
            if atual.proximo.valor == valor:
                atual.proximo = atual.proximo.proximo
                return
            atual = atual.proximo
    # Método imprimir
    """
    Este método percorre a lista e imprime os valores dos nós, mostrando a estrutura da lista encadeada.
    """
    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

# Exemplo de uso:
minha_lista = ListaEncadeada()
minha_lista.adicionar(1)
minha_lista.adicionar(2)
minha_lista.adicionar(3)
minha_lista.imprimir()  # Isso imprimirá "1 -> 2 -> 3 -> None"

minha_lista.remover(2)
minha_lista.imprimir()  # Isso imprimirá "1 -> 3 -> None"

# Atenção!

"""
    Um vértice (nó) em uma lista ligada é uma estrutura na qual há o elemento da lista e o endereço 
    para o próximo vértice.

    Diferentemente de estruturas de dados como arrays ou listas em que os elementos estão armazenados 
    em locais contíguos na memória, em uma lista encadeada, os nós podem estar dispersos por toda a 
    memória, mas são conectados por meio de ponteiros.

    Aqui estão alguns conceitos e características importantes das listas encadeadas:

    Nó (Node): Cada elemento em uma lista encadeada é representado por um nó. Cada nó contém dois 
    campos: o valor do elemento (ou dados) e um ponteiro que aponta para o próximo nó na lista.

    Cabeça (Head): O primeiro nó em uma lista encadeada é chamado de cabeça (head). É a partir deste 
    nó que a travessia ou manipulação da lista começa.

    Nó Final (Tail): O último nó em uma lista encadeada pode ser chamado de nó final (tail). Ele é o 
    nó que não possui um ponteiro para o próximo elemento (geralmente aponta para None ou nulo).

    Elementos Encadeados: Os nós na lista são conectados por meio de ponteiros. O último nó aponta para 
    None, indicando o fim da lista.

    Vantagens:

    Tamanhos variáveis: Listas encadeadas podem crescer ou encolher dinamicamente, pois a alocação de 
    memória é feita conforme necessário. 
    Inserções e remoções eficientes: Inserir ou remover elementos  em uma lista encadeada é eficiente, 
    desde que você tenha acesso ao nó onde a operação ocorre.

    Desvantagens:

    Acesso aleatório ineficiente: Para acessar um elemento específico, você deve percorrer a lista a 
    partir do início.
    Uso de memória: Cada nó requer memória adicional para armazenar o ponteiro, o que pode tornar as 
    listas encadeadas menos eficientes em termos de uso de memória em comparação com arrays.
    
    Tipos de Listas Encadeadas:

    Simplesmente Encadeada (Singly Linked List): Cada nó tem um único ponteiro que aponta para o próximo 
    nó na lista.

    Duplamente Encadeada (Doubly Linked List): Cada nó tem dois ponteiros, um que aponta para o próximo 
    nó e outro que aponta para o nó anterior na lista.

    Circularmente Encadeada (Circular Linked List): A última referência em uma lista encadeada aponta de 
    volta para o primeiro nó, criando um ciclo.


    As listas encadeadas são amplamente utilizadas em algoritmos e estruturas de dados. Elas são 
    particularmente úteis quando a ordem de inserção ou a sequência dos elementos é importante e 
    quando você precisa de inserções ou remoções eficientes no início ou no meio da lista.
"""