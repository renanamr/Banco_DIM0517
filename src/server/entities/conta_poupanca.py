from .conta import Conta;
from config import TipoConta;


class ContaPoupanca(Conta):

  pontuacao = 10;
  
  def __init__(self, numero, saldo):
    self.tipo =  TipoConta.POUPANCA
    super().__init__(numero, saldo)

  def renda_juros(self, juros: float):
    juros = 1 + juros/100
    self.saldo*=juros