from concurrent.futures import ThreadPoolExecutor
from tornado import gen
thread_pool = ThreadPoolExecutor(2)


def my_sleep(count):
    import time
    for i in range(count):
        print(i)
        time.sleep(1)


@gen.coroutine
def call_blocking():
    print('start of call_blocking')
    yield thread_pool.submit(my_sleep, 10)
    print('end of call_blocking')


if __name__ == '__main__':
    call_blocking()
