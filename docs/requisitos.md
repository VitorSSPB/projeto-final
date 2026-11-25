# Requisitos - Controle de Equipamentos de Laboratório

## Requisitos funcionais

| Código | Requisito | Prioridade | Situação |
|---|---|---|---|
| RF01 | O sistema deve permitir abrir um chamado informando o equipamento e a descrição do problema. | Obrigatório | Feito |
| RF02 | O sistema deve registrar automaticamente a data/hora de abertura e o status "Aberto". | Obrigatório | Feito |
| RF03 | O sistema deve exibir um painel com os equipamentos inoperantes (chamados não resolvidos). | Obrigatório | Feito |
| RF04 | O técnico deve poder alterar o status do chamado (Aberto -> Em andamento -> Resolvido). | Importante | Feito |
| RF05 | O sistema deve permitir cadastrar equipamentos (patrimônio, laboratório, tipo). | Importante | Feito |
| RF06 | O sistema deve mostrar o histórico de chamados de um equipamento. | Desejável | Feito |
| RF07 | O sistema deve exigir login e liberar cada função conforme o perfil (Professor, Técnico ou Administrador). | Importante | Feito |
| RF08 | O administrador deve poder cadastrar novos usuários. | Desejável | Feito |

## Requisitos não funcionais

| Código | Requisito | Situação |
|---|---|---|
| RNF01 | Os dados devem ser armazenados em banco de dados MySQL. | Feito |
| RNF02 | A lógica deve ser escrita em Python, usando classes com atributos privados e validação (encapsulamento). | Feito |
| RNF03 | O sistema deve funcionar pelo navegador dos computadores do laboratório, sem instalar nada no cliente. | Feito |
| RNF04 | A interface deve ser simples: abrir um chamado em menos de 1 minuto. | Feito |
| RNF05 | O código deve ser versionado no GitHub com colaboração de todos os integrantes. | Feito |
| RNF06 | O sistema deve validar os dados e mostrar mensagens de erro claras ao usuário. | Feito |
| RNF07 | As senhas devem ser guardadas criptografadas no banco de dados. | Feito |

## Funcionalidades mínimas (MVP)

**Obrigatório:** RF01, RF02, RF03 e RNF02 (abrir chamado, painel de inoperantes e encapsulamento).

**Depois do mínimo:** RF04 e RF05.

**Extra, se der tempo:** RF06.

**Extras incluídos na Entrega 4:** RF07, RF08 e RNF07 (login com perfis e senhas criptografadas).

**Situação atual:** todos os requisitos funcionais e não funcionais foram implementados até a Entrega 4.
