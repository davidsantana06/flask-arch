from flask_login import login_required
from http import HTTPStatus

from app.misc import render_template

from . import home


@home.get('/')
def index():
    return (render_template('index'), HTTPStatus.OK)


@home.get('/login-test')
@login_required
def login_test():
    return (render_template('index'), HTTPStatus.OK)


@home.get('/socket')
def socket():
    return (render_template('socket'), HTTPStatus.OK)
