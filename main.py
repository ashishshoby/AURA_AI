import time

from src.voice.speech_to_text import listen
from src.core.intent_handler import handle_command
from src.apps.app_database import build_process_cache

def main():

    print("AURA AI Started")

    print("Building App Cache...")
    build_process_cache()

    while True:

        start = time.time()

        command = listen()

        if command:

            print(f"Detected: {command}")

            print(
                f"Recognition Time: "
                f"{round(time.time() - start, 2)} sec"
            )

            handle_command(command)


if __name__ == "__main__":

    main()