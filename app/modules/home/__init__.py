from app.lib.core import Module

home = Module('home', __name__, static_url_path=f'/{__name__}')

from .events import *
from .views import *
