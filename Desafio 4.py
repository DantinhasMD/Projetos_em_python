# Desafio 3 - Tranformção em POO - Definimos as classes do código: Contas, Usuários e Conta Bancária

class Usuario: #Organizar os Usuarios do Banco
    usuarios = []

    def __init__(self, nome, cpf, data_nascimento, logradouro, bairro, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = {
            "logradouro": logradouro,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        }
        Usuario.usuarios.append(self)

    @staticmethod
    def cpf_existe(cpf):
        """Verifica se o CPF já está cadastrado."""
        for usuario in Usuario.usuarios:
            if usuario.cpf == cpf:
                return True
        return False

    @staticmethod
    def criar_usuario():
        print('''
        Você optou por: Criar Usuário!
        ''')
        cpf = input('Informe seu CPF (apenas números): ')

        if Usuario.cpf_existe(cpf): #Chmar a função de verificação antes
            print("\nUsuário já cadastrado!\n")
            return None

        print("\nUsuário não encontrado! Vamos coletar suas informações:\n")
        nome = input('Nome completo: ')
        data_nascimento = input('Data de Nascimento (Ex: 01.01.2000 -> 01012000): ')

        print('''Vamos coletar suas informações de endereço:''')
        logradouro = input('Logradouro (Ex: Rua A, 151, apt 18): ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')

        endereco = {"logradouro": logradouro, "bairro": bairro, "cidade": cidade, "estado": estado}

        return Usuario(nome, cpf, data_nascimento, logradouro, bairro, cidade, estado)

class Conta: #Organizar as Contas do Banco
    contas = []

    def __init__(self, numero, cpf, saldo=0):
        self.numero = numero
        self.cpf = cpf
        self.saldo = saldo
        self.transacoes = []
        Conta.contas.append(self)

    @staticmethod
    def criar_conta(AGENCIA="0001"):
        """Cria uma conta apenas se o CPF já estiver cadastrado."""
        print("\nVocê optou por: Criar Conta!")

        cpf = input('\nInforme seu cpf (apenas o número):')

        if Usuario.cpf_existe(cpf):
            num_conta = len(Conta.contas) + 1
            nova_conta = Conta(numero=num_conta, cpf=cpf)
            print(f"""\nConta Criada com Sucesso!

                  ====== INFORMAÇÕES ======
                  Número da agência: {AGENCIA}
                  Número da Conta: {nova_conta.numero}
                  CPF cadastrado: {cpf}
            """)
            return nova_conta
        else:
            print("\nUsuário não encontrado! Cadastre-se primeiro.")

    @staticmethod
    def verificar_conta(num_conta):
      for conta in Conta.contas:
          if conta.numero == num_conta:
             return conta
      return None

    @staticmethod
    def depositar():
      print('\nVocê optou por: Depositar!')
      num_conta = int(input('\nInforme o número da conta: '))
      conta = Conta.verificar_conta(num_conta)

      if conta:
            valor = float(input('\nInforme o valor do depósito: '))
            if valor <= 0:
                print("\nValor inválido para depósito.")
                return
            conta.saldo += valor
            conta.transacoes.append(("Depósito", valor))
            print('\nDepósito realizado com sucesso!')

      else:
          print('\nConta não encontrada.')

    @staticmethod
    def consultar_extrato():
      print('\nVocê optou por: Consultar Extrato!')
      num_conta = int(input('\nInforme o número da conta: '))
      conta = Conta.verificar_conta(num_conta)

      if conta:
         print(f"\nExtrato da Conta {conta.numero} (CPF: {conta.cpf})")
         print("-" * 30)
         for tipo, valor in conta.transacoes:
             print(f"{tipo}: R$ {valor:.2f}")
         print("-" * 30)
         print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
      else:
        print("\nConta não encontrada.")

    @staticmethod
    def sacar(LIMITE_DE_SAQUES=3, limite_saque=500):
      print('\nVocê optou por: Sacar!')
      num_conta = int(input('\nInforme o número da conta: '))
      conta = Conta.verificar_conta(num_conta)

      if conta:
        saques_realizados = sum(1 for transacao in conta.transacoes if transacao[0]== 'Saque')
        if saques_realizados >= LIMITE_DE_SAQUES:
           print('\nLimite de Saques Diários Atingidos!')
           return

        valor = float(input('\nInforme o valor do saque: '))

        if valor <= 0:
            print('\nValor inválido.')
            return

        if valor > limite_saque:
           print('\nSaque maior do que o limite permitido')
           return

        if valor > conta.saldo:
            print('\nSaldo insuficiente para realizar o saque.')
            return

        conta.saldo -= valor
        conta.transacoes.append(('Saque', valor))
        print('\nSaque realizado com sucesso!')

      else:
        print('\nConta não encontrada!')

class Banco:

    @staticmethod
    def menu():
      print('\nSeja Bem-Vindo ao Banco X')
      menu = '''========= MENU =========
      [U] Novo Usuário
      [N] Nova Conta
      [D] Depositar
      [C] Consultar extrato
      [S] Sacar
      [X] Encerrar'''
      return print(menu)

    @staticmethod
    def encerrar_programa():
      return print("\nPrograma encerrado.")

    @staticmethod
    def main():
        Banco.menu()

        opcoes = {
            'u': lambda: Usuario.criar_usuario(),
            'n': lambda: Conta.criar_conta(),
            's': lambda: Conta.sacar(),
            'c': lambda: Conta.consultar_extrato(),
            'd': lambda: Conta.depositar(),
            'x': Banco.encerrar_programa
        }

        while True:
            opcao = input("\nQual operação deseja realizar: ")

            if opcao in opcoes:
                if opcao == 'x':
                    opcoes[opcao]()
                    break
                else:
                    opcoes[opcao]()
            else:
                print('\nEsta não é uma opção válida, tente novamente!')

        print("\nObrigado por utilizar nossos serviços!")

Banco.main()
