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
from src.system.volume_control import volume_up
from src.system.volume_control import volume_down
from src.system.volume_control import mute
from src.system.volume_control import unmute
from src.system.volume_control import set_volume
import re
from src.system.screenshot import take_screenshot
from src.system.process_manager import (
    get_top_cpu_processes,
    get_top_ram_processes,
    kill_process
)
from src.music.music_controller import (
    open_spotify,
    search_song,
    play_music,
    pause_music,
    next_song,
    previous_song
)
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

    if command in (
    "cpu usage",
    "cpu status",
    "processor usage"
):

        response = get_cpu_usage()

        speak(response)

        return True
    
    # --- RAM Usage ---

    if command in (
    "ram usage",
    "memory usage",
    "memory status"
):

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
    
    # --- Volume Controls ---

    if command in (
    "volume up",
    "increase volume",
    "increase sound",
    "sound up"
):

     speak(volume_up())

     return True


    if command in (
    "volume down",
    "decrease volume",
    "lower volume",
    "sound down"
):

        speak(volume_down())

        return True


    if command in (
    "mute",
    "mute volume",
    "mute audio"
):

     speak(mute())

     return True


    if command in (
    "unmute",
    "unmute volume",
    "unmute audio"
):

        speak(unmute())

        return True


    if "volume" in command:

        match = re.search(r"(\d+)", command)

        if match:

            percent = int(match.group(1))

            if 0 <= percent <= 100:

                speak(set_volume(percent))

                return True

        else:

            speak(
                "Please specify a volume level between 0 and 100."
            )

            return True
        
        # --- Screenshot ---

    if command in (
    "take screenshot",
    "capture screen",
    "screenshot"
   ):

        filepath = take_screenshot()
        speak(filepath)
        print("SCREENSHOT PATH:", filepath)

        return True
    
    # --- Process Manager ---

    if any(
    phrase in command
    for phrase in (
        "cpu hungry",
        "cpu hungry apps",
        "top processes",
        "cpu usage by apps"
    )
):

        processes = get_top_cpu_processes()

        print("\nTop CPU Processes:\n")

        for proc in processes:

            print(
                f"{proc['name']} "
                f"({proc['cpu']}%)"
            )

        speak(
            "Showing top CPU processes."
        )

        return True


    # --- RAM Manager ---

    if any(
    phrase in command
    for phrase in (
        "ram hungry",
        "ram hungry apps",
        "memory hungry",
        "memory hungry apps"
    )
):

        processes = get_top_ram_processes()

        print("\nTop RAM Processes:\n")

        for proc in processes:

            print(
                f"{proc['name']} "
                f"({proc['ram']}%)"
            )

        speak(
            "Showing top memory consuming applications."
        )

        return True


    # --- Kill Process ---

    if command.startswith("kill "):

        process_name = command.replace(
            "kill ",
            ""
        ).strip()

        success = kill_process(
            process_name
        )

        if success:

            speak(
                f"{process_name} terminated."
            )

        else:

            speak(
                "Process not found."
            )

        return True
    
    # --- Music Controls ---

    if command == "open spotify":

        speak(open_spotify())

        return True
    
    # --- Spotify Search ---

    if command.startswith("search spotify for "):

        song = command.replace(
        "search spotify for ",
        "",
        1
    ).strip()

        speak(
        search_song(song)
    )

        return True

    # --- Play Music ---

    if command in ("play music", "play song", "play", "play the song","play it"):

        speak(play_music())

        return True


    if command in ("pause music", "pause song", "pause", "pause the song","stop the song", "stop music","stop it"):

        speak(pause_music())

        return True


    if command in ("next song", "skip song","skip","next"):

        speak(next_song())

        return True


    if command in ("previous song", "last song","previous"):

        speak(previous_song())

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