import subprocess


def get_store_apps():

    apps = {}

    result = subprocess.run(
        ["powershell", "Get-StartApps"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()

    for line in lines[2:]:

        if not line.strip():
            continue

        try:

            parts = line.rsplit(None, 1)

            if len(parts) == 2:

                app_name = parts[0].strip().lower()

                app_id = parts[1].strip()

                apps[app_name] = app_id

        except:
            pass

    return apps

def open_store_app(app_name):

    apps = get_store_apps()

    app_name = app_name.lower()

    for app in apps:

        if app_name in app:

            app_id = apps[app]

            print("Opening:", app)

            import subprocess

            subprocess.Popen([
                "explorer.exe",
                f"shell:AppsFolder\\{app_id}"
            ])

            return True

    return False


if __name__ == "__main__":
    # simple test when run as a script
    print(get_store_apps())