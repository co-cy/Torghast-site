from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from pyScript.validators import Length
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    login = StringField('Ник или email', validators=[DataRequired("Введите логин"), Length(3, 16)])
    password = PasswordField('Пароль', validators=[DataRequired("Введите пароль"), Length(8, 64)])
    # recaptcha = None
    remember_me = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    nickname = StringField('Ник', validators=[DataRequired("Введите ник"), Length(3, 16)])
    email = EmailField('email', validators=[DataRequired("Введите email"), Length(4, 32)])
    password = PasswordField('Пароль', validators=[DataRequired("Введите пароль"), Length(8, 64)])
    repeat_password = PasswordField('Повторный пароль', validators=[DataRequired("Введите повторный пароль"), Length(8, 64)])
    remember_me = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Зарегистрироваться')


