from tornado import gen
from tornado.ioloop import IOLoop
from tornado.httpclient import HTTPClient, AsyncHTTPClient


def synchronous_visit():
    http_client = HTTPClient()
    response = http_client.fetch('http://www.baidu.com')
    print(response.body)


def handle_response(response):
    print(response.body)


def asynchronous_visit():
    http_client = AsyncHTTPClient()
    http_client.fetch('http://www.baidu.com', callback=handle_response)


@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch('http://www.baidu.com')
    print(response.body)


@gen.coroutine
def outer_coroutine():
    print('start call another coroutine')
    yield coroutine_visit()
    print('end of outer_couroutine')


def func_normal():
    print('start to call a coroutine ')
    IOLoop.current().run_sync(lambda: coroutine_visit())
    print('end of calling a coroutine')


if __name__ == '__main__':
    # synchronous_visit()  # yes
    # asynchronous_visit()  # no
    # coroutine_visit()  # no
    # outer_coroutine()  # no
    func_normal()  # yes
