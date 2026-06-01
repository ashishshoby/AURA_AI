import os
import re
from datetime import datetime

from click import command
from src.voice.text_to_speech import speak
from src.apps.app_manager import open_app
from src.apps.app_manager import close_app
from src.apps.running_apps import get_running_apps
from src.file_search.search_engine import search_files, search_by_topic
from src.file_search.search_memory import store_results
from src.file_search.search_memory import get_result
from src.brain.brain import ask_brain
from src.system.system_info import get_battery_status
from src.system.system_info import get_cpu_usage
from src.system.system_info import get_ram_usage
from src.system.system_info import get_disk_space
from src.system.system_info import get_wifi_status
CHAT_MODE = False

def handle_command(command):

    global CHAT_MODE

    command = command.lower().strip()

    print("COMMAND:", command)

    # --- Greetings ---

    if command in ("hello", "hi", "hey"):

        speak("Hello Ashish")

        return True

    # --- Identity ---

    if "who are you" in command:

        speak("I am Aura AI, your personal desktop assistant")

        return True

    # --- Exit ---

    if command == "exit":

        speak("Goodbye")

        exit()

    # --- Time ---

    if "time" in command and "what" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

        return True

    # --- Date ---

    if "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        speak(f"Today is {today}")

        return True

    # --- Chat Mode ---

    if command == "start chat mode":

        CHAT_MODE = True

        speak("Chat mode enabled")

        return True

    if command == "stop chat mode":

        CHAT_MODE = False

        from src.brain.chat import clear_chat

        clear_chat()

        speak("Chat mode disabled")

        return True
    # --- Open Application ---

    if command.startswith(("open ", "launch ", "start ")):

        # Check for "open result N" first
        result_match = re.match(
            r"open result (\d+)",
            command
        )

        if result_match:

            index = int(result_match.group(1))

            result = get_result(index)

            if result is None:

                speak("No search results available")

                return True

            path = result["path"]

            if os.path.exists(path):

                speak(f"Opening {result['name']}")

                os.startfile(path)

            else:

                speak("That file no longer exists")

            return True

        # Regular app open
        app_name = re.sub(
            r"^(open|launch|start)\s+",
            "",
            command
        ).strip()

        speak(f"Opening {app_name}")

        success = open_app(app_name)

        if not success:

            speak("Application not found")

        return True

    # --- Close Application ---

    if command.startswith("close "):

        app_name = command.replace(
            "close ",
            ""
        ).strip()

        success = close_app(app_name)

        if success:

            speak(f"Closing {app_name}")

        else:

            speak("Application not found")

        return True

    # --- Running Apps ---

    if "what apps are running" in command:

        apps = get_running_apps()

        print("\nRunning Apps:\n")

        for app in apps[:20]:

            print(app)

        speak(
            f"I found {len(apps)} running applications"
        )

        return True


    # --- Battery Status ---

    if "battery" in command:

        response = get_battery_status()

        speak(response)

        return True
    # --- CPU Usage ---

    if "cpu" in command:

        response = get_cpu_usage()

        speak(response)

        return True
    
    # --- RAM Usage ---

    if "ram" in command or "memory usage" in command:

        response = get_ram_usage()

        speak(response)

        return True
    
    # --- Disk Space ---

    if "disk space" in command:

        response = get_disk_space()

        speak(response)

        return True
    
    # --- WiFi Status ---

    if "wifi" in command or "internet" in command:

        response = get_wifi_status()

        speak(response)

        return True
# --- File Search ---

    if command.startswith(("find ", "search for ", "search ")):
        
        # Topic search
        if "documents" in command or "related to" in command or "about" in command or "containing" in command:
            results = search_by_topic(command)
            speak(f"Searching for documents related to {command.split('about')[-1].strip()}")
        
        # Simple file search
        else:
            keyword = re.sub(r"^(find|search for|search)\s+", "", command).strip()
            results = search_files(keyword)
            speak(f"Searching for {keyword}")

        store_results(results)

        if results:
            print(f"\nSearch Results ({len(results)} found):\n")
            for i, file in enumerate(results[:20], 1):
                print(f"  {i}. {file['name']}")
                print(f"     {file['path']}")
            speak(f"I found {len(results)} matching files")
        else:
            speak("No matching files found")

        return True
    # --- Continuous Chat Mode ---

    if CHAT_MODE:

        from src.brain.chat import chat

        response = chat(command)

        speak(response)

        return True

    # --- Ollama Brain (questions / unknown commands) ---

    from src.brain.chat import chat

    speak("Let me think about that")

    response = chat(command)

    speak(response)

    return True