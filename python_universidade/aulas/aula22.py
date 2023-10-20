# Programação Orientada a Objetos (POO)

# Classes

# Importando o módulo 'math'
import math

# Definindo uma classe chamada 'Circulo'.
class Circulo:
    # Método construtor que inicializa o raio do círculo.
    def __init__(self, raio):
        self.raio = raio
        
    # Método pára calcular a área do circulo.
    def calcular_area(self):
        area = math.pi * self.raio ** 2
        return area
    
# Criando uma instância (objeto) da classe 'Circulo'.
circulo1 = Circulo(5)

# Acessando o raio.
raio_do_circulo = circulo1.raio

# Calculando a área do círculo.
area_do_circulo = circulo1.calcular_area()

# Imprimindo
print(f'Raio do circulo : {raio_do_circulo}')
print(f'Área do círculo : {area_do_circulo:.2f}')


# Informações sobre o módulo nativo do Python chamado 'math'.
"""
    O módulo math é um módulo padrão da biblioteca padrão do Python que fornece funções 
    matemáticas e constantes matemáticas para realizar operações matemáticas mais 
    avançadas em seus programas. Ele é amplamente utilizado quando você precisa realizar 
    cálculos matemáticos, como cálculos trigonométricos, exponenciais, raízes quadradas, 
    entre outros. Aqui estão algumas das funcionalidades principais do módulo math:

    Constantes Matemáticas: O módulo math inclui constantes matemáticas importantes, 
    como π (pi) e e (número de Euler). Você pode acessar essas constantes usando math.pi 
    e math.e.

    Funções Matemáticas: O módulo fornece uma ampla variedade de funções matemáticas, 
    como math.sqrt() (raiz quadrada), math.sin() (seno), math.cos() (cosseno), 
    math.tan() (tangente), math.exp() (exponencial), math.log() (logaritmo natural), 
    math.log10() (logaritmo na base 10), entre outras.

    Funções Trigonométricas: O módulo inclui funções trigonométricas, como seno, cosseno 
    e tangente, que são úteis para trabalhar com ângulos e triângulos.

    Funções Hiperbólicas: Além das funções trigonométricas, o módulo math oferece funções 
    hiperbólicas, como math.sinh() (seno hiperbólico) e math.cosh() (cosseno hiperbólico).

    Funções de Arredondamento: Você pode usar math.floor() (arredondamento para baixo) e 
    math.ceil() (arredondamento para cima) para manipular números reais.

    Funções de Potenciação e Raiz: O módulo math fornece funções para elevar um número a 
    uma potência, como math.pow(), e para calcular raízes, como math.sqrt().

    Constantes de Precisão: Além de π e e, o módulo math também fornece constantes de 
    precisão, como math.inf (infinito positivo) e math.nan (não é um número).

    Funções de Sinal: Você pode usar funções como math.copysign() para copiar o sinal de 
    um número de um para outro.

    O módulo math é uma ferramenta poderosa para cálculos matemáticos em Python e é 
    amplamente utilizado em áreas como ciência, engenharia, matemática e física. 
    Ele oferece um conjunto abrangente de funções para ajudar a resolver problemas 
    matemáticos complexos em seus programas.
"""