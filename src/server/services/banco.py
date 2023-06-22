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
  ans = {}
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
  ans['status'] = 'Ok'
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
  ans = {}
  juros = float(request.json["juros"])
  try:
    _renda_juros(juros)
  except Exception as e:
    print(e, file=sys.stderr) 
    return str(e), 400
  ans['status'] = 'Ok'
  return ans, 200

def _renda_juros(juros:float):
  for numero in _contas:
    if getTipo(numero)==TipoConta.POUPANCA:
        _contas[numero].renda_juros(juros)
    
  
  




def saldoConta(numero : int) -> float:
  if(numero in _contas):
    conta = _contas[numero];
    return conta.saldo
  else:
    raise Exception("Conta não existe!")



@operations.put("/<numero>/credito")
def credito(numero : int):
  ans = {}
  valor = float(request.json["valor"])
  try:
    _credito(int(numero), valor)
  except Exception as e:
    print(e, file=sys.stderr) 
    return str(e), 400
  ans['status'] = 'Ok'
  return ans, 200

def _credito(numero : int, valor : float, tipo=TipoCredito.DEPOSITO):
  if valor < 0:
    raise Exception("Não é possível creditar valores negativos!")
  if(numero in _contas):
    conta = _contas[numero] 
    conta.credito(valor, tipo)
  else:
    raise Exception("Conta não existe!")
  



@operations.put("/transferencia")
def transferir():
  ans = {}
  valor = float(request.json["valor"])
  origem = int(request.json["origem"])
  destino = int(request.json["destino"])
  try:
    _transferir(valor,origem,destino)
  except Exception as e:
    print(e, file=sys.stderr) 
    return str(e), 400
  ans['status'] = 'Ok'
  return ans, 200

def _transferir(valor:int,origem:int,destino:int):
  if valor < 0:
    raise Exception("Não é possível transferir valores negativos!")
  if(origem in _contas and destino in _contas):
    if _contas[origem].saldo < valor:
      raise Exception("Saldo insuficiente!")
    _debito(origem,valor)
    _credito(destino,valor, TipoCredito.TRANSFERENCIA)
  else:
    raise("Conta não existe!")
  




@operations.put("/<numero>/debito")
def debito(numero : int):
  ans = {}
  valor = float(request.json["valor"])
  try:
    _debito(int(numero), valor)
  except Exception as e:
    print(e, file=sys.stderr) 
    return str(e), 400

  ans['status'] = 'Ok'
  return ans, 200

def _debito(numero:int, valor:float):
  if(not exists(numero)):
    raise Exception("Conta inexistente!")
  if valor < 0:
    raise Exception("Não é possível debitar valores negativos!")
  if _contas[numero].saldo < valor:
    raise Exception("Saldo insuficiente!")

  _contas[numero].saldo -= valor




@operations.get("/<numero>/informacoes")
def get_info(numero : int):
  ans = {}
  try:
    conta_info = _get_info(int(numero))
    ans['saldo'] = conta_info.saldo 
    match conta_info.tipo:
      case TipoConta.NORMAL:
        ans['tipo'] = 'normal'
      case TipoConta.BONUS:
        ans['tipo'] = 'bonus'
      case TipoConta.POUPANCA:
        ans['tipo'] = 'poupanca'
      case _: 
        raise Exception('Tipo de conta indefinido')
  except Exception as e:
    print(e, file=sys.stderr) 
    return "Conta inválida!", 400

  return ans, 200

def _get_info(numero:int):
  conta_info = _contas[numero]
  return conta_info
