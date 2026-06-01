CHAT_HISTORY = []

def add_message(role, content):

    CHAT_HISTORY.append({
        "role": role,
        "content": content
    })

    if len(CHAT_HISTORY) > 10:
        CHAT_HISTORY.pop(0)

def get_history():
    return CHAT_HISTORY

def clear_history():
    CHAT_HISTORY.clear()