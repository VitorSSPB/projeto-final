import repositorio
from models import Chamado, Equipamento

print("Equipamentos cadastrados:")
for e in repositorio.listar_equipamentos():
    print(" ", e.id, e)

repositorio.salvar_chamado(Chamado(1, "Computador travando ao abrir o navegador."))
print("OK: chamado salvo")

print("Equipamentos inoperantes:")
for linha in repositorio.listar_inoperantes():
    print(" ", linha["patrimonio"], "-", linha["descricao_problema"], "-", linha["status_resolucao"])

try:
    repositorio.salvar_equipamento(Equipamento("PAT-0001", "Laboratório 1", "Mouse"))
except ValueError as erro:
    print("OK:", erro)
