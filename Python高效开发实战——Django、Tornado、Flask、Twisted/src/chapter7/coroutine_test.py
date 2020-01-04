import tornado.web
import tornado.gen
import tornado.ioloop
import tornado.httpclient


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch('http://www.baidu.com')
        self.write(response.body)


handlers = [
    (r'/', MainHandler),
]


def make_app():
    return tornado.web.Application(handlers)


def main():
    app = make_app()
    app.listen(8888, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
