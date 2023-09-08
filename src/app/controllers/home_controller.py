from flask import Blueprint, render_template

home_controller = Blueprint('main', __name__, url_prefix='')


@home_controller.get('/')
def index():
    response = render_template('pages/home/index.html.j2'), 200
    return response
