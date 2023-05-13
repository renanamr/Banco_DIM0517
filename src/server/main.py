from services.banco import Banco
from time import sleep

banco = Banco()

def invalid_input():
    print("O número digitado é inválido")

def crie_conta():
    print("Digite o número da conta a ser criado:")
    numero = int(input())
    if(banco.criarConta(numero)):
        print("Conta criada com sucesso!")
    else:
        print("Esse conta já existe, tente novamente!")
        crie_conta()

def consulta_saldo():
    print("Digite o número da conta:")
    numero = int(input())
    try:
        print("Essa conta tem "+str(banco.saldoConta(numero))+" reais")
    except:
        print("Essa conta não existe!")
    
def tela():
    print()
    print("#"*60)
    print("Digite o número correspondente para realizar a operação:")
    print("1. Cadastrar conta:")
    print("2. Consultar saldo:")
    print("3. Crédito:")
    print("4. Débito:")
    print("5. Transferência:")
    print("#"*60)
    print()
    escolha = int(input())
    match escolha:
        case 1:
            crie_conta()
        case 2:
            consulta_saldo()
        case 3:
            credito()
        case 4:
            debito()
        case 5:
            transfere()
        case _:
            invalid_input()
    
    sleep(2)


while(True):
    tela()
