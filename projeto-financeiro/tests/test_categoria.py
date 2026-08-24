import pytest

from financeiro.categoria import Categoria


class TestCategoria:
    def test_criar_categoria(self) -> None:
        categoria = Categoria("Alimentação")

        assert categoria.nome == "Alimentação"

    def test_categoria_sem_nome(self) -> None:
        with pytest.raises(ValueError):
            Categoria("")
