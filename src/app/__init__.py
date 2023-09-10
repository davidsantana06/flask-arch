from flask import Flask

from app.config import configure_all


def create_app() -> Flask:
    app: Flask = Flask(__name__)

    configure_all(app)

    return app
