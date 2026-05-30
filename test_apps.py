from src.apps.app_scanner import scan_apps

apps = scan_apps()

print(f"Total Apps Found: {len(apps)}")

for app in sorted(apps.keys()):
    print(app)