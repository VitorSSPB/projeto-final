from models import Equipamento, Chamado

pc = Equipamento("pat-0105", "Laboratório 2", "Computador")
print(pc)

c = Chamado(3, "PC 05 do laboratório 2 está sem internet.")
print(c.status_resolucao)
c.alterar_status("Em andamento")
print(c.status_resolucao)

try:
    c.data = "ontem"
except AttributeError:
    print("OK: não deixou alterar a data")

try:
    Chamado(3, "curto")
except ValueError as e:
    print("OK:", e)

try:
    c.alterar_status("Quebrado")
except ValueError as e:
    print("OK:", e)

try:
    Chamado("abc", "Equipamento com código inválido.")
except ValueError as e:
    print("OK:", e)

try:
    c.alterar_status("Resolvido")
    c.alterar_status("Aberto")
except ValueError as e:
    print("OK:", e)
