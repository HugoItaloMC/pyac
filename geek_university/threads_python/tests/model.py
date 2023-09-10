import json
from datetime import datetime


# Modelos
class Carro:

    def __init__(self, modelo: str, ano: str):
        self.modelo: str = modelo
        self.ano: str = ano

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": {attrs: getattr(self, attrs) for attrs in self.__dict__.keys() if attrs is not None}}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False, indent=True)

    def __repr__(self):
        return self.__str__()


class Cliente(Carro):

    def __init__(self, nome: str, ano: str, modelo: str):
        super().__init__(modelo, ano)
        self.nome: str = nome

    def __call__(self, *args, **kwargs):
        return self.__call__(*args, **kwargs)

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": {attr: getattr(self, attr) for attr in self.__dict__.keys() if attr is not None}}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False, indent=True)

    def __repr__(self):
        return self.__str__()


class Servico:

    def __init__(self):
        self.descricao: str = str()
        self.concluido: bool = False
        self.data_ordem: datetime = datetime.now()
        self.cliente = Cliente
        self.data_concluido: datetime = None

    def __iter__(self):
        yield from {
            "_class": self.__class__.__name__,
            "_attrs": str({attr: getattr(self, attr) for attr in self.__dict__.keys()})}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False, indent=True)

    def __repr__(self):
        return self.__str__()

