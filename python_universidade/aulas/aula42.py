# Estrutura de Dados

# Pilha Dinâmica

# Criando uma classe chamada Node.
class Node:
    def __init__(self, dado=None):
        # Inicialização de um nó da lista encadeada com dado (opcional) e próxima referência (None)
        self.dado = dado  # Dado a ser armazenado no nó
        self.prox = None  # Referência para o próximo nó

    # Método para obter o conteúdo do nó
    def get_dado(self):
        return self.dado

    # Método para atribuir um valor ao conteúdo do nó
    def set_dado(self, novo_valor):
        self.dado = novo_valor

    # Método para obter a referência do próximo nó
    def get_prox(self):
        return self.prox

    # Método para atribuir uma referência para o próximo nó
    def set_prox(self, novo_prox):
        self.prox = novo_prox
# Info
"""
    Aqui está uma explicação do código:

    A classe Node representa um nó em uma lista encadeada. Cada nó contém um dado 
    (armazenado na variável dado) e uma referência para o próximo nó na lista 
    (armazenada na variável prox).

    O construtor __init__ é chamado quando um novo objeto Node é criado. Ele permite que 
    você inicialize um nó com um dado opcional. Se nenhum dado for fornecido, o nó será criado 
    com dado definido como None e prox definido como None.

    get_dado é um método que retorna o conteúdo do nó.

    set_dado é um método que permite atribuir um novo valor ao conteúdo do nó.

    get_prox é um método que retorna a referência para o próximo nó na lista.

    set_prox é um método que permite atribuir uma nova referência para o próximo nó na lista.

    Essa classe Node é uma parte fundamental na construção de uma lista encadeada, que é uma 
    estrutura de dados linear na qual os elementos são armazenados em nós que estão ligados uns 
    aos outros por meio de referências. Cada nó contém um dado e uma referência para o próximo nó 
    na sequência, permitindo a criação de estruturas de dados flexíveis para armazenar e manipular 
    informações.
"""

# Criando uma classe chamada Node
class Node:
    def __init__(self, dado=None):
        self.dado = dado
        self.prox = None

class PilhaDin:
    def __init__(self):
        self.topo = None  # Inicializa o topo como nulo (sem nós)

    def is_empty(self):
        # Verifica se a pilha está vazia
        return self.topo is None

    def push(self, x):
        novo = Node()  # Cria um novo nó
        novo.set_dado(x)  # Define o valor no novo nó
        novo.set_prox(self.topo)  # Configura o próximo do novo nó como o topo atual
        self.topo = novo  # Atualiza o topo para ser o novo nó

    def top(self):
        if not self.is_empty():
            return self.topo.get_dado()  # Retorna o dado no topo
        else:
            return None

    def pop(self):
        if not self.is_empty():
            resp = self.topo.get_dado()  # Captura o dado no topo
            self.topo = self.topo.get_prox()  # Atualiza o topo para ser o próximo nó
            return resp  # Retorna o dado capturado
        else:
            return None

    def print(self):
        if not self.is_empty():
            resp = ""
            aux = self.topo
            while aux is not None:
                resp = ", " + str(aux.get_dado()) + resp
                aux = aux.get_prox()
            print("P:[ " + resp + " ]")
        else:
            print("Pilha Vazia!")

# Exemplo de uso:
pilha = PilhaDin()
pilha.push(1)
pilha.push(2)
pilha.push(3)

print("Topo da pilha:", pilha.top())  # Deve imprimir: Topo da pilha: 3

print("Elemento removido:", pilha.pop())  # Deve imprimir: Elemento removido: 3

pilha.print()  # Deve imprimir: P:[ 2, 1 ]
