import os

from src.file_search.search_engine import search_files


def open_file(filename):

    results = search_files(filename)

    if not results:

        return False

    path = results[0]["path"]

    if not os.path.exists(path):
        return False

    os.startfile(
        path
    )

    return True
