from flask import Blueprint
# from flask_login import login_required
from http import HTTPStatus

from app.lib.utils import render_page


home = Blueprint('home', __name__, url_prefix='')


@home.get('/')
def index():
    return (render_page('home/index'), HTTPStatus.OK)
