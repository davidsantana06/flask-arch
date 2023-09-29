from http import HTTPStatus
from werkzeug.exceptions import HTTPException

from app.misc import render_template

from . import error
from .constants import ERROR_MESSAGE, GENERIC_MESSAGE


@error.app_errorhandler(Exception)
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
