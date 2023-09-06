import json
from datetime import datetime
from queue import Queue
from threading import Thread, RLock

lock = RLock()

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

    def __iter__(self):
        yield from {"_class": self.__class__.__name__,
                    "_attrs": {attr: getattr(self, attr) for attr in self.__dict__.keys() if attr is not None}}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False, indent=True)

    def __repr__(self):
        return self.__str__()


class Servico:

    def __init__(self, descricao: str, concluido: bool = False):
        self.descricao = descricao
        self.concluido = concluido
        self.data_ordem: datetime = datetime.now()

    def __iter__(self):
        yield from {
            "_class": self.__class__.__name__,
            "_attrs": str({attr: getattr(self, attr) for attr in self.__dict__.keys() if attr is not None})}.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False, indent=True)

    def __repr__(self):
        return self.__str__()


# Ordem de Servico
def ordem_servico(queue) -> None:
    nome: str = input("::\tNOME CLIENTE:\t")
    ano: str = input("***\tDADOS VEICULO\t***\n::\tANO:\t")
    modelo: str = input("::\tMODELO:\t")
    cliente: Cliente = Cliente(ano=ano, modelo=modelo, nome=nome)

    descricao: str = input("***\tDESCRICÃO DO SERVICO\t***\n::\tDESCRICAO:\t")
    servico: Servico = Servico(descricao=descricao)
    queue.put({"cliente": cliente, "servico": servico})


def status_servico(queue) -> None:
    task = queue.get()
    print(task)


if __name__ == '__main__':
    queue = Queue()

    threads = [Thread(target=ordem_servico, args=(queue,)),
               Thread(target=status_servico, args=(queue,))]

    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
