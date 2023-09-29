from flask import Flask
from app.misc import dt_now, format_dt, template


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'template': template,
        'dt_now': dt_now,
        'format_dt': format_dt
    })
