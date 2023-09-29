from os import path


ROOT_DIRECTORY = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', '..'
    )
)
OUTPUT_DIRECTORY = path.join(ROOT_DIRECTORY, 'output')
UPLOADS_DIRECTORY = path.join(ROOT_DIRECTORY, 'uploads')
SRC_DIRECTORY = path.join(ROOT_DIRECTORY, 'src')
APP_DIRECTORY = path.join(SRC_DIRECTORY, 'app')
MODULES_DIRECTORY = path.join(APP_DIRECTORY, 'modules')
