from flask import Blueprint, render_template, request, current_app
from pyScript.wtf_forms import LoginForm, RegistrationForm
from flask_login import login_user
from pyScript.login import SingIn
from database.users import User
from database.db import db


blueprint = Blueprint('register', __name__)


@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    login_form = LoginForm
    reg_form = RegistrationForm()
    if request.method == 'POST':
        args = request.args.to_dict()

        if args.get('registration', None) is None:
            form = LoginForm()
            if SingIn(form):
                return 'вошёл и залогинился в базе'
            return render_template('register.html', login_form=login_form, reg_form=reg_form)
        else:
            form = RegistrationForm()

            if form.validate_on_submit():
                # TODO form validation and validators
                with current_app.app_context():
                    user = User(form.email, form.nickname, form.password)
                    db.session.add(user)
                    db.session.commit()
                    # TODO add a remember button
                    login_user(user, remember=True)
                return 'зареган'
            return render_template('register.html', login_form=login_form, reg_form=reg_form)

    else:
        return render_template('register.html', login_form=login_form, reg_form=reg_form)
