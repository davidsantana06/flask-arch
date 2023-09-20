from flask import Blueprint
from http import HTTPStatus
from typing import Dict, Tuple

from .forms import LoginForm
from .lib.utils import render_page
from .services import find_all_users


main: Blueprint = Blueprint('main', __name__, url_prefix='')


@main.get('/')
def index() -> Tuple[str, HTTPStatus]:
    # data: Dict[str, object] = {
    #     'users': find_all_users()
    # }
    return (render_page('index'), HTTPStatus.OK)
