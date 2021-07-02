from flask import Blueprint, render_template, request, redirect

blueprint = Blueprint('register', __name__)


@blueprint.route('/register', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        if 'register' in request.form:
            login = request.form['login']
            password = request.form['password']
            print(login, password)
            return render_template('register.html', some_inf=f'You are succesful register, {login}!')
        else:
            login = request.form['login']
            password = request.form['password']
            print(login, password)
            return redirect('/')