import json
from multiprocessing import Queue, cpu_count
from concurrent.futures.process import ProcessPoolExecutor

from main import run_queue, pool_queue


def main_queue(queue) -> object:
    pool_queue(queue)

    while queue.qsize() > 0:
        work = run_queue(queue)

        with open('task.jsonl', "a+") as file:
            file.write("\n%s" % work)


def main() -> None:

    core = cpu_count() * 2
    with ProcessPoolExecutor(max_workers=core) as executor:
        for _ in range(1, core + 1):
            queue = Queue()
            if input("::\tDESEJA REALIZAR OUTRO ORCCAMENTO?\n[Y\\N]: ".lower()) == 'n':
                break
            else:
                executor.map(main_queue(queue=queue))


if __name__ == '__main__':
    main()
