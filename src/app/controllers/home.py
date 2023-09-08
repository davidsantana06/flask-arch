from flask import Blueprint, render_template

home = Blueprint('main', __name__, url_prefix='')


@home.get('/')
def index():
    response = render_template('pages/home/index.html.j2'), 200
    return response
