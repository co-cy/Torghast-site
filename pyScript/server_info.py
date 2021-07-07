from flask import Blueprint, render_template, redirect, request
from pyScript.wtf_forms import LoginForm

blueprint = Blueprint('server_info', __name__)


@blueprint.route('/server_info', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    return render_template('server_info.html', login_form=login_form)