# xhs_search.py

import requests
from bs4 import BeautifulSoup

def search_xiaohongshu(query: str, num_results: int = 20):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    search_url = f"https://www.bing.com/search?q=site%3Axiaohongshu.com+{query}"
    response = requests.get(search_url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for item in soup.select("li.b_algo")[:num_results]:
        title_tag = item.find("h2")
        desc_tag = item.find("p")
        link_tag = title_tag.find("a") if title_tag else None

        if title_tag and link_tag:
            results.append({
                "title": title_tag.text.strip(),
                "link": link_tag["href"],
                "snippet": desc_tag.text.strip() if desc_tag else ""
            })

    return results
