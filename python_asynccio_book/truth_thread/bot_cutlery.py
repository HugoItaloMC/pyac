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
        super().__init__(target=self.gerenciar_mesa)

        #    Este bot vai servir mesas e precisará ser responsável por alguns
        #  talheres. Cada bot acompanha os talheres que tirou da cozinha aqui.
        #  (A classe Cutlery será definida posteriormente.)
        self.talheres: Talheres = Talheres(faca=0, garfo=0)

        #    O bot também receberá tarefas. Eles serão adicionados a esta fila de tarefas e o
        #  bot irá executá-los durante seu loop de processamento principal, a seguir.
        self.tarefa: Queue = Queue()

    def gerenciar_mesa(self) -> None:
        #   A rotina primária deste bot é este loop infinito. Se você precisar desligar um
        # bot, você deve dar a eles a tarefa de desligamento.
        while True:
            tarefas: Queue = self.tarefa.get()  # Buscando Tarefa
                #    Existem apenas três tarefas definidas para este bot. Este, prepare a mesa, é o que
                #  o bot deve fazer para obter uma nova mesa pronta para o serviço. Para o nosso teste, o único
                #  requisito é pegar os talheres da cozinha e colocá-los sobre a mesa.
                #  `limpar mesa` é usado quando uma mesa deve ser limpa: o bot deve retornar os
                #  talheres de volta para a cozinha. shutdown apenas desliga o bot.
            if tarefas == 'preparar mesa':
                cozinha.fornecer(em_direcao=self.talheres, faca=4, garfo=4)
            elif tarefas == 'limpar mesa':
                self.talheres.fornecer(em_direcao=cozinha, faca=4, garfo=4)
            elif tarefas == 'finalizar':
                return  # Break Loop


#  Definindo objeto Talheres.

#    attrs, que é uma biblioteca Python de código aberto que não tem nada a ver com
#  threads ou asyncio, é uma biblioteca realmente maravilhosa para facilitar a criação de classes.
#    Aqui, a decorator @attrs vai garantir que essa aula de Cutelaria receba todo o
#  código clichê usual (como __init__()) configurado automaticamente.
@attrs
class Talheres:
    #    A função attrib() fornece uma maneira fácil de criar atributos, incluindo
    #  defaults, que normalmente você poderia ter tratado como argumentos de palavra-chave no método __init__().
    faca: int = attrib(default=0)
    garfo: int = attrib(default=0)

    def fornecer(self, em_direcao: 'Talheres', faca: int = 0, garfo: int = 0) -> None:
        #    Este método é utilizado para transferir facas e garfos de um objeto Talheres para
        #  outro. Normalmente, será usado por bots para obter talheres da cozinha para
        #  novas mesas e devolver os talheres à cozinha depois que a mesa for limpa.
        self.alterar(-faca, -garfo)
        em_direcao.alterar(faca, garfo)

    def alterar(self, faca, garfo):
        # Esta é uma função utilitária muito simples para alterar os dados de inventário na instância do objeto.
        self.faca += faca
        self.garfo += garfo


#    Definimos cozinha como o identificador do estoque de talheres da cozinha. Typicalmamente,
#  cada um dos bots obterá talheres deste local. Também é necessário que eles devolvem
#  os talheres a esta loja quando uma mesa é limpa.
cozinha: Talheres = Talheres(faca=100, garfo=100)

#  Este script é executado durante o teste. Para nosso teste, usaremos 10 ThreadBots.
bots: List[ThreadBot] = [ThreadBot() for i in range(10)]


for bot in bots:
    #  Obtemos o número de tabelas como um parâmetro de linha de comando e, em seguida, damos a cada
    # bot esse número de tarefas para preparar e limpar mesas no restaurante.
    for line in range(int(sys.argv[1])):
        bot.tarefa.put('preparar mesa')
        bot.tarefa.put('limpar mesa')

    #  A tarefa de desligamento fará com que os bots parem (para que bot.join() um pouco mais
    # para baixo retornará). O restante do script imprime mensagens de diagnóstico e inicializa os robôs.
    bot.tarefa.put('finalizar')
print('Inventário da Cozinha antes do servico: ', cozinha)

for bot in bots:
    bot.start()
    threads.append(bot)

for thread in threads:
    thread.join()

print('Inventário da Cozinha depois do servico: ', cozinha)
