from typing import Dict;
from entities import Conta, ContaBonus,ContaPoupanca;
from config import TipoCredito,TipoConta;
import json, sys
from flask import Blueprint,request,jsonify

operations = Blueprint("operations_blueprint",__name__,url_prefix = "/banco/conta")



#Singleton removido
_contas: Dict[int, Conta] = {}

@operations.post("/")
def criarConta():
  numero = int(request.json['numero'])
  tipo = request.json['tipo']

  match tipo:
    case 'bonus':
      if not _criarContaBonus(numero):
        return('Conta já existe', 400)
    case 'poupanca':
      if not _criarContaPoupanca(numero):
        return('Conta já existe', 400)
    case 'normal':
      saldo = float(request.json['saldo'])
      if not _criarConta(numero, saldo):
        return ('Conta já existe', 400)
    case _:
      return('Tipo inválido', 400)
  
  return ('Ok', 200)

def _criarConta(numero : int, saldo: float) -> bool:
  if(numero in _contas):
    return False
  else:
    _contas[numero] = Conta(numero, 0.0)
    _credito(numero, saldo)
    return True

def _criarContaBonus(numero : int) -> bool:
  if(numero in _contas):
    return False
  else:
    _contas[numero] = ContaBonus(numero, 0.0);
    return True  

def _criarContaPoupanca(numero : int) -> bool:
  if(numero in _contas):
    return False
  else:
    _contas[numero] = ContaPoupanca(numero, 0.0);
    return True
  
@operations.get("/<numero>/saldo")
def getSaldo(numero : int):
  try:
    saldo = _getSaldo(int(numero))
  except:
    return "Numero inválido", 400
  
  ans = {"saldo": saldo}
  return ans, 200

def _getSaldo(numero : int):
  conta = _contas[numero]
  return conta.saldo

def exists(numero:int) -> bool:
  return numero in _contas

def getTipo(numero:int):
  if(exists(numero)):
    return _contas[numero].tipo
  else:
    raise Exception("Conta não existe!")



@operations.put("/rendimento")
def renda_juros():
  numero = int(request.json["numero"])
  valor = float(request.json["valor"])
  return _renda_juros(numero, valor)

def _renda_juros(numero:int,valor:float):
  if not exists(numero):
      return "Conta não existe!",400
  
  if getTipo(numero)!=TipoConta.POUPANCA:
      return "Essa conta não é poupança!",400
  
  _contas[numero].renda_juros(valor)
  return "OK",200
  




def saldoConta(numero : int) -> float:
  if(numero in _contas):
    conta = _contas[numero];
    return conta.saldo
  else:
    raise Exception("Conta não existe!")



@operations.put("/<numero>/credito")
def credito(numero : int):
  valor = float(request.json["valor"])
  return _credito(numero,valor)

def _credito(numero : int, valor : float, tipo=TipoCredito.DEPOSITO):
  if valor < 0:
    return "Não é possível creditar valores negativos!",400
  if(numero in _contas):
    conta = _contas[numero] 
    conta.credito(valor, tipo)
    return "OK",200
  else:
    return "Conta não existe!",400
  



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
