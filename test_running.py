from src.apps.running_apps import get_running_apps

apps = get_running_apps()

for app in apps[:100]:
    print(app)
    