# Estrutura de Dados Lineares

# Filas: uma estrutura de dados
"""
    A fila (queue) é uma estrutura de dados similar à pilha, que apresenta uma regra de acesso 
    aos dados identificada pela sigla Fifo – First In First Out –, a qual determina que o primeiro 
    elemento a entrar na fila será o primeiro a sair dela. Há, nessa estrutura, uma diferença 
    fundamental comparando-a com a pilha. Na pilha as inserções e remoções são feitas em um mesmo 
    ponto, denominado topo. Por outro lado, na fila há pontos diferentes para as operações de inserção 
    e de remoção.

    Considere, por exemplo, uma fila de banco. Nesse caso há dois pontos de movimentação na fila. 
    Um cliente que chega ao banco entra no final da fila, ao passo que o cliente que está mais 
    próximo ao caixa, ou seja, que chegou primeiro na fila, é o próximo a ser atendido e sairá 
    da fila. Dessa forma, os pontos de movimentação na fila serão denominados tail (calda), que 
    é o final da fila, onde os elementos serão inseridos, e head (cabeça), que marca o início da 
    fila, por onde os elementos serão removidos.

    A implementação de uma fila pode ser feita considerando um vetor. Nesse caso, precisamos de duas 
    variáveis adicionais para representar o início e o final da fila, ou head e tail, respectivamente. 
    Assim como ocorre com a pilha, essas variáveis serão úteis para armazenar os índices do vetor que 
    representam essas posições
"""

# Implementando uma fila com Python
"""
    Uma fila é uma estrutura de dados que segue o princípio FIFO (First-In, First-Out), onde o 
    primeiro elemento a ser inserido é o primeiro a ser removido. Você pode implementar uma fila 
    em Python usando uma lista. 
"""
# Criando uma classe chamada Fila.
class Fila:
    def __init__(self):
        self.items = []
    # Método para verificar se a fila está vazia.
    def vazia(self):
        return len(self.items) == 0
    # Método que adiciona (enfileira) o elemento ao final da fila.
    def enfileirar(self, item):
        self.items.append(item)
    # Método que remove (desenfileira) o primeiro elemento da fila.
    def desenfileirar(self):
        if not self.vazia():
            return self.items.pop(0)  # Remove o primeiro elemento (o mais antigo)
    # Método que retorna o primeiro elemento da fila (sem remover).
    def frente(self):
        if not self.vazia():
            return self.items[0]  # Retorna o primeiro elemento da fila
    # Método que retorna o tamanho da fila.
    def tamanho(self):
        return len(self.items)

# Exemplo de uso:

# Criando nosso objeto (instância) da classe Fila
minha_fila = Fila()
# Adicionando (enfileirando) o primeiro elemento.
minha_fila.enfileirar(1)
# Adiconando o segundo elemento.
minha_fila.enfileirar(2)
# Imprimindo o primeiro elemento da fila.
print(minha_fila.frente())  # Isso imprimirá 1
# Removendo o primeiro elemento da fila.
item = minha_fila.desenfileirar()  # Desenfileira o 1
# Imprime o elemento removido.
print(item)  # Isso imprimirá 1
