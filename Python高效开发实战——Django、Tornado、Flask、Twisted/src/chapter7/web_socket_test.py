import tornado.web
import tornado.ioloop
import tornado.websocket


from tornado.options import define, options, parse_command_line

define('port', default=8888, help='run on the given port', type=int)

clients = dict()


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        self.render('index.html')


class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args, **kwargs):
        self.id = self.get_argument('Id')
        self.stream.set_nodelay(True)
        clients[self.id] = {'id': self.id, 'object': self}

    def on_message(self, message):
        print('Client %s received a message: %s' % (self.id, message))

    def on_close(self):
        if self.id in clients:
            del clients[self.id]
            print('Client %s is closed' % self.id)

    def check_origin(self, origin):
        return True


def make_app():
    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/websocket', MyWebSocketHandler),
    ])
    return app


import threading
import time
import datetime
import asyncio


def send_time():
    asyncio.set_event_loop(asyncio.new_event_loop())
    while True:
        for key in clients.keys():
            msg = str(datetime.datetime.now())
            clients[key]['object'].write_message(msg)
            print('write to client %s: %s' % (key, msg))
        time.sleep(1)


if __name__ == '__main__':
    threading.Thread(target=send_time).start()
    # parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
