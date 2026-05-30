from src.voice.speech_to_text import listen
from src.core.intent_handler import handle_command


def main():

    print("AURA AI Started")

    while True:

        command = listen()

        if command:

            print(f"Detected: {command}")

            if command.lower() == "exit":

                print("Shutting down AURA")

                break

            handle_command(command)


if __name__ == "__main__":

    main()