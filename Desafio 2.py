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
    for usuario in usuarios: # Usuário vai estar dentro de usuarios
        if usuario[2] == cpf: # O [2] acessa o terceiro elemento dos parâmetros de usuario (cpf) e verifica se há um igual
            print("CPF já cadastrado.")
            return
    # Recolhe os argumentos dos parâmetros
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
    # Parâmetros de usuario
    usuario = [nome, data_nascimento, cpf, {'logradouro': logradouro, 'bairro': bairro, 'cidade': cidade, 'estado': estado}] # Lista
    usuarios.append(usuario) # Adicionar o usuário
    
    print('''
          Usuário criado com sucesso!
          ''')

# Função para criar uma nova conta
def criar_conta(AGENCIA, contas, usuarios):
    cpf = input('Informe o CPF do usuário:')
    for usuario in usuarios: 
        if usuario[2] == cpf: # o cpf realmente existe
            conta_numero = len(contas) + 1 # Verificar quantas contas existem e somar +1
            conta = [AGENCIA, conta_numero, cpf] # Parâmetros de conta
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
def depositar(contas, /): # Função deposito: positional 
    conta_numero = int(input('Informe o número da conta: ')) # Definir aqui, não precisa do parâmetro
    saldo = float(input('Informe o valor do depósito: ')) # Definir aqui, não precisa do parâmetro
    for conta in contas:
        if conta[1] == conta_numero: # Conferir se o numero da conta informado  esta em conta - elemento dois
            if len(conta) == 3: # Se conta só tiver 3 elemntos, adiciona uma lista vazia
                conta.append([]) # Nessa lista colocaremos saldo
            conta[3].append(('depósito', saldo)) # No quarto elemento, saldo!
            print('''
                  Depósito realizado com sucesso!
                  ''')
            return

    print('''
          Conta não encontrada
          ''')

# Função para sacar dinheiro
def sacar(*, contas, LIMITE_DE_SAQUES): # Função saque: keyword
    conta_numero = int(input('Informe o número da conta: '))
    saldo = float(input('Informe o valor do saque: '))
    saques_realizados = 0
    for conta in contas:
        if conta[1] == conta_numero: 
            for transacao in conta[3]: # Parâmetro que criamos - SALDO
                if transacao[0] == 'saque': # Transacao é apenas o nome que demos para facilitar o entendimento
                    saques_realizados += 1 # Vai adicionar até ter 3 "saque" dentro de conta[3]
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
    saldo = [transacao] # Elemento de saldo
    print('''
          Conta não encontrada
          ''')

# Função para consultar o extrato
def consultar_extrato(saldo, /, *, contas): # Função extrato: positional (saldo) e keyword (extrato)
    conta_numero = int(input('Informe o número da conta: '))
    for conta in contas:
        if conta[1] == conta_numero:
            for transacao in conta[3]:
                if transacao[0] == 'depósito': # Verificar se o primeiro elemento é um deposito
                    saldo += transacao[1] # Pega o saldo = 0 e soma
                elif transacao[0] == 'saque': # Ou um saque
                    saldo -= transacao[1] # Pega o saldo = 0 e subtrai
                print(f'''
                      Extrato da conta: 
                      {transacao}
                      ''')

            print("Saldo atual: R$", saldo)
            return
    print("Conta não encontrada.")

# Função para encerrar o programa
def encerrar_programa():
    return print("Programa encerrado.")

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
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
                sacar(contas=contas, LIMITE_DE_SAQUES=LIMITE_DE_SAQUES)
                continue

            elif opcao == 'c':
                consultar_extrato(saldo, contas=contas)
                continue

            elif opcao == "d":
                depositar(contas)
                continue

            elif opcao == 'x':
                encerrar_programa()
                break
            
            else:
                print('ix')
                continue

    print("Obrigado por utilizar nossos serviços!")
main()