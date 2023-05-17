from .conta import Conta;


class ContaBonus(Conta):

  pontuacao = 10;
  
  def __init__(self, numero, saldo):
    super().__init__(numero, saldo)
