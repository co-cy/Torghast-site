from flask import Blueprint, render_template, redirect, request
from flask_login import current_user, login_user
from pyScript.wtf_forms import LoginForm
from database.users import User

blueprint = Blueprint('main_page', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/index', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()

    args = request.args.to_dict()
    next_page = args.get('next', None)

    config = {
        'title_name': 'Torghast',
    }

    if login_form.validate_on_submit():
        user_login = User.query.filter_by(nickname=login_form.login.data).first()
        user_email = User.query.filter_by(email=login_form.login.data).first()

        user = user_login or user_email
        if user:
            if user.check_password(login_form.password.data):
                login_user(user, remember=True)
                if next_page is not None:
                    return redirect(next_page)
                else:
                    with open('monitor_info.txt', 'r') as f:
                        data = list(f.readline().split('&'))
                    return render_template('main_page.html', login_form=login_form, **config, server_name=data[0], server_online=data[1])
            else:
                login_form.password.errors.append('Неверный пароль')

        else:
            login_form.login.errors.append('Не найден логин или пароль')

    if next_page is not None:
        return redirect(next_page)
    else:
        with open('monitor_info.txt', 'r') as f:
            data = list(f.readline().split('&'))
        return render_template('main_page.html', login_form=login_form, **config, server_name=data[0], server_online=data[1])
