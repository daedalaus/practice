import tornado.web
import tornado.ioloop


session_id = 1


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        global session_id
        session = self.get_secure_cookie('session')
        if not session:
            self.set_secure_cookie('session', str(session_id))
            session_id = session_id + 1
            self.write('Your session got a new session!')
        else:
            self.write('Your session was set! It is %s' % session)


app = tornado.web.Application([
    (r'/', MainHandler),
], cookie_secret='SECRET_DONT_LEAK')


def main():
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
