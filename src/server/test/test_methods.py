import pytest
from server.entities import conta_bonus
import server.services.banco as banco_test
from config import *


class TestBanco:

    @pytest.fixture(autouse=True)
    def setup(self):
        #setUp

        yield 

        #tearDown 
        banco_test._contas = {}



    #<! Testes do credito >
    def test_credito_sucesso_adicao_comum(self):
        banco_test._criarConta(1,0)
        banco_test._credito(1,20)
        assert banco_test._getSaldo(1) == 20       
    
    def test_credito_erro_valor_negativo(self):
        banco_test._criarConta(1,0)
        with pytest.raises(Exception):
            banco_test._credito(1,-20)

    def test_credito_erro_conta_nao_existe(self):
        with pytest.raises(Exception):
            banco_test._credito(1,20)

    def test_credito_sucesso_conta_bonus(self):
        banco_test._criarContaBonus(1)
        banco_test._credito(1,100)
        bonus = banco_test._contas[1].pontuacao
        assert banco_test._getSaldo(1) == 100 
        assert bonus == 11



    #<! Testes do debito >
    def test_debito_1(self):
        banco_test._criarConta(1,20)
        banco_test._debito(1,20)
        assert banco_test._getSaldo(1) == 0
    
    def test_debito_2(self):
        banco_test._criarConta(1,20)
        with pytest.raises(Exception):
            banco_test._debito(1,40)
    
    def test_debito_3(self):
        with pytest.raises(Exception):
            banco_test._debito(1,40)
    
    def test_debito_4(self):
        banco_test._criarConta(1,20)
        with pytest.raises(Exception):
            banco_test._debito(1,-20)
    


    #<! Testes de transferencia >
    def test_transferencia_1(self):
        banco_test._criarConta(1,20)
        banco_test._criarConta(2,30)
        banco_test._transferir(20,1,2)
        assert banco_test._contas[1].saldo == 0 
        assert banco_test._contas[2].saldo == 50 
        
    
    def test_transferencia_2(self):
        banco_test._criarConta(1,20)
        banco_test._criarConta(2,30)
        with pytest.raises(Exception):
            banco_test._transferir(30,1,2)
    
    def test_transferencia_3(self):
        banco_test._criarConta(1,20)
        with pytest.raises(Exception):
            banco_test._transferir(20,1,2)
    
    def test_transferencia_4(self):
        banco_test._criarConta(1,20)
        banco_test._criarConta(2,30)
        with pytest.raises(Exception):
            banco_test._transferir(-20,1,2)
    


    #<! Testes de pegar infromação >
    def test_get_info_1(self):
        banco_test._criarConta(1,20)
        assert TipoConta.NORMAL == banco_test._get_info(1).tipo
    
    def test_get_info_2(self):
        banco_test._criarContaBonus(1)
        assert TipoConta.BONUS == banco_test._get_info(1).tipo
    
    def test_get_info_3(self):
        banco_test._criarContaPoupanca(1)
        assert TipoConta.POUPANCA == banco_test._get_info(1).tipo

    #<! Testes de rendimento de juros >

    def test_render_juros(self):
        banco_test._criarContaPoupanca(1)
        banco_test._criarContaPoupanca(2)
        banco_test._credito(1, 20)
        banco_test._credito(2, 30)
        banco_test._renda_juros(100)
        assert banco_test._getSaldo(1) == 40
        assert banco_test._getSaldo(2) == 60
    