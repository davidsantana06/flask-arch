from flask import Flask

from app.extensions import database, bcrypt, csrf, login_manager, socket_io
from app.models import User


def configure_database(app: Flask) -> None:
    database.init_app(app)
    
    with app.app_context():
        database.create_all()


def configure_login_manager(app: Flask) -> None:
    login_manager.init_app(app)
    login_manager.login_message = 'Please log in to access this page'
    login_manager.login_message_category = 'info'
    login_manager.login_view = 'auth.login'
    login_manager.user_loader(lambda user_id: User.find_by_id(int(user_id)))


def configure_extensions(app: Flask) -> None:
    bcrypt.init_app(app)
    csrf.init_app(app)
    socket_io.init_app(app, cors_allowed_origins='*')

    # configure_database(app)
    configure_login_manager(app)
