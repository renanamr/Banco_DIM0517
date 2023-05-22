from typing import Dict;
from src.server.entities import Conta;


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
  

  def saldoConta(self, numero : int) -> float:
    if(numero in self._contas):
      conta = self._contas[numero];
      return conta.saldo
    else:
      raise Exception("Conta não existe!")
    
  def credito(self, numero : int, valor : float):
    if valor < 0:
      raise Exception("Não é possível creditar valores negativos!")
    if(numero in self._contas):
      conta = self._contas[numero] 
      conta.saldo += valor
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
      self.credito(destino,valor)
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

