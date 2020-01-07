from flask import Flask, abort, redirect, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/check')


@app.route('/check')
def f_check():
    print('check enter')
    abort(400)


@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400


if __name__ == '__main__':
    app.run()
