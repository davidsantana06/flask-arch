from flask import Blueprint

home = Blueprint('home', __name__, static_folder='static', static_url_path=f'/{__name__}', template_folder='templates')

from .events import *
from .views import *
