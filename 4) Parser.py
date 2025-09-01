import requests
import sys
import csv
import os
import time

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

# Load API key from environment variable
API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
HEADERS = {"x-api-key": API_KEY} if API_KEY else {}

def search_papers(keyword, year_start=None, year_end=None, venue=None, limit=100, outfile="results.csv"):
    params = {
        "query": keyword,
        "limit": limit,  # up to 100 per request
        "fields": "title,year,venue"
    }

    if year_start and year_end:
        params["year"] = f"{year_start}-{year_end}"
    if venue:
        params["venue"] = venue

    response = requests.get(BASE_URL, params=params, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        papers = data.get("data", [])

        with open(outfile, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Year", "Venue"])
            for paper in papers:
                writer.writerow([paper.get("title"), paper.get("year"), paper.get("venue")])

        print(f"✅ Saved {len(papers)} papers for '{keyword}' to {outfile}")

    else:
        print("ERROR:", response.status_code, response.text)


if __name__ == "__main__":
    # --- Interactive prompt mode ---
    if len(sys.argv) == 1:
        keyword = input("Enter keyword: ").strip()
        year_start = input("Enter start year (or leave blank): ").strip() or None
        year_end = input("Enter end year (or leave blank): ").strip() or None
        venue = input("Enter venue (or leave blank): ").strip() or None

        outfile = f"results_{keyword.replace(' ', '_')}.csv"
        search_papers(keyword, year_start, year_end, venue, outfile=outfile)

    # --- Batch mode with keywords.txt ---
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".txt"):
        with open(sys.argv[1], "r") as f:
            keywords = [line.strip() for line in f if line.strip()]
        for kw in keywords:
            outfile = f"results_{kw.replace(' ', '_')}.csv"
            search_papers(kw, outfile=outfile)
            time.sleep(1)  # throttle to respect API rate limit

    # --- Command-line mode ---
    else:
        keyword = sys.argv[1]
        year_start = sys.argv[2] if len(sys.argv) > 2 else None
        year_end = sys.argv[3] if len(sys.argv) > 3 else None
        venue = sys.argv[4] if len(sys.argv) > 4 else None

        outfile = f"results_{keyword.replace(' ', '_')}.csv"
        search_papers(keyword, year_start, year_end, venue, outfile=outfile)
