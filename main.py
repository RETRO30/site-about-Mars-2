from flask import Flask
from flask import render_template
from flask import redirect
import json

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KSN6W4VdXRcR1tzR7IHMmtNFgW6UsTZn'


@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:profession>')
def training(profession):
    return render_template('training.html', title='Заготовка', profession=profession)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    professions = list(
        map(lambda x: x.strip(), open('static/txt/professions.txt', encoding='utf8').readlines()))
    return render_template('list_prof.html', title='Список профессий', type_list=type_list,
                           professions=professions)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    with open('answer.json', 'rt', encoding='utf8') as f:
        data = json.loads(f.read())
    return render_template('auto_answer.html', **data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    data = list(
        map(lambda x: x.strip(), open('static/txt/distribution.txt', encoding='utf8').readlines()))
    return render_template('distribution.html', title='Размещение по каютам', data=data)


@app.route('/table/<user_sex>/<int:user_age>')
def table(user_sex, user_age):
    return render_template('table.html', title='Цвет каюты', user_sex=user_sex, user_age=user_age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
