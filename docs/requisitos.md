# Requisitos - Controle de Equipamentos de Laboratório

## Requisitos funcionais

| Código | Requisito | Prioridade |
|--------|-----------|------------|
| RF01 | O sistema deve permitir abrir um chamado informando o equipamento e a descrição do problema. | Obrigatório |
| RF02 | O sistema deve registrar automaticamente a data/hora de abertura e o status "Aberto". | Obrigatório |
| RF03 | O sistema deve exibir um painel com os equipamentos inoperantes (chamados não resolvidos). | Obrigatório |
| RF04 | O técnico deve poder alterar o status do chamado (Aberto → Em andamento → Resolvido). | Importante |
| RF05 | O sistema deve permitir cadastrar equipamentos (patrimônio, laboratório, tipo). | Importante |
| RF06 | O sistema deve mostrar o histórico de chamados de um equipamento. | Desejável |

## Requisitos não funcionais

| Código | Requisito |
|--------|-----------|
| RNF01 | Os dados devem ser armazenados em banco de dados MySQL. |
| RNF02 | A lógica deve ser escrita em Python, usando classes com atributos privados e validação (encapsulamento). |
| RNF03 | O sistema deve funcionar pelo navegador dos computadores do laboratório, sem instalar nada no cliente. |
| RNF04 | A interface deve ser simples: abrir um chamado em menos de 1 minuto. |
| RNF05 | O código deve ser versionado no GitHub com colaboração de todos os integrantes. |
| RNF06 | O sistema deve validar os dados e mostrar mensagens de erro claras ao usuário. |

## Funcionalidades mínimas (MVP)

**Obrigatório:** RF01, RF02, RF03 e RNF02 (abrir chamado, painel de inoperantes e encapsulamento).

**Depois do mínimo:** RF04 e RF05.

**Extra, se der tempo:** RF06.
