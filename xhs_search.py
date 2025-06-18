from playwright.sync_api import sync_playwright

def search_xiaohongshu(query: str, max_results: int = 10):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        search_url = f"https://www.xiaohongshu.com/search_result?keyword={query}"
        page.goto(search_url)
        page.wait_for_timeout(5000)  # 等待 5 秒加载页面内容

        items = page.query_selector_all("div.search-note-item")
        results = []

        for item in items[:max_results]:
            title = item.query_selector("span.title") or item.query_selector("div.desc")
            link_tag = item.query_selector("a")
            if title and link_tag:
                href = link_tag.get_attribute("href")
                results.append({
                    "title": title.inner_text().strip(),
                    "link": "https://www.xiaohongshu.com" + href,
                    "snippet": ""
                })

        browser.close()
        return results
