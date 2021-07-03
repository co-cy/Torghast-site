from flask_login import login_user
from database.users import User


def SingIn(form) -> bool:
    if form.validate_on_submit():
        user_login = User.query.filter_by(nickname=form.login.data).first()
        user_email = User.query.filter_by(email=form.login.data).first()
        if user_login and user_login.check_password(form.password.data):
            login_user(user_login, remember=form.remember_me.data)
            return True
        elif user_email and user_email.check_password(form.password.data):
            login_user(user_email, remember=form.remember_me.data)
            return True
    else:
        return False
