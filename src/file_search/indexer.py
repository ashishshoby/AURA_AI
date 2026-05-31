import os
import json
from datetime import datetime

INDEX_FILE = "data/file_index.json"

IGNORE_FOLDERS = {
    "$RECYCLE.BIN",
    "System Volume Information",
    "Windows",
    "Program Files",
    "Program Files (x86)",
    "ProgramData",
    "__pycache__",
    ".git",
    "venv",
    ".venv",
    "node_modules",
    "WinSxS",
    "AppData"
}


def get_drives():

    drives = []

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        drive = f"{letter}:\\"

        if os.path.exists(drive):

            drives.append(drive)

    return drives


def build_index():

    files = []

    total_files = 0

    for drive in get_drives():

        print(f"Scanning {drive}")

        for root, dirs, filenames in os.walk(drive):

            root_lower = root.lower()

            if (
                "$recycle.bin" in root_lower
                or "system volume information" in root_lower
                or "\\windows" in root_lower
                or "\\program files" in root_lower
                or "\\programdata" in root_lower
                or "\\appdata" in root_lower
                or "node_modules" in root_lower
                or "\\winsxs" in root_lower
                or "\\venv" in root_lower
                or "\\.venv" in root_lower
            ):
                continue

            dirs[:] = [
                d for d in dirs
                if d not in IGNORE_FOLDERS
            ]

            try:

                for filename in filenames:

                    full_path = os.path.join(
                        root,
                        filename
                    )

                    try:

                        stat = os.stat(full_path)

                        files.append({
                            "name": filename,
                            "path": full_path,
                            "extension": os.path.splitext(filename)[1].lower(),
                            "size": stat.st_size,
                            "modified": datetime.fromtimestamp(
                                stat.st_mtime
                            ).strftime("%Y-%m-%d %H:%M:%S")
                        })

                        total_files += 1

                    except:
                        pass

            except:
                pass

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(
        INDEX_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            files,
            f,
            indent=4
        )

    print(
        f"\nIndexed {total_files} files successfully"
    )