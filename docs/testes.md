# Roteiro de Testes - Controle de Equipamentos de Laboratório

Responsável: Rodrigo
Data da execução: 25/11/2026
Versão testada: Entrega 3 (chamado gravado no banco, status no painel e histórico)

## Como os testes foram feitos

Cada teste foi executado no sistema rodando pelo Flask (`python app.py`), com o banco carregado pelos scripts `sql/banco.sql` e `sql/dados_teste.sql`. Para cada caso, foi feita a ação descrita e comparado o resultado com o esperado.

## Casos de teste

| Nº | O que fazer | Resultado esperado | Resultado |
|----|-------------|--------------------|-----------|
| T01 | Abrir chamado escolhendo um equipamento e escrevendo uma descrição normal | Mensagem de sucesso e chamado aparece no painel | OK |
| T02 | Tentar enviar o chamado sem escolher o equipamento | O sistema não deixa enviar | OK |
| T03 | Enviar chamado com descrição de menos de 10 caracteres | Não deixa enviar e mostra o aviso; nada é gravado | OK |
| T04 | No painel, mudar o status de um chamado para "Em andamento" | Status muda no painel e aparece "Status atualizado!" | OK |
| T05 | No painel, mudar o status do chamado para "Resolvido" | O chamado sai do painel | OK |
| T06 | Abrir o histórico do equipamento do chamado resolvido | O chamado aparece no histórico como "Resolvido" | OK |
| T07 | Cadastrar um equipamento novo | Ele aparece na lista do formulário de abrir chamado | OK |
| T08 | Cadastrar um patrimônio que já existe | Mostra o aviso e não duplica | OK |
| T09 | Tentar cadastrar com o patrimônio vazio | O sistema não deixa enviar | OK |
| T10 | Abrir 2 chamados para a mesma máquina | Os dois aparecem no painel | OK |
| T11 | Clicar em todos os links do menu | Todas as páginas abrem | OK |

**Resumo:** 11 testes executados, 11 aprovados, 0 reprovados.

## Problemas encontrados

Os casos de teste passaram, mas durante a execução foram observados dois pontos de melhoria, registrados como cartões com a etiqueta "bug" no Trello:

| Nº | Problema | Gravidade | Responsável |
|----|----------|-----------|-------------|
| B01 | As mensagens de erro (descrição curta, patrimônio repetido, equipamento não encontrado) aparecem com a mesma faixa verde das mensagens de sucesso | Baixa (visual) | Vitor |
| B02 | Se o formulário for enviado com o código de um equipamento que não existe (alterando a página pelo navegador), o banco recusa e o sistema mostra uma página de erro em vez de um aviso | Média | Lucas |
