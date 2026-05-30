import os
import subprocess
import psutil

from src.apps.app_scanner import scan_apps
from src.apps.store_apps import open_store_app


OPEN_ALIASES = {
    "chrome": "google chrome",
    "vscode": "visual studio code",
    "code": "visual studio code",
    "telegram": "telegram web",
    "vlc": "vlc media player",
    "edge": "microsoft edge",
    "github": "github desktop",

}

PROCESS_ALIASES = {
    "chrome": "chrome.exe",
    "google chrome": "chrome.exe",

    "vscode": "code.exe",
    "code": "code.exe",
    "visual studio code": "code.exe",

    "telegram": "telegram.exe",
    "telegram web": "telegram.exe",
    "telegram desktop": "Telegram Desktop.exe",
    "telegram": "telegram Desktop.exe",    

    "vlc": "vlc.exe",
    "vlc media player": "vlc.exe",

    "edge": "msedge.exe",
    "microsoft edge": "msedge.exe",

    "powershell": "powershell.exe",
    "windows powershell": "powershell.exe",

    "cmd": "cmd.exe",
    "command prompt": "cmd.exe",

    "brave": "brave.exe",

    "notepad": "notepad.exe",

    "calculator": "CalculatorApp.exe"
,
    "microsoft store": "WinStore.App.exe",
    "store": "WinStore.App.exe",
}


def open_app(app_name):

    app_name = app_name.lower().strip()

    # Windows built-in apps

    if app_name == "notepad":
        subprocess.Popen("notepad.exe")
        return True

    if app_name == "calculator":
        subprocess.Popen("calc.exe")
        return True

    # Alias conversion

    if app_name in OPEN_ALIASES:
        app_name = OPEN_ALIASES[app_name]

    apps = scan_apps()

    # Exact match

    if app_name in apps:
        os.startfile(apps[app_name])
        return True

    # Partial match

    for app in apps:

        if app_name in app:

            print("Matched:", app)

            os.startfile(apps[app])

            return True

    # Microsoft Store apps

    if open_store_app(app_name):
        return True

    return False


def close_app(app_name):

    app_name = app_name.lower().strip()

    # Fast alias lookup

    if app_name in PROCESS_ALIASES:

        process_name = PROCESS_ALIASES[app_name]

        os.system(
            f'taskkill /f /im "{process_name}" >nul 2>&1'
        )

        return True

    # Fallback search

    for process in psutil.process_iter(['name']):

        try:

            name = process.info['name']

            if not name:
                continue

            if app_name in name.lower():

                process.kill()

                print("Closed:", name)

                return True

        except:
            pass

    return False