from flask import Flask
from http import HTTPStatus
from werkzeug.exceptions import HTTPException

from app.misc import render_template


ERROR_MESSAGE = {
    400: 'Invalid request.',
    401: 'Unauthorized access.',
    403: 'Forbidden acess.',
    404: 'Page not found.',
    405: 'HTTP method not allowed.',
    500: 'Internal server error.'
}
GENERIC_MESSAGE = 'An unexpected error has occurred.'


def error_handler(e: Exception):
    error_code = e.code if (isinstance(e, HTTPException)) else 500
    description = ERROR_MESSAGE.get(error_code, GENERIC_MESSAGE)
    http_status = HTTPStatus(error_code)
    data = {
        'error': {
            'code': error_code,
            'description': description
        }
    }

    return (render_template('error-handler', data), http_status)


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, error_handler)
