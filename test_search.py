from src.file_search.search_engine import search_files

results = search_files("network notes")

for file in results:

    print(file["path"])