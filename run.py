from os import environ
from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host=environ.get('HOST'), port=int(environ.get('PORT')), debug=int(environ.get('DEBUG')))
