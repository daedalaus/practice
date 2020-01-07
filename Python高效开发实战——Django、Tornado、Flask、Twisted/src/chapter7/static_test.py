import tornado.web
import tornado.gen
import tornado.ioloop
import tornado.httpclient


class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        # http = tornado.httpclient.AsyncHTTPClient()
        # response = yield http.fetch('http://www.baidu.com')
        # self.write(response.body)
        self.render('./assets/js/templates/index.html')


handlers = [
    (r'/', MainHandler),
    (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/css'}),
    (r'/images/png/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/images'}),
    (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/js', 'default_filename':
                                                  'templates/index.html'})
]


def make_app():
    return tornado.web.Application(handlers, static_path='./my_static')


def main():
    app = make_app()
    app.listen(8888, '127.0.0.1')
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
