from flask import Blueprint, render_template, request
from pyScript.wtf_forms import LoginForm
from pyScript.login import SingIn


blueprint = Blueprint('main_page', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('main_page.html', form=form)
    if request.method == 'POST':
        if SingIn(form):
            return render_template('main_page.html', some_inf=f'Welcome {123}', form=form)
        else:
            return 'неудача'
