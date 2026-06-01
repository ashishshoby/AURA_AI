import os
import json
from datetime import datetime
from src.file_search.document_parser import extract_text

INDEX_FILE = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "file_index.json"
))

IGNORE_FOLDERS = {
    "$Recycle.Bin",
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
    "AppData",
    ".vscode",
    ".codex",
    "site-packages",
    "Packages",
    "Temp",
    "Cache"
    "OneDriveTemp",
    ".tmp",
}

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".pptx", ".txt", ".html", ".doc"}

def get_drives():

    return [
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Downloads")
    ]


def build_index():

    files = []

    total_files = 0

    for folder in get_drives():
        if not os.path.exists(folder):
            continue

        print(f"Scanning {folder}")

        for root, dirs, filenames in os.walk(folder):

            # Filtering directories
            dirs[:] = [
                d for d in dirs
                if d not in IGNORE_FOLDERS
                and not d.startswith('.')
            ]

            if "$Recycle.Bin" in root:
                continue

            if "AppData" in root:
                continue

            if ".vscode" in root:
                continue

            if ".codex" in root:
                continue

            if "site-packages" in root:
                continue

            try:
                for filename in filenames:
                    extension = os.path.splitext(filename)[1].lower()
                    if extension not in SUPPORTED_EXTENSIONS:
                        continue

                    full_path = os.path.join(root, filename)

                    try:
                        stat = os.stat(full_path)
                        text_content = extract_text(full_path)

                        files.append({
                            "name": filename,
                            "path": full_path,
                            "extension": extension,
                            "size": stat.st_size,
                            "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                            "content": text_content,
                            "keywords": [],  # Placeholder for future keyword extraction
                            "summary_cache": None  # Placeholder for summary cache
                        })

                        total_files += 1
                        if total_files % 100 == 0:
                            print(f"Indexed {total_files} files...")

                    except Exception as e:
                        print(f"Could not process file {full_path}: {e}")

            except Exception as e:
                print(f"Error walking directory {root}: {e}")

    os.makedirs(os.path.dirname(INDEX_FILE), exist_ok=True)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(files, f, indent=4)

    print(f"\nIndexed {total_files} files successfully")