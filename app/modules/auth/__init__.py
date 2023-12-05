from app.lib.core import Module

auth = Module('auth', __name__, static_url_path=f'/{__name__}')

from .views import *
