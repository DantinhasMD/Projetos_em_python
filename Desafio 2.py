# Desafio 2 - Melhorando em Funções
def menu():
  print('''Seja Bem-Vindo ao Banco X
  ''')
  menu = '''========= MENU =========
[U] Novo Usuário
[N] Nova Conta
[D] Depositar
[C] Consultar extrato
[S] Sacar
[X] Encerrar'''
  return print(menu)

def criar_usuario(usuarios):
  print('''
  Você optou por: Criar Usuário!
  ''')
  cpf = input('Informe seu cpf (apenas o número):')
  for usuario in usuarios:
    if usuario[2] == cpf:
      print('''
      Usuário já Cadastrado!
      ''')
      return

  print('''
  Usuário não Encontrado! Vamos Coletar suas informações:
  ''')
  nome = input('Nome completo: ')
  data_nascimento = input('Data de Nascimento (Ex: 01.01.2000: 01012000):')
  cpf = input('Cpf (Ex: 123456789-12: 12345678912): ')

  print('''
  Vamos coletar suas informações de enfereço:
  ''')
  logradouro = input('Logradouro (Ex: Rua Benjamim, 151, apt 18):')
  bairro = input('Bairro: ')
  cidade = input('Cidade: ')
  estado = input('Estado: ')

  usuario = [nome, data_nascimento, cpf, {'logradouro': logradouro, 'bairro': bairro, 'cidade': cidade, 'estado': estado}]
  usuarios.append(usuario)
  print('''
  Usuário criado com Sucesso!
  ''')
  return

def criar_conta(usuarios, contas, AGENCIA):
  print('''
  Você optou por: Criar Conta!''')

  cpf = input('Informe seu cpf (apenas o número):')
  for usuario in usuarios:
        if usuario[2] == cpf:
          num_conta = len(contas) + 1
          conta = [AGENCIA, num_conta, cpf]
          contas.append(conta)

          print(f'''Conta Criada com Sucesso!

                       ====== INFORMAÇÕES ======

                       Número da agência:{AGENCIA}
                       Número da Conta: {num_conta}
                       CPF cadastrado: {cpf}
          ''')
          return


  print('''
  Usuário não Encontrado!
  ''')

def depositar(contas, /):
  print('''
  Você optou por: Depositar!''')
  num_conta = int(input('Informe o número da conta: '))
  for conta in contas:
    if conta[1]== num_conta:
      saldo = float(input('Informe o valor do depósito: '))
      if len(conta) == 3:
        conta.append([])
        conta[3].append(('depósito', saldo)) #transação
        print('''
              Depósito realizado com sucesso!
                  ''')
        return


  print('''
  Conta não encontrada
  ''')

def sacar(*, contas, LIMITE_DE_SAQUES, limite_saque):
  print('''
  Você optou por: Sacar!''')
  num_conta = int(input('Informe o número da conta: '))
  for conta in contas:
    if conta[1]== num_conta:
      saques_realizados = sum(1 for transacao in conta[3] if transacao[0]== 'saque')
      if saques_realizados >= LIMITE_DE_SAQUES:
          print('''
          Limite de Saques Diários Atingidos!
          ''')
          return

      saldo = float(input('Informe o valor do saque: '))

      if saldo > limite_saque:
          print('''
          Saque maior do que o limite permitido
          ''')
          return

      conta[3].append(('saque', saldo))
      print('''
       Saque realizado com sucesso!
       ''')
      return

  print('''
  Conta não encontrada!
  ''')

def consultar_extrato(saldo, *, contas):
    conta_numero = int(input('Informe o número da conta: '))
    for conta in contas:
        if conta[1] == conta_numero:
            for transacao in conta[3]:
                if transacao[0] == 'depósito':
                    saldo += transacao[1]
                elif transacao[0] == 'saque':
                    saldo -= transacao[1]
                print(f'''
                      Extrato da conta:
                      {transacao}
                      ''')

            print("Saldo atual: R$", saldo)
            return
    print("Conta não encontrada.")


def encerrar_programa():
  return print("Programa encerrado.")

def main():
    usuarios = []
    contas = []
    AGENCIA = 698
    saldo = 0
    LIMITE_DE_SAQUES = 3
    limite_saque = 500

    menu()

    opcoes = {
        'u': lambda: criar_usuario(usuarios),
        'n': lambda: criar_conta(usuarios, contas, AGENCIA),
        's': lambda: sacar(contas=contas, LIMITE_DE_SAQUES=LIMITE_DE_SAQUES, limite_saque=limite_saque),
        'c': lambda: consultar_extrato(saldo=saldo, contas=contas),
        'd': lambda: depositar(contas),
        'x': encerrar_programa
    }

    while True:
        opcao = input("Qual operação deseja realizar: ")

        if opcao in opcoes:
            if opcao == 'x':
                opcoes[opcao]()
                break
            else:
                opcoes[opcao]()
        else:
            print('Esta não é uma opção válida, tente novamente!')

    print("Obrigado por utilizar nossos serviços!")

main()
