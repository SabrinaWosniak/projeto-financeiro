# Sistema de Controle Financeiro Pessoal

Projeto feito para a disciplina de Programação Orientada a Objetos II.

## Classes do projeto

- Conta: controla uma conta e seu saldo.
- Categoria: serve para organizar os lançamentos.
- Lancamento: registra uma entrada ou saída de dinheiro.
- Fechamento: junta os lançamentos de um período.
- Conciliacao: verifica se os débitos e créditos estão iguais.
- Extrato: mostra um resumo dos fechamentos.

## Decisões do projeto

### Fechamento

O fechamento guarda uma cópia dos lançamentos.

Escolhi fazer assim para que mudanças na lista original não alterem o fechamento.

### Conciliacao

A conciliação foi feita como uma classe separada.

Escolhi assim porque ela tem uma função própria: verificar se os débitos e créditos estão iguais.

### Sem lançamentos

Um fechamento pode ser criado sem lançamentos. Nesse caso, os valores ficam zerados.

### Conciliação diferente

Se os débitos e créditos forem diferentes, a conciliação não é válida e o sistema mostra um erro.

## Testes

O projeto usa pytest.

Foram feitos testes para verificar os casos corretos e os casos de erro.

Atualmente, os 23 testes estão passando.

## Para executar todos os testes:

PYTHONPATH=. pytest
