import subprocess
from datetime import datetime
from src.voice.text_to_speech import speak
from src.apps.app_manager import open_app
from src.apps.app_manager import close_app
from src.apps.running_apps import get_running_apps
from src.file_search.search_engine import find_files



def handle_command(command):

    command = command.lower().strip()

    print("COMMAND:", command)

    if "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

        return

    elif "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        speak(f"Today is {today}")

        return

    elif "hello" in command:

        speak("Hello Ashish")

        return

    elif "who are you" in command:

        speak("I am Aura AI, your personal desktop assistant")

        return

    elif command == "exit":

        speak("Goodbye")

        exit()

    elif command.startswith("open "):

        app_name = command.replace(
            "open ",
            ""
        ).strip()

        speak(f"Opening {app_name}")

        success = open_app(app_name)

        if not success:

            speak("Application not found")

        return

    elif command.startswith("close "):

        app_name = command.replace(
            "close ",
            ""
        ).strip()

        success = close_app(app_name)

        if success:

            speak(f"Closing {app_name}")

        else:

            speak("Application not found")

        return

    elif "what apps are running" in command:

        apps = get_running_apps()

        print("\nRunning Apps:\n")

        for app in apps[:20]:

            print(app)

        speak(
            f"I found {len(apps)} running applications"
        )

        return
    
    elif command.startswith("find "):

        keyword = command.replace(
            "find ",
            ""
        ).strip()

        speak(f"Searching for {keyword}")

        results = find_files(keyword)

        for file in results[:20]:
            print(file)

        speak(f"I found {len(results)} matching files")

        return

    else:

        speak("Command not recognized")