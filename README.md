# Controle de Equipamentos de Laboratório - ETEC

Sistema interno para a ETEC registrar chamados de defeito em computadores e
periféricos dos laboratórios e organizar a fila de manutenção, substituindo as
anotações em papel.

## Objetivo

Desenvolver um sistema web interno para a ETEC que permita ao professor abrir
chamados técnicos informando o equipamento com defeito e o problema, e ao
técnico de manutenção visualizar os equipamentos inoperantes e acompanhar a
fila de manutenção, mantendo o histórico no banco de dados MySQL.

## Integrantes

| Integrante     | Função                                     |
|----------------|--------------------------------------------|
| Vitor Barbosa  | Tech Lead - front-end (HTML/CSS) e Flask   |
| Lucas          | Back-end - Python e MySQL                  |
| Pedro          | Documentação                               |
| Rodrigo        | Usuários, cronograma, dados e testes       |

## Tecnologias

- Python 3
- Flask
- MySQL + mysql-connector-python
- HTML e CSS
- Git/GitHub, Trello e OneDrive

## Estrutura do projeto

```
projeto-final-pa/
|-- templates/   -> páginas HTML
|-- static/      -> CSS
|-- sql/         -> scripts do banco de dados
|-- docs/        -> documentação (requisitos, diagramas, manual)
`-- README.md
```

## Andamento

| Entrega | Data  | Conteúdo                                              | Situação         |
|---------|-------|-------------------------------------------------------|------------------|
| 1       | 06/11 | Planejamento, telas em HTML, banco e classes           | Em andamento     |
| 2       | 13/11 | Flask, conexão com o banco, README e diagramas         | A fazer          |
| 3       | 20/11 | Integração (formulário grava no banco) e testes        | A fazer          |
| 4       | 27/11 | Histórico, correções, documentação final e ensaios     | A fazer          |
