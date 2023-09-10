from threading import Thread
from queue import Queue

from main import run_queue, pool_queue


def main_queue(queue):
    pool_queue(queue)

    while queue.qsize() > 0:
        work = run_queue(queue)

        with open('task.json', "w+") as file:
            file.write(work.__str__())


def main() -> None:
    queue = Queue()
    threads = list()

    thread = Thread(target=main_queue, args=(queue,))
    threads.append(thread)

    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


if __name__ == '__main__':
    main()
