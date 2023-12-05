from os import path, mkdir


def create_folder(folder: str) -> None:
    if not path.exists(folder):
        mkdir(folder)
