from datetime import date


class Lancamento:

    def __init__(
        self,
        descricao: str,
        valor: float,
        data: date,
        categoria,
        tipo: str
    ) -> None:

        if not descricao:
            raise ValueError("Descrição é obrigatória")

        if valor <= 0:
            raise ValueError("Valor deve ser positivo")

        if tipo not in ["debito", "credito"]:
            raise ValueError("Tipo deve ser 'debito' ou 'credito'")

        self._descricao = descricao
        self._valor = valor
        self._data = data
        self._categoria = categoria
        self._tipo = tipo

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def data(self) -> date:
        return self._data

    @property
    def categoria(self):
        return self._categoria

    @property
    def tipo(self) -> str:
        return self._tipo