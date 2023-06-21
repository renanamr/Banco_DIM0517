import pytest
import server.services.banco as banco_test
from config import *


class TestBanco:

    @pytest.fixture(autouse=True)
    def setup(self):
        #setUp

        yield 

        #tearDown 
        banco_test._contas = {}

    def test_debito_1(self):
        banco_test._criarConta(1,20)
        assert banco_test._debito(1,20)[1] == 200
        
    
    def test_debito_2(self):
        banco_test._criarConta(1,20)
        assert banco_test._debito(1,40)[1] == 400
    
    def test_debito_3(self):
        assert banco_test._debito(1,20)[1] == 400
    
    def test_debito_4(self):
        banco_test._criarConta(1,20)
        assert banco_test._debito(1,-20)[1] == 400
    
    def test_transferencia_1(self):
        banco_test._criarConta(1,20)
        banco_test._criarConta(2,30)
        assert banco_test._transferir(20,1,2)[1] == 200
        
    
    def test_transferencia_2(self):
        banco_test._criarConta(1,20)
        banco_test._criarConta(2,30)
        assert banco_test._transferir(30,1,2)[1] == 400
    
    def test_transferencia_3(self):
        banco_test._criarConta(1,20)
        assert banco_test._transferir(20,1,2)[1] == 400
    
    def test_transferencia_4(self):
        banco_test._criarConta(1,20)
        banco_test._criarConta(2,30)
        assert banco_test._transferir(-20,1,2)[1] == 400
    
    def test_get_info_1(self):
        banco_test._criarConta(1,20)
        assert "TipoConta.NORMAL" in banco_test._get_info(1)[0]
    
    def test_get_info_2(self):
        banco_test._criarContaBonus(1)
        assert "TipoConta.BONUS" in banco_test._get_info(1)[0]
    
    def test_get_info_3(self):
        banco_test._criarContaPoupanca(1)
        assert "TipoConta.POUPANCA" in banco_test._get_info(1)[0]
    
    def test_get_info_4(self):
        assert banco_test._get_info(1)[1] == 400