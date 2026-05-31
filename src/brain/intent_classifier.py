def classify_intent(command):

    command_lower = command.lower().strip()

    if command_lower.startswith("open "):
        return "OPEN_APP"

    if command_lower.startswith("launch "):
        return "OPEN_APP"

    if command_lower.startswith("start "):
        return "OPEN_APP"

    if command_lower.startswith("close "):
        return "CLOSE_APP"

    if command_lower.startswith("find "):
        return "SEARCH_FILE"

    if command_lower.startswith("search "):
        return "SEARCH_FILE"

    chat_keywords = [
        "what is",
        "who is",
        "who are",
        "explain",
        "tell me about",
        "define",
        "how does",
        "how do",
        "why is",
        "why does"
    ]

    if any(
        command_lower.startswith(keyword)
        for keyword in chat_keywords
    ):
        return "CHAT"

    if "time" in command_lower:
        return "TIME"

    if "date" in command_lower:
        return "DATE"

    return "CHAT"
