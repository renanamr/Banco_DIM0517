from typing import Dict;
from entities import Conta;


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
      return False;
    else:
      self._contas[numero] = Conta(numero, 0.0);
      return True;

