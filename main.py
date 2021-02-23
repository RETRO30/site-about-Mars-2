from flask import Flask
from flask import render_template
import json

app = Flask(__name__)


@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:profession>')
def training(profession):
    return render_template('training.html', title='Заготовка', profession=profession)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    professions = list(map(lambda x: x.strip(), open('static/txt/professions.txt', encoding='utf8').readlines()))
    return render_template('list_prof.html', title='Список профессий', type_list=type_list, professions=professions)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    with open('answer.json', 'rt', encoding='utf8') as f:
        data = json.loads(f.read())
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
