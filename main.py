from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:profession>')
def training(profession):
    return render_template('training.html', title='Заготовка', profession=profession)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
