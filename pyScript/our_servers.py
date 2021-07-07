from flask import Blueprint, render_template, redirect, request
from flask_login import current_user, login_user, login_required
from pyScript.wtf_forms import LoginForm
from database.users import User

blueprint = Blueprint('our_servers', __name__)


@blueprint.route('/servers', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()
    return render_template('our_servers.html', login_form=login_form)