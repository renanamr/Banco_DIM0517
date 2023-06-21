import requests

PREFIX = "http://localhost:5000/banco/conta/"

def credito():
    
    numero = int(input("Digite o numero da conta:"))
    valor = float(input("Digite o valor a ser adicionado:"))
    
    url = PREFIX+str(numero)+"/credito"
    
    ans = requests.put(url,json = {"valor":valor})
    
    if ans.status_code=='200':
        print("Foram creditados " + str(valor) + " a conta " + str(numero))
    else:
        print(ans.text)

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
    print("Digite o número da conta a ser criado:")
    numero = int(input())
    print("Digite o saldo inicial da conta:")
    saldo = int(input())

    url = PREFIX
    ans = requests.post(url,json = {"numero":numero,"saldo":saldo, "tipo": "normal"})

    if ans.status_code=='200':
        print("Contra criada com sucesso! numero: "+str(numero)+" saldo: "+str(saldo))
    else:
        print(ans.text)

def crie_conta_bonus():
    print("Digite o número da conta bônus a ser criado:")
    numero = int(input())

    url = PREFIX
    ans = requests.post(url,json = {"numero":numero,"tipo": "bonus"})

    if ans.status_code=='200':
        print("Contra criada com sucesso! numero: "+str(numero))
    else:
        print(ans.text)

def crie_conta_poupanca():
    print("Digite o número da conta poupança a ser criada:")
    numero = int(input())
    url = PREFIX
    ans = requests.post(url,json = {"numero":numero,"tipo": "poupanca"})

    if ans.status_code=='200':
        print("Contra criada com sucesso! numero: "+str(numero))
    else:
        print(ans.text)


def consulta_saldo():
    print("Digite o número da conta:")
    numero = int(input())

    url = PREFIX+str(numero)+"/saldo"
    ans = requests.get(url)

    if ans.status_code=='200':
        print("Contra criada com sucesso! numero: "+str(numero))
    else:
        print(ans.text)


def renda_juros():
    numero = int(input("Digite o numero da conta:"))
    valor = float(input("Digite os juros:"))

    url = PREFIX+"rendimento"

    ans = requests.put(url,json = {"numero":numero,"valor":valor})

    if ans.status_code=='200':
        print("Juros de " + str(valor) + " rendidos com sucesso, na conta " + str(numero))
    else:
        print(ans.text)


def get_info():
    numero = int(input("Digite o número da conta:"))
    url = PREFIX+str(numero)+"/informacoes"
    
    ans = requests.get(url)
    
    print(ans.text)
    
