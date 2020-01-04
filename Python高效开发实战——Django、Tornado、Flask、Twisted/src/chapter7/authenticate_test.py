import uuid
import tornado.web
import tornado.ioloop
import tornado.escape


dict_sessions = {}


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        # print(self.current_user)
        self.current_user = 'set_user'

        if self.get_secure_cookie('session_id') is None:
            return None
        session_id = self.get_secure_cookie('session_id').decode('utf-8')
        return dict_sessions.get(session_id)


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write('Hello, ' + name)


class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # self.write('<html><body><form action="/login" method="post">'
        #            '{% module xsrf_form_html() %}'
        #            'Name: <input type="text" name="name">'
        #            '<input type="submit" value="Sign in">'
        #            '</form></body></html>')
        self.render('login.html')

    def post(self, *args, **kwargs):
        if len(self.get_argument('name')) < 3:
            self.redirect('/login')
            return
        session_id = str(uuid.uuid1())
        dict_sessions[session_id] = self.get_argument('name')
        self.set_secure_cookie('session_id', session_id)
        self.redirect('/')


def make_app():
    settings = {
        'cookie_secret': 'SECRET_DONT_LEAK',
        'login_url': '/login',
        'xsrf_cookies': True
    }
    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/login', LoginHandler),
    ], **settings)
    return app


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
