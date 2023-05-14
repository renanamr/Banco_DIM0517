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
    
  def transferir(self, origem, destino, valor : float) -> float:
    if(origem in self._contas and destino in self._contas):
      conta_origem = self._contas[origem]
      conta_destino =  self._contas[destino]
      conta_origem -= valor
      conta_destino += valor
      return True
    else:
      raise Exception("Conta não existe!")
    
  def credito(self, numero : int, valor : float):
    if(numero in self._contas):
      conta = self._contas[numero] 
      conta.saldo += valor
      return True
    else:
      raise Exception("Conta não existe!")
    
  def transferir(self, origem, destino, valor : float) -> float:
    if(origem in self._contas and destino in self._contas):
      conta_origem = self._contas[origem]
      conta_destino =  self._contas[destino]
      conta_origem -= valor
      conta_destino += valor
      return True
    else:
      raise Exception("Conta não existe!")

