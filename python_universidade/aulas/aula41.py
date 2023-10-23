# Estrutura de Dados

# Pilhas

# Criando uma classe chamada Pilha
class Pilha:
    def __init__(self):
        # Inicialização da pilha no estado vazio
        self.topo = -1  # Inicializa o topo da pilha como -1
        self.MAX = 30  # Tamanho máximo da pilha
        self.memo = [None] * self.MAX  # Cria uma matriz para armazenar os elementos da pilha

    def is_empty(self):
        # Verifica se a pilha está vazia
        return self.topo == -1

    def is_full(self):
        # Verifica se a pilha está cheia
        return self.topo == self.MAX - 1

    def push(self, x):
        # Insere um valor na pilha
        if not self.is_full():  # Verifica se a pilha não está cheia
            self.topo += 1  # Incrementa o topo
            self.memo[self.topo] = x  # Insere o elemento no topo
        else:
            print("Pilha Cheia!!")

    def print(self):
        # Exibe o conteúdo da pilha
        if not self.is_empty():  # Verifica se a pilha não está vazia
            msg = ", ".join(str(self.memo[i]) for i in range(self.topo + 1))  # Cria uma string com os elementos da pilha
            print(f"P: [ {msg} ]")  # Exibe a pilha formatada
        else:
            print("Pilha Vazia!!")

    def pop(self):
        # Remove e retorna o elemento no topo da pilha
        if not self.is_empty():  # Verifica se a pilha não está vazia
            top_element = self.memo[self.topo]  # Obtém o elemento no topo
            self.topo -= 1  # Decrementa o topo para remover o elemento
            return top_element
        else:
            return None  # Retorna None se a pilha estiver v

# Info
"""
    Uma pilha é uma estrutura de dados linear que segue o princípio de "last-in, first-out" (LIFO), o 
    que significa que o último elemento adicionado à pilha é o primeiro a ser removido. Vamos examinar 
    o código detalhadamente, linha por linha:

    A declaração public class Pilha { inicia a definição de uma classe chamada "Pilha". Classes são uma 
    forma de organizar código em orientação a objetos. O código relacionado à pilha será encapsulado 
    nesta classe.

    private int topo; declara uma variável de instância "topo" que representa o índice do topo da pilha. 
    Inicialmente, é definido como -1.

    private int MAX; declara uma variável de instância "MAX" que especifica o tamanho máximo da pilha. 
    Neste caso, o tamanho máximo é definido como 30.

    private Object memo[]; declara uma matriz de objetos "memo" que representa os elementos da pilha. Os 
    objetos em Java são usados como elementos da pilha.

    O construtor public Pilha() é chamado quando um objeto da classe é criado. Ele inicializa o estado 
    da pilha para vazia. O topo é definido como -1, o tamanho máximo é definido como 30, e a matriz de 
    objetos é criada com um tamanho máximo de 30.

    O método public boolean isEmpty() verifica se a pilha está vazia, retornando true se o topo for igual 
    a -1.

    private boolean isFull() é um método privado que verifica se a pilha está cheia, retornando true se o 
    topo for igual a MAX - 1.

    public void push(Object x) é um método para inserir um valor na pilha. Ele verifica se a pilha não está 
    cheia (usando isFull) e, se não estiver cheia, aumenta o topo e insere o elemento na posição correta da 
    matriz.

    Se a pilha estiver cheia, uma mensagem de erro é exibida.

    public void print() é um método para exibir o conteúdo da pilha. Ele verifica se a pilha não está 
    vazia (usando isEmpty) e, se não estiver vazia, itera pelos elementos da matriz e os imprime em uma 
    representação de string.

    Se a pilha estiver vazia, uma mensagem informando que a pilha está vazia é exibida.

    public Object pop() é um método que retorna o elemento no topo da pilha e o remove da pilha. Ele 
    verifica se a pilha não está vazia e, se não estiver vazia, retorna o elemento na posição do topo e 
    decrementa o topo.

    Se a pilha estiver vazia, ele retorna null.

    public Object top() é um método que retorna o elemento no topo da pilha sem removê-lo. Ele verifica 
    se a pilha não está vazia e, se não estiver vazia, retorna o elemento na posição do topo.

    Se a pilha estiver vazia, ele retorna null.

    Este código fornece uma implementação básica de uma pilha em Java, permitindo a adição de elementos, 
    a remoção do elemento no topo e a consulta do elemento no topo, além de verificar se a pilha está 
    vazia ou cheia. É uma estrutura de dados essencial usada em várias aplicações, como na avaliação de 
    expressões matemáticas, na reversão de texto e em muitos outros cenários onde o LIFO é útil.
"""