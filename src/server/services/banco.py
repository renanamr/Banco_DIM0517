from typing import Dict;
from src.server.entities import Conta, ContaBonus,ContaPoupanca;
from src.server.config import TipoCredito,TipoConta;


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if (cls not in cls._instances):
            instance = super().__call__(*args, **kwargs);
            cls._instances[cls] = instance;
        return cls._instances[cls];


class Banco(metaclass=SingletonMeta):

  _contas: Dict[int, Conta] = {}
  
  def criarConta(self, numero : int) -> bool:
    if(numero in self._contas):
      return False
    else:
      self._contas[numero] = Conta(numero, 0.0);
      return True

  def criarContaBonus(self, numero : int) -> bool:
    if(numero in self._contas):
      return False
    else:
      self._contas[numero] = ContaBonus(numero, 0.0);
      return True  
  
  def criarContaPoupanca(self, numero : int, saldo : float) -> bool:
    if(numero in self._contas):
      return False
    else:
      self._contas[numero] = ContaPoupanca(numero, saldo);
      return True

  def exists(self,numero:int) -> bool:
    return numero in self._contas
  
  def getTipo(self,numero:int):
    if(self.exists(numero)):
      return self._contas[numero].tipo
    else:
      raise Exception("Conta não existe!")

  def renda_juros(self,numero:int,val:float):
    if not self.exists(numero):
        raise Exception("Essa conta não existe!")
        return
    
    if self.getTipo(numero)!=TipoConta.POUPANCA:
        raise Exception("Essa conta não é poupança!")
        return
    
    self._contas[numero].renda_juros(val)
    


  def saldoConta(self, numero : int) -> float:
    if(numero in self._contas):
      conta = self._contas[numero];
      return conta.saldo
    else:
      raise Exception("Conta não existe!")
    
  def credito(self, numero : int, valor : float, tipo=TipoCredito.DEPOSITO):
    if valor < 0:
      raise Exception("Não é possível creditar valores negativos!")
    if(numero in self._contas):
      conta = self._contas[numero] 
      conta.credito(valor, tipo)
      return True
    else:
      raise Exception("Conta não existe!")
    
  def transferir(self, origem : int, destino : int, valor : float) -> float:
    if valor < 0:
      raise Exception("Não é possível transferir valores negativos!")
    if(origem in self._contas and destino in self._contas):
      if self._contas[origem].saldo < valor:
        raise Exception("Saldo insuficiente!")
      self.debito(origem,valor)
      self.credito(destino,valor, TipoCredito.TRANSFERENCIA)
      return True
    else:
      raise Exception("Conta não existe!")
  
  def debito(self,numero: int, valor:float):
    if valor < 0:
      raise Exception("Não é possível debitar valores negativos!")
    if self._contas[numero].saldo < valor:
      raise Exception("Saldo insuficiente!")

    self._contas[numero].saldo -= valor
    return True

