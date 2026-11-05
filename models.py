from datetime import datetime


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
            raise ValueError("Status inválido.")
        self.__id = id
        self.__equipamento_id = int(equipamento_id)
        self.__data = data or datetime.now()
        self.__status_resolucao = status_resolucao
        self.descricao_problema = descricao_problema

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
