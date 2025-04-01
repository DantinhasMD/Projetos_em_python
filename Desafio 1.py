# Desafio 1
print('Seja bem-vindo ao Banco X!')

print('''Opções Disponíveis:
[S] - Sacar
[C] - Consultar extrato
[D] - Depositar
[X] - Encerrar''')

saldo = 0
LIMITE_DE_SAQUES = 3
numero_de_saques = 0
limite_saque = 500

while True:
  opcao = input("Qual operação deseja realizar: ")
  if opcao not in ['s','c','d','x']:
    print('Digite uma opção válida')
    continue
  else:
    if opcao == 's':
      saque = float(input("Informe quanto deseja sacar: "))

      excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

      excedeu_saldo = saldo < saque

      if saque > limite_saque:
         print('O valor excede o limite da conta. Tente Novamente!')
         continue

      elif excedeu_saldo:
          print('Saldo insuficiente para concluir a operação')
          continue

      elif excedeu_saque:
          print('O número de saques diários disponíveis já foi ultrapassado. Tente novamente amanhã!')
          continue

      else:
        saldo -= saque
        print(f'O valor de R$ {saque:.2f} foi debitado de sua conta. Extrato final de R$ {saldo:.2f}')
        numero_de_saques += 1
        continue

    elif opcao == 'c':
      print(f'Seu extrato é de R$ {saldo:.2f}')
      continue

    elif opcao == 'd':
      deposito = float(input('Informe quanto deseja depositar: '))
      if deposito < 0:
        print("O valor não foi identificado. Por favor, tente novamente!")
        continue

      else:
        saldo += deposito
        print(f'Seu extrato atual é de R$ {saldo:.2f}')
        continue

    else:
      print("Obrigado por utilizar nossos serviços!")
      break
