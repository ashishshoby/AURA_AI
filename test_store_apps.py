# test_store_apps.py

import subprocess

result = subprocess.run(
    ["powershell", "Get-StartApps"],
    capture_output=True,
    text=True
)

print(result.stdout)