from asyncio import create_task, gather, run
from aiohttp import ClientSession


async def fetch(session, url):
    async with session.get(f'http://0.0.0.0:8000/items/{url}') as r:
        if r.status != 200:
            r.raise_for_status()
        return await r.text()


async def fetch_all(session, urls):
    tasks: list = []

    for url in urls:
        task = create_task(fetch(session, url=url))
        tasks.append(task)
    return await gather(*tasks)


async def main():
    urls = range(1, 2501)
    async with ClientSession() as session:
        recv = await fetch_all(session=session, urls=urls)
        print(recv)

if __name__ == '__main__':
    from time import time
    init = time()
    run(main())
    print(time() - init)
