from flask import Blueprint, render_template, request

blueprint = Blueprint('main_page', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main_page.html')
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print(login, password)
        return render_template('main_page.html', some_inf=f'Welcome {login}')
