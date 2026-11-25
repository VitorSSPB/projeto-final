import repositorio

chamado = repositorio.buscar_chamado(1)
print("Chamado 1:", chamado.descricao_problema, "-", chamado.status_resolucao)

repositorio.atualizar_status(1, "Em andamento")
print("OK: status alterado para", repositorio.buscar_chamado(1).status_resolucao)

try:
    repositorio.atualizar_status(1, "Quebrado")
except ValueError as erro:
    print("OK:", erro)

try:
    repositorio.atualizar_status(9999, "Resolvido")
except ValueError as erro:
    print("OK:", erro)

equipamento = repositorio.buscar_equipamento(3)
print("Histórico do", equipamento)
for linha in repositorio.historico_equipamento(3):
    print(" ", linha["data"], "-", linha["descricao_problema"], "-", linha["status_resolucao"])
