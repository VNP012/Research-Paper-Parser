import requests
import sys

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_papers(keyword, year_start=None, year_end=None, venue=None, limit=5):
    params = {
        "query": keyword,
        "limit": limit,
        "fields": "title,year,venue"
    }

    if year_start and year_end:
        params["year"] = f"{year_start}-{year_end}"
    if venue:
        params["venue"] = venue

    print("DEBUG: Query params ->", params)   # NEW: see exactly what we send

    response = requests.get(BASE_URL, params=params)
    print("DEBUG: Response code ->", response.status_code)   # NEW: see if API worked

    if response.status_code == 200:
        data = response.json()
        print("DEBUG: Total results found ->", data.get("total", 0))   # NEW: show result count
        for paper in data.get("data", []):
            print(f"{paper.get('title')} ({paper.get('year')}) – {paper.get('venue')}")
    else:
        print("ERROR:", response.status_code, response.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <keyword> [year_start] [year_end] [venue]")
        sys.exit(1)

    keyword = sys.argv[1]
    year_start = sys.argv[2] if len(sys.argv) > 2 else None
    year_end = sys.argv[3] if len(sys.argv) > 3 else None
    venue = sys.argv[4] if len(sys.argv) > 4 else None

    search_papers(keyword, year_start, year_end, venue)

