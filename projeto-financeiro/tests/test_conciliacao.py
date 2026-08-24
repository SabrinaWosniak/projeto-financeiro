from datetime import date

import pytest

from financeiro.categoria import Categoria
from financeiro.conciliacao import Conciliacao
from financeiro.lancamento import Lancamento


class TestConciliacao:
    def setup_method(self) -> None:
        self.categoria = Categoria("Financeiro")

        self.debito1 = Lancamento(
            "Mercado", 100.0, date.today(), self.categoria, "debito"
        )

        self.debito2 = Lancamento(
            "Internet", 100.0, date.today(), self.categoria, "debito"
        )

        self.credito = Lancamento(
            "Salário", 200.0, date.today(), self.categoria, "credito"
        )

    def test_totais(self) -> None:
        conciliacao = Conciliacao([self.debito1, self.debito2], [self.credito])

        assert conciliacao.total_debitos() == 200.0
        assert conciliacao.total_creditos() == 200.0

    def test_conciliacao_bate(self) -> None:
        conciliacao = Conciliacao([self.debito1, self.debito2], [self.credito])

        assert conciliacao.esta_conciliada() is True

    def test_verificar_conciliacao(self) -> None:
        conciliacao = Conciliacao([self.debito1, self.debito2], [self.credito])

        conciliacao.verificar()

    def test_conciliacao_nao_bate(self) -> None:
        credito2 = Lancamento(
            "Freelance", 50.0, date.today(), self.categoria, "credito"
        )

        conciliacao = Conciliacao(
            [self.debito1, self.debito2], [self.credito, credito2]
        )

        assert conciliacao.esta_conciliada() is False

    def test_verificar_conciliacao_invalida(self) -> None:
        credito2 = Lancamento(
            "Freelance", 50.0, date.today(), self.categoria, "credito"
        )

        conciliacao = Conciliacao(
            [self.debito1, self.debito2], [self.credito, credito2]
        )

        with pytest.raises(ValueError):
            conciliacao.verificar()
