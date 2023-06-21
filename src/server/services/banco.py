from typing import Dict;
from entities import Conta, ContaBonus,ContaPoupanca;
from config import TipoCredito,TipoConta;

from flask import Blueprint,request,jsonify

operations = Blueprint("operations_blueprint",__name__,url_prefix = "/banco/conta")



#Singleton removido
_contas: Dict[int, Conta] = {}

def criarConta(numero : int, saldo: float) -> bool:
  if(numero in _contas):
    return False
  else:
    _contas[numero] = Conta(numero, 0.0);
    credito(numero, saldo)
    return True

def criarContaBonus(numero : int) -> bool:
  if(numero in _contas):
    return False
  else:
    _contas[numero] = ContaBonus(numero, 0.0);
    return True  

def criarContaPoupanca(numero : int) -> bool:
  if(numero in _contas):
    return False
  else:
    _contas[numero] = ContaPoupanca(numero, 0.0);
    return True

def exists(numero:int) -> bool:
  return numero in _contas

def getTipo(numero:int):
  if(exists(numero)):
    return _contas[numero].tipo
  else:
    raise Exception("Conta não existe!")

def renda_juros(numero:int,val:float):
  if not exists(numero):
      raise Exception("Essa conta não existe!")
      return
  
  if getTipo(numero)!=TipoConta.POUPANCA:
      raise Exception("Essa conta não é poupança!")
      return
  
  _contas[numero].renda_juros(val)
  


def saldoConta(numero : int) -> float:
  if(numero in _contas):
    conta = _contas[numero];
    return conta.saldo
  else:
    raise Exception("Conta não existe!")
  
def credito(numero : int, valor : float, tipo=TipoCredito.DEPOSITO):
  if valor < 0:
    raise Exception("Não é possível creditar valores negativos!")
  if(numero in _contas):
    conta = _contas[numero] 
    conta.credito(valor, tipo)
    return True
  else:
    raise Exception("Conta não existe!")

@operations.put("/transferencia")
def transferir():
  valor = request.json["valor"]
  origem = request.json["origem"]
  destino = request.json["destino"]
  return _transferir(valor,origem,destino)

def _transferir(valor:int,origem:int,destino:int):
  if valor < 0:
    return "Não é possível transferir valores negativos!",400
  if(origem in _contas and destino in _contas):
    if _contas[origem].saldo < valor:
      return "Saldo insuficiente!",400
    _debito(origem,valor)
    credito(destino,valor, TipoCredito.TRANSFERENCIA)
    return "OK",200
  else:
    return "Conta não existe!",400
  

@operations.put("/<numero>/debito")
def debito(numero : int):
  valor = float(request.json["valor"])
  return _debito(numero,valor)

def _debito(numero:int, valor:float):
  if(not exists(numero)):
    return "Essa conta não existe",400
  if valor < 0:
    return "Não é possível debitar valores negativos!",400
  if _contas[numero].saldo < valor:
    return "Saldo insuficiente!",400

  _contas[numero].saldo -= valor
  return "OK",200

@operations.get("/<numero>/informacoes")
def get_info(numero:int):
  return _get_info(numero)

def _get_info(numero:int):
  if(not exists(numero)):
    return "Essa conta não existe",400
  
  conta_info = _contas[numero]
  info = "Tipo = " + str(conta_info.tipo) + ", Saldo = " + str(conta_info.saldo)
  return info,200
