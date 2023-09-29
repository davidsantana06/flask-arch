from flask import Blueprint

auth = Blueprint(
    'auth', __name__, static_folder='static', static_url_path='/%s' % __name__, template_folder='templates'
)

from .views import *
