from flask import Flask

from app.extensions import database, bcrypt, csrf, login_manager, socket_io
from app.models import User


def load_user(user_id: str) -> User:
    return User.find_by_id(int(user_id))


def configure_extensions(app: Flask) -> None:
    # database.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.user_loader(load_user)

    socket_io.init_app(app, cors_allowed_origins='*')
