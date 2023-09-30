from http import HTTPStatus

from app.misc import render_template

from . import auth
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = {
        'form': LoginForm()
    }
    return (render_template('login', data), HTTPStatus.OK)
