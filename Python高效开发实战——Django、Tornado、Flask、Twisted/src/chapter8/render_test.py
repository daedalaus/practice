from flask import Flask, render_template, request
from wtform import BulletinForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/bd/view_bulletins', methods=['GET', 'POST'])
def view_bulletins():
    if request.method == 'GET':
        form = BulletinForm()
    else:
        form = BulletinForm(request.form)
    return render_template('view_bulletin.html', form=form)


if __name__ == '__main__':
    app.run()
