from flask import Blueprint
from http import HTTPStatus
from typing import Tuple

from app.lib.utils import render_page


auth = Blueprint('auth', __name__, url_prefix='')


@auth.get('/login')
def login() -> Tuple[str, HTTPStatus]:
    return (render_page('home/index'), HTTPStatus.OK)
