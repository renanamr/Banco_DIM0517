from services.banco import *

import time

def operacao_banco():
    print("Bem vindo ao app do Banco DIM0517")
    print("Escolha umas das opções abaixo: ")
    print("(1) Cadastrar Conta Comum")
    print("(2) Cadastrar Conta Bônus")
    print("(3) Cadastrar Conta Poupança")
    print("(4) Consultar Saldo")
    print("(5) Crédito (Adicionar fundos)")
    print("(6) Débito (Subtrair valor)")
    print("(7) Transferência")
    print("(8) Render Juros")
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
            crie_conta_poupanca()
        case '4':
            consulta_saldo()         
        case '5':
            credito()
        case '6':
            debito()
        case '7':
            transferir()
        case '8':
            renda_juros()
        case _:
            invalid_input()
    
    print("\n"*2)

    time.sleep(2)

if __name__ == '__main__':
    while(True):
        operacao_banco()