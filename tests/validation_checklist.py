import os
import sys
from unittest.mock import patch

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.core import intent_handler
from src.file_search.search_memory import LAST_RESULTS


COMMANDS = [
    "hello",
    "what time is it",
    "open chrome",
    "close chrome",
    "open telegram",
    "close telegram",
    "find pdf",
    "find assuregate",
    "open result 1",
    "what is python",
    "what is data mining",
    "summarize assuregate documentation",
]


def _fake_search_files(query):
    if query == "pdf":
        return [
            {
                "name": "sample.pdf",
                "path": r"C:\AURA\Validation\sample.pdf",
                "extension": ".pdf",
                "modified": "2026-05-31 00:00:00",
            }
        ]

    if query == "assuregate":
        return [
            {
                "name": "AssureGate Documentation.pdf",
                "path": r"C:\AURA\Validation\AssureGate Documentation.pdf",
                "extension": ".pdf",
                "modified": "2026-05-31 00:00:00",
            }
        ]

    return []


def run_validation():
    spoken = []
    opened_paths = []
    ai_calls = []

    def fake_chat(command):
        ai_calls.append(("fast", command))
        return "AI response."

    def fake_ask_brain(command):
        ai_calls.append(("heavy", command))
        return "Summary response."

    def fake_startfile(path):
        opened_paths.append(path)

    def fake_exists(path):
        return path in {
            r"C:\AURA\Validation\sample.pdf",
            r"C:\AURA\Validation\AssureGate Documentation.pdf",
        }

    patches = [
        patch.object(intent_handler, "speak", lambda text: spoken.append(str(text))),
        patch.object(intent_handler, "open_app", lambda app: app in {"chrome", "telegram"}),
        patch.object(intent_handler, "close_app", lambda app: app in {"chrome", "telegram"}),
        patch.object(intent_handler, "search_files", _fake_search_files),
        patch.object(intent_handler, "chat", fake_chat),
        patch.object(intent_handler, "ask_brain", fake_ask_brain),
        patch.object(intent_handler.os, "startfile", fake_startfile, create=True),
        patch.object(intent_handler.os.path, "exists", fake_exists),
    ]

    LAST_RESULTS.clear()
    results = []

    with patches[0], patches[1], patches[2], patches[3], patches[4], patches[5], patches[6], patches[7]:
        for command in COMMANDS:
            before_speech = len(spoken)
            before_ai = len(ai_calls)
            passed = bool(intent_handler.handle_command(command))
            spoke = len(spoken) > before_speech

            if command.startswith(("open ", "close ", "find ")) and command != "open result 1":
                ai_ok = len(ai_calls) == before_ai
            elif command == "open result 1":
                ai_ok = len(ai_calls) == before_ai and opened_paths
            else:
                ai_ok = True

            results.append((command, passed and spoke and ai_ok))

    return results


if __name__ == "__main__":
    for command, passed in run_validation():
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {command}")
