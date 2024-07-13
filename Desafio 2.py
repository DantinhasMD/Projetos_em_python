# Melhorar o código do Desafio 1 - ATENÇÃO, CÓDIGO COM ERROS !
# O SALDO NÃO ESTÁ FUNCIONANDO - ACUMULADOR ERRADO! 
print('Seja Bem Vindo ao Banco X!') # Menu com todas as funções novas

def menu(): 
    menu = ''' 
========= MENU =========
[U] Novo Usuário
[N] Nova Conta
[D] Depositar
[C] Consultar extrato
[S] Sacar
[X] Encerrar

'''
    return print(menu)

# Criar Funções para: Novo usuário, Nova conta, Sacar, Depositar, Consultar extrato e Encerrar 
def criar_usuario(usuarios):
    cpf = input('Informe seu cpf (apenas o número):')
    for usuario in usuarios:
        if usuario[2] == cpf: # Verifica se o CPF já existe
            print("CPF já cadastrado.")
            return
    
    print('''
          Vamos coletar seus dados!
          ''')
    nome = input('Nome completo: ')
    data_nascimento = input('Data de Nascimento (Ex: 01.01.2000: 01012000):')
    cpf = input('Cpf (Ex: 123456789-12: 12345678912): ')
    
    print('''
          Agora vamos coletar suas informações de endereço!
          ''')
    logradouro = input('Logradouro (Ex: Rua Benjamim, 151, apt 18):')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')
    
    usuario = [nome, data_nascimento, cpf, {'logradouro': logradouro, 'bairro': bairro, 'cidade': cidade, 'estado': estado}] # Lista
    usuarios.append(usuario) # Adicionar o usuário
    
    print('''
          Usuário criado com sucesso!
          ''')

# Função para criar uma nova conta
def criar_conta(AGENCIA, contas, usuarios):
    cpf = input('Informe o CPF do usuário:')
    for usuario in usuarios: 
        if usuario[2] == cpf: # Este ASSUME que o cpf está em outra posição
            conta_numero = len(contas) + 1
            conta = [AGENCIA, conta_numero, cpf]
            contas.append(conta)

        print('''
              Conta criada com sucesso!
              ''')
        print(f'''
              ====== INFORMAÇÕES ======

              Número da agência:{AGENCIA}
              Número da Conta: {conta_numero}
              CPF cadastrado: {cpf}
            
             ''')
        return
    print('''
          Usuário não encontrado.
          ''')

# Função para depositar dinheiro
def depositar(contas, conta_numero, saldo, /): # Função deposito: positional 
    conta_numero = int(input('Informe o número da conta: '))
    saldo = float(input('Informe o valor do depósito: '))
    for conta in contas:
        if conta[1] == conta_numero: # ASSUMIR outro número de conta
            if len(conta) == 3:
                conta.append([])
            conta[3].append(('depósito', saldo))
            print('''
                  Depósito realizado com sucesso!
                  ''')
            return

    print('''
          Conta não encontrada
          ''')

# Função para sacar dinheiro
def sacar(*, contas, conta_numero, saldo, LIMITE_DE_SAQUES): # Função saque: keyword
    conta_numero = int(input('Informe o número da conta: '))
    saldo = float(input('Informe o valor do saque: '))
    saques_realizados = 0
    for conta in contas:
        if conta[1] == conta_numero: 
            for transacao in conta[3]:
                if transacao[0] == 'saque':
                    saques_realizados += 1
            if saques_realizados >= LIMITE_DE_SAQUES:
                print('''
                      Limite de saques atingido
                      ''')
                return
            if saldo > 500:
                print('''
                      Valor de saque excede o limite de R$500
                      ''')
                return
            conta[3].append(('saque', saldo))
            print('''
                  Saque realizado com sucesso!
                  ''')
            return
    print('''
          Conta não encontrada
          ''')

# Função para consultar o extrato
def consultar_extrato(saldo, /, *, contas, conta_numero, extrato): # Função extrato: positional (saldo) e keyword (extrato)
    conta_numero = int(input('Informe o número da conta: '))
    for conta in contas:
        if conta[1] == conta_numero:
            for transacao in conta[3:]:
                if transacao[0] == 'depósito':
                    saldo += transacao[1]
                elif transacao[0] == 'saque':
                    saldo -= transacao[1]
            if extrato:
                print("Extrato da conta:")
                for transacao in conta[3:]:
                    print(transacao)
            print("Saldo atual: R$", saldo)
            return
    print("Conta não encontrada.")

# Função para encerrar o programa
def encerrar_programa():
    return print("Programa encerrado.")

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"
    conta_numero = 1
    saldo = 0
    extrato = ''
    usuarios = []
    contas = []

    menu()
    while True:
        opcao = input("Qual operação deseja realizar: ")
        if opcao not in ['u','n','s', 'c', 'd' , 'x']:
            print('Esta não é uma opção válida, tente novamente!')
            continue

        else: 
            if opcao == 'u':
                criar_usuario(usuarios)
                continue
            
            elif opcao == 'n':
                criar_conta(AGENCIA, contas, usuarios)
                continue
            
            elif opcao == "s":
                sacar(contas=contas, conta_numero=conta_numero, saldo=saldo, LIMITE_DE_SAQUES=LIMITE_DE_SAQUES)
                continue

            elif opcao == 'c':
                consultar_extrato(saldo, contas=contas, conta_numero='conta_numero', extrato=extrato)
                continue

            elif opcao == "d":
                depositar(contas, saldo, extrato)
                continue

            elif opcao == 'x':
                encerrar_programa()
                break
            
            else:
                print('ix')
                continue

    print("Obrigado por utilizar nossos serviços!")
main()