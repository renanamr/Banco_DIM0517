from .conta import Conta;
from config import TipoCredito,TipoConta;


class ContaBonus(Conta):

  pontuacao = 10;
  
  def __init__(self, numero, saldo):
    self.tipo =  TipoConta.BONUS
    super().__init__(numero, saldo)
    

  def credito(self, valor: float, tipo: TipoCredito):
    if(tipo == TipoCredito.DEPOSITO):
      self.pontuacao += (valor // 100);
    elif(tipo == TipoCredito.TRANSFERENCIA):
      self.pontuacao += (valor // 150);
      
    super().credito(valor, tipo);
