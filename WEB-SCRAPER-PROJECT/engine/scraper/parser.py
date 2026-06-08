from bs4 import BeautifulSoup
import re

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.text.strip() if soup.title else ""
    emails = re.findall(r"[\\w\\.-]+@[\\w\\.-]+", html)
    phones = re.findall(r"\\+?\\d[\\d\\s-]{8,}", html)
    links = [a.get("href") for a in soup.find_all("a") if a.get("href")]
    headers = [h.text.strip() for h in soup.find_all("h1")]
    images = [img.get("src") for img in soup.find_all("img") if img.get("src")]

    return {
        "titles": title,
        "emails": list(set(emails)),
        "phones": list(set(phones)),
        "links": links,
        "addresses": [],
        "headers": headers,
        "images": images
    }
