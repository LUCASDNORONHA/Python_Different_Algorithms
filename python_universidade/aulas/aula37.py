# Estruturas de Dados Lineares

# Pilhas: uma estrutura de dados
"""
    A pilha (stack) é uma estrutura de dados que considera duas operações básicas; empilhar (push) 
    e desempilhar (pop) elementos. Essa estrutura considera uma regra específica de acesso aos dados, 
    na qual as operações serão realizadas no topo da pilha. Essa regra de acesso é 
    denominada Lifo (Last In First Out), que é a sigla, em inglês, para definir que o último que 
    chega é o primeiro que sai. O funcionamento da pilha pode ser melhor compreendido com a utilização 
    de uma analogia: quando lavamos pratos, podemos ensaboá-los e empilhá-los um a um enquanto não 
    chegamos ao último prato. Após finalizar essa etapa, vamos enxaguá-los começando, naturalmente, 
    pelo último prato até que finalizamos com o primeiro. Note que, o último prato a entrar na pilha 
    foi o primeiro a sair. 
    
    A implementação de uma pilha pode ser feita considerando um vetor. Nesse caso,
    há o problema do tamanho fixo do vetor, visto que essa estrutura deve ter o espaço de memória no 
    computador previamente alocado para o seu armazenamento. Adicionalmente, utilizamos uma variável que 
    servirá como um apontador (ponteiro) para uma posição da pilha, mais especificamente o topo da pilha.
"""

# Implementação de uma pilha com Python.
"""
    Você pode implementar uma pilha em Python usando uma lista e as operações append() para 
    empilhar (inserir) elementos e pop() para desempilhar (remover) elementos. 
"""
# Criando uma classe chamada Pilha.
class Pilha:
    def __init__(self):
        self.items = []
    # Método que verifica se a lista está vazia.
    def vazia(self):
        return len(self.items) == 0
    # Método que empilha novos elementos na pilha.
    def empilhar(self, item):
        self.items.append(item)
    # Método que desempilha o último elemento que entrou na pilha.
    def desempilhar(self):
        if not self.vazia():
            return self.items.pop()
        else:
            return None  # Pilha vazia
    # Retorna o último elemento do topo da lista (sem remover).
    def topo(self):
        if not self.vazia():
            return self.items[-1]
        else:
            return None  # Pilha vazia
    # Método que retorna o tamanho da pilha.
    def tamanho(self):
        return len(self.items)

# Exemplo de uso:

# Criando o objeto da nossa classe pilha.
minha_pilha = Pilha()
# Empilhando o primeiro elemento.
minha_pilha.empilhar(1)
# Empilhando o segundo elemento.
minha_pilha.empilhar(2)
# Empilhando o terceiro elemento.
minha_pilha.empilhar(3)
# Imprimindo a pilha.
print("Pilha após empilhar 1, 2 e 3:", minha_pilha.items)
# Imprimindo o topo da pilha (último elemento)
print("Topo da pilha:", minha_pilha.topo())
# Removendo (desempilhando) o último elemento da pilha.
item_removido = minha_pilha.desempilhar()
# Imprimindo o elemento removido.
print(f"Item removido da pilha: {item_removido}")
# Imprimindo a pilha após desempilhar o úlimo elemento.
print("Pilha após desempilhar:", minha_pilha.items)
