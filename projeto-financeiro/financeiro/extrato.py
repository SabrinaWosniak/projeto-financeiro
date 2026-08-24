class Extrato:
    def __init__(self, fechamentos: list) -> None:
        self._fechamentos = list(fechamentos)

    def quantidade_lancamentos(self) -> int:
        return sum(
            fechamento.quantidade_lancamentos() for fechamento in self._fechamentos
        )

    def total_debitos(self) -> float:
        return sum(fechamento.total_debitos() for fechamento in self._fechamentos)

    def total_creditos(self) -> float:
        return sum(fechamento.total_creditos() for fechamento in self._fechamentos)

    def saldo_final(self) -> float:
        return self.total_creditos() - self.total_debitos()
