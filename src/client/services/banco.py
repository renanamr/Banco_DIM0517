from src.server.services.banco import Banco

def credito():
    banco = Banco()
    numero = int(input("Digite o numero da conta:"))
    valor = float(input("Digite o valor a ser adicionado:"))
    if banco.credito(numero, valor):
        print("Foram adicionados " + str(valor) + " a conta " + str(numero))

def transferir():
    banco = Banco()
    origem = int(input("Digite o numero da conta de origem:"))
    destino = int(input("Digite o numero da conta de destino:"))
    valor = float(input("Digite o valor a ser transferido:"))
    if banco.transferir(origem, destino, valor):
        print("Foram transferidos " + str(valor) + " da conta " + str(origem) + " para a conta " + str(destino))

def debito():
    banco = Banco()
    numero = int(input("Digite o numero da conta:"))
    valor = float(input("Digite o valor a ser debitado:"))
    if banco.debito(numero, valor):
        print("Foram retirados " + str(valor) + " a conta " + str(numero))

def invalid_input():
    print("O número digitado é inválido")

def crie_conta():
    banco = Banco()
    print("Digite o número da conta a ser criado:")
    numero = int(input())
    print("Digite o saldo inicial da conta:")
    saldo = int(input())
    if(banco.criarConta(numero, saldo)):
        print("Conta criada com sucesso!")
    else:
        print("Esse conta já existe, tente novamente!")
        crie_conta()

def consulta_saldo():
    banco = Banco()
    print("Digite o número da conta:")
    numero = int(input())
    try:
        print("Essa conta tem "+str(banco.saldoConta(numero))+" reais")
    except:
        print("Essa conta não existe!")