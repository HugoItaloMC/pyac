import json
from datetime import datetime
from queue import Queue
from threading import Thread, RLock

from model import Servico
from app import schema_data

lock = RLock()


# Ordem de Servico
def pool_queue(queue):
    queue.put(Servico())


def run_queue(queue) -> Servico:
    work = queue.get()
    with lock:
        data = schema_data()
        work.cliente = json.loads(work.cliente(nome=data['nome'], modelo=data['modelo'], ano=data['ano']).__str__())
        work.descricao = data['descricao']

        if data['status']:
            work.concluido = True
            work.data_concluido = datetime.now()

        queue.task_done()
        return work
