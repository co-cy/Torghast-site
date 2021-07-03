from flask import Blueprint, render_template, request, current_app
from pyScript.wtf_forms import LoginForm, RegistrationForm
from flask_login import login_user
from database.users import User
from database.db import db
from pyScript import monitor


blueprint = Blueprint('register', __name__)


@blueprint.route('/register', methods=['POST', 'GET'])
@blueprint.route('/reg', methods=['POST', 'GET'])
def register():
    login_form = LoginForm()
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        user_nickname = User.query.filter_by(nickname=reg_form.nickname.data).first()
        user_email = User.query.filter_by(email=reg_form.email.data).first()

        if not user_nickname:
            valid_nick = True
        else:
            valid_nick = False
            reg_form.nickname.errors.append('Ник занят')

        if not user_email:
            valid_email = True
        else:
            valid_email = False
            reg_form.email.errors.append('Email занят')

        if reg_form.password.data == reg_form.repeat_password.data:
            valid_password = True
        else:
            valid_password = False
            reg_form.repeat_password.errors.append('Пароли не совпадают')

        if valid_nick and valid_email and valid_password:
            # Добавление в базу данных пользователя
            with current_app.app_context():
                user = User(reg_form.email.data, reg_form.nickname.data, reg_form.password.data)
                print(user.password)
                print(len(user.password))
                db.session.add(user)
                db.session.commit()
            # Авторизация пользователя
            login_user(user, remember=True)
    data = monitor.request('localhost', 25565)
    config = {
        'title_name': 'Register',
        'server_name': data[0],
        'server_online': data[1]
    }
    return render_template('register.html', reg_form=reg_form, login_form=login_form, **config)