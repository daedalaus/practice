from tornado import gen
from tornado.httpclient import AsyncHTTPClient

from concurrent.futures import ThreadPoolExecutor
thread_pool = ThreadPoolExecutor(2)


@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    list_response = yield [
        http_client.fetch('http://www.baidu.com'),
        http_client.fetch('http://www.sina.com'),
        http_client.fetch('http://www.163.com')
    ]

    for response in list_response:
        print(response.body)


if __name__ == '__main__':
    coroutine_visit()