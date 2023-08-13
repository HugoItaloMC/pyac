from concurrent.futures import ThreadPoolExecutor as Executor  # For ThreadPool

"""
  A melhor prática para usar threads é usar a classe ThreadPoolExecutor de
o módulo concurrent.futures, passando todos os dados necessários por meio de método submit() .
"""


def main(data: int) -> None:
    to_str = str(data)
    return to_str


if __name__ == '__main__':

    data = 10002
    with Executor(max_workers=10) as exc:
        future = exc.submit(main, data)

        print(dir(future), type(future.result()), future.result())
