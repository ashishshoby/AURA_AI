import os


def scan_apps():

    apps = {}

    start_menu = [
        os.path.join(
            os.environ["PROGRAMDATA"],
            r"Microsoft\Windows\Start Menu\Programs"
        ),

        os.path.join(
            os.environ["APPDATA"],
            r"Microsoft\Windows\Start Menu\Programs"
        )
    ]

    for folder in start_menu:

        for root, dirs, files in os.walk(folder):

            for file in files:

                if file.endswith(".lnk"):

                    app_name = file.replace(".lnk", "").lower()

                    apps[app_name] = os.path.join(
                        root,
                        file
                    )

    return apps