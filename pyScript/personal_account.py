from flask import Blueprint, render_template, redirect, request
from flask_login import current_user, login_user, login_required
from pyScript.wtf_forms import LoginForm
from database.users import User

blueprint = Blueprint('personal_account', __name__)


@blueprint.route('/lk', methods=['GET', 'POST'])
@blueprint.route('/personal_account', methods=['GET', 'POST'])
@blueprint.route('/account', methods=['GET', 'POST'])
@login_required
def index():
    login_form = LoginForm()
    return render_template('personal_account_page.html', login_form=login_form)