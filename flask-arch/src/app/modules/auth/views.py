from flask import Blueprint
from http import HTTPStatus

from app.lib.utils import redirect_to


auth = Blueprint('auth', __name__, url_prefix='')


@auth.get('/login')
def login():
    return (redirect_to('home.index'), HTTPStatus.TEMPORARY_REDIRECT)
