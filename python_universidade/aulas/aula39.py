# Estruturas de Dados lineares

# Filas Circulares: uma estrutura de dados
"""
    A fila circular é uma variação da implementação anterior e busca um aproveitamento melhor 
    das posições disponíveis na fila.

    Filas circulares, também conhecidas como filas de anel ou filas de buffer, são uma variação 
    de filas lineares em que os elementos são organizados em um anel, de forma que, quando a fila 
    está cheia e um novo elemento é inserido, ele substitui o elemento mais antigo. Esse 
    comportamento é diferente das filas lineares, em que a adição de um novo elemento quando a 
    fila está cheia resulta em um erro de estouro ou requer a remoção de um elemento existente.

    As filas circulares podem ser implementadas em várias linguagens de programação, incluindo 
    Python, e são uma ferramenta útil para lidar com situações em que os dados mais antigos são 
    menos relevantes e podem ser descartados quando a fila está cheia.
"""
# Criando uma classe chamada FilaCircular.
class FilaCircular:
    """
    Nesta implementação, a classe FilaCircular é criada com um tamanho máximo especificado. 
    A fila é representada como uma lista de tamanho fixo, onde os elementos são inseridos e 
    removidos em um ciclo. O índice de início e o índice de fim são controlados para indicar 
    onde a fila começa e termina. O operador % é usado para garantir que os índices permaneçam 
    dentro dos limites da lista, tornando-a circula.
    """
    # Método construtor que recebe os atributos.
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.fila = [None] * tamanho_maximo  # Inicializa a fila com None
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0
    # Método para verificar se a lista está vazia.
    def vazia(self):
        return self.tamanho == 0
    # Método para verificar se a lista está cheia.
    def cheia(self):
        return self.tamanho == self.tamanho_maximo
    # Método para adicionar (enfileirar) elementos na fila.
    """
    O método enfileirar é usado para adicionar um elemento ao final da fila. Ele verifica se a 
    fila não está cheia antes de inserir o elemento. O elemento é adicionado na posição fim, e o 
    índice fim é atualizado. Se o índice fim atingir o tamanho máximo, ele volta ao início da 
    fila usando a operação %. O tamanho da fila é incrementado.
    """
    def enfileirar(self, item):
        if not self.cheia():
            self.fila[self.fim] = item
            self.fim = (self.fim + 1) % self.tamanho_maximo
            self.tamanho += 1
    # Método desenfileirar (remover) elementos da fila.
    """
    O método desenfileirar remove e retorna o elemento no início da fila (o elemento mais antigo). 
    Ele verifica se a fila não está vazia antes de tentar remover um elemento. O elemento no índice 
    inicio é removido, o índice inicio é atualizado, e, se atingir o tamanho máximo, ele volta ao 
    início da fila usando %. O tamanho da fila é decrementado, e o elemento removido é retornado.
    """
    def desenfileirar(self):
        if not self.vazia():
            item = self.fila[self.inicio]
            self.fila[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.tamanho_maximo
            self.tamanho -= 1
            return item
    # Método que retorna o primeiro elemento da fila (sem remover).
    def frente(self):
        if not self.vazia():
            return self.fila[self.inicio]
    # Método que retorna o tamanho da fila.
    def tamanho_atual(self):
        return self.tamanho

# Exemplo de uso:
fila = FilaCircular(5)  # Cria uma fila circular com tamanho máximo de 5

# Enfileirando elementos
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
# Imprimindo a verificação se fila está cheia ou não.
print("Fila cheia:", fila.cheia())
# Desenfileria o elemento mais antigo da fila (o primeiro elemento da fila enfileirado dos valores contidos)
item = fila.desenfileirar()
# Retorna elemento removido.
print(f"Item desenfileirado: {item}")
# Enfileirando novo elemento
fila.enfileirar(6)
# Imprimindo tamanho atual da fila.
print("Tamanho atual da fila:", fila.tamanho_atual())
# Imprimindo o primeiro elemento da fila.
print("Frente da fila:", fila.frente())


# Atenção!
"""
    Considerar a implementação de uma fila circular pode retardar o transbordamento
    da fila (overflow), porém, esse evento fatalmente ocorrerá em algum momento. Isso
    ocorre pois estamos utilizando uma estrutura de dados com tamanho pré-definido,
    o que acarreta em uma alocação estática de memória. A alocação estática de memória, 
    no contexto de implementação, reserva um segmento de bytes contíguos na
    memória, o que facilita o acesso. Por outro lado, sempre haverá um tamanho limite
    para este tipo de estrutura.
"""