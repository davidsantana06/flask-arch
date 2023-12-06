from flask import flash, url_for, redirect

from app.lib.core import render_template

from . import auth
from .forms import LoginForm


@auth.get('/login')
def login():
    return render_template(auth, 'login', {'form': LoginForm()})


@auth.post('/login')
def login_post():
    flash('You have been logged in', 'success')
    return redirect(url_for('home.index'))
