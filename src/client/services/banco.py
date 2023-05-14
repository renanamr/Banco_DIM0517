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
