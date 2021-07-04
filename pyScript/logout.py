from flask_login import logout_user, login_required
from flask import Blueprint, redirect, request


blueprint = Blueprint('logout', __name__)


@blueprint.route('/logout')
@login_required
def logout():

    # TODO check next page is save
    next_page = request.args.get('next', '/')
    logout_user()
    return redirect(next_page)
