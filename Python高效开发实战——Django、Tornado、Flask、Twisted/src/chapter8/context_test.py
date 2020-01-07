import datetime
from flask import Flask, session, g, request


app = Flask(__name__)

app.secret_key = 'SET_ME_BEFORE_USE_SESSION'


@app.route('/write_session')
def write_session():
    session['new_session'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(session.modified)
    print(session.new)
    return session['key_time']


@app.route('/read_session')
def read_session():
    return session.get('key_time') or 'None'


@app.route('/prefix/echo_url')
def echo_url():
    print('base_url', request.base_url)
    print('path', request.path)
    print('script_root', request.script_root)
    print('url', request.url)
    print('url_root', request.url_root)
    return request.base_url


class MyDB(object):
    def __init__(self):
        print('A db connection is created')

    def close(self):
        print('A db is closed')


def connect_to_database():
    return MyDB()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = connect_to_database()
        g._database = db
    return db


@app.teardown_request
def teardown_db(response):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
