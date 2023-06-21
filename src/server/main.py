from flask import Flask
from .services.banco import Banco
app = Flask(__name__)


#app.register_blueprint(routes_app)

# @app.get("/debito/<numero:int>/<valor:float>")
# def debito():
#     banco = Banco()
#     numero = int(input("Digite o numero da conta:"))
#     valor = float(input("Digite o valor a ser debitado:"))
#     if banco.debito(numero, valor):
#         print("Foram retirados " + str(valor) + " a conta " + str(numero))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
