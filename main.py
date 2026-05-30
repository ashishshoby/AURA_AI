from src.voice.speech_to_text import listen


def main():

    print("AURA AI Started")

    while True:

        command = listen()

        if command:

            print(f"Detected: {command}")

            if command.lower() == "exit":

                print("Shutting down AURA")

                break


if __name__ == "__main__":

    main()