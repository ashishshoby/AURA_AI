import os
import json
from rapidfuzz import fuzz, process
from src.file_search.search_memory import store_results

INDEX_FILE = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "file_index.json"
))

_index_cache = None

def _load_index():
    global _index_cache
    if _index_cache is not None:
        return _index_cache
    if not os.path.exists(INDEX_FILE):
        print("Warning: file_index.json not found")
        return None
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        _index_cache = json.load(f)
    return _index_cache

def search_files(keyword, max_results=50):
    """
    Search the pre-built file index for matching files by filename and content.
    Returns a list of dicts: {"name", "path", "extension", "modified", "score"}
    """
    keyword = keyword.lower().strip()
    index = _load_index()

    if index is None:
        return _find_files_live(keyword)

    results = []
    for i, entry in enumerate(index):
        name_score = fuzz.WRatio(keyword, entry["name"].lower())
        
        content = entry.get("content")
        content_score = 0
        if content:
            # Simple substring check for performance; for more advanced search,
            # a different scoring mechanism would be needed.
            if keyword in content.lower():
                content_score = 80  # Base score for a content match
                # Optional: A more sophisticated scoring could be based on frequency or fuzz.ratio
                # This is a placeholder for simplicity.
                content_score += fuzz.partial_ratio(keyword, content.lower()) / 10
        
        # Combine scores, giving filename match a higher weight
        total_score = max(name_score, content_score)

        if total_score > 75:  # Relevance threshold
            results.append({
                "name": entry["name"],
                "path": entry["path"],
                "extension": entry.get("extension", ""),
                "modified": entry.get("modified", ""),
                "score": total_score
            })

    # Sort by relevance score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    
    store_results(results)

    return results[:max_results]

def find_files(keyword, max_results=50):
    """Alias for search_files — keeps existing imports working."""
    return search_files(keyword, max_results)

def _find_files_live(keyword, search_path="D:\\"):
    """Fallback live search when index is unavailable."""
    results = []
    for root, dirs, files in os.walk(search_path):
        try:
            for file in files:
                if keyword.lower() in file.lower():
                    full_path = os.path.join(root, file)
                    results.append({
                        "name": file,
                        "path": full_path,
                        "extension": os.path.splitext(file)[1].lower(),
                        "modified": "",
                        "score": 0
                    })
        except:
            pass
    return results

def search_by_topic(query, max_results=50):
    """
    Parses a topic query to search for documents.
    Handles queries like "find PDFs about cybersecurity".
    """
    query = query.lower().strip()
    keywords = query
    file_type_filter = None

    # Simple parsing for file types
    supported_types = ['pdf', 'docx', 'pptx', 'txt', 'html', 'doc']
    for file_type in supported_types:
        if f"{file_type}s" in query or file_type in query:
            file_type_filter = f".{file_type}"
            # Remove file type from keywords
            keywords = keywords.replace(f"{file_type}s", "").replace(file_type, "").strip()

    # Remove filler words
    filler_words = ["find", "documents", "related to", "about", "containing", "notes on", "files"]
    for word in filler_words:
        keywords = keywords.replace(word, "").strip()

    results = search_files(keywords, max_results=max_results * 2)  # Get more results to filter

    if file_type_filter:
        results = [r for r in results if r['extension'] == file_type_filter]

    return results[:max_results]