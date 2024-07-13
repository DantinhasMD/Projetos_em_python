# Melhorando código 2 - ATENÇÃO, CÓDIGO COM ERROS

print('Seja Bem Vindo ao Banco X!')

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, numero, cpf):
        self.agencia = agencia
        self.numero = numero
        self.cpf = cpf
        self.saldo = 0
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(('depósito', valor))
        print('Depósito realizado com sucesso!')

    def sacar(self, valor):
        if valor > 500:
            print('Valor de saque excede o limite de R$500')
            return
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.transacoes.append(('saque', valor))
        print('Saque realizado com sucesso!')

    def consultar_extrato(self):
        print('Extrato da conta:')
        for transacao in self.transacoes:
            print(transacao)
        print('Saldo atual: R$', self.saldo)

class Banco:
    LIMITE_DE_SAQUES = 3
    AGENCIA = '0001'

    def __init__(self):
        self.usuarios = []
        self.contas = []

    def menu(self):
        menu = ''' 
========= MENU =========
[U] Novo Usuário
[N] Nova Conta
[D] Depositar
[C] Consultar extrato
[S] Sacar
[X] Encerrar
'''
        print(menu)

    def criar_usuario(self):
        cpf = input('Informe seu cpf (apenas o número):')
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print('CPF já cadastrado.')
                return

        print('Vamos coletar seus dados!')
        nome = input('Nome completo: ')
        data_nascimento = input('Data de Nascimento (Ex: 01.01.2000: 01012000):')
        
        print('Agora vamos coletar suas informações de endereço!')
        logradouro = input('Logradouro (Ex: Rua Benjamim, 151, apt 18):')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')

        endereco = {'logradouro': logradouro, 'bairro': bairro, 'cidade': cidade, 'estado': estado}
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print('Usuário criado com sucesso!')

    def criar_conta(self):
        cpf = input('Informe o CPF do usuário:')
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                conta_numero = len(self.contas) + 1
                conta = Conta(self.AGENCIA, conta_numero, cpf)
                self.contas.append(conta)
                print('Conta criada com sucesso!')
                print(f'''
                      ====== INFORMAÇÕES ======
                      Número da agência: {self.AGENCIA}
                      Número da Conta: {conta_numero}
                      CPF cadastrado: {cpf}
                      ''')
                return
        print('Usuário não encontrado.')

    def depositar(self):
        conta_numero = int(input('Informe o número da conta: '))
        valor = float(input('Informe o valor do depósito: '))
        for conta in self.contas:
            if conta.numero == conta_numero:
                conta.depositar(valor)
                return
        print('Conta não encontrada.')

    def sacar(self):
        conta_numero = int(input('Informe o número da conta: '))
        valor = float(input('Informe o valor do saque: '))
        for conta in self.contas:
            if conta.numero == conta_numero:
                conta.sacar(valor)
                return
        print('Conta não encontrada.')

    def consultar_extrato(self):
        conta_numero = int(input('Informe o número da conta: '))
        for conta in self.contas:
            if conta.numero == conta_numero:
                conta.consultar_extrato()
                return
        print('Conta não encontrada.')

    def encerrar_programa(self):
        print('Programa encerrado.')

    def iniciar(self):
        self.menu()
        while True:
            opcao = input('Qual operação deseja realizar: ').lower()
            if opcao not in ['u','n','s','c','d','x']:
                print('Esta não é uma opção válida, tente novamente!')
                continue

            if opcao == 'u':
                self.criar_usuario()
            elif opcao == 'n':
                self.criar_conta()
            elif opcao == 's':
                self.sacar()
            elif opcao == 'c':
                self.consultar_extrato()
            elif opcao == 'd':
                self.depositar()
            elif opcao == 'x':
                self.encerrar_programa()
                break

        print('Obrigado por utilizar nossos serviços!')

# Inicializar o banco e iniciar o programa
banco = Banco()
banco.iniciar()
