from models import Usuario

tecnico = Usuario("Técnico de Manutenção", "Tecnico", "Técnico")
tecnico.definir_senha("tec123")
print(tecnico.login, "-", tecnico.perfil)

print("OK: senha certa aceita" if tecnico.verificar_senha("tec123") else "ERRO")
print("OK: senha errada recusada" if not tecnico.verificar_senha("errada") else "ERRO")
print("OK: senha guardada criptografada" if "tec123" not in tecnico.senha_hash else "ERRO")

professor = Usuario("Professor Exemplo", "professor", "Professor")
print("OK: professor pode abrir chamado" if professor.pode("abrir_chamado") else "ERRO")
print("OK: professor não altera status" if not professor.pode("alterar_status") else "ERRO")
print("OK: técnico altera status" if tecnico.pode("alterar_status") else "ERRO")
print("OK: técnico não cadastra equipamento" if not tecnico.pode("cadastrar_equipamento") else "ERRO")

try:
    Usuario("Aluno", "aluno", "Aluno")
except ValueError as e:
    print("OK:", e)

try:
    tecnico.definir_senha("123")
except ValueError as e:
    print("OK:", e)

try:
    tecnico.senha_hash = "trocada"
except AttributeError:
    print("OK: não deixou trocar a senha direto")
