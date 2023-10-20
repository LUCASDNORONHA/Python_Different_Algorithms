# Programação Orientada a Objetos (POO)

# Classes

# Definindo uma classe chamada 'Pessoa'.

class Pessoa:
    # Método construtor que inicializa os atributos da classe
    def __init__(self, nome, idade):
        self.nome = nome # Atributo 'nome'.
        self.idade = idade # Atributo 'idade'.

    # Método para exibir informações sobre a pessoa.
    def apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos.')

# Criando uma instância (objeto) da classe 'Pessoa'.
pessoa1 = Pessoa('Lucas', 25)

# Acessando atributos.
print(f'Nome : {pessoa1.nome}')
print(f'Idade : {pessoa1.idade}')

# Acessando método 'apresentar()' da classe pessoa pelo objeto objeto instaciado.
pessoa1.apresentar()


# Informações sobre Classes.
"""
    Uma classe é um conceito fundamental na programação orientada a objetos (POO), que é 
    um paradigma de programação amplamente utilizado em muitas linguagens, incluindo 
    Python, Java, C++, e muitas outras. 

    Uma classe é uma estrutura que representa um modelo ou um plano para criar objetos. 
    Ela define as características (atributos) e o comportamento (métodos) que os objetos 
    criados a partir dessa classe terão. Em outras palavras, uma classe é um projeto ou 
    uma descrição para criar objetos que compartilham as mesmas propriedades e 
    funcionalidades.

    Aqui estão alguns conceitos-chave relacionados a classes:

    1. **Objeto:** Um objeto é uma instância de uma classe. Ele é uma entidade concreta 
    criada com base no modelo definido pela classe. Os objetos têm atributos (dados) e 
    métodos (ações) que são especificados pela classe.

    2. **Atributos:** Os atributos são variáveis que representam características do objeto. 
    Por exemplo, se você tiver uma classe "Carro", os atributos podem incluir "cor",
    "modelo" e "ano de fabricação".

    3. **Métodos:** Os métodos são funções definidas na classe que descrevem o 
    comportamento do objeto. Por exemplo, uma classe "Carro" pode ter métodos como
    "ligar", "desligar" e "acelerar".

    4. **Encapsulamento:** A POO promove o encapsulamento, que é o princípio de que os 
    detalhes internos de uma classe devem ser ocultos dos usuários. Isso é alcançado por 
    meio do uso de modificadores de acesso, como público, privado e protegido.

    5. **Herança:** A herança permite que você crie uma nova classe com base em uma classe 
    existente, herdando seus atributos e métodos. Isso promove a reutilização de código.

    6. **Polimorfismo:** O polimorfismo permite que objetos de classes diferentes sejam 
    tratados de maneira uniforme. Isso é alcançado por meio de interfaces comuns e métodos 
    que podem ser implementados de maneira diferente em classes diferentes.

    A criação de classes permite organizar o código de forma mais eficiente, promove a 
    reutilização de código e ajuda a modelar objetos do mundo real de forma mais precisa 
    no software. Em linguagens de programação orientadas a objetos, como Python, a 
    definição e o uso de classes são fundamentais para a criação de software eficaz e 
    organizado.

    
    O método __init__ é um construtor especial que é chamado quando um objeto da classe 
    é criado. Ele inicializa os atributos da classe com os valores fornecidos.
"""