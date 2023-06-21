import requests

PREFIX = "http://localhost:5000/banco/conta/"

def credito():
    return 
    banco = Banco()
    numero = int(input("Digite o numero da conta:"))
    valor = float(input("Digite o valor a ser adicionado:"))
    if banco.credito(numero, valor):
        print("Foram adicionados " + str(valor) + " a conta " + str(numero))

def transferir():
    
    origem = int(input("Digite o numero da conta de origem:"))
    destino = int(input("Digite o numero da conta de destino:"))
    valor = float(input("Digite o valor a ser transferido:"))

    url = PREFIX+"transferencia"

    ans = requests.put(url,json = {"origem":origem,"destino":destino,"valor":valor})

    if ans.status_code=='200':
        print("Foram transferidos " + str(valor) + " da conta " + str(origem) + " para a conta " + str(destino))
    else:
        print(ans.text)

def debito():
    
    numero = int(input("Digite o numero da conta:"))
    valor = float(input("Digite o valor a ser debitado:"))
    
    url = PREFIX+str(numero)+"/debito"
    
    ans = requests.put(url,json = {"valor":valor})
    
    if ans.status_code=='200':
        print("Foram retirados " + str(valor) + " a conta " + str(numero))
    else:
        print(ans.text)

def invalid_input():
    print("O número digitado é inválido")

def crie_conta():
    return 
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
    return 
    banco = Banco()
    print("Digite o número da conta bônus a ser criado:")
    numero = int(input())
    if(banco.criarContaBonus(numero)):
        print("Conta bônus criada com sucesso!")
    else:
        print("Esse conta já existe, tente novamente!")
        crie_conta_bonus()

def crie_conta_poupanca():
    return 
    banco = Banco()
    print("Digite o número da conta poupança a ser criada:")
    numero = int(input())
    print("Digite o saldo da conta poupança a ser criada:")
    saldo = float(input())
    if(banco.criarContaPoupanca(numero, saldo)):
        print("Conta poupança criada com sucesso!")
    else:
        print("Esse conta já existe, tente novamente!")
        crie_conta_bonus()


def consulta_saldo():
    return 
    banco = Banco()
    print("Digite o número da conta:")
    numero = int(input())
    try:
        print("Essa conta tem "+str(banco.saldoConta(numero))+" reais")
    except:
        print("Essa conta não existe!")


def renda_juros():
    return 
    banco = Banco()
    print("Digite o número da conta:")
    numero = int(input())        

    print("Digite os juros:")
    val = float(input())    
    
    banco.renda_juros(numero,val)

    print("Juros rendidos com sucesso, agora você tem: "+str(banco.saldoConta(numero)))


def get_info():
    numero = int(input("Digite o número da conta:"))
    url = PREFIX+str(numero)+"/informacoes"
    
    ans = requests.get(url)
    
    print(ans.text)
    
