import pytest

from financeiro.conta import Conta


class TestConta:
    def test_criar_conta(self) -> None:
        conta = Conta("Nubank", 1000.0)

        assert conta.nome == "Nubank"
        assert conta.saldo == 1000.0

    def test_depositar(self) -> None:
        conta = Conta("Nubank", 1000.0)

        conta.depositar(500.0)

        assert conta.saldo == 1500.0

    def test_sacar(self) -> None:
        conta = Conta("Nubank", 1000.0)

        conta.sacar(300.0)

        assert conta.saldo == 700.0

    def test_nao_sacar_valor_maior_que_saldo(self) -> None:
        conta = Conta("Nubank", 1000.0)

        with pytest.raises(ValueError):
            conta.sacar(1500.0)
