from app.extensions import mvc, database, bcrypt, csrf

from flask import Flask


def configure_extensions(app: Flask) -> None:
    mvc.init_app(app)
    # database.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
