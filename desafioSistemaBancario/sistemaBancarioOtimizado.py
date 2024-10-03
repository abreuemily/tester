import datetime as dt
import pytz
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[cu] Cadastrar usuário
[cc] Criar conta correntee
[q] Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 10
users = {}
contas_corrente = {}
cont_numeros_de_conta = 1

def cria_conta_corrente(usuario):
  global contas_corrente, cont_numeros_de_conta
  agencia = '0001'
  contas_corrente.update({cont_numeros_de_conta : [agencia, cont_numeros_de_conta, usuario]})
  cont_numeros_de_conta += 1

def cadastrar_usuario(nome, data_nascimento, cpf, logradouro, nro, bairro, cidade, sigla_estado):
  global users
  endereco = f'{logradouro} - {bairro} - {cidade}/{sigla_estado}'
  dados = [nome, data_nascimento, cpf, endereco]
  users.update({cpf : dados})

def saque(*, valor):
  global limite, saldo, extrato, numero_saques
  while valor > limite:
    valor = int(input('O limite para saque é de R$ 500.00. Informe o valor do saque: R$'))
  if valor > saldo:
    print('Infelizmente o(a) senhor(a) está sem dinheirokkkkkk')
  else:
    saldo-=valor
    numero_saques+=1
    extrato = extrato + f"\nsaque: R$ {valor:.2f} Realizado no dia {dt.datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}\n"
    print('Saque efetuado com sucesso!')

def deposito(valor,/):
  global extrato, saldo
  saldo += valor
  extrato = extrato + f'\ndepósito: R$ {valor:.2f} Realizado no dia {dt.datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M")}\n'
  print('Depósito efetuado com sucesso!')

def tirar_extrato(saldo,/,*,extrato):
  if len(extrato) == 0:
    print('Não foram realizadas movimentações')
  else:
    print(f'{extrato}\nSaldo atual: R$ {saldo:.2f}')

while True:

  opcao = input(menu)

  if opcao == 'd':

    valor = int(input('Informe o valor para depósito: R$ '))

    while valor < 0:

      valor = int(input('Valor invalido. Informe um valor válido: R$ '))

    deposito(valor)

  elif opcao == 's':

    if numero_saques >= LIMITE_SAQUES:

      print('O limite de saques é 10 por dia. Saque outro dia.')

    else:

      valor_saque = int(input('O limite para saque é de R$ 500.00. Informe o valor do saque: R$'))

      saque(valor=valor_saque)

  elif opcao == 'e':
    tirar_extrato(saldo, extrato=extrato)

  elif opcao == 'cu':
    print('Vamos precisar de algumas informações. Não se preocupe, respeitamos a LGPD.')

    cpf = input('Primeiro, informe o CPF para verificarmos se o usuário já é cadastrado: ')

    if users.get(cpf) == None:
      print('Certo, vamor dar continuidade ao cadastro.')

      nome = input('Informe o nome: ')

      data_nascimento = input('Informe a data de nascimento (dd/mm/YY): ')

      print('Agora, o endereço:')

      logradouro = input('Logradouro: ')

      nro = input('Nº da resedência: ')

      bairro = input('Bairro: ')

      cidade = input('Cidade: ')

      estado = input('Sigla do seu estado: ')

      cadastrar_usuario(nome, data_nascimento, cpf, logradouro, nro, bairro, cidade, estado)

      print('O usuário foi cadastrado com sucesso!!!')
    
    else: 

      print('Esse usuário já é cadastrado.')
  
  elif opcao == 'cc':

    print('Ah, então você quer criar uma conta corrente? Então tá!')

    cpf = input('Primeiro, precisamos saber se tem cadástro. informe o CPF: ')

    if users.get(cpf) == None:
      print('Antes de abrir uma coonta corrente, faça o seu cadastro.')

    else: 

      print('Este usuário é cadastrado!')

      cria_conta_corrente(cpf)

      print(f'Conta criada com sucesso! O numero da sua conta é {cont_numeros_de_conta - 1}.')

  elif opcao == 'q':
    break

  else:
    print('Por favor, escolha uma opção válida (anta)')
