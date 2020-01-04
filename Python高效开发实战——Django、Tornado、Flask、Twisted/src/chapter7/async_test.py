import tornado.web
import tornado.ioloop
import tornado.httpclient


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('http://www.baidu.com', callback=self.on_response)

    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        self.write(response.body)
        self.finish()


handlers = [
    (r'/', MainHandler),
]


def make_app():
    return tornado.web.Application(handlers)


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
