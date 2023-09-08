from os import path


SRC_FOLDER_PATH: str = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', '..'
    )
)
APP_FOLDER_PATH: str = path.join(SRC_FOLDER_PATH, 'app')
OUTPUT_FOLDER_PATH: str = path.join(SRC_FOLDER_PATH, 'output')
UPLOADS_FOLDER_PATH: str = path.join(SRC_FOLDER_PATH, 'uploads')
