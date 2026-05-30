import psutil

IGNORE = [
    "svchost.exe",
    "runtimebroker.exe",
    "searchhost.exe",
    "sihost.exe",
    "ctfmon.exe",
    "dwm.exe",
    "conhost.exe",
    "taskhostw.exe",
    "fontdrvhost.exe"
]


def get_running_apps():

    apps = []

    for process in psutil.process_iter(['name']):

        try:

            name = process.info['name']

            if not name:
                continue

            if name.lower() in IGNORE:
                continue

            apps.append(name)

        except:
            pass

    return sorted(set(apps))