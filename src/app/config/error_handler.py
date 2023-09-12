from flask import Flask
from typing import Dict, Tuple
from werkzeug.exceptions import HTTPException
from app.core.utils import render_page


ERROR_MESSAGE: Dict[int, str] = {
    400: 'Invalid request.',
    401: 'Unauthorized access.',
    403: 'Forbidden acess.',
    404: 'Page not found.',
    405: 'HTTP method not allowed.',
    500: 'Internal server error.'
}
GENERIC_MESSAGE: str = 'An unexpected error has occurred.'


def error_handler(e: Exception) -> Tuple[str, int]:
    error_code: int = e.code if (isinstance(e, HTTPException)) else 500
    description: str = ERROR_MESSAGE.get(error_code, GENERIC_MESSAGE)
    data: dict[str, object] = {
        'error': {
            'code': error_code,
            'description': description
        }
    }

    return (render_page('error_handler', data), error_code)


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, error_handler)