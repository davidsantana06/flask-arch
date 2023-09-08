class ErrorService:
    GENERIC_MESSAGE = 'Ocorreu um erro inesperado.'
    ERROR_MESSAGE = {
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

    def get_error_message(self, error_code: int) -> str:
        message: str = self.ERROR_MESSAGE.get(error_code, self.GENERIC_MESSAGE)
        return message
