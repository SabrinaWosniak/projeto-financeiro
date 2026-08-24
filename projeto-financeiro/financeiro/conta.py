class Conta:
    def __init__(self, nome: str, saldo: float = 0.0) -> None:
        if not nome:
            raise ValueError("Nome da conta é obrigatório")

        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")

        self._saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")

        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")

        self._saldo -= valor
