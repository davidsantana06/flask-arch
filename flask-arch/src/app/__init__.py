from flask import Flask
from .config import configure_all


def create_app() -> Flask:
    app = Flask(__name__)
    configure_all(app)
    return app
