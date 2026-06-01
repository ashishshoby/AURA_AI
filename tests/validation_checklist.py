import os
import sys
from unittest.mock import patch, MagicMock

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.core import intent_handler
from src.file_search import search_memory


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


def _fake_search_files(query, max_results=50):
    if "pdf" in query:
        return [
            {
                "name": "sample.pdf",
                "path": r"C:\AURA\Validation\sample.pdf",
                "extension": ".pdf",
                "modified": "2026-05-31 00:00:00",
                "score": 100,
            }
        ]

    if "assuregate" in query:
        return [
            {
                "name": "AssureGate Documentation.pdf",
                "path": r"C:\AURA\Validation\AssureGate Documentation.pdf",
                "extension": ".pdf",
                "modified": "2026-05-31 00:00:00",
                "score": 100,
            }
        ]

    return []


def run_validation():
    spoken = []
    opened_paths = []
    ai_calls = []

    def fake_speak(text):
        spoken.append(str(text))

    def fake_open_app(app):
        return app in {"chrome", "telegram"}

    def fake_close_app(app):
        return app in {"chrome", "telegram"}

    def fake_ask_brain(prompt):
        ai_calls.append(prompt)
        return "AI response."

    def fake_startfile(path):
        opened_paths.append(path)

    def fake_exists(path):
        return path in {
            r"C:\AURA\Validation\sample.pdf",
            r"C:\AURA\Validation\AssureGate Documentation.pdf",
        }

    patches = [
        patch.object(intent_handler, "speak", fake_speak),
        patch.object(intent_handler, "open_app", fake_open_app),
        patch.object(intent_handler, "close_app", fake_close_app),
        patch.object(intent_handler, "search_files", _fake_search_files),
        patch.object(intent_handler, "ask_brain", fake_ask_brain),
        patch.object(intent_handler.os, "startfile", fake_startfile, create=True),
        patch.object(intent_handler.os.path, "exists", fake_exists),
    ]

    search_memory.LAST_RESULTS.clear()
    results = []

    with patches[0], patches[1], patches[2], patches[3], patches[4], patches[5], patches[6]:
        for command in COMMANDS:
            before_speech = len(spoken)
            before_ai = len(ai_calls)
            before_opened = len(opened_paths)

            passed = bool(intent_handler.handle_command(command))
            spoke = len(spoken) > before_speech

            # Commands should NOT call Ollama
            if command.startswith(("open ", "close ", "find ")):
                if command == "open result 1":
                    ai_ok = len(ai_calls) == before_ai
                    file_ok = len(opened_paths) > before_opened
                    results.append((command, passed and spoke and ai_ok and file_ok))
                else:
                    ai_ok = len(ai_calls) == before_ai
                    results.append((command, passed and spoke and ai_ok))

            # Simple commands (hello, time) should NOT call Ollama
            elif command in ("hello",) or "time" in command:
                ai_ok = len(ai_calls) == before_ai
                results.append((command, passed and spoke and ai_ok))

            # Questions SHOULD call Ollama
            else:
                ai_ok = len(ai_calls) > before_ai
                results.append((command, passed and spoke and ai_ok))

    return results


if __name__ == "__main__":
    print("=" * 50)
    print("AURA AI — Validation Suite")
    print("=" * 50)
    print()

    all_results = run_validation()
    pass_count = sum(1 for _, p in all_results if p)
    fail_count = len(all_results) - pass_count

    for command, passed in all_results:
        status = "PASS" if passed else "FAIL"
        icon = "[+]" if passed else "[-]"
        print(f"  {icon} {status}: {command}")

    print()
    print(f"Results: {pass_count}/{len(all_results)} passed")

    if fail_count:
        print(f"         {fail_count} FAILED")
    else:
        print("         All tests passed!")

    print("=" * 50)
