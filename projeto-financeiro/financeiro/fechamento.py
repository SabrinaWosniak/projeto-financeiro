class Fechamento:
    def __init__(self, lancamentos: list) -> None:
        if not lancamentos:
            raise ValueError("Não é possível fechar um período sem lançamentos")

        self._lancamentos = list(lancamentos)

    def quantidade_lancamentos(self) -> int:
        return len(self._lancamentos)

    def total_debitos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self._lancamentos
            if lancamento.tipo == "debito"
        )

    def total_creditos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self._lancamentos
            if lancamento.tipo == "credito"
        )

    def saldo(self) -> float:
        return self.total_creditos() - self.total_debitos()
