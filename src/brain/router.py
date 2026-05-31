from src.brain.fast_brain import ask_fast
from src.brain.heavy_brain import ask_heavy


def ask_brain(prompt):

    prompt_lower = prompt.lower()

    heavy_phrases = [
        "summarize document",
        "summarize this document",
        "summarize pdf",
        "summarize report",
        "document summarization",
        "analyze document",
        "analyze this document",
        "analyze report",
        "analyze pdf",
        "document analysis",
        "project analysis",
        "analyze project",
        "analyze this project",
        "long-form reasoning",
        "long form reasoning",
        "reason through",
        "explain in detail"
    ]

    if any(
        phrase in prompt_lower
        for phrase in heavy_phrases
    ):
        return ask_heavy(prompt)

    return ask_fast(prompt)
