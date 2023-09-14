from flask import Flask
from app.extensions import database, bcrypt, csrf


def configure_extensions(app: Flask) -> None:
    # database.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
