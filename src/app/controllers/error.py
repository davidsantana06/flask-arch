from app.services.error_service import ErrorService

from flask import (
    Blueprint,
    render_template
)
from typing import Tuple
from werkzeug.exceptions import HTTPException

error = Blueprint('error', __name__, url_prefix='')
error_service = ErrorService()


@error.app_errorhandler(Exception)
def handle_exception(e: Exception):
    e_code: int = 0

    if (isinstance(e, HTTPException)):
        e_code = e.code
    else:
        e_code = 500

    message: str = error_service.get_error_message(e_code)
    return (message, e_code)
