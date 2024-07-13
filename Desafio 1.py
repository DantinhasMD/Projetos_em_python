# Criar um Sistema bancário - deposito, saque e extrato
print('Seja Bem Vindo ao Banco X!') # Abrir sistema, dar boas vindas e apresentar as opções 

print(''' Opções:
[S] Sacar
[C] Consultar extrato
[D] Depositar
[X] Encerrar

''')
saldo = 2755
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True: 

    opcao = input("Qual operação deseja realizar: ")
    if opcao not in ['s', 'c', 'd' , 'x']:
        print('Esta não é uma opção válida, tente novamente!')
        continue

    else: 
        if opcao == 's':
            saque = float(input("Informe quanto deseja sacar: "))

            excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

            excedeu_saldo = saldo < saque

            if saque > 500: # Permitir saques de até R$500
                print('O valor excede o limite da conta. Tente Novamente!') 
                continue # Informar que o limite para saque foi ultrapassado

            elif excedeu_saldo: 
                print('Saldo insuficiente para concluir a operação')
                continue

            elif excedeu_saque: # Permitir apenas 3 saques
                print('O número de saques diários disponíveis já foi ultrapassado. Tente novamente amanhã!')
                continue

            else:
                saldo -= saque
                print(f'O valor de R$ {saque:.2f} foi debitado de sua conta. Extrato final de R$ {saldo:.2f}')
                numero_de_saques += 1
                continue

        elif opcao == 'c':
            print(f"Seu extrato é de R$ {saldo:.2f}")
            continue

        elif opcao == 'd':
            deposito = float(input('Informe quanto deseja depositar: '))
            if deposito > 0:
                saldo += deposito
                print(f'Seu extrato atual é de R$ {saldo:.2f}')
                continue

            else: 
                print("O valor não foi identificado. Por favor, tente novamente!")
                continue

        else: 
            print(f'Você optou por encerrar a operação! Seu extrato final é de R$ {saldo:.2f}')

    print("Obrigado por utilizar nossos serviços!")
    break

     