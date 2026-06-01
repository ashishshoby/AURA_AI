LAST_RESULTS = []


def store_results(results):
    """Store search results for later retrieval via 'open result N'."""

    global LAST_RESULTS

    LAST_RESULTS.clear()

    LAST_RESULTS.extend(results)


def get_result(index):
    """Get a stored result by 1-based index. Returns dict or None."""

    if index < 1 or index > len(LAST_RESULTS):
        return None

    return LAST_RESULTS[index - 1]