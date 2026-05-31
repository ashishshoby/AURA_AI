import json

with open("data/file_index.json", "r", encoding="utf-8") as f:
    files = json.load(f)

count = 0

for file in files:

    if file.get("extension") == ".pdf":

        print(file["name"])

        count += 1

        if count == 20:
            break

print("\nTotal PDFs found:", count)