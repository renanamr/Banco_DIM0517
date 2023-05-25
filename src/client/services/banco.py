from src.server.services.banco import Banco
from src.server.config import TipoConta;

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

def crie_conta_bonus():
    banco = Banco()
    print("Digite o número da conta bônus a ser criado:")
    numero = int(input())
    if(banco.criarContaBonus(numero)):
        print("Conta bônus criada com sucesso!")
    else:
        print("Esse conta já existe, tente novamente!")
        crie_conta_bonus()

def crie_conta_poupanca():
    banco = Banco()
    print("Digite o número da conta poupança a ser criado:")
    numero = int(input())
    if(banco.criarContaPoupanca(numero)):
        print("Conta poupança criada com sucesso!")
    else:
        print("Esse conta já existe, tente novamente!")
        crie_conta_bonus()


def consulta_saldo():
    banco = Banco()
    print("Digite o número da conta:")
    numero = int(input())
    try:
        print("Essa conta tem "+str(banco.saldoConta(numero))+" reais")
    except:
        print("Essa conta não existe!")


def renda_juros():
    banco = Banco()
    print("Digite o número da conta:")
    numero = int(input())        

    print("Digite os juros:")
    val = float(input())    
    
    banco.renda_juros(numero,val)

    print("Juros rendidos com sucesso, agora você tem: "+str(banco.saldoConta(numero)))