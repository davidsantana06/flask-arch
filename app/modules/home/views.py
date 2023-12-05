from flask_login import login_required
from http import HTTPStatus

from . import home


@home.get('/')
def index():
    return home.render_template('index')


@home.get('/login-test')
@login_required
def login_test():
    return home.render_template('index')


@home.get('/socket')
def socket():
    return home.render_template('socket')
