from src.server.config import TipoCredito;


class Conta:
  
  def __init__(self, numero : int, saldo : float):
        self.numero = numero
        self.saldo = saldo


  def credito(self, valor: float, tipo: TipoCredito):
    self.saldo+= valor;