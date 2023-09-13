import asyncio
import pstats

from main import request_data


def task():
    make = asyncio.get_event_loop()
    queue = asyncio.Queue()
    task1 = make.create_task(request_data(queue))
    group = asyncio.gather(task1)
    make.run_until_complete(group)


if __name__ == '__main__':
    #import cProfile
    #import io
    #from pstats import SortKey

    #profile = cProfile.Profile()
    #profile.enable()

    task()

    #profile.disable()
    #profile.dump_stats('stats/run.stats')

    #_str = io.StringIO()
    #_stats = pstats.Stats(profile, stream=_str).sort_stats(SortKey.TIME)
    #_stats.print_stats()
    #print(_str.getvalue())
