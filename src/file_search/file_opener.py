import os

from src.file_search.search_engine import search_files
from src.file_search.search_memory import get_result


def open_file(filename):
    """Opens the best match for a given filename."""

    results = search_files(filename, max_results=1)

    if not results:
        return False

    path = results[0]["path"]

    if not os.path.exists(path):
        return False

    os.startfile(path)

    return True


def open_result(index):
    """Open a file from the last search results by 1-based index."""

    result = get_result(index)

    if result is None:
        return False

    path = result["path"]

    if not os.path.exists(path):
        return False

    os.startfile(path)

    return True
