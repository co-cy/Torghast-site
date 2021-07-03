from flask import Blueprint, render_template, request, current_app
from pyScript.wtf_forms import LoginForm, RegistrationForm
from flask_login import login_user
from database.users import User
from database.db import db


blueprint = Blueprint('register', __name__)


@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        user_nickname = User.query.filter_by(nickname=reg_form.login.data).first()
        user_email = User.query.filter_by(email=reg_form.login.data).first()

        if not user_nickname:
            valid_nick = True
        else:
            valid_nick = False
            reg_form.nickname.errors.append('Ник занят')

        if not user_email:
            valid_email = True
        else:
            valid_email = False
            reg_form.email.errors.append('email занят')

        if reg_form.password == reg_form.repeat_password:
            valid_password = True
        else:
            valid_password = False
            reg_form.repeat_password.errors.append('Пароли не совпадают')

        if valid_nick and valid_email and valid_password:
            # Добавление в базу данных пользователя
            with current_app.app_context():
                user = User(reg_form.email, reg_form.nickname, reg_form.password)
                db.session.add(user)
                db.session.commit()
            # Авторизация пользователя
            login_user(user, remember=reg_form.remember_me)

    return render_template('register.html', reg_form=reg_form)