from flask import Flask
from app.extensions import mvc, database, bcrypt, csrf


def configure_extensions(app: Flask) -> None:
    mvc.init_app(app)
    # database.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
