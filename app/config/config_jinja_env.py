from flask import Flask

from app.lib.core import (
    css, img, js,
    layout, include, macro
)
from app.lib.utils import format_dt


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'inc': include,
        'layout': layout,
        'macro': macro,
        'css': css,
        'img': img,
        'js': js,
        'format_dt': format_dt
    })
