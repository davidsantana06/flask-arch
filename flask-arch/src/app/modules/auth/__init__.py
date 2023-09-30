from flask import Blueprint

auth = Blueprint(
    'auth', __name__, static_folder='static', static_url_path=f'/{__name__}', template_folder='templates'
)

from .views import *
