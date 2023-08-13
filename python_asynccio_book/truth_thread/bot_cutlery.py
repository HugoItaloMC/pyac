#  Veremos por que o encadeamento é considerado inseguro.
# To Bot Cutlery

import sys
from threading import Thread
from queue import Queue
from attr import attrs, attrib
from typing import List

threads: List[Thread] = []


class ThreadBot(Thread):  # 1 -- Um ThreadBot é uma subclasse de um thread.

    def __init__(self):
        #  A função de destino do thread é o método manage_table(), definido posteriormente em o arquivo.
        super().__init__(target=self.manage_table)

        #    Este bot vai servir mesas e precisará ser responsável por algumas
        #  talheres. Cada bot acompanha os talheres que tirou da cozinha aqui.
        #  (A classe Cutlery será definida posteriormente.)
        self.cutlery: Cutlery = Cutlery(knives=0, forks=0)

        #    O bot também receberá tarefas. Eles serão adicionados a esta fila de tarefas e o
        #  bot irá executá-los durante seu loop de processamento principal, a seguir.
        self.tasks: Queue = Queue()

    def manage_table(self):
        #   A rotina primária deste bot é este loop infinito. Se você precisar desligar um
        # bot, você deve dar a eles a tarefa de desligamento.
        while True:
            task = self.tasks.get()  # Buscando Tarefa
            if task == 'prepare table':
                #    Existem apenas três tarefas definidas para este bot. Este, prepare a mesa, é o que
                #  o bot deve fazer para obter uma nova mesa pronta para o serviço. Para o nosso teste, o único
                #  O requisito é pegar os talheres da cozinha e colocá-los sobre a mesa.
                #  clear table é usado quando uma mesa deve ser limpa: o bot deve retornar o usado
                #  talheres de volta para a cozinha. shutdown apenas desliga o bot.
                kitchen.give(to=self.cutlery, knives=4, forks=4)  # 6
            elif task == 'clear table':
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return


#  shows the definition of the Cutlery object.

#    attrs, que é uma biblioteca Python de código aberto que não tem nada a ver com
#  threads ou asyncio, é uma biblioteca realmente maravilhosa para facilitar a criação de classes.
#    Aqui, a decorator @attrs vai garantir que essa aula de Cutelaria receba todo o
#  código clichê usual (como __init__()) configurado automaticamente.
@attrs
class Cutlery:
    #    A função attrib() fornece uma maneira fácil de criar atributos, incluindo
    #  defaults, que normalmente você poderia ter tratado como argumentos de palavra-chave no método __init__().
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: 'Cutlery', knives=0, forks=0):
        #    Este método é utilizado para transferir facas e garfos de um objeto Talheres para
        #  outro. Normalmente, será usado por bots para obter talheres da cozinha para
        #  novas mesas e devolver os talheres à cozinha depois que a mesa for limpa.
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        # Esta é uma função utilitária muito simples para alterar os dados de inventário no objeto instância.
        self.knives += knives
        self.forks += forks

#    Definimos cozinha como o identificador do estoque de talheres da cozinha. Typicalmamente,
#  cada um dos bots obterá talheres deste local. Também é necessário que eles devolvem
#  os talheres a esta loja quando uma mesa é limpa.
kitchen: Cutlery = Cutlery(knives=100, forks=100)

#  Este script é executado durante o teste. Para nosso teste, usaremos 10 ThreadBots.
bots: List[ThreadBot] = [ThreadBot() for i in range(10)]


for bot in bots:
    #  Obtemos o número de tabelas como um parâmetro de linha de comando e, em seguida, damos a cada
    # bot esse número de tarefas para preparar e limpar mesas no restaurante.
    for line in range(int(sys.argv[1])):
        bot.tasks.put('prepare table')
        bot.tasks.put('clear table')

    #  A tarefa de desligamento fará com que os bots parem (para que bot.join() um pouco mais
    # para baixo retornará). O restante do script imprime mensagens de diagnóstico e inicializa
    # os robôs.
    bot.tasks.put('shutdown')
print('Kitchen inventory before service: ', kitchen)

for bot in bots:
    bot.start()
    threads.append(bot)

for thread in threads:
    thread.join()

print('Kitchen inventory after service: ', kitchen)
