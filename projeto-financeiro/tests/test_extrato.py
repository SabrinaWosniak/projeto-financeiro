from datetime import date

from financeiro.categoria import Categoria
from financeiro.extrato import Extrato
from financeiro.fechamento import Fechamento
from financeiro.lancamento import Lancamento


class TestExtrato:
    def setup_method(self) -> None:
        self.categoria = Categoria("Financeiro")

        self.debito = Lancamento(
            "Mercado", 100.0, date.today(), self.categoria, "debito"
        )

        self.credito = Lancamento(
            "Salário", 500.0, date.today(), self.categoria, "credito"
        )

    def test_criar_extrato(self) -> None:
        fechamento = Fechamento([self.debito, self.credito])

        extrato = Extrato([fechamento])

        assert extrato.quantidade_lancamentos() == 2

    def test_total_debitos(self) -> None:
        fechamento = Fechamento([self.debito, self.credito])

        extrato = Extrato([fechamento])

        assert extrato.total_debitos() == 100.0

    def test_total_creditos(self) -> None:
        fechamento = Fechamento([self.debito, self.credito])

        extrato = Extrato([fechamento])

        assert extrato.total_creditos() == 500.0

    def test_saldo_final(self) -> None:
        fechamento = Fechamento([self.debito, self.credito])

        extrato = Extrato([fechamento])

        assert extrato.saldo_final() == 400.0
