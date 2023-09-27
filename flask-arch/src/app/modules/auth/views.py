from flask import Blueprint
from http import HTTPStatus

from app.lib.utils import render_page

from .forms import LoginForm


auth = Blueprint('auth', __name__, url_prefix='')


@auth.get('/login')
def login():
    data = {
        'form': LoginForm()
    }
    return (render_page('auth/login', data), HTTPStatus.OK)
