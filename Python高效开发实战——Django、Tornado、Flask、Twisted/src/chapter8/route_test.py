from flask import Flask, request, url_for


app = Flask(__name__)


@app.route('/login/<username>')
def show_welcome(username):
    return 'Hi %s' % username


@app.route('/add/<int:number>')
def add_one(number):
    return '%d' % (number + 1)


@app.route('/school/')
def schools():
    return 'The school page'


@app.route('/student')
def students():
    return 'The student page'


@app.route('/send_message', methods=['get', 'POST'])
def send_message():
    if request.method == 'POST':
        message = request.form.get('message')
        if not message:
            return 'received message failed'
        else:
            return 'received message: %s' % message
    else:
        return '<form action="/send_message" method="post">' \
                'message: <input type="text" name="message">' \
                '<input type="submit" value="Send">' \
                '</form>'


@app.route('/message', methods=['POST'])
def do_send():
    return 'This is for post methods'


@app.route('/message', methods=['get'])
def show_the_send_form():
    return '<form action="/message" method="post">' \
            'message: <input type="text" name="message">' \
            '<input type="submit" value="Send">' \
            '</form>'


@app.route('/industry')
def f_industry(): pass


@app.route('/book/<book_name>')
def f_book(book_name): pass


def url_for_test():
    with app.test_request_context():
        print(url_for('f_industry'))
        print(url_for('f_industry', name='web'))
        # print(url_for('f_book'))
        print(url_for('f_book', book_name='Python Book'))


if __name__ == '__main__':
    url_for_test()
    app.run()
