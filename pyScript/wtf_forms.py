from wtforms import StringField, PasswordField, BooleanField, SubmitField
from pyScript.validators import Length, ComplexPassword
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    login = StringField('Ник или email', validators=[DataRequired("Введите логин"), Length(3, 16)])
    password = PasswordField('Пароль', validators=[DataRequired("Введите пароль"), Length(8, 64)])
    # TODO add recaptcha
    # recaptcha = None
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    nickname = StringField('Ник', validators=[DataRequired("Введите ник"), Length(3, 16)])
    email = EmailField('email', validators=[DataRequired("Введите email"), Length(4, 32)])
    password = PasswordField('Пароль', validators=[DataRequired("Введите пароль"), Length(8, 64), ComplexPassword()])
    repeat_password = PasswordField('Повторный пароль', validators=[DataRequired("Введите повторный пароль"), Length(8, 64), ComplexPassword()])
    # TODO add recaptcha
    # recaptcha = None
    submit = SubmitField('Зарегистрироваться')


