from datetime import timedelta
from flask import Blueprint, request, redirect
from flask_login import login_user, logout_user, current_user, login_required
from http import HTTPStatus

from app.misc import render_template
from app.models import User

from . import auth
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = {
        'form': LoginForm()
    }
    return (render_template('login', data), HTTPStatus.OK)
