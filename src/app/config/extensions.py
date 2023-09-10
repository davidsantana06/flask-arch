from app.extensions import mvc

from flask import Flask


def configure_extensions(app: Flask) -> None:
    mvc.init_app(app)
