from flask import Blueprint, redirect, url_for

home = Blueprint('main', __name__, url_prefix='')


@home.get('/')
def index():
    return redirect(url_for('.test'))


@home.get('/test')
def test():
    return 'test', 200
