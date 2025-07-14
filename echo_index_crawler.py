import requests
from bs4 import BeautifulSoup

def crawl_forums(keywords=["start your business", "ai tools", "divine economy"]):
    urls = ["https://reddit.com/r/startups", "https://forums.hardwarezone.com.sg", "https://www.blackhatworld.com"]
    for url in urls:
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'html.parser')
            print(f"Crawled {url}")
            for word in keywords:
                if word.lower() in res.text.lower():
                    print(f"🔍 Found match for '{word}' in {url}")
        except Exception as e:
            print(f"Failed to crawl {url}: {e}")

# crawl_forums()
