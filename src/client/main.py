from services.banco import *


if __name__ == '__main__':
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
            exit(0)
        case '2':
            exit(0)            
        case '3':
            credito()
        case '4':
            exit(0)
        case '5':
            exit(0)
        case _:
            raise Exception("Opção inválida")