from os import path


ROOT_FOLDER_PATH = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', '..'
    )
)
OUTPUT_FOLDER_PATH = path.join(ROOT_FOLDER_PATH, 'output')
UPLOADS_FOLDER_PATH = path.join(ROOT_FOLDER_PATH, 'uploads')
SRC_FOLDER_PATH = path.join(ROOT_FOLDER_PATH, 'src')
APP_FOLDER_PATH = path.join(SRC_FOLDER_PATH, 'app')
RESOURCES_FOLDER_PATH = path.join(SRC_FOLDER_PATH, 'resources')
