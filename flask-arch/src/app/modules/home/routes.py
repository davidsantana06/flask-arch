from flask import Blueprint
from flask_login import login_required
from http import HTTPStatus
from typing import Tuple

from app.lib.utils import render_page

from .forms import LoginForm
from .services import find_all_users


home = Blueprint('home', __name__, url_prefix='')


@home.get('/')
@login_required
def index() -> Tuple[str, HTTPStatus]:
    # data = {
    #     'users': find_all_users()
    # }
    return (render_page('home/index'), HTTPStatus.OK)
