from services.banco import *

import time

def operacao_banco():
    print("Bem vindo ao app do Banco DIM0517")
    print("Escolha umas das opções abaixo: ")
    print("(1) Cadastrar Conta Comum")
    print("(2) Cadastrar Conta Bônus")
    print("(3) Consultar Saldo")
    print("(4) Crédito (Adicionar fundos)")
    print("(5) Débito (Subtrair valor)")
    print("(6) Transferência")
    print("(0) Sair")

    opcao = input("Digite aqui sua opcao:")

    match opcao:
        case '0':
            exit(0)
        case '1':
            crie_conta()
        case '2':
            crie_conta_bonus()
        case '3':
            consulta_saldo()         
        case '4':
            credito()
        case '5':
            debito()
        case '6':
            transferir()
        case _:
            invalid_input()
    
    print("\n"*2)

    time.sleep(2)

if __name__ == '__main__':
    while(True):
        operacao_banco()