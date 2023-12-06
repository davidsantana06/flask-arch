from flask import (
    Flask,
    render_template
)
from werkzeug.exceptions import HTTPException


_ERROR_MESSAGE = {
    400: 'Invalid request.',
    401: 'Unauthorized access.',
    403: 'Forbidden acess.',
    404: 'Page not found.',
    405: 'HTTP method not allowed.',
    500: 'Internal server error.'
}
_GENERIC_MESSAGE = 'An unexpected error has occurred.'


def _error_handler(e: Exception):
    error_code = e.code if (isinstance(e, HTTPException)) else 500
    description = _ERROR_MESSAGE.get(error_code, _GENERIC_MESSAGE)

    return render_template('error-handler.jinja', **{'error': {'code': error_code, 'description': description}})


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, _error_handler)
