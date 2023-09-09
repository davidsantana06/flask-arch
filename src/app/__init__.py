from app.core.constants import Constants

from flask import (
    Flask,
    render_template
)
from mvc_flask import FlaskMVC
from typing import Any, Dict, Tuple
from werkzeug.exceptions import HTTPException


def configure_app(app: Flask) -> None:
    pass


def configure_context_processors(app: Flask) -> None:
    pass


def configure_error_handler(app: Flask) -> None:
    error_message: Dict[int, str] = {
        400: 'Requisição inválida.',
        401: 'Acesso não autorizado.',
        402: 'Pagamento necessário.',
        403: 'Acesso proibido.',
        404: 'Página não encontrada.',
        405: 'Método HTTP não permitido.',
        406: 'Não é possível satisfazer o cabeçalho Accept.',
        407: 'Autenticação de proxy necessária.',
        408: 'Tempo limite da solicitação esgotado.',
        409: 'Conflito na solicitação.',
        410: 'Recurso não disponível.',
        411: 'Comprimento necessário no cabeçalho Content-Length.',
        412: 'Falha na pré-condição.',
        413: 'Entidade muito grande.',
        414: 'URI da solicitação muito longa.',
        415: 'Tipo de mídia não suportado.',
        416: 'Intervalo solicitado não satisfatório.',
        417: 'Expectativa falhou.',
        418: 'Eu sou um bule de chá (teapot).',
        429: 'Limite de taxa excedido.',
        500: 'Erro interno do servidor.',
        501: 'Funcionalidade não implementada.',
        502: 'Bad Gateway.',
        503: 'Serviço indisponível.'
    }

    def error_handler(e: Exception):
        error_code: int = e.code if (isinstance(e, HTTPException)) else 500
        description: str = error_message.get(error_code, 'Ocorreu um erro inesperado.')
        data: dict[str, object] = {
            'error': {
                'code': error_code,
                'description': description
            }
        }

        return data

    app.register_error_handler(Exception, error_handler)


def configure_extensions(app: Flask) -> None:
    mvc: FlaskMVC = FlaskMVC()
    mvc.init_app(app)


def create_app() -> Flask:
    app: Flask = Flask(__name__)

    configure_error_handler(app)
    configure_extensions(app)

    return app
