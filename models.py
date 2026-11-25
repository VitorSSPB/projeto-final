from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


class Equipamento:
    TIPOS_VALIDOS = ("Computador", "Monitor", "Teclado", "Mouse",
                     "Impressora", "Projetor", "Outro")

    def __init__(self, patrimonio, laboratorio, tipo, id=None):
        self.__id = id
        self.patrimonio = patrimonio
        self.laboratorio = laboratorio
        self.tipo = tipo

    @property
    def id(self):
        return self.__id

    @property
    def patrimonio(self):
        return self.__patrimonio

    @patrimonio.setter
    def patrimonio(self, valor):
        valor = str(valor).strip().upper()
        if not valor:
            raise ValueError("O patrimônio não pode ficar vazio.")
        self.__patrimonio = valor

    @property
    def laboratorio(self):
        return self.__laboratorio

    @laboratorio.setter
    def laboratorio(self, valor):
        valor = str(valor).strip()
        if not valor:
            raise ValueError("Informe o laboratório.")
        self.__laboratorio = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        if valor not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido: {valor}")
        self.__tipo = valor

    def __str__(self):
        return f"{self.tipo} {self.patrimonio} ({self.laboratorio})"


class Chamado:
    STATUS_VALIDOS = ("Aberto", "Em andamento", "Resolvido")

    def __init__(self, equipamento_id, descricao_problema,
                 data=None, status_resolucao="Aberto", id=None):
        if status_resolucao not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido: {status_resolucao}")
        self.__id = id
        self.__equipamento_id = self.__validar_equipamento_id(equipamento_id)
        self.__data = data or datetime.now()
        self.__status_resolucao = status_resolucao
        self.descricao_problema = descricao_problema

    @staticmethod
    def __validar_equipamento_id(valor):
        try:
            valor = int(valor)
        except (TypeError, ValueError):
            raise ValueError("Escolha um equipamento válido.")
        if valor <= 0:
            raise ValueError("Escolha um equipamento válido.")
        return valor

    @property
    def id(self):
        return self.__id

    @property
    def equipamento_id(self):
        return self.__equipamento_id

    @property
    def data(self):
        return self.__data

    @property
    def status_resolucao(self):
        return self.__status_resolucao

    @property
    def descricao_problema(self):
        return self.__descricao_problema

    @descricao_problema.setter
    def descricao_problema(self, texto):
        texto = str(texto).strip()
        if len(texto) < 10:
            raise ValueError("Descreva o problema com pelo menos 10 caracteres.")
        self.__descricao_problema = texto

    def alterar_status(self, novo_status):
        if novo_status not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido: {novo_status}")
        if self.__status_resolucao == "Resolvido":
            raise ValueError("Chamado já resolvido não pode ser alterado.")
        self.__status_resolucao = novo_status


class Usuario:
    PERFIS_VALIDOS = ("Professor", "Técnico", "Administrador")

    PERMISSOES = {
        "Professor": ("abrir_chamado", "ver_painel", "ver_historico"),
        "Técnico": ("abrir_chamado", "ver_painel", "ver_historico", "alterar_status"),
        "Administrador": ("abrir_chamado", "ver_painel", "ver_historico", "alterar_status",
                          "cadastrar_equipamento", "gerenciar_usuarios"),
    }

    def __init__(self, nome, login, perfil, senha_hash=None, id=None):
        self.__id = id
        self.nome = nome
        self.login = login
        self.perfil = perfil
        self.__senha_hash = senha_hash

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        valor = str(valor).strip()
        if len(valor) < 3:
            raise ValueError("O nome precisa ter pelo menos 3 caracteres.")
        self.__nome = valor

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, valor):
        valor = str(valor).strip().lower()
        if len(valor) < 3 or " " in valor:
            raise ValueError("O login precisa ter pelo menos 3 caracteres e não pode ter espaços.")
        self.__login = valor

    @property
    def perfil(self):
        return self.__perfil

    @perfil.setter
    def perfil(self, valor):
        if valor not in self.PERFIS_VALIDOS:
            raise ValueError(f"Perfil inválido: {valor}")
        self.__perfil = valor

    @property
    def senha_hash(self):
        return self.__senha_hash

    def definir_senha(self, senha):
        if len(str(senha)) < 6:
            raise ValueError("A senha precisa ter pelo menos 6 caracteres.")
        self.__senha_hash = generate_password_hash(str(senha), method="pbkdf2:sha256")

    def verificar_senha(self, senha):
        if self.__senha_hash is None:
            return False
        return check_password_hash(self.__senha_hash, str(senha))

    def pode(self, acao):
        return acao in self.PERMISSOES[self.__perfil]
