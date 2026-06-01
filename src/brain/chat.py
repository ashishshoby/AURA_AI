from src.brain.brain import ask_brain

CHAT_HISTORY = []


def chat(prompt):

    CHAT_HISTORY.append(
        f"User: {prompt}"
    )

    context = "\n".join(
        CHAT_HISTORY[-10:]
    )

    response = ask_brain(
        f"""
You are Aura AI.

Maintain conversation context.

{context}

Assistant:
"""
    )

    CHAT_HISTORY.append(
        f"Assistant: {response}"
    )

    return response


def clear_chat():

    CHAT_HISTORY.clear()