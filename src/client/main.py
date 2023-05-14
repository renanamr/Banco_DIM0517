from services.banco import *

import time

def operacao_banco():
    print("Bem vindo ao app do Banco DIM0517")
    print("Escolha umas das opções abaixo: ")
    print("(1) Cadastrar Conta")
    print("(2) Consultar Saldo")
    print("(3) Crédito (Adicionar fundos)")
    print("(4) Débito (Subtrair valor)")
    print("(5) Transferência")
    print("(0) Sair")

    opcao = input("Digite aqui sua opcao:")

    match opcao:
        case '0':
            exit(0)
        case '1':
            crie_conta()
        case '2':
            consulta_saldo()         
        case '3':
            credito()
        case '4':
            debito()
        case '5':
            transferir()
        case _:
            invalid_input()
    
    print("\n"*2)

    time.sleep(2)

if __name__ == '__main__':
    while(True):
        operacao_banco()