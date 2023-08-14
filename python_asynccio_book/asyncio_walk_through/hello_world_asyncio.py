#  • Iniciar o loop de evento assíncrono
#  • Chamar funções async/await
#  • Criação de uma tarefa a ser executada no loop
#  • Aguardando a conclusão de várias tarefas
#  • Fechar o loop após a conclusão de todas as tarefas simultâneas

import asyncio
import time


async def main() -> None:
    print(f"{time.ctime()} Hello")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} GoodBye !")

if __name__ == '__main__':

    execucao = asyncio.get_event_loop()
    #  execucao = asyncio.get_event_loop()
    # Você precisa de uma instância de loop antes de poder executar qualquer co-rotina, e é assim que você
    # pegue um. Na verdade, em qualquer lugar que você chamá-lo, get_event_loop() fornecerá o mesmo
    # instância de loop a cada vez, contanto que você esteja usando apenas um único thread.2 Se você estiver
    # dentro de uma função def assíncrona, você deve chamar asyncio.get_running_loop()
    # em vez disso, o que sempre oferece o que você espera.

    tarefa = execucao.create_task(main())
    # tarefa = execucao.create_task(main())
    # Nesse caso, a chamada específica é execucao.create_task(main()). Sua função de corrotina
    # não será executada até que você faça isso. Dizemos que os agendamentos create_task()
    # sua corrotina seja executada no loop.3 O objeto de tarefa retornado pode ser usado para
    # monitorar o status da tarefa (por exemplo, se ela ainda está em execução ou foi
    # concluído) e também pode ser usado para obter um valor de resultado de sua conclusão
    # coroutine. Você pode cancelar a tarefa com tarefa.cancel().

    execucao.run_until_complete(tarefa)
    #  execucao.run_until_complete(tarefa)
    # Essa chamada bloqueará o thread atual, que normalmente será o thread principal.
    # Observe que run_until_complete() manterá o loop em execução somente até o determinado
    # coro conclui - mas todas as outras tarefas agendadas no loop também serão executadas enquanto o
    # loop está em execução. Internamente, asyncio.run() chama run_until_complete() para você
    # e, portanto, bloqueia o thread principal da mesma maneira.

    pendente = asyncio.all_tasks(loop=execucao)
    for tarefa in pendente:
        tarefa.cancel()

    grupo = asyncio.gather(*pendente, return_exceptions=True)
    # grupo = asyncio.gather(tarefa1, tarefa2, tarefa3)
    # Quando a parte “principal” do programa é desbloqueada, seja por um sinal de processo
    # sendo recebido ou o loop sendo interrompido por algum código chamando execucao.stop(), o
    # código após run_until_complete() será executado. O idioma padrão mostrado aqui é
    # para reunir as tarefas ainda pendentes, cancelá-las e, em seguida, usar execucao.run_until_complete()
    # novamente até que essas tarefas sejam concluídas. collect() é o método para fazer o
    # reunião. Observe que asyncio.run() fará todo o cancelamento, coleta e
    # aguardando a conclusão das tarefas pendentes.

    execucao.run_until_complete(grupo)

    execucao.close()
    # execucao.close() é geralmente a ação final: deve ser chamado em um loop parado e
    # ele limpará todas as filas e desligará o executor. Um loop parado pode ser reiniciado,
    # mas um loop fechado se foi para sempre. Internamente, asyncio.run() fechará o
    # loop antes de retornar. Isso é bom porque run() cria um novo loop de evento a cada
    # vez que você chamá-lo.