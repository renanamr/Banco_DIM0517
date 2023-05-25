from enum import Enum

class TipoCredito(Enum):
  DEPOSITO = 1
  TRANSFERENCIA = 2


class TipoConta(Enum):
  NORMAL = 1
  BONUS = 2
  POUPANCA = 3