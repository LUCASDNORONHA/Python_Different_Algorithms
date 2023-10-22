# Brincando com classe e funções.

# Classe Conta Bancária:
""" 
    Crie uma classe ContaBancaria com atributos como número da conta, titular da conta e 
    saldo. Implemente métodos para depositar, sacar e mostrar o saldo da conta.
"""

# Criando a classe ContaBancaria.
class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    # Método depositar.
    def depositar(self, deposito):
        self.saldo += deposito
        print()
        print('Deposito feito com sucesso!')
    
    # Método sacar.
    def sacar(self, saque):
        self.saldo -= saque
        print()
        print('Saque feito com sucesso!')
    
    # Método mostrar saldo.
    def mostrar_saldo(self):
        print(f'Saldo : {self.saldo}')

    # Método mostrar informações da conta.
    def mostrar_info_conta(self):
        print(f'Titular : {self.titular}')
        print(f'Conta : {self.numero_conta}')

# Criando função ClienteAcessarConta,
def ClienteAcessarConta():
    while True:
        print('-'*50)
        fazer = input('\n Depositar\n Sacar\n Mostrar Saldo\n Sair\n Digite uma das opções: ')
        print('-'*50)
        print()

        if fazer.lower() == 'Depositar'.lower():
            print('-'*50)
            valor = float(input(' Digite valor a ser depositado : '))
            conta1.depositar(valor)
            print('-'*50)
            print()

        elif fazer.lower() == 'Sacar'.lower():
            print('-'*50)
            valor = float(input(' Digite o valor que deseja sacar : '))
            conta1.sacar(valor)
            print('-'*50)
            print()

        elif fazer.lower() == 'Mostrar Saldo'.lower():
            print('-'*50)
            conta1.mostrar_saldo()
            print('-'*50)
            print()

        elif fazer.lower() == 'Sair'.lower():
            print('-'*50)
            print(' Saindo da conta...')
            print('-'*50)
            break

        else:
            print('-'*50)
            print(' Opção inválida. Tente novamente.')
            print('-'*50)
            print()


# Criando nossa instância (objeto) da nossa classe  ContaBancaria.
conta1 = ContaBancaria(2232433, 'Lucas Dias Noronha', 500.00,)

# Imprimindo informações da conta.
print('-'*50)
print()
conta1.mostrar_info_conta()
print()
print('-'*50)

# Chamando acesso a conta.
ClienteAcessarConta()