from flask import (
    flash, url_for, redirect,
    request
)
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import (
    login_user, logout_user,
    current_user
)

from app.lib.core import jsonify_message, jsonify_redirect, render_template
from app.models import User

from . import auth
from .forms import LoginForm, RegisterForm


@auth.before_request
def before_request():
    if not any(endpoint in request.endpoint for endpoint in ['static', 'auth.logout']):
        if current_user.is_authenticated:
            return redirect(url_for('home.index'))


@auth.get('/login')
def login():
    return render_template(auth, 'login', {'form': LoginForm()})


@auth.post('/login')
def login_post():
    flash('You have been logged in.', 'success')
    return redirect(url_for('home.index'))


'''
@auth.post('/login')
def login_post():
    response = jsonify_message('Invalid e-mail or password!', 'danger')
    form = LoginForm(request.form)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.find_by_email(email)

        if (not user is None) and (check_password_hash(user.password, password)):
            login_user(user)
            next = request.args.get('next')

            if (next is None) or (not next.startswith('/')):
                next = url_for('home.index')

            response = jsonify_redirect(next)

    return response
'''


@auth.get('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out.', 'success')

    return redirect(url_for('home.index'))


@auth.get('/register')
def register():
    return render_template(auth, 'register', {'form': RegisterForm()})


@auth.post('/register')
def register_post():
    form = RegisterForm(request.form)
    response = jsonify_message('The entered data is invalid!', 'danger')

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        user = User.find_by_email_or_username(email, username)

        if not user is None:
            response = jsonify_message('The email or username is already taken.', 'warning')
        else:
            name = form.name.data
            password = generate_password_hash(form.password.data)
            user = User(name, email, username, password)
            User.save(user)

            flash('Your registration was successful. To continue, please log in.', 'success')
            response = jsonify_redirect(url_for('.login'))

    return response
