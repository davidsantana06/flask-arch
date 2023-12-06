from flask_login import login_required
from app.lib.core import render_template
from . import home


@home.get('/')
def index():
    return render_template(home, 'index')


@home.get('/login-test')
@login_required
def login_test():
    return render_template(home, 'index')


@home.get('/socket')
def socket():
    return render_template(home, 'socket')
