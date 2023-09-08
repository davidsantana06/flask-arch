from os import path

class Constants():
    SRC_FOLDER_PATH: str = path.abspath(
        path.join(
            path.dirname(__file__),
            '..', '..'
        )
    )
    OUTPUT_FOLDER_PATH: str = path.join(SRC_FOLDER_PATH, 'output')
    UPLOADS_FOLDER_PATH: str = path.join(SRC_FOLDER_PATH, 'uploads')
