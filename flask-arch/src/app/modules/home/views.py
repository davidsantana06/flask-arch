from flask import Blueprint
from flask_login import login_required
from http import HTTPStatus

from app.lib.utils import render_page


home = Blueprint('home', __name__, url_prefix='')


@home.get('/')
def index():
    return (render_page('home/index'), HTTPStatus.OK)


@home.get('/login-test')
@login_required
def login_test():
    return (render_page('home/index'), HTTPStatus.OK)
