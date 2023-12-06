from flask import jsonify
from werkzeug import Response


def jsonify_message(message: str, category: str = 'message') -> Response:
    '''
    Generates a JSON response for messages.

    :param message: The message to be sent.
    :type message: str

    :param category: The category of the message. Defaults to 'message'.
    :type category: str, optional

    :return: The JSON response.
    :rtype: Response
    '''
    return jsonify({'message': message, 'category': category})


def jsonify_redirect(url: str) -> Response:
    '''
    Generates a JSON response for redirection.

    :param url: The URL for redirection.
    :type url: str

    :return: The JSON response.
    :rtype: Response
    '''
    return jsonify({'redirect': url})
