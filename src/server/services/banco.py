from typing import Dict;
from src.server.entities import Conta, ContaBonus;
from src.server.config import TipoCredito;


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


  def saldoConta(self, numero : int) -> float:
    if(numero in self._contas):
      conta = self._contas[numero];
      return conta.saldo
    else:
      raise Exception("Conta não existe!")
    
  def credito(self, numero : int, valor : float, tipo=TipoCredito.DEPOSITO):
    if(numero in self._contas):
      conta = self._contas[numero] 
      conta.credito(valor, tipo)
      return True
    else:
      raise Exception("Conta não existe!")
    
  def transferir(self, origem : int, destino : int, valor : float) -> float:
    if(origem in self._contas and destino in self._contas):
      self.debito(origem,valor)
      self.credito(destino,valor, TipoCredito.TRANSFERENCIA)
      return True
    else:
      raise Exception("Conta não existe!")
  
  def debito(self,numero: int, valor:float):
    return self.credito(numero,-valor)

