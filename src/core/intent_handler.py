# src/core/intent_handler.py

import subprocess
from datetime import datetime


def handle_command(command):

    command = command.lower()

    if "open notepad" in command:

        print("Opening Notepad...")

        subprocess.Popen("notepad.exe")

        return

    if "open calculator" in command:

        print("Opening Calculator...")

        subprocess.Popen("calc.exe")

        return

    if "what time is it" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        print(f"Current Time: {current_time}")

        return
    
    if "what is today's date" in command:

        today = datetime.now().strftime("%d %B %Y")

        print(f"Today's Date: {today}")

        return

    print("Command not recognized.")