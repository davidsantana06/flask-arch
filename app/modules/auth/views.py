from . import auth
from .forms import LoginForm


@auth.get('/login')
def login():
    return auth.render_template('login', {'form': LoginForm()})
