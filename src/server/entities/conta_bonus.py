from .conta import Conta;
from src.server.config import TipoCredito;


class ContaBonus(Conta):

  pontuacao = 10;
  
  def __init__(self, numero, saldo):
    super().__init__(numero, saldo)

  def credito(self, valor: float, tipo: TipoCredito):
    if(tipo == TipoCredito.DEPOSITO):
      self.pontuacao += (valor // 100);
    elif(tipo == TipoCredito.TRANSFERENCIA):
      self.pontuacao += (valor // 200);
      
    super().credito(valor, tipo);
