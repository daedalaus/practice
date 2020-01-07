import sqlite3
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_cookie('cookie_test', 'hellocookie')
        self.write('Hello World')


class EntryHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = sqlite3.connect('test.db')

    def get(self, slug='default'):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM demo WHERE slug = "%s"' % slug)
        # entry = self.db.get('SELECT * FROM entries WHERE slug = %s', slug)
        entries = cursor.fetchall()
        if not entries:
            raise tornado.web.HTTPError(404)
        self.render('entry.html', entries=entries)

    def on_finish(self):
        self.db.close()


class PrintInHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        name = self.get_argument('name')
        print('name:', name)
        friends = self.get_arguments('friend')
        print('friends:', friends)
        cookie = self.get_cookie('cookie_test')
        print('cookie:', cookie)
        method = self.request.method
        print('method:', method)
        uri = self.request.uri
        print('uri:', uri)
        path = self.request.path
        print('path:', path)
        query = self.request.query
        print('query:', query)
        version = self.request.version
        print('version:', version)
        headers = self.request.headers
        print('headers:', headers)
        body = self.request.body
        print('body:', body)
        remote_ip = self.request.remote_ip
        print('remote_ip:', remote_ip)
        protocol = self.request.protocol
        print('protocol:', protocol)
        host = self.request.host
        print('host:', host)
        arguments = self.request.arguments
        print('arguments:', arguments)
        files = self.request.files
        print('files:', files)
        cookies = self.request.cookies
        print('cookies:', cookies)
        self.write('success')


class ResponseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.test2()
        # self.write({'name': 'mike', 'age': 18, 'city': 'shanghai'})
        self.redirect('/')

    def test1(self):
        self.set_header('number', 9)
        self.set_header('language', 'france')
        self.set_header('language', 'chinese')

    def test2(self):
        self.set_header('number', 8)
        self.set_header('language', 'france')
        self.add_header('language', 'chinese')


handlers = [
    (r'/', MainHandler),
    (r'/entry/([^/]*)', EntryHandler),
    (r'/request', PrintInHandler),
    (r'/response', ResponseHandler),
]


def make_app():
    return tornado.web.Application(handlers)


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


def db_test():
    db = sqlite3.connect('test.db')
    cur = db.cursor()
    # cur.execute('create table demo(id int, slug varchar(20))')
    # cur.execute('insert into demo values (%d, "%s")' % (1, 'default'))
    # cur.execute('insert into demo values (%d, "%s")' % (2, 'abc'))
    # cur.execute('insert into demo values (%d, "%s")' % (3, '2015-09-10'))
    # cur.execute('insert into demo values (%d, "%s")' % (4, 'default'))
    # cur.execute('insert into demo values (%d, "%s")' % (5, 'default'))
    # cur.execute('insert into demo values (%d, "%s")' % (6, 'default'))
    cur.execute('select * from demo')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print('====')
    cur.execute('select * from demo where slug =  "%s"' % 'default')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # db.commit()


if __name__ == '__main__':
    main()
    # db_test()

