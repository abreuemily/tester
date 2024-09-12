menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def saque():
  global limite, saldo, extrato, numero_saques

  valor_saque = int(input('O limite para saque é de R$ 500.00. Informe o valor do saque: R$'))

  while valor_saque > limite:
    valor_saque = int(input('O limite para saque é de R$ 500.00. Informe o valor do saque: R$'))
  
  if valor_saque > saldo:
    print('Infelizmente o(a) senhor(a) está sem dinheirokkkkkk')

  else:
    saldo-=valor_saque
    numero_saques+=1
    extrato = extrato + f"\nsaque: R$ {valor_saque:.2f}\n"
    print('Saque efetuado com sucesso!')

def deposito():
  global extrato, saldo
  
  valor_deposito = int(input('Informe o valor para depósito: R$ '))
  
  while valor_deposito < 0:
    valor_deposito = int(input('Valor invalido. Informe um valor válido: R$ '))
  
  saldo += valor_deposito
  extrato = extrato + f'\ndepósito: R$ {valor_deposito:.2f}\n'

  print('Depósito efetuado com sucesso!')

def tirar_extrato():
  global extrato, saldo

  if len(extrato) == 0:
    print('Não foram realizadas movimentações')
  
  else:
    print(f'{extrato}\nSaldo atual: R$ {saldo:.2f}')


while True:

  opcao = input(menu)

  if opcao == 'd':
    deposito()
  
  elif opcao == 's':
    if numero_saques >= LIMITE_SAQUES:
      print('O limite de saques é 3 por dia. Saque outro dia.')

    else:
      saque()

  elif opcao == 'e':
    tirar_extrato()

  elif opcao == 'q':
    break

  else:
    print('Por favor, escolha uma opção válida (anta)')